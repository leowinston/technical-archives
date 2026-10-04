---
tags: [probability, problem, part-3]
topics: ["[[Law of Total Probability]]"]
---
# P19 — Urn Chosen at Random
Back to [Index](../Index.md)

> [!question] Problem
> Three urns each hold 5 balls. Urn 1 has 2 green, urn 2 has 3 green, and urn 3 has 1 green. Pick an urn uniformly at random and draw one ball. Let $X = 1$ if it is green and $X = 0$ otherwise.
> (a) Find $\P(X = 1)$ and $\E[X]$.
> (b) Given that the ball is green, what is the probability it came from urn 2?

## Solution
**(a)** Use LOTP, partitioning by urn:
$$
\P(X = 1) = \tfrac25\cdot\tfrac13 + \tfrac35\cdot\tfrac13 + \tfrac15\cdot\tfrac13 = \tfrac{2 + 3 + 1}{15} = \boxed{\tfrac{6}{15} = \tfrac25}
$$
$X$ is an indicator, so $X \sim \Bern(2/5)$ and $\E[X] = \P(X = 1) = \tfrac25$.

**(b)** By Bayes,
$$
\P(U_2 \mid X = 1) = \frac{\tfrac35 \cdot \tfrac13}{\tfrac25} = \boxed{\tfrac12}
$$
Of the 6 equally likely green "slots", 3 are in urn 2.

## Takeaway
LOTP is a weighted average. Because the urns are equally likely and equally sized, $\P(\text{green})$ is just the overall fraction of green balls, $6/15$.

## Related topics
- [Law of Total Probability](../Notes/Law%20of%20Total%20Probability.md)
- [Bayes' Rule](../Notes/Bayes%27%20Rule.md)
- [Bernoulli and Binomial](../Notes/Bernoulli%20and%20Binomial.md)
