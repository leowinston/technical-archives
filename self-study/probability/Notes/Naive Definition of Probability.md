---
tags: [probability, topic, part-1]
---
# Naive Definition of Probability
Back to [[self-study/probability/Index|Index]] · Part 1

## Definition
For a finite sample space where every outcome is **equally likely**,
$$
\boxed{\Pnaive(A) = \frac{\card{A}}{\card{S}} = \frac{\text{favorable outcomes}}{\text{total outcomes}}}
$$

## When it applies
- **Symmetry:** fair coins, fair dice, well-shuffled decks.
- **By design:** a simple random sample, where every subset of size $k$ is equally likely.
- It needs **equal mass per pebble**. Don't assume it. "There is or isn't life on Mars" does not make the probability $1/2$.

## Complements
$$
\Pnaive(A^c) = \frac{\card{S} - \card{A}}{\card{S}} = 1 - \Pnaive(A)
$$
For "at least one", count the complement "none".

## Example
$\P(\text{at least one 6 in 6 rolls}) = 1 - \dfrac{5^6}{6^6} \approx 0.665$

## Problems
- [[P01 - Birthday Problem]]
- [[P02 - Full House and the Newton-Pepys Problem]]
- [[P10 - Mixed Practice Comparisons]]

See also: [[Axioms of Probability]], which drops the equal-likelihood requirement
