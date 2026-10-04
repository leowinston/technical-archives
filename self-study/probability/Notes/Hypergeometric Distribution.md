---
tags: [probability, topic, part-4]
---
# Hypergeometric Distribution
Back to [Index](../Index.md) · Part 4

## Story
An urn has $w$ white and $b$ black balls. Draw $n$ **without replacement**, with all samples equally likely. The number of white balls drawn is $X \sim \HGeom(w, b, n)$.
$$
\boxed{\P(X = k) = \frac{\binom{w}{k}\binom{b}{n-k}}{\binom{w+b}{n}}}, \qquad 0 \le k \le w, \;\; 0 \le n-k \le b
$$
**Key step:** by the naive definition, choose $k$ of the white balls and $n-k$ of the black ones. The PMF sums to 1 by Vandermonde's identity.

## Binomial vs Hypergeometric
Both count successes in $n$ draws.
- **Binomial:** with replacement, so the trials are independent.
- **Hypergeometric:** without replacement, so the trials are dependent. Each white ball drawn makes the next one less likely.

When $w + b$ is large compared to $n$, the two are nearly the same.

## Uses
Capture–recapture (tagged vs untagged animals), card hands (aces vs non-aces), quality inspection.

## Problems
- [P21 - Random Slips of Paper](../Problems/P21%20-%20Random%20Slips%20of%20Paper.md)
