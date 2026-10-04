---
tags: [math-315, topic, lecture-2]
---
# Cancellation Error
Back to [Index](../Index.md) · Section 2.2 (slides 40–42)

**Catastrophic cancellation** happens when two nearly equal numbers are subtracted. The leading digits cancel, and what is left is mostly roundoff.

## Error analysis
With $\hat x = x(1 + \delta_x)$ and $\hat y = y(1 + \delta_y)$:
$$
\hat x - \hat y = (x - y)\left(1 + \frac{x\delta_x - y\delta_y}{x - y}\right)
$$
The relative error can be as large as $u\,\dfrac{|x| + |y|}{|x - y|}$, which blows up when $x \approx y$.

## Example
True lengths $L_1 = 253.51$, $L_2 = 252.49$ cm are measured as $254$ and $252$ cm, each with under $2\%$ error. The difference is $2$ cm instead of $1.02$ cm, an error of about $100\%$.

## Quadratic formula
For $ax^2 + bx + c = 0$ with $|b| \gg |a|, |c|$, $\sqrt{b^2 - 4ac} \approx |b|$. When $b > 0$, $x_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a}$ cancels. Rationalize instead:
$$
x_1 = \frac{-2c}{b + \sqrt{b^2 - 4ac}}
$$
When $b < 0$, the same problem hits $x_2$.

## Prevention
Avoid computing small values by subtracting nearly equal numbers. Rearrange the formula instead.

## Explorations
- [EX21 - Cancellation in the Quadratic Formula](../Explorations/EX21%20-%20Cancellation%20in%20the%20Quadratic%20Formula.md)

See also: [Floating-Point Arithmetic](Floating-Point%20Arithmetic.md), [Rounding and Machine Precision](Rounding%20and%20Machine%20Precision.md)
