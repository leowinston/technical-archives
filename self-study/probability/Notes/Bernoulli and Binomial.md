---
tags: [probability, topic, part-4]
---
# Bernoulli and Binomial
Back to [[self-study/probability/Index|Index]] · Part 4

## Bernoulli
$X \sim \Bern(p)$ ("$X$ is distributed as Bernoulli $p$") if
$$
\P(X = 1) = p, \qquad \P(X = 0) = 1 - p
$$
It models one trial with success probability $p$. Every indicator $\Ind_A$ is $\Bern(\P(A))$.

## Binomial
**Story:** $X$ counts the successes in $n$ **independent** $\Bern(p)$ trials. Then $X \sim \Bin(n, p)$ with
$$
\boxed{\P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}, \qquad k = 0, 1, \dots, n}
$$
The $\binom{n}{k}$ counts which trials succeed, and $p^k(1-p)^{n-k}$ is the probability of any one such sequence.

## Facts
- $n - X \sim \Bin(n, 1-p)$, counting failures.
- $X = I_1 + \cdots + I_n$, a sum of indicators, so $\E[X] = np$.
- **Shape:** $\Bin(10, \tfrac12)$ is symmetric about 5. $\Bin(10, \tfrac18)$ peaks at 1. $\Bin(9, \tfrac45)$ peaks at 7 and 8.

## Problems
- [[P21 - Random Slips of Paper]]
- [[P20 - Even Number of Successes]]

See also: [[Hypergeometric Distribution]]
