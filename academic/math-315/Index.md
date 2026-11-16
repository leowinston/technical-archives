---
tags: [math-315, index]
---
# Math 315 — Numerical Analysis Index

Topic notes hold definitions, key results, and short derivations. The explorations are the worked examples I learned the most from: the ones where something surprising happens.

- Topic notes live in `Topics 1/` (Lectures 2–3), `Topics 2/` (Lecture 4 and textbook 5.1 Differentiation), and `Topics 3/` (textbook 5.2–5.3 Integration)
- Exploration notes live in `Explorations 1/`, `Explorations 2/`, and `Explorations 3/`, matching the topic folders

---

## Lecture 2 — Computer Arithmetic

### 2.2 Floating-Point Numbers
- [Floating-Point Number Systems](Topics%201/Floating-Point%20Number%20Systems.md) — $x = \pm m\beta^{E}$, normalization, uneven spacing
- [Exponent and Mantissa](Topics%201/Exponent%20and%20Mantissa.md) — $E = \lfloor \log_\beta x \rfloor$, digits by repeated scaling
- [Overflow and Underflow](Topics%201/Overflow%20and%20Underflow.md) — UFL $= \beta^{L}$, OFL $= \beta^{U+1}(1 - \beta^{-p})$
- [Rounding and Machine Precision](Topics%201/Rounding%20and%20Machine%20Precision.md) — chopping vs nearest, $u = \tfrac12\beta^{1-p}$
- [IEEE Floating-Point Standard](Topics%201/IEEE%20Floating-Point%20Standard.md) — single ($p = 24$) and double ($p = 53$)

### 2.2 Floating-Point Arithmetic
- [Floating-Point Arithmetic](Topics%201/Floating-Point%20Arithmetic.md) — absorption, commutative but not associative
- [Cancellation Error](Topics%201/Cancellation%20Error.md) — subtracting nearly equal numbers, stable quadratic formula

---

## Lecture 3 — Direct Methods for Linear Systems

### 3.1 Gaussian Elimination
- [Triangular Systems](Topics%201/Triangular%20Systems.md) — diagonal, back and forward substitution, $n^2$ flops
- [Gaussian Elimination](Topics%201/Gaussian%20Elimination.md) — row operations, multipliers $m_{ij}$, $\tfrac23n^3$ flops

### 3.2 The LU Decomposition
- [LU Decomposition](Topics%201/LU%20Decomposition.md) — elementary row matrices, $L$ = multipliers, existence
- [Determinants via LU](Topics%201/Determinants%20via%20LU.md) — $\det A = (-1)^p\prod u_{ii}$
- [Partial Pivoting](Topics%201/Partial%20Pivoting.md) — small pivots, $|m_{ij}| \le 1$, $PA = LU$
  - [Permutation and Multiplier Matrices](Topics%201/Permutation%20and%20Multiplier%20Matrices.md) — moving the $P_j$ next to $A$ (supplement + whiteboard)

### 3.3 Special Matrices and Other Factorizations
- [LDLT Factorization](Topics%201/LDLT%20Factorization.md) — symmetric $A = LDL^{\top}$
- [Symmetric Positive Definite Matrices](Topics%201/Symmetric%20Positive%20Definite%20Matrices.md) — $\mathbf{x}^{\top}A\mathbf{x} > 0$ and its consequences
- [Cholesky Factorization](Topics%201/Cholesky%20Factorization.md) — $A = GG^{\top}$, $\tfrac13n^3$ flops
- [QR Factorization](Topics%201/QR%20Factorization.md) — orthogonal $Q$, $R\mathbf{x} = Q^{\top}\mathbf{b}$
- [Singular Value Decomposition](Topics%201/Singular%20Value%20Decomposition.md) — $A = U\Sigma V^{\top}$, $\sigma_i = \sqrt{\lambda_i(A^{\top}A)}$

### B.13 Vector and Matrix Norms
- [Vector Norms](Topics%201/Vector%20Norms.md) — $\ell_1$, $\ell_2$, $\ell_\infty$
- [Matrix Norms](Topics%201/Matrix%20Norms.md) — induced norms, column/row sums, spectral, Frobenius
- [Norm of an Orthogonal Matrix](Topics%201/Norm%20of%20an%20Orthogonal%20Matrix.md) — $\|Q\mathbf{x}\| = \|\mathbf{x}\|$ so $\|Q\|_2 = 1$; fails for $p = 1, \infty$

### 3.4 Estimating and Improving Accuracy
- [Forward and Backward Error](Topics%201/Forward%20and%20Backward%20Error.md) — error vs residual
- [Condition Number](Topics%201/Condition%20Number.md) — $\kappa(A) = \|A\|\|A^{-1}\|$, $\kappa_2 = \sigma_1/\sigma_n$

---

## Lecture 4 — Interpolation and Least Squares

### 4.1 Polynomial Interpolation
- [Polynomial Interpolation](Topics%202/Polynomial%20Interpolation.md) — $p(x_i) = f_i$, exact degree, uniqueness for distinct nodes
- [Power Series Form and the Vandermonde Matrix](Topics%202/Power%20Series%20Form%20and%20the%20Vandermonde%20Matrix.md) — $V\mathbf{a} = \mathbf{f}$, $\det V = \prod_{i>j}(x_i - x_j)$
- [Newton Form](Topics%202/Newton%20Form.md) — $N_j = \prod_{k<j}(x - x_k)$, lower triangular system
- [Divided Differences](Topics%202/Divided%20Differences.md) — $c_j = f[x_0, \dots, x_j]$, table and algorithm
- [Lagrange Form](Topics%202/Lagrange%20Form.md) — $\ell_k(x_j) = \delta_{kj}$, no linear solve
- [Chebyshev Polynomials](Topics%202/Chebyshev%20Polynomials.md) — $T_{j+1} = 2xT_j - T_{j-1}$, Chebyshev points

### 4.2 The Error in Polynomial Interpolation
- [Interpolation Error](Topics%202/Interpolation%20Error.md) — $\omega_{N+1}(x)f^{(N+1)}(\xi)/(N+1)!$, Runge's function

### 4.3 Polynomial Splines
- [Linear Splines](Topics%202/Linear%20Splines.md) — broken line, $h^2/8$ error, hat basis
- [Cubic Splines](Topics%202/Cubic%20Splines.md) — $C^2$ pieces, $4N$ unknowns, natural / clamped / not-a-knot
- [Cubic B-Splines](Topics%202/Cubic%20B-Splines.md) — $A = \tfrac{1}{4h^3}$, $B = -\tfrac{1}{h^3}$, tridiagonal $(\tfrac14, 1, \tfrac14)$ system

### 4.4–4.5 Least Squares Fitting
- [Least Squares Fitting](Topics%202/Least%20Squares%20Fitting.md) — $\min\|V\mathbf{a} - \mathbf{f}\|_2^2$, $M \ll N$
- [Normal Equations](Topics%202/Normal%20Equations.md) — $V^{\top}V\mathbf{a} = V^{\top}\mathbf{f}$, SPD, Cholesky
- [Least Squares via QR](Topics%202/Least%20Squares%20via%20QR.md) — $R_m\mathbf{a} = \mathbf{b}$, residual $\|\mathbf{c}\|_2$
- [Least Squares with a General Basis](Topics%202/Least%20Squares%20with%20a%20General%20Basis.md) — $W_{ij} = \phi_j(x_i)$, $W^{\top}W\mathbf{a} = W^{\top}\mathbf{f}$
- [Conditioning of the Normal Equations](Topics%202/Conditioning%20of%20the%20Normal%20Equations.md) — $\kappa(V^{\top}V) = \kappa(V)^2$, SPD $\ne$ well-conditioned

---

## Chapter 5 — Differentiation (textbook, Topics 2)

### 5.1 Differentiation
- [Finite Difference Formulas](Topics%202/Finite%20Difference%20Formulas.md) — forward $O(h)$, central $O(h^2)$, from Taylor series
- [Step Size and Roundoff in Numerical Differentiation](Topics%202/Step%20Size%20and%20Roundoff%20in%20Numerical%20Differentiation.md) — truncation vs cancellation, $h^* \sim \sqrt\varepsilon$ and $\varepsilon^{1/3}$
- [Differentiating Tabulated Data](Topics%202/Differentiating%20Tabulated%20Data.md) — unequal-mesh three-point formula, chord error $-\tfrac{h_{i+1} - h_i}{2}f''$, `np.gradient`
- [Differentiating a Cubic Spline](Topics%202/Differentiating%20a%20Cubic%20Spline.md) — global, $S'$ error $O(h^3)$, `CubicSpline.derivative`

---

## Chapter 5 — Integration (textbook, Topics 3)

### 5.2.1–5.2.2 Basic Rules and Their Errors
- [Quadrature Rules](Topics%203/Quadrature%20Rules.md) — $R(f) = \sum w_if(x_i)$, $I(f) - I(q) = I(f - q)$, interpolatory weights
- [Midpoint and Trapezoidal Rules](Topics%203/Midpoint%20and%20Trapezoidal%20Rules.md) — basic and composite $R_{CM}$, $R_{CT}$
- [Error in the Midpoint and Trapezoidal Rules](Topics%203/Error%20in%20the%20Midpoint%20and%20Trapezoidal%20Rules.md) — $-\tfrac{(b-a)h^2}{12}f''$ and $+\tfrac{(b-a)h^2}{24}f''$
- [Newton-Cotes Rules](Topics%203/Newton-Cotes%20Rules.md) — equally spaced, open vs closed, superconvergence, oscillating weights
- [Simpson's Rule](Topics%203/Simpson%27s%20Rule.md) — $\tfrac{b-a}{6}[f(a) + 4f(m) + f(b)]$, DOP $3$, composite $O(h^4)$
- [Degree of Precision](Topics%203/Degree%20of%20Precision.md) — monomial test, method of undetermined coefficients
- [Peano's Theorem](Topics%203/Peano%27s%20Theorem.md) — $I - R = \kappa f^{(m+1)}(\eta)$, $\kappa$ from $f = x^{m+1}$

### 5.2.3–5.2.5 Adaptive, Gauss, and Lobatto Rules
- [Adaptive Integration](Topics%203/Adaptive%20Integration.md) — error estimate $\lvert R_2 - R_1\rvert$, bisect the worst subinterval
- [Gauss Rules](Topics%203/Gauss%20Rules.md) — free points and weights, DOP $2N+1$, Gauss-Kronrod
- [Lobatto Rules](Topics%203/Lobatto%20Rules.md) — endpoints included, DOP $2N-1$, comparison with Gauss
- [Transformation from a Canonical Interval](Topics%203/Transformation%20from%20a%20Canonical%20Interval.md) — $x = \tfrac{b-a}{2}t + \tfrac{a+b}{2}$, $w_i = \tfrac{b-a}{2}w_i^*$

### 5.3.2 Integration in Practice (Python)
- [Integrating Tabulated Data](Topics%203/Integrating%20Tabulated%20Data.md) — trapezoid = linear spline, cubic spline + Simpson
- [Improper Integrals](Topics%203/Improper%20Integrals.md) — split at singularities, $x = 1/t$, subtract out the slow part

---

## Explorations

| # | Exploration | Source | Topics |
|---|---|---|---|
| 4 | [EX04 - Exploration 3.2.12 - A Matrix with No LU Decomposition](Explorations%201/EX04%20-%20Exploration%203.2.12%20-%20A%20Matrix%20with%20No%20LU%20Decomposition.md) | handout p. 6 | [LU Decomposition](Topics%201/LU%20Decomposition.md), [Partial Pivoting](Topics%201/Partial%20Pivoting.md) |
| 5 | [EX05 - Four-Digit Arithmetic With and Without Pivoting](Explorations%201/EX05%20-%20Four-Digit%20Arithmetic%20With%20and%20Without%20Pivoting.md) | handout pp. 7–8 | [Partial Pivoting](Topics%201/Partial%20Pivoting.md) |
| 13 | [EX13 - Small Residual, Large Error](Explorations%201/EX13%20-%20Small%20Residual%2C%20Large%20Error.md) | handout pp. 21–22 | [Forward and Backward Error](Topics%201/Forward%20and%20Backward%20Error.md), [Condition Number](Topics%201/Condition%20Number.md) |
| 14 | [EX14 - Determinant Versus Condition Number](Explorations%201/EX14%20-%20Determinant%20Versus%20Condition%20Number.md) | handout p. 23 | [Condition Number](Topics%201/Condition%20Number.md), [Determinants via LU](Topics%201/Determinants%20via%20LU.md) |
| 19 | [EX19 - Absorption and Non-Associativity](Explorations%201/EX19%20-%20Absorption%20and%20Non-Associativity.md) | slides 36–38 | [Floating-Point Arithmetic](Topics%201/Floating-Point%20Arithmetic.md) |
| 21 | [EX21 - Cancellation in the Quadratic Formula](Explorations%201/EX21%20-%20Cancellation%20in%20the%20Quadratic%20Formula.md) | constructed | [Cancellation Error](Topics%201/Cancellation%20Error.md) |
| 29 | [EX29 - Runge Function with Equispaced and Chebyshev Nodes](Explorations%202/EX29%20-%20Runge%20Function%20with%20Equispaced%20and%20Chebyshev%20Nodes.md) | handout p. 13 | [Interpolation Error](Topics%202/Interpolation%20Error.md), [Chebyshev Polynomials](Topics%202/Chebyshev%20Polynomials.md) |
| 31 | [EX31 - Deriving the Cubic B-Spline](Explorations%202/EX31%20-%20Deriving%20the%20Cubic%20B-Spline.md) | handout pp. 18–20 | [Cubic B-Splines](Topics%202/Cubic%20B-Splines.md), [Cubic Splines](Topics%202/Cubic%20Splines.md) |
| 37 | [EX37 - Optimal Step Size for the Derivative of e^x](Explorations%202/EX37%20-%20Optimal%20Step%20Size%20for%20the%20Derivative%20of%20e%5Ex.md) | textbook Prob. 5.1.3 | [Step Size and Roundoff in Numerical Differentiation](Topics%202/Step%20Size%20and%20Roundoff%20in%20Numerical%20Differentiation.md) |
| 39 | [EX39 - np.gradient Versus a Cubic Spline Derivative of sin x](Explorations%202/EX39%20-%20np.gradient%20Versus%20a%20Cubic%20Spline%20Derivative%20of%20sin%20x.md) | textbook Exs. 5.3.1–5.3.2 | [Differentiating Tabulated Data](Topics%202/Differentiating%20Tabulated%20Data.md), [Differentiating a Cubic Spline](Topics%202/Differentiating%20a%20Cubic%20Spline.md) |
| 42 | [EX42 - Simpson's Rule by Undetermined Coefficients](Explorations%203/EX42%20-%20Simpson%27s%20Rule%20by%20Undetermined%20Coefficients.md) | textbook Exs. 5.2.5–5.2.6 | [Degree of Precision](Topics%203/Degree%20of%20Precision.md), [Simpson's Rule](Topics%203/Simpson%27s%20Rule.md), [Peano's Theorem](Topics%203/Peano%27s%20Theorem.md) |
| 45 | [EX45 - Two- and Three-Point Gauss Rules](Explorations%203/EX45%20-%20Two-%20and%20Three-Point%20Gauss%20Rules.md) | textbook Probs. 5.2.26–5.2.27, 5.2.30 | [Gauss Rules](Topics%203/Gauss%20Rules.md), [Peano's Theorem](Topics%203/Peano%27s%20Theorem.md) |
| 49 | [EX49 - Cardiac Output from Dye Concentration Data](Explorations%203/EX49%20-%20Cardiac%20Output%20from%20Dye%20Concentration%20Data.md) | textbook Ex. 5.3.7 | [Integrating Tabulated Data](Topics%203/Integrating%20Tabulated%20Data.md) |
| 51 | [EX51 - Singular Integrands sin x over x and cos x over sqrt x](Explorations%203/EX51%20-%20Singular%20Integrands%20sin%20x%20over%20x%20and%20cos%20x%20over%20sqrt%20x.md) | textbook Exs. 5.3.9–5.3.11, Prob. 5.2.37 | [Improper Integrals](Topics%203/Improper%20Integrals.md), [Gauss Rules](Topics%203/Gauss%20Rules.md) |

---

## Sources
- *Math 315 Lecture 2 slides: Computer Arithmetic* (`source/MATH_315_Lecture_2.pdf`)
- *Math 315 Lecture 3 handout: Direct Methods for Linear Systems* (`source/Math_315_Lecture_3_handout.pdf`)
- *Partial pivoting supplement* (`source/Math_315_Lecture_3_Partial_Pivoting.pdf`)
- Lecture whiteboard photo (`source/IMG_1784.jpg`)
- *Math 315 Lecture 4 handout: Interpolation, Splines, and Least Squares* ([Math_315_Lecture_4_handout.pdf](Topics%202/Math_315_Lecture_4_handout.pdf))
- *Math 315 Lecture 4 fill-in notes* (slides 34–51: cubic B-splines, spline tools in Python, least squares, normal equations, QR), covered by the Lecture 4 Topics 2 notes
- Textbook *Chapter 5: Differentiation and Integration* (pp. 171–213), Sections 5.1–5.3. Topic notes cite "Section 5.x (textbook)" and exploration notes cite the textbook example or problem number. The textbook's Matlab code is replaced by Python (NumPy/SciPy) throughout.

The other explorations, the practice-test problems, problem sets, and labs are kept locally and listed in `Local Index.md`.
