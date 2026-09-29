---
tags: [probability, problem, part-1]
topics: ["[[Binomial Coefficients]]", "[[Naive Definition of Probability]]"]
---
# P10 — Mixed Practice Comparisons
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> Fill in each blank with $=$, $<$, or $>$ and explain.
> (a) ways to choose 5 of 10 people ___ ways to choose 6 of 10
> (b) ways to split 10 people into 2 teams of 5 ___ ways to split 10 into a team of 6 and a team of 4
> (c) $\P$(all 3 people in a group were born on Jan 1) ___ $\P$(one each was born on Jan 1, 2, 3)
> (d) Toss a fair coin until $HH$ or $TH$ appears. Martin wins if $HH$ comes first. $\P(\text{Martin wins})$ ___ $1/2$

## Solution
**(a) $>$.** $\binom{10}{5} = 252 > 210 = \binom{10}{6}$. $\binom{n}{k}$ peaks at $k = n/2$.

**(b) $<$.** The two 5-teams have no labels, so there are $\binom{10}{5}/2 = 126$ splits. For 6 and 4, the teams are distinguishable by size: $\binom{10}{6} = 210$.

**(c) $<$.** All on Jan 1 is one outcome, $1/365^3$. One on each of Jan 1–3 can happen in $3! = 6$ orders, $6/365^3$.

**(d) $<$.** As soon as a $T$ appears, $TH$ must come before $HH$: the first $H$ after that $T$ completes $TH$. So Martin wins only if the first two tosses are $HH$:
$$
\P(\text{Martin wins}) = \tfrac14 < \tfrac12
$$

## Related topics
- [[Binomial Coefficients]]
- [[Naive Definition of Probability]]
