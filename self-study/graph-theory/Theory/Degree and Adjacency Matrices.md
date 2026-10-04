---
tags: [graph-theory, theory, spectral-graph-theory]
source: Handwritten notes "Graphs" (Diagonal matrix, Adjacency matrix)
---
# Degree and Adjacency Matrices
Back to [Index](../Index.md) · Handwritten notes

For $G = (V, E)$ with $V = \{v_1, \dots, v_n\}$:

## Degree matrix
✎ The diagonal holds the degree of every vertex $v \in V$:
$$
D_{ii} = d(v_i) = \card{\{(v_i, v_j) \in E \mid i \ne j\}}, \qquad D_{ij} = 0 \ (i \ne j).
$$

## Adjacency matrix
✎ It records which vertices are connected:
$$
A_{ij} = A_{ji} = \begin{cases} 1 & (i, j) \in E \\ 0 & \text{otherwise (including } i = j) \end{cases}
$$
$A$ is **symmetric**, so the spectral theorem ([Positive Semidefinite Matrices](../../convex-optimization/topics/Positive%20Semidefinite%20Matrices.md)) gives real eigenvalues and $A = Q\Lambda Q^{\top}$.

✎ Correction to my notes: $\Lambda$ is **not** positive definite for $A$. Since $\tr A = 0$, $A$ has negative eigenvalues unless $E = \emptyset$.

## Largest eigenvalue
$$
\boxed{\,\text{average degree} \le \lambda_{\max}(A) \le \Delta(G)\,}
$$
✎ If $G$ is $d$-regular, then $\Delta(G) = \delta(G) = d$ and $\lambda_{\max} = d$, with eigenvector $\ones$. My notes wrote $\lambda_{\max} = \Delta(G)$ in general, but equality needs regularity (for connected $G$).

Regularization replaces $D$ with $D + \tau I$ and $A$ with $A + \tfrac{\tau}{n}J$, which adds $\tau$ to every degree ([Regularized Spectral Clustering](Regularized%20Spectral%20Clustering.md)).

See also: [Laplacian of a Graph](Laplacian%20of%20a%20Graph.md), [Neighbourhood, Degree, and Regularity](Neighbourhood%2C%20Degree%2C%20and%20Regularity.md), [EX06 - Matrices and Spectrum of the Path P3](../Examples/EX06%20-%20Matrices%20and%20Spectrum%20of%20the%20Path%20P3.md)
