---
tags: [math-315, exploration, lecture-2, floating-point]
source: Lecture 2 slides, slides 36–38 (Example 2.2.11 and the associativity question)
topics: ["[[Floating-Point Arithmetic]]", "[[Rounding and Machine Precision]]"]
---
# EX19 — Absorption and Non-Associativity
Back to [[academic/math-315/Index|Index]]

> [!question] Problem
> (a) In a system with $\beta = 10$, $p = 10$, $L = -20$, $U = 20$, compute $\operatorname{fl}(x + y)$ for $x = 2 \times 10^{4}$ and $y = 3 \times 10^{-10}$.
> (b) With precision $p = 5$, let $x = 10^{10}$, $y = 1$, $z = -10^{10}$. Which is most accurate?
> (A) $(x + y) + z$ (B) $x + (y + z)$ (C) $(x + z) + y$ (D) It does not matter

## Setup
- **Rounding:** to nearest, after every operation
- **Absorption rule:** if $|y| < |x|\,u$ then $\operatorname{fl}(x + y) = x$
- **Unit roundoff:** $u = \tfrac12 \cdot 10^{1-p}$

## Strategy
1. Align exponents and see which digits survive.
2. Check the result against the absorption rule.
3. Evaluate each ordering in (b), rounding at every step.

## Solution
**(a) Absorption**

Align $y$ to the exponent of $x$:
$$
\begin{align*}
x &= 2.000000000 \times 10^{4} \\
y &= 0.00000000000003 \times 10^{4}
\end{align*}
$$
The exact sum is
$$
x + y = 20000.0000000003 = 2.00000000000003 \times 10^{4}
$$
which needs 15 significant digits. With $p = 10$ it rounds to
$$
\operatorname{fl}(x + y) = 2.000000000 \times 10^{4} = x
$$
Check the rule: $u = \tfrac12 \times 10^{-9}$, so $|x|\,u = 10^{-5}$, and $|y| = 3 \times 10^{-10} < 10^{-5}$. $\checkmark$

**(b) Three orderings with $p = 5$**

The exact answer is $x + y + z = 1$.

*(A) $(x + y) + z$*
$$
\begin{align*}
x + y &= 10000000001 = 1.0000000001 \times 10^{10} \to 1.0000 \times 10^{10} \\
(1.0000 \times 10^{10}) + (-10^{10}) &= \boxed{\,0\,}
\end{align*}
$$
$y$ was absorbed into $x$, since $1 < 10^{10} \cdot u = 5 \times 10^{5}$.

*(B) $x + (y + z)$*
$$
\begin{align*}
y + z &= -9999999999 \to -1.0000 \times 10^{10} \\
10^{10} + (-1.0000 \times 10^{10}) &= \boxed{\,0\,}
\end{align*}
$$
This time $y$ was absorbed into $z$.

*(C) $(x + z) + y$*
$$
\begin{align*}
x + z &= 10^{10} - 10^{10} = 0 \quad \text{(exact)} \\
0 + 1 &= \boxed{\,1\,}
\end{align*}
$$
The two large numbers cancel exactly first, so $y$ survives.

**Answer: (C).** (A) and (B) have a relative error of $100\%$.

### Commutativity still holds
Each single operation is "compute exactly, then round", and $x + y$ and $y + x$ have the same exact value. So $\operatorname{fl}(x + y) = \operatorname{fl}(y + x)$ always. Associativity involves **two** roundings, and they happen at different places depending on the grouping.

### Same thing in IEEE double
```python
>>> (1e10 + 1) - 1e10      # 1.0: p = 53 is enough to keep the 1
>>> (1e17 + 1) - 1e17      # 0.0: 1 < 1e17 * 2**-53, absorbed
>>> (1e17 - 1e17) + 1      # 1.0
```

## Result
- (a) $\operatorname{fl}(2 \times 10^{4} + 3 \times 10^{-10}) = 2 \times 10^{4}$.
- (b) $(x + z) + y = 1$ is correct. The other two orderings give $0$.

## Takeaways
- Floating-point addition is commutative but **not** associative.
- When adding numbers of very different sizes, combine the ones of similar size first. A common rule: sum from smallest magnitude to largest.
- (C) is only safe here because $x + z$ is exact. In general, subtracting nearly equal numbers causes [[Cancellation Error]].

## Related topics
- [[Floating-Point Arithmetic]]
- [[Rounding and Machine Precision]]
- [[Cancellation Error]]
