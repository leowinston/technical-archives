---
tags: [probability, topic, part-4]
---
# Discrete Uniform Distribution
Back to [Index](../Index.md) · Part 4

## Story
Pick a number uniformly at random from a finite, nonempty set $C$. Then $X \sim \DUnif(C)$ and
$$
\boxed{\P(X = x) = \frac{1}{\card{C}} \quad (x \in C), \qquad \P(X \in A) = \frac{\card{A}}{\card{C}} \quad (A \subseteq C)}
$$
This is the [Naive Definition of Probability](Naive%20Definition%20of%20Probability.md) in random-variable language.

## Example
Draw 5 of 100 numbered slips **without** replacement. The value on the $j$-th slip is still $\DUnif(1, \dots, 100)$ by symmetry. No slip "prefers" position $j$.

## Problems
- [P21 - Random Slips of Paper](../Problems/P21%20-%20Random%20Slips%20of%20Paper.md)
- [P23 - Expected Value of a Die](../Problems/P23%20-%20Expected%20Value%20of%20a%20Die.md)
