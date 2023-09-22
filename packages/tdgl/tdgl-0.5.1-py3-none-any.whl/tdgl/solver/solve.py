import itertools
import logging
from datetime import datetime
from typing import Callable, Dict, Sequence, Tuple, Union

import numba
import numpy as np
import scipy.sparse as sp

try:
    import jax  # type: ignore
    import jax.numpy as jnp  # type: ignore
except (ModuleNotFoundError, ImportError):
    jax = None

from .. import distance
from ..device.device import Device, TerminalInfo
from ..finite_volume.operators import MeshOperators
from ..finite_volume.util import get_supercurrent
from ..parameter import Parameter
from ..solution.solution import Solution
from ..sources.constant import ConstantField
from .options import SolverOptions, SparseSolver
from .runner import DataHandler, Runner

logger = logging.getLogger(__name__)


@numba.njit(fastmath=True, parallel=True)
def get_A_induced_numba(
    J_site: np.ndarray,
    areas: np.ndarray,
    sites: np.ndarray,
    edge_centers: np.ndarray,
) -> np.ndarray:
    """Calculates the induced vector potential on the mesh edges.

    Args:
        J_site: The current density on the sites, shape ``(n, )``
        areas: The mesh site areas, shape ``(n, )``
        sites: The mesh site coordinates, shape ``(n, 2)``
        edge_centers: The coordinates of the edge centers, shape ``(m, 2)``

    Returns:
        The induced vector potential on the mesh edges.
    """
    assert J_site.ndim == 2
    assert J_site.shape[1] == 2
    assert sites.shape == J_site.shape
    assert edge_centers.ndim == 2
    assert edge_centers.shape[1] == 2
    out = np.empty((edge_centers.shape[0], sites.shape[1]), dtype=J_site.dtype)
    for i in numba.prange(edge_centers.shape[0]):
        for k in range(J_site.shape[1]):
            tmp = 0.0
            for j in range(J_site.shape[0]):
                dr = np.sqrt(
                    (edge_centers[i, 0] - sites[j, 0]) ** 2
                    + (edge_centers[i, 1] - sites[j, 1]) ** 2
                )
                tmp += J_site[j, k] * areas[j] / dr
            out[i, k] = tmp
    return out


def validate_terminal_currents(
    terminal_currents: Union[Callable, Dict[str, float]],
    terminal_info: Sequence[TerminalInfo],
    solver_options: SolverOptions,
    num_evals: int = 100,
) -> None:
    """Ensure that the terminal currents satisfy current conservation."""

    def check_total_current(currents: Dict[str, float]):
        names = set([t.name for t in terminal_info])
        if unknown := set(currents).difference(names):
            raise ValueError(
                f"Unknown terminal(s) in terminal currents: {list(unknown)}."
            )
        total_current = sum(currents.values())
        if total_current:
            raise ValueError(
                f"The sum of all terminal currents must be 0 (got {total_current:.2e})."
            )

    if callable(terminal_currents):
        times = np.random.default_rng().random(num_evals) * solver_options.solve_time
        for t in times:
            check_total_current(terminal_currents(t))
    else:
        check_total_current(terminal_currents)


def solve_for_psi_squared(
    *,
    psi: np.ndarray,
    abs_sq_psi: np.ndarray,
    mu: np.ndarray,
    epsilon: np.ndarray,
    gamma: float,
    u: float,
    dt: float,
    psi_laplacian: sp.spmatrix,
) -> Union[Tuple[np.ndarray, np.ndarray], None]:
    """Solve for :math:`\\psi_i^{n+1}` and :math:`|\\psi_i^{n+1}|^2` given
    :math:`\\psi_i^n` and :math:`\\mu_i^n`.

    Args:
        psi: The current value of the order parameter, :math:`\\psi_^n`
        abs_sq_psi: The current value of the superfluid density, :math:`|\\psi^n|^2`
        mu: The current value of the electric potential, :math:`\\mu^n`
        epsilon: The disorder parameter, :math:`\\epsilon`
        gamma: The inelastic scattering parameter, :math:`\\gamma`.
        u: The ratio of relaxation times for the order parameter, :math:`u`
        dt: The time step
        psi_laplacian: The covariant Laplacian for the order parameter

    Returns:
        ``None`` if the calculation failed to converge, otherwise the new order
        parameter :math:`\\psi^{n+1}` and superfluid density :math:`|\\psi^{n+1}|^2`.
    """
    U = np.exp(-1j * mu * dt)
    z = U * gamma**2 / 2 * psi
    with np.errstate(all="raise"):
        try:
            w = z * abs_sq_psi + U * (
                psi
                + (dt / u)
                * np.sqrt(1 + gamma**2 * abs_sq_psi)
                * ((epsilon - abs_sq_psi) * psi + psi_laplacian @ psi)
            )
            c = w.real * z.real + w.imag * z.imag
            two_c_1 = 2 * c + 1
            w2 = np.abs(w) ** 2
            discriminant = two_c_1**2 - 4 * np.abs(z) ** 2 * w2
        except Exception:
            logger.debug("Unable to solve for |psi|^2.", exc_info=True)
            return None
    if np.any(discriminant < 0):
        return None
    new_sq_psi = (2 * w2) / (two_c_1 + np.sqrt(discriminant))
    psi = w - z * new_sq_psi
    return psi, new_sq_psi


def adaptive_euler_step(
    step: int,
    psi: np.ndarray,
    abs_sq_psi: np.ndarray,
    mu: np.ndarray,
    epsilon: np.ndarray,
    gamma: float,
    u: float,
    dt: float,
    psi_laplacian: MeshOperators,
    options: SolverOptions,
) -> Tuple[np.ndarray, np.ndarray, float]:
    """Update the order parameter and time step in an adaptive Euler step.

    Args:
        step: The solve step index, :math:`n`
        psi: The current value of the order parameter, :math:`\\psi_^n`
        abs_sq_psi: The current value of the superfluid density, :math:`|\\psi^n|^2`
        mu: The current value of the electric potential, :math:`\\mu^n`
        epsilon: The disorder parameter, :math:`\\epsilon`
        gamma: The inelastic scattering parameter, :math:`\\gamma`.
        u: The ratio of relaxation times for the order parameter, :math:`u`
        dt: The tentative time step, which will be updated
        psi_laplacian: The covariant Laplacian for the order parameter
        options: The solver options for the simulation

    Returns:
        :math:`\\psi^{n+1}`, :math:`|\\psi^{n+1}|^2`, and :math:`\\Delta t^{n}`.
    """
    kwargs = dict(
        psi=psi,
        abs_sq_psi=abs_sq_psi,
        mu=mu,
        epsilon=epsilon,
        gamma=gamma,
        u=u,
        dt=dt,
        psi_laplacian=psi_laplacian,
    )
    result = solve_for_psi_squared(**kwargs)
    for retries in itertools.count():
        if result is not None:
            break  # First evaluation of |psi|^2 was successful.
        if (not options.adaptive) or retries > options.max_solve_retries:
            raise RuntimeError(
                f"Solver failed to converge in {options.max_solve_retries}"
                f" retries at step {step} with dt = {dt:.2e}."
                f" Try using a smaller dt_init."
            )
        kwargs["dt"] = dt = dt * options.adaptive_time_step_multiplier
        result = solve_for_psi_squared(**kwargs)
    psi, new_sq_psi = result
    return psi, new_sq_psi, dt


def solve(
    device: Device,
    options: SolverOptions,
    applied_vector_potential: Union[Callable, float] = 0,
    terminal_currents: Union[Callable, Dict[str, float], None] = None,
    disorder_epsilon: Union[float, Callable] = 1,
    seed_solution: Union[Solution, None] = None,
):
    """Solve a TDGL model.

    Args:
        device: The :class:`tdgl.Device` to solve.
        options: An instance :class:`tdgl.SolverOptions` specifying the solver
            parameters.
        applied_vector_potential: A function or :class:`tdgl.Parameter` that computes
            the applied vector potential as a function of position ``(x, y, z)``. If a float
            ``B`` is given, the applied vector potential will be that of a uniform magnetic
            field with strength ``B`` ``field_units``.
        terminal_currents: A dict of ``{terminal_name: current}`` or a callable with signature
            ``func(time: float) -> {terminal_name: current}``, where ``current`` is a float
            in units of ``current_units`` and ``time`` is the dimensionless time.
        disorder_epsilon: A float in range [-1, 1], or a callable with signature
            ``disorder_epsilon(r: Tuple[float, float]) -> epsilon``, where ``epsilon``
            is a float in range [-1, 1]. Setting
            :math:`\\epsilon(\\mathbf{r})=T_c(\\mathbf{r})/T_c - 1 < 1` suppresses the
            critical temperature at position :math:`\\mathbf{r}`, which can be used
            to model inhomogeneity.
        seed_solution: A :class:`tdgl.Solution` instance to use as the initial state
            for the simulation.

    Returns:
        A :class:`tdgl.Solution` instance.
    """

    start_time = datetime.now()
    options.validate()
    current_units = options.current_units
    field_units = options.field_units
    output_file = options.output_file

    ureg = device.ureg
    mesh = device.mesh
    sites = device.points
    edges = mesh.edge_mesh.edges
    edge_directions = mesh.edge_mesh.directions
    normalized_directions = edge_directions / mesh.edge_mesh.edge_lengths[:, np.newaxis]
    length_units = ureg(device.length_units)
    xi = device.coherence_length.magnitude
    u = device.layer.u
    gamma = device.layer.gamma
    K0 = device.K0
    A0 = device.A0
    probe_points = device.probe_point_indices
    # The vector potential is evaluated on the mesh edges,
    # where the edge coordinates are in dimensionful units.
    edge_centers = xi * mesh.edge_mesh.centers
    edge_xs, edge_ys = edge_centers.T
    Bc2 = device.Bc2
    z0 = device.layer.z0 * np.ones_like(edge_xs)
    J_scale = 4 * ((ureg(current_units) / length_units) / K0).to_base_units()
    assert "dimensionless" in str(J_scale.units), str(J_scale.units)
    J_scale = J_scale.magnitude
    time_dependent_vector_potential = (
        isinstance(applied_vector_potential, Parameter)
        and applied_vector_potential.time_dependent
    )
    if not callable(applied_vector_potential):
        applied_vector_potential = ConstantField(
            applied_vector_potential,
            field_units=field_units,
            length_units=device.length_units,
        )
    applied_vector_potential_ = applied_vector_potential
    # Evaluate the vector potential
    vector_potential_scale = (
        (ureg(field_units) * length_units / (Bc2 * xi * length_units))
        .to_base_units()
        .magnitude
    )
    A_kwargs = dict(t=0) if time_dependent_vector_potential else dict()
    vector_potential = applied_vector_potential_(edge_xs, edge_ys, z0, **A_kwargs)
    vector_potential = np.asarray(vector_potential)[:, :2]
    if vector_potential.shape != edge_xs.shape + (2,):
        raise ValueError(
            f"Unexpected shape for vector_potential: {vector_potential.shape}."
        )
    vector_potential *= vector_potential_scale

    dt_max = options.dt_max if options.adaptive else options.dt_init

    # Find the current terminal sites.
    terminal_info = device.terminal_info()
    for term_info in terminal_info:
        if term_info.length == 0:
            raise ValueError(
                f"Terminal {term_info.name!r} does not contain any points"
                " on the boundary of the mesh."
            )
    if terminal_info:
        normal_boundary_index = np.concatenate(
            [t.site_indices for t in terminal_info], dtype=np.int64
        )
    else:
        normal_boundary_index = np.array([], dtype=np.int64)
    # Define the source-drain current.
    if terminal_currents and device.probe_points is None:
        logger.warning(
            "The terminal currents are non-null, but the device has no probe points."
        )
    terminal_names = [term.name for term in terminal_info]
    if terminal_currents is None:
        terminal_currents = {name: 0 for name in terminal_names}
    if callable(terminal_currents):
        current_func = terminal_currents
    else:
        terminal_currents = {
            name: terminal_currents.get(name, 0) for name in terminal_names
        }

        def current_func(t):
            return terminal_currents

    validate_terminal_currents(current_func, terminal_info, options)

    # Construct finite-volume operators
    logger.info("Constructing finite volume operators.")
    terminal_psi = options.terminal_psi
    operators = MeshOperators(
        mesh,
        fixed_sites=normal_boundary_index,
        fix_psi=(terminal_psi is not None),
    )
    operators.build_operators(sparse_solver=options.sparse_solver)
    operators.set_link_exponents(vector_potential)
    divergence = operators.divergence
    mu_boundary_laplacian = operators.mu_boundary_laplacian
    mu_laplacian_lu = operators.mu_laplacian_lu
    mu_gradient = operators.mu_gradient
    use_pardiso = options.sparse_solver is SparseSolver.PARDISO
    if use_pardiso:
        assert mu_laplacian_lu is None
        import pypardiso  # type: ignore

        mu_laplacian = operators.mu_laplacian
    # Initialize the order parameter and electric potential
    psi_init = np.ones(len(mesh.sites), dtype=np.complex128)
    if terminal_psi is not None:
        psi_init[normal_boundary_index] = terminal_psi
    mu_init = np.zeros(len(mesh.sites))
    mu_boundary = np.zeros_like(mesh.edge_mesh.boundary_edge_indices, dtype=float)
    # Create the epsilon parameter, which sets the local critical temperature.
    if callable(disorder_epsilon):
        epsilon = np.array([float(disorder_epsilon(r)) for r in sites])
    else:
        epsilon = disorder_epsilon * np.ones(len(sites), dtype=float)
    if np.any(epsilon < -1) or np.any(epsilon > 1):
        raise ValueError("The disorder parameter epsilon must be in range [-1, 1].")

    if options.include_screening:
        A_scale = (ureg("mu_0") / (4 * np.pi) * K0 / A0).to(1 / length_units)
        areas = A_scale.magnitude * mesh.areas * xi**2
        if not options.screening_use_numba:
            # Pre-compute the kernel for the screening integral.
            inv_rho = A_scale / distance.cdist(
                edge_centers.astype(np.float32), sites.astype(np.float32)
            )
            areas = areas[:, np.newaxis].astype(np.float32)

            if options.screening_use_jax:
                if jax is None:
                    logger.warning(
                        "Ignoring options.screening_use_jax because jax is not available."
                    )
                else:
                    inv_rho = jax.device_put(inv_rho)

    # Running list of the max abs change in |psi|^2 between subsequent solve steps.
    # This list is used to calculate the adaptive time step.
    d_psi_sq_vals = []
    tentative_dt = options.dt_init
    # Parameters for the self-consistent screening calculation.
    step_size = options.screening_step_size
    drag = options.screening_step_drag

    # This is the function called at each step of the solver.
    def update(
        state,
        running_state,
        dt,
        *,
        psi,
        mu,
        supercurrent,
        normal_current,
        induced_vector_potential,
        applied_vector_potential=None,
    ):
        A_induced = induced_vector_potential
        A_applied = applied_vector_potential
        nonlocal tentative_dt, vector_potential
        step = state["step"]
        time = state["time"]
        old_sq_psi = np.abs(psi) ** 2
        # Compute the current density for this step
        # and update the current boundary conditions.
        currents = current_func(time)
        for term in terminal_info:
            current_density = (-1 / term.length) * sum(
                currents.get(name, 0) for name in terminal_names if name != term.name
            )
            mu_boundary[term.boundary_edge_indices] = J_scale * current_density

        dA_dt = 0.0
        if time_dependent_vector_potential:
            vector_potential = applied_vector_potential_(edge_xs, edge_ys, z0, t=time)
            vector_potential = vector_potential_scale * vector_potential[:, :2]
            dA_dt = np.einsum(
                "ij, ij -> i",
                (vector_potential - A_applied) / dt,
                normalized_directions,
            )
            if not options.include_screening:
                if np.any(np.abs(dA_dt) > 0):
                    operators.set_link_exponents(vector_potential)
        else:
            assert A_applied is None

        screening_error = np.inf
        A_induced_vals = []
        v = [0]  # Velocity for Polyak's method
        # This loop runs only once if options.include_screening is False
        for screening_iteration in itertools.count():
            if screening_error < options.screening_tolerance:
                break  # Screening calculation converged.
            if screening_iteration > options.max_iterations_per_step:
                raise RuntimeError(
                    f"Screening calculation failed to converge at step {step} after"
                    f" {options.max_iterations_per_step} iterations. Relative error in"
                    f" induced vector potential: {screening_error:.2e}"
                    f" (tolerance: {options.screening_tolerance:.2e})."
                )
            if options.include_screening:
                # Update the link variables in the covariant Laplacian and gradient
                # for psi based on the induced vector potential from the previous iteration.
                operators.set_link_exponents(vector_potential + A_induced)
                if time_dependent_vector_potential:
                    dA_dt = np.einsum(
                        "ij, ij -> i",
                        (vector_potential + A_induced - A_applied) / dt,
                        normalized_directions,
                    )

            # Adjust the time step and calculate the new the order parameter
            if screening_iteration == 0:
                # Find a new time step only for the first screening iteration.
                dt = tentative_dt
            psi, abs_sq_psi, dt = adaptive_euler_step(
                step,
                psi,
                old_sq_psi,
                mu,
                epsilon,
                gamma,
                u,
                dt,
                operators.psi_laplacian,
                options,
            )
            # Compute the supercurrent, scalar potential, and normal current
            supercurrent = get_supercurrent(psi, operators.psi_gradient, edges)
            rhs = (divergence @ (supercurrent - dA_dt)) - (
                mu_boundary_laplacian @ mu_boundary
            )
            if use_pardiso:
                mu = pypardiso.spsolve(mu_laplacian, rhs)
            else:
                mu = mu_laplacian_lu(rhs)
            normal_current = -((mu_gradient @ mu) + dA_dt)

            if not options.include_screening:
                break

            # Evaluate the induced vector potential.
            # This matrix multiplication takes the vast majority of the time
            # during a solve with screening.
            J_site = mesh.get_quantity_on_site(supercurrent + normal_current)
            if options.screening_use_numba:
                new_A_induced = get_A_induced_numba(J_site, areas, sites, edge_centers)
            elif options.screening_use_jax and jax is not None:
                new_A_induced = np.asarray(jnp.matmul(inv_rho, J_site * areas))
            else:
                new_A_induced = np.matmul(inv_rho, J_site * areas)
            # Update induced vector potential using Polyak's method
            dA = new_A_induced - A_induced
            v.append((1 - drag) * v[-1] + step_size * dA)
            A_induced = A_induced + v[-1]
            A_induced_vals.append(A_induced)
            if len(A_induced_vals) > 1:
                screening_error = np.max(
                    np.linalg.norm(dA, axis=1) / np.linalg.norm(A_induced, axis=1)
                )
                del v[:-2]
                del A_induced_vals[:-2]

        running_state.append("dt", dt)
        if probe_points is not None:
            # Update the voltage and phase difference
            running_state.append("mu", mu[probe_points])
            running_state.append("theta", np.angle(psi[probe_points]))
        if options.include_screening:
            running_state.append("screening_iterations", screening_iteration)

        if options.adaptive:
            # Compute the max abs change in |psi|^2, averaged over the adaptive window,
            # and use it to select a new time step.
            d_psi_sq_vals.append(np.abs(abs_sq_psi - old_sq_psi).max())
            window = options.adaptive_window
            if step > window:
                new_dt = options.dt_init / max(1e-10, np.mean(d_psi_sq_vals[-window:]))
                tentative_dt = np.clip(0.5 * (new_dt + dt), 0, dt_max)

        results = (
            dt,
            psi,
            mu,
            supercurrent,
            normal_current,
            A_induced,
        )
        if time_dependent_vector_potential:
            results = results + (vector_potential,)
        return results

    # Set the initial conditions.
    if seed_solution is None:
        num_edges = len(edges)
        parameters = {
            "psi": psi_init,
            "mu": mu_init,
            "supercurrent": np.zeros(num_edges),
            "normal_current": np.zeros(num_edges),
            "induced_vector_potential": np.zeros((num_edges, 2)),
        }
    else:
        if seed_solution.device != device:
            raise ValueError(
                "The seed_solution.device must be equal to the device being simulated."
            )
        seed_data = seed_solution.tdgl_data
        parameters = {
            "psi": seed_data.psi,
            "mu": seed_data.mu,
            "supercurrent": seed_data.supercurrent,
            "normal_current": seed_data.normal_current,
            "induced_vector_potential": seed_data.induced_vector_potential,
        }
    if time_dependent_vector_potential:
        parameters["applied_vector_potential"] = vector_potential
        fixed_values = (epsilon,)
        fixed_names = ("epsilon",)
    else:
        fixed_values = (vector_potential, epsilon)
        fixed_names = ("applied_vector_potential", "epsilon")
    running_names_and_sizes = {"dt": 1}
    if probe_points is not None:
        running_names_and_sizes["mu"] = len(probe_points)
        running_names_and_sizes["theta"] = len(probe_points)
    if options.include_screening:
        running_names_and_sizes["screening_iterations"] = 1

    with DataHandler(output_file=output_file, logger=logger) as data_handler:
        data_handler.save_mesh(mesh)
        result = Runner(
            function=update,
            options=options,
            data_handler=data_handler,
            initial_values=list(parameters.values()),
            names=list(parameters),
            fixed_values=fixed_values,
            fixed_names=fixed_names,
            running_names_and_sizes=running_names_and_sizes,
            logger=logger,
        ).run()
        end_time = datetime.now()
        logger.info(f"Simulation ended at {end_time}")
        logger.info(f"Simulation took {end_time - start_time}")

        if result:
            solution = Solution(
                device=device,
                path=data_handler.output_path,
                options=options,
                applied_vector_potential=applied_vector_potential_,
                terminal_currents=terminal_currents,
                disorder_epsilon=disorder_epsilon,
                total_seconds=(end_time - start_time).total_seconds(),
            )
            solution.to_hdf5()
            return solution
        return None
