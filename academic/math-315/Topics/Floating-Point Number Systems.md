---
tags: [math-315, topic, lecture-2]
---
# Floating-Point Number Systems
Back to [Index](../Index.md) · Section 2.2 (slides 23–25, 29, 32)

## Definition
Given a base $\beta > 1$, precision $p \ge 1$, and exponent range $L \le E \le U$, the system $F$ is the set of all
$$
x = \pm\, m\,\beta^{E}, \qquad m = \sum_{j=0}^{p-1} d_j\,\beta^{-j}, \quad 0 \le d_j \le \beta - 1
$$
$m$ is the **mantissa** and $E$ is the **exponent**.

## Normalization
Require $d_0 \ne 0$, so $1 \le m < \beta$. This makes every representation unique. In binary $d_0$ is always $1$, so it need not be stored, which gains one extra bit of precision.

## Example
$$
-117 = -(1.17)\times 10^{2} = -(1.110101)_2 \times 2^{6}
$$
In base 10, $p = 3$. In base 2, $(1.110101)_2 = 1 + \tfrac12 + \tfrac14 + \tfrac1{16} + \tfrac1{64} = \tfrac{117}{64}$.

## Spacing
Floating-point numbers are **not** equally spaced. Within $[\beta^{E}, \beta^{E+1})$ the gap is $\beta^{E-p+1}$, so the gap grows with $|x|$ while the *relative* gap stays roughly constant.

## Explorations
- [EX16 - Base-2 Representation of -117 and 0.1](../Explorations/EX16%20-%20Base-2%20Representation%20of%20-117%20and%200.1.md)
- [EX17 - A Toy Binary Floating-Point System](../Explorations/EX17%20-%20A%20Toy%20Binary%20Floating-Point%20System.md)

See also: [Exponent and Mantissa](Exponent%20and%20Mantissa.md), [Overflow and Underflow](Overflow%20and%20Underflow.md), [Rounding and Machine Precision](Rounding%20and%20Machine%20Precision.md)
