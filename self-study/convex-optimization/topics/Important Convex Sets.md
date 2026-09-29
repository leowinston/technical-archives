---
tags: [convex-optimization, topic, ch-2]
source: Boyd & Vandenberghe §2.2 (pp. 27–35)
---
# Important Convex Sets
Back to [[self-study/convex-optimization/Index|Index]] · Section 2.2

| Set | Definition |
|---|---|
| hyperplane | $\{x \mid a^{\top}x = b\}$, $a \ne 0$ |
| halfspace | $\{x \mid a^{\top}x \le b\}$ |
| Euclidean ball | $\{x \mid \lVert x - x_c\rVert_2 \le r\}$ |
| ellipsoid | $\{x \mid (x - x_c)^{\top}P^{-1}(x - x_c) \le 1\}$, $P \succ 0$ |
| norm cone | $\{(x, t) \mid \lVert x\rVert \le t\}$ |
| polyhedron | $\{x \mid Ax \preceq b,\ Cx = d\}$ |
| PSD cone | $\Spsd{n} = \{X \in \Sym{n} \mid X \succeq 0\}$ |

## Notes
- The ellipsoid's semi-axis lengths are $\sqrt{\lambda_i(P)}$.
- The norm cone with $\lVert\cdot\rVert_2$ is the **second-order cone** (the "ice cream cone").
- A **simplex** is the convex hull of $k+1$ affinely independent points. The probability simplex is $\{x \succeq 0,\ \ones^{\top}x = 1\}$.
- $\Spsd{n}$ is a convex cone: if $A, B \succeq 0$ and $\theta_1, \theta_2 \ge 0$ then $x^{\top}(\theta_1A + \theta_2B)x \ge 0$.

See also: [[Positive Semidefinite Matrices]], [[Affine and Convex Sets]]
