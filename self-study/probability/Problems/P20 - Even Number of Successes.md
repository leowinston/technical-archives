---
tags: [probability, problem, part-3]
topics: ["[[Law of Total Probability]]", "[[Independence of Events]]"]
---
# P20 — Even Number of Successes
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> Run $n \ge 1$ independent trials. Trial $i$ succeeds with probability $p_i$. Let $q_i = 1 - p_i$ and $b_i = q_i - \tfrac12$. Let $A_n$ be the event that the number of successes is **even**.
> (a) Show that $\P(A_2) = \tfrac12 + 2b_1b_2$.
> (b) Show by induction that $\P(A_n) = \tfrac12 + 2^{n-1}b_1b_2\cdots b_n$.
> (c) Check (b) when some $p_i = \tfrac12$, when all $p_i = 0$, and when all $p_i = 1$.

## Setup
Write $q_i = \tfrac12 + b_i$ and $p_i = \tfrac12 - b_i$. Condition on whether the first $k$ trials had an even count, then look at trial $k+1$:
- even so far and trial $k+1$ fails → still even
- odd so far and trial $k+1$ succeeds → becomes even

## Solution
**(a)** Two trials give an even count if both fail or both succeed:
$$
\P(A_2) = q_1q_2 + p_1p_2 = \left(\tfrac12 + b_1\right)\left(\tfrac12 + b_2\right) + \left(\tfrac12 - b_1\right)\left(\tfrac12 - b_2\right) = \tfrac12 + 2b_1b_2
$$
The $\pm\tfrac12 b_i$ cross terms cancel.

**(b)** *Base case.* $\P(A_1) = q_1 = \tfrac12 + b_1 = \tfrac12 + 2^0b_1$. ✓

*Inductive hypothesis.* $\P(A_k) = \tfrac12 + c$ with $c = 2^{k-1}b_1\cdots b_k$.

*Inductive step.* By LOTP on $\{A_k, A_k^c\}$, using independence of trial $k+1$:
$$
\begin{aligned}
\P(A_{k+1}) &= \P(A_k)\,q_{k+1} + \P(A_k^c)\,p_{k+1} \\
&= \left(\tfrac12 + c\right)\left(\tfrac12 + b_{k+1}\right) + \left(\tfrac12 - c\right)\left(\tfrac12 - b_{k+1}\right) \\
&= \tfrac12 + 2c\,b_{k+1} = \tfrac12 + 2^{k}b_1\cdots b_{k+1}. \qquad \blacksquare
\end{aligned}
$$

**(c)**
- Some $p_i = \tfrac12$: then $b_i = 0$ and $\P(A_n) = \tfrac12$. One fair coin makes the parity fair, whatever the others do.
- All $p_i = 0$: $b_i = \tfrac12$, so $\P(A_n) = \tfrac12 + 2^{n-1}2^{-n} = 1$. Zero successes is even. ✓
- All $p_i = 1$: $b_i = -\tfrac12$, so $\P(A_n) = \tfrac12 + \tfrac12(-1)^n$. That is 1 for even $n$ and 0 for odd $n$. ✓

## Related topics
- [[Law of Total Probability]]
- [[Independence of Events]]
- [[Bernoulli and Binomial]]
