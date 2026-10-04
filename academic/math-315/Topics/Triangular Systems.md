---
tags: [math-315, topic, lecture-3]
---
# Triangular Systems
Back to [Index](../Index.md) · Section 3.1.1

## Diagonal systems
$$
a_{ii}x_i = b_i \implies x_i = \frac{b_i}{a_{ii}}
$$
This costs $n$ divisions, so $O(n)$.

## Back substitution ($U\mathbf{x} = \mathbf{y}$)
The last row has only $x_n$ in it. Solve from the bottom up:
$$
x_i = \frac{1}{u_{ii}}\left(y_i - \sum_{j=i+1}^{n} u_{ij}x_j\right), \qquad i = n, \dots, 1
$$
```
for i from n down to 1:
    x[i] = (y[i] - sum(u[i][j] * x[j] for j from i+1 to n)) / u[i][i]
```

## Forward substitution ($L\mathbf{x} = \mathbf{y}$)
The first row has only $x_1$ in it. Solve from the top down:
$$
x_i = \frac{1}{l_{ii}}\left(y_i - \sum_{j=1}^{i-1} l_{ij}x_j\right), \qquad i = 1, \dots, n
$$
Both methods need every $u_{ii}$ (or $l_{ii}$) to be nonzero. For a triangular matrix that is the same as being nonsingular.

## Operation count
Row $i$ costs $2(i-1)$ flops in the sum plus 1 division:
$$
\sum_{i=1}^{n} 2(i-1) + n = (n-1)n + n = n^2
$$
So solving a triangular system is $O(n^2)$.

## Example
$$
\begin{bmatrix} 2 & 1 & -1 \\ 0 & 3 & 2 \\ 0 & 0 & 4 \end{bmatrix}\mathbf{x} = \begin{bmatrix} 3 \\ 13 \\ 8 \end{bmatrix}
\implies x_3 = 2,\ x_2 = 3,\ x_1 = 1
$$

## Explorations
- [EX01 - Back Substitution on a 3x3 System](../Explorations/EX01%20-%20Back%20Substitution%20on%20a%203x3%20System.md)
- [EX02 - Forward Substitution on a 3x3 System](../Explorations/EX02%20-%20Forward%20Substitution%20on%20a%203x3%20System.md)

See also: [Gaussian Elimination](Gaussian%20Elimination.md), [LU Decomposition](LU%20Decomposition.md)
