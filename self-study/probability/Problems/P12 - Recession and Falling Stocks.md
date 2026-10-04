---
tags: [probability, problem, part-3]
topics: ["[[Bayes' Rule]]", "[[Law of Total Probability]]"]
---
# P12 — Recession and Falling Stocks
Back to [Index](../Index.md)

> [!question] Problem
> A recession ($R$) happens with probability $0.1$. In a recession, stocks fall ($F$) with probability $0.9$. Otherwise they fall with probability $0.3$. Stocks just fell. What is the probability that a recession is underway?

## Strategy
We know $\P(F \mid R)$ but want $\P(R \mid F)$, so reverse it with Bayes. The denominator comes from LOTP over $\{R, R^c\}$.

## Solution
**LOTP.**
$$
\P(F) = \underbrace{0.9 \cdot 0.1}_{0.09} + \underbrace{0.3 \cdot 0.9}_{0.27} = 0.36
$$
**Bayes.**
$$
\P(R \mid F) = \frac{\P(F \mid R)\P(R)}{\P(F)} = \frac{0.09}{0.36} = \boxed{0.25}
$$

## Reading the answer
- A fall makes a recession **2.5 times** more likely than the prior 0.1, but still unlikely.
- Most falls ($0.27$ of the $0.36$) happen outside recessions, because non-recession periods are so much more common. This is the **base rate** effect.
- **Odds form:** prior odds $1:9$, likelihood ratio $0.9/0.3 = 3$, posterior odds $3:9 = 1:3$, so $\P = 1/4$. ✓

## Related topics
- [Bayes' Rule](../Notes/Bayes%27%20Rule.md)
- [Law of Total Probability](../Notes/Law%20of%20Total%20Probability.md)
