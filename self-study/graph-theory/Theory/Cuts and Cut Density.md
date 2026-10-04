---
tags: [graph-theory, theory, spectral-graph-theory]
source: Handwritten notes "Spectral Clustering"
---
# Cuts and Cut Density
Back to [Index](../Index.md) · Handwritten notes

Let $G = (V, E)$ be a connected graph with $n$ vertices.
- **Cluster:** a set $A \subseteq V$.
- **Cut:** a partition of $V$ into $A$ and $V - A$. The two parts are disjoint: $A \cap (V - A) = \emptyset$.
- $E(A, V - A)$ is the set of edges with one end on each side.

## Density
$$
\boxed{\,\phi(A, V - A) = n \cdot \frac{\card{E(A, V - A)}}{\card{A}\cdot\card{V - A}}\,}
$$
✎ The numerator counts edges actually in $G$ across the cut. The denominator counts the possible edges across it. The factor $n$ scales for size.

✎ Sketch: two clusters (blue and red) joined by one edge. The cut along the yellow line crosses a single edge, so its density is low.

Sanity check: in $K_n$ every possible edge is present, so every cut has density $n$.

✎ Caveat: a long path hanging by one edge has a low density too, so density can prefer cutting off a thin tree over splitting real clusters ([EX08 - Whisker Cut Versus Regularized Clustering](../Examples/EX08%20-%20Whisker%20Cut%20Versus%20Regularized%20Clustering.md)).

See also: [Sparsest Cut](Sparsest%20Cut.md), [Spectral Clustering Algorithm](Spectral%20Clustering%20Algorithm.md), [Regularized Spectral Clustering](Regularized%20Spectral%20Clustering.md)
