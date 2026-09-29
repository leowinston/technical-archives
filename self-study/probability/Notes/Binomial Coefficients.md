---
tags: [probability, topic, part-1]
---
# Binomial Coefficients
Back to [[self-study/probability/Index|Index]] · Part 1

## Definition
$\binom{n}{k}$ ("$n$ choose $k$") is the number of subsets of size $k$ from a set of size $n$.
$$
\boxed{\binom{n}{k} = \frac{n(n-1)\cdots(n-k+1)}{k!} = \frac{n!}{(n-k)!\,k!}}, \qquad \binom{n}{k} = 0 \text{ for } k > n
$$

## Adjusting for overcounting
Count ordered choices, then divide by the number of orderings of each group.
- Committee of 2 from 4 people: $4 \cdot 3 / 2 = 6$.
- Words with repeated letters: STATISTICS $= \dfrac{10!}{3!\,3!\,2!} = 50400$.

## Tips
- **Cancel common terms first:** $\binom{100}{2} = \dfrac{100 \cdot 99}{2} = 4950$. Never compute $100!$.
- **Symmetry:** $\binom{n}{k} = \binom{n}{n-k}$. Choosing who is in is the same as choosing who is out.
- **Equal-sized groups:** when the groups have no labels, divide by the number of ways to order them (see [[P03 - Splitting Twelve People into Teams]]).

## Problems
- [[P02 - Full House and the Newton-Pepys Problem]]
- [[P03 - Splitting Twelve People into Teams]]
- [[P04 - Lattice Paths]]
- [[P10 - Mixed Practice Comparisons]]

See also: [[Binomial Theorem]], [[Story Proofs]]
