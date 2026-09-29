---
tags: [probability, topic, part-3]
---
# Conditional Independence
Back to [[self-study/probability/Index|Index]] · Part 3

## Definition
$A$ and $B$ are **conditionally independent given $E$** if
$$
\P(A \cap B \mid E) = \P(A \mid E)\,\P(B \mid E)
$$

## Neither implies the other
| | Example |
|---|---|
| Independent, **not** conditionally independent | Alice and Bob each call you independently. Given that **exactly one** called, learning it was Alice tells you it wasn't Bob. |
| Conditionally independent, **not** independent | You play two games against one of two twins, one of whom is much stronger. Given which twin, the games are independent. Without knowing, winning game 1 makes it more likely you face the weaker twin, so it raises $\P(\text{win game } 2)$. |

## Example
A baby cries if and only if it is hungry ($H$) or tired ($T$), with $H \indep T$. Given crying $C$,
$$
\P(H, T \mid C) = \frac{ht}{c} < \frac{ht}{c^2} = \P(H \mid C)\,\P(T \mid C), \qquad c = h + t - ht
$$
If the baby is crying and not hungry, it must be tired, so $H$ and $T$ are dependent given $C$.

## Problems
- [[P22 - Matching Pennies and Mystery Opponents]]

See also: [[Independence of Events]]
