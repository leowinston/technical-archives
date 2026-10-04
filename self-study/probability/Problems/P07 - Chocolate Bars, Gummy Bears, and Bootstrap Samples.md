---
tags: [probability, problem, part-1]
topics: ["[[Stars and Bars]]", "[[Inclusion-Exclusion]]"]
---
# P07 — Chocolate Bars, Gummy Bears, and Bootstrap Samples
Back to [Index](../Index.md)

> [!question] Problem
> 1. There are 15 chocolate bars and 10 children. Count the distributions if the bars are
>    (a) interchangeable, (b) interchangeable and every child gets at least one, (c) distinct, (d) distinct and every child gets at least one.
> 2. A pack holds 30 to 50 gummy bears in 5 flavors. How many flavor compositions are possible? Use only a couple of binomial coefficients.
> 3. From $n$ distinct numbers, a **bootstrap sample** draws $n$ times with replacement. How many samples are there if (a) order matters, (b) order doesn't matter?

## Solution
**1(a)** 15 stars and 9 bars: $\binom{24}{9} = \boxed{1{,}307{,}504}$.

**1(b)** Give each child one bar first, then place the remaining 5 freely: $\binom{14}{9} = \boxed{2002}$.

**1(c)** Each bar picks one of 10 children: $\boxed{10^{15}}$.

**1(d)** Stars and bars doesn't apply to distinct objects. Use inclusion–exclusion on $A_i$ = child $i$ gets nothing:
$$
\sum_{j=0}^{10}(-1)^j\binom{10}{j}(10-j)^{15}
$$
Here $j$ counts the children forced to get nothing.

**2** A pack of exactly $m$ bears in 5 flavors gives $\binom{m+4}{4}$ compositions. Sum over $m$ and use the hockey stick identity:
$$
\sum_{m=30}^{50}\binom{m+4}{4} = \sum_{j=34}^{54}\binom{j}{4} = \boxed{\binom{55}{5} - \binom{34}{5}} = 3{,}200{,}505
$$

**3(a)** $n^n$.
**3(b)** $n$ draws are placed into $n$ "boxes" (how often each $a_j$ is used): $\binom{2n-1}{n}$.
These unordered samples are **not** equally likely. $\{a_1, \dots, a_n\}$ (each once) arises from $n!$ orderings, but $\{a_1, a_1, \dots, a_1\}$ arises from only one.

## Related topics
- [Stars and Bars](../Notes/Stars%20and%20Bars.md)
- [Inclusion-Exclusion](../Notes/Inclusion-Exclusion.md)
- [Story Proofs](../Notes/Story%20Proofs.md) (hockey stick)
