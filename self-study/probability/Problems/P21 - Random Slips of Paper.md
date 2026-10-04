---
tags: [probability, problem, part-4]
topics: ["[[Bernoulli and Binomial]]", "[[Hypergeometric Distribution]]", "[[Discrete Uniform Distribution]]"]
---
# P21 — Random Slips of Paper
Back to [Index](../Index.md)

> [!question] Problem
> A hat holds 100 slips numbered $1, \dots, 100$. Five are drawn one at a time.
> **With replacement:** (a) the distribution of how many drawn slips are $\ge 80$; (b) the distribution of the $j$-th draw; (c) $\P(\text{100 is drawn at least once})$.
> **Without replacement:** (d)–(f) the same three questions.

## Solution
There are 21 "good" slips ($80, \dots, 100$) and 79 others.

| | With replacement | Without replacement |
|---|---|---|
| Count $\ge 80$ | $\Bin(5,\, 0.21)$ | $\HGeom(21,\, 79,\, 5)$ |
| $j$-th draw | $\DUnif(1, \dots, 100)$ | $\DUnif(1, \dots, 100)$ (by symmetry) |
| $\P(\text{100 drawn})$ | $1 - 0.99^5 \approx 0.049$ | $5/100 = 0.05$ |

**(a)** Independent draws, each good with probability $0.21$: Binomial story.
**(d)** No replacement: the draws are dependent, which is the Hypergeometric story.
$$
\P(X = k) = \frac{\binom{21}{k}\binom{79}{5-k}}{\binom{100}{5}}
$$
**(b, e)** Each slip is equally likely to be in position $j$, with or without replacement.
**(c)** Use the complement: $\P(X_1 \ne 100, \dots, X_5 \ne 100) = 0.99^5$ by independence.
**(f)** 100 is equally likely to be in any of the 100 positions of a full random ordering, and we see the first 5.

## Takeaway
Replacement changes the **count** distribution (Binomial vs Hypergeometric) but not the distribution of any **single** draw.

## Related topics
- [Bernoulli and Binomial](../Notes/Bernoulli%20and%20Binomial.md)
- [Hypergeometric Distribution](../Notes/Hypergeometric%20Distribution.md)
- [Discrete Uniform Distribution](../Notes/Discrete%20Uniform%20Distribution.md)
