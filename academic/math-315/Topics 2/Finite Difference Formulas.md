---
tags: [math-315, topic, chapter-5]
---
# Finite Difference Formulas
Back to [Index](../Index.md) · Section 5.1 (textbook)

Replace the limit in $f'(x) = \lim_{h\to0}\frac{f(x+h) - f(x)}{h}$ with a fixed small $h$.

## Forward difference (first order)
Taylor: $f(x+h) = f(x) + hf'(x) + \tfrac{h^2}{2}f''(x) + \cdots$, so
$$
\boxed{\,f'(x) \approx \frac{f(x+h) - f(x)}{h}, \qquad \frac{f(x+h) - f(x)}{h} - f'(x) \approx \frac{h}{2}f''(x)\,}
$$
The error is $O(h)$: dividing $h$ by $10$ divides the error by $10$.

## Central difference (second order)
Subtracting the expansions of $f(x \pm h)$ cancels the even terms: $f(x+h) - f(x-h) \approx 2hf'(x) + \tfrac{h^3}{3}f'''(x)$, so
$$
\boxed{\,f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}, \qquad \text{error} \approx \frac{h^2}{6}f'''(x)\,}
$$
The error is $O(h^2)$: dividing $h$ by $10$ divides the error by $100$.

## Example
For $f(x) = x^4$ at $x = 1$ with $h = 10^{-2}$: forward gives $4.0604$ (error $\approx \tfrac h2 \cdot 12 = 0.06$), central gives $4.0004$ (error $\approx \tfrac{h^2}{6}\cdot 24 = 4\times10^{-4}$).

## When to use it
For a formula $f$, differentiate symbolically or with automatic differentiation instead. Finite differences are for functions known only through values, such as [tabulated data](Differentiating%20Tabulated%20Data.md).

## Explorations
- [EX36 - Forward and Central Differences for x^4 at x = 1](../Explorations%202/EX36%20-%20Forward%20and%20Central%20Differences%20for%20x%5E4%20at%20x%20%3D%201.md)

See also: [Step Size and Roundoff in Numerical Differentiation](Step%20Size%20and%20Roundoff%20in%20Numerical%20Differentiation.md), [Cancellation Error](../Topics%201/Cancellation%20Error.md)
