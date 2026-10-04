---
tags: [convex-optimization, topic, ch-1]
source: Boyd & Vandenberghe §1.3–1.5 (pp. 7–14)
---
# Convex Optimization Overview
Back to [Index](../Index.md) · Sections 1.3–1.5

## The problem
$$
\begin{array}{ll}
\text{minimize} & f_0(x) \\
\text{subject to} & f_i(x) \le b_i, \quad i = 1, \dots, m
\end{array}
$$
where every $f_0, \dots, f_m$ is ✎ **convex**:
$$
f_i(\alpha x + \beta y) \le \alpha f_i(x) + \beta f_i(y), \qquad \alpha + \beta = 1,\ \alpha, \beta \ge 0.
$$
Least-squares and LPs are ✎ **special cases**.

## Why it matters
- No analytic solution in general, but interior-point methods solve it reliably in roughly $\max\{n^3, n^2m, F\}$ work per step.
- The hard part is **recognizing** or **formulating** a problem as convex. After that, solving it is close to a technology.

## Book outline
- **Part I (Theory):** convex sets, convex functions, convex problems, and ✎ **Lagrangian duality**, which plays a ✎ **central role**.
- **Part II:** applications. **Part III:** algorithms.

See also: [Convex Functions](Convex%20Functions.md), [Convex Optimization Problems](Convex%20Optimization%20Problems.md)
