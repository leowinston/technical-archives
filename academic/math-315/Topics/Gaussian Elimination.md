---
tags: [math-315, topic, lecture-3]
---
# Gaussian Elimination
Back to [Index](../Index.md) · Section 3.1.2

## Goal
Reduce $A\mathbf{x} = \mathbf{b}$ to an equivalent upper triangular system, then back substitute ([Triangular Systems](Triangular%20Systems.md)).

## Row operations
Work on the augmented matrix $[\,A \mid \mathbf{b}\,]$ with three moves:
- **Scale:** $R_i \leftarrow sR_i$ ($s \neq 0$)
- **Swap:** $R_i \leftrightarrow R_j$
- **Replace:** $R_i \leftarrow R_i - sR_j$

## Elimination step
With pivot $a_{jj}$, the multiplier $m_{ij} = a_{ij}/a_{jj}$ zeroes out $a_{ij}$:
$$
a_{ik} \leftarrow a_{ik} - m_{ij}a_{jk}, \qquad b_i \leftarrow b_i - m_{ij}b_j
$$
If the pivot is $0$, this fails and you need [Partial Pivoting](Partial%20Pivoting.md).
```
for j from 1 to n-1:
    for i from j+1 to n:
        m = a[i][j] / a[j][j]
        row i of [A | b] -= m * row j
```

## Operation count
With $k = n - j$ rows below the pivot, each costing $1 + 2k$ flops:
$$
\sum_{k=1}^{n-1} k(1 + 2k) = \frac{(n-1)n}{2} + \frac{(n-1)n(2n-1)}{3} \approx \frac{2}{3}n^3
$$
Elimination is $O(n^3)$, which dominates the $O(n^2)$ back substitution.

## Example
$$
\begin{bmatrix} 2 & 1 & 1 \\ 4 & 3 & 3 \\ 8 & 7 & 9 \end{bmatrix}
\xrightarrow[R_3 - 4R_1]{R_2 - 2R_1}
\begin{bmatrix} 2 & 1 & 1 \\ 0 & 1 & 1 \\ 0 & 3 & 5 \end{bmatrix}
$$

## Explorations
- [EX03 - Gaussian Elimination and LU of a 3x3 Matrix](../Explorations/EX03%20-%20Gaussian%20Elimination%20and%20LU%20of%20a%203x3%20Matrix.md)
- [EX04 - Exploration 3.2.12 - A Matrix with No LU Decomposition](../Explorations/EX04%20-%20Exploration%203.2.12%20-%20A%20Matrix%20with%20No%20LU%20Decomposition.md)

See also: [LU Decomposition](LU%20Decomposition.md), [Partial Pivoting](Partial%20Pivoting.md)
