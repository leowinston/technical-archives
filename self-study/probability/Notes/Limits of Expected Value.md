---
tags: [probability, topic, part-6]
---
# Limits of Expected Value
Back to [Index](../Index.md) · Part 6

## Ensemble vs time average
$\E[X]$ is the **arithmetic mean over many parallel, independent copies** of a bet (the [Law of Large Numbers](Law%20of%20Large%20Numbers.md)). One person repeating a bet **over time**, with wealth that compounds, experiences the **geometric mean** of the multipliers instead.

## Multiplicative bet
Each round, wealth is multiplied by $1.5$ or $0.6$ with equal probability.
$$
\E[\text{multiplier}] = 1.05, \qquad \text{typical multiplier} = \sqrt{1.5 \cdot 0.6} \approx 0.949
$$
The expected value grows 5% per round, but the typical path **shrinks** about 5% per round. The mean is propped up by a few enormous paths.

## Ruin
Expected value treats a 1% chance of ruin as just 1% of a loss. Ruin is **absorbing**: you can't play on after it. Repeated 100 times,
$$
\P(\text{survive}) = 0.99^{100} \approx 0.37
$$

## Takeaway
Use expected value for many independent, additive bets. When outcomes compound, or ruin is possible, look at growth rates and survival probabilities as well.

## Problems
- [P25 - When Expected Value Misleads](../Problems/P25%20-%20When%20Expected%20Value%20Misleads.md)

See also: [Expected Value](Expected%20Value.md), [Central Limit Theorem](Central%20Limit%20Theorem.md)
