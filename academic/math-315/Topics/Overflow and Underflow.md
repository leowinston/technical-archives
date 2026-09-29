---
tags: [math-315, topic, lecture-2]
---
# Overflow and Underflow
Back to [[academic/math-315/Index|Index]] · Section 2.2 (slides 30–31, 39)

## Definitions
The **underflow level** is the smallest positive number in $F$, and the **overflow level** is the largest:
$$
\text{UFL} = m_{\min}\,\beta^{L} = \beta^{L}, \qquad
\text{OFL} = \beta^{U+1}\left(1 - \beta^{-p}\right)
$$
OFL has every digit equal to $\beta - 1$ and exponent $U$.

## IEEE double
With $\beta = 2$, $p = 53$, $L = -1022$, $U = 1023$:
$$
\text{OFL} \approx 1.7977 \times 10^{308}, \qquad \text{UFL} \approx 2.2251 \times 10^{-308}
$$

## In arithmetic
In multiplication and division the exponents add or subtract, so the result can fall outside $[L, U]$.
- Exponent $> U$: **overflow** (usually $\pm\infty$).
- Exponent $< L$: **underflow**, usually rounded to $0$.

## Example
With $\beta = 10$, $L = -20$, $U = 20$, $x = 4 \times 10^{18}$, $y = -2 \times 10^{-17}$:
$$
x/y = -2 \times 10^{35} \ \text{overflows}, \qquad y^2 = 4 \times 10^{-34} \ \text{underflows to } 0
$$
Of the four operations on two positive numbers, only subtraction can never overflow.

## Explorations
- [[EX18 - Exploration 2.2.9 - Overflow Level of IEEE Double Precision]]
- [[EX20 - Overflow and Underflow in Base-10 Arithmetic]]
- [[EX17 - A Toy Binary Floating-Point System]]

See also: [[Floating-Point Number Systems]], [[IEEE Floating-Point Standard]]
