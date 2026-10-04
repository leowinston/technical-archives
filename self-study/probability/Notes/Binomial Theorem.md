---
tags: [probability, topic, part-1]
---
# Binomial Theorem
Back to [Index](../Index.md) · Part 1

## Statement
For any nonnegative integer $n$,
$$
\boxed{(x+y)^n = \sum_{k=0}^{n} \binom{n}{k} x^k y^{n-k}}
$$

## Story
$(x+y)^n$ is a product of $n$ factors. Each term of the expansion picks $x$ or $y$ from every factor, **without regard to order**. The term $x^k y^{n-k}$ appears once for each choice of which $k$ factors give an $x$, so $\binom{n}{k}$ times.

## Induction (key step)
Assume the result for $m$. Then $(x+y)^{m+1} = (x+y)(x+y)^m$. Shift the index $j = k+1$ in the $x$ part and combine with [Pascal's rule](Story%20Proofs.md), $\binom{m}{j-1} + \binom{m}{j} = \binom{m+1}{j}$. Full proof: [P05 - Proof of the Binomial Theorem by Induction](../Problems/P05%20-%20Proof%20of%20the%20Binomial%20Theorem%20by%20Induction.md).

## Example
$x = y = 1$ gives $\sum_k \binom{n}{k} = 2^n$, the number of subsets.
