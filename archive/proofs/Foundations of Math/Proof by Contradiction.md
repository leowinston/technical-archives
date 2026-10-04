---
tags:
  - foundations-of-math
  - proof
  - partial-portfolio
course: MATH 250
portfolio: "Proof Portfolio- Foundations of Math- Spring 2026"
date: 2026-02-27
---
# Proof by Contradiction
Back to [Index](../Index.md)

*Proof Portfolio- Foundations of Math- Spring 2026* · Leo Winston · February 27, 2026

(Homework $3$ - Problem $\#6$) **Theorem:** For all positive real numbers $x$, the sum of $x$ and its reciprocal is greater than or equal to $2$

*Proof.* Let $x \in \R^+$ Suppose for the sake of contradiction that the sum of $x$ and its reciprocal is strictly less than $2$. Since the positive real numbers do not include zero, the reciprocal of $x$ is well-defined.

Since $x$ is strictly positive, we may multiply both sides of the inequality by $x$ without reversing the inequality sign or encountering zero-division:
$$
\begin{align*}
x+\frac{1}{x} &<2\\
x^2 + 1 &< 2x
\end{align*}
$$
By subtracting $2x$ from both sides, we can then factor the left-hand side of the inequality to obtain:
$$
\begin{align*}
x^2 -2x+1 &< 0 \\
(x-1)(x-1) &< 0 \\
(x-1)^2 &< 0
\end{align*}
$$
Under the domain of the real numbers, squaring any number yields a non-negative real number. Since $x \in \R,$ and $x-1$ is a real number, it follows that $(x-1)^2 \ge 0$. Thus we've reached a contradiction, since for our inequality to hold $(x-1)^2 < 0$. Consequently, our initial assumption that there exists a positive real $x$ where $x +\frac{1}{x} < 2$ must be false. Therefore, the sum of a positive real number and its reciprocal must be greater than or equal to 2. $\blacksquare$
