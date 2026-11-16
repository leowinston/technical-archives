---
tags: [convex-optimization, topic, ch-3]
source: Boyd & Vandenberghe §3.1.6–3.1.7 (p. 75)
---
# Sublevel Sets and Epigraph
Back to [Index](../Index.md) · Sections 3.1.6–3.1.7

## Sublevel sets
$$
C_\alpha = \{x \in \dom f \mid f(x) \le \alpha\}
$$
$f$ convex $\Rightarrow$ every $C_\alpha$ is convex. **The converse is false**: $f(x) = -e^{x}$ is concave, yet every sublevel set is an interval.

> [!note] ✎ Margin sketch (p. 75)
> A valley-shaped curve with a double arrow under it: cutting the graph at height $\alpha$ leaves **one interval**, so the sublevel set is convex.

## Epigraph
$$
\epi f = \{(x, t) \mid x \in \dom f,\ f(x) \le t\} \subseteq \R^{n+1}
$$
$$
\boxed{\,f \text{ convex} \iff \epi f \text{ convex set}\,}
$$
This is the bridge between convex **sets** (Ch. 2) and convex **functions** (Ch. 3). Concave $\iff$ $\hypo f = \{(x, t) \mid t \le f(x)\}$ convex.

## Explorations
- [EX03 - Sublevel Sets of a Quasiconvex Function](../explorations/EX03%20-%20Sublevel%20Sets%20of%20a%20Quasiconvex%20Function.md)

See also: [Quasiconvex Functions](Quasiconvex%20Functions.md), [Convex Functions](Convex%20Functions.md)
