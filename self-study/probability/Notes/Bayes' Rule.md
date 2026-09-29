---
tags: [probability, topic, part-3]
---
# Bayes' Rule
Back to [[self-study/probability/Index|Index]] · Part 3

## Statement
Bayes' rule reverses a conditional probability:
$$
\boxed{\P(A \mid B) = \frac{\P(B \mid A)\,\P(A)}{\P(B)}}
$$
It follows from writing $\P(A \cap B)$ both ways: $\P(A \mid B)\P(B) = \P(B \mid A)\P(A)$. The denominator usually comes from the [[Law of Total Probability]].

## Odds form
With $\text{odds}(A) = \P(A)/\P(A^c)$,
$$
\frac{\P(A \mid B)}{\P(A^c \mid B)} = \underbrace{\frac{\P(B \mid A)}{\P(B \mid A^c)}}_{\text{likelihood ratio}} \cdot \frac{\P(A)}{\P(A^c)}, \qquad \P(A) = \frac{\text{odds}(A)}{1 + \text{odds}(A)}
$$

## Example
Recession with probability 0.1. Stocks fall with probability 0.9 in a recession and 0.3 otherwise.
$$
\P(\text{rec} \mid \text{fall}) = \frac{0.9 \cdot 0.1}{0.9 \cdot 0.1 + 0.3 \cdot 0.9} = \frac{0.09}{0.36} = 0.25
$$
Details: [[P12 - Recession and Falling Stocks]].

## Problems
- [[P14 - Random Coin, Fair or Biased]]
- [[P15 - Six-Fingered Man]]
- [[P17 - Defense Attorney's Fallacy]]
- [[P18 - Spam Filter]]
