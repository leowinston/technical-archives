---
tags: [probability, topic, part-2]
---
# Axioms of Probability
Back to [[self-study/probability/Index|Index]] · Part 2

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

## Interpretations
- **Frequentist:** the long-run frequency over many repetitions.
- **Bayesian:** a degree of belief. It also applies to one-off events like an election.

Both obey the same axioms.

See also: [[Inclusion-Exclusion]], [[Naive Definition of Probability]]
