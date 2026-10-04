---
tags: [convex-optimization, topic, ch-3]
source: Boyd & Vandenberghe §3.2 (pp. 79–90)
---
# Operations That Preserve Convexity of Functions
Back to [Index](../Index.md) · Section 3.2

> [!important] ✎ Highlighted section heading

| Operation | Rule |
|---|---|
| nonnegative weighted sum | $\sum w_i f_i$, $w_i \ge 0$ |
| affine composition | $f(Ax + b)$ |
| pointwise max / sup | $\max_i f_i(x)$, $\sup_{y} f(x, y)$ |
| scalar composition $h(g(x))$ | $h$ convex nondecreasing, $g$ convex |
| | $h$ convex nonincreasing, $g$ concave |
| minimization | $\inf_{y \in C} f(x, y)$, $f$ jointly convex, $C$ convex |
| perspective | $t\,f(x/t)$, $t > 0$ |

## Examples
- Piecewise-linear $\max_i (a_i^{\top}x + b_i)$ is convex.
- Largest eigenvalue $\lambda_{\max}(X) = \sup_{\lVert y\rVert_2 = 1} y^{\top}Xy$ is a sup of linear functions of $X$.
- $\operatorname{dist}(x, C) = \inf_{y \in C}\lVert x - y\rVert$ is convex when $C$ is.
- $e^{g(x)}$ is convex for convex $g$.

## Explorations
- [EX05 - Pointwise Max of Affine Functions](../explorations/EX05%20-%20Pointwise%20Max%20of%20Affine%20Functions.md)

See also: [Operations That Preserve Convexity of Sets](Operations%20That%20Preserve%20Convexity%20of%20Sets.md), [Examples of Convex Functions](Examples%20of%20Convex%20Functions.md)
