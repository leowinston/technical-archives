---
tags: [convex-optimization, topic, ml-notebook, spectral-graph-theory]
source: ML notebook "Graphs" / "Laplacian of graph G"
---
# Graph Laplacian
Back to [[self-study/convex-optimization/Index|Index]] · ML notebook

## Matrices of $G = (V, E)$
- **Degree matrix:** $D_{ii} = d(v_i) = \card{\{(v_i, v_j) \in E\}}$.
- **Adjacency matrix:** $A_{ij} = A_{ji} = 1$ if $(i, j) \in E$, and $A_{ii} = 0$. It is symmetric, so the spectral theorem applies.

## Laplacian
$$
\boxed{\,L_G = D_G - A_G, \qquad x^{\top}L_Gx = \sum_{(i,j) \in E}(x_i - x_j)^2 \ge 0\,}
$$
- $L_G \succeq 0$.
- Every row sums to $0$, so $\lambda = 0$ is an eigenvalue with eigenvector $\ones$.

## Spectral gap
$$
0 = \lambda_1 \le \lambda_2 \le \cdots \le \lambda_n
$$
| $\lambda_2$ | Graph |
|---|---|
| $= 0$ | not connected |
| $> 0$, small | connected but nearly disconnected |
| $> 0$, big | very connected |

$\lambda_2$ is the **Fiedler value** and its eigenvector is the **Fiedler vector**.

## Convexity link
$\lambda_2 = \min\{x^{\top}Lx \mid \lVert x\rVert_2 = 1,\ x \perp \ones\}$. It is a concave function of the edge weights (a min of linear functions), so maximizing it is a convex problem.

See also: [[Spectral Clustering and Sparsest Cut]], [[Positive Semidefinite Matrices]]
