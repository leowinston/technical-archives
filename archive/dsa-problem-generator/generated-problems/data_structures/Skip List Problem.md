---
tags:
  - data-structures-and-algorithms
  - generated-problem
  - data-structures
  - skip-list
course: CS 253
topic: skip_list
seed: 1
---
# Skip List Problem
Back to [[archive/dsa-problem-generator/Index|Index]] · `data_structures` · seed 1 · `--topic skip-list --seed 1`

> [!question] Problem · Skip List Tracing Challenge
> Construct a skip list by inserting the keys in the order below. Use the prescribed tower heights to remove coin-flip ambiguity. After the structure is built, remove the keys $36,\ 75,\ 91$, showing each pointer update.
>
> | Key | 66 | 36 | 56 | 58 | 90 | 27 | 51 | 75 | 94 | 91 |
> |---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
> | **Height** | 1 | 1 | 5 | 1 | 1 | 1 | 3 | 1 | 1 | 1 |

> [!info]- Why the generator kept this instance
> **Rule:** at least 5 promotions above the base level, at least two towers of height $\ge 3$, and a tallest tower of height $\ge 4$.
> **This instance:** 6 promotions ($56$ adds 4 levels, $51$ adds 2), tallest tower 5.
> Fair coin flips often give an almost flat list, which is just a linked list. The rule throws those away.

---

## The big picture
A skip list is a sorted linked list with **express lanes**. Every key gets a tower, and level $L_k$ links together the keys whose towers reach height $k$. A search starts at the top-left sentinel, moves right while the next key is still $\le$ the target, and drops a level otherwise.

Normally the tower height comes from coin flips:
$$
\P(\text{height} \ge k) = 2^{-(k-1)}.
$$
On average the list is balanced, so search, insert, and delete take $O(\log n)$ expected time. A study problem can't use coin flips, though, because every student would build a different list. So the **generator** flips the coins (capped at height 5) and prints the results as a table. The randomness moves from the solver to the problem.

## Getting to the solution

**1 · Build.** The insertion order does not matter for the final shape. Each key's tower sits at its sorted position:
$$
27,\ 36,\ 51^{(3)},\ 56^{(5)},\ 58,\ 66,\ 75,\ 90,\ 91,\ 94
$$
To insert a key, search for it and record the last node visited on each level (its **predecessors**). Then splice the new tower in after them, one level at a time up to its height.

**2 · Delete.** Search for the key, then point each predecessor past it on every level the tower reaches. All three deleted keys have height 1, so each deletion changes exactly one pointer on $L_1$:

| Delete | Search path (top-down) | Pointer update on $L_1$ |
|:-:|---|---|
| 36 | $L_5$–$L_2$: next key 56 or 51 is too big, drop · $L_1$: $-\infty \to 27 \to$ **36** | $27.\text{next} \leftarrow 51$ |
| 75 | $L_5$, $L_4$: $-\infty \to 56$, drop · $L_3$, $L_2$: $56$, drop · $L_1$: $56 \to 58 \to 66 \to$ **75** | $66.\text{next} \leftarrow 90$ |
| 91 | same express route to 56 · $L_1$: $56 \to 58 \to 66 \to 90 \to$ **91** | $90.\text{next} \leftarrow 94$ |

The search for 91 skips from $-\infty$ straight to 56 on the top level. Tall towers pay off exactly like this.

## Solution

![[archive/dsa-problem-generator/generated-problems/data_structures/skip_list-seed1-solution.svg]]

> [!success] Answer
> $L_5 = L_4 = \{56\}$ · $L_3 = L_2 = \{51, 56\}$ · $L_1 = \{27, 51, 56, 58, 66, 90, 94\}$, each level between the sentinels $-\infty$ and $+\infty$.

---

## Connections
- [[self-study/probability/Notes/Bernoulli and Binomial|Bernoulli and Binomial]]: each promotion is a $\Bern(\tfrac12)$ trial, so the number of keys reaching level $k$ is $\Bin\!\big(n,\ 2^{-(k-1)}\big)$.
- [[self-study/probability/Notes/Expected Value|Expected Value]]: with the height capped at 5, the expected number of promotions per key is
$$
\sum_{k=2}^{5} 2^{-(k-1)} = \tfrac12 + \tfrac14 + \tfrac18 + \tfrac1{16} = \tfrac{15}{16},
$$
so about $9.4$ for 10 keys. This instance has 6, and the rule's floor is 5.
- [[archive/experiments/Data Structures and Algorithms/Hashmap Experimental Analysis|HashMap Experimental Analysis]]: the other randomized dictionary from CS 253. There the randomness is in the hash, not the structure.
- Other generator topics in `data_structures`: `hashing`.

## Files
- Source: `skip_list-seed1.tex` (generator output, unchanged)
- Compiled: [[archive/dsa-problem-generator/generated-problems/data_structures/skip_list-seed1.pdf|skip_list-seed1.pdf]]
- Regenerate: `python3 cs253_problem_generator.py --topic skip-list --seed 1 --with-solution`
