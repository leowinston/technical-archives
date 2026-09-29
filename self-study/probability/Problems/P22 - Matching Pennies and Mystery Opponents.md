---
tags: [probability, problem, part-4]
topics: ["[[Conditional Independence]]", "[[Independence of Random Variables]]"]
---
# P22 — Matching Pennies and Mystery Opponents
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> (a) A and B each flip a fair penny. $X = 1$ if A's penny is Heads and $-1$ otherwise, and $Y$ is defined the same way for B. A wins if the pennies match. Let $Z = XY$. Are $X$ and $Y$ independent? Are they independent given $Z$?
> (b) Two friends, Alice and Bob, are the only people who ever call you. Let $X$ indicate that Alice calls next Friday, $Y$ that Bob does, and $Z$ that exactly one of them calls. $X \indep Y$. Are they independent given $Z = 1$?
> (c) You play two games against one of two twins. Against one you win with probability $1/2$, against the other with probability $3/4$. You don't know which twin it is. Let $X$ and $Y$ indicate wins in games 1 and 2. Are $X$ and $Y$ independent?

## Solution
**(a)** Unconditionally, $X \indep Y$ by assumption. Given $Z = 1$, we know $X = Y$, so $X$ determines $Y$. **Independent, but not conditionally independent.**

**(b)** Given $Z = 1$, $Y = 1 - X$. **Independent, but not conditionally independent.**

**(c)** Let $W$ indicate facing the weaker twin, with $\P(W = 1) = 1/2$. Given the twin, the games are i.i.d. Bernoulli, so **conditionally independent**. Unconditionally,
$$
\P(Y = 1) = \tfrac12\cdot\tfrac12 + \tfrac12\cdot\tfrac34 = \tfrac58,
\qquad
\P(Y = 1 \mid X = 1) = \frac{\tfrac12\left(\tfrac12\right)^2 + \tfrac12\left(\tfrac34\right)^2}{5/8} = \frac{13/32}{5/8} = \tfrac{13}{20} > \tfrac58
$$
Winning game 1 is evidence that you face the weaker twin. **Conditionally independent, but not independent.**

## Related topics
- [[Conditional Independence]]
- [[Independence of Random Variables]]
- [[P14 - Random Coin, Fair or Biased]] (same structure as (c))
