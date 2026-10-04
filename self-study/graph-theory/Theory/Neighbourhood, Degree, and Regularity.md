---
tags: [graph-theory, theory, ch-1]
source: Kelly, Graph Theory §1.1.3, §1.1.5 (pp. 5, 7)
---
# Neighbourhood, Degree, and Regularity
Back to [Index](../Index.md) · Sections 1.1.3, 1.1.5

## Neighbourhood
$x$ and $y$ are **adjacent** if $xy \in E$.
$$
N(x) = \{y \in V \mid xy \in E\}
$$
✎ "The set of all vertices that have an edge with $x$." Since there are no loops, $x \notin N(x)$.

## Degree
$$
\boxed{\,d(x) = \card{N(x)}\,}
$$
✎ The number of neighbours equals the number of edges at vertex $x$.

The **maximum** and **minimum degree** are $\Delta(G) = \max_{x} d(x)$ and $\delta(G) = \min_{x} d(x)$. ✎ Some vertices $x, y$ attain them: $d(x) = \Delta(G)$, $d(y) = \delta(G)$.

## Regular graphs
$G$ is **$k$-regular** if $d(x) = k$ for every $x$, so $\Delta(G) = \delta(G) = k$.

| Graph | Regular? |
|---|---|
| $K_n$ | $(n-1)$-regular |
| $C_n$ | 2-regular |
| $P_n$, $n \ge 3$ | no: the ends have degree 1, the middle vertices degree 2 |

✎ Sketches: $K_2$, $C_3$, $C_4$, $K_4$ are regular. $K_4$ minus an edge is not (degrees $3, 3, 2, 2$).

See also: [Degree and Adjacency Matrices](Degree%20and%20Adjacency%20Matrices.md), [Paths, Connectivity, and Distance](Paths%2C%20Connectivity%2C%20and%20Distance.md)
