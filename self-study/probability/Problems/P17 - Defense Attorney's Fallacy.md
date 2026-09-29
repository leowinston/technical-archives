---
tags: [probability, problem, part-3]
topics: ["[[Bayes' Rule]]"]
---
# P17 — Defense Attorney's Fallacy
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> A woman was murdered, and her husband is on trial. He had a history of abusing her. The defense argues that abuse is irrelevant, since only 1 in 10,000 abusive husbands goes on to murder his wife. Assume:
> - 1 in 10 husbands abuse their wives
> - 1 in 5 murdered wives are murdered by their husbands
> - 50% of husbands who murder their wives abused them beforehand
>
> Given all the evidence, what is the probability that the husband is guilty?

## Strategy
The defense computes $\P(\text{murder} \mid \text{abuse})$. But we **know the wife was murdered**, so the relevant quantity is $\P(G \mid A, M)$: guilt given abuse **and** murder. Condition on $M$ throughout.

## Solution
Let $M$ be the event that the wife was murdered, $G$ that the husband did it, and $A$ that he abused her.
$$
\P(G \mid M) = 0.2, \qquad \P(A \mid G, M) = 0.5, \qquad \P(A \mid G^c, M) = 0.1
$$
For the last one: if the husband is innocent, his abuse has nothing to do with the murder, so the base rate applies.
$$
\P(G \mid A, M) = \frac{0.5 \cdot 0.2}{0.5 \cdot 0.2 + 0.1 \cdot 0.8} = \frac{0.10}{0.18} = \boxed{\frac59} \approx 0.56
$$

## Takeaway
Abuse raises the probability of guilt from $0.2$ to about $0.56$, so it is strongly relevant. The fallacy is conditioning on the wrong population: all abusive husbands, rather than those whose wives **were** murdered.

## Related topics
- [[Bayes' Rule]]
- [[Conditioning on Extra Evidence]]
