---
tags:
  - foundations-of-math
  - proof
  - final-portfolio
course: MATH 250
portfolio: "Final Portfolio - Foundations of Math - Spring 2026"
date: 2026-05-01
---
# Proof by Induction
Back to [[archive/proofs/Index|Index]]

*Final Portfolio - Foundations of Math - Spring 2026* · Leo Winston · May 1, 2026

<center>(Exam 2 Review #11)</center>

**Theorem:** If $n \in \mathbb{N}$, then
$1^3+2^3+3^3+4^3+\dots+n^3=\dfrac{n^2(n+1)^2}{4}$.

*Proof.* Let $n \in \mathbb{N}$, and let $P(n)$ be the statement
$$
\sum_{i=1}^{n} i^3 = 1^3 + 2^3 + \cdots + n^3 = \frac{n^2(n+1)^2}{4}.
$$

**Base Case:** Let $n = 1$. Then,
$$
\sum_{i=1}^{1} i^3 = 1^3 = 1,
$$
and
$$
\frac{n^2(n+1)^2}{4} = \frac{1^2(1+1)^2}{4} = \frac{1 \cdot 4}{4} = 1.
$$
Since both sides equal $1$, $P(1)$ holds.

**Inductive Hypothesis:** Suppose $P(k)$ holds for some $k \in \mathbb{N}$.
That is, suppose
$$
\sum_{i=1}^{k} i^3 = \frac{k^2(k+1)^2}{4}.
$$

**Inductive Step:** We want to show that $P(k+1)$ holds. By evaluating the sum up to $k+1$ and separating the final term, we may substitute our inductive hypothesis:
$$
\begin{align*}
\sum_{i=1}^{k+1}i^3
    &= \left(\sum_{i=1}^{k}i^3\right) + (k+1)^3 \\
    &= \frac{k^2(k+1)^2}{4} + (k+1)^3 \quad \text{(by the inductive hypothesis)} \\
    &= (k+1)^2 \left(\frac{k^2}{4} + (k+1)\right) \\
    &= (k+1)^2 \left(\frac{k^2 + 4(k+1)}{4}\right) \\
    &= (k+1)^2 \left(\frac{k^2 + 4k + 4}{4}\right).
\end{align*}
$$
Finally, by factoring $k^2+4k+4 = (k+2)^2$, we obtain:
$$
\sum_{i=1}^{k+1}i^3 = \frac{(k+1)^2(k+2)^2}{4}.
$$

This is precisely the statement $P(k+1)$. Since $P(1)$ holds, and $P(k)$ implies $P(k+1)$ for an arbitrary $k \in \mathbb{N}$, it follows by the principle of mathematical induction that $P(n)$ holds for all $n \in \mathbb{N}$. That is,
$$
\sum_{i=1}^{n} i^3 = \frac{n^2(n+1)^2}{4}. \tag*{$\blacksquare$}
$$
