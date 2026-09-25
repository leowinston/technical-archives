---
tags: [math-212, topic, chapter-2]
---
# Variation of Parameters
Back to [[Index]] · Chapter 2.1

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

Since $1/y_1 = \mu$, this is the same answer the [[Linear First-Order Equations|integrating factor method]] gives.

## Workbook problems
- [[WB1 P11 - Deriving Variation of Parameters]]
- [[WB1 P12 - Problem 10 by Variation of Parameters]]
