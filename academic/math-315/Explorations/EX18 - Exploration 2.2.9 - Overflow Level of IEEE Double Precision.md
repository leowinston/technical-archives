---
tags: [math-315, exploration, lecture-2, floating-point]
source: Lecture 2 slides, slide 31 (Exploration 2.2.9), with slide 35 (IEEE table)
topics: ["[[Overflow and Underflow]]", "[[IEEE Floating-Point Standard]]"]
---
# EX18 — Exploration 2.2.9: Overflow Level of IEEE Double Precision
Back to [[academic/math-315/Index|Index]]

> [!question] Problem
> Determine OFL for a floating-point system with $\beta = 2$, $p = 53$, and $U = 1023$.
> Then, with $L = -1022$, find UFL and $u$ (rounding to nearest), and compare with single precision ($p = 24$, $L = -126$, $U = 127$).

## Setup
- **Formulas:** $\text{OFL} = \beta^{U+1}(1 - \beta^{-p})$, $\text{UFL} = \beta^{L}$, $u = \tfrac12\beta^{1-p}$
- **Double:** 11 exponent bits, 52 stored mantissa bits plus the hidden bit, so $p = 53$

## Strategy
1. Substitute into the OFL formula.
2. Explain the formula from the largest mantissa.
3. Evaluate numerically, in a way that doesn't overflow.
4. Repeat for UFL, $u$, and single precision.

## Solution
**Substitute.**
$$
\text{OFL} = 2^{1024}\left(1 - 2^{-53}\right)
$$

**Why the formula looks like this.** The largest mantissa has every bit equal to $1$:
$$
m_{\max} = (1.\underbrace{11\cdots1}_{52})_2 = \sum_{j=0}^{52} 2^{-j} = 2 - 2^{-52} = 2\left(1 - 2^{-53}\right)
$$
Multiplying by $2^{U} = 2^{1023}$ gives $2^{1024}(1 - 2^{-53})$. $\checkmark$

**Evaluate.**
$$
2^{-53} \approx 1.1102230246251565 \times 10^{-16}
$$
$$
\text{OFL} = 2^{1024}\left(1 - 1.1102230246251565 \times 10^{-16}\right) \approx \boxed{\,1.7976931348623157 \times 10^{308}\,}
$$
This is exactly Python's `sys.float_info.max`.

> [!warning] Evaluating it in double precision
> Typing `2.0**1024 * (1 - 2**-53)` fails: $2^{1024}$ is itself larger than OFL, so the first factor overflows. Rearrange so no intermediate result leaves the range:
> ```python
> 2.0**1023 * (2 - 2.0**-52)   # 1.7976931348623157e+308
> ```

**UFL and $u$.**
$$
\text{UFL} = 2^{-1022} \approx 2.2251 \times 10^{-308}, \qquad
u = \tfrac12 \cdot 2^{1-53} = 2^{-53} \approx 1.1102 \times 10^{-16}
$$
The same $2^{-53}$ appears in OFL and in $u$. That is not a coincidence: $1 - 2^{-53}$ is "one minus a unit roundoff".

**Single precision.**
$$
\begin{align*}
\text{OFL} &= 2^{128}\left(1 - 2^{-24}\right) \approx 3.4028 \times 10^{38} \\
\text{UFL} &= 2^{-126} \approx 1.1755 \times 10^{-38} \\
u &= 2^{-24} \approx 5.9605 \times 10^{-8}
\end{align*}
$$

## Result
| | Single | Double |
|---|---|---|
| OFL | $3.40 \times 10^{38}$ | $1.80 \times 10^{308}$ |
| UFL | $1.18 \times 10^{-38}$ | $2.23 \times 10^{-308}$ |
| $u$ | $5.96 \times 10^{-8}$ | $1.11 \times 10^{-16}$ |

## Takeaways
- $\text{OFL} \approx \beta^{U+1}$. The factor $1 - \beta^{-p}$ only changes the last digit.
- The range comes from the exponent bits and the precision from the mantissa bits.
- Computing a formula can overflow even when the answer is representable. Order the operations with care.
- Subnormals go below UFL, down to $2^{-1074} \approx 4.9 \times 10^{-324}$ in double, at reduced precision.

## Related topics
- [[Overflow and Underflow]]
- [[IEEE Floating-Point Standard]]
- [[Rounding and Machine Precision]]
