---
tags: [proofs, index]
---
# Proofs Index

My proofs typed up in LaTeX, one proof per note. The wording is exactly as I wrote it. Only the LaTeX was changed where it had to be for Obsidian.

- Foundations of Math portfolio proofs live in `Foundations of Math/`, tagged `#foundations-of-math` plus `#partial-portfolio` or `#final-portfolio`
- Exploration proofs I wrote on my own live in `Explorations/`, tagged `#exploration`
- $\R$, $\Z$, $\Q$, $\N$ are defined in the vault `preamble.sty`

---

## Foundations of Math — Partial Portfolio
*Proof Portfolio- Foundations of Math- Spring 2026* · February 27, 2026

| # | Proof | Source | Theorem |
|---|---|---|---|
| 1 | [[Direct Proof 1\|Direct Proof]] | Exam 1 Review #2.i | $a$ and $(a+1)(a-1)$ have opposite parity |
| 2 | [[Proof by Contrapositive]] | Exam 1 Review #2.j | $x^2$ irrational $\Rightarrow$ $x$ irrational |
| 3 | [[Proof by Contradiction]] | Homework 3 #6 | $x + \frac1x \ge 2$ for $x > 0$ |
| 4 | [[If and Only If (Equivalence) Proof]] | Exam 1 Review #2.l | $n, n+2, n+4$ all prime $\iff n = 3$ |

## Foundations of Math — Final Portfolio
*Final Portfolio - Foundations of Math - Spring 2026* · May 1, 2026

| # | Proof | Source | Theorem |
|---|---|---|---|
| 1 | [[Proof by Induction]] | Exam 2 Review #11 | $\sum_{i=1}^n i^3 = \frac{n^2(n+1)^2}{4}$ |
| 2 | [[Equivalence Relation Proof]] | Homework 8 #5 | $aRb \iff 4 \mid a^2 - b^2$ is an equivalence relation |
| 3 | [[Injectivity and Surjectivity Proof]] | Exam 3 Review #7 | $f(x) = \frac{x+1}{x}$ is injective, not surjective |
| 4 | [[Continuity Proof]] | Homework 10 #2 | $2x^2 + 1$ is continuous at $x = 2$ |
| 5 | [[Direct Proof 2\|Direct Proof]] | Homework 3 #5 | $x + \frac1x \ge 2$ for $x > 0$ |
| 6 | [[Set Theoretic Proof]] | Homework 3 #14 | $A-C \nsubseteq A-B \Rightarrow B \nsubseteq C$ |

The same theorem appears in both portfolios, proved two ways: $x + \frac1x \ge 2$ by contradiction in the [[Proof by Contradiction|Partial Portfolio]] and directly in the [[Direct Proof 2|Final Portfolio]].

## Explorations
- [[Inductive Proof of the Fibonacci Recurrence]] — strong induction, $\begin{bmatrix}1&1\\1&0\end{bmatrix}^n$ state-transition form
- [[Banach's Fixed Point Theorem]] — contraction on a complete space (unfinished draft, April 2026)

---

## Sources
- Raw TeX files in `source-temp/`
