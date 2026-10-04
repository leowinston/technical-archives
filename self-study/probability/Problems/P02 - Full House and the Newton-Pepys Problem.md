---
tags: [probability, problem, part-1]
topics: ["[[Binomial Coefficients]]", "[[Naive Definition of Probability]]"]
---
# P02 — Full House and the Newton–Pepys Problem
Back to [Index](../Index.md)

> [!question] Problem
> (a) A 5-card hand is dealt from a shuffled 52-card deck. Find $\P(\text{full house})$: three cards of one rank and two of another.
> (b) Which is most likely? $A$: at least one 6 in 6 dice. $B$: at least two 6's in 12 dice. $C$: at least three 6's in 18 dice.

## Solution
**(a)** All $\binom{52}{5}$ hands are equally likely. Build a full house with the multiplication rule (a tree):
1. Rank of the triple: 13 choices. Which 3 of its 4 suits: $\binom43$.
2. Rank of the pair: 12 remaining choices. Which 2 suits: $\binom42$.
$$
\P(\text{full house}) = \frac{13\binom43 \cdot 12\binom42}{\binom{52}{5}} = \frac{3744}{2598960} \approx 0.00144
$$

**(b)** Count the complements ("too few 6's") over $6^6$, $6^{12}$, and $6^{18}$ equally likely outcomes.
$$
\begin{aligned}
\P(A) &= 1 - \frac{5^6}{6^6} \approx 0.665 \\
\P(B) &= 1 - \frac{5^{12} + \binom{12}{1}5^{11}}{6^{12}} \approx 0.619 \\
\P(C) &= 1 - \frac{5^{18} + \binom{18}{1}5^{17} + \binom{18}{2}5^{16}}{6^{18}} \approx 0.597
\end{aligned}
$$
In $\P(B)$, $\binom{12}{1}5^{11}$ counts exactly one 6: choose which die, then fill the other 11 with non-6's.

$$
\boxed{A \text{ is most likely}}
$$

## Related topics
- [Binomial Coefficients](../Notes/Binomial%20Coefficients.md)
- [Naive Definition of Probability](../Notes/Naive%20Definition%20of%20Probability.md)
- [Bernoulli and Binomial](../Notes/Bernoulli%20and%20Binomial.md): $B$ and $C$ are Binomial tail probabilities.
