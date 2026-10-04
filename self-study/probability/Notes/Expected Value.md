---
tags: [probability, topic, part-5]
---
# Expected Value
Back to [Index](../Index.md) · Part 5

## Definition
For discrete $X$,
$$
\boxed{\E[X] = \sum_x x\,\P(X = x)}
$$
It is the average of the values, **weighted by their probabilities**.

## Properties
- **Linearity:** $\E[aX + bY + c] = a\E[X] + b\E[Y] + c$. This holds **even when $X$ and $Y$ are dependent**.
- **Fundamental bridge:** $\E[\Ind_A] = \P(A)$. Write a count as a sum of indicators, then add their probabilities. For example, $\E[\Bin(n, p)] = np$.

## Example
Fair die: $\E[X] = \dfrac{1 + 2 + \cdots + 6}{6} = 3.5$.
- **Shortcut:** for equally likely **evenly spaced** values, the mean is $\dfrac{\text{min} + \text{max}}{2} = \dfrac{1 + 6}{2}$.
- The shortcut fails for uneven values. If the 6 is misread as a 9, the faces are $1, 2, 3, 4, 5, 9$, and $\E[X] = 24/6 = 4$, not $(1 + 9)/2 = 5$.

## Problems
- [P23 - Expected Value of a Die](../Problems/P23%20-%20Expected%20Value%20of%20a%20Die.md)
- [P24 - Expected Present Value of a Risky Company](../Problems/P24%20-%20Expected%20Present%20Value%20of%20a%20Risky%20Company.md)

See also: [Variance](Variance.md), [Law of Large Numbers](Law%20of%20Large%20Numbers.md), [Limits of Expected Value](Limits%20of%20Expected%20Value.md)
