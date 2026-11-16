---
tags: [math-212, index]
---
# Math 212 — Differential Equations Index

The topics from the course that I find most interesting: how solutions behave, not just how to compute them. Each note holds the definition, the key result, and only the steps that matter.

---

## Existence and Uniqueness
- [Existence and Uniqueness Theorems](Topics%201/Existence%20and%20Uniqueness%20Theorems.md) — Thm 2.4.1 (linear), Thm 2.4.2 (nonlinear, via Picard iteration and Banach), interval of existence, singular solutions

## Autonomous Equations and Population Dynamics
- [Autonomous Equations and Phase Lines](Topics%201/Autonomous%20Equations%20and%20Phase%20Lines.md) — equilibria, stability, concavity via $y'' = f'(y)f(y)$
  - Stability: [Stable Equilibrium](Topics%201/Stable%20Equilibrium.md), [Unstable Equilibrium](Topics%201/Unstable%20Equilibrium.md), [Semistable Equilibrium](Topics%201/Semistable%20Equilibrium.md)
- [Logistic Growth](Topics%201/Logistic%20Growth.md) — $y' = r(1 - y/K)y$, carrying capacity
- [Threshold Growth](Topics%201/Threshold%20Growth.md) — a critical threshold: die out below it, blow up above it
- [Logistic Growth with a Threshold](Topics%201/Logistic%20Growth%20with%20a%20Threshold.md) — both effects in one cubic
- [Harvesting](Topics%201/Harvesting.md) — Schaefer model, maximum sustainable yield
- [Bifurcations](Topics%201/Bifurcations.md) — saddle-node, pitchfork, transcritical

## Second-Order Linear Equations
- [Solutions of Linear Homogeneous Equations; the Wronskian](Topics%202/Solutions%20of%20Linear%20Homogeneous%20Equations;%20the%20Wronskian.md) — $W = y_1y_2' - y_1'y_2$, fundamental sets, Abel's theorem
- [Complex Roots of the Characteristic Equation](Topics%202/Complex%20Roots%20of%20the%20Characteristic%20Equation.md) — $e^{{\lambda x}}(c_1\cos\mu x + c_2\sin\mu x)$, amplitude–phase form
- [Variation of Parameters](Topics%202/Variation%20of%20Parameters.md) — $u_1' = -y_2F/(P_0W)$, $u_2' = y_1F/(P_0W)$

## Vibrations
- [Mechanical and Electrical Vibrations](Topics%202/Mechanical%20and%20Electrical%20Vibrations.md) — $mx'' + cx' + kx = F(t)$, over/critical/underdamping, the spring–circuit analogy
- [Forced Periodic Vibrations](Topics%202/Forced%20Periodic%20Vibrations.md) — beats and resonance

## The Laplace Transform
Enrichment beyond the course: the first three notes follow the in-class handout, and the rest go on to Boyce & DiPrima Chapter 6.
- [The Laplace Transform](Topics%203/The%20Laplace%20Transform.md) — $F(s) = \int_0^\infty e^{{-st}}f(t)\,dt$, why the weight, first transforms, linearity
- [Transforms of Derivatives](Topics%203/Transforms%20of%20Derivatives.md) — $\mathcal{{L}}\{{f'\}} = sF(s) - f(0)$, derivatives become multiplication
- [Solving Initial Value Problems with the Laplace Transform](Topics%203/Solving%20Initial%20Value%20Problems%20with%20the%20Laplace%20Transform.md) — transform, solve, invert; poles are characteristic roots
- [Inverse Transforms and Partial Fractions](Topics%203/Inverse%20Transforms%20and%20Partial%20Fractions.md) — first shift theorem, which pole gives which term
- [Step Functions and the Second Shift Theorem](Topics%203/Step%20Functions%20and%20the%20Second%20Shift%20Theorem.md) — $u_c(t)$, delayed and switched forcing
- [Impulses and the Dirac Delta](Topics%203/Impulses%20and%20the%20Dirac%20Delta.md) — $\mathcal{{L}}\{{\delta(t-c)\}} = e^{{-cs}}$, a hammer blow sets the velocity
- [Convolution and the Transfer Function](Topics%203/Convolution%20and%20the%20Transfer%20Function.md) — $Y = HG$, impulse response, resonance as a double pole

---

## Sources
- Boyce & DiPrima, *Elementary Differential Equations and Boundary Value Problems*, Ch. 1–3 and 6
- *Math 212 Workbook*, Parts 1–2, and the *Discovering Laplace Transforms* enrichment handout

The rest of the course (routine solution methods, workbook problems, practice exams) is kept locally and listed in `Local Index.md`.
