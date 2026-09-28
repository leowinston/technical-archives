---
tags: [math-315, exploration, lecture-3]
source: Constructed example for Section 3.1.1
topics: ["[[Triangular Systems]]"]
---
# EX01 — Back Substitution on a 3×3 System
Back to [[Index]]

> [!question] Problem
> Solve $U\mathbf{x} = \mathbf{y}$ by back substitution and count the floating-point operations:
> $$
> \begin{bmatrix} 2 & 1 & -1 \\ 0 & 3 & 2 \\ 0 & 0 & 4 \end{bmatrix}
> \begin{bmatrix} x_1 \\ x_2 \\ x_3 \end{bmatrix} =
> \begin{bmatrix} 3 \\ 13 \\ 8 \end{bmatrix}
> $$

## Setup
- **Matrix type:** upper triangular, $n = 3$
- **Nonsingular?** Yes. $\det U = 2 \cdot 3 \cdot 4 = 24 \neq 0$, so every divisor $u_{ii}$ is nonzero.
- **Method:** back substitution, $x_i = \dfrac{1}{u_{ii}}\Big(y_i - \sum_{j>i} u_{ij}x_j\Big)$

## Strategy
1. The last row involves only $x_3$. Solve it.
2. Move up one row. Every unknown to the right is already known, so subtract those terms and divide by the diagonal.
3. Tally multiplications, subtractions and divisions row by row and compare with $n^2$.

## Solution
Written out as equations, the system is
$$
\begin{align*}
2x_1 + x_2 - x_3 &= 3 \\
3x_2 + 2x_3 &= 13 \\
4x_3 &= 8
\end{align*}
$$

**Row $i = 3$.** The inner loop is empty ($j$ runs from $4$ to $3$):
$$
x_3 = \frac{y_3}{u_{33}} = \frac{8}{4} = 2
$$

**Row $i = 2$.** The inner loop runs for $j = 3$:
$$
\begin{align*}
x_2 &= y_2 = 13 \\
x_2 &= x_2 - u_{23}x_3 = 13 - (2)(2) = 9 \\
x_2 &= \frac{x_2}{u_{22}} = \frac{9}{3} = 3
\end{align*}
$$

**Row $i = 1$.** The inner loop runs for $j = 2, 3$:
$$
\begin{align*}
x_1 &= y_1 = 3 \\
x_1 &= x_1 - u_{12}x_2 = 3 - (1)(3) = 0 \\
x_1 &= x_1 - u_{13}x_3 = 0 - (-1)(2) = 2 \\
x_1 &= \frac{x_1}{u_{11}} = \frac{2}{2} = 1
\end{align*}
$$
$$
\boxed{\,\mathbf{x} = \begin{bmatrix} 1 \\ 3 \\ 2 \end{bmatrix}\,}
$$

### Trace of the algorithm
```
x = [_, _, _]
i = 3:  x[3] = 8                  -> x[3] = 8 / 4          = 2
i = 2:  x[2] = 13
        j = 3:  x[2] = 13 - 2*2   = 9
                                   -> x[2] = 9 / 3          = 3
i = 1:  x[1] = 3
        j = 2:  x[1] = 3 - 1*3    = 0
        j = 3:  x[1] = 0 - (-1)*2 = 2
                                   -> x[1] = 2 / 2          = 1
```

### Operation count
| Row $i$ | Inner passes $n - i$ | mult | sub | div | Flops |
|---|---|---|---|---|---|
| 3 | 0 | 0 | 0 | 1 | 1 |
| 2 | 1 | 1 | 1 | 1 | 3 |
| 1 | 2 | 2 | 2 | 1 | 5 |
| **Total** | | 3 | 3 | 3 | **9** |

This matches the general formula:
$$
\sum_{i=1}^{n}\big[2(n-i) + 1\big] = 2\cdot\frac{(n-1)n}{2} + n = n^2 = 3^2 = 9
$$
Row $i$ costs $2(n-i) + 1$ flops, the odd numbers $1, 3, 5, \dots$, and the first $n$ odd numbers add up to $n^2$.

## Check
$$
U\mathbf{x} = \begin{bmatrix} 2(1) + 1(3) - 1(2) \\ 3(3) + 2(2) \\ 4(2) \end{bmatrix} = \begin{bmatrix} 3 \\ 13 \\ 8 \end{bmatrix} = \mathbf{y} \quad\checkmark
$$

## Takeaways
- Each row brings in exactly **one** new unknown. That is why triangular systems are easy.
- The cost is $O(n^2)$. The expensive part of a general solve is getting to triangular form ([[Gaussian Elimination]]), not this step.
- A zero on the diagonal would make the division impossible. For triangular matrices, "nonsingular" means exactly "no zero diagonal entries".

## Related topics
- [[Triangular Systems]]
- [[LU Decomposition]]
