---
tags: [graph-theory, theory, ch-2]
source: Kelly, Graph Theory §2.1–2.2 (pp. 13–15)
---
# Matchings and Augmenting Paths
Back to [[self-study/graph-theory/Index|Index]] · Sections 2.1–2.2 · ✎ "Marriage"

## Matching
A **matching** is $M \subseteq E$ with $e_1 \cap e_2 = \emptyset$ for all $e_1 \ne e_2 \in M$.
✎ If $e_1 = ab$ and $e_2 = cd$, then $\{a, b\} \cap \{c, d\} = \emptyset$, so $a, b, c, d$ are all different: no two matched edges share a vertex.
- $v$ is **saturated** by $M$ if some edge of $M$ contains $v$.
- A **perfect** matching saturates every vertex. ✎ The cube's four vertical edges are one.

In a bipartite $G = (A \cup B, E)$, a matching that saturates $A$ is the same as an injection $f : A \to B$ with $x f(x) \in E$. The **neighbourhood of a set** is $N(X) = \bigcup_{x \in X} N(x)$.

## Alternating and augmenting paths
$P = x_1 \dots x_l$ is **$M$-alternating** if its edges are alternately in $M$ and not in $M$.
✎ For $2 \le i \le l - 2$: $(i, i+1) \in M \Rightarrow (i+1, i+2) \notin M$, and $(i, i+1) \notin M \Rightarrow (i+1, i+2) \in M$.
It is **$M$-augmenting** if both ends $x_1$ and $x_l$ are unsaturated. Flip every edge along $P$ to get a matching with one more edge:
$$
\boxed{\,M \text{ maximum} \implies \text{no } M\text{-augmenting path}\,}
$$

See also: [[Hall's Theorem]], [[EX04 - When Hall's Condition Fails]]
