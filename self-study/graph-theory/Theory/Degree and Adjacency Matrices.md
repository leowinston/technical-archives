---
tags: [graph-theory, theory, spectral-graph-theory]
source: Handwritten notes "Graphs" (Diagonal matrix, Adjacency matrix)
---
# Degree and Adjacency Matrices
Back to [[self-study/graph-theory/Index|Index]] · Handwritten notes

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
$A$ is **symmetric**, so the spectral theorem ([[Positive Semidefinite Matrices]]) gives real eigenvalues and $A = Q\Lambda Q^{\top}$.

✎ Correction to my notes: $\Lambda$ is **not** positive definite for $A$. Since $\tr A = 0$, $A$ has negative eigenvalues unless $E = \emptyset$.

## Largest eigenvalue
$$
\boxed{\,\text{average degree} \le \lambda_{\max}(A) \le \Delta(G)\,}
$$
✎ If $G$ is $d$-regular, then $\Delta(G) = \delta(G) = d$ and $\lambda_{\max} = d$, with eigenvector $\ones$. My notes wrote $\lambda_{\max} = \Delta(G)$ in general, but equality needs regularity (for connected $G$).

Regularization replaces $D$ with $D + \tau I$ and $A$ with $A + \tfrac{\tau}{n}J$, which adds $\tau$ to every degree ([[Regularized Spectral Clustering]]).

See also: [[Laplacian of a Graph]], [[Neighbourhood, Degree, and Regularity]], [[EX06 - Matrices and Spectrum of the Path P3]]
