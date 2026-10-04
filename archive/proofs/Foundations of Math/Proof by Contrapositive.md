---
tags:
  - foundations-of-math
  - proof
  - partial-portfolio
course: MATH 250
portfolio: "Proof Portfolio- Foundations of Math- Spring 2026"
date: 2026-02-27
---
# Proof by Contrapositive
Back to [Index](../Index.md)

*Proof Portfolio- Foundations of Math- Spring 2026* · Leo Winston · February 27, 2026

(Exam 1 Review $\#2.j$) **Theorem:** Suppose $x \in \R$. If $x^2$ is irrational, then $x$ is irrational.

*Proof.* Let $x \in \R$. For this proof, we will show the contrapositive, that is, we will prove that $x$ is rational, then $x^2$ is rational. Assume $x \in \mathbb{Q}$. Then, by definition of a rational number, $\exists p,q \in \mathbb{Z}$ such that $x = \frac{p}{q}$, where $q \ne 0$:
$$
\begin{align*}
x&=\frac{p}{q}
\end{align*}
$$
Squaring both sides and distributing yields:
$$
\begin{align*}
x^2&=(\frac{p}{q})^2 \\
x^2&=\frac{p^2}{q^2}
\end{align*}
$$
Because $p,q \in \Z$ and the integers are closed under multiplication, $p^2$ and $q^2$ must also both be integers. Furthermore, $q \ne 0$ implies $q^2 =q \cdot q \ne 0$, since the product of nonzero integers yields a nonzero integer. By definition of a rational number, $x^2 \in \Q$. Therefore, we have proven the contrapositive, and it follows that if $x^2$ is irrational, $x$ must also be irrational. $\blacksquare$
