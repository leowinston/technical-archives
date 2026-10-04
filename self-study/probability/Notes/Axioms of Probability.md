---
tags: [probability, topic, part-2]
---
# Axioms of Probability
Back to [Index](../Index.md) · Part 2

## Definition
A **probability space** is a sample space $S$ together with a function $\P$ that sends each event $A \subseteq S$ to $\P(A) \in [0, 1]$, such that
1. $\P(\emptyset) = 0$ and $\P(S) = 1$
2. If $A_1, A_2, \dots$ are **disjoint**, then $\P\!\left(\bigcup_j A_j\right) = \sum_j \P(A_j)$

Pebbles may now have **unequal** mass, or even be "mud" spread over a region. The total mass is always 1.

## Consequences
$$
\begin{aligned}
\P(A^c) &= 1 - \P(A) \\
A \subseteq B &\implies \P(A) \le \P(B) \\
\P(A \cup B) &= \P(A) + \P(B) - \P(A \cap B)
\end{aligned}
$$
**Key step for the complement:** $A$ and $A^c$ are disjoint with union $S$, so $\P(A) + \P(A^c) = 1$.
**For the union:** write $A \cup B = A \cup (B \cap A^c)$, which is a disjoint union.

## Measure-theoretic version
In measure theory a probability space is a triple $(S, \mathscr F, \P)$, where $\mathscr F$ is a $\sigma$-field of events and $\P$ is a **measure** with $\P(S) = 1$ (see [Measures, Semirings, and Rings](../../ergodic-theory/Theory/Measures%2C%20Semirings%2C%20and%20Rings.md)). Axiom 2 above is exactly $\sigma$-additivity.
- For finite or countable $S$, take $\mathscr F$ = all subsets. Nothing changes.
- For an uncountable $S$, such as infinite sequences of coin flips, not every subset can be given a consistent probability. So $\P$ is defined only on $\mathscr F$ (see [Sequence Spaces and Sigma-Fields](../../ergodic-theory/Theory/Sequence%20Spaces%20and%20Sigma-Fields.md)).
- $\mathscr F$ is closed under complements and countable unions. That is what makes $\P(A^c)$ and $\P(A \cup B)$ in the consequences well-defined.

## Interpretations
- **Frequentist:** the long-run frequency over many repetitions.
- **Bayesian:** a degree of belief. It also applies to one-off events like an election.

Both obey the same axioms.

See also: [Inclusion-Exclusion](Inclusion-Exclusion.md), [Naive Definition of Probability](Naive%20Definition%20of%20Probability.md)
