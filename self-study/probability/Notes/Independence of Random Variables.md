---
tags: [probability, topic, part-4]
---
# Independence of Random Variables
Back to [Index](../Index.md) · Part 4

## Definition
$X$ and $Y$ are **independent** if, for all $x, y \in \mathbb{R}$,
$$
\P(X \le x, Y \le y) = \P(X \le x)\,\P(Y \le y)
$$
In the discrete case this is the same as
$$
\boxed{\P(X = x, Y = y) = \P(X = x)\,\P(Y = y) \quad \text{for all } x, y}
$$
For $X_1, \dots, X_n$, the joint CDF must factor. Unlike events, one equation covers every subset.

**i.i.d.** means independent and identically distributed: $X_1, X_2, \dots \iid F$.

## Example
Two players each flip a fair penny. $X = 1$ if A's penny is Heads and $-1$ otherwise, and $Y$ is defined the same way for B's penny. Let $Z = XY$, which is $1$ exactly when the pennies match.
- Unconditionally, $X \indep Y$, and in fact $X \indep Z$ as well.
- Given $Z = 1$, $X = Y$, so they are completely dependent. Given $Z = -1$, $Y = -X$.

## Problems
- [P22 - Matching Pennies and Mystery Opponents](../Problems/P22%20-%20Matching%20Pennies%20and%20Mystery%20Opponents.md)
- [P26 - Simulation and SPY Returns Lab](../Problems/P26%20-%20Simulation%20and%20SPY%20Returns%20Lab.md), which tests whether daily returns are independent

See also: [Independence of Events](Independence%20of%20Events.md), [Conditional Independence](Conditional%20Independence.md)
