---
tags:
  - math-315
  - exploration
  - chapter-5
source: Textbook Section 5.2.2, Examples 5.2.5–5.2.6 and Problems 5.2.12–5.2.13
topics:
  - "[[../Topics 3/Degree of Precision]]"
  - "[[../Topics 3/Simpson's Rule]]"
  - "[[../Topics 3/Peano's Theorem]]"
---
# EX42 — Simpson's Rule by Undetermined Coefficients
Back to [Index](../Index.md)

> [!question] Problem
> For $\int_{-1}^1f(x)\,dx \approx w_0f(-1) + w_1f(0) + w_2f(1)$:
> (a) Choose the weights to maximize the DOP.
> (b) Find the DOP.
> (c) Find the Peano constant $\kappa$ in $I - R = \kappa f^{(4)}(\eta)$.
> (d) Check that integrating the interpolating quadratic gives the same rule.

## Setup
- $I(x^m) = \int_{-1}^1x^m\,dx = \tfrac{2}{m+1}$ for even $m$, $0$ for odd $m$
- Three unknowns, so the first three equations of precision determine them

## Strategy
1. Tabulate $I(x^m)$ and $R(x^m)$.
2. Solve $m = 0, 1, 2$, then test $m = 3, 4$.
3. Use $f = x^4$ for $\kappa$.

## Solution
**(a) Equations of precision**

| $m$ | $I(x^m)$ | $R(x^m)$ |
|---|---|---|
| 0 | $2$ | $w_0 + w_1 + w_2$ |
| 1 | $0$ | $-w_0 + w_2$ |
| 2 | $\tfrac23$ | $w_0 + w_2$ |
| 3 | $0$ | $-w_0 + w_2$ |
| 4 | $\tfrac25$ | $w_0 + w_2$ |

From $m = 1$, $w_0 = w_2$. From $m = 2$, $w_0 = w_2 = \tfrac13$. From $m = 0$, $w_1 = 2 - \tfrac23 = \tfrac43$:
$$
\boxed{\,R(f) = \tfrac13\big[f(-1) + 4f(0) + f(1)\big]\,}
$$

**(b) DOP**

$m = 3$: $-w_0 + w_2 = 0 = I(x^3)$. $\checkmark$ $m = 4$: $w_0 + w_2 = \tfrac23 \ne \tfrac25$. So $\text{DOP} = 3$, one more than the three weights alone promise.

**(c) Peano constant**

$f = x^4$ has $f^{(4)} = 24$:
$$
\kappa = \frac{I(x^4) - R(x^4)}{4!} = \frac{\tfrac25 - \tfrac23}{24} = \frac{-\tfrac4{15}}{24} = \boxed{\,-\frac{1}{90}\,}
$$

**(d) By interpolation**

The quadratic through $(-1, f_{-1})$, $(0, f_0)$, $(1, f_1)$ is
$$
q(x) = f_0 + \frac{f_1 - f_{-1}}{2}x + \frac{f_1 - 2f_0 + f_{-1}}{2}x^2
$$
The odd term integrates to $0$:
$$
\int_{-1}^1q = 2f_0 + \frac{f_1 - 2f_0 + f_{-1}}{2}\cdot\frac23 = \frac13f_{-1} + \frac43f_0 + \frac13f_1 \ \checkmark
$$

## Result
Simpson's rule, $\text{DOP} = 3$, error $-\tfrac1{90}f^{(4)}(\eta)$ on $[-1, 1]$.

## Takeaways
- Symmetric points make every odd equation automatic, which is where the extra degree comes from.
- The DOP table is reused for $\kappa$: no new integrals are needed.

## Related topics
- [Degree of Precision](../Topics%203/Degree%20of%20Precision.md)
- [Simpson's Rule](../Topics%203/Simpson%27s%20Rule.md)
- [Peano's Theorem](../Topics%203/Peano%27s%20Theorem.md)
- [Quadrature Rules](../Topics%203/Quadrature%20Rules.md)
