---
tags: [math-315, topic, chapter-5]
---
# Degree of Precision
Back to [Index](../Index.md) · Section 5.2.2 (textbook)

The degree of precision (DOP) measures how many polynomials a rule integrates exactly.

## Definition
$R(f) = \sum w_if(x_i)$ has $\text{DOP} = m$ if $R(f) = I(f)$ for every polynomial of degree $\le m$, but not for some polynomial of degree $m + 1$.

## Test with monomials
By linearity, it is enough to check powers of $x$:
$$
\boxed{\,\text{DOP} = m \iff R(x^r) = I(x^r) \text{ for } r = 0, \dots, m, \text{ and } R(x^{m+1}) \ne I(x^{m+1})\,}
$$
A higher DOP usually means a more accurate rule.

## Method of undetermined coefficients
Fix the points, then choose the weights so the **equations of precision** hold in order, $r = 0, 1, 2, \dots$, with none skipped:
$$
\sum_{i=0}^{N}w_ix_i^r = \int_{-1}^{1}x^r\,dx = \begin{cases}\tfrac{2}{r+1} & r \text{ even} \\ 0 & r \text{ odd}\end{cases}
$$
$N + 1$ weights satisfy $r = 0, \dots, N$. Then test $r = N+1, N+2, \dots$ to see how far it actually holds.

## Example
For $w_0f(-1) + w_1f(0) + w_2f(1)$: $r = 0, 1, 2$ give $w_0 = w_2 = \tfrac13$, $w_1 = \tfrac43$ (Simpson). $r = 3$ also holds since both sides are $0$, but $r = 4$ gives $\tfrac23 \ne \tfrac25$. So $\text{DOP} = 3$.

## Common values
Midpoint and trapezoidal: $1$. Simpson and Weddle: $3$. $(N+1)$-point Gauss: $2N + 1$. $(N+1)$-point Lobatto: $2N - 1$.

## Explorations
- [EX42 - Simpson's Rule by Undetermined Coefficients](../Explorations%203/EX42%20-%20Simpson%27s%20Rule%20by%20Undetermined%20Coefficients.md)
- [EX44 - Weddle's Three-Eighths Rule and the Two-Point Open Rule](../Explorations%203/EX44%20-%20Weddle%27s%20Three-Eighths%20Rule%20and%20the%20Two-Point%20Open%20Rule.md)

See also: [Peano's Theorem](Peano%27s%20Theorem.md), [Quadrature Rules](Quadrature%20Rules.md)
