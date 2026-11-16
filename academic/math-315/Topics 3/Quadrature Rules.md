---
tags: [math-315, topic, chapter-5]
---
# Quadrature Rules
Back to [Index](../Index.md) · Section 5.2.2 (textbook)

Approximate $I(f) = \int_a^b f(x)\,dx$ using only values of $f$ at points in $[a, b]$.

## Form
$$
\boxed{\,R(f) = \sum_{i=0}^{N}w_if(x_i)\,}
$$
with **points** (nodes) $x_0 < \cdots < x_N$ and **weights** $w_i$. Both $I$ and $R$ are **linear functionals**: $R(\alpha f + \beta g) = \alpha R(f) + \beta R(g)$.

## Error of integrating an approximation
If $R(f) = I(q)$ for some simpler $q \approx f$, linearity gives
$$
I(f) - R(f) = I(f - q)
$$
So the integration error is the integral of the approximation error. If $\max|f - q| = \epsilon$ then $|I(f) - I(q)| \le \epsilon\,|b - a|$.

## Interpolatory rules
Take $q = q_N$, the [interpolating polynomial](../Topics%202/Polynomial%20Interpolation.md) in [Lagrange form](../Topics%202/Lagrange%20Form.md). Then
$$
I(q_N) = \sum_{i=0}^{N}\underbrace{\int_a^b\ell_i(x)\,dx}_{w_i}\,f(x_i)
$$
The weights depend only on the points, not on $f$. An interpolatory rule with $N + 1$ points is exact for every polynomial of degree $\le N$.

## Example
Interpolating at the two endpoints gives $w_1 = w_2 = \int_c^d\ell_i = \tfrac{d-c}{2}$: the [trapezoidal rule](Midpoint%20and%20Trapezoidal%20Rules.md).

## Explorations
- [EX42 - Simpson's Rule by Undetermined Coefficients](../Explorations%203/EX42%20-%20Simpson%27s%20Rule%20by%20Undetermined%20Coefficients.md)

See also: [Newton-Cotes Rules](Newton-Cotes%20Rules.md), [Degree of Precision](Degree%20of%20Precision.md)
