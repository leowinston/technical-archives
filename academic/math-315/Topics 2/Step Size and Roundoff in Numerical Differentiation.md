---
tags: [math-315, topic, chapter-5]
---
# Step Size and Roundoff in Numerical Differentiation
Back to [Index](../Index.md) · Section 5.1 (textbook)

Shrinking $h$ cuts the truncation error, but $f(x+h) - f(x)$ subtracts two nearly equal numbers and then divides by a tiny $h$. That is [catastrophic cancellation](../Topics%201/Cancellation%20Error.md), magnified.

## Total error model
If each computed $f$ value has relative error at most $u = \varepsilon/2$:
$$
E_{\text{fwd}}(h) \approx \frac{h}{2}|f''| + \frac{\varepsilon|f|}{h}, \qquad
E_{\text{cen}}(h) \approx \frac{h^2}{6}|f'''| + \frac{\varepsilon|f|}{2h}
$$
Truncation falls with $h$ and roundoff grows like $1/h$, so the total error has a minimum.

## Best step size
Setting $E'(h) = 0$:
$$
\boxed{\,h^*_{\text{fwd}} = \sqrt{\frac{2\varepsilon|f|}{|f''|}} \sim \sqrt{\varepsilon} \approx 10^{-8}, \qquad
h^*_{\text{cen}} = \Big(\frac{3\varepsilon|f|}{2|f'''|}\Big)^{1/3} \sim \varepsilon^{1/3} \approx 10^{-5}\,}
$$
At best the forward difference keeps about $8$ digits and the central difference about $10$–$11$. Steps much smaller than $\sqrt{\varepsilon}$ are useless.

## Example
For $x^4$ at $x = 1$ in double precision, the forward error falls like $h$ until $h \approx 10^{-8}$. The central error falls like $h^2$ until $h \approx 10^{-5}$, then grows. At $h = 10^{-16}$, $1 + h$ rounds to $1$ and the forward difference returns $0$.

## Explorations
- [EX36 - Forward and Central Differences for x^4 at x = 1](../Explorations%202/EX36%20-%20Forward%20and%20Central%20Differences%20for%20x%5E4%20at%20x%20%3D%201.md)
- [EX37 - Optimal Step Size for the Derivative of e^x](../Explorations%202/EX37%20-%20Optimal%20Step%20Size%20for%20the%20Derivative%20of%20e%5Ex.md)

See also: [Finite Difference Formulas](Finite%20Difference%20Formulas.md), [Rounding and Machine Precision](../Topics%201/Rounding%20and%20Machine%20Precision.md)
