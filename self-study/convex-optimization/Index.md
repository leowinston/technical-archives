---
tags: [convex-optimization, index]
---
# Convex Optimization Index

Self-study notes built from two sources: my annotated copy of Boyd & Vandenberghe (Ch. 1 – §4.5) and my ML notebook. Topic notes hold definitions, key results, and short derivations. Exploration notes hold worked examples with numpy and Desmos, and link back to the topics they use.

- Topic notes live in `Topics/`
- Exploration notes live in `Explorations/`
- ✎ marks a place where I highlighted or wrote on the page

## Where my annotations are densest
| Rank | Where | What I marked |
|---|---|---|
| 1 | §4.4.1 Markowitz (p. 155) | "Algory", $x_i$ as a vector, "how much asset$_i$", Cov $\Sigma$, "long every stock" |
| 2 | Ch. 3 Convex functions | definition, §3.1.4 heading, sublevel-set sketch (p. 75), §3.2 heading, quasiconvex sketches (pp. 95–96) |
| 3 | §4.2 Convex problems | concave maximization, local = global (pp. 137–138) |
| 4 | Ch. 1 Introduction | "exceptions", "convex", "special cases", "Lagrangian duality", "central role" |
| 5 | §2.4 Generalized inequalities | Figure 2.17 "Left" / "Right" (p. 46) |

---

## Chapter 1 — Introduction

### 1.1 Mathematical Optimization
- [[Mathematical Optimization]] — standard form, problem classes, ✎ the solvable "exceptions"

### 1.2 Least-Squares and Linear Programming
- [[Least-Squares and Linear Programming]] — normal equations $A^{\top}Ax = A^{\top}b$, LPs, Chebyshev approximation

### 1.3–1.5 Convex Optimization and Outline
- [[Convex Optimization Overview]] — ✎ convex $f_i$, ✎ special cases, ✎ Lagrangian duality's central role

---

## Part I — Theory

## Chapter 2 — Convex Sets

### 2.1 Affine and Convex Sets
- [[Affine and Convex Sets]] — lines vs segments, convex hull, cones

### 2.2 Some Important Examples
- [[Important Convex Sets]] — halfspaces, balls, ellipsoids, norm cones, polyhedra, $\Spsd{n}$

### 2.3 Operations That Preserve Convexity
- [[Operations That Preserve Convexity of Sets]] — intersection, affine maps, perspective

### 2.4 Generalized Inequalities
- [[Generalized Inequalities and Minimal Elements]] — proper cones, ✎ minimum vs minimal (Fig. 2.17)

### 2.5 Separating and Supporting Hyperplanes
- [[Separating and Supporting Hyperplanes]] — $a^{\top}x \le b$ on $C$, $\ge b$ on $D$

### 2.6 Dual Cones
- [[Dual Cones]] — $K^{*}$, self-dual cones, dual characterization of minimal elements

## Chapter 3 — Convex Functions

### 3.1 Basic Properties and Examples
- [[Convex Functions]] — ✎ definition, ✎ concave, restriction to a line
- [[First-Order Condition]] — tangent line is a global underestimator
- [[Second-Order Conditions]] — ✎ $\nabla^2 f \succeq 0$
- [[Examples of Convex Functions]] — norms, max, log-sum-exp, $\log\det$ (concave; evaluate via Cholesky)
- [[Sublevel Sets and Epigraph]] — ✎ sublevel-set sketch, $f$ convex $\iff \epi f$ convex
- [[Jensen's Inequality]] — $f(\E X) \le \E f(X)$, ✎ dithering hurts (ML notebook)

### 3.2 Operations That Preserve Convexity
- [[Operations That Preserve Convexity of Functions]] — ✎ sums, max/sup, composition, minimization

### 3.3 The Conjugate Function
- [[Conjugate Function]] — $f^{*}(y) = \sup_x(y^{\top}x - f(x))$, Fenchel's inequality

### 3.4 Quasiconvex Functions
- [[Quasiconvex Functions]] — ✎ convex sublevel sets, $f(\theta x + (1-\theta)y) \le \max\{f(x), f(y)\}$

### 3.5 Log-Concave and Log-Convex Functions
- [[Log-Concave and Log-Convex Functions]] — Gaussian densities, why MLE is convex

### 3.6 Convexity with Respect to Generalized Inequalities
- [[Convexity with Respect to Generalized Inequalities]] — $K$-convex, matrix convex

## Chapter 4 — Convex Optimization Problems

### 4.1 Optimization Problems
- [[Optimization Problems in Standard Form]] — $p^\star$, equivalent problems, epigraph form

### 4.2 Convex Optimization
- [[Convex Optimization Problems]] — convex $f_i$, affine $h_i$, ✎ concave maximization
- [[Local and Global Optima]] — ✎ every local optimum is global
- [[Optimality Criterion for Differentiable Objectives]] — $\nabla f_0(x)^{\top}(y - x) \ge 0$

### 4.3 Linear Optimization Problems
- [[Linear Programs]] — diet problem, Chebyshev center, piecewise-linear minimization

### 4.4 Quadratic Optimization Problems
- [[Quadratic Programs]] — QP, QCQP, SOCP, robust LP
- [[Markowitz Portfolio Optimization]] — ✎ minimize $x^{\top}\Sigma x$ s.t. return, budget, long-only

### 4.5 Geometric Programming
- [[Geometric Programming]] — posynomials, log change of variables, cantilever beam

---

## ML Notebook — Related Material

### Multivariable and Matrix Background
- [[Gradient, Jacobian, and Hessian]] — $\nabla f$, $J$, $\nabla^2 f$, $\Delta f = \tr(\nabla^2 f)$
- [[Positive Semidefinite Matrices]] — spectral theorem, four equivalent PSD conditions

### Learning as Convex Optimization
- [[Least Squares by Gradient Descent]] — $\nabla L = \tfrac2n X^{\top}(Xw - y)$
- [[Maximum Likelihood Estimation]] — Gaussian MLE = least squares
- [[Bias-Variance Tradeoff]] — bias² + variance + $\sigma^2$, ridge regularization

### Graphs as Optimization Problems
- [[Sparsest Cut as a Spectral Relaxation]] — $\{\pm1\}^n \to$ sphere relaxation, $\lambda_2 \le \phi_G$, $\lambda_2(w)$ concave, regularization
- Graph definitions ($L_G$, Fiedler vector, sweep algorithm) live in [[self-study/graph-theory/Index|Graph Theory]]
- [[Regularized Spectral Clustering]] (graph theory) — ridge term $\tau\sum_i(x_i - \bar x)^2$ in the cut relaxation

---

## Explorations

| # | Exploration | Source | Topics |
|---|---|---|---|
| 1 | [[EX01 - Minimum Versus Minimal Elements in R2]] | ✎ Fig. 2.17 | [[Generalized Inequalities and Minimal Elements]] |
| 2 | [[EX02 - Checking Convexity with the Hessian]] | ✎ §3.1.4–3.1.5 | [[Second-Order Conditions]], [[Examples of Convex Functions]] |
| 3 | [[EX03 - Sublevel Sets of a Quasiconvex Function]] | ✎ pp. 75, 95–96 sketches | [[Quasiconvex Functions]], [[Sublevel Sets and Epigraph]] |
| 4 | [[EX04 - Jensen and Dithering]] | ML notebook | [[Jensen's Inequality]] |
| 5 | [[EX05 - Pointwise Max of Affine Functions]] | ✎ §3.2, §4.3 | [[Operations That Preserve Convexity of Functions]], [[Linear Programs]] |
| 6 | [[EX06 - Local Versus Global Minima]] | ✎ §4.2.2 | [[Local and Global Optima]] |
| 7 | [[EX07 - Markowitz Three-Asset Portfolio]] | ✎ §4.4.1 | [[Markowitz Portfolio Optimization]], [[Quadratic Programs]] |
| 8 | [[EX08 - Least Squares by Gradient Descent]] | ML notebook | [[Least Squares by Gradient Descent]] |
| 9 | [[EX09 - Gaussian MLE Equals Least Squares]] | ML notebook | [[Maximum Likelihood Estimation]] |
| 10 | [[EX10 - Relaxation Gap on a 10-Node Graph]] | ML notebook | [[Sparsest Cut as a Spectral Relaxation]] |
| 11 | [[EX11 - Log Det via Cholesky]] | §3.1.5, lecture | [[Examples of Convex Functions]], [[academic/math-315/Topics/Cholesky Factorization\|Cholesky Factorization]] |

---

## Sources
- Boyd & Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004. Annotated excerpt covering Ch. 1 – §4.5 (`source-temp/ConvexOpt.pdf`)
- ML notebook, handwritten iPad notes (`source-temp/ML notebook.pdf`)
- Macros for this course (`\dom`, `\epi`, `\argmin`, `\Spsd{n}`, …) live in the vault `preamble.sty`
