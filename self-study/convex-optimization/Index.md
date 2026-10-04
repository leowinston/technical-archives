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
- [Mathematical Optimization](topics/Mathematical%20Optimization.md) — standard form, problem classes, ✎ the solvable "exceptions"

### 1.2 Least-Squares and Linear Programming
- [Least-Squares and Linear Programming](topics/Least-Squares%20and%20Linear%20Programming.md) — normal equations $A^{\top}Ax = A^{\top}b$, LPs, Chebyshev approximation

### 1.3–1.5 Convex Optimization and Outline
- [Convex Optimization Overview](topics/Convex%20Optimization%20Overview.md) — ✎ convex $f_i$, ✎ special cases, ✎ Lagrangian duality's central role

---

## Part I — Theory

## Chapter 2 — Convex Sets

### 2.1 Affine and Convex Sets
- [Affine and Convex Sets](topics/Affine%20and%20Convex%20Sets.md) — lines vs segments, convex hull, cones

### 2.2 Some Important Examples
- [Important Convex Sets](topics/Important%20Convex%20Sets.md) — halfspaces, balls, ellipsoids, norm cones, polyhedra, $\Spsd{n}$

### 2.3 Operations That Preserve Convexity
- [Operations That Preserve Convexity of Sets](topics/Operations%20That%20Preserve%20Convexity%20of%20Sets.md) — intersection, affine maps, perspective

### 2.4 Generalized Inequalities
- [Generalized Inequalities and Minimal Elements](topics/Generalized%20Inequalities%20and%20Minimal%20Elements.md) — proper cones, ✎ minimum vs minimal (Fig. 2.17)

### 2.5 Separating and Supporting Hyperplanes
- [Separating and Supporting Hyperplanes](topics/Separating%20and%20Supporting%20Hyperplanes.md) — $a^{\top}x \le b$ on $C$, $\ge b$ on $D$

### 2.6 Dual Cones
- [Dual Cones](topics/Dual%20Cones.md) — $K^{*}$, self-dual cones, dual characterization of minimal elements

## Chapter 3 — Convex Functions

### 3.1 Basic Properties and Examples
- [Convex Functions](topics/Convex%20Functions.md) — ✎ definition, ✎ concave, restriction to a line
- [First-Order Condition](topics/First-Order%20Condition.md) — tangent line is a global underestimator
- [Second-Order Conditions](topics/Second-Order%20Conditions.md) — ✎ $\nabla^2 f \succeq 0$
- [Examples of Convex Functions](topics/Examples%20of%20Convex%20Functions.md) — norms, max, log-sum-exp, $\log\det$ (concave; evaluate via Cholesky)
- [Sublevel Sets and Epigraph](topics/Sublevel%20Sets%20and%20Epigraph.md) — ✎ sublevel-set sketch, $f$ convex $\iff \epi f$ convex
- [Jensen's Inequality](topics/Jensen%27s%20Inequality.md) — $f(\E X) \le \E f(X)$, ✎ dithering hurts (ML notebook)

### 3.2 Operations That Preserve Convexity
- [Operations That Preserve Convexity of Functions](topics/Operations%20That%20Preserve%20Convexity%20of%20Functions.md) — ✎ sums, max/sup, composition, minimization

### 3.3 The Conjugate Function
- [Conjugate Function](topics/Conjugate%20Function.md) — $f^{*}(y) = \sup_x(y^{\top}x - f(x))$, Fenchel's inequality

### 3.4 Quasiconvex Functions
- [Quasiconvex Functions](topics/Quasiconvex%20Functions.md) — ✎ convex sublevel sets, $f(\theta x + (1-\theta)y) \le \max\{f(x), f(y)\}$

### 3.5 Log-Concave and Log-Convex Functions
- [Log-Concave and Log-Convex Functions](topics/Log-Concave%20and%20Log-Convex%20Functions.md) — Gaussian densities, why MLE is convex

### 3.6 Convexity with Respect to Generalized Inequalities
- [Convexity with Respect to Generalized Inequalities](topics/Convexity%20with%20Respect%20to%20Generalized%20Inequalities.md) — $K$-convex, matrix convex

## Chapter 4 — Convex Optimization Problems

### 4.1 Optimization Problems
- [Optimization Problems in Standard Form](topics/Optimization%20Problems%20in%20Standard%20Form.md) — $p^\star$, equivalent problems, epigraph form

### 4.2 Convex Optimization
- [Convex Optimization Problems](topics/Convex%20Optimization%20Problems.md) — convex $f_i$, affine $h_i$, ✎ concave maximization
- [Local and Global Optima](topics/Local%20and%20Global%20Optima.md) — ✎ every local optimum is global
- [Optimality Criterion for Differentiable Objectives](topics/Optimality%20Criterion%20for%20Differentiable%20Objectives.md) — $\nabla f_0(x)^{\top}(y - x) \ge 0$

### 4.3 Linear Optimization Problems
- [Linear Programs](topics/Linear%20Programs.md) — diet problem, Chebyshev center, piecewise-linear minimization

### 4.4 Quadratic Optimization Problems
- [Quadratic Programs](topics/Quadratic%20Programs.md) — QP, QCQP, SOCP, robust LP
- [Markowitz Portfolio Optimization](topics/Markowitz%20Portfolio%20Optimization.md) — ✎ minimize $x^{\top}\Sigma x$ s.t. return, budget, long-only

### 4.5 Geometric Programming
- [Geometric Programming](topics/Geometric%20Programming.md) — posynomials, log change of variables, cantilever beam

---

## ML Notebook — Related Material

### Multivariable and Matrix Background
- [Gradient, Jacobian, and Hessian](topics/Gradient%2C%20Jacobian%2C%20and%20Hessian.md) — $\nabla f$, $J$, $\nabla^2 f$, $\Delta f = \tr(\nabla^2 f)$
- [Positive Semidefinite Matrices](topics/Positive%20Semidefinite%20Matrices.md) — spectral theorem, four equivalent PSD conditions

### Learning as Convex Optimization
- [Least Squares by Gradient Descent](topics/Least%20Squares%20by%20Gradient%20Descent.md) — $\nabla L = \tfrac2n X^{\top}(Xw - y)$
- [Maximum Likelihood Estimation](topics/Maximum%20Likelihood%20Estimation.md) — Gaussian MLE = least squares
- [Bias-Variance Tradeoff](topics/Bias-Variance%20Tradeoff.md) — bias² + variance + $\sigma^2$, ridge regularization

### Graphs as Optimization Problems
- [Sparsest Cut as a Spectral Relaxation](topics/Sparsest%20Cut%20as%20a%20Spectral%20Relaxation.md) — $\{\pm1\}^n \to$ sphere relaxation, $\lambda_2 \le \phi_G$, $\lambda_2(w)$ concave, regularization
- Graph definitions ($L_G$, Fiedler vector, sweep algorithm) live in [Graph Theory](../graph-theory/Index.md)
- [Regularized Spectral Clustering](../graph-theory/Theory/Regularized%20Spectral%20Clustering.md) (graph theory) — ridge term $\tau\sum_i(x_i - \bar x)^2$ in the cut relaxation

---

## Explorations

| # | Exploration | Source | Topics |
|---|---|---|---|
| 1 | [EX01 - Minimum Versus Minimal Elements in R2](explorations/EX01%20-%20Minimum%20Versus%20Minimal%20Elements%20in%20R2.md) | ✎ Fig. 2.17 | [Generalized Inequalities and Minimal Elements](topics/Generalized%20Inequalities%20and%20Minimal%20Elements.md) |
| 2 | [EX02 - Checking Convexity with the Hessian](explorations/EX02%20-%20Checking%20Convexity%20with%20the%20Hessian.md) | ✎ §3.1.4–3.1.5 | [Second-Order Conditions](topics/Second-Order%20Conditions.md), [Examples of Convex Functions](topics/Examples%20of%20Convex%20Functions.md) |
| 3 | [EX03 - Sublevel Sets of a Quasiconvex Function](explorations/EX03%20-%20Sublevel%20Sets%20of%20a%20Quasiconvex%20Function.md) | ✎ pp. 75, 95–96 sketches | [Quasiconvex Functions](topics/Quasiconvex%20Functions.md), [Sublevel Sets and Epigraph](topics/Sublevel%20Sets%20and%20Epigraph.md) |
| 4 | [EX04 - Jensen and Dithering](explorations/EX04%20-%20Jensen%20and%20Dithering.md) | ML notebook | [Jensen's Inequality](topics/Jensen%27s%20Inequality.md) |
| 5 | [EX05 - Pointwise Max of Affine Functions](explorations/EX05%20-%20Pointwise%20Max%20of%20Affine%20Functions.md) | ✎ §3.2, §4.3 | [Operations That Preserve Convexity of Functions](topics/Operations%20That%20Preserve%20Convexity%20of%20Functions.md), [Linear Programs](topics/Linear%20Programs.md) |
| 6 | [EX06 - Local Versus Global Minima](explorations/EX06%20-%20Local%20Versus%20Global%20Minima.md) | ✎ §4.2.2 | [Local and Global Optima](topics/Local%20and%20Global%20Optima.md) |
| 7 | [EX07 - Markowitz Three-Asset Portfolio](explorations/EX07%20-%20Markowitz%20Three-Asset%20Portfolio.md) | ✎ §4.4.1 | [Markowitz Portfolio Optimization](topics/Markowitz%20Portfolio%20Optimization.md), [Quadratic Programs](topics/Quadratic%20Programs.md) |
| 8 | [EX08 - Least Squares by Gradient Descent](explorations/EX08%20-%20Least%20Squares%20by%20Gradient%20Descent.md) | ML notebook | [Least Squares by Gradient Descent](topics/Least%20Squares%20by%20Gradient%20Descent.md) |
| 9 | [EX09 - Gaussian MLE Equals Least Squares](explorations/EX09%20-%20Gaussian%20MLE%20Equals%20Least%20Squares.md) | ML notebook | [Maximum Likelihood Estimation](topics/Maximum%20Likelihood%20Estimation.md) |
| 10 | [EX10 - Relaxation Gap on a 10-Node Graph](explorations/EX10%20-%20Relaxation%20Gap%20on%20a%2010-Node%20Graph.md) | ML notebook | [Sparsest Cut as a Spectral Relaxation](topics/Sparsest%20Cut%20as%20a%20Spectral%20Relaxation.md) |
| 11 | [EX11 - Log Det via Cholesky](explorations/EX11%20-%20Log%20Det%20via%20Cholesky.md) | §3.1.5, lecture | [Examples of Convex Functions](topics/Examples%20of%20Convex%20Functions.md), [Cholesky Factorization](../../academic/math-315/Topics/Cholesky%20Factorization.md) |

---

## Sources
- Boyd & Vandenberghe, *Convex Optimization*, Cambridge University Press, 2004. Annotated excerpt covering Ch. 1 – §4.5 (`source-temp/ConvexOpt.pdf`)
- ML notebook, handwritten iPad notes (`source-temp/ML notebook.pdf`)
- Macros for this course (`\dom`, `\epi`, `\argmin`, `\Spsd{n}`, …) live in the vault `preamble.sty`
