---
tags: [graph-theory, theory, ch-1]
source: Kelly, Graph Theory §1.2 (pp. 8–10)
---
# Trees and Leaves
Back to [[self-study/graph-theory/Index|Index]] · Section 1.2

## Acyclic graphs and trees
$G$ is **acyclic** if no subgraph is isomorphic to a cycle $C_n$. ✎ That is, no $G_s = (V', E')$ with $V' \subseteq V$ and $E' \subseteq E$ is a $C_3$, $C_4$, $C_5$, ….
A **tree** is a connected, acyclic graph.

## Characterising trees
The following are equivalent:
1. $G$ is a tree.
2. $G$ is **maximal acyclic**: adding any edge creates a cycle.
3. $G$ is **minimal connected**: removing any edge disconnects it.

Key step for (1 ⇒ 2): $x$ and $y$ are joined by a path $P$, so $xPy$ plus the new edge $xy$ is a cycle.

## Leaves
A **leaf** is a vertex with $d(v) = 1$. Every tree with $\card{T} \ge 2$ has a leaf. The ends of a longest path give two, and $P_n$ shows that two is the best possible.

## Edge count
$$
\boxed{\,e(T) = \card{T} - 1\,}
$$
✎ "$n$ vertices ⇒ $n - 1$ edges." ✎ Proof by induction: remove a leaf $x$. Then $T - x$ is still a tree, so $e(T) = e(T - x) + 1 = (n - 2) + 1$. Read backwards, "you can simply add a vertex!" (and one edge).

## Examples
- [[EX02 - Checking a Graph for Trees]]

See also: [[Spanning Trees]], [[Paths, Connectivity, and Distance]], [[Regularized Spectral Clustering]] (trees hanging off a graph by one edge fool vanilla spectral clustering)
