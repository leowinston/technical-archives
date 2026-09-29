---
tags: [probability, topic, part-3]
---
# Conditional Probability
Back to [[self-study/probability/Index|Index]] · Part 3

## Definition
For $\P(B) > 0$,
$$
\boxed{\P(A \mid B) = \frac{\P(A \cap B)}{\P(B)}}
$$
$\P(A \mid B)$ is the probability of $A$ **once you know $B$ happened**. $\P(A)$ is the **prior** and $\P(A \mid B)$ is the **posterior**.

## Example
A random day is rainy with probability 10%. Given that the day is in August, the probability is 15%. Learning the month moves the probability of rain.

## Notes
- **$\P(A \mid B) \ne \P(B \mid A)$ in general.** Confusing the two is the prosecutor's fallacy.
- **Frequentist view:** among the repetitions where $B$ happened, $\P(A \mid B)$ is the fraction where $A$ also happened.
- Time order doesn't restrict you. You may condition on the second card to learn about the first.
- $\P(A \mid A) = 1$, but $\P(A)$ is still the prior. Don't replace it with 1 in the middle of a calculation.
- **Chain rule:** $\P(A_1 \cap A_2 \cap A_3) = \P(A_1)\,\P(A_2 \mid A_1)\,\P(A_3 \mid A_1, A_2)$

## Problems
- [[P11 - Two Cards, a Heart and a Red]]
- [[P13 - The Two-Child Problem]]

See also: [[Bayes' Rule]], [[Law of Total Probability]]
