---
tags: [convex-optimization, exploration, ch-3]
source: Book §3.1.5 (p. 74, $\log\det X$ example); Boyd's lecture question on evaluating it without eigenvalues
topics: ["[[Examples of Convex Functions]]", "[[Convex Functions]]", "[[academic/math-315/Topics/Cholesky Factorization|Cholesky Factorization]]"]
---
# EX11 — Log Det via Cholesky
Back to [[self-study/convex-optimization/Index|Index]]

> [!question] Problem
> Let
> $$
> A = \begin{bmatrix} 4 & -1 & 1 \\ -1 & 4.25 & 2.75 \\ 1 & 2.75 & 3.5 \end{bmatrix}
> $$
> (a) Compute $\log\det A$ exactly without eigenvalues.
> (b) With $V = \operatorname{diag}(1, -1, 0)$, check that $g(t) = \log\det(A + tV)$ is concave on $t \in [-1, 1]$.

## Strategy
Reuse the factor $G$ from math-315 [[academic/math-315/Explorations/EX08 - Cholesky Factorization of a 3x3 SPD Matrix|EX08]]. Since $G$ is triangular, $\det G = \prod_k g_{kk}$, so $\det A = (\det G)^2$.

## Solution
**(a) From the Cholesky factor.**
$$
G = \begin{bmatrix} 2 & 0 & 0 \\ -0.5 & 2 & 0 \\ 0.5 & 1.5 & 1 \end{bmatrix}, \qquad
\log\det A = 2(\log 2 + \log 2 + \log 1) = 4\log 2 \approx 2.7726
$$
So $\det A = 16$. No eigenvalues are needed, and the arithmetic is exact up to the square roots in $G$.

**Why not cofactor expansion?** The Leibniz formula sums $n!$ signed products. Cholesky costs $\tfrac13 n^3$ flops. At $n = 20$ that is about $2.4 \times 10^{18}$ terms versus about $2700$ flops.

**(b) Concavity along a line.**

| $t$ | $-1$ | $-0.5$ | $0$ | $0.5$ | $1$ |
|---|---|---|---|---|---|
| $g(t)$ | 2.9007 | 2.8886 | 2.7726 | 2.5081 | 1.9188 |
| $\Delta g$ | | $-0.012$ | $-0.116$ | $-0.265$ | $-0.589$ |

The differences keep decreasing, which is what a concave $g$ does.

```python
import numpy as np

A = np.array([[4, -1, 1], [-1, 4.25, 2.75], [1, 2.75, 3.5]])
G = np.linalg.cholesky(A)
print(2 * np.log(np.diag(G)).sum())   # 2.7725887  (= 4 log 2)
print(np.linalg.slogdet(A))           # sign=1.0, logabsdet=2.7725887

V = np.diag([1., -1., 0.])
for t in np.linspace(-1, 1, 5):
    print(t, 2 * np.log(np.diag(np.linalg.cholesky(A + t * V))).sum())
```

## Result
- $\log\det A = 2\sum_k \log g_{kk} = 4\log 2$.
- $\log\det$ looks complicated because it is a degree-$n$ polynomial with $n!$ terms inside a log. Even so, it is concave on $\Spd{n}$, and one Cholesky factorization gives its exact value in $O(n^3)$ time.
- Eigenvalues also cost $O(n^3)$, but they need an iterative method with a larger constant. Cholesky is a finite direct method and doubles as the $X \succ 0$ test.

## Related topics
- [[Examples of Convex Functions]]
- [[Convex Functions]] (restriction to a line)
- [[academic/math-315/Topics/Cholesky Factorization|Cholesky Factorization]]
