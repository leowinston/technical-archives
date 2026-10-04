---
tags: [probability, topic, part-3]
---
# Law of Total Probability
Back to [Index](../Index.md) · Part 3

## Statement
If $A_1, \dots, A_n$ **partition** $S$ (disjoint, with union $S$) and each $\P(A_i) > 0$, then
$$
\boxed{\P(B) = \sum_{i=1}^n \P(B \mid A_i)\,\P(A_i)}
$$
**Key step:** $B = (B \cap A_1) \cup \cdots \cup (B \cap A_n)$ is a disjoint union, and $\P(B \cap A_i) = \P(B \mid A_i)\P(A_i)$.

## Using it
- $\P(B)$ is a **weighted average** of the conditional probabilities, weighted by the $\P(A_i)$.
- Choose the partition that makes each $\P(B \mid A_i)$ easy. A good partition splits one hard problem into easy pieces.
- The simplest partition is $\{A, A^c\}$: $\P(B) = \P(B \mid A)\P(A) + \P(B \mid A^c)\P(A^c)$.

## Example
Pick one of three urns at random. The fractions of green balls are $\tfrac25, \tfrac35, \tfrac15$. Then
$$
\P(\text{green}) = \tfrac13\left(\tfrac25 + \tfrac35 + \tfrac15\right) = \tfrac25
$$

## Problems
- [P19 - Urn Chosen at Random](../Problems/P19%20-%20Urn%20Chosen%20at%20Random.md)
- [P16 - Monty Hall](../Problems/P16%20-%20Monty%20Hall.md)
- [P20 - Even Number of Successes](../Problems/P20%20-%20Even%20Number%20of%20Successes.md)
- [P12 - Recession and Falling Stocks](../Problems/P12%20-%20Recession%20and%20Falling%20Stocks.md)

See also: [Bayes' Rule](Bayes%27%20Rule.md)
