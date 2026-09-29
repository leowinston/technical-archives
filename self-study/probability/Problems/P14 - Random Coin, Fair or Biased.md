---
tags: [probability, problem, part-3]
topics: ["[[Bayes' Rule]]", "[[Conditioning on Extra Evidence]]"]
---
# P14 — Random Coin, Fair or Biased
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> You have one fair coin and one coin that lands Heads with probability $3/4$. You pick one at random and flip it 3 times. It lands Heads all three times.
> (a) What is the probability you picked the fair coin?
> (b) What is the probability that a 4th flip lands Heads?

## Solution
**(a)** Let $F$ be the event that the coin is fair and $A$ the event of three Heads.
$$
\P(F \mid A) = \frac{\P(A \mid F)\P(F)}{\P(A \mid F)\P(F) + \P(A \mid F^c)\P(F^c)}
= \frac{(1/2)^3 \cdot \tfrac12}{(1/2)^3 \cdot \tfrac12 + (3/4)^3 \cdot \tfrac12}
= \frac{8}{8 + 27} = \boxed{\frac{8}{35}} \approx 0.23
$$

**(b)** Given the coin, the flips are independent, so condition on the coin, using the **posterior** from (a):
$$
\P(H_4 \mid A) = \tfrac12 \cdot \tfrac{8}{35} + \tfrac34 \cdot \tfrac{27}{35} = \boxed{\frac{97}{140}} \approx 0.69
$$

> [!warning] Prior vs posterior
> After observing $A$, writing "$\P(A) = 1$ because we know $A$ happened" inside the Bayes calculation is **wrong**. $\P(A)$ and $\P(F)$ are the probabilities *before* the data. The update from $\P(\cdot)$ to $\P(\cdot \mid A)$ is what Bayes' rule computes.

## Related topics
- [[Bayes' Rule]]
- [[Conditioning on Extra Evidence]]
- [[Conditional Independence]]: the flips are independent given the coin, but not unconditionally.
