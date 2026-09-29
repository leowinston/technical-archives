---
tags: [probability, problem, part-1]
topics: ["[[Binomial Theorem]]", "[[Story Proofs]]"]
---
# P05 — Proof of the Binomial Theorem by Induction
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> Prove that for every integer $n \ge 1$,
> $$(x+y)^n = \sum_{k=0}^{n}\binom{n}{k}x^k y^{n-k}.$$

## Proof
Let $P(n)$ be the statement above.

**Base case ($n = 1$).** The left side is $x + y$. The right side is $\binom10 x^0y^1 + \binom11 x^1 y^0 = x + y$. So $P(1)$ holds.

**Inductive step.** Suppose $P(m)$ holds for some $m \ge 1$. Then
$$
\begin{aligned}
(x+y)^{m+1} &= (x+y)\sum_{k=0}^{m}\binom{m}{k}x^k y^{m-k} && \text{(inductive hypothesis)} \\
&= \sum_{k=0}^{m}\binom{m}{k}x^{k+1}y^{m-k} + \sum_{k=0}^{m}\binom{m}{k}x^{k}y^{m+1-k}.
\end{aligned}
$$
In the first sum, let $j = k + 1$. In the second, rename $k$ to $j$:
$$
= \sum_{j=1}^{m+1}\binom{m}{j-1}x^{j}y^{m+1-j} + \sum_{j=0}^{m}\binom{m}{j}x^{j}y^{m+1-j}.
$$
Pull out $j = m+1$ from the first sum and $j = 0$ from the second, then combine the rest:
$$
= x^{m+1} + y^{m+1} + \sum_{j=1}^{m}\left[\binom{m}{j-1} + \binom{m}{j}\right]x^j y^{m+1-j}.
$$
By Pascal's rule, $\binom{m}{j-1} + \binom{m}{j} = \binom{m+1}{j}$. Since $\binom{m+1}{0} = \binom{m+1}{m+1} = 1$, the end terms fold back into the sum:
$$
(x+y)^{m+1} = \sum_{j=0}^{m+1}\binom{m+1}{j}x^j y^{m+1-j}.
$$
So $P(m) \Rightarrow P(m+1)$. By induction, $P(n)$ holds for all $n \in \mathbb{Z}^+$. $\blacksquare$

## Intuition
Each term of $(x+y)^n$ comes from choosing $x$ or $y$ in every factor, without regard to order. There are $\binom{n}{k}$ ways to choose $x$ exactly $k$ times.

## Related topics
- [[Binomial Theorem]]
- [[Story Proofs]] (Pascal's rule)
