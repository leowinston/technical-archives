---
tags: [convex-optimization, topic, ch-4]
source: Boyd & Vandenberghe §4.3 (pp. 146–152)
---
# Linear Programs
Back to [[self-study/convex-optimization/Index|Index]] · Section 4.3

## Forms
$$
\begin{array}{ll}
\text{minimize} & c^{\top}x + d \\
\text{subject to} & Gx \preceq h,\ \ Ax = b
\end{array}
\qquad\qquad
\begin{array}{ll}
\text{minimize} & c^{\top}x \\
\text{subject to} & Ax = b,\ \ x \succeq 0
\end{array}
$$
(general form, standard form). The feasible set is a polyhedron, and an optimum is attained at a vertex if one exists.

## Examples
- **Diet problem:** cheapest mix of foods meeting nutrient minimums, $\min c^{\top}x$ s.t. $Ax \succeq b,\ x \succeq 0$.
- **Chebyshev center:** the largest ball $\{x_c + u \mid \lVert u\rVert_2 \le r\}$ in a polyhedron. Maximize $r$ s.t. $a_i^{\top}x_c + r\lVert a_i\rVert_2 \le b_i$.
- **Piecewise-linear minimization:** $\min \max_i(a_i^{\top}x + b_i)$ becomes minimize $t$ s.t. $a_i^{\top}x + b_i \le t$.

## Linear-fractional programs
Minimizing $(c^{\top}x + d)/(e^{\top}x + f)$ over a polyhedron is quasiconvex. The substitution $y = x/(e^{\top}x + f)$ turns it into an LP.

See also: [[Least-Squares and Linear Programming]], [[Quadratic Programs]]
