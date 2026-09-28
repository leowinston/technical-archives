---
tags: [math-315, exploration, lecture-2, floating-point]
source: Constructed example for Section 2.2 (slides 40–42, Example 2.2.13)
topics: ["[[Cancellation Error]]", "[[Rounding and Machine Precision]]"]
---
# EX21 — Cancellation in the Quadratic Formula
Back to [[Index]]

> [!question] Problem
> Solve $x^2 + 62.10x + 1 = 0$ using 4-digit arithmetic with rounding.
> (a) Use the standard formula for both roots and find the relative errors.
> (b) Explain the bad root using the cancellation error formula.
> (c) Recompute it with the rationalized formula $x_1 = \dfrac{-2c}{b + \sqrt{b^2 - 4ac}}$.

## Setup
- **Coefficients:** $a = 1$, $b = 62.10$, $c = 1$, so $b \gg a, c$ and $b > 0$
- **True roots:** $x_1 = -0.01610723\ldots$, $x_2 = -62.08389\ldots$
- **Arithmetic:** $\operatorname{fl}_4(\cdot)$ rounds every intermediate result to 4 significant digits

## Strategy
1. Compute the discriminant and its square root in 4 digits.
2. Form both roots with the standard formula.
3. Locate the subtraction of nearly equal numbers.
4. Rewrite $x_1$ so it has no subtraction.

## Solution
**(a) Standard formula**

*Discriminant.*
$$
\begin{align*}
b^2 &= \operatorname{fl}_4(3856.41) = 3856 \\
b^2 - 4ac &= 3856 - 4 = 3852 \\
\sqrt{3852} &= \operatorname{fl}_4(62.0645\ldots) = 62.06
\end{align*}
$$

*The "+" root.*
$$
x_1 = \frac{-62.10 + 62.06}{2} = \frac{-0.04000}{2} = -0.02000
$$
$$
E_{\text{rel}}(x_1) = \frac{|-0.02000 + 0.01610723|}{0.01610723} \approx \boxed{\,0.242\,} = 24\%
$$

*The "−" root.*
$$
x_2 = \frac{-62.10 - 62.06}{2} = \frac{\operatorname{fl}_4(-124.16)}{2} = \frac{-124.2}{2} = -62.10
$$
$$
E_{\text{rel}}(x_2) = \frac{|-62.10 + 62.08389|}{62.08389} \approx \boxed{\,2.6 \times 10^{-4}\,}
$$
$x_2$ is as good as 4 digits allow. $x_1$ has lost nearly all its digits.

**(b) Why $x_1$ failed**

$\sqrt{b^2 - 4ac} = 62.0678\ldots$ was rounded to $62.06$. That is a relative error of only
$$
\delta = \frac{62.06 - 62.0678}{62.0678} \approx -1.3 \times 10^{-4}
$$
The numerator then subtracts two nearly equal numbers, $62.10$ and $62.06$. From the cancellation formula,
$$
\hat x - \hat y = (x - y)\left(1 + \frac{x\delta_x - y\delta_y}{x - y}\right)
$$
the relative error is amplified by roughly
$$
\frac{|y|}{|x - y|} = \frac{62.07}{62.10 - 62.07} \approx \frac{62.07}{0.0322} \approx 1900
$$
And $1900 \times 1.3 \times 10^{-4} \approx 0.24$, which is the $24\%$ we saw. $\checkmark$ The subtraction itself was exact. It only **exposed** the earlier rounding error.

For $x_2$, the two terms have the same sign, so the magnitudes add and nothing is amplified.

**(c) Rationalized formula**

Multiply the top and bottom by the conjugate:
$$
x_1 = \frac{-b + \sqrt{b^2 - 4ac}}{2a} \cdot \frac{b + \sqrt{b^2 - 4ac}}{b + \sqrt{b^2 - 4ac}} = \frac{b^2 - (b^2 - 4ac)}{2a\left(b + \sqrt{b^2 - 4ac}\right)} = \frac{-2c}{b + \sqrt{b^2 - 4ac}}
$$
Now the denominator adds two positive numbers:
$$
x_1 = \frac{-2}{\operatorname{fl}_4(62.10 + 62.06)} = \frac{-2}{124.2} = \operatorname{fl}_4(-0.0161030\ldots) = -0.01610
$$
$$
E_{\text{rel}}(x_1) = \frac{|-0.01610 + 0.01610723|}{0.01610723} \approx \boxed{\,4.5 \times 10^{-4}\,}
$$
An equivalent fix is Vieta's formula: $x_1 x_2 = c/a$, so $x_1 = c/(a x_2) = 1/(-62.10) = -0.01610$.

## Comparison
| | Formula | 4-digit value | Rel. error |
|---|---|---|---|
| $x_1$ | $\dfrac{-b + \sqrt{\cdot}}{2a}$ | $-0.02000$ | $24\%$ |
| $x_1$ | $\dfrac{-2c}{b + \sqrt{\cdot}}$ | $-0.01610$ | $0.045\%$ |
| $x_2$ | $\dfrac{-b - \sqrt{\cdot}}{2a}$ | $-62.10$ | $0.026\%$ |

## Takeaways
- Cancellation doesn't create error. It magnifies error that is already there, by about $|x|/|x - y|$.
- For $b > 0$, compute $x_2$ with the standard formula and $x_1$ with $-2c/(b + \sqrt{\cdot})$ or $c/(ax_2)$. For $b < 0$, swap the roles.
- Algebraically equal formulas can behave very differently in floating point.

## Related topics
- [[Cancellation Error]]
- [[Rounding and Machine Precision]]
- [[Floating-Point Arithmetic]]
