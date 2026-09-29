---
tags: [probability, problem, part-1]
topics: ["[[Story Proofs]]"]
---
# P06 — Story Proofs for Binomial Identities
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> Give story proofs of
> (a) $\displaystyle\sum_{k=0}^n\binom{n}{k} = 2^n$
> (b) $\displaystyle\binom{n}{k} + \binom{n}{k-1} = \binom{n+1}{k}$ for $n \ge k \ge 1$
> (c) $\displaystyle\sum_{k=0}^n\binom{n}{k}^2 = \binom{2n}{n}$
> (d) $\displaystyle\binom{k}{k} + \binom{k+1}{k} + \cdots + \binom{n}{k} = \binom{n+1}{k+1}$

## Solution
**(a)** Both sides count the subsets of $\{1, \dots, n\}$. On the right, each element is in or out ($2^n$). On the left, group the subsets by size $k$.

**(b)** A club has $n + 1$ members, one of whom is the president. The right side counts committees of size $k$. Split by the president:
- The president is **not** on it: choose all $k$ from the other $n$, giving $\binom{n}{k}$.
- The president **is** on it: choose the other $k-1$ from $n$, giving $\binom{n}{k-1}$.

**(c)** Choose $n$ people from a group of $n$ men and $n$ women, giving $\binom{2n}{n}$. Split by the number of men $k$: $\binom{n}{k}\binom{n}{n-k} = \binom{n}{k}^2$. Sum over $k$.

**(d)** Line up $n + 1$ people by age, labeled $1, \dots, n+1$ from youngest. Choose a group of $k + 1$ (the right side). Split by the **oldest** person in the group, say person $j + 1$ for $j = k, \dots, n$. The other $k$ must come from the $j$ younger people, which gives $\binom{j}{k}$. Summing over $j$ gives the left side. (This is the **hockey stick** identity.)

## Related topics
- [[Story Proofs]]
- [[P05 - Proof of the Binomial Theorem by Induction]], which uses (b)
