---
tags: [probability, problem, part-6]
topics: ["[[Limits of Expected Value]]"]
---
# P25 — When Expected Value Misleads
Back to [Index](../Index.md)

> [!question] Problem
> Each round, your wealth is multiplied by $1.5$ (Heads) or $0.6$ (Tails) with a fair coin.
> (a) Find the expected multiplier per round and $\E[W_{100}]$, starting from $W_0 = 1$.
> (b) Find the median wealth after 100 rounds.
> (c) A different bet has a 1% chance of total ruin each time. What is the chance of surviving 100 independent rounds?

## Solution
**(a)** $\E[\text{multiplier}] = \tfrac12(1.5) + \tfrac12(0.6) = 1.05$. The rounds are independent, so
$$
\E[W_{100}] = 1.05^{100} \approx \boxed{131.5}
$$

**(b)** The median path has 50 Heads and 50 Tails:
$$
W_{100} = 1.5^{50}\,0.6^{50} = 0.9^{50} \approx \boxed{0.005}
$$
The typical player loses about 99.5%. The per-round **geometric** growth is $\sqrt{0.9} \approx 0.949$: a 5% loss per round, even though the arithmetic mean is a 5% gain.

**(c)**
$$
0.99^{100} \approx \boxed{0.37}
$$
A "small" per-round risk is likely to wipe you out eventually.

## Why they disagree
- $\E[W_{100}]$ averages over **many parallel players**. A handful of extremely lucky paths carry the mean.
- One player moving **through time** experiences the product of multipliers. By the [Law of Large Numbers](../Notes/Law%20of%20Large%20Numbers.md) applied to $\log W$, $\tfrac1n\log W_n \to \E[\log(\text{multiplier})] = \tfrac12\ln 0.9 < 0$.
- Expected value treats ruin as one more bad outcome, weighted by its probability. In reality, ruin ends the game.

## Related topics
- [Limits of Expected Value](../Notes/Limits%20of%20Expected%20Value.md)
- [Expected Value](../Notes/Expected%20Value.md)
- [Law of Large Numbers](../Notes/Law%20of%20Large%20Numbers.md)
