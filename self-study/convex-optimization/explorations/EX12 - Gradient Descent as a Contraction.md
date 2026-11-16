---
tags: [convex-optimization, exploration, numerical-optimization]
source: Nocedal & Wright §3.3; Math 315 Lecture 7; my Banach proof
topics: ["[[Gradient Descent as a Fixed Point Iteration]]", "[[Convergence Rate of Steepest Descent]]"]
---
# EX12 — Gradient Descent as a Contraction
Back to [Index](../Index.md)

> [!question] Problem
> $f(x) = \tfrac12x^{\top}Qx$ with $Q = \operatorname{diag}(1, 10)$, so $m = 1$, $L = 10$, $\kappa = 10$, and $x^* = 0$.
> (a) For which fixed steps $\alpha$ is $g(x) = x - \alpha\nabla f(x)$ a contraction?
> (b) Find the best $\alpha$ and its contraction constant.
> (c) Run it from $x_0 = (10, 1)$ and compare with the prediction.

## Setup
$\nabla f(x) = Qx$, so $g(x) = (I - \alpha Q)x$ is linear, and
$$
g(x) - g(y) = \begin{bmatrix} 1 - \alpha & 0 \\ 0 & 1 - 10\alpha \end{bmatrix}(x - y)
$$

## Solution
**(a)** The contraction constant is the largest stretch factor, $q = \max\{\lvert 1 - \alpha\rvert,\ \lvert 1 - 10\alpha\rvert\}$.

| $\alpha$ | $\lvert 1 - \alpha\rvert$ | $\lvert 1 - 10\alpha\rvert$ | $q$ | |
|---|---|---|---|---|
| 0.10 | 0.90 | 0.00 | 0.90 | contraction |
| 0.1818 | 0.818 | 0.818 | 0.818 | contraction, best |
| 0.19 | 0.81 | 0.90 | 0.90 | contraction |
| 0.21 | 0.79 | 1.10 | 1.10 | **not** a contraction |

$q < 1$ exactly when $0 < \alpha < 2/L = 0.2$. Past that, the steep direction overshoots by more than it started with.

**(b)** The two factors balance when $1 - \alpha = -(1 - 10\alpha)$:
$$
\alpha = \frac{2}{m + L} = \frac{2}{11}, \qquad q = \frac{L - m}{L + m} = \frac{9}{11} = 0.8182
$$

**(c)**

```python
import numpy as np
Q = np.diag([1.0, 10.0]); x = np.array([10.0, 1.0]); a = 2/11
for k in range(5):
    x = x - a * (Q @ x)
```

| $k$ | $\lVert x_k\rVert_2$ | ratio |
|---|---|---|
| 0 | 10.0499 | |
| 1 | 8.2226 | 0.8182 |
| 2 | 6.7276 | 0.8182 |
| 3 | 5.5044 | 0.8182 |
| 4 | 4.5036 | 0.8182 |
| 5 | 3.6848 | 0.8182 |

Every step shrinks the error by exactly $9/11$. The first coordinate is multiplied by $+\tfrac{9}{11}$ and the second by $-\tfrac{9}{11}$: the flat direction creeps and the steep direction flips sign each step. That is the zigzag.

## Takeaways
- The step size limit $\alpha < 2/L$ is not a rule of thumb. It is the condition for $g$ to be a contraction, and [Banach's Fixed Point Theorem](../../../archive/proofs/Explorations/Banach's%20Fixed%20Point%20Theorem.md) does the rest.
- The best possible rate $\tfrac{\kappa - 1}{\kappa + 1}$ depends only on the condition number. At $\kappa = 10$ it takes $\ln(10^{-6})/\ln(9/11) \approx 69$ steps for six digits.
- This is the $n$-dimensional version of $\lvert g'(x^*)\rvert < 1$ from [Fixed Point Iteration](../../../academic/math-315/Topics%204/Fixed%20Point%20Iteration.md).

## Related topics
- [Gradient Descent as a Fixed Point Iteration](../numerical-optimization/Gradient%20Descent%20as%20a%20Fixed%20Point%20Iteration.md)
- [Convergence Rate of Steepest Descent](../numerical-optimization/Convergence%20Rate%20of%20Steepest%20Descent.md)
- [EX08 - Least Squares by Gradient Descent](EX08%20-%20Least%20Squares%20by%20Gradient%20Descent.md)
