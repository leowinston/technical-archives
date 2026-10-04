---
tags: [probability, topic, part-1]
---
# Sampling With and Without Replacement
Back to [Index](../Index.md) · Part 1

Choose $k$ objects from $n$, one at a time.

## The four cases
| | Order matters | Order doesn't matter |
|---|---|---|
| **With replacement** | $n^k$ | $\binom{n+k-1}{k}$ |
| **Without replacement** | $n(n-1)\cdots(n-k+1)$ | $\binom{n}{k}$ |

- Without replacement and $k > n$ gives $0$.
- $k = n$ without replacement gives the **permutations**, $n!$.
- Only the ordered cases have **equally likely** outcomes under random sampling. The unordered with-replacement count ([Stars and Bars](Stars%20and%20Bars.md)) does not, so don't use it with the naive definition.

## Example
Birthdays of $k$ people: $365^k$ possible assignments, and $365 \cdot 364 \cdots (365-k+1)$ of them have no shared birthday.
$$
\P(\text{match}) = 1 - \frac{365 \cdot 364 \cdots (365-k+1)}{365^k}, \qquad \text{already} > \tfrac12 \text{ at } k = 23
$$

## Problems
- [P01 - Birthday Problem](../Problems/P01%20-%20Birthday%20Problem.md)
- [P07 - Chocolate Bars, Gummy Bears, and Bootstrap Samples](../Problems/P07%20-%20Chocolate%20Bars%2C%20Gummy%20Bears%2C%20and%20Bootstrap%20Samples.md)

See also: [Multiplication Rule](Multiplication%20Rule.md), [Binomial Coefficients](Binomial%20Coefficients.md)
