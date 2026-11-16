---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, §3.1
---
# Wolfe Conditions
Back to [Index](../Index.md) · Nocedal & Wright §3.1

What counts as a good enough step along $p_k$. Write $\phi(\alpha) = f(x_k + \alpha p_k)$, so $\phi'(0) = \nabla f_k^{\top}p_k < 0$.

## Sufficient decrease (Armijo)
$$
\phi(\alpha) \le \phi(0) + c_1\,\alpha\,\phi'(0), \qquad c_1 \in (0, 1)
$$
The decrease must be at least a fraction $c_1$ of what the initial slope predicts. In practice $c_1 = 10^{-4}$. Alone it is not enough: every tiny step satisfies it.

## Curvature condition
$$
\phi'(\alpha) \ge c_2\,\phi'(0), \qquad c_2 \in (c_1, 1)
$$
The slope at the new point must have flattened. If it is still steeply negative, there is more decrease available further along, so the step was too short. Typical $c_2 = 0.9$ for Newton and quasi-Newton directions.

Together these are the **Wolfe conditions**. The **strong Wolfe conditions** replace the second by $\lvert\phi'(\alpha)\rvert \le c_2\,\lvert\phi'(0)\rvert$, which also rules out points where the slope is too positive.

## Existence
If $f$ is continuously differentiable and bounded below along the ray, there are intervals of step lengths satisfying the Wolfe and strong Wolfe conditions.

## Backtracking
Start from $\bar\alpha$ (use $1$ for Newton and quasi-Newton) and shrink until Armijo holds:
```
α ← ᾱ
while φ(α) > φ(0) + c₁ α φ′(0):
    α ← ρ α            # ρ in (0, 1)
```
The curvature condition is not needed, because the accepted step is within a factor $\rho$ of one that was rejected for being too long.

## Goldstein conditions
$$
\phi(0) + (1 - c)\,\alpha\,\phi'(0) \le \phi(\alpha) \le \phi(0) + c\,\alpha\,\phi'(0), \qquad 0 < c < \tfrac12
$$
A two-sided version of Armijo. It can exclude every minimizer of $\phi$.

See also: [Line Search Methods](Line%20Search%20Methods.md), [Step-Length Selection](Step-Length%20Selection.md), [Zoutendijk's Theorem](Zoutendijk's%20Theorem.md)
