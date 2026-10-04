---
tags: [convex-optimization, topic, ch-3, ml-notebook]
source: Boyd & Vandenberghe §3.1.8 (p. 77); ML notebook "Jensen's Inequality"
---
# Jensen's Inequality
Back to [Index](../Index.md) · Section 3.1.8

## Statement
For convex $f$ and a random variable $X$ with $X \in \dom f$:
$$
\boxed{\,f(\E X) \le \E f(X)\,}
$$
The basic convexity inequality is the two-point case $\P(X = x) = \theta$, $\P(X = y) = 1 - \theta$.

## Dithering (ML notebook)
Add zero-mean noise $z$ to $x_0$:
$$
f(x_0) \le \E f(x_0 + z).
$$
- Convex $f$ (a cost): ✎ **dithering hurts** — noise can only raise the average cost.
- Affine $f$: the mean is the same whether or not you dither, e.g. $\tfrac12\big(f(x_0 + \Delta x) + f(x_0 - \Delta x)\big) = f(x_0)$.

## Consequences
- AM–GM: apply Jensen to $-\log$.
- Hölder's inequality follows from the concavity of $\log$.

## Explorations
- [EX04 - Jensen and Dithering](../explorations/EX04%20-%20Jensen%20and%20Dithering.md)

See also: [Convex Functions](Convex%20Functions.md), [Bias-Variance Tradeoff](Bias-Variance%20Tradeoff.md)
