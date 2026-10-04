---
tags: [probability, topic, part-3]
---
# Conditioning on Extra Evidence
Back to [Index](../Index.md) · Part 3

> Conditional probabilities are probabilities, and all probabilities are conditional.

Every "unconditional" $\P(A)$ quietly conditions on background knowledge. Conditioning on an extra event $E$ keeps every rule intact.

## Bayes and LOTP with extra conditioning
$$
\P(A \mid B, E) = \frac{\P(B \mid A, E)\,\P(A \mid E)}{\P(B \mid E)}, \qquad \P(B \mid E) = \sum_i \P(B \mid A_i, E)\,\P(A_i \mid E)
$$

## Sequential updating
You get the same answer whether you condition on all the evidence at once or one piece at a time, using each posterior as the next prior.

## Example
One fair coin and one coin with $\P(H) = 3/4$. Pick one at random and flip it 3 times: all Heads. Then $\P(\text{fair} \mid HHH) = 8/35$. For a 4th flip, condition on which coin you have:
$$
\P(H_4 \mid HHH) = \tfrac12 \cdot \tfrac{8}{35} + \tfrac34 \cdot \tfrac{27}{35} = \tfrac{97}{140}
$$

## Problems
- [P14 - Random Coin, Fair or Biased](../Problems/P14%20-%20Random%20Coin%2C%20Fair%20or%20Biased.md)
- [P15 - Six-Fingered Man](../Problems/P15%20-%20Six-Fingered%20Man.md)
