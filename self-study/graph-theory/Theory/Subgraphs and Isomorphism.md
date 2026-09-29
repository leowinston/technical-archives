---
tags: [graph-theory, theory, ch-1]
source: Kelly, Graph Theory §1.1.2–1.1.3 (pp. 4–5)
---
# Subgraphs and Isomorphism
Back to [[self-study/graph-theory/Index|Index]] · Sections 1.1.2–1.1.3

## Subgraph
$H = (V', E')$ is a **subgraph** of $G = (V, E)$ if $V' \subseteq V$ and $E' \subseteq E$: delete some vertices and edges.
- $G - xy$ removes the edge. ✎ Sketch: $x$ and $y$ both stay.
- $G - x$ removes $x$ **and every edge at $x$**.
- $G + xy$ and $G + x$ add them.

## Induced subgraph
$$
G[X] = \big(X,\ \{xy \in E \mid x, y \in X\}\big)
$$
✎ Keep every vertex $v \in X$, and keep an edge $xy \in E$ exactly when both ends $x, y \in X$.

## Isomorphism
A bijection $f : V \to V'$ is a **graph isomorphism** if
$$
\boxed{\,f(u)f(v) \in E' \iff uv \in E\,}
$$
✎ Map every vertex of $V$ through $f$. Then $f(u)f(v)$ is an edge of $E'$ exactly when $uv$ is an edge of $E$. Isomorphic graphs are the same graph with the vertices relabeled.

See also: [[Graphs and Common Graphs]], [[Trees and Leaves]] (acyclic is defined through subgraphs)
