---
tags:
  - math-315
  - exploration
  - lecture-4
source: Lecture 4 handout, pp. 18–20 (Section 4.3.2, construction of a B-spline)
topics:
  - "[[../Topics 2/Cubic B-Splines]]"
  - "[[../Topics 2/Cubic Splines]]"
---
# EX31 — Deriving the Cubic B-Spline
Back to [Index](../Index.md)

> [!question] Problem
> Let $B_p$ be supported on $[x_p - 2h, x_p + 2h]$ and symmetric about $x_p$, with $B_p(x_p) = 1$. On the left half,
> $$
> B_p = A\,(x - [x_p - 2h])^3 \ \text{ on } [x_p - 2h, x_p - h], \qquad
> B_p = A\,(x - [x_p - 2h])^3 + B\,(x - [x_p - h])^3 \ \text{ on } [x_p - h, x_p]
> $$
> (a) Find $A$ and $B$.
> (b) Verify that $B_p \in C^2$.
> (c) Fill in the table of $B_p$, $B_p'$, $B_p''$ at the knots.

![L4-cubic-b-spline.png](../Assets/L4-cubic-b-spline.png)

## Setup
- Shift so that $x_p = 0$, and write $t = x - x_p$. The knots are $t = -2h, -h, 0, h, 2h$.
- By symmetry the right half is $B_p(t) = B_p(-t)$.

## Strategy
1. Normalization at $t = 0$ gives one equation.
2. $C^1$ at $t = 0$ gives a second equation. Check the remaining conditions.

## Solution
**(a) The constants**

At $t = 0$ the left formula gives
$$
A(2h)^3 + B(h)^3 = 1 \implies 8A + B = \frac{1}{h^3}
$$
For the derivative, the left side gives $B_p'(0^-) = 3A(2h)^2 + 3B(h)^2 = 12Ah^2 + 3Bh^2$. By symmetry $B_p'(0^+) = -B_p'(0^-)$. Continuity forces both to be $0$:
$$
4A + B = -(4A + B) \implies B = -4A
$$
$$
8A - 4A = \frac{1}{h^3} \implies \boxed{\,A = \frac{1}{4h^3}, \quad B = -\frac{1}{h^3}\,}
$$

**(b) $C^2$ everywhere**
- At $t = -2h$: $A(t + 2h)^3$ and its first two derivatives vanish there, so $B_p$ meets the zero function in $C^2$.
- At $t = -h$: the new term $B(t + h)^3$ has value, slope, and curvature all $0$ at $t = -h$, so nothing jumps.
- At $t = 0$: $B_p''$ is even under the symmetry, so its left and right values match automatically:
$$
B_p''(0) = 6A(2h) + 6B(h) = \frac{3}{h^2} - \frac{6}{h^2} = -\frac{3}{h^2}
$$
- By symmetry the right half behaves the same way. Only $B_p'''$ jumps at the knots.

**(c) Knot values**

At $t = -h$:
$$
B_p = Ah^3 = \tfrac14, \qquad B_p' = 3Ah^2 = \tfrac{3}{4h}, \qquad B_p'' = 6Ah = \tfrac{3}{2h^2}
$$

| $t$ | $-2h$ | $-h$ | $0$ | $h$ | $2h$ |
|---|---|---|---|---|---|
| $B_p$ | $0$ | $\tfrac14$ | $1$ | $\tfrac14$ | $0$ |
| $B_p'$ | $0$ | $\tfrac{3}{4h}$ | $0$ | $-\tfrac{3}{4h}$ | $0$ |
| $B_p''$ | $0$ | $\tfrac{3}{2h^2}$ | $-\tfrac{3}{h^2}$ | $\tfrac{3}{2h^2}$ | $0$ |

> [!warning] Handout sign slip
> On $[x_p, x_p + h]$ the handout writes $B_p' = -\tfrac{3}{4h^3}\big[4(x - [x_p + h])^2 - (x - [x_p + 2h])^2\big]$. That gives $B_p'(x_p + h) = +\tfrac{3}{4h}$, which contradicts its own table. The correct form is
> $$
> B_p'(x) = -\frac{3}{4h^3}\Big[(x - [x_p + 2h])^2 - 4(x - [x_p + h])^2\Big]
> $$
> The same sign flip appears in $B_p''$ on that interval.

## Result
- $A = \dfrac{1}{4h^3}$ and $B = -\dfrac{1}{h^3}$.
- $B_p$ has the values $\tfrac14, 1, \tfrac14$ at $x_{p-1}, x_p, x_{p+1}$. It is $C^2$ with compact support of width $4h$.

## Takeaways
- Every row of the interpolation matrix is $\big(\tfrac14, 1, \tfrac14\big)$, which makes the system tridiagonal.
- With this normalization the B-splines sum to $\tfrac32$ at each node, not $1$. The usual normalization is $B_p(x_p) = \tfrac23$.

## Related topics
- [Cubic B-Splines](../Topics%202/Cubic%20B-Splines.md)
- [Cubic Splines](../Topics%202/Cubic%20Splines.md)
