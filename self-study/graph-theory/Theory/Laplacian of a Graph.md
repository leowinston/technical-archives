---
tags: [graph-theory, theory, spectral-graph-theory]
source: Handwritten notes "Laplacian of graph G"
---
# Laplacian of a Graph
Back to [Index](../Index.md) · Handwritten notes

$$
\boxed{\,L_G = D_G - A_G, \qquad x^{\top} L_G\, x = \sum_{(i,j) \in E} (x_i - x_j)^2 \ge 0\,}
$$

## Properties
- **Every row sums to 0**: $d(v_i)$ on the diagonal, minus a 1 for each neighbour.
- So $\lambda = 0$ is an eigenvalue, with eigenvector $\ones$.
- $L_G$ is **positive semidefinite**. The quadratic form above is a sum of squares.

## ✎ PSD via $B^{\top}B$
My notes list the four equivalent PSD conditions (in [Positive Semidefinite Matrices](../../convex-optimization/topics/Positive%20Semidefinite%20Matrices.md)). For $L_G$, the condition $M = B^{\top}B$ is concrete. Take $B$ to be the signed **incidence matrix**, with one row per edge $(i, j)$ holding $+1$ at $i$ and $-1$ at $j$. Then $L_G = B^{\top}B$ and $\lVert Bx \rVert^2 = \sum_E (x_i - x_j)^2$.

## Regularized
Adding weight $\tfrac{\tau}{n}$ to every pair gives $L_G + \tau\big(I - \tfrac1n J\big) \succeq 0$. That shifts every nonzero eigenvalue by $\tau$ without changing any eigenvector. See [Regularized Spectral Clustering](Regularized%20Spectral%20Clustering.md) for why the degree normalization is needed.

See also: [Spectral Gap and Fiedler Vector](Spectral%20Gap%20and%20Fiedler%20Vector.md), [Degree and Adjacency Matrices](Degree%20and%20Adjacency%20Matrices.md), [Laplace Operator and the Graph Laplacian](Laplace%20Operator%20and%20the%20Graph%20Laplacian.md)
