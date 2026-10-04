---
tags: [graph-theory, example, ch-1]
source: Constructed from ✎ the coloured C_2k (top of p. 12), the C_5 argument (p. 11), and the circuit split (p. 12)
topics: ["[[Bipartite Graphs and Odd Cycles]]"]
---
# EX03 — Two-Colouring Cycles and Odd Circuits
Back to [Index](../Index.md)

> [!question] Problem
> (a) Two-colour $C_6$.
> (b) Show $C_5$ cannot be two-coloured.
> (c) The circuit $C = 1\,2\,3\,4\,5\,3\,6\,1$ uses edges $12, 23, 34, 45, 53, 36, 61$. Find an odd cycle inside it.

## Strategy
1. Colour greedily around the cycle. Each vertex's colour is forced by the previous one.
2. For (c), split the circuit at the repeated vertex.

## Solution
**(a)** Alternate: $A = \{2, 4, 6\}$ (blue), $B = \{1, 3, 5\}$ (red). Every edge $\{i, i+1\}$ joins opposite parities, and so does $\{6, 1\}$. So $C_6$ is bipartite.

**(b)** Put $1 \in A$ (WLOG). Then $2 \in B$, $3 \in A$, $4 \in B$, $5 \in A$. The edge $\{5, 1\}$ has both ends in $A$. ✎ "$x \in A$, $y \in A$, but $xy \in E$: contradiction, cannot be bipartite."

**(c)** $C$ has 8 entries, so its length is $7$ (odd). The vertex $z = 3$ repeats:
$$
C' = 1\,2\,\underline{3}\,6\,1 \ \ (\text{length } 4), \qquad C'' = \underline{3}\,4\,5\,\underline{3} \ \ (\text{length } 3).
$$
The lengths add: $4 + 3 = 7$. So exactly one piece is odd, and $C''$ is the odd cycle $\boxed{3\,4\,5}$, a triangle.

## Takeaways
- Two-colouring a cycle forces every colour, and the last edge decides: an even cycle closes up, an odd one clashes.
- Splitting an odd circuit keeps an odd piece, because odd = even + odd.

## Related topics
- [Bipartite Graphs and Odd Cycles](../Theory/Bipartite%20Graphs%20and%20Odd%20Cycles.md)
