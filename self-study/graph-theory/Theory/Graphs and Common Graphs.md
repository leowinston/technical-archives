---
tags: [graph-theory, theory, ch-1]
source: Kelly, Graph Theory §1.1–1.1.1 (pp. 2–4)
---
# Graphs and Common Graphs
Back to [[self-study/graph-theory/Index|Index]] · Section 1.1

## Graph
A **graph** is $G = (V, E)$ with $E \subseteq \{\{x, y\} \mid x, y \in V,\ x \ne y\}$.
- ✎ Every edge joins two vertices $v_1 \ne v_2$, and the pair is **unordered**: $v_1 - v_2$ has no direction.
- ✎ No loops and no multiple edges. They are "outlawed" for now.
- Shorthand: $xy$ for the edge $\{x, y\}$, $\card{G} = \card{V}$, $e(G) = \card{E}$.

## Common graphs
| Graph | Edges on $\{1, \dots, n\}$ | $e(G)$ |
|---|---|---|
| path $P_n$ | $\{i, i+1\}$ | $n - 1$, its **length** |
| cycle $C_n$, $n \ge 3$ | $\{i, i+1\}$ and ✎ $\{n, 1\}$, "connects back to the beginning" | $n$ |
| complete $K_n$ | every pair | $\binom{n}{2}$ |
| empty $\overline{K_n}$ | none | $0$ |

✎ $C_n$ needs $n \ge 3$ because it "doesn't work for 2": $\{1, 2\}$ and $\{2, 1\}$ are the same edge. $C_3$ has $E = \{\{1,2\}, \{2,3\}, \{1,3\}\}$: all adjacent vertices connect, so $C_3 = K_3$.

See also: [[Subgraphs and Isomorphism]], [[Neighbourhood, Degree, and Regularity]], [[Regularized Spectral Clustering]] (adds a faint $K_n$ to the graph)
