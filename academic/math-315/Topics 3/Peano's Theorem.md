---
tags: [math-315, topic, chapter-5]
---
# Peano's Theorem
Back to [Index](../Index.md) · Section 5.2.2 (textbook)

Peano's theorem turns a rule's [DOP](Degree%20of%20Precision.md) into an error formula.

## Statement
If $R$ has $\text{DOP} = m$ and $f \in C^{m+1}[a, b]$, there is a kernel $K(x)$, independent of $f$, with
$$
I(f) - R(f) = \int_a^bK(x)f^{(m+1)}(x)\,dx
$$
When $K$ does not change sign (true for midpoint, trapezoidal, Simpson, Gauss, Lobatto),
$$
\boxed{\,I(f) - R(f) = \kappa\,f^{(m+1)}(\eta), \qquad \eta \in (a, b)\,}
$$

## Finding the Peano constant $\kappa$
Plug in $f = x^{m+1}$, whose $(m+1)$st derivative is the constant $(m+1)!$:
$$
\kappa = \frac{I(x^{m+1}) - R(x^{m+1})}{(m+1)!}
$$
These are the same numbers already computed when checking the DOP.

## Values on $[-1, 1]$
| Rule | DOP | $\kappa$ |
|---|---|---|
| Midpoint | 1 | $\tfrac13$ |
| Trapezoidal | 1 | $-\tfrac23$ |
| Simpson | 3 | $-\tfrac1{90}$ |
| Gauss 2-point | 3 | $\tfrac1{135}$ |

## Scaling with $h$
On an interval of length $h$, the error is $\bar\kappa\,h^{m+2}f^{(m+1)}(\eta)$. For Simpson on $[-\tfrac h2, \tfrac h2]$, $\kappa = -\tfrac{h^5}{2880}$. A composite rule with $N = (b-a)/h$ pieces then has error $O(h^{m+1})$.

## Explorations
- [EX42 - Simpson's Rule by Undetermined Coefficients](../Explorations%203/EX42%20-%20Simpson%27s%20Rule%20by%20Undetermined%20Coefficients.md)
- [EX43 - Simpson's Rule on a Short Interval and the Composite Error](../Explorations%203/EX43%20-%20Simpson%27s%20Rule%20on%20a%20Short%20Interval%20and%20the%20Composite%20Error.md)
- [EX45 - Two- and Three-Point Gauss Rules](../Explorations%203/EX45%20-%20Two-%20and%20Three-Point%20Gauss%20Rules.md)

See also: [Error in the Midpoint and Trapezoidal Rules](Error%20in%20the%20Midpoint%20and%20Trapezoidal%20Rules.md), [Simpson's Rule](Simpson%27s%20Rule.md)
