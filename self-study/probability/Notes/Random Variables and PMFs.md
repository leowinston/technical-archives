---
tags: [probability, topic, part-4]
---
# Random Variables and PMFs
Back to [Index](../Index.md) · Part 4

## Definitions
- A **random variable** is a function $X : S \to \mathbb{R}$. It assigns a number to every outcome.
- $X$ is **discrete** if its **support** (the values $x$ with $\P(X = x) > 0$) is finite or countable.
- The **PMF** is $p_X(x) = \P(X = x)$. It is nonnegative and $\sum_x p_X(x) = 1$.
- The **indicator** of an event is $\Ind_A = 1$ if $A$ occurs and $0$ otherwise.

## Distribution vs variable
A distribution is a **blueprint**. Different random variables can share one. If $X$ indicates Heads and $Y = 1 - X$, both are $\Bern(1/2)$, but $\P(X = Y) = 0$.

## Functions of a random variable
$$
\P(g(X) = y) = \sum_{x \,:\, g(x) = y} \P(X = x)
$$
**Example:** for $2X$, **stretch the support** ($\{0,1,2\} \to \{0,2,4\}$) and keep the probabilities. Multiplying the PMF by 2 is wrong, because it would no longer sum to 1.

See also: [Bernoulli and Binomial](Bernoulli%20and%20Binomial.md), [Expected Value](Expected%20Value.md)
