---
tags: [convex-optimization, topic, ml-notebook]
source: ML notebook "Bias-Variance tradeoff"
---
# Bias-Variance Tradeoff
Back to [[self-study/convex-optimization/Index|Index]] · ML notebook

## Setup (from the notebook)
A model $\hat f$ is trained on random data and evaluated at a fixed point $x_0$. The true relationship is
$$
y = f(x_0) + \epsilon, \qquad \E\epsilon = 0,\ \Var\epsilon = \sigma^2,
$$
with a linear model $\hat y = \beta_0 + \beta_1x_1 + \beta_2x_2 + \cdots$.

## Decomposition
$$
\boxed{\,\E\big[(y - \hat f(x_0))^2\big] = \underbrace{\big(f(x_0) - \E\hat f(x_0)\big)^2}_{\text{bias}^2} + \underbrace{\Var \hat f(x_0)}_{\text{variance}} + \sigma^2\,}
$$
- More flexible models lower the bias and raise the variance.
- $\sigma^2$ is irreducible.

## Convex optimization link
**Regularized least-squares** trades the two off with a convex objective:
$$
\text{minimize } \lVert X\beta - y\rVert_2^2 + \delta\lVert\beta\rVert_2^2
$$
Larger $\delta$ shrinks $\beta$: more bias, less variance. This is Chapter 6.3 (regularized approximation) of the book.

The same penalty appears in [[Regularized Spectral Clustering]]. There, $\tau\sum_i(x_i - \bar x)^2$ is added to the cut relaxation, and $\tau$ trades fitting fine structure against stability on sparse graphs.

See also: [[Jensen's Inequality]], [[Least Squares by Gradient Descent]]
