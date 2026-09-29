---
tags: [convex-optimization, exploration, ch-3]
source: Book §3.1.4–3.1.5 (pp. 71–74, ✎ "Second-order conditions" highlighted)
topics: ["[[Second-Order Conditions]]", "[[Examples of Convex Functions]]", "[[Positive Semidefinite Matrices]]"]
---
# EX02 — Checking Convexity with the Hessian
Back to [[self-study/convex-optimization/Index|Index]]

> [!question] Problem
> (a) Show $f(x, y) = x^2/y$ is convex on $y > 0$, and evaluate $\nabla^2 f(1, 2)$.
> (b) Show log-sum-exp $f(z) = \log\sum_k e^{z_k}$ is convex, and evaluate $\nabla^2 f$ at $z = (1, 2, 3)$.

## Strategy
Compute $\nabla^2 f$ and show $v^{\top}\nabla^2 f\,v \ge 0$ for all $v$. Then check numerically that the eigenvalues are $\ge 0$.

## Solution
**(a) Quadratic-over-linear.**
$$
\nabla^2 f(x, y) = \frac{2}{y^3}\begin{bmatrix} y^2 & -xy \\ -xy & x^2\end{bmatrix} = \frac{2}{y^3}\begin{bmatrix} y \\ -x\end{bmatrix}\begin{bmatrix} y \\ -x\end{bmatrix}^{\top} \succeq 0
$$
It is a positive multiple of an outer product $bb^{\top}$, so it is PSD with rank 1. At $(1, 2)$:
$$
\nabla^2 f(1,2) = \begin{bmatrix} 1 & -0.5 \\ -0.5 & 0.25\end{bmatrix}, \qquad \lambda = 0,\ 1.25.
$$

**(b) Log-sum-exp.** With $s = \operatorname{softmax}(z)$:
$$
\nabla^2 f = \operatorname{diag}(s) - ss^{\top}, \qquad v^{\top}\nabla^2 f\,v = \sum_k s_kv_k^2 - \Big(\sum_k s_kv_k\Big)^2 \ge 0
$$
by Cauchy–Schwarz (it is a variance under the weights $s$). At $z = (1,2,3)$: $s = (0.090, 0.245, 0.665)$ and $\lambda = 0,\ 0.119,\ 0.371$.

```python
import numpy as np

def hess_qol(x, y):
    return 2 / y**3 * np.array([[y*y, -x*y], [-x*y, x*x]])

z = np.array([1., 2., 3.])
s = np.exp(z) / np.exp(z).sum()
H_lse = np.diag(s) - np.outer(s, s)

print(np.linalg.eigvalsh(hess_qol(1., 2.)))  # [0.   1.25]
print(np.linalg.eigvalsh(H_lse))             # [0.     0.1186 0.3709]
```

## Result
- Both Hessians are PSD everywhere, so both functions are convex.
- Each has a zero eigenvalue. $x^2/y$ is flat along rays $(x, y) = t(x_0, y_0)$, and log-sum-exp is flat along $\ones$: $f(z + t\ones) = f(z) + t$.

## Related topics
- [[Second-Order Conditions]]
- [[Examples of Convex Functions]]
- [[Positive Semidefinite Matrices]]
