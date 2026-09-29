---
tags: [graph-theory, theory, spectral-graph-theory, background]
source: Handwritten notes "Continuous functions" (Laplacian column)
---
# Laplace Operator and the Graph Laplacian
Back to [[self-study/graph-theory/Index|Index]] · Handwritten notes

The gradient, Jacobian, and Hessian recap lives in [[Gradient, Jacobian, and Hessian]] (convex opt). This note keeps only the piece that explains the name $L_G$.

## Continuous Laplacian
✎ "A scalar value containing the non-mixed second partials":
$$
\Delta f = \nabla^2 f = \tr(H_f) = \sum_i \frac{\partial^2 f}{\partial x_i^2}.
$$
✎ $\Delta$ is a **differential operator**: it takes $f : \R^n \to \R$ and returns another function $\R^n \to \R$.

## Discrete version
Replace $\R^n$ by a graph and $f$ by values $x_i$ on the vertices. The second difference $x_{i-1} - 2x_i + x_{i+1}$ approximates $f''$, and summing over neighbours gives
$$
\boxed{\,(L_G\,x)_i = \sum_{j \in N(i)} (x_i - x_j) \ \approx\ -\Delta f\,}
$$
- **Harmonic** ($\Delta f = 0$): $f$ equals its local average. The discrete statement is $L_Gx = 0$, and on a connected graph only constants satisfy it (the $\lambda_1 = 0$ eigenvector $\ones$).
- Watch the notation: this $\Delta$ is not the max degree $\Delta(G)$.

## Examples
- [[EX05 - Continuous and Discrete Laplacians]]

See also: [[Laplacian of a Graph]]
