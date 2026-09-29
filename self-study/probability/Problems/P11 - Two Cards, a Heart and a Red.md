---
tags: [probability, problem, part-3]
topics: ["[[Conditional Probability]]"]
---
# P11 — Two Cards, a Heart and a Red
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> Two cards are drawn without replacement from a shuffled deck. $A$: the first card is a heart. $B$: the second card is red. Find $\P(A \mid B)$ and $\P(B \mid A)$.

## Solution
**Joint.** First a heart (13 ways), then a red card from the remaining 25:
$$
\P(A \cap B) = \frac{13 \cdot 25}{52 \cdot 51} = \frac{25}{204}
$$
**Marginals by symmetry.** $\P(A) = \tfrac14$. The second card is equally likely to be any card, so $\P(B) = \tfrac12$.

$$
\P(A \mid B) = \frac{25/204}{1/2} = \boxed{\frac{25}{102}}, \qquad \P(B \mid A) = \frac{25/204}{1/4} = \boxed{\frac{25}{51}}
$$

## Takeaways
- **$\P(A \mid B) \ne \P(B \mid A)$.** Keep track of which event is on which side of the bar.
- **Direct check for $\P(B \mid A)$:** after a heart, 25 of the remaining 51 cards are red.
- Conditioning on the **later** card is fine. Time order doesn't limit what you can condition on.

## Related topics
- [[Conditional Probability]]
