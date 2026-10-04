---
tags: [graph-theory, theory, ch-2]
source: Kelly, Graph Theory §2.3–2.4 (pp. 15–18)
---
# Hall's Theorem
Back to [Index](../Index.md) · Sections 2.3–2.4

Let $G = (A \cup B, E)$ be bipartite. Then
$$
\boxed{\,\text{there is a matching saturating } A \iff \card{N(A')} \ge \card{A'} \text{ for every } A' \subseteq A\,}
$$
✎ "Must be $\ge$": the people who are liked must be at least as many as the people who are choosing. ✎ "If too concentrated ⇒ no pairing": when some group $A'$ likes too few people, they cannot all be paired.

## Proof idea
- (⇒) The partners of $A'$ are distinct and lie in $N(A')$.
- (⇐) Take a maximum matching $M$ and suppose $a_0$ is unsaturated. Grow $A_i \subseteq A$ and $B_i \subseteq B$ along alternating paths from $a_0$, with $\card{A_i} = i + 1$ and $\card{B_i} = i$. Hall gives a new $b \in N(A_i) \setminus B_i$. It is saturated, or else there would be an augmenting path, and its partner enlarges $A_i$. The sets would grow forever, which is impossible.

## Corollaries (pp. 16–18, not annotated)
- A $k$-regular bipartite graph ($k \ge 1$) has a perfect matching: $k\card{A'} \le k\card{N(A')}$.
- A matching saturating $\card{A} - d$ vertices exists $\iff \card{N(A')} \ge \card{A'} - d$ for all $A'$.
- Sets $S_1, \dots, S_n$ have distinct representatives $\iff \card{\bigcup_{i \in I} S_i} \ge \card{I}$ for all $I$.

## Examples
- [EX04 - When Hall's Condition Fails](../Examples/EX04%20-%20When%20Hall%27s%20Condition%20Fails.md)

See also: [Matchings and Augmenting Paths](Matchings%20and%20Augmenting%20Paths.md)
