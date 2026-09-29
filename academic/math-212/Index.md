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
- [[Mathematical Models]] — falling objects, radioactive decay, Newton's law of cooling, RC circuits

### 1.2 Solutions and Direction Fields
- [[Solutions and Direction Fields]] — what a solution is, integral curves, direction fields

### 1.3 Classification of Differential Equations
- [[Classification of Differential Equations]] — ODE vs PDE, order, linear vs nonlinear, homogeneous vs nonhomogeneous
- [[Systems of Differential Equations]] — coupled equations, Lotka–Volterra predator–prey

---

## Chapter 2 — First-Order Differential Equations

### 2.1 Linear Equations; Method of Integrating Factors
- [[Linear First-Order Equations]] — standard form $y' + p(t)y = g(t)$, integrating factor $\mu = e^{\int p\,dt}$
- [[Variation of Parameters]] — $y = y_1 u$ with $y_1$ solving the complementary equation

### 2.2 Separable Equations
- [[Separable Equations]] — $M(x)\,dx + N(y)\,dy = 0$, implicit vs explicit, interval of validity
- [[Homogeneous Substitution]] — $\dfrac{dy}{dx} = F\!\left(\tfrac{y}{x}\right)$ via $y = xv$

### 2.3 Modeling with First-Order Equations
- [[Modeling with First-Order Equations]] — mixing, finance, motion with resistance, cooling, Torricelli

### 2.4 Differences Between Linear and Nonlinear Equations
- [[Existence and Uniqueness Theorems]] — Thm 2.4.1 (linear), Thm 2.4.2 (nonlinear, via Picard iteration and Banach), interval of existence, singular solutions
- [[Bernoulli Equations]] — $y' + p(t)y = q(t)y^n$, substitution $v = y^{1-n}$

### 2.5 Autonomous Equations and Population Dynamics
- [[Autonomous Equations and Phase Lines]] — equilibria, stability, concavity via $y'' = f'(y)f(y)$
  - Stability: [[Stable Equilibrium]], [[Unstable Equilibrium]], [[Semistable Equilibrium]]
- Population models
  - [[Exponential Growth]]
  - [[Logistic Growth]]
  - [[Threshold Growth]] (critical threshold)
  - [[Logistic Growth with a Threshold]]
  - [[Gompertz Growth]]
- [[Harvesting]] — Schaefer model, maximum sustainable yield
- [[Bifurcations]] — saddle-node, pitchfork, transcritical

### 2.6 Exact Equations and Integrating Factors
- [[Exact Equations]] — $M_y = N_x$, potential function $\psi(x,y) = c$
- [[Integrating Factors for Exact Equations]] — $\mu(x)$ or $\mu(y)$ for non-exact equations

---

## Workbook — Part 1: First-Order Differential Equations

| #   | Problem                                                           | Classification                                  | Topics                                                                           |
| --- | ----------------------------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------------------------------- |
| 1   | [[WB1 P01 - Car Slowing Down to a Stop]]                          | 1st-order linear, homogeneous (constant coeff.) | [[Mathematical Models]], [[Linear First-Order Equations]]                        |
| 2   | [[WB1 P02 - Direct Integration of y'' = 3x + 1]]                  | 2nd-order linear, nonhomogeneous                | [[Classification of Differential Equations]], [[Solutions and Direction Fields]] |
| 3   | [[WB1 P03 - Classifying Linear and Nonlinear Equations]]          | Classification drill                            | [[Classification of Differential Equations]]                                     |
| 4   | [[WB1 P04 - Direct Integration of First-Order Equations]]         | 1st-order, $y' = f(x)$                          | [[Solutions and Direction Fields]]                                               |
| 5   | [[WB1 P05 - The Equation y' - ay = 0]]                            | 1st-order linear, homogeneous                   | [[Linear First-Order Equations]], [[Exponential Growth]]                         |
| 6   | [[WB1 P06 - General Solution of the Homogeneous Linear Equation]] | Proof                                           | [[Linear First-Order Equations]], [[Existence and Uniqueness Theorems]]          |
| 7   | [[WB1 P07 - Linear Equation with an Exact Left Side]]             | 1st-order linear, nonhomogeneous                | [[Linear First-Order Equations]]                                                 |
| 8   | [[WB1 P08 - Linear Equation y' - 2y = 4 - x]]                     | 1st-order linear, nonhomogeneous                | [[Linear First-Order Equations]]                                                 |
| 9   | [[WB1 P09 - Deriving the Integrating Factor]]                     | Derivation                                      | [[Linear First-Order Equations]]                                                 |
| 10  | [[WB1 P10 - Linear Equation with Exponential Forcing]]            | 1st-order linear, nonhomogeneous                | [[Linear First-Order Equations]]                                                 |
| 11  | [[WB1 P11 - Deriving Variation of Parameters]]                    | Derivation                                      | [[Variation of Parameters]]                                                      |
| 12  | [[WB1 P12 - Problem 10 by Variation of Parameters]]               | 1st-order linear, nonhomogeneous                | [[Variation of Parameters]]                                                      |
| 13  | [[WB1 P13 - Separable Equation with an Implicit Solution]]        | 1st-order nonlinear, separable                  | [[Separable Equations]]                                                          |
| 14  | [[WB1 P14 - Separable Equation with cos x]]                       | 1st-order nonlinear, separable                  | [[Separable Equations]]                                                          |
| 15  | [[WB1 P15 - Separable Equation with an Explicit Solution]]        | 1st-order nonlinear, separable                  | [[Separable Equations]], [[Existence and Uniqueness Theorems]]                   |
| 16  | [[WB1 P16 - Separable IVP with Interval of Validity]]             | 1st-order nonlinear, separable, IVP             | [[Separable Equations]], [[Existence and Uniqueness Theorems]]                   |
| 17  | [[WB1 P17 - Exact Equation 1]]                                    | Exact                                           | [[Exact Equations]]                                                              |
| 18  | [[WB1 P18 - Exact Equation 2]]                                    | Exact (also separable)                          | [[Exact Equations]], [[Separable Equations]]                                     |
| 19  | [[WB1 P19 - Non-Exact Equation Made Exact by x]]                  | Non-exact → exact with $\mu = x$                | [[Exact Equations]], [[Integrating Factors for Exact Equations]]                 |
| 20  | [[WB1 P20 - Integrating Factor mu(x)]]                            | Non-exact → exact with $\mu(x)$                 | [[Integrating Factors for Exact Equations]]                                      |
| 21  | [[WB1 P21 - Integrating Factor mu(y)]]                            | Non-exact → exact with $\mu(y)$                 | [[Integrating Factors for Exact Equations]]                                      |
| 22  | [[WB1 P22 - Rewriting as a Linear Equation]]                      | 1st-order linear, nonhomogeneous                | [[Linear First-Order Equations]]                                                 |
| 23  | [[WB1 P23 - Exponential Growth]]                                  | Autonomous, linear                              | [[Exponential Growth]], [[Autonomous Equations and Phase Lines]]                 |
| 24  | [[WB1 P24 - Logistic Growth]]                                     | Autonomous, nonlinear                           | [[Logistic Growth]], [[Autonomous Equations and Phase Lines]]                    |
| 25  | [[WB1 P25 - A Critical Threshold]]                                | Autonomous, nonlinear                           | [[Threshold Growth]], [[Autonomous Equations and Phase Lines]]                   |
| 26  | [[WB1 P26 - Critical Threshold Blow-Up]]                          | Autonomous, nonlinear, IVP                      | [[Threshold Growth]], [[Existence and Uniqueness Theorems]]                      |
| 27  | [[WB1 P27 - Logistic Growth with a Threshold]]                    | Autonomous, nonlinear                           | [[Logistic Growth with a Threshold]], [[Autonomous Equations and Phase Lines]]   |

---

## Sources
- *Math 212 Workbook — Part 1: First Order Differential Equations*
- Boyce & DiPrima, *Elementary Differential Equations and Boundary Value Problems*, Ch. 1–2
- Differential Equations Companion (LaTeX reference)
