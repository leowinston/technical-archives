---
tags: [convex-optimization, topic, ch-3]
source: Boyd & Vandenberghe §3.4 (pp. 95–104)
---
# Quasiconvex Functions
Back to [Index](../Index.md) · Section 3.4

## Definition
$f$ is **quasiconvex** (unimodal) if $\dom f$ and every sublevel set
$$
S_\alpha = \{x \in \dom f \mid f(x) \le \alpha\}
$$
are convex. **Quasiconcave:** $-f$ is quasiconvex. **Quasilinear:** both.

> [!note] ✎ Margin sketches (pp. 95–96)
> You drew a curve with one dip and arrows under it, and traced the interval $[a, b]$ on Figure 3.9. On $\R$, quasiconvex means each sublevel set is **one interval**: the function falls, then rises. It can have flat parts and need not be convex.

## Modified Jensen inequality
$$
\boxed{\,f(\theta x + (1-\theta)y) \le \max\{f(x), f(y)\}\,}
$$

## Examples
- $\log x$ on $\R_{++}$ (quasilinear), $\lceil x\rceil$ (quasilinear).
- Length of a vector, $\max\{i \mid x_i \ne 0\}$, is quasiconvex on $\R^n_+$.
- $x_1x_2$ on $\R^2_+$ is quasiconcave but neither convex nor concave.

## Explorations
- [EX03 - Sublevel Sets of a Quasiconvex Function](../explorations/EX03%20-%20Sublevel%20Sets%20of%20a%20Quasiconvex%20Function.md)

See also: [Sublevel Sets and Epigraph](Sublevel%20Sets%20and%20Epigraph.md)
