---
tags: [math-315, topic, lecture-3]
---
# QR Factorization
Back to [[academic/math-315/Index|Index]] · Section 3.3 (QR)

## Statement
$A = QR$, with $Q$ orthogonal and $R$ upper triangular. It exists whenever $A \in \mathbb{R}^{m\times n}$, $m \ge n$, has full column rank.

## Orthogonal matrices
$$
Q^{\top}Q = I \iff Q^{-1} = Q^{\top} \iff \mathbf{q}_i^{\top}\mathbf{q}_j = \delta_{ij}
$$
Orthogonal matrices preserve length, $\|Q\mathbf{x}\|_2 = \|\mathbf{x}\|_2$, so $\kappa_2(Q) = 1$.

## Solving
$$
QR\mathbf{x} = \mathbf{b} \implies R\mathbf{x} = Q^{\top}\mathbf{b}
$$
Compute $\mathbf{y} = Q^{\top}\mathbf{b}$, then back substitute.

## Gram–Schmidt (by hand)
$$
r_{ij} = \mathbf{q}_i^{\top}\mathbf{a}_j, \qquad
\mathbf{v}_j = \mathbf{a}_j - \sum_{i<j} r_{ij}\mathbf{q}_i, \qquad
r_{jj} = \|\mathbf{v}_j\|_2, \qquad
\mathbf{q}_j = \mathbf{v}_j / r_{jj}
$$

## Cost
It costs $\tfrac43 n^3$ flops, about twice LU. It is used mainly for least squares.

## Example
$$
\begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}
= \begin{bmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{bmatrix}
\begin{bmatrix} 5 & 4 \\ 0 & 3 \end{bmatrix}
$$

## Explorations
- [[EX09 - QR Factorization and Solve of a 2x2 System]]

See also: [[Singular Value Decomposition]], [[Condition Number]]
