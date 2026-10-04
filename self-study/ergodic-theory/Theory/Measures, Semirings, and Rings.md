---
tags: [ergodic-theory, topic, measure-theory]
source: Measure theory notes (April 2026) §3–4
---
# Measures, Semirings, and Rings
Back to [Index](../Index.md) · Sections 3–4

## Measures
A **measure** on $(\Omega, \mathscr F)$ is $\mu : \mathscr F \to [0, \infty]$ with $\mu(\emptyset) = 0$ and **$\sigma$-additivity**: for disjoint $A_i$,
$$
\boxed{\,\mu\Big(\bigcup_{i=1}^\infty A_i\Big) = \sum_{i=1}^\infty \mu(A_i)\,}
$$
- $\mu(\Omega) = 1$: $(\Omega, \mathscr F, \mu)$ is a **probability space**. This is the same object as in [Axioms of Probability](../../probability/Notes/Axioms%20of%20Probability.md), with events restricted to $\mathscr F$.
- $\mu(\Omega) < \infty$: $\mu$ is **finite**.
- $\Omega = \bigcup A_i$ with every $\mu(A_i) < \infty$: $\mu$ is **$\sigma$-finite**.

## Semirings
To build measures on complicated sets (like the Borel sets of $\R$), start from simpler collections. $\mathcal S$ is a **semiring** if:
1. $\emptyset \in \mathcal S$
2. $A, B \in \mathcal S \implies A \cap B \in \mathcal S$
3. $A, B \in \mathcal S \implies B \setminus A = \bigcup_{i=1}^n C_i$ for disjoint $C_i \in \mathcal S$

Example: the half-open intervals $(a, b] \subseteq \R$.

## Rings
A **ring** $\mathcal R$ is a semiring that is also closed under finite unions: $A, B \in \mathcal R \implies A \cup B \in \mathcal R$.

See also: [Sequence Spaces and Sigma-Fields](Sequence%20Spaces%20and%20Sigma-Fields.md)
