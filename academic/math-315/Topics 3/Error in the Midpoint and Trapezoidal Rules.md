---
tags: [math-315, topic, chapter-5]
---
# Error in the Midpoint and Trapezoidal Rules
Back to [Index](../Index.md) · Section 5.2.2 (textbook)

Integrate the [interpolation error](../Topics%202/Interpolation%20Error.md), then pull $f''$ out with a mean value theorem.

## Two mean value theorems
- **Integral MVT.** If $g, w$ are continuous and $w \ge 0$, then $\int_a^bw\,g = g(\eta)\int_a^bw$ for some $\eta \in (a, b)$.
- **MVT for sums.** If $g$ is continuous and $w_i \ge 0$, then $\sum w_ig(x_i) = \big(\sum w_i\big)g(\eta)$.

## One interval $[c, d]$
For the trapezoidal rule, $(x - c)(d - x) \ge 0$ on $[c, d]$, so
$$
I(f) - R_T(f) = -\int_c^d\frac{(x - c)(d - x)}{2}f''(\xi_x)\,dx = -\frac{(d - c)^3}{12}f''(\eta)
$$
The midpoint rule gives $I(f) - R_M(f) = +\dfrac{(d - c)^3}{24}f''(\tau)$.

## Composite rules
Sum the $N$ local errors and apply the MVT for sums with $Nh = b - a$:
$$
\boxed{\,I(f) - R_{CT}(f, h) = -\frac{(b - a)h^2}{12}f''(\eta), \qquad
I(f) - R_{CM}(f, h) = +\frac{(b - a)h^2}{24}f''(\eta)\,}
$$
Each local error is $O(h^3)$, and there are $N = O(1/h)$ of them, so the total is $O(h^2)$. Halving $h$ divides the error by $4$.

## The point $\eta$
$\eta$ exists but is unknown in general, and there can be more than one. For $f = \tfrac{(x-c)^3}{6}$ it is the midpoint of $[c, d]$.

## Explorations
- [EX40 - Locating the Unknown Point in the Trapezoidal Error](../Explorations%203/EX40%20-%20Locating%20the%20Unknown%20Point%20in%20the%20Trapezoidal%20Error.md)
- [EX41 - Trapezoidal Rule Error for x^2 + x - 1](../Explorations%203/EX41%20-%20Trapezoidal%20Rule%20Error%20for%20x%5E2%20%2B%20x%20-%201.md)
- [EX48 - Composite Rule Convergence for e^x on 0 to 1](../Explorations%203/EX48%20-%20Composite%20Rule%20Convergence%20for%20e%5Ex%20on%200%20to%201.md)

See also: [Midpoint and Trapezoidal Rules](Midpoint%20and%20Trapezoidal%20Rules.md), [Peano's Theorem](Peano%27s%20Theorem.md)
