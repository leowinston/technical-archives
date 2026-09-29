---
tags: [probability, problem, part-1]
topics: ["[[Binomial Coefficients]]", "[[Multiplication Rule]]"]
---
# P04 — Lattice Paths
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> Each step goes one unit up or one unit right.
> (a) How many paths go from $(0,0)$ to $(110, 111)$?
> (b) How many paths go from $(0,0)$ to $(210, 211)$ and pass through $(110, 111)$?

## Solution
**(a)** Every path uses exactly $110$ right moves ($R$) and $111$ up moves ($U$), so $221$ moves in total. A path is a string of length 221 with 110 $R$'s. Choose which positions are $R$:
$$
\boxed{\binom{221}{110}} = \frac{221!}{110!\,111!}
$$

**(b)** Split the path at $(110, 111)$. From there to $(210, 211)$ takes 100 right and 100 up moves. By the multiplication rule,
$$
\boxed{\binom{221}{110}\binom{200}{100}}
$$

## Related topics
- [[Binomial Coefficients]]
- [[Multiplication Rule]]
