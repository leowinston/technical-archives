---
tags: [probability, topic, part-5]
---
# Central Limit Theorem
Back to [[self-study/probability/Index|Index]] · Part 5

## Statement
Let $X_1, X_2, \dots$ be **i.i.d.** with mean $\mu$ and **finite** variance $\sigma^2$. Then
$$
\boxed{\frac{\bar X_n - \mu}{\sigma/\sqrt{n}} \;\to\; \Normal(0, 1) \text{ in distribution}}
$$
Equivalently, $X_1 + \cdots + X_n \approx \Normal(n\mu, n\sigma^2)$ for large $n$. Many independent random pieces add up to a bell curve, whatever the shape of each piece.

## The assumptions matter
1. **Independence.** Each piece must not feed on the others.
2. **Finite, stable variance.** No single piece can dominate, and the spread can't change over time.

## Markets break both
- **Clustering:** volatile days follow volatile days, so the variance is not stable.
- **Cascades:** a sell-off triggers more selling, so the pieces are not independent.

The result is **fat tails**. A normal model says a 3-SD day has probability about $0.27\%$, but real return series show such days far more often.

## Problems
- [[P26 - Simulation and SPY Returns Lab]]

See also: [[Law of Large Numbers]], [[Variance]]
