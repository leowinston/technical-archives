---
tags: [probability, topic, part-1]
---
# Story Proofs
Back to [[self-study/probability/Index|Index]] · Part 1

A **story proof** shows an identity by showing that both sides count the same set.

## Standard identities
| Identity | Story |
|---|---|
| $\sum_{k=0}^n \binom{n}{k} = 2^n$ | Count subsets by their size. |
| $\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$ | $n+1$ people, one is president. Committees of $k$ either exclude or include the president. |
| $\sum_{k=0}^n \binom{n}{k}^2 = \binom{2n}{n}$ | Choose $n$ from $n$ men and $n$ women. Take $k$ men and $n-k$ women, and $\binom{n}{n-k} = \binom{n}{k}$. |
| $n\binom{n-1}{k-1} = k\binom{n}{k}$ | Choose the captain first, or choose the team first. |
| $\sum_{j=k}^{n} \binom{j}{k} = \binom{n+1}{k+1}$ | Line up $n+1$ people by age. Condition on the oldest person in a chosen group of $k+1$ (**hockey stick**). |

## Problems
- [[P05 - Proof of the Binomial Theorem by Induction]]
- [[P06 - Story Proofs for Binomial Identities]]

See also: [[Binomial Coefficients]]
