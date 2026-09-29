---
tags: [convex-optimization, exploration, ch-4]
source: Constructed for Book §4.4.1 (p. 155, ✎ your most-annotated page)
topics: ["[[Markowitz Portfolio Optimization]]", "[[Quadratic Programs]]", "[[Optimality Criterion for Differentiable Objectives]]"]
---
# EX07 — Markowitz Three-Asset Portfolio
Back to [[self-study/convex-optimization/Index|Index]]

> [!question] Problem
> Three assets with mean returns and covariance
> $$\bar p = \begin{bmatrix}0.10\\0.07\\0.03\end{bmatrix},\qquad \Sigma = \begin{bmatrix}0.04 & 0.006 & 0\\ 0.006 & 0.01 & 0\\ 0 & 0 & 0.0001\end{bmatrix}.$$
> Solve minimize $x^{\top}\Sigma x$ s.t. $\bar p^{\top}x \ge r_{\min}$, $\ones^{\top}x = 1$, $x \succeq 0$ for $r_{\min} = 0.07$. Then trace the efficient frontier.

## Setup
- $x_i$ = fraction of the budget in asset $i$ (✎ "how much asset$_i$").
- Asset 1 is risky and high-return, asset 2 is moderate, asset 3 is nearly riskless.

## Strategy
1. Guess that the return constraint is **active** ($\bar p^{\top}x = r_{\min}$) and that $x \succ 0$, so no-shorting is inactive.
2. Then the problem is equality-constrained, and the optimality condition $\nabla f_0 + A^{\top}\nu = 0$ gives a linear **KKT system**:
$$
\begin{bmatrix} 2\Sigma & A^{\top} \\ A & 0\end{bmatrix}\begin{bmatrix} x \\ \nu\end{bmatrix} = \begin{bmatrix} 0 \\ b\end{bmatrix}, \qquad A = \begin{bmatrix}\bar p^{\top} \\ \ones^{\top}\end{bmatrix},\ b = \begin{bmatrix} r_{\min} \\ 1\end{bmatrix}
$$
3. Check the guess: is $x \succeq 0$?

## Solution
```python
import numpy as np

pbar = np.array([0.10, 0.07, 0.03])
S = np.array([[0.04, 0.006, 0.0],
              [0.006, 0.01, 0.0],
              [0.0, 0.0, 0.0001]])
A = np.vstack([pbar, np.ones(3)])
K = np.block([[2 * S, A.T], [A, np.zeros((2, 2))]])

def markowitz(rmin):
    sol = np.linalg.solve(K, np.r_[np.zeros(3), rmin, 1.0])
    x = sol[:3]
    return x, np.sqrt(x @ S @ x)

x, sd = markowitz(0.07)
print(x, sd)  # [0.2315 0.5949 0.1736] 0.0857
```
$$
\boxed{\,x^\star = (0.232,\ 0.595,\ 0.174),\qquad \sqrt{x^{\star\top}\Sigma x^\star} = 0.0857\,}
$$
All entries are positive, so the guess holds and this is the QP solution.

**Efficient frontier.** Repeat for other $r_{\min}$:

| $r_{\min}$ | $x^\star$ | std. dev. |
|---|---|---|
| 0.04 | $(0.057,\ 0.151,\ 0.793)$ | 0.0228 |
| 0.05 | $(0.115,\ 0.299,\ 0.586)$ | 0.0432 |
| 0.06 | $(0.173,\ 0.447,\ 0.380)$ | 0.0643 |
| 0.07 | $(0.232,\ 0.595,\ 0.174)$ | 0.0857 |
| 0.08 | $(1/3,\ 2/3,\ 0)$ ✱ | 0.1075 |

✱ At $0.08$ the KKT solve gives $x_3 = -0.033 < 0$, a short position. With **"long every stock"** ($x \succeq 0$) the constraint $x_3 \ge 0$ becomes active. Setting $x_3 = 0$ leaves two equations in two unknowns, $x_1 = 1/3$, $x_2 = 2/3$.

## Graph
The frontier in (std. dev., return) space. Asset 3 alone is the point at the bottom left.
```desmos-graph
left=0; right=0.13; top=0.09; bottom=0.025
---
(0.0228,0.04)|#2d70b3
(0.0432,0.05)|#2d70b3
(0.0643,0.06)|#2d70b3
(0.0857,0.07)|#c74440
(0.1075,0.08)|#2d70b3
(0.01,0.03)|open|#000000
```

## Takeaways
- Risk rises with the required return: that is the tradeoff the QP makes explicit.
- $\Sigma \succeq 0$ is exactly what makes the objective convex.
- Nonnegativity switches on only at high $r_{\min}$. That is complementary slackness in action.

## Related topics
- [[Markowitz Portfolio Optimization]]
- [[Quadratic Programs]]
- [[Optimality Criterion for Differentiable Objectives]]
