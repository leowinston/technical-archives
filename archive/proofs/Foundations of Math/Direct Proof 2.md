---
tags:
  - foundations-of-math
  - proof
  - final-portfolio
course: MATH 250
portfolio: "Final Portfolio - Foundations of Math - Spring 2026"
date: 2026-05-01
---
# Direct Proof
Back to [Index](../Index.md)

*Final Portfolio - Foundations of Math - Spring 2026* · Leo Winston · May 1, 2026

<center>(Problem #5 Homework #3)</center>

**Theorem:** For all positive real numbers $x$, the sum of $x$ and its reciprocal is greater than or equal to $2$.

*Proof.* Let $x \in \mathbb{R}^+$. Since $x$ is a real number, $x-1$ is also a real number. A fundamental property of the real numbers is that the square of any real number is non-negative. Therefore, we establish that:
$$
(x-1)^2 \ge 0
$$
Expanding the left-hand side yields:
$$
x^2 - 2x + 1 \ge 0
$$
By adding $2x$ to both sides of the inequality, we obtain:
$$
x^2 + 1 \ge 2x
$$
Because $x \in \mathbb{R}^+$, $x$ is strictly positive. Therefore, we can divide both sides of the inequality by $x$ without encountering zero-division or reversing the direction of the inequality sign. Doing so results in:
$$
\begin{align*}
\frac{x^2 + 1}{x} &\ge \frac{2x}{x} \\
\frac{x^2}{x} + \frac{1}{x} &\ge 2 \\
x + \frac{1}{x} &\ge 2
\end{align*}
$$
Thus, for any positive real number $x$, the sum of $x$ and its reciprocal is greater than or equal to $2$. $\blacksquare$
