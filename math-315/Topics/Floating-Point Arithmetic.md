---
tags: [math-315, topic, lecture-2]
---
# Floating-Point Arithmetic
Back to [[Index]] · Section 2.2 (slides 36–38)

Even when $x, y \in F$, the exact result of $x \circ y$ usually is not in $F$, so it gets rounded.

## Addition and subtraction
The operands are shifted to a common exponent, and the smaller one loses digits. If $|x| < |y|\,u$, the result is just $y$ (or $-y$): $x$ is **absorbed**.

With $\beta = 10$, $p = 10$: $\;2 \times 10^{4} + 3 \times 10^{-10} = 20000.0000000003 \to 2 \times 10^{4}$.

## Multiplication and division
No shifting is needed, but the exact product needs up to $2p$ digits and a quotient may need infinitely many. The exponents can also leave $[L, U]$ (see [[Overflow and Underflow]]).

## Arithmetic rules
- **Commutative:** yes, $x + y = y + x$.
- **Associative:** no, $x + (y + z) \ne (x + y) + z$ in general.

With $p = 5$, $x = 10^{10}$, $y = 1$, $z = -10^{10}$:
$$
(x + y) + z = 0, \qquad x + (y + z) = 0, \qquad (x + z) + y = 1
$$
Only the last one is correct.

## Explorations
- [[EX19 - Absorption and Non-Associativity]]
- [[EX20 - Overflow and Underflow in Base-10 Arithmetic]]

See also: [[Rounding and Machine Precision]], [[Cancellation Error]]
