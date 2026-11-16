---
tags:
  - math-212
  - topic
  - chapter-6
---
# The Laplace Transform
Back to [Index](../Index.md) · Chapter 6.1 · Enrichment handout, Parts I–III

Weight $f$ by a decaying exponential and integrate. The input is a function of $t$; the output is a function of $s$:
$$
F(s) = \mathcal{L}\{f(t)\}(s) = \int_0^\infty e^{-st}f(t)\,dt
$$

## Why the weight
$\int_0^\infty 1\,dt$ diverges, but $\int_0^\infty e^{-st}\,dt = \dfrac1s$ for $s > 0$. The factor $e^{-st}$ decays fast enough to tame anything that grows slower than it does.

## When it exists
If $f$ is piecewise continuous and of **exponential order**, $|f(t)| \le Me^{ct}$, then $F(s)$ exists for $s > c$.

## First transforms
| $f(t)$ | $F(s)$ | valid for |
|---|---|---|
| $1$ | $\dfrac{1}{s}$ | $s > 0$ |
| $e^{at}$ | $\dfrac{1}{s-a}$ | $s > a$ |
| $t^n$ | $\dfrac{n!}{s^{n+1}}$ | $s > 0$ |
| $\sin bt$ | $\dfrac{b}{s^2+b^2}$ | $s > 0$ |
| $\cos bt$ | $\dfrac{s}{s^2+b^2}$ | $s > 0$ |

The $t^n$ row comes from integrating by parts $n$ times: each pass trades one power of $t$ for a factor $n/s$.

## Linearity
$$
\mathcal{L}\{af + bg\} = a\,\mathcal{L}\{f\} + b\,\mathcal{L}\{g\}
$$
**Example.** $\mathcal{L}\{3 + 2e^{2t}\} = \dfrac{3}{s} + \dfrac{2}{s-2}$ for $s > 2$, the smaller of the two domains.

See also: [Transforms of Derivatives](Transforms%20of%20Derivatives.md), [Inverse Transforms and Partial Fractions](Inverse%20Transforms%20and%20Partial%20Fractions.md)
