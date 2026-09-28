---
tags: [math-315, topic, lecture-3, appendix-b]
---
# Vector Norms
Back to [[Index]] · Appendix B.13.1

## Definition
$\|\cdot\|: \mathbb{R}^n \to \mathbb{R}$ is a norm if it satisfies:
1. $\|\mathbf{x}\| \ge 0$, and $\|\mathbf{x}\| = 0 \iff \mathbf{x} = \mathbf{0}$
2. $\|\alpha\mathbf{x}\| = |\alpha|\,\|\mathbf{x}\|$
3. $\|\mathbf{x} + \mathbf{y}\| \le \|\mathbf{x}\| + \|\mathbf{y}\|$

## $\ell_p$-norms
$$
\|\mathbf{x}\|_p = \left(\sum_{i=1}^{n} |x_i|^p\right)^{1/p}
$$
| $p$ | Formula |
|---|---|
| $1$ | $\sum_i \lvert x_i\rvert$ |
| $2$ | $\sqrt{\mathbf{x}^{\top}\mathbf{x}}$ |
| $\infty$ | $\max_i \lvert x_i\rvert$ |

## Relations
$$
\|\mathbf{x}\|_\infty \le \|\mathbf{x}\|_2 \le \|\mathbf{x}\|_1 \le n\,\|\mathbf{x}\|_\infty
$$

## Example
For $\mathbf{x} = (3, -4, 12)$: $\|\mathbf{x}\|_1 = 19$, $\|\mathbf{x}\|_2 = 13$, $\|\mathbf{x}\|_\infty = 12$.

## Explorations
- [[EX11 - l1 Norm of a 3x2 Matrix]]
- [[EX13 - Small Residual, Large Error]]

See also: [[Matrix Norms]]
