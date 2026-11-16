---
tags: [convex-optimization, topic, ch-2]
source: Boyd & Vandenberghe §2.4 (pp. 43–46)
---
# Generalized Inequalities and Minimal Elements
Back to [Index](../Index.md) · Section 2.4

## Proper cones
A cone $K$ is **proper** if it is convex, closed, solid (nonempty interior), and pointed (contains no line). It defines
$$
x \preceq_K y \iff y - x \in K, \qquad x \prec_K y \iff y - x \in \operatorname{int} K.
$$
$K = \R^n_+$ gives componentwise $\le$. $K = \Spsd{n}$ gives the matrix inequality $X \preceq Y$.

## Minimum vs minimal
Unlike $\le$ on $\R$, $\preceq_K$ is only a **partial** order: two points need not be comparable.

> [!important] ✎ Highlighted: Figure 2.17 "Left" / "Right"
> - **Minimum** $x_1$: every point is $\succeq x_1$, so $S \subseteq x_1 + K$.
> - **Minimal** $x_2$: no point is $\preceq x_2$ except itself, so $(x_2 - K) \cap S = \{x_2\}$.

A minimum is unique if it exists. There can be many minimal elements (a Pareto front).

## Explorations
- [EX01 - Minimum Versus Minimal Elements in R2](../explorations/EX01%20-%20Minimum%20Versus%20Minimal%20Elements%20in%20R2.md)

See also: [Dual Cones](Dual%20Cones.md)
