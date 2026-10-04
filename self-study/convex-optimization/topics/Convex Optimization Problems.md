---
tags: [convex-optimization, topic, ch-4]
source: Boyd & Vandenberghe §4.2.1 (pp. 136–138)
---
# Convex Optimization Problems
Back to [Index](../Index.md) · Section 4.2.1

## Standard form
$$
\begin{array}{ll}
\text{minimize} & f_0(x) \\
\text{subject to} & f_i(x) \le 0, \quad i = 1, \dots, m \\
& a_i^{\top}x = b_i, \quad i = 1, \dots, p
\end{array}
$$
with $f_0, \dots, f_m$ **convex** and the equality constraints **affine**. The feasible set is convex: it is an intersection of convex sublevel sets and hyperplanes.

## Concave maximization
> [!important] ✎ Highlighted: "Concave maximization problems"
> Maximizing a ✎ **concave** $f_0$ over the same constraints is also called convex, since it is the same as minimizing the convex $-f_0$.

## Abstract vs standard form
Convexity is a property of the **description**, not only of the feasible set. With $f_1(x) = x_1/(1 + x_2^2) \le 0$ and $h_1(x) = (x_1 + x_2)^2 = 0$, the feasible set $\{x_1 \le 0,\ x_1 = -x_2\}$ is convex, but the problem is not in convex form. Rewriting $f_1$ as $x_1 \le 0$ and $h_1$ as $x_1 + x_2 = 0$ fixes it.

See also: [Local and Global Optima](Local%20and%20Global%20Optima.md), [Optimality Criterion for Differentiable Objectives](Optimality%20Criterion%20for%20Differentiable%20Objectives.md)
