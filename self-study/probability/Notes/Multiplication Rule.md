---
tags: [probability, topic, part-1]
---
# Multiplication Rule
Back to [Index](../Index.md) · Part 1

## Statement
If experiment 1 has $a$ outcomes and, **for each** of them, experiment 2 has $b$ outcomes, then the compound experiment has
$$
\boxed{a \cdot b \text{ outcomes}}
$$
A tree diagram is the picture: $a$ branches, each splitting into $b$.

## Notes
- The order you make the choices doesn't matter: cone then flavor or flavor then cone, $2 \cdot 3 = 3 \cdot 2 = 6$ options.
- **Subsets:** each of $n$ elements is either in or out, so a set of size $n$ has $2^n$ subsets. The power set of $A$ has $2^{\card{A}}$ elements, including $\emptyset$ and $A$.
- **Trap:** ordered vs unordered. Two cones from 6 options gives $6^2 = 36$ ordered pairs, but $\binom{6}{2} + 6 = 21$ unordered ones, **not** $36/2 = 18$. The pairs $(x, x)$ are counted only once.

## Problems
- [P04 - Lattice Paths](../Problems/P04%20-%20Lattice%20Paths.md)

See also: [Sampling With and Without Replacement](Sampling%20With%20and%20Without%20Replacement.md), [Binomial Coefficients](Binomial%20Coefficients.md)
