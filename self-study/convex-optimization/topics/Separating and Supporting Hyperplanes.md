---
tags: [convex-optimization, topic, ch-2]
source: Boyd & Vandenberghe §2.5 (pp. 46–51)
---
# Separating and Supporting Hyperplanes
Back to [[self-study/convex-optimization/Index|Index]] · Section 2.5

## Separating hyperplane theorem
If $C, D$ are convex and disjoint, there are $a \ne 0$ and $b$ with
$$
\boxed{\,a^{\top}x \le b \ \ \forall x \in C, \qquad a^{\top}x \ge b \ \ \forall x \in D\,}
$$
**Proof idea** (when $\operatorname{dist}(C, D) > 0$): take the closest pair $c \in C$, $d \in D$, and use the perpendicular bisector of the segment $cd$:
$$
a = d - c, \qquad b = \frac{\lVert d\rVert_2^2 - \lVert c\rVert_2^2}{2}.
$$

## Supporting hyperplane
For $x_0$ on the boundary of $C$, a **supporting hyperplane** is $\{x \mid a^{\top}x = a^{\top}x_0\}$ with $a^{\top}x \le a^{\top}x_0$ for all $x \in C$. Every convex set has one at every boundary point.

These theorems drive duality: they are the geometric reason a dual problem gives a certificate.

See also: [[Dual Cones]], [[First-Order Condition]]
