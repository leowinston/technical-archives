---
tags: [probability, topic, part-2]
---
# Inclusion-Exclusion
Back to [Index](../Index.md) · Part 2

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
- [P08 - de Montmort's Matching Problem](../Problems/P08%20-%20de%20Montmort%27s%20Matching%20Problem.md)
- [P09 - A Die Rolled n Times with a Missing Face](../Problems/P09%20-%20A%20Die%20Rolled%20n%20Times%20with%20a%20Missing%20Face.md)
- [P07 - Chocolate Bars, Gummy Bears, and Bootstrap Samples](../Problems/P07%20-%20Chocolate%20Bars%2C%20Gummy%20Bears%2C%20and%20Bootstrap%20Samples.md) (part d)
