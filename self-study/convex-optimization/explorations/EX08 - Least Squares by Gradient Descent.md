---
tags: [convex-optimization, exploration, ml-notebook]
source: ML notebook "Gradient Descent"; Book §1.2.1
topics: ["[[Least Squares by Gradient Descent]]", "[[Least-Squares and Linear Programming]]"]
---
# EX08 — Least Squares by Gradient Descent
Back to [[self-study/convex-optimization/Index|Index]]

> [!question] Problem
> Fit $\hat y = w_0 + w_1t$ to the points $(0,1), (1,2), (2,2), (3,4)$ by minimizing $L(w) = \tfrac1n\lVert Xw - y\rVert_2^2$.
> (a) Solve the normal equations.
> (b) Run gradient descent from $w = 0$ and confirm it converges to the same $w$.

## Setup
$$
X = \begin{bmatrix}1&0\\1&1\\1&2\\1&3\end{bmatrix},\quad y = \begin{bmatrix}1\\2\\2\\4\end{bmatrix},\quad X^{\top}X = \begin{bmatrix}4&6\\6&14\end{bmatrix},\quad X^{\top}y = \begin{bmatrix}9\\18\end{bmatrix}
$$

## Solution
**(a)**
$$
\begin{bmatrix}4&6\\6&14\end{bmatrix}w = \begin{bmatrix}9\\18\end{bmatrix} \ \Rightarrow\ \boxed{\,w^\star = (0.9,\ 0.9)\,}, \qquad L(w^\star) = 0.175
$$

**(b)** The Hessian $\tfrac2nX^{\top}X$ has eigenvalues $0.595$ and $8.405$, so take $t = 1/8.405$. The first step uses
$$
\nabla L(0) = \tfrac24 X^{\top}(0 - y) = (-4.5,\ -9).
$$
```python
import numpy as np

X = np.array([[1., 0.], [1., 1.], [1., 2.], [1., 3.]])
y = np.array([1., 2., 2., 4.])
n = len(y)

H = 2 / n * X.T @ X
t = 1 / np.linalg.eigvalsh(H).max()

w = np.zeros(2)
for k in range(200):
    grad = 2 / n * X.T @ (X @ w - y)   # (2/n) X^T (residual)
    w -= t * grad

print(w, np.mean((X @ w - y) ** 2))    # [0.9 0.9] 0.175
print(np.linalg.solve(X.T @ X, X.T @ y))  # [0.9 0.9]
```
| $k$ | $w^{(k)}$ |
|---|---|
| 0 | $(0,\ 0)$ |
| 1 | $(0.535,\ 1.071)$ |
| 2 | $(0.561,\ 1.059)$ |
| 200 | $(0.900,\ 0.900)$ |

The ratio $\kappa = 8.405/0.595 \approx 14$ is why it zig-zags slowly after the first step.

## Graph
```desmos-graph
left=-0.5; right=3.5; top=4.5; bottom=0
---
(0,1)|#000000
(1,2)|#000000
(2,2)|#000000
(3,4)|#000000
y=0.9+0.9x|#2d70b3
```

## Takeaways
- $L$ is convex ($\nabla^2L \succeq 0$), so GD cannot get stuck. It converges to the normal-equations answer.
- The speed depends on the condition number of $X^{\top}X$, a Chapter 9 theme.

## Related topics
- [[Least Squares by Gradient Descent]]
- [[Least-Squares and Linear Programming]]
- [[Gradient, Jacobian, and Hessian]]
