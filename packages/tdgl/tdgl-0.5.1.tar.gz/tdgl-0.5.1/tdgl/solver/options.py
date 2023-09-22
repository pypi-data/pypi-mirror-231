import os
from dataclasses import dataclass
from enum import Enum
from typing import Union


class SolverOptionsError(ValueError):
    pass


class SparseSolver(Enum):
    """Supported sparse linear solvers."""

    SUPERLU: str = "superlu"
    UMFPACK: str = "umfpack"
    PARDISO: str = "pardiso"


@dataclass
class SolverOptions:
    """Options for the TDGL solver.

    Args:
        solve_time: Total simulation time, after any thermalization.
        skip_time: Amount of 'thermalization' time to simulate before recording data.
        dt_init: Initial time step.
        dt_max: Maximum adaptive time step.
        adaptive: Whether to use an adpative time step. Setting ``dt_init = dt_max``
            is equivalent to setting ``adaptive = False``.
        adaptive_window: Number of most recent solve steps to consider when
            computing the time step adaptively.
        max_solve_retries: The maximum number of times to reduce the time step in a
            given solve iteration before giving up.
        adaptive_time_step_multiplier: The factor by which to multiple the time
            step ``dt`` for each adaptive solve retry.
        sparse_solver: One of "superlu", "umfpack", or "pardiso". "umfpack" requires
            suitesparse, which can be installed via conda, and scikit-umfpack, which
            can be installed via pip. "pardiso" requires an Intel CPU and the
            pypardiso package, which can be installed via pip or conda.
        terminal_psi: Fixed value for the order parameter in current terminals.
        field_units: The units for magnetic fields.
        current_units: The units for currents.
        output_file: Path to an HDF5 file in which to save the data.
            If the file name already exists, a unique name will be generated.
            If ``output_file`` is ``None``, the solver results will not be saved
            to disk.
        pause_on_interrupt: Pause the simulation in the event of a KeyboardInterrupt.
        save_every: Save interval in units of solve steps.
        progress_interval: Minimum number of solve steps between progress bar updates.
        include_screening: Whether to include screening in the simulation.
        max_iterations_per_step: The maximum number of screening iterations per solve
            step.
        screening_tolerance: Relative tolerance for the induced vector potential, used
            to evaluate convergence of the screening calculation within a single time
            step.
        screening_step_size: Step size :math:`\\alpha` for Polyak's method.
        screening_step_drag: Drag parameter :math:`\\beta` for Polyak's method.
        screening_use_numba: Use numba for the screening calculation.
        screening_use_jax: Use jax for the screenig calculation.
    """

    solve_time: float
    skip_time: float = 0.0
    dt_init: float = 1e-6
    dt_max: float = 1e-1
    adaptive: bool = True
    adaptive_window: int = 10
    max_solve_retries: int = 10
    adaptive_time_step_multiplier: float = 0.25
    sparse_solver: Union[SparseSolver, str] = SparseSolver.SUPERLU
    terminal_psi: Union[float, complex, None] = 0.0
    pause_on_interrupt: bool = True
    save_every: int = 100
    progress_interval: int = 0
    field_units: str = "mT"
    current_units: str = "uA"
    output_file: Union[os.PathLike, None] = None
    include_screening: bool = False
    max_iterations_per_step: int = 1000
    screening_tolerance: float = 1e-3
    screening_step_size: float = 1.0
    screening_step_drag: float = 0.5
    screening_use_numba: bool = True
    screening_use_jax: bool = False

    def validate(self) -> None:
        if self.dt_init > self.dt_max:
            raise SolverOptionsError("dt_init must be less than or equal to dt_max.")
        solver = self.sparse_solver
        if isinstance(solver, str):
            try:
                solver = SparseSolver[solver.upper()]
            except KeyError:
                valid_solvers = list(SparseSolver.__members__.keys())
                if solver not in valid_solvers:
                    raise ValueError(
                        f"sparse solver must be one of {valid_solvers!r}, got {solver}."
                    )
            self.sparse_solver = solver
        if self.terminal_psi is not None and not (0 <= abs(self.terminal_psi) <= 1):
            raise SolverOptionsError(
                "terminal_psi must be None or have absolute value in [0, 1]"
                f" (got {self.terminal_psi})."
            )
        if not (0 < self.adaptive_time_step_multiplier < 1):
            raise SolverOptionsError(
                "adaptive_time_step_multiplier must be in (0, 1)"
                f" (got {self.adaptive_time_step_multiplier})."
            )
        if not (0 < self.screening_step_drag <= 1):
            raise SolverOptionsError(
                "screening_step_drag must be in (0, 1)"
                f" (got {self.screening_step_drag})."
            )
        if self.screening_step_size <= 0:
            raise SolverOptionsError(
                "screening_step_size must be in > 0"
                f" (got {self.screening_step_size})."
            )
        if self.screening_tolerance <= 0:
            raise SolverOptionsError(
                "screening_tolerance must be in > 0"
                f" (got {self.screening_tolerance})."
            )
        if self.screening_use_jax and self.screening_use_numba:
            raise SolverOptionsError(
                "screening_use_jax and screening_use_numba cannot both be true."
            )
