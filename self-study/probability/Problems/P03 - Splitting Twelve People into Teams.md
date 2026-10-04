---
tags: [probability, problem, part-1]
topics: ["[[Binomial Coefficients]]"]
---
# P03 — Splitting Twelve People into Teams
Back to [Index](../Index.md)

> [!question] Problem
> (a) How many ways are there to split 12 people into 3 teams, one with 2 people and two with 5 people each?
> (b) How many ways are there to split 12 people into 3 teams of 4?

## Strategy
Line the 12 people up and cut the line into blocks. Then divide out the orderings that don't change the teams: the order **within** each team, and the order **of** teams that have the same size.

## Solution
**(a)** Choose the pair, then one team of 5 from the remaining 10. The two 5-teams have no labels, so swapping them gives the same split. Divide by $2!$.
$$
\binom{12}{2}\binom{10}{5}\cdot\frac12 = \frac{12!}{2!\,5!\,5!}\cdot\frac{1}{2!} = \boxed{8316}
$$

**(b)** Arrange all 12 people ($12!$), divide by $4!$ for the order within each team, and divide by $3!$ for the order of the three equal-sized teams:
$$
\frac{12!}{4!\,4!\,4!\,3!} = \boxed{5775}
$$

> [!tip] Check
> In (a), only the two teams of the **same size** can be swapped. The 2-person team is always distinguishable, so we divide by $2!$, not $3!$.

## Related topics
- [Binomial Coefficients](../Notes/Binomial%20Coefficients.md) (adjusting for overcounting)
