---
tags: [math-315, exploration, lecture-3]
source: Constructed example for Section 3.1.2 (Lower Triangular Systems)
topics: ["[[Triangular Systems]]", "[[LU Decomposition]]"]
---
# EX02 — Forward Substitution on a 3×3 System
Back to [[academic/math-315/Index|Index]]

> [!question] Problem
> (a) Solve $L\mathbf{x} = \mathbf{y}$ by forward substitution:
> $$
> \begin{bmatrix} 2 & 0 & 0 \\ 1 & 3 & 0 \\ -1 & 2 & 4 \end{bmatrix}
> \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} =
> \begin{bmatrix} 4 \\ 11 \\ 8 \end{bmatrix}
> $$
> (b) How does the operation count change when $L$ is **unit** lower triangular, as in $A = LU$?

## Setup
- **Matrix type:** lower triangular, $n = 3$, $\det L = 2 \cdot 3 \cdot 4 = 24 \neq 0$
- **Method:** forward substitution, $x_i = \dfrac{1}{l_{ii}}\Big(y_i - \sum_{j<i} l_{ij}x_j\Big)$

## Strategy
1. The first row involves only $x_1$. Solve it.
2. Move down. Everything to the left is already known.
3. For (b), note which divisions disappear when $l_{ii} = 1$.

## Solution
**(a)**

**Row 1.** No inner loop:
$$
x_1 = \frac{4}{2} = 2
$$

**Row 2.** $j = 1$:
$$
x_2 = \frac{11 - (1)(2)}{3} = \frac{9}{3} = 3
$$

**Row 3.** $j = 1, 2$:
$$
\begin{align*}
x_3 &= 8 - (-1)(2) = 10 \\
x_3 &= 10 - (2)(3) = 4 \\
x_3 &= \frac{4}{4} = 1
\end{align*}
$$
$$
\boxed{\,\mathbf{x} = \begin{bmatrix} 2 \\ 3 \\ 1 \end{bmatrix}\,}
$$

**Operation count.** Row $i$ costs $2(i-1)$ flops for the sum and 1 for the division:
$$
\underbrace{(0 + 1)}_{i=1} + \underbrace{(2 + 1)}_{i=2} + \underbrace{(4 + 1)}_{i=3} = 9 = n^2
$$
In general:
$$
\sum_{i=1}^{n} 2(i-1) + n = (n-1)n + n = n^2
$$

**(b) Unit lower triangular.** In $A = LU$, $L$ has $l_{ii} = 1$, so the division step `x[i] = x[i] / l[i][i]` is skipped:
$$
\text{flops} = \sum_{i=1}^{n} 2(i-1) = n^2 - n
$$
For $n = 3$ this is $6$. Here is an example with the unit $L$ from [[EX03 - Gaussian Elimination and LU of a 3x3 Matrix]]:
$$
\begin{bmatrix} 1 & 0 & 0 \\ 2 & 1 & 0 \\ 4 & 3 & 1 \end{bmatrix}\mathbf{y} = \begin{bmatrix} 4 \\ 10 \\ 24 \end{bmatrix}
\implies
\begin{aligned}
y_1 &= 4 \\
y_2 &= 10 - 2(4) = 2 \\
y_3 &= 24 - 4(4) - 3(2) = 2
\end{aligned}
$$
That is exactly 6 flops: $1 + 1$ for $y_2$ and $2 + 2$ for $y_3$.

```
# forward substitution with unit L (no divisions)
for i from 1 to n:
    y[i] = b[i] - sum(l[i][j] * y[j] for j from 1 to i-1)
```

## Check
$$
L\mathbf{x} = \begin{bmatrix} 2(2) \\ 1(2) + 3(3) \\ -1(2) + 2(3) + 4(1) \end{bmatrix} = \begin{bmatrix} 4 \\ 11 \\ 8 \end{bmatrix} \quad\checkmark
$$

## Takeaways
- Forward substitution mirrors back substitution and has the same $n^2$ cost.
- With a unit diagonal the cost drops to $n^2 - n$. This is the $L\mathbf{y} = \mathbf{b}$ half of an LU solve.

## Related topics
- [[Triangular Systems]]
- [[LU Decomposition]]
