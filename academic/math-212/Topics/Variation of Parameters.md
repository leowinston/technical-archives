---
tags: [math-212, topic, chapter-2]
---
# Variation of Parameters
Back to [Index](../Index.md) · Chapter 2.1

For $y' + p(x)y = f(x)$:
1. Solve the **complementary** (homogeneous) equation $y_1' + p y_1 = 0$, which gives $y_1 = e^{-\int p\,dx}$.
2. Replace the constant with a function by looking for $y = u(x)\,y_1(x)$.
3. Substitute. The terms with $u$ cancel and leave $u' y_1 = f$.

$$
\begin{align*}
u' &= \frac{f(x)}{y_1(x)} \\
y &= y_1(x)\left[\int \frac{f(x)}{y_1(x)}\,dx + c\right]
\end{align*}
$$

Since $1/y_1 = \mu$, this is the same answer the [integrating factor method](Linear%20First-Order%20Equations.md) gives.

## Workbook problems
- [WB1 P11 - Deriving Variation of Parameters](../Workbook%201/WB1%20P11%20-%20Deriving%20Variation%20of%20Parameters.md)
- [WB1 P12 - Problem 10 by Variation of Parameters](../Workbook%201/WB1%20P12%20-%20Problem%2010%20by%20Variation%20of%20Parameters.md)
