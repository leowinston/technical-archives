---
tags: [math-315, topic, lecture-3]
---
# Forward and Backward Error
Back to [Index](../Index.md) · Section 3.4 (recap from Chapter 2)

## Condition of a scalar problem
For $y = f(x)$ with a perturbed input $\hat x$:
$$
\kappa_{\text{abs}} = \frac{|f(\hat x) - f(x)|}{|\hat x - x|}, \qquad
\kappa_{\text{rel}} = \frac{|\Delta y / y|}{|\Delta x / x|}
$$
This is the forward error divided by the backward error.

## For $A\mathbf{x} = \mathbf{b}$
$$
\text{error: } \mathbf{e} = \mathbf{x} - \hat{\mathbf{x}}, \qquad \text{residual: } \mathbf{r} = \mathbf{b} - A\hat{\mathbf{x}}
$$
The error is unknown because $\mathbf{x}$ is unknown. The residual can always be computed.

## The catch
A small residual does **not** guarantee a small error. The two are linked by $\mathbf{e} = A^{-1}\mathbf{r}$, and the size of $A^{-1}$ is what the [Condition Number](Condition%20Number.md) measures.

## Example
$$
A = \begin{bmatrix} 0.913 & 0.659 \\ 0.457 & 0.330 \end{bmatrix}: \quad
\|\mathbf{r}_1\|_1 = 2.1 \times 10^{-4} \text{ but relative error } 1.29
$$

## Explorations
- [EX13 - Small Residual, Large Error](../Explorations/EX13%20-%20Small%20Residual%2C%20Large%20Error.md)

See also: [Condition Number](Condition%20Number.md), [Vector Norms](Vector%20Norms.md)
