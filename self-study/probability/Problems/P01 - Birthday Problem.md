---
tags: [probability, problem, part-1]
topics: ["[[Sampling With and Without Replacement]]", "[[Naive Definition of Probability]]"]
---
# P01 — Birthday Problem
Back to [Index](../Index.md)

> [!question] Problem
> (a) There are $k$ people in a room. Each birthday is equally likely to be any of 365 days (ignore Feb 29), independently. Find the probability that at least two share a birthday.
> (b) A hash table stores $k$ phone numbers in $n$ locations, each number sent to a uniformly random location, independently. Find the probability that at least one location holds more than one number.

## Strategy
1. Birthdays are **ordered sampling with replacement** from 365 days, so there are $365^k$ equally likely outcomes.
2. Count the complement, "no match", which is sampling **without** replacement.

## Solution
**(a)**
$$
\P(\text{no match}) = \frac{365 \cdot 364 \cdots (365 - k + 1)}{365^k}
\quad\Longrightarrow\quad
\boxed{\P(\text{match}) = 1 - \frac{365 \cdot 364 \cdots (365 - k + 1)}{365^k}}
$$
| $k$ | $\P(\text{match})$ |
|---|---|
| 23 | $0.507$ |
| 57 | $0.990$ |
| 366 | $1$ (pigeonhole) |

**Why it's so high:** 23 people form $\binom{23}{2} = 253$ **pairs**, and any one of them can match.

**(b)** This is the same problem with $365 \to n$:
$$
\P(\text{collision}) = 1 - \frac{n(n-1)\cdots(n-k+1)}{n^k} \quad (k \le n), \qquad = 1 \text{ if } k > n
$$
For example, $k = 10$ numbers in $n = 100$ slots collide with probability $\approx 0.37$.

## Related topics
- [Sampling With and Without Replacement](../Notes/Sampling%20With%20and%20Without%20Replacement.md)
- [Naive Definition of Probability](../Notes/Naive%20Definition%20of%20Probability.md)
