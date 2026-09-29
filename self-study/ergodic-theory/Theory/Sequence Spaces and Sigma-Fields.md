---
tags: [ergodic-theory, topic, measure-theory]
source: Measure theory notes (April 2026) §1–2
---
# Sequence Spaces and Sigma-Fields
Back to [[self-study/ergodic-theory/Index|Index]] · Sections 1–2

## The big picture
Ergodic theory models systems whose probability laws stay constant over time. Fix a **state space** $\rho$ (e.g. $\{1, \dots, 6\}$ for a die) and run a **doubly infinite sequence** of experiments:
$$
\omega = (\dots, \omega_{-1}, \omega_0, \omega_1, \dots), \qquad \omega_i \in \rho
$$
The sample space $\Omega$ is the set of all such sequences.

## Measurable spaces
A **measurable space** is a pair $(\Omega, \mathscr F)$, where $\mathscr F$ is a **$\sigma$-field** of subsets of $\Omega$:
1. $\emptyset, \Omega \in \mathscr F$
2. $A \in \mathscr F \implies A^c \in \mathscr F$
3. $A_1, A_2, \dots \in \mathscr F \implies \bigcup_{i=1}^\infty A_i \in \mathscr F$

## Closed under countable intersection
By De Morgan,
$$
\boxed{\,\bigcap_{i=1}^\infty A_i = \Big(\bigcup_{i=1}^\infty A_i^c\Big)^c\,}
$$
Each $A_i^c \in \mathscr F$ by (2), so their union is in $\mathscr F$ by (3), and so is its complement by (2).

See also: [[Measures, Semirings, and Rings]]
