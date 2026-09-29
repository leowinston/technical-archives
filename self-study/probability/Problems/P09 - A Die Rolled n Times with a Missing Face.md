---
tags: [probability, problem, part-2]
topics: ["[[Inclusion-Exclusion]]"]
---
# P09 — A Die Rolled $n$ Times with a Missing Face
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> A fair die is rolled $n$ times. What is the probability that at least one of the 6 faces never appears?

## Strategy
Let $A_i$ be the event that face $i$ never appears. We want $\P(A_1 \cup \cdots \cup A_6)$. Intersections are easy: if $j$ given faces are all missing, every roll lands on the other $6 - j$ faces.

## Solution
$$
\P(A_{i_1} \cap \cdots \cap A_{i_j}) = \left(\frac{6-j}{6}\right)^n
$$
There are $\binom6j$ ways to choose the $j$ missing faces. The $j = 6$ term is 0, since some face must appear. So
$$
\boxed{\P(\text{some face missing}) = \sum_{j=1}^{5}(-1)^{j+1}\binom6j\left(1 - \frac j6\right)^n}
= 6\left(\tfrac56\right)^n - 15\left(\tfrac46\right)^n + 20\left(\tfrac36\right)^n - 15\left(\tfrac26\right)^n + 6\left(\tfrac16\right)^n
$$
The first term alone, $6(5/6)^n = 6 \cdot 5^n/6^n$, is a quick upper bound.

| $n$ | 6 | 10 | 13 | 20 |
|---|---|---|---|---|
| $\P$ | 0.985 | 0.728 | 0.486 | 0.152 |

So you need about 13 rolls before seeing all six faces is more likely than not.

## Related topics
- [[Inclusion-Exclusion]]
- [[Naive Definition of Probability]]
