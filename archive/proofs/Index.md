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
| 1 | [Direct Proof](Foundations%20of%20Math/Direct%20Proof%201.md) | Exam 1 Review #2.i | $a$ and $(a+1)(a-1)$ have opposite parity |
| 2 | [Proof by Contrapositive](Foundations%20of%20Math/Proof%20by%20Contrapositive.md) | Exam 1 Review #2.j | $x^2$ irrational $\Rightarrow$ $x$ irrational |
| 3 | [Proof by Contradiction](Foundations%20of%20Math/Proof%20by%20Contradiction.md) | Homework 3 #6 | $x + \frac1x \ge 2$ for $x > 0$ |
| 4 | [If and Only If (Equivalence) Proof](Foundations%20of%20Math/If%20and%20Only%20If%20%28Equivalence%29%20Proof.md) | Exam 1 Review #2.l | $n, n+2, n+4$ all prime $\iff n = 3$ |

## Foundations of Math — Final Portfolio
*Final Portfolio - Foundations of Math - Spring 2026* · May 1, 2026

| # | Proof | Source | Theorem |
|---|---|---|---|
| 1 | [Proof by Induction](Foundations%20of%20Math/Proof%20by%20Induction.md) | Exam 2 Review #11 | $\sum_{i=1}^n i^3 = \frac{n^2(n+1)^2}{4}$ |
| 2 | [Equivalence Relation Proof](Foundations%20of%20Math/Equivalence%20Relation%20Proof.md) | Homework 8 #5 | $aRb \iff 4 \mid a^2 - b^2$ is an equivalence relation |
| 3 | [Injectivity and Surjectivity Proof](Foundations%20of%20Math/Injectivity%20and%20Surjectivity%20Proof.md) | Exam 3 Review #7 | $f(x) = \frac{x+1}{x}$ is injective, not surjective |
| 4 | [Continuity Proof](Foundations%20of%20Math/Continuity%20Proof.md) | Homework 10 #2 | $2x^2 + 1$ is continuous at $x = 2$ |
| 5 | [Direct Proof](Foundations%20of%20Math/Direct%20Proof%202.md) | Homework 3 #5 | $x + \frac1x \ge 2$ for $x > 0$ |
| 6 | [Set Theoretic Proof](Foundations%20of%20Math/Set%20Theoretic%20Proof.md) | Homework 3 #14 | $A-C \nsubseteq A-B \Rightarrow B \nsubseteq C$ |

The same theorem appears in both portfolios, proved two ways: $x + \frac1x \ge 2$ by contradiction in the [Partial Portfolio](Foundations%20of%20Math/Proof%20by%20Contradiction.md) and directly in the [Final Portfolio](Foundations%20of%20Math/Direct%20Proof%202.md).

## Explorations
- [Inductive Proof of the Fibonacci Recurrence](Explorations/Inductive%20Proof%20of%20the%20Fibonacci%20Recurrence.md) — strong induction, $\begin{bmatrix}1&1\\1&0\end{bmatrix}^n$ state-transition form
- [Banach's Fixed Point Theorem](Explorations/Banach%27s%20Fixed%20Point%20Theorem.md) — contraction on a complete space (drafted April 2026, finished September 2026) · proves ODE existence and uniqueness via [Picard iteration](../../academic/math-212/Topics/Existence%20and%20Uniqueness%20Theorems.md)

---

## Sources
- Raw TeX files in `source-temp/`
