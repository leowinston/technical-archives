---
tags: [math-315, topic, lecture-3]
---
# Cholesky Factorization
Back to [Index](../Index.md) · Section 3.3.3

## Statement
For SPD $A$, the pivots are positive, so $D^{1/2}$ is real:
$$
A = LDL^{\top} = \big(LD^{1/2}\big)\big(LD^{1/2}\big)^{\top} = GG^{\top}, \qquad G = LD^{1/2}
$$
$G$ is lower triangular with $g_{kk} > 0$.

## Entry formulas
Matching $a_{ik} = \sum_{j \le k} g_{ij}g_{kj}$ for $i \ge k$ gives
$$
g_{kk} = \sqrt{a_{kk} - \sum_{j<k} g_{kj}^2}, \qquad
g_{ik} = \frac{a_{ik} - \sum_{j<k} g_{ij}g_{kj}}{g_{kk}}
$$
```
for k from 1 to n:
    s = a[k][k] - sum(g[k][j]^2 for j < k)
    if s <= 0: stop "not SPD"
    g[k][k] = sqrt(s)
    for i from k+1 to n:
        g[i][k] = (a[i][k] - sum(g[i][j] * g[k][j] for j < k)) / g[k][k]
```

## Cost and solve
It costs $\tfrac13 n^3$ flops, **half of LU**. To solve, do $G\mathbf{y} = \mathbf{b}$ (forward), then $G^{\top}\mathbf{x} = \mathbf{y}$ (back).

## Example
$$
G = \begin{bmatrix} 2 & 0 & 0 \\ -0.5 & 2 & 0 \\ 0.5 & 1.5 & 1 \end{bmatrix}, \qquad
GG^{\top} = \begin{bmatrix} 4 & -1 & 1 \\ -1 & 4.25 & 2.75 \\ 1 & 2.75 & 3.5 \end{bmatrix}
$$

## Explorations
- [EX08 - Cholesky Factorization of a 3x3 SPD Matrix](../Explorations/EX08%20-%20Cholesky%20Factorization%20of%20a%203x3%20SPD%20Matrix.md)

See also: [Symmetric Positive Definite Matrices](Symmetric%20Positive%20Definite%20Matrices.md), [LDLT Factorization](LDLT%20Factorization.md), [Log det via Cholesky](../../../self-study/convex-optimization/explorations/EX11%20-%20Log%20Det%20via%20Cholesky.md) (convex opt)
