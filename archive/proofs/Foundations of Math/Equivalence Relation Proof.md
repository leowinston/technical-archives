---
tags:
  - foundations-of-math
  - proof
  - final-portfolio
course: MATH 250
portfolio: "Final Portfolio - Foundations of Math - Spring 2026"
date: 2026-05-01
---
# Equivalence Relation Proof
Back to [[archive/proofs/Index|Index]]

*Final Portfolio - Foundations of Math - Spring 2026* · Leo Winston · May 1, 2026

<center>(Homework 8 #5)</center>

**Theorem:** Let $R$ be the relation on $\mathbb{Z}$ defined by $aRb$ if $a^2-b^2$ is divisible by $4$. The relation $R$ is an equivalence relation on $\mathbb{Z}$.

*Proof.* Let $R$ be the relation on $\mathbb{Z}$ defined by $aRb$ if $4 \mid (a^2-b^2)$. We will prove that $R$ is an equivalence relation by showing it is reflexive, symmetric, and transitive.

**Reflexive:** Let $a \in \mathbb{Z}.$ Since $a^2 - a^2 = 0 = 4(0)$, and $0 \in \mathbb{Z}$, it follows by definition of divides that $4 \mid (a^2-a^2)$. Thus, $aRa$ by definition of $R$, so the relation $R$ is reflexive.

**Symmetric:** Let $a,b \in \mathbb{Z}$ such that $aRb$. By definition of $R$, $4 \mid (a^2-b^2)$. By definition of divides, $a^2-b^2=4k$ for some integer $k$. Multiplying both sides of the equation by $-1$ yields $b^2-a^2 = 4(-k)$. Since $k$ is an integer, $-k$ is also an integer. Thus, by definition of divides, $4 \mid (b^2 - a^2)$. Therefore, $bRa$ by definition of $R$, proving that $R$ is symmetric.

**Transitive:** Let $a,b,c \in \mathbb{Z}$ such that $aRb$ and $bRc$. By definition of $R$, there exist integers $k$ and $n$ such that $a^2-b^2=4k$ and $b^2-c^2=4n$. Adding these two equations yields:
$$
(a^2-b^2) + (b^2-c^2) = 4k + 4n
$$
By simplifying the left-hand side and factoring the right-hand side, we obtain $a^2 - c^2 = 4(k+n)$. Since $k$ and $n$ are integers, their sum $k+n$ is also an integer due to closure under addition. Thus, by definition of divides, $4 \mid (a^2-c^2)$. Therefore, $aRc$ by definition of $R$, proving that $R$ is transitive.

Because the relation $R$ is reflexive, symmetric, and transitive, it is an equivalence relation on $\mathbb{Z}$. $\blacksquare$
