---
tags: [convex-optimization, topic, ml-notebook, spectral-graph-theory]
source: ML notebook "Spectral Clustering" / "Sparsest Cut"
---
# Spectral Clustering and Sparsest Cut
Back to [[self-study/convex-optimization/Index|Index]] · ML notebook

## Cuts
For a connected $G = (V, E)$ with $n$ vertices, a **cut** splits $V$ into $A$ and $V - A$. Its **density** is
$$
\phi(A, V - A) = n\,\frac{\card{E(A, V - A)}}{\card{A}\cdot\card{V - A}} = n \cdot \frac{\text{edges cut}}{\text{possible edges}}.
$$
The **sparsest cut** attains $\phi_G = \min_A \phi(A, V - A)$. Checking every subset is $2^n$ work (NP-hard) — ✎ "approximations are awesome".

## Theorem (Cheeger-type)
1. $\phi_G \ge \lambda_2$.
2. The algorithm below finds a cut with density at most $4\sqrt{\Delta(G)\,\lambda_2}$, where $\Delta(G)$ is the max degree.

## Algorithm
```
v ← Fiedler vector of L_G
sort vertices by v
for k = 1..n−1:   A_k ← first k vertices
return the A_k with the lowest density
```
Only $n - 1$ cuts are checked, not $2^n$.

## Why it is a relaxation
Minimizing $x^{\top}Lx$ over $x \in \{\pm1\}^n$ is combinatorial. Relaxing to $x \perp \ones$, $\lVert x\rVert_2 = 1$ is solved exactly by the Fiedler vector.

## Explorations
- [[EX10 - Fiedler Vector Sparsest Cut on a 10-Node Graph]]

See also: [[Graph Laplacian]]
