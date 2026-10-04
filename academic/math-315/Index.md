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
- [Floating-Point Number Systems](Topics/Floating-Point%20Number%20Systems.md) — $x = \pm m\beta^{E}$, normalization, uneven spacing
- [Exponent and Mantissa](Topics/Exponent%20and%20Mantissa.md) — $E = \lfloor \log_\beta x \rfloor$, digits by repeated scaling
- [Overflow and Underflow](Topics/Overflow%20and%20Underflow.md) — UFL $= \beta^{L}$, OFL $= \beta^{U+1}(1 - \beta^{-p})$
- [Rounding and Machine Precision](Topics/Rounding%20and%20Machine%20Precision.md) — chopping vs nearest, $u = \tfrac12\beta^{1-p}$
- [IEEE Floating-Point Standard](Topics/IEEE%20Floating-Point%20Standard.md) — single ($p = 24$) and double ($p = 53$)

### 2.2 Floating-Point Arithmetic
- [Floating-Point Arithmetic](Topics/Floating-Point%20Arithmetic.md) — absorption, commutative but not associative
- [Cancellation Error](Topics/Cancellation%20Error.md) — subtracting nearly equal numbers, stable quadratic formula

---

## Lecture 3 — Direct Methods for Linear Systems

### 3.1 Gaussian Elimination
- [Triangular Systems](Topics/Triangular%20Systems.md) — diagonal, back and forward substitution, $n^2$ flops
- [Gaussian Elimination](Topics/Gaussian%20Elimination.md) — row operations, multipliers $m_{ij}$, $\tfrac23n^3$ flops

### 3.2 The LU Decomposition
- [LU Decomposition](Topics/LU%20Decomposition.md) — elementary row matrices, $L$ = multipliers, existence
- [Determinants via LU](Topics/Determinants%20via%20LU.md) — $\det A = (-1)^p\prod u_{ii}$
- [Partial Pivoting](Topics/Partial%20Pivoting.md) — small pivots, $|m_{ij}| \le 1$, $PA = LU$
  - [Permutation and Multiplier Matrices](Topics/Permutation%20and%20Multiplier%20Matrices.md) — moving the $P_j$ next to $A$ (supplement + whiteboard)

### 3.3 Special Matrices and Other Factorizations
- [LDLT Factorization](Topics/LDLT%20Factorization.md) — symmetric $A = LDL^{\top}$
- [Symmetric Positive Definite Matrices](Topics/Symmetric%20Positive%20Definite%20Matrices.md) — $\mathbf{x}^{\top}A\mathbf{x} > 0$ and its consequences
- [Cholesky Factorization](Topics/Cholesky%20Factorization.md) — $A = GG^{\top}$, $\tfrac13n^3$ flops
- [QR Factorization](Topics/QR%20Factorization.md) — orthogonal $Q$, $R\mathbf{x} = Q^{\top}\mathbf{b}$
- [Singular Value Decomposition](Topics/Singular%20Value%20Decomposition.md) — $A = U\Sigma V^{\top}$, $\sigma_i = \sqrt{\lambda_i(A^{\top}A)}$

### B.13 Vector and Matrix Norms
- [Vector Norms](Topics/Vector%20Norms.md) — $\ell_1$, $\ell_2$, $\ell_\infty$
- [Matrix Norms](Topics/Matrix%20Norms.md) — induced norms, column/row sums, spectral, Frobenius

### 3.4 Estimating and Improving Accuracy
- [Forward and Backward Error](Topics/Forward%20and%20Backward%20Error.md) — error vs residual
- [Condition Number](Topics/Condition%20Number.md) — $\kappa(A) = \|A\|\|A^{-1}\|$, $\kappa_2 = \sigma_1/\sigma_n$

---

## Explorations

| # | Exploration | Source | Topics |
|---|---|---|---|
| 1 | [EX01 - Back Substitution on a 3x3 System](Explorations/EX01%20-%20Back%20Substitution%20on%20a%203x3%20System.md) | constructed | [Triangular Systems](Topics/Triangular%20Systems.md) |
| 2 | [EX02 - Forward Substitution on a 3x3 System](Explorations/EX02%20-%20Forward%20Substitution%20on%20a%203x3%20System.md) | constructed | [Triangular Systems](Topics/Triangular%20Systems.md), [LU Decomposition](Topics/LU%20Decomposition.md) |
| 3 | [EX03 - Gaussian Elimination and LU of a 3x3 Matrix](Explorations/EX03%20-%20Gaussian%20Elimination%20and%20LU%20of%20a%203x3%20Matrix.md) | constructed | [Gaussian Elimination](Topics/Gaussian%20Elimination.md), [LU Decomposition](Topics/LU%20Decomposition.md), [Determinants via LU](Topics/Determinants%20via%20LU.md) |
| 4 | [EX04 - Exploration 3.2.12 - A Matrix with No LU Decomposition](Explorations/EX04%20-%20Exploration%203.2.12%20-%20A%20Matrix%20with%20No%20LU%20Decomposition.md) | handout p. 6 | [LU Decomposition](Topics/LU%20Decomposition.md), [Partial Pivoting](Topics/Partial%20Pivoting.md) |
| 5 | [EX05 - Four-Digit Arithmetic With and Without Pivoting](Explorations/EX05%20-%20Four-Digit%20Arithmetic%20With%20and%20Without%20Pivoting.md) | handout pp. 7–8 | [Partial Pivoting](Topics/Partial%20Pivoting.md) |
| 6 | [EX06 - PA = LU for a Matrix with a Zero Pivot](Explorations/EX06%20-%20PA%20%3D%20LU%20for%20a%20Matrix%20with%20a%20Zero%20Pivot.md) | handout pp. 9–10 | [Partial Pivoting](Topics/Partial%20Pivoting.md), [Permutation and Multiplier Matrices](Topics/Permutation%20and%20Multiplier%20Matrices.md), [Determinants via LU](Topics/Determinants%20via%20LU.md) |
| 7 | [EX07 - LDLT Factorization of a 2x2 Symmetric Matrix](Explorations/EX07%20-%20LDLT%20Factorization%20of%20a%202x2%20Symmetric%20Matrix.md) | handout p. 11 | [LDLT Factorization](Topics/LDLT%20Factorization.md), [Cholesky Factorization](Topics/Cholesky%20Factorization.md) |
| 8 | [EX08 - Cholesky Factorization of a 3x3 SPD Matrix](Explorations/EX08%20-%20Cholesky%20Factorization%20of%20a%203x3%20SPD%20Matrix.md) | handout pp. 13–14 | [Cholesky Factorization](Topics/Cholesky%20Factorization.md), [Symmetric Positive Definite Matrices](Topics/Symmetric%20Positive%20Definite%20Matrices.md) |
| 9 | [EX09 - QR Factorization and Solve of a 2x2 System](Explorations/EX09%20-%20QR%20Factorization%20and%20Solve%20of%20a%202x2%20System.md) | constructed | [QR Factorization](Topics/QR%20Factorization.md) |
| 10 | [EX10 - SVD and Condition Number of a 2x2 Matrix](Explorations/EX10%20-%20SVD%20and%20Condition%20Number%20of%20a%202x2%20Matrix.md) | constructed | [Singular Value Decomposition](Topics/Singular%20Value%20Decomposition.md), [Condition Number](Topics/Condition%20Number.md) |
| 11 | [EX11 - l1 Norm of a 3x2 Matrix](Explorations/EX11%20-%20l1%20Norm%20of%20a%203x2%20Matrix.md) | handout p. 19 | [Matrix Norms](Topics/Matrix%20Norms.md), [Vector Norms](Topics/Vector%20Norms.md) |
| 12 | [EX12 - Four Norms of a 3x3 Matrix](Explorations/EX12%20-%20Four%20Norms%20of%20a%203x3%20Matrix.md) | handout p. 20 | [Matrix Norms](Topics/Matrix%20Norms.md), [Singular Value Decomposition](Topics/Singular%20Value%20Decomposition.md) |
| 13 | [EX13 - Small Residual, Large Error](Explorations/EX13%20-%20Small%20Residual%2C%20Large%20Error.md) | handout pp. 21–22 | [Forward and Backward Error](Topics/Forward%20and%20Backward%20Error.md), [Condition Number](Topics/Condition%20Number.md) |
| 14 | [EX14 - Determinant Versus Condition Number](Explorations/EX14%20-%20Determinant%20Versus%20Condition%20Number.md) | handout p. 23 | [Condition Number](Topics/Condition%20Number.md), [Determinants via LU](Topics/Determinants%20via%20LU.md) |
| 15 | [EX15 - Exploration 2.2.1 - Five-Digit Product of 100pi and 10e](Explorations/EX15%20-%20Exploration%202.2.1%20-%20Five-Digit%20Product%20of%20100pi%20and%2010e.md) | slide 22 | [Rounding and Machine Precision](Topics/Rounding%20and%20Machine%20Precision.md), [Floating-Point Arithmetic](Topics/Floating-Point%20Arithmetic.md) |
| 16 | [EX16 - Base-2 Representation of -117 and 0.1](Explorations/EX16%20-%20Base-2%20Representation%20of%20-117%20and%200.1.md) | slides 24–28 | [Floating-Point Number Systems](Topics/Floating-Point%20Number%20Systems.md), [Exponent and Mantissa](Topics/Exponent%20and%20Mantissa.md) |
| 17 | [EX17 - A Toy Binary Floating-Point System](Explorations/EX17%20-%20A%20Toy%20Binary%20Floating-Point%20System.md) | constructed | [Floating-Point Number Systems](Topics/Floating-Point%20Number%20Systems.md), [Overflow and Underflow](Topics/Overflow%20and%20Underflow.md), [Rounding and Machine Precision](Topics/Rounding%20and%20Machine%20Precision.md) |
| 18 | [EX18 - Exploration 2.2.9 - Overflow Level of IEEE Double Precision](Explorations/EX18%20-%20Exploration%202.2.9%20-%20Overflow%20Level%20of%20IEEE%20Double%20Precision.md) | slide 31 | [Overflow and Underflow](Topics/Overflow%20and%20Underflow.md), [IEEE Floating-Point Standard](Topics/IEEE%20Floating-Point%20Standard.md) |
| 19 | [EX19 - Absorption and Non-Associativity](Explorations/EX19%20-%20Absorption%20and%20Non-Associativity.md) | slides 36–38 | [Floating-Point Arithmetic](Topics/Floating-Point%20Arithmetic.md) |
| 20 | [EX20 - Overflow and Underflow in Base-10 Arithmetic](Explorations/EX20%20-%20Overflow%20and%20Underflow%20in%20Base-10%20Arithmetic.md) | slides 39, 43 | [Overflow and Underflow](Topics/Overflow%20and%20Underflow.md), [Floating-Point Arithmetic](Topics/Floating-Point%20Arithmetic.md) |
| 21 | [EX21 - Cancellation in the Quadratic Formula](Explorations/EX21%20-%20Cancellation%20in%20the%20Quadratic%20Formula.md) | constructed | [Cancellation Error](Topics/Cancellation%20Error.md) |

---

## Sources
- *Math 315 Lecture 2 slides: Computer Arithmetic* (`source/MATH_315_Lecture_2.pdf`)
- *Math 315 Lecture 3 handout: Direct Methods for Linear Systems* (`source/Math_315_Lecture_3_handout.pdf`)
- *Partial pivoting supplement* (`source/Math_315_Lecture_3_Partial_Pivoting.pdf`)
- Lecture whiteboard photo (`source/IMG_1784.jpg`)
