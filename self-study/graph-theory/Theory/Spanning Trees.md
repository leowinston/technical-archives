---
tags: [graph-theory, theory, ch-1]
source: Kelly, Graph Theory §1.2 (pp. 10–11)
---
# Spanning Trees
Back to [Index](../Index.md) · Section 1.2

$T$ is a **spanning tree** of $G$ if $T$ is a tree on **all** of $V(G)$ and $T$ is a subgraph of $G$.
✎ One graph usually has many: $T_1, T_2, T_3 \subseteq G$ in my sketch.

## Existence
$$
\boxed{\text{Every connected graph contains a spanning tree.}}
$$
A tree is a minimal connected graph (see [Trees and Leaves](Trees%20and%20Leaves.md)). So delete edges while the graph stays connected. What remains is minimal connected, and so it is a spanning tree. ✎ Sketch: cross out one edge on each cycle.
```
T ← G
while T has a cycle C:
    remove any edge of C      # T stays connected
return T                      # a tree with |V| − 1 edges
```

See also: [EX02 - Checking a Graph for Trees](../Examples/EX02%20-%20Checking%20a%20Graph%20for%20Trees.md), [Paths, Connectivity, and Distance](Paths%2C%20Connectivity%2C%20and%20Distance.md)
