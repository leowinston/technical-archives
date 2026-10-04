---
tags: [graph-theory, index]
---
# Graph Theory Index

Self-study notes from two sources: my annotated copy of Adam Kelly's Cambridge *Graph Theory* notes (pp. 1–25; my annotations run from §1.1 to Hall's theorem), and my handwritten spectral graph theory page. Theory notes hold definitions, key results, and short proofs. Example notes hold worked problems and link back to the theory they use.

- Theory notes live in `Theory/`
- Example notes live in `Examples/`
- ✎ marks a place where I highlighted or wrote on the page

---

## Chapter 1 — Introduction

### 1.1 Definitions
- [Graphs and Common Graphs](Theory/Graphs%20and%20Common%20Graphs.md) — $G = (V, E)$, ✎ unordered pairs, $P_n$, $C_n$ (✎ $n \ge 3$), $K_n$
- [Subgraphs and Isomorphism](Theory/Subgraphs%20and%20Isomorphism.md) — $G - xy$, ✎ induced subgraph $G[X]$, ✎ $f(u)f(v) \in E' \iff uv \in E$
- [Neighbourhood, Degree, and Regularity](Theory/Neighbourhood%2C%20Degree%2C%20and%20Regularity.md) — ✎ $N(x)$, $d(x) = \card{N(x)}$, $\Delta$, $\delta$, ✎ regular sketches
- [Paths, Connectivity, and Distance](Theory/Paths%2C%20Connectivity%2C%20and%20Distance.md) — ✎ distinctness, ✎ joining paths, components, graph metric

### 1.2 Trees
- [Trees and Leaves](Theory/Trees%20and%20Leaves.md) — ✎ acyclic, three characterisations, ✎ $e(T) = \card{T} - 1$
- [Spanning Trees](Theory/Spanning%20Trees.md) — ✎ $T_1, T_2, T_3 \subseteq G$, every connected graph has one

### 1.3 Bipartite Graphs
- [Bipartite Graphs and Odd Cycles](Theory/Bipartite%20Graphs%20and%20Odd%20Cycles.md) — ✎ $C_5$ fails, ✎ circuits, bipartite $\iff$ no odd cycle

## Chapter 2 — Hall's Theorem
- [Matchings and Augmenting Paths](Theory/Matchings%20and%20Augmenting%20Paths.md) — ✎ "marriage", saturated, ✎ alternating paths
- [Hall's Theorem](Theory/Hall%27s%20Theorem.md) — ✎ $\card{N(A')} \ge \card{A'}$, "people liked ≥ people choosing"

---

## Spectral Graph Theory (handwritten notes)

### Background
- [Laplace Operator and the Graph Laplacian](Theory/Laplace%20Operator%20and%20the%20Graph%20Laplacian.md) — $\Delta f = \tr H_f$, $L_G \approx -\Delta$, harmonic functions

### Matrices of a graph
- [Degree and Adjacency Matrices](Theory/Degree%20and%20Adjacency%20Matrices.md) — $D$, $A$, spectral theorem, $\lambda_{\max}(A) \le \Delta(G)$
- [Laplacian of a Graph](Theory/Laplacian%20of%20a%20Graph.md) — $L_G = D_G - A_G \succeq 0$, four PSD conditions
- [Spectral Gap and Fiedler Vector](Theory/Spectral%20Gap%20and%20Fiedler%20Vector.md) — $0 = \lambda_1 \le \lambda_2$, connectivity, Fiedler vector

### Cuts and clustering
- [Cuts and Cut Density](Theory/Cuts%20and%20Cut%20Density.md) — $\phi(A, V - A) = n\,\card{E(A, V-A)} / (\card{A}\card{V-A})$
- [Sparsest Cut](Theory/Sparsest%20Cut.md) — $2^n$ subsets, NP-hard, $\phi_G \ge \lambda_2$
- [Spectral Clustering Algorithm](Theory/Spectral%20Clustering%20Algorithm.md) — sweep steps ①–④, $\phi \le 4\sqrt{\Delta(G)\lambda_2}$
- [Regularized Spectral Clustering](Theory/Regularized%20Spectral%20Clustering.md) — vanilla vs regularized, $D_\tau = D + \tau I$, $A_\tau = A + \tfrac{\tau}{n}J$, ridge term, dangling paths

---

## Examples

| # | Example | Source | Theory |
|---|---|---|---|
| 1 | [EX01 - Short-Circuiting a Joined Path](Examples/EX01%20-%20Short-Circuiting%20a%20Joined%20Path.md) | ✎ p. 6 | [Paths, Connectivity, and Distance](Theory/Paths%2C%20Connectivity%2C%20and%20Distance.md) |
| 2 | [EX02 - Checking a Graph for Trees](Examples/EX02%20-%20Checking%20a%20Graph%20for%20Trees.md) | ✎ pp. 8–10 | [Trees and Leaves](Theory/Trees%20and%20Leaves.md), [Spanning Trees](Theory/Spanning%20Trees.md) |
| 3 | [EX03 - Two-Colouring Cycles and Odd Circuits](Examples/EX03%20-%20Two-Colouring%20Cycles%20and%20Odd%20Circuits.md) | ✎ pp. 11–12 | [Bipartite Graphs and Odd Cycles](Theory/Bipartite%20Graphs%20and%20Odd%20Cycles.md) |
| 4 | [EX04 - When Hall's Condition Fails](Examples/EX04%20-%20When%20Hall%27s%20Condition%20Fails.md) | ✎ p. 15 | [Hall's Theorem](Theory/Hall%27s%20Theorem.md), [Matchings and Augmenting Paths](Theory/Matchings%20and%20Augmenting%20Paths.md) |
| 5 | [EX05 - Continuous and Discrete Laplacians](Examples/EX05%20-%20Continuous%20and%20Discrete%20Laplacians.md) | handwritten | [Laplace Operator and the Graph Laplacian](Theory/Laplace%20Operator%20and%20the%20Graph%20Laplacian.md) |
| 6 | [EX06 - Matrices and Spectrum of the Path P3](Examples/EX06%20-%20Matrices%20and%20Spectrum%20of%20the%20Path%20P3.md) | handwritten | [Degree and Adjacency Matrices](Theory/Degree%20and%20Adjacency%20Matrices.md), [Laplacian of a Graph](Theory/Laplacian%20of%20a%20Graph.md) |
| 7 | [EX07 - Sweep Cut on Two Joined Triangles](Examples/EX07%20-%20Sweep%20Cut%20on%20Two%20Joined%20Triangles.md) | handwritten | [Spectral Clustering Algorithm](Theory/Spectral%20Clustering%20Algorithm.md), [Sparsest Cut](Theory/Sparsest%20Cut.md) |
| 8 | [EX08 - Whisker Cut Versus Regularized Clustering](Examples/EX08%20-%20Whisker%20Cut%20Versus%20Regularized%20Clustering.md) | constructed | [Regularized Spectral Clustering](Theory/Regularized%20Spectral%20Clustering.md), [Cuts and Cut Density](Theory/Cuts%20and%20Cut%20Density.md) |

---

## Related
Shared background lives in the convex-optimization notes, and the graph notes link to it rather than repeating it:
- [Gradient, Jacobian, and Hessian](../convex-optimization/topics/Gradient%2C%20Jacobian%2C%20and%20Hessian.md) — the multivariable recap
- [Positive Semidefinite Matrices](../convex-optimization/topics/Positive%20Semidefinite%20Matrices.md) — spectral theorem, four PSD conditions
- [Sparsest Cut as a Spectral Relaxation](../convex-optimization/topics/Sparsest%20Cut%20as%20a%20Spectral%20Relaxation.md) — sparsest cut as a relaxation, concavity of $\lambda_2$ in edge weights, regularization as adding weight $\tfrac{\tau}{n}$ along $K_n$
- [Bias-Variance Tradeoff](../convex-optimization/topics/Bias-Variance%20Tradeoff.md) — ridge regularization, the same penalty as in [Regularized Spectral Clustering](Theory/Regularized%20Spectral%20Clustering.md)

## Sources
- Adam Kelly, *Graph Theory* (Cambridge Part II notes, Lent 2021), pp. 1–25
- Handwritten iPad page "Graphs" (spectral graph theory + multivariable review)