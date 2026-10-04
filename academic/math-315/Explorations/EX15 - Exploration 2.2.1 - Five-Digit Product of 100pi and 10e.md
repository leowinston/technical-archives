---
tags: [math-315, exploration, lecture-2, floating-point]
source: Lecture 2 slides, slide 22 (Exploration 2.2.1)
topics: ["[[Rounding and Machine Precision]]", "[[Floating-Point Arithmetic]]"]
---
# EX15 — Exploration 2.2.1: Five-Digit Product of 100π and 10e
Back to [Index](../Index.md)

> [!question] Problem
> Use scientific notation to write approximations of $100\pi$ and $10e$ with five significant digits. Multiply these approximations, keep only five significant digits, and write the result in the same notation. How accurate is this approximation of $1000e\pi$? What is the percentage error?

## Setup
- **True values:** $100\pi = 314.159265\ldots$, $\;10e = 27.182818\ldots$, $\;1000e\pi = 8539.734222673567\ldots$
- **Arithmetic:** $\beta = 10$, $p = 5$, rounding to nearest
- **Measure:** $E_{\text{rel}} = \dfrac{|\hat y - y|}{|y|}$

## Strategy
1. Round each input to 5 significant digits.
2. Multiply exactly, then round the product to 5 digits.
3. Compare with the true product.
4. Compare the result with $u = \tfrac12 \cdot 10^{1-5}$.

## Solution
**Step 1: Round the inputs.**
$$
\begin{align*}
100\pi &= 314.159265\ldots \to 3.1416 \times 10^{2} \\
10e &= 27.182818\ldots \to 2.7183 \times 10^{1}
\end{align*}
$$
(The slide writes $2.7183 \cdot 10$, which is the same thing.)

Their relative errors are
$$
\frac{|314.16 - 314.1593|}{314.1593} \approx 2.34 \times 10^{-6}, \qquad
\frac{|27.183 - 27.1828|}{27.1828} \approx 6.68 \times 10^{-6}
$$

**Step 2: Multiply and round.**
$$
3.1416 \times 10^{2} \times 2.7183 \times 10^{1} = 8.539811\ldots \times 10^{3} \to 8.5398 \times 10^{3}
$$
The exact product of two 5-digit mantissas has up to 10 digits. It has to be rounded back to 5.

**Step 3: Relative error.**
$$
E_{\text{rel}} = \left|\frac{8539.8 - 8539.734222673567}{8539.734222673567}\right| = \frac{0.065777}{8539.73} \approx \boxed{\,7.7025 \times 10^{-6}\,}
$$
The percentage error is about $\boxed{\,0.00077\%\,}$.

**Step 4: Compare with $u$.**
For $\beta = 10$, $p = 5$ with rounding to nearest,
$$
u = \tfrac12 \times 10^{1-5} = 5 \times 10^{-5}
$$
Each single rounding is within $u$. The final error is $7.7 \times 10^{-6}$, well under $3u$, which is the rough worst case for three roundings (two inputs and one product).

### Why the errors roughly add
Write $\hat a = a(1 + \delta_a)$, $\hat b = b(1 + \delta_b)$, and $\operatorname{fl}(\hat a\hat b) = \hat a\hat b(1 + \delta_\times)$. Then
$$
\operatorname{fl}(\hat a\hat b) = ab(1 + \delta_a)(1 + \delta_b)(1 + \delta_\times) \approx ab(1 + \delta_a + \delta_b + \delta_\times)
$$
Here $\delta_a \approx +2.34 \times 10^{-6}$, $\delta_b \approx +6.68 \times 10^{-6}$, and
$$
\delta_\times = \frac{8539.8 - 8539.81128}{8539.81128} \approx -1.32 \times 10^{-6}
$$
The sum is $2.34 + 6.68 - 1.32 = 7.70$, in units of $10^{-6}$. That matches $E_{\text{rel}}$. $\checkmark$

## Result
$$
1000e\pi \approx 8.5398 \times 10^{3}, \qquad E_{\text{rel}} \approx 7.70 \times 10^{-6} \approx 0.00077\%
$$

## Takeaways
- Multiplication does not amplify relative errors: they add, to first order.
- Every intermediate result is rounded, so even a single product carries three rounding errors.
- Compare with [EX21](EX21%20-%20Cancellation%20in%20the%20Quadratic%20Formula.md), where subtraction **does** amplify relative error.

## Related topics
- [Rounding and Machine Precision](../Topics/Rounding%20and%20Machine%20Precision.md)
- [Floating-Point Arithmetic](../Topics/Floating-Point%20Arithmetic.md)
