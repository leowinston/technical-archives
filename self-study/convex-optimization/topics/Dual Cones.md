---
tags: [convex-optimization, topic, ch-2]
source: Boyd & Vandenberghe §2.6 (pp. 51–59)
---
# Dual Cones
Back to [[self-study/convex-optimization/Index|Index]] · Section 2.6

## Definition
$$
K^{*} = \{y \mid x^{\top}y \ge 0 \ \text{ for all } x \in K\}
$$
$K^{*}$ is always a convex cone, even when $K$ is not. $y \in K^{*}$ means $-y$ is the normal of a halfspace containing $K$.

## Self-dual cones
| $K$ | $K^{*}$ |
|---|---|
| $\R^n_+$ | $\R^n_+$ |
| $\Spsd{n}$ (with $\tr(XY)$) | $\Spsd{n}$ |
| $\{(x, t) \mid \lVert x\rVert_2 \le t\}$ | itself |
| $\{(x, t) \mid \lVert x\rVert \le t\}$ | $\{(u, v) \mid \lVert u\rVert_{*} \le v\}$ (dual norm) |

## Dual characterization of minimum
$x$ is the **minimum** of $S$ iff it is the unique minimizer of $\lambda^{\top}z$ over $S$ for **every** $\lambda \succ_{K^{*}} 0$. If $x$ minimizes $\lambda^{\top}z$ for **some** $\lambda \succ_{K^{*}} 0$, it is **minimal**.

See also: [[Generalized Inequalities and Minimal Elements]]
