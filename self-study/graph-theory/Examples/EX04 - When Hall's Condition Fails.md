---
tags: [graph-theory, example, ch-2]
source: Constructed from ✎ the a₁a₂a₃ / b₁…b₅ sketch under Hall's Theorem (p. 15)
topics: ["[[Hall's Theorem]]", "[[Matchings and Augmenting Paths]]"]
---
# EX04 — When Hall's Condition Fails
Back to [Index](../Index.md)

> [!question] Problem
> $A = \{a_1, a_2, a_3\}$ and $B = \{b_1, \dots, b_5\}$.
> (a) Each $a_i$ likes only $b_1$ and $b_2$. Is there a matching saturating $A$?
> (b) Now $N(a_1) = \{b_1, b_2\}$, $N(a_2) = \{b_1\}$, $N(a_3) = \{b_2, b_3\}$. Start from $M = \{a_1b_1, a_3b_2\}$ and find a matching saturating $A$.

## Strategy
1. Check Hall's condition $\card{N(A')} \ge \card{A'}$ on the subsets.
2. If $M$ leaves some $a$ unsaturated, look for an $M$-augmenting path starting at $a$.

## Solution
**(a)** $N(A) = \{b_1, b_2\}$, so $\card{N(A)} = 2 < 3 = \card{A}$. Hall fails, and there is **no** matching saturating $A$. ✎ Two choosers can be matched ($a_1b_1$, $a_2b_2$), but then $a_3$ has no match. The likes are "too concentrated", and $b_3, b_4, b_5$ go unused.

**(b)** Check Hall first:

| $A'$ | $N(A')$ | OK? |
|---|---|---|
| singletons | sizes $2, 1, 2$ | yes |
| $\{a_1, a_2\}$ | $\{b_1, b_2\}$ | yes |
| $\{a_1, a_3\}$, $\{a_2, a_3\}$ | size $3$ | yes |
| $A$ | $\{b_1, b_2, b_3\}$ | yes |

$a_2$ is unsaturated. Follow the alternating path
$$
a_2 \xrightarrow{\notin M} b_1 \xrightarrow{\in M} a_1 \xrightarrow{\notin M} b_2 \xrightarrow{\in M} a_3 \xrightarrow{\notin M} b_3 .
$$
Both ends are unsaturated, so it is $M$-augmenting. Flip it:
$$
\boxed{M' = \{a_2b_1,\ a_1b_2,\ a_3b_3\}}
$$

## Takeaways
- Hall's condition fails exactly when some group of choosers shares too few options.
- The proof of Hall's theorem is this example run in reverse: no augmenting path means a violating set $A'$.

## Related topics
- [Hall's Theorem](../Theory/Hall%27s%20Theorem.md)
- [Matchings and Augmenting Paths](../Theory/Matchings%20and%20Augmenting%20Paths.md)
