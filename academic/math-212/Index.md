---
tags: [math-212, index]
---
# Math 212 — Differential Equations Index

Topic notes hold definitions, theorems, and standard forms. Problem notes hold worked workbook examples and link back to the topics they use.

- Topic notes live in `Topics/`
- Problem notes live in `Workbook 1/`

---

## Chapter 1 — Introduction

### 1.1 Differential Equations and Mathematical Models
- [Mathematical Models](Topics/Mathematical%20Models.md) — falling objects, radioactive decay, Newton's law of cooling, RC circuits

### 1.2 Solutions and Direction Fields
- [Solutions and Direction Fields](Topics/Solutions%20and%20Direction%20Fields.md) — what a solution is, integral curves, direction fields

### 1.3 Classification of Differential Equations
- [Classification of Differential Equations](Topics/Classification%20of%20Differential%20Equations.md) — ODE vs PDE, order, linear vs nonlinear, homogeneous vs nonhomogeneous
- [Systems of Differential Equations](Topics/Systems%20of%20Differential%20Equations.md) — coupled equations, Lotka–Volterra predator–prey

---

## Chapter 2 — First-Order Differential Equations

### 2.1 Linear Equations; Method of Integrating Factors
- [Linear First-Order Equations](Topics/Linear%20First-Order%20Equations.md) — standard form $y' + p(t)y = g(t)$, integrating factor $\mu = e^{\int p\,dt}$
- [Variation of Parameters](Topics/Variation%20of%20Parameters.md) — $y = y_1 u$ with $y_1$ solving the complementary equation

### 2.2 Separable Equations
- [Separable Equations](Topics/Separable%20Equations.md) — $M(x)\,dx + N(y)\,dy = 0$, implicit vs explicit, interval of validity
- [Homogeneous Substitution](Topics/Homogeneous%20Substitution.md) — $\dfrac{dy}{dx} = F\!\left(\tfrac{y}{x}\right)$ via $y = xv$

### 2.3 Modeling with First-Order Equations
- [Modeling with First-Order Equations](Topics/Modeling%20with%20First-Order%20Equations.md) — mixing, finance, motion with resistance, cooling, Torricelli

### 2.4 Differences Between Linear and Nonlinear Equations
- [Existence and Uniqueness Theorems](Topics/Existence%20and%20Uniqueness%20Theorems.md) — Thm 2.4.1 (linear), Thm 2.4.2 (nonlinear, via Picard iteration and Banach), interval of existence, singular solutions
- [Bernoulli Equations](Topics/Bernoulli%20Equations.md) — $y' + p(t)y = q(t)y^n$, substitution $v = y^{1-n}$

### 2.5 Autonomous Equations and Population Dynamics
- [Autonomous Equations and Phase Lines](Topics/Autonomous%20Equations%20and%20Phase%20Lines.md) — equilibria, stability, concavity via $y'' = f'(y)f(y)$
  - Stability: [Stable Equilibrium](Topics/Stable%20Equilibrium.md), [Unstable Equilibrium](Topics/Unstable%20Equilibrium.md), [Semistable Equilibrium](Topics/Semistable%20Equilibrium.md)
- Population models
  - [Exponential Growth](Topics/Exponential%20Growth.md)
  - [Logistic Growth](Topics/Logistic%20Growth.md)
  - [Threshold Growth](Topics/Threshold%20Growth.md) (critical threshold)
  - [Logistic Growth with a Threshold](Topics/Logistic%20Growth%20with%20a%20Threshold.md)
  - [Gompertz Growth](Topics/Gompertz%20Growth.md)
- [Harvesting](Topics/Harvesting.md) — Schaefer model, maximum sustainable yield
- [Bifurcations](Topics/Bifurcations.md) — saddle-node, pitchfork, transcritical

### 2.6 Exact Equations and Integrating Factors
- [Exact Equations](Topics/Exact%20Equations.md) — $M_y = N_x$, potential function $\psi(x,y) = c$
- [Integrating Factors for Exact Equations](Topics/Integrating%20Factors%20for%20Exact%20Equations.md) — $\mu(x)$ or $\mu(y)$ for non-exact equations

---

## Workbook — Part 1: First-Order Differential Equations

| # | Problem | Classification | Topics |
|---|---------|----------------|--------|
| 1 | [WB1 P01 - Car Slowing Down to a Stop](Workbook%201/WB1%20P01%20-%20Car%20Slowing%20Down%20to%20a%20Stop.md) | 1st-order linear, homogeneous (constant coeff.) | [Mathematical Models](Topics/Mathematical%20Models.md), [Linear First-Order Equations](Topics/Linear%20First-Order%20Equations.md) |
| 2 | [WB1 P02 - Direct Integration of y'' = 3x + 1](Workbook%201/WB1%20P02%20-%20Direct%20Integration%20of%20y%27%27%20%3D%203x%20%2B%201.md) | 2nd-order linear, nonhomogeneous | [Classification of Differential Equations](Topics/Classification%20of%20Differential%20Equations.md), [Solutions and Direction Fields](Topics/Solutions%20and%20Direction%20Fields.md) |
| 3 | [WB1 P03 - Classifying Linear and Nonlinear Equations](Workbook%201/WB1%20P03%20-%20Classifying%20Linear%20and%20Nonlinear%20Equations.md) | Classification drill | [Classification of Differential Equations](Topics/Classification%20of%20Differential%20Equations.md) |
| 4 | [WB1 P04 - Direct Integration of First-Order Equations](Workbook%201/WB1%20P04%20-%20Direct%20Integration%20of%20First-Order%20Equations.md) | 1st-order, $y' = f(x)$ | [Solutions and Direction Fields](Topics/Solutions%20and%20Direction%20Fields.md) |
| 5 | [WB1 P05 - The Equation y' - ay = 0](Workbook%201/WB1%20P05%20-%20The%20Equation%20y%27%20-%20ay%20%3D%200.md) | 1st-order linear, homogeneous | [Linear First-Order Equations](Topics/Linear%20First-Order%20Equations.md), [Exponential Growth](Topics/Exponential%20Growth.md) |
| 6 | [WB1 P06 - General Solution of the Homogeneous Linear Equation](Workbook%201/WB1%20P06%20-%20General%20Solution%20of%20the%20Homogeneous%20Linear%20Equation.md) | Proof | [Linear First-Order Equations](Topics/Linear%20First-Order%20Equations.md), [Existence and Uniqueness Theorems](Topics/Existence%20and%20Uniqueness%20Theorems.md) |
| 7 | [WB1 P07 - Linear Equation with an Exact Left Side](Workbook%201/WB1%20P07%20-%20Linear%20Equation%20with%20an%20Exact%20Left%20Side.md) | 1st-order linear, nonhomogeneous | [Linear First-Order Equations](Topics/Linear%20First-Order%20Equations.md) |
| 8 | [WB1 P08 - Linear Equation y' - 2y = 4 - x](Workbook%201/WB1%20P08%20-%20Linear%20Equation%20y%27%20-%202y%20%3D%204%20-%20x.md) | 1st-order linear, nonhomogeneous | [Linear First-Order Equations](Topics/Linear%20First-Order%20Equations.md) |
| 9 | [WB1 P09 - Deriving the Integrating Factor](Workbook%201/WB1%20P09%20-%20Deriving%20the%20Integrating%20Factor.md) | Derivation | [Linear First-Order Equations](Topics/Linear%20First-Order%20Equations.md) |
| 10 | [WB1 P10 - Linear Equation with Exponential Forcing](Workbook%201/WB1%20P10%20-%20Linear%20Equation%20with%20Exponential%20Forcing.md) | 1st-order linear, nonhomogeneous | [Linear First-Order Equations](Topics/Linear%20First-Order%20Equations.md) |
| 11 | [WB1 P11 - Deriving Variation of Parameters](Workbook%201/WB1%20P11%20-%20Deriving%20Variation%20of%20Parameters.md) | Derivation | [Variation of Parameters](Topics/Variation%20of%20Parameters.md) |
| 12 | [WB1 P12 - Problem 10 by Variation of Parameters](Workbook%201/WB1%20P12%20-%20Problem%2010%20by%20Variation%20of%20Parameters.md) | 1st-order linear, nonhomogeneous | [Variation of Parameters](Topics/Variation%20of%20Parameters.md) |
| 13 | [WB1 P13 - Separable Equation with an Implicit Solution](Workbook%201/WB1%20P13%20-%20Separable%20Equation%20with%20an%20Implicit%20Solution.md) | 1st-order nonlinear, separable | [Separable Equations](Topics/Separable%20Equations.md) |
| 14 | [WB1 P14 - Separable Equation with cos x](Workbook%201/WB1%20P14%20-%20Separable%20Equation%20with%20cos%20x.md) | 1st-order nonlinear, separable | [Separable Equations](Topics/Separable%20Equations.md) |
| 15 | [WB1 P15 - Separable Equation with an Explicit Solution](Workbook%201/WB1%20P15%20-%20Separable%20Equation%20with%20an%20Explicit%20Solution.md) | 1st-order nonlinear, separable | [Separable Equations](Topics/Separable%20Equations.md), [Existence and Uniqueness Theorems](Topics/Existence%20and%20Uniqueness%20Theorems.md) |
| 16 | [WB1 P16 - Separable IVP with Interval of Validity](Workbook%201/WB1%20P16%20-%20Separable%20IVP%20with%20Interval%20of%20Validity.md) | 1st-order nonlinear, separable, IVP | [Separable Equations](Topics/Separable%20Equations.md), [Existence and Uniqueness Theorems](Topics/Existence%20and%20Uniqueness%20Theorems.md) |
| 17 | [WB1 P17 - Exact Equation 1](Workbook%201/WB1%20P17%20-%20Exact%20Equation%201.md) | Exact | [Exact Equations](Topics/Exact%20Equations.md) |
| 18 | [WB1 P18 - Exact Equation 2](Workbook%201/WB1%20P18%20-%20Exact%20Equation%202.md) | Exact (also separable) | [Exact Equations](Topics/Exact%20Equations.md), [Separable Equations](Topics/Separable%20Equations.md) |
| 19 | [WB1 P19 - Non-Exact Equation Made Exact by x](Workbook%201/WB1%20P19%20-%20Non-Exact%20Equation%20Made%20Exact%20by%20x.md) | Non-exact → exact with $\mu = x$ | [Exact Equations](Topics/Exact%20Equations.md), [Integrating Factors for Exact Equations](Topics/Integrating%20Factors%20for%20Exact%20Equations.md) |
| 20 | [WB1 P20 - Integrating Factor mu(x)](Workbook%201/WB1%20P20%20-%20Integrating%20Factor%20mu%28x%29.md) | Non-exact → exact with $\mu(x)$ | [Integrating Factors for Exact Equations](Topics/Integrating%20Factors%20for%20Exact%20Equations.md) |
| 21 | [WB1 P21 - Integrating Factor mu(y)](Workbook%201/WB1%20P21%20-%20Integrating%20Factor%20mu%28y%29.md) | Non-exact → exact with $\mu(y)$ | [Integrating Factors for Exact Equations](Topics/Integrating%20Factors%20for%20Exact%20Equations.md) |
| 22 | [WB1 P22 - Rewriting as a Linear Equation](Workbook%201/WB1%20P22%20-%20Rewriting%20as%20a%20Linear%20Equation.md) | 1st-order linear, nonhomogeneous | [Linear First-Order Equations](Topics/Linear%20First-Order%20Equations.md) |
| 23 | [WB1 P23 - Exponential Growth](Workbook%201/WB1%20P23%20-%20Exponential%20Growth.md) | Autonomous, linear | [Exponential Growth](Topics/Exponential%20Growth.md), [Autonomous Equations and Phase Lines](Topics/Autonomous%20Equations%20and%20Phase%20Lines.md) |
| 24 | [WB1 P24 - Logistic Growth](Workbook%201/WB1%20P24%20-%20Logistic%20Growth.md) | Autonomous, nonlinear | [Logistic Growth](Topics/Logistic%20Growth.md), [Autonomous Equations and Phase Lines](Topics/Autonomous%20Equations%20and%20Phase%20Lines.md) |
| 25 | [WB1 P25 - A Critical Threshold](Workbook%201/WB1%20P25%20-%20A%20Critical%20Threshold.md) | Autonomous, nonlinear | [Threshold Growth](Topics/Threshold%20Growth.md), [Autonomous Equations and Phase Lines](Topics/Autonomous%20Equations%20and%20Phase%20Lines.md) |
| 26 | [WB1 P26 - Critical Threshold Blow-Up](Workbook%201/WB1%20P26%20-%20Critical%20Threshold%20Blow-Up.md) | Autonomous, nonlinear, IVP | [Threshold Growth](Topics/Threshold%20Growth.md), [Existence and Uniqueness Theorems](Topics/Existence%20and%20Uniqueness%20Theorems.md) |
| 27 | [WB1 P27 - Logistic Growth with a Threshold](Workbook%201/WB1%20P27%20-%20Logistic%20Growth%20with%20a%20Threshold.md) | Autonomous, nonlinear | [Logistic Growth with a Threshold](Topics/Logistic%20Growth%20with%20a%20Threshold.md), [Autonomous Equations and Phase Lines](Topics/Autonomous%20Equations%20and%20Phase%20Lines.md) |

---

## Sources
- *Math 212 Workbook — Part 1: First Order Differential Equations*
- Boyce & DiPrima, *Elementary Differential Equations and Boundary Value Problems*, Ch. 1–2
- Differential Equations Companion (LaTeX reference)
