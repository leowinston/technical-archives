---
tags: [probability, topic, part-1]
---
# Binomial Coefficients
Back to [Index](../Index.md) · Part 1

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
- **Equal-sized groups:** when the groups have no labels, divide by the number of ways to order them (see [P03 - Splitting Twelve People into Teams](../Problems/P03%20-%20Splitting%20Twelve%20People%20into%20Teams.md)).

## Problems
- [P02 - Full House and the Newton-Pepys Problem](../Problems/P02%20-%20Full%20House%20and%20the%20Newton-Pepys%20Problem.md)
- [P03 - Splitting Twelve People into Teams](../Problems/P03%20-%20Splitting%20Twelve%20People%20into%20Teams.md)
- [P04 - Lattice Paths](../Problems/P04%20-%20Lattice%20Paths.md)
- [P10 - Mixed Practice Comparisons](../Problems/P10%20-%20Mixed%20Practice%20Comparisons.md)

See also: [Binomial Theorem](Binomial%20Theorem.md), [Story Proofs](Story%20Proofs.md)
