---
tags: [convex-optimization, topic, ch-2]
source: Boyd & Vandenberghe §2.1 (pp. 21–27)
---
# Affine and Convex Sets
Back to [Index](../Index.md) · Section 2.1

## Affine sets
$C$ is **affine** if the whole line through any two points stays in $C$:
$$
x_1, x_2 \in C,\ \theta \in \R \ \Rightarrow\ \theta x_1 + (1-\theta)x_2 \in C.
$$
Example: the solution set $\{x \mid Ax = b\}$ of a linear system.

## Convex sets
$C$ is **convex** if the *segment* between any two points stays in $C$:
$$
\boxed{\,x_1, x_2 \in C,\ 0 \le \theta \le 1 \ \Rightarrow\ \theta x_1 + (1-\theta)x_2 \in C\,}
$$
A **convex combination** is $\sum \theta_i x_i$ with $\theta_i \ge 0$, $\sum\theta_i = 1$. The **convex hull** $\conv C$ is the set of all of them, the smallest convex set containing $C$.

## Cones
$C$ is a **convex cone** if $\theta_1 x_1 + \theta_2 x_2 \in C$ for all $\theta_1, \theta_2 \ge 0$ (conic combinations).

| Combination | Coefficients | Set |
|---|---|---|
| affine | $\sum\theta_i = 1$ | affine set |
| convex | $\sum\theta_i = 1$, $\theta_i \ge 0$ | convex set |
| conic | $\theta_i \ge 0$ | convex cone |

See also: [Important Convex Sets](Important%20Convex%20Sets.md), [Operations That Preserve Convexity of Sets](Operations%20That%20Preserve%20Convexity%20of%20Sets.md)
