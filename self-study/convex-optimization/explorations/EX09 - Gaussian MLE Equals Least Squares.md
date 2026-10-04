---
tags: [convex-optimization, exploration, ml-notebook]
source: ML notebook "Maximum Likelihood Estimation"
topics: ["[[Maximum Likelihood Estimation]]", "[[Least Squares by Gradient Descent]]", "[[Log-Concave and Log-Convex Functions]]"]
---
# EX09 — Gaussian MLE Equals Least Squares
Back to [Index](../Index.md)

> [!question] Problem
> Simulate $n = 50$ points from $y_i = 1 + 2x_i + \epsilon_i$ with $\epsilon_i \sim \Normal(0, 0.5^2)$. Maximize the log-likelihood numerically and compare with least squares.

## Strategy
1. Write the negative log-likelihood, which is convex in $w$:
$$
-\log L(w) = \frac n2\log(2\pi\sigma^2) + \frac{1}{2\sigma^2}\lVert y - Xw\rVert_2^2
$$
2. Minimize it by gradient descent, with $\nabla(-\log L) = -\tfrac{1}{\sigma^2}X^{\top}(y - Xw)$.
3. Compare with `lstsq`.

## Solution
```python
import numpy as np

rng = np.random.default_rng(0)
n, sigma = 50, 0.5
X = np.c_[np.ones(n), rng.uniform(0, 5, n)]
y = X @ np.array([1., 2.]) + sigma * rng.standard_normal(n)

w_ls = np.linalg.lstsq(X, y, rcond=None)[0]

w = np.zeros(2)
for _ in range(20000):
    w -= 1e-3 * (-(X.T @ (y - X @ w)) / sigma**2)

print(w_ls, w)  # [0.8787 2.0523] [0.8787 2.0523]
```
$$
\boxed{\,\hat w_{\text{MLE}} = \hat w_{\text{LS}} = (0.879,\ 2.052)\,}
$$
The negative log-likelihood is $36.12$ at $\hat w$, lower than $36.73$ at the true $w = (1, 2)$. The MLE fits *this* sample better than the truth does.

## Takeaways
- The $\log$ turns the product into a sum, and the Gaussian exponent turns the sum into squared error.
- The Gaussian is log-concave, so $-\log L$ is convex and the MLE is a convex problem. Laplacian noise would give $\ell_1$ regression, which is also convex.

## Related topics
- [Maximum Likelihood Estimation](../topics/Maximum%20Likelihood%20Estimation.md)
- [Log-Concave and Log-Convex Functions](../topics/Log-Concave%20and%20Log-Convex%20Functions.md)
