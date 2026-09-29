---
tags:
  - foundations-of-math
  - proof
  - partial-portfolio
course: MATH 250
portfolio: "Proof Portfolio- Foundations of Math- Spring 2026"
date: 2026-02-27
---
# If and only If (Equivalence) Proof
Back to [[archive/proofs/Index|Index]]

*Proof Portfolio- Foundations of Math- Spring 2026* · Leo Winston · February 27, 2026

(Exam 1 Review $\#2.l$) **Theorem:** For $n \in \mathbb{N}$, $n, n+2$ and $n+4$ are all prime if and only if $n=3$.

*Proof.* Let $n \in \N$. We want to show that $n,n+2,n+4$ are all prime if and only if $n = 3$. We will begin by proving the backward implication. Suppose $n = 3$. By the definition of a prime number, a natural number $p > 1$ is prime if its only divisors are $1$ and $p$. The only factors of $n = 3$ are $3$ and $1$, the only factors of $n+2 = 5$ are $5$ and $1$, and the only factors of $n+4 = 7$ are $7$ and $1$. Therefore, $n, n+2,n+4$ are all prime. So, the backward implication holds.

Now, suppose $(n\text{ is prime}) \wedge (n+2\text{ is prime}) \wedge (n+4\text{ is prime})$. Since $n \in \N$, it can be represented in terms of its remainder when divided by 3, by the division algorithm. Thus, $\exists k \in \mathbb{Z}$ such that $n = 3k, n =3k+1$, or $n=3k+2$. We will analyze these three cases.

**Case 1:** Suppose $n = 3k$. Since $n$ is prime, and the only prime divisible by 3 is 3 itself, then $n = 3$.

**Case 2:** Suppose $n = 3k+1$. Then:
$$
\begin{align*}
n &= 3k+1 \\
n + 2 &= 3k+3 \\
n + 2 &= 3(k+1)
\end{align*}
$$
This shows $n+2$ is a multiple of 3. Since $n+2$ is prime, it must be that $n+2=3$, which implies $n=1$. However, 1 is not prime by definition, contradicting our assumption that $n$ is prime. Thus, this case is impossible.

**Case 3:** Suppose $n = 3k+2$. Then:
$$
\begin{align*}
n &= 3k+2 \\
n + 4 &= 3k+6 \\
n + 4 &= 3(k+2)
\end{align*}
$$
This shows $n+4$ is a multiple of 3. Since $n+4$ is prime, it must be that $n + 4 =3$. However, this implies $n=-1$, which contradicts $n \in \N$. Thus, this case is also impossible. In all valid cases, $n = 3$, so we've shown the forward implication. Since we've proven both implications, $n, n+2, n+4$ are all prime if and only if $n = 3$. $\blacksquare$
