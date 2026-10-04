---
tags:
  - foundations-of-math
  - proof
  - partial-portfolio
course: MATH 250
portfolio: "Proof Portfolio- Foundations of Math- Spring 2026"
date: 2026-02-27
---
# Direct Proof
Back to [Index](../Index.md)

*Proof Portfolio- Foundations of Math- Spring 2026* · Leo Winston · February 27, 2026

(Exam 1 Review $\#2.i$) **Theorem:** For every integer $a$, the numbers $a$ and $(a+1)(a-1)$ have opposite parity.

*Proof.* Suppose $a \in \mathbb{Z}$. We will show that $a$ has opposite parity to the quantity $(a+1)(a-1)$. First, suppose $a$ is even. By definition of even integers, $a = 2k$ for some $k \in \mathbb{Z}$. Then, we want to show that the quantity $(a+1)(a-1)$ is odd:
$$
\begin{align*}
(a+1)(a-1) &= ((2k)+1)((2k)-1) \\
&= (2k+1)(2k-1) \\
&= 4k^2-2k+2k-1 \\
&= 4k^2-1
\end{align*}
$$
To write this result as an odd integer, we rewrite the constant $-1$ as $-2+1$, allowing us to factor out a $2$ from the leading terms:
$$
\begin{align*}
&= 4k^2-2+1 \\
&= 2(2k^2-1)+1
\end{align*}
$$
Because $k$ is an integer, $2k^2 - 1$ is also an integer, as the integers are closed under multiplication and subtraction. Thus, in the case that $a$ is even, $(a+1)(a-1)$ must be odd by the definition of an odd integer.

Now, suppose that $a$ is an odd integer. Then, by definition, there exists $t \in \mathbb{Z}$ such that $a=2t+1$:
$$
\begin{align*}
(a+1)(a-1) &= ((2t+1)+1)((2t+1)-1)
\end{align*}
$$
By simplifying the constants before multiplying, we can reveal a common factor of $2$:
$$
\begin{align*}
&= (2t+2)(2t) \\
&= 4t^2 + 4t \\
&= 2(2t^2+2t)
\end{align*}
$$
Since $t \in \mathbb{Z}$, $2t^2+2t$ must also be an integer, as the integers are closed under multiplication and addition. Then, $(a+1)(a-1)$ must be an even integer since it is divisible by two. Thus, in the case that $a$ is odd, $(a+1)(a-1)$ is even. So, in all cases, $a$ and $(a+1)(a-1)$ have opposite parity. $\blacksquare$
