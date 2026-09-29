---
tags: [probability, problem, part-2]
topics: ["[[Inclusion-Exclusion]]"]
---
# P08 — de Montmort's Matching Problem
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> A shuffled deck has $n$ cards labeled $1, \dots, n$. Flip them over one at a time, counting $1, 2, \dots, n$ as you go. You win if some card's label equals the number you say. Find $\P(\text{win})$.

## Strategy
Let $A_i$ be the event that card $i$ is in position $i$. Then $\P(\text{win}) = \P(A_1 \cup \cdots \cup A_n)$. Use inclusion–exclusion and symmetry.

## Solution
**Single events.** There are $n!$ equally likely orderings. Fix card $i$ in spot $i$ and arrange the rest: $(n-1)!$ orderings. So $\P(A_i) = \tfrac{(n-1)!}{n!} = \tfrac1n$. By symmetry, card $i$ is equally likely to be in any of the $n$ spots.

**Intersections.** $\P(A_i \cap A_j) = \tfrac{(n-2)!}{n!}$, and in general $\P(A_{i_1} \cap \cdots \cap A_{i_k}) = \tfrac{(n-k)!}{n!}$. There are $\binom{n}{k}$ such terms, and
$$
\binom{n}{k}\frac{(n-k)!}{n!} = \frac{1}{k!}.
$$
**So**
$$
\boxed{\P(\text{win}) = 1 - \frac{1}{2!} + \frac{1}{3!} - \cdots + (-1)^{n+1}\frac{1}{n!}} \;\to\; 1 - \frac1e \approx 0.632
$$

## Check with $n = 4$
$1 - \tfrac12 + \tfrac16 - \tfrac1{24} = \tfrac{15}{24} = 0.625$, already close to the limit. By brute force, 9 of the 24 orderings have no match, and $1 - \tfrac{9}{24} = \tfrac{15}{24}$. ✓

## Related topics
- [[Inclusion-Exclusion]]
