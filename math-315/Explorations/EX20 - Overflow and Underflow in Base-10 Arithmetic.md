---
tags: [math-315, exploration, lecture-2, floating-point]
source: Lecture 2 slides, slides 39 and 43 (Example 2.2.12 and Concept Check Q2)
topics: ["[[Overflow and Underflow]]", "[[Floating-Point Arithmetic]]"]
---
# EX20 — Overflow and Underflow in Base-10 Arithmetic
Back to [[Index]]

> [!question] Problem
> Use a system with $\beta = 10$, $L = -20$, $U = 20$, and let $x = 4 \times 10^{18}$, $y = -2 \times 10^{-17}$.
> (a) Which of $xy$, $x/y$, $x^2$, $y^2$ overflow or underflow?
> (b) Of the four basic operations, which cannot overflow when applied to two positive numbers?

## Setup
- **Representable:** both $x$ and $y$ have exponents in $[-20, 20]$
- **Rule:** in $\times$ and $\div$ the mantissas multiply or divide and the exponents add or subtract
- **Normalization:** a mantissa product $\ge 10$ adds $1$ to the exponent, and a quotient $< 1$ subtracts $1$

## Strategy
1. For each operation, compute the mantissa and exponent separately.
2. Normalize and compare the exponent with $[L, U]$.
3. For (b), bound each result in terms of the operands.

## Solution
**(a) The four operations**

*$xy$:*
$$
(4)(-2) \times 10^{18 + (-17)} = -8 \times 10^{1}
$$
Exponent $1 \in [-20, 20]$: **fine.**

*$x/y$:*
$$
\frac{4}{-2} \times 10^{18 - (-17)} = -2 \times 10^{35}
$$
Exponent $35 > U = 20$: **overflow.**

*$x^2$:*
$$
16 \times 10^{36} = 1.6 \times 10^{37}
$$
Exponent $37 > 20$: **overflow.**

*$y^2$:*
$$
4 \times 10^{-34}
$$
Exponent $-34 < L = -20$: **underflow**, rounded to $0$.

| Operation | Exact | Exponent | Outcome |
|---|---|---|---|
| $xy$ | $-8 \times 10^{1}$ | $1$ | OK |
| $x/y$ | $-2 \times 10^{35}$ | $35$ | overflow |
| $x^2$ | $1.6 \times 10^{37}$ | $37$ | overflow |
| $y^2$ | $4 \times 10^{-34}$ | $-34$ | underflow $\to 0$ |

Note that $xy$ is fine even though $x$ is huge and $y$ is tiny. The exponents nearly cancel.

**(b) Which operations can't overflow?**

Let $0 < a, b \le \text{OFL}$.
- **Addition:** $\text{OFL} + \text{OFL} = 2\,\text{OFL}$. **Can** overflow.
- **Multiplication:** $10^{15} \cdot 10^{15} = 10^{30}$. **Can** overflow.
- **Division:** $10^{15} / 10^{-15} = 10^{30}$. **Can** overflow.
- **Subtraction:** $|a - b| < \max(a, b) \le \text{OFL}$. **Cannot** overflow.

**Answer: only subtraction.** (Subtraction can still lose accuracy through cancellation, and $a - b$ can be tiny, but it never exceeds OFL.)

### Avoiding it
If $x^2$ appears only as an intermediate, rescale. For example,
$$
\sqrt{x^2 + y^2} = |x|\sqrt{1 + (y/x)^2} \qquad (|x| \ge |y|)
$$
never forms $x^2$. This is what `hypot` does, and why norm routines scale first.

## Result
- $xy = -80$: fine.
- $x/y$ and $x^2$: overflow.
- $y^2$: underflows to $0$.
- Only subtraction of two positive numbers can never overflow.

## Takeaways
- Overflow and underflow depend on the **exponents**, not on the precision.
- Underflow to $0$ is silent and can be dangerous. For example, $y^2/y^2$ becomes $0/0$.
- Reorder or rescale so that intermediate results stay in range.

## Related topics
- [[Overflow and Underflow]]
- [[Floating-Point Arithmetic]]
- [[Vector Norms]]
