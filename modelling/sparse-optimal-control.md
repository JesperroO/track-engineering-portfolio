# Sparse optimal control — numerical implementation

[Modelling showcase](lap-time-modelling.md)

Alongside the vehicle project, I implement a **semismooth Newton / primal-dual active-set solver** for sparse PDE-constrained optimal control. This is concrete numerical-method experience in constructing constrained systems and diagnosing convergence.

## Implemented problem

The finite-element solver uses the Helmholtz state equation `−Δy + y = u`, homogeneous state/adjoint boundary conditions, L2 control weight `nu` and L1 threshold field `alpha(x)`. The implemented control law is:

`u = 0` for `|p| ≤ alpha(x)`; otherwise `u = (p − sign(p) alpha(x)) / nu`.

The active set is `|p| > alpha(x)`. I assemble the generalized derivative explicitly: the control/adjoint block contains **`−chi_active / nu`**, representing the transition between zero and nonzero control.

## My technical work

- Assemble the coupled **state, control and adjoint** residuals and block Jacobian with FEniCSx/UFL.
- Precompile forms and reuse PETSc matrix/vector allocations inside nonlinear iterations.
- Solve sparse block systems through MUMPS or an AMG-based preconditioned alternative.
- Record residual and active-set volume; investigate mesh refinement, reentrant boundaries and convergence failures separately.
- Keep UFL active-set logic and exported per-DOF field calculations consistent.

The implementation is in my [FEniCSx-SSN-Solver repository](https://github.com/JesperroO/FEniCSx-SSN-Solver): `ssn/solver.py`, `ssn/amr_engine.py` and `ssn/amg_preconditioner.py`. The motorcycle project also contains exploratory SSN/KKT formulations.
