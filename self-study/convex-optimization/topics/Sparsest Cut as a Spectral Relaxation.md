---
tags: [convex-optimization, topic, ml-notebook, relaxation]
source: ML notebook "Spectral Clustering" / "Sparsest Cut" / "Laplacian of graph G"
---
# Sparsest Cut as a Spectral Relaxation
Back to [Index](../Index.md) · ML notebook

The graph definitions ($L_G$, cut density $\phi$, the Fiedler vector, the sweep algorithm) live in the graph-theory notes. This note covers only the optimization view.

## Hard problem → easy relaxation
The sparsest cut ([Sparsest Cut](../../graph-theory/Theory/Sparsest%20Cut.md)) minimizes over $2^n$ subsets, which is NP-hard. Encode a cut as $x \in \{\pm 1\}^n$. Then drop the integrality:
$$
\min_{x \in \{\pm1\}^n,\ \text{balanced}} x^{\top}L_Gx \quad\longrightarrow\quad \boxed{\,\lambda_2 = \min_{x \perp \ones,\ \lVert x\rVert_2 = 1} x^{\top}L_Gx\,}
$$
The relaxed problem is nonconvex (a sphere constraint), but it is solved exactly by an eigenvector. That solution is the Fiedler vector.

## Relaxation bounds
The relaxation gives a lower bound, and rounding (the sweep) gives a feasible cut:
$$
\lambda_2 \ \le\ \phi_G \ \le\ \phi(\text{sweep}) \ \le\ 4\sqrt{\Delta(G)\,\lambda_2}.
$$
This is the same pattern as LP/SDP relaxations: solve the relaxation, then round it and bound the gap.

## Concavity in the edge weights
With edge weights $w \ge 0$, $L(w) = \sum_{e} w_e\, b_e b_e^{\top}$ is linear in $w$. So
$$
\lambda_2(w) = \min_{x \perp \ones,\ \lVert x\rVert = 1} x^{\top}L(w)\,x
$$
is a pointwise **min of linear functions**, which makes it **concave**. Maximizing algebraic connectivity under a weight budget is therefore a convex problem (an SDP).

## Regularization
Adding weight $\tfrac{\tau}{n}$ to every pair moves $w$ along the edges of $K_n$. For $L$ this adds exactly $\tau$ to $\lambda_2$ and leaves the Fiedler vector unchanged. With degree normalization, the relaxation gains a ridge term $\tau\sum_i(x_i - \bar x)^2$ that stops long dangling paths from looking cheap (see [Regularized Spectral Clustering](../../graph-theory/Theory/Regularized%20Spectral%20Clustering.md)).

## Explorations
- [EX10 - Relaxation Gap on a 10-Node Graph](../explorations/EX10%20-%20Relaxation%20Gap%20on%20a%2010-Node%20Graph.md)

See also: [Operations That Preserve Convexity of Functions](Operations%20That%20Preserve%20Convexity%20of%20Functions.md), [Positive Semidefinite Matrices](Positive%20Semidefinite%20Matrices.md), [Spectral Clustering Algorithm](../../graph-theory/Theory/Spectral%20Clustering%20Algorithm.md), [Regularized Spectral Clustering](../../graph-theory/Theory/Regularized%20Spectral%20Clustering.md)
