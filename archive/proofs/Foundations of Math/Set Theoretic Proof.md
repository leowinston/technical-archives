---
tags:
  - foundations-of-math
  - proof
  - final-portfolio
course: MATH 250
portfolio: "Final Portfolio - Foundations of Math - Spring 2026"
date: 2026-05-01
---
# Set Theoretic Proof
Back to [Index](../Index.md)

*Final Portfolio - Foundations of Math - Spring 2026* · Leo Winston · May 1, 2026

<center>(Homework 3 #14)</center>

**Theorem:** Let $A, B$, and $C$ be arbitrary sets. If $A-C \nsubseteq A-B$, then $B \nsubseteq C$.

*Proof.* Let $A, B, C$ be arbitrary sets. We will proceed by proving the contrapositive. That is, we will show $B \subseteq C$ implies $A-C \subseteq A-B$. Assume $B \subseteq C$, and let $x$ be an arbitrary element of $A - C$. By definition of set difference, $x \in A - C$ implies $x \in A$ and $x \not \in C$. By definition of a subset, the assumption $B \subseteq C$ means every element of $B$ is also an element of $C$. Consequently, since $x \notin C$, it logically follows $x \notin B$.
Now we have established that $x \in A$ and $x \notin B$. By definition of set difference, this implies $x \in A - B$. So, by definition of subset, $A - C \subseteq A - B$. Thus, we have proven the contrapositive. Therefore, the original statement holds: if $A - C \not\subseteq A - B$, then $B \not\subseteq C$. $\blacksquare$
