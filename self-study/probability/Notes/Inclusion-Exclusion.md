---
tags: [probability, topic, part-2]
---
# Inclusion-Exclusion
Back to [[self-study/probability/Index|Index]] · Part 2

## Formula
$$
\P(A \cup B \cup C) = \P(A) + \P(B) + \P(C) - \P(A \cap B) - \P(A \cap C) - \P(B \cap C) + \P(A \cap B \cap C)
$$
$$
\boxed{\P\!\left(\bigcup_{i=1}^n A_i\right) = \sum_i \P(A_i) - \sum_{i<j} \P(A_i \cap A_j) + \sum_{i<j<k} \P(A_i \cap A_j \cap A_k) - \cdots + (-1)^{n+1}\P(A_1 \cap \cdots \cap A_n)}
$$

## Intuition
In the three-circle Venn diagram, adding the singles counts each pairwise overlap twice. Subtracting the pairs removes the triple center completely, so add it back once.

## When to use it
Use it for "at least one of the $A_i$" when the intersections are easy to compute, especially **by symmetry**, when every $k$-fold intersection has the same probability.

## Example: de Montmort
Shuffle $n$ labeled cards. You win if card $i$ lands in position $i$ for some $i$. Then $\P(A_i) = 1/n$, since card $i$ is equally likely to be in any position, and
$$
\P(\text{win}) = 1 - \frac{1}{2!} + \frac{1}{3!} - \cdots + (-1)^{n+1}\frac{1}{n!} \;\to\; 1 - \frac1e \approx 0.63
$$

## Problems
- [[P08 - de Montmort's Matching Problem]]
- [[P09 - A Die Rolled n Times with a Missing Face]]
- [[P07 - Chocolate Bars, Gummy Bears, and Bootstrap Samples]] (part d)
