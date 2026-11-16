---
tags: [math-315, topic, chapter-5]
---
# Simpson's Rule
Back to [Index](../Index.md) · Section 5.2.2 (textbook)

Simpson's rule integrates the quadratic through $a$, $\tfrac{a+b}{2}$, $b$. It is the closed 3-point [Newton-Cotes rule](Newton-Cotes%20Rules.md) and the 3-point [Lobatto rule](Lobatto%20Rules.md).

## Rule and error
$$
\boxed{\,\int_a^bf(x)\,dx \approx \frac{b - a}{6}\Big[f(a) + 4f\big(\tfrac{a+b}{2}\big) + f(b)\Big], \qquad
I - R = -\frac{(b - a)^5}{2880}f^{(4)}(\eta)\,}
$$
The DOP is $3$: it is exact for cubics even though it is built from a quadratic. On $[-1, 1]$ the Peano constant is $-\tfrac1{90}$.

## Composite Simpson
Apply Simpson on each of $N$ subintervals of length $H$, using each midpoint. The MVT for sums gives
$$
I - R_{CS} = -\frac{(b - a)H^4}{2880}f^{(4)}(\eta)
$$
In terms of the node spacing $h = H/2$ (an even number $2N$ of panels), this is $-\tfrac{(b-a)h^4}{180}f^{(4)}(\eta)$, with weights $\tfrac h3(1, 4, 2, 4, \dots, 2, 4, 1)$. Halving $h$ divides the error by $16$.

## In Python
```python
S = scipy.integrate.simpson(f(xs), x=xs)
```

## Explorations
- [EX42 - Simpson's Rule by Undetermined Coefficients](../Explorations%203/EX42%20-%20Simpson%27s%20Rule%20by%20Undetermined%20Coefficients.md)
- [EX43 - Simpson's Rule on a Short Interval and the Composite Error](../Explorations%203/EX43%20-%20Simpson%27s%20Rule%20on%20a%20Short%20Interval%20and%20the%20Composite%20Error.md)
- [EX48 - Composite Rule Convergence for e^x on 0 to 1](../Explorations%203/EX48%20-%20Composite%20Rule%20Convergence%20for%20e%5Ex%20on%200%20to%201.md)

See also: [Peano's Theorem](Peano%27s%20Theorem.md), [Degree of Precision](Degree%20of%20Precision.md)
