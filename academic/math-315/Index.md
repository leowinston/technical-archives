---
tags: [math-315, index]
---
# Math 315 — Numerical Analysis Index

Topic notes hold definitions, key results, and short derivations. Exploration notes hold worked examples with actual matrices and full derivations, and link back to the topics they use.

- Topic notes live in `Topics/`
- Exploration notes live in `Explorations/`

---

## Lecture 2 — Computer Arithmetic

### 2.2 Floating-Point Numbers
- [[Floating-Point Number Systems]] — $x = \pm m\beta^{E}$, normalization, uneven spacing
- [[Exponent and Mantissa]] — $E = \lfloor \log_\beta x \rfloor$, digits by repeated scaling
- [[Overflow and Underflow]] — UFL $= \beta^{L}$, OFL $= \beta^{U+1}(1 - \beta^{-p})$
- [[Rounding and Machine Precision]] — chopping vs nearest, $u = \tfrac12\beta^{1-p}$
- [[IEEE Floating-Point Standard]] — single ($p = 24$) and double ($p = 53$)

### 2.2 Floating-Point Arithmetic
- [[Floating-Point Arithmetic]] — absorption, commutative but not associative
- [[Cancellation Error]] — subtracting nearly equal numbers, stable quadratic formula

---

## Lecture 3 — Direct Methods for Linear Systems

### 3.1 Gaussian Elimination
- [[Triangular Systems]] — diagonal, back and forward substitution, $n^2$ flops
- [[Gaussian Elimination]] — row operations, multipliers $m_{ij}$, $\tfrac23n^3$ flops

### 3.2 The LU Decomposition
- [[LU Decomposition]] — elementary row matrices, $L$ = multipliers, existence
- [[Determinants via LU]] — $\det A = (-1)^p\prod u_{ii}$
- [[Partial Pivoting]] — small pivots, $|m_{ij}| \le 1$, $PA = LU$
  - [[Permutation and Multiplier Matrices]] — moving the $P_j$ next to $A$ (supplement + whiteboard)

### 3.3 Special Matrices and Other Factorizations
- [[LDLT Factorization]] — symmetric $A = LDL^{\top}$
- [[Symmetric Positive Definite Matrices]] — $\mathbf{x}^{\top}A\mathbf{x} > 0$ and its consequences
- [[Cholesky Factorization]] — $A = GG^{\top}$, $\tfrac13n^3$ flops
- [[QR Factorization]] — orthogonal $Q$, $R\mathbf{x} = Q^{\top}\mathbf{b}$
- [[Singular Value Decomposition]] — $A = U\Sigma V^{\top}$, $\sigma_i = \sqrt{\lambda_i(A^{\top}A)}$

### B.13 Vector and Matrix Norms
- [[Vector Norms]] — $\ell_1$, $\ell_2$, $\ell_\infty$
- [[Matrix Norms]] — induced norms, column/row sums, spectral, Frobenius

### 3.4 Estimating and Improving Accuracy
- [[Forward and Backward Error]] — error vs residual
- [[Condition Number]] — $\kappa(A) = \|A\|\|A^{-1}\|$, $\kappa_2 = \sigma_1/\sigma_n$

---

## Explorations

| # | Exploration | Source | Topics |
|---|---|---|---|
| 1 | [[EX01 - Back Substitution on a 3x3 System]] | constructed | [[Triangular Systems]] |
| 2 | [[EX02 - Forward Substitution on a 3x3 System]] | constructed | [[Triangular Systems]], [[LU Decomposition]] |
| 3 | [[EX03 - Gaussian Elimination and LU of a 3x3 Matrix]] | constructed | [[Gaussian Elimination]], [[LU Decomposition]], [[Determinants via LU]] |
| 4 | [[EX04 - Exploration 3.2.12 - A Matrix with No LU Decomposition]] | handout p. 6 | [[LU Decomposition]], [[Partial Pivoting]] |
| 5 | [[EX05 - Four-Digit Arithmetic With and Without Pivoting]] | handout pp. 7–8 | [[Partial Pivoting]] |
| 6 | [[EX06 - PA = LU for a Matrix with a Zero Pivot]] | handout pp. 9–10 | [[Partial Pivoting]], [[Permutation and Multiplier Matrices]], [[Determinants via LU]] |
| 7 | [[EX07 - LDLT Factorization of a 2x2 Symmetric Matrix]] | handout p. 11 | [[LDLT Factorization]], [[Cholesky Factorization]] |
| 8 | [[EX08 - Cholesky Factorization of a 3x3 SPD Matrix]] | handout pp. 13–14 | [[Cholesky Factorization]], [[Symmetric Positive Definite Matrices]] |
| 9 | [[EX09 - QR Factorization and Solve of a 2x2 System]] | constructed | [[QR Factorization]] |
| 10 | [[EX10 - SVD and Condition Number of a 2x2 Matrix]] | constructed | [[Singular Value Decomposition]], [[Condition Number]] |
| 11 | [[EX11 - l1 Norm of a 3x2 Matrix]] | handout p. 19 | [[Matrix Norms]], [[Vector Norms]] |
| 12 | [[EX12 - Four Norms of a 3x3 Matrix]] | handout p. 20 | [[Matrix Norms]], [[Singular Value Decomposition]] |
| 13 | [[EX13 - Small Residual, Large Error]] | handout pp. 21–22 | [[Forward and Backward Error]], [[Condition Number]] |
| 14 | [[EX14 - Determinant Versus Condition Number]] | handout p. 23 | [[Condition Number]], [[Determinants via LU]] |
| 15 | [[EX15 - Exploration 2.2.1 - Five-Digit Product of 100pi and 10e]] | slide 22 | [[Rounding and Machine Precision]], [[Floating-Point Arithmetic]] |
| 16 | [[EX16 - Base-2 Representation of -117 and 0.1]] | slides 24–28 | [[Floating-Point Number Systems]], [[Exponent and Mantissa]] |
| 17 | [[EX17 - A Toy Binary Floating-Point System]] | constructed | [[Floating-Point Number Systems]], [[Overflow and Underflow]], [[Rounding and Machine Precision]] |
| 18 | [[EX18 - Exploration 2.2.9 - Overflow Level of IEEE Double Precision]] | slide 31 | [[Overflow and Underflow]], [[IEEE Floating-Point Standard]] |
| 19 | [[EX19 - Absorption and Non-Associativity]] | slides 36–38 | [[Floating-Point Arithmetic]] |
| 20 | [[EX20 - Overflow and Underflow in Base-10 Arithmetic]] | slides 39, 43 | [[Overflow and Underflow]], [[Floating-Point Arithmetic]] |
| 21 | [[EX21 - Cancellation in the Quadratic Formula]] | constructed | [[Cancellation Error]] |

---

## Sources
- *Math 315 Lecture 2 slides: Computer Arithmetic* (`source/MATH_315_Lecture_2.pdf`)
- *Math 315 Lecture 3 handout: Direct Methods for Linear Systems* (`source/Math_315_Lecture_3_handout.pdf`)
- *Partial pivoting supplement* (`source/Math_315_Lecture_3_Partial_Pivoting.pdf`)
- Lecture whiteboard photo (`source/IMG_1784.jpg`)
