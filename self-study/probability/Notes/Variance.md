---
tags: [probability, topic, part-5]
---
# Variance
Back to [Index](../Index.md) · Part 5

## Definition
With $\mu = \E[X]$,
$$
\boxed{\Var(X) = \E\big[(X - \mu)^2\big] = \E[X^2] - (\E[X])^2}, \qquad \SD(X) = \sqrt{\Var(X)}
$$
Variance measures spread around the mean, in squared units.

## Properties
- $\Var(aX + b) = a^2 \Var(X)$. Shifting doesn't change spread.
- **If $X \indep Y$:** $\Var(X + Y) = \Var(X) + \Var(Y)$. Unlike linearity of expectation, this **needs independence** (or at least zero covariance).
- **Sample mean of $n$ i.i.d. draws:** $\Var(\bar X_n) = \sigma^2/n$, so $\SD(\bar X_n) = \sigma/\sqrt{n}$.

## Examples
- $\Var(\Bern(p)) = p(1-p)$ and $\Var(\Bin(n, p)) = np(1-p)$.
- **Fair die:** $\E[X^2] = 91/6$, so $\Var(X) = \tfrac{91}{6} - \tfrac{49}{4} = \tfrac{35}{12} \approx 2.92$.

## Problems
- [P23 - Expected Value of a Die](../Problems/P23%20-%20Expected%20Value%20of%20a%20Die.md)

See also: [Law of Large Numbers](Law%20of%20Large%20Numbers.md), [Central Limit Theorem](Central%20Limit%20Theorem.md)
