---
tags: [probability, problem, part-3]
topics: ["[[Conditional Probability]]"]
---
# P13 — The Two-Child Problem
Back to [Index](../Index.md)

> [!question] Problem
> A family has two children. Each child is independently a boy or a girl with probability $1/2$. Find the probability that both are girls given
> (a) at least one is a girl
> (b) the **older** child is a girl
> (c) at least one is a girl **born in winter** (seasons equally likely, independent of sex)

## Solution
**(a)** The sample space is $\{GG, GB, BG, BB\}$. Knowing at least one is a girl removes $BB$ and leaves 3 equally likely outcomes, only one of which is $GG$:
$$
\P(GG \mid \text{at least one } G) = \frac{1/4}{3/4} = \boxed{\frac13}
$$

**(b)** This leaves $\{GG, GB\}$ (older child listed first):
$$
\P(GG \mid \text{older is } G) = \frac{1/4}{1/2} = \boxed{\frac12}
$$

**(c)** A given child is a winter girl with probability $\tfrac12 \cdot \tfrac14 = \tfrac18$.
$$
\P(\text{at least one winter girl}) = 1 - \left(\tfrac78\right)^2 = \tfrac{15}{64}
$$
Both girls and at least one born in winter:
$$
\P = \tfrac14\left(1 - \left(\tfrac34\right)^2\right) = \tfrac{7}{64}
\quad\Longrightarrow\quad
\P(GG \mid \text{winter girl}) = \frac{7/64}{15/64} = \boxed{\frac{7}{15}}
$$

## Takeaway
The answer depends on **exactly what was learned and how**. More specific information about one girl, such as "older" or "born in winter", picks out one child more sharply and pushes the answer from $1/3$ toward $1/2$. If you met one of the children **at random** and she was a girl, the answer would also be $1/2$.

## Related topics
- [Conditional Probability](../Notes/Conditional%20Probability.md)
