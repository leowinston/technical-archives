---
tags:
  - foundations-of-math
  - proof
  - final-portfolio
course: MATH 250
portfolio: "Final Portfolio - Foundations of Math - Spring 2026"
date: 2026-05-01
---
# Continuity Proof
Back to [Index](../Index.md)

*Final Portfolio - Foundations of Math - Spring 2026* · Leo Winston · May 1, 2026

<center>(Homework 10 #2)</center>

**Theorem:** The function $f: \mathbb{R} \rightarrow \mathbb{R}$ defined by $f(x) = 2x^2+1$ is continuous at $x=2$.

*Proof.* Let $f: \mathbb{R} \rightarrow \mathbb{R}$ be defined by $f(x)=2x^2+1$. We will show $f$ is continuous at the point $x=2$. Let $\epsilon > 0$. We choose $\delta = \min\{1, \frac{\epsilon}{10}\}$. By definition of the minimum element of a set, it follows that $\delta \le 1$ and $\delta \le \frac{\epsilon}{10}$. Suppose $x \in \mathbb{R}$ such that $|x-2| < \delta$.
Now, evaluate $|f(x)-f(2)|$. Using the function definition of $f$, and factoring the difference of squares yields:
$$
\begin{align*}
|f(x) - f(2)| &= |(2x^2+1) - (2(2)^2+1)| \\
&= |2x^2+1-9| \\
&= |2x^2-8| \\
&= 2|x^2-4| \\
&= 2|x-2||x+2|
\end{align*}
$$
We chose $\delta$ such that $|x-2| < \delta \le 1$. Consequently, $|x-2|$ must be strictly less than $1$. This implies:
$$
\begin{align*}
-1 < x - 2 &< 1\\
-1+4 < (x - 2)+4 &< 1 + 4\\
 3 < x + 2 &< 5
\end{align*}
$$
Since $-5 < 3$, we see that $-5<x+2<5$. It logically follows that $|x+2|$ is strictly less than 5. Since $|x+2| < 5$, and $|x-2| < \delta \le \frac{\epsilon}{10}$, we have:
$$
\begin{align*}
|f(x) - f(2)| &= 2|x-2||x+2|\\
&< 2 (\delta) (5) \\
&\le 10 \left(\frac{\epsilon}{10}\right) \\
&= \epsilon
\end{align*}
$$
Thus, $|f(x) - f(2)| < \epsilon$. Therefore, by the definition of continuity, $f$ is continuous at $x=2$. $\blacksquare$
