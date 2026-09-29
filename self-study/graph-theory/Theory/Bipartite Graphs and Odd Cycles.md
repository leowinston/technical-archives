---
tags: [graph-theory, theory, ch-1]
source: Kelly, Graph Theory §1.3 (pp. 11–13)
---
# Bipartite Graphs and Odd Cycles
Back to [[self-study/graph-theory/Index|Index]] · Section 1.3

## Bipartite
$G$ is **bipartite** if $V = A \cup B$ with $A \cap B = \emptyset$ and every edge has one end in $A$ and one in $B$.
✎ Colour $A$ blue and $B$ red. Then every edge is blue–red. The cube is an example.

## Cycles
$$
\boxed{\,C_{2k} \text{ is bipartite}, \qquad C_{2k+1}\ (k \ge 1) \text{ is not}\,}
$$
- $C_{2k}$: put even $i$ in $A$ and odd $i$ in $B$. The neighbours $i \pm 1$ have the opposite parity.
- $C_{2k+1}$: ✎ every $v \in A$ has $d(v) = 2$ and connects to two vertices in $B$. Counting edges gives $2\card{A} = 2\card{B}$, but $2k + 1$ is odd. ✎ The simplest case is $C_3$.

## Circuits
A **circuit** $x_1 \dots x_l$ has $x_1 = x_l$ and consecutive vertices adjacent, and vertices may repeat. Its length is $l - 1$ (✎ $l$ entries, $l - 1$ edges).
**An odd circuit contains an odd cycle.** Split it at a repeated vertex $z$ into two shorter circuits. One of them is odd, so induct.

## Bipartite criterion
$$
\boxed{\,G \text{ bipartite} \iff G \text{ has no odd cycle}\,}
$$
For (⇐), work in one component. Fix $v$, and let $A = \{u \mid d(u, v) \text{ odd}\}$ and $B = \{u \mid d(u, v) \text{ even}\}$. An edge inside $A$ or inside $B$ would close an odd circuit.

## Examples
- [[EX03 - Two-Colouring Cycles and Odd Circuits]]

See also: [[Matchings and Augmenting Paths]]
