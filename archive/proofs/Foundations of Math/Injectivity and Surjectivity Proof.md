---
tags:
  - foundations-of-math
  - proof
  - final-portfolio
course: MATH 250
portfolio: "Final Portfolio - Foundations of Math - Spring 2026"
date: 2026-05-01
---
# Injectivity and Surjectivity Proof
Back to [[archive/proofs/Index|Index]]

*Final Portfolio - Foundations of Math - Spring 2026* · Leo Winston · May 1, 2026

<center>(Exam 3 Review #7)</center>

**Theorem:** The function $f: \mathbb{R}-\{0\} \rightarrow \mathbb{R}$ defined by $f(x) = \frac{x+1}{x}$ is injective, but not surjective.

*Proof.* Let $f: \mathbb{R} - \{0\} \rightarrow \mathbb{R}$ be defined by $f(x)=\frac{x+1}{x}$. We will show that $f$ is injective, and not surjective.

**Injective:**
Let $x_1,x_2$ be in the domain of $f$. Suppose $f(x_1) = f(x_2)$. By the definition of $f$, this yields:
$$
\frac{x_1+1}{x_1} = \frac{x_2+1}{x_2}.
$$
Since $x_1$ and $x_2$ are in the domain of $f$, it follows that they are both non-zero, which implies the product $x_1x_2 \ne 0$. So, we can multiply both sides of the equation by $x_1x_2$ to obtain:
$$
\begin{align*}
x_{1}x_{2}\left(\frac{x_1+1}{x_1}\right) &= x_{1}x_{2}\left(\frac{x_2+1}{x_2}\right) \\
x_2(x_1+1) &= x_1(x_2+1)\\
x_1x_2+x_2 &= x_1x_2+x_1 \\
x_2 &= x_1
\end{align*}
$$
We've shown that $f(x_1)=f(x_2)$ implies $x_1=x_2$. Therefore, by definition of function injectivity, $f$ is injective.

**Surjective:**
Consider $y = 1$, which is an element of the codomain $\mathbb{R}$. Assume, for the sake of contradiction, that $1=f(x)$ for some $x \in \mathbb{R} - \{0\}$. By definition of $f$, we have:
$$
\begin{align*}
1 &= \frac{x+1}{x}\\
x &= x+1 \\
0 &= 1
\end{align*}
$$
Because $x \neq 0$, we may multiply both sides of the equation by $x$. Subtracting both sides of the equation by $x$ yields $0 \ne 1$. This is a contradiction. Thus our original assumption, that there exists an $x \in \mathbb{R} - \{0\}$ such that $y=1=f(x)$, is false. Therefore, $f$ is not surjective, by definition of function surjectivity.

We've shown that the function $f$ is injective, but not surjective, so the theorem holds. $\blacksquare$
