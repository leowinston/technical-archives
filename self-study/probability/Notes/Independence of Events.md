---
tags: [probability, topic, part-3]
---
# Independence of Events
Back to [Index](../Index.md) · Part 3

## Definition
$$
\boxed{A \indep B \iff \P(A \cap B) = \P(A)\,\P(B)}
$$
If $\P(B) > 0$, this is the same as $\P(A \mid B) = \P(A)$: learning $B$ tells you nothing about $A$. The relation is symmetric.

## Facts
- **Independent is not the same as disjoint.** If $A \cap B = \emptyset$ and both have positive probability, then knowing $A$ happened tells you $B$ didn't, so they are dependent.
- If $A \indep B$, then $A \indep B^c$, $A^c \indep B$, and $A^c \indep B^c$.

## Three events
$A$, $B$, $C$ are independent if all of the following hold:
$$
\P(A \cap B) = \P(A)\P(B), \quad \P(A \cap C) = \P(A)\P(C), \quad \P(B \cap C) = \P(B)\P(C), \quad \P(A \cap B \cap C) = \P(A)\P(B)\P(C)
$$
- **Pairwise is not enough.** With two fair coins, let $A$ = first is H, $B$ = second is H, and $C$ = both match. Each pair is independent, but $\P(A \cap B \cap C) = \tfrac14 \ne \tfrac18$.
- **The triple condition alone is not enough either.** If $\P(A) = 0$, it holds automatically and says nothing about $B$ and $C$.

## Problems
- [P20 - Even Number of Successes](../Problems/P20%20-%20Even%20Number%20of%20Successes.md)

See also: [Conditional Independence](Conditional%20Independence.md), [Independence of Random Variables](Independence%20of%20Random%20Variables.md)
