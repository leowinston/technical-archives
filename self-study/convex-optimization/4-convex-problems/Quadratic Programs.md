---
tags: [convex-optimization, topic, ch-4]
source: Boyd & Vandenberghe §4.4 (pp. 152–160)
---
# Quadratic Programs
Back to [Index](../Index.md) · Section 4.4

## QP
$$
\begin{array}{ll}
\text{minimize} & \tfrac12 x^{\top}Px + q^{\top}x + r \\
\text{subject to} & Gx \preceq h,\ \ Ax = b
\end{array}
\qquad P \in \Spsd{n}
$$
A convex quadratic over a polyhedron. **QCQP:** the inequality constraints are convex quadratics too.

## Examples
- Least-squares with bounds $l \preceq x \preceq u$.
- **Distance between polyhedra:** minimize $\lVert x_1 - x_2\rVert_2^2$ with $x_1 \in \mathcal P_1$, $x_2 \in \mathcal P_2$.
- **Risk-sensitive LP:** random cost $c$ with mean $\bar c$, covariance $\Sigma$. Minimize $\bar c^{\top}x + \gamma\, x^{\top}\Sigma x$.
- **Markowitz portfolio** — see [Markowitz Portfolio Optimization](Markowitz%20Portfolio%20Optimization.md).

## SOCP
$$
\text{minimize } f^{\top}x \ \ \text{s.t.}\ \ \lVert A_ix + b_i\rVert_2 \le c_i^{\top}x + d_i
$$
Contains LPs ($A_i = 0$) and QCQPs. **Robust LP:** if $a_i$ lies in an ellipsoid $\{\bar a_i + P_iu \mid \lVert u\rVert_2 \le 1\}$, the worst-case constraint is $\bar a_i^{\top}x + \lVert P_i^{\top}x\rVert_2 \le b_i$.

See also: [Linear Programs](Linear%20Programs.md), [Markowitz Portfolio Optimization](Markowitz%20Portfolio%20Optimization.md)
