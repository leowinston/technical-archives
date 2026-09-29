---
tags: [probability, topic, part-5]
---
# Law of Large Numbers
Back to [[self-study/probability/Index|Index]] · Part 5

## Statement
Let $X_1, X_2, \dots$ be i.i.d. with finite mean $\mu$, and let $\bar X_n = \tfrac1n(X_1 + \cdots + X_n)$. Then
$$
\boxed{\bar X_n \to \mu \quad \text{as } n \to \infty}
$$
The **strong** law says this happens with probability 1. The **weak** law says $\P(\abs{\bar X_n - \mu} > \varepsilon) \to 0$ for every $\varepsilon > 0$.

## Why
$\Var(\bar X_n) = \sigma^2/n \to 0$, so the average concentrates at $\mu$ (by Chebyshev, when $\sigma^2 < \infty$).

## Notes
- **No gambler's fallacy.** Early deviations are **swamped** by later data, not **corrected**. After 10 Heads, the coin is still 50-50.
- The law describes an average over **many independent repetitions**. If you play once, or your wealth compounds, $\mu$ may not describe what happens to you (see [[Limits of Expected Value]]).

## Example
Average of $n$ die rolls $\to 3.5$. See the simulation in [[P26 - Simulation and SPY Returns Lab]].

See also: [[Central Limit Theorem]]
