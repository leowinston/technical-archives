---
tags: [convex-optimization, exploration, ch-3]
source: Constructed from ✎ margin sketches on pp. 75, 95–96
topics: ["[[Quasiconvex Functions]]", "[[Sublevel Sets and Epigraph]]"]
---
# EX03 — Sublevel Sets of a Quasiconvex Function
Back to [Index](../Index.md)

> [!question] Problem
> Let $f(x) = 1 - e^{-x^2}$ (the valley shape you sketched).
> (a) Find the sublevel set $S_{0.5}$.
> (b) Show $f$ is **not** convex using $x = 0.5$, $y = 2$.
> (c) Check the modified Jensen inequality for the same points.

## Strategy
1. Solve $f(x) \le \alpha$ for an interval.
2. Compare $f$ at the midpoint with the chord.
3. Compare $f$ at the midpoint with $\max\{f(x), f(y)\}$.

## Solution
**(a)**
$$
1 - e^{-x^2} \le 0.5 \iff x^2 \le \ln 2 \iff x \in [-0.8326,\ 0.8326]
$$
In general $S_\alpha = [-\sqrt{-\ln(1-\alpha)},\ \sqrt{-\ln(1-\alpha)}]$ for $0 \le \alpha < 1$, and $S_\alpha = \R$ for $\alpha \ge 1$. Every sublevel set is an interval, so $f$ is **quasiconvex**.

**(b)** $f(0.5) = 0.2212$, $f(2) = 0.9817$, and the midpoint $1.25$ gives
$$
f(1.25) = 0.7904 \ >\ \tfrac12(0.2212 + 0.9817) = 0.6015.
$$
The chord lies **below** the graph, so $f$ is not convex. (Here $f'' < 0$ for $\lvert x\rvert > 1/\sqrt2$.)

**(c)** $f(1.25) = 0.7904 \le \max\{0.2212,\ 0.9817\} \ \checkmark$

## Graph
Blue: $f$. Dashed: the level $\alpha = 0.5$. Green: $S_{0.5}$ on the axis. Red: the chord from (b).
```desmos-graph
left=-3; right=3; top=1.3; bottom=-0.3
---
y=1-e^{-x^{2}}|#2d70b3
y=0.5|dashed|#000000
y=0|x>-0.8326|x<0.8326|#388c46
y=0.2212+0.5071(x-0.5)|x>0.5|x<2|#c74440
(1.25,0.7904)|#c74440
(1.25,0.6015)|open|#c74440
```

## Takeaways
- Quasiconvex = "one dip": each horizontal cut leaves one interval, exactly your double-arrow sketch.
- Flat tails break convexity but not quasiconvexity.

## Related topics
- [Quasiconvex Functions](../topics/Quasiconvex%20Functions.md)
- [Sublevel Sets and Epigraph](../topics/Sublevel%20Sets%20and%20Epigraph.md)
