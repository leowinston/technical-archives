---
tags: [probability, problem, part-3]
topics: ["[[Bayes' Rule]]"]
---
# P18 — Spam Filter
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> 80% of email is spam. The phrase "free money" appears in 10% of spam and 1% of non-spam. A new email contains "free money". What is the probability that it is spam?

## Solution
Let $S$ be the event that the email is spam and $F$ the event that it contains "free money".
$$
\P(S \mid F) = \frac{\P(F \mid S)\P(S)}{\P(F \mid S)\P(S) + \P(F \mid S^c)\P(S^c)} = \frac{(0.1)(0.8)}{(0.1)(0.8) + (0.01)(0.2)} = \frac{0.08}{0.082} = \boxed{\frac{40}{41}} \approx 0.976
$$

## Odds check
Prior odds are $0.8 : 0.2 = 4$, and the likelihood ratio is $0.1/0.01 = 10$. Posterior odds are $40$, so $\P = 40/41$. ✓

## Related topics
- [[Bayes' Rule]]
- [[Law of Total Probability]]
