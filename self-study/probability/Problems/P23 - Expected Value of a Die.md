---
tags: [probability, problem, part-5]
topics: ["[[Expected Value]]", "[[Variance]]"]
---
# P23 — Expected Value of a Die
Back to [[self-study/probability/Index|Index]]

> [!question] Problem
> (a) Find $\E[X]$ and $\Var(X)$ for a fair six-sided die.
> (b) The 6 is misread as a 9, so the faces are $1, 2, 3, 4, 5, 9$. Find the new mean. Does the $(\min + \max)/2$ shortcut still work?
> (c) Find the expected sum of 10 fair dice and its variance.

## Solution
**(a)** $X \sim \DUnif(1, \dots, 6)$.
$$
\E[X] = \frac{1 + 2 + \cdots + 6}{6} = \frac{21}{6} = \boxed{3.5} = \frac{1 + 6}{2}
$$
$$
\E[X^2] = \frac{1 + 4 + 9 + 16 + 25 + 36}{6} = \frac{91}{6}, \qquad \Var(X) = \frac{91}{6} - \frac{49}{4} = \boxed{\frac{35}{12}} \approx 2.92
$$

**(b)**
$$
\E[X] = \frac{1 + 2 + 3 + 4 + 5 + 9}{6} = \frac{24}{6} = \boxed{4}, \qquad \text{but } \frac{1 + 9}{2} = 5
$$
The shortcut needs the values to be **evenly spaced**, so they pair up symmetrically around the middle ($1 + 6 = 2 + 5 = 3 + 4$). One large value moves the mean by $(9 - 6)/6 = 0.5$, not by half the change in the maximum.

**(c)** By linearity, $\E[S] = 10 \cdot 3.5 = \boxed{35}$. The dice are independent, so $\Var(S) = 10 \cdot \tfrac{35}{12} \approx \boxed{29.2}$.
By the [[Central Limit Theorem]], $S$ is already close to $\Normal(35, 29.2)$.

## Related topics
- [[Expected Value]]
- [[Variance]]
- [[Discrete Uniform Distribution]]
