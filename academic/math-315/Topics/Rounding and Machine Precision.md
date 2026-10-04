---
tags: [math-315, topic, lecture-2]
---
# Rounding and Machine Precision
Back to [Index](../Index.md) · Section 2.2 (slides 33–34)

## Rounding
$\operatorname{fl}(x)$ is the machine number obtained by rounding the real number $x$.
- **Chopping** (round toward zero): truncate after $p$ digits. $\operatorname{fl}(x)$ is the nearest machine number between $0$ and $x$.
- **Round to nearest**: $\operatorname{fl}(x)$ is the closest machine number. On a tie, choose the one whose last digit is **even**.

With $\beta = 10$, $p = 4$: chopping gives $\operatorname{fl}(2/3) = 0.6666$, and nearest gives $0.6667$.

## Machine precision
The **unit roundoff** $u$ is the bound
$$
\left|\frac{\operatorname{fl}(x) - x}{x}\right| \le u \qquad \text{for } \text{UFL} < |x| < \text{OFL}
$$
Equivalently $\operatorname{fl}(x) = x(1 + \delta)$ with $|\delta| \le u$.

## Value of $u$
$$
u = \beta^{1-p} \ \text{(chopping)}, \qquad u = \tfrac12\beta^{1-p} \ \text{(nearest)}
$$
IEEE double with rounding to nearest: $u = 2^{-53} \approx 1.11 \times 10^{-16}$. (MATLAB's `eps` $= 2^{-52}$ is the gap after $1$, which is $2u$.)

## Explorations
- [EX15 - Exploration 2.2.1 - Five-Digit Product of 100pi and 10e](../Explorations/EX15%20-%20Exploration%202.2.1%20-%20Five-Digit%20Product%20of%20100pi%20and%2010e.md)
- [EX17 - A Toy Binary Floating-Point System](../Explorations/EX17%20-%20A%20Toy%20Binary%20Floating-Point%20System.md)
- [EX05 - Four-Digit Arithmetic With and Without Pivoting](../Explorations/EX05%20-%20Four-Digit%20Arithmetic%20With%20and%20Without%20Pivoting.md)

See also: [Floating-Point Number Systems](Floating-Point%20Number%20Systems.md), [Floating-Point Arithmetic](Floating-Point%20Arithmetic.md), [IEEE Floating-Point Standard](IEEE%20Floating-Point%20Standard.md)
