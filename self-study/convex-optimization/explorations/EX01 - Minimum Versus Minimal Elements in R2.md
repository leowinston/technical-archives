---
tags: [convex-optimization, exploration, ch-2]
source: Constructed, modelled on Figure 2.17 (p. 46, ✎ "Left"/"Right" highlighted)
topics: ["[[Generalized Inequalities and Minimal Elements]]"]
---
# EX01 — Minimum Versus Minimal Elements in $\R^2$
Back to [[self-study/convex-optimization/Index|Index]]

> [!question] Problem
> Use $K = \R^2_+$ (componentwise $\le$).
> (a) $S_1 = \{(1,1), (2,3), (3,2)\}$. Does $S_1$ have a minimum element?
> (b) $S_2 = \{(1,3), (2,1), (3,2), (4,4)\}$. Find the minimum, if any, and every minimal element.

## Strategy
1. $x$ is the **minimum** iff $S \subseteq x + K$: every point is up and to the right of $x$.
2. $x$ is **minimal** iff $(x - K) \cap S = \{x\}$: nothing else is down and to the left of $x$.

## Solution
**(a)** $(1,1) \preceq (2,3)$ and $(1,1) \preceq (3,2)$, so $S_1 \subseteq (1,1) + K$ and $\boxed{(1,1) \text{ is the minimum}}$.

**(b)** Compare the candidates:

| Point | Dominated by? | Minimal? |
|---|---|---|
| $(1,3)$ | none ($x = 1$ is the smallest) | yes |
| $(2,1)$ | none ($y = 1$ is the smallest) | yes |
| $(3,2)$ | $(2,1) \preceq (3,2)$ | no |
| $(4,4)$ | everything | no |

$(1,3)$ and $(2,1)$ are **incomparable**: $1 < 2$ but $3 > 1$. So $S_2$ has **no minimum**, and its minimal elements are $\boxed{(1,3),\ (2,1)}$.

## Graph
Red: $x_1 + K$ for (a) contains all of $S_1$. Blue: $x_2 - K$ at $(2,1)$ meets $S_2$ only at $(2,1)$.
```desmos-graph
left=-0.5; right=5; top=5; bottom=-0.5
---
y\ge1|x>1|#c74440
(1,1)|#c74440
(2,3)|#c74440
(3,2)|#c74440
y\le1|x<2|#2d70b3
(1,3)|#2d70b3
(2,1)|#2d70b3
(3,2)|#2d70b3
(4,4)|#2d70b3
```

## Takeaways
- A minimum beats **everything**. A minimal point is beaten by **nothing**.
- Minimal elements form a Pareto front. That is the vector-optimization picture from §4.7.

## Related topics
- [[Generalized Inequalities and Minimal Elements]]
- [[Dual Cones]]
