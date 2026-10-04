---
tags: [probability, problem, part-3]
topics: ["[[Bayes' Rule]]", "[[Conditioning on Extra Evidence]]"]
---
# P15 — Six-Fingered Man
Back to [Index](../Index.md)

> [!question] Problem
> One of the $n$ men in a country committed a crime. Initially each is equally likely to be the one. A witness reports that the perpetrator has six fingers on his right hand. Eyewitnesses aren't perfectly reliable, so the perpetrator has six fingers with probability $p_1 < 1$, while an innocent man has six fingers with probability $p_0 < p_1$. Let $a = p_0/p_1$ and $b = (1-p_1)/(1-p_0)$.
> (a) Rugen has six fingers. Find $\P(\text{Rugen is guilty})$.
> (b) Everyone is now checked, and Rugen is the **only** six-fingered man. Find $\P(\text{Rugen is guilty})$.

## Solution
Let $G$ be the event that Rugen is guilty, $\P(G) = 1/n$. Let $M$ be the event that he has six fingers, and $N$ the event that nobody else does.

**(a)**
$$
\P(G \mid M) = \frac{p_1 \cdot \tfrac1n}{p_1 \cdot \tfrac1n + p_0\left(1 - \tfrac1n\right)} = \boxed{\frac{1}{1 + a(n-1)}}
$$
If six fingers are rare among innocent men ($a$ small), this can be large even for big $n$.

**(b)** Given $G$, the other $n-1$ men are innocent, so $\P(N \mid G) = (1-p_0)^{n-1}$. Given $G^c$, the guilty man is one of the others and must lack six fingers, while the rest are innocent: $\P(N \mid G^c) = (1-p_1)(1-p_0)^{n-2}$. Then
$$
\P(G \mid M, N) = \frac{p_1 (1-p_0)^{n-1} \tfrac1n}{p_1(1-p_0)^{n-1}\tfrac1n + p_0(1-p_1)(1-p_0)^{n-2}\left(1 - \tfrac1n\right)} = \boxed{\frac{1}{1 + ab(n-1)}}
$$
Since $b < 1$, learning that nobody else matches **raises** the probability of guilt.

## Related topics
- [Bayes' Rule](../Notes/Bayes%27%20Rule.md)
- [Conditioning on Extra Evidence](../Notes/Conditioning%20on%20Extra%20Evidence.md)
