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
- [[Graphs and Common Graphs]] — $G = (V, E)$, ✎ unordered pairs, $P_n$, $C_n$ (✎ $n \ge 3$), $K_n$
- [[Subgraphs and Isomorphism]] — $G - xy$, ✎ induced subgraph $G[X]$, ✎ $f(u)f(v) \in E' \iff uv \in E$
- [[Neighbourhood, Degree, and Regularity]] — ✎ $N(x)$, $d(x) = \card{N(x)}$, $\Delta$, $\delta$, ✎ regular sketches
- [[Paths, Connectivity, and Distance]] — ✎ distinctness, ✎ joining paths, components, graph metric

### 1.2 Trees
- [[Trees and Leaves]] — ✎ acyclic, three characterisations, ✎ $e(T) = \card{T} - 1$
- [[Spanning Trees]] — ✎ $T_1, T_2, T_3 \subseteq G$, every connected graph has one

### 1.3 Bipartite Graphs
- [[Bipartite Graphs and Odd Cycles]] — ✎ $C_5$ fails, ✎ circuits, bipartite $\iff$ no odd cycle

## Chapter 2 — Hall's Theorem
- [[Matchings and Augmenting Paths]] — ✎ "marriage", saturated, ✎ alternating paths
- [[Hall's Theorem]] — ✎ $\card{N(A')} \ge \card{A'}$, "people liked ≥ people choosing"

---

## Spectral Graph Theory (handwritten notes)

### Background
- [[Laplace Operator and the Graph Laplacian]] — $\Delta f = \tr H_f$, $L_G \approx -\Delta$, harmonic functions

### Matrices of a graph
- [[Degree and Adjacency Matrices]] — $D$, $A$, spectral theorem, $\lambda_{\max}(A) \le \Delta(G)$
- [[Laplacian of a Graph]] — $L_G = D_G - A_G \succeq 0$, four PSD conditions
- [[Spectral Gap and Fiedler Vector]] — $0 = \lambda_1 \le \lambda_2$, connectivity, Fiedler vector

### Cuts and clustering
- [[Cuts and Cut Density]] — $\phi(A, V - A) = n\,\card{E(A, V-A)} / (\card{A}\card{V-A})$
- [[Sparsest Cut]] — $2^n$ subsets, NP-hard, $\phi_G \ge \lambda_2$
- [[Spectral Clustering Algorithm]] — sweep steps ①–④, $\phi \le 4\sqrt{\Delta(G)\lambda_2}$
- [[Regularized Spectral Clustering]] — vanilla vs regularized, $D_\tau = D + \tau I$, $A_\tau = A + \tfrac{\tau}{n}J$, ridge term, dangling paths

---

## Examples

| # | Example | Source | Theory |
|---|---|---|---|
| 1 | [[EX01 - Short-Circuiting a Joined Path]] | ✎ p. 6 | [[Paths, Connectivity, and Distance]] |
| 2 | [[EX02 - Checking a Graph for Trees]] | ✎ pp. 8–10 | [[Trees and Leaves]], [[Spanning Trees]] |
| 3 | [[EX03 - Two-Colouring Cycles and Odd Circuits]] | ✎ pp. 11–12 | [[Bipartite Graphs and Odd Cycles]] |
| 4 | [[EX04 - When Hall's Condition Fails]] | ✎ p. 15 | [[Hall's Theorem]], [[Matchings and Augmenting Paths]] |
| 5 | [[EX05 - Continuous and Discrete Laplacians]] | handwritten | [[Laplace Operator and the Graph Laplacian]] |
| 6 | [[EX06 - Matrices and Spectrum of the Path P3]] | handwritten | [[Degree and Adjacency Matrices]], [[Laplacian of a Graph]] |
| 7 | [[EX07 - Sweep Cut on Two Joined Triangles]] | handwritten | [[Spectral Clustering Algorithm]], [[Sparsest Cut]] |
| 8 | [[EX08 - Whisker Cut Versus Regularized Clustering]] | constructed | [[Regularized Spectral Clustering]], [[Cuts and Cut Density]] |

---

## Related
Shared background lives in the convex-optimization notes, and the graph notes link to it rather than repeating it:
- [[Gradient, Jacobian, and Hessian]] — the multivariable recap
- [[Positive Semidefinite Matrices]] — spectral theorem, four PSD conditions
- [[Sparsest Cut as a Spectral Relaxation]] — sparsest cut as a relaxation, concavity of $\lambda_2$ in edge weights, regularization as adding weight $\tfrac{\tau}{n}$ along $K_n$
- [[Bias-Variance Tradeoff]] — ridge regularization, the same penalty as in [[Regularized Spectral Clustering]]

## Sources
- Adam Kelly, *Graph Theory* (Cambridge Part II notes, Lent 2021), pp. 1–25
- Handwritten iPad page "Graphs" (spectral graph theory + multivariable review)