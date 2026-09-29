---
tags: [probability, problem, part-3]
topics: ["[[Law of Total Probability]]"]
---
# P16 — Monty Hall
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> There are 3 doors: one car and two goats. You pick a door. Monty, who knows where the car is, always opens a **different** door with a goat, choosing at random if he has two options, and offers you a switch. Should you switch?

## Solution
Condition on where the car is (LOTP). Say you picked door 1, and let $C_i$ be the event that the car is behind door $i$.
$$
\P(\text{win by switching}) = \P(\text{win} \mid C_1)\tfrac13 + \P(\text{win} \mid C_2)\tfrac13 + \P(\text{win} \mid C_3)\tfrac13 = 0 + 1\cdot\tfrac13 + 1\cdot\tfrac13 = \boxed{\tfrac23}
$$
If the car is behind door 2 or 3, Monty is **forced** to reveal the other goat, and switching wins.

## Intuition: a million doors
You pick 1 door of 1,000,000. Monty opens 999,998 goat doors and leaves exactly one other door closed. Your first pick is still a $10^{-6}$ shot. The remaining door carries almost all the probability.

> [!warning] Assumptions matter
> The $2/3$ depends on Monty **always** opening a goat door and choosing at random between two goats. If he only opens doors when you've picked the car, switching is a disaster.

## Related topics
- [[Law of Total Probability]]
- [[Bayes' Rule]]
