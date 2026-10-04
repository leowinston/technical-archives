---
tags: [math-315, topic, lecture-3]
---
# LDLT Factorization
Back to [Index](../Index.md) · Section 3.3.2

## Setup
$A$ is **symmetric** if $A = A^{\top}$. Pull the pivots out of $U$:
$$
D = \operatorname{diag}(u_{11}, \dots, u_{nn}), \qquad M^{\top} = D^{-1}U \implies A = LDM^{\top}
$$

## Derivation
By symmetry, $LDM^{\top} = \big(LDM^{\top}\big)^{\top} = MDL^{\top}$. Multiply by $M^{-1}$ on the left and $M^{-\top}$ on the right:
$$
\underbrace{\big(M^{-1}L\big)D}_{\text{lower}} = \underbrace{D\big(M^{-1}L\big)^{\top}}_{\text{upper}}
$$
Both sides must be diagonal. Since $M^{-1}L$ has a unit diagonal, $M^{-1}L = I$, so $L = M$:
$$
\boxed{\,A = LDL^{\top}\,}
$$

## Remarks
- Only $n(n+1)/2$ numbers need to be stored.
- By hand: apply each row operation to the columns as well.

## Example
$$
\begin{bmatrix} 4 & 2 \\ 2 & 3 \end{bmatrix}
= \begin{bmatrix} 1 & 0 \\ \tfrac12 & 1 \end{bmatrix}
\begin{bmatrix} 4 & 0 \\ 0 & 2 \end{bmatrix}
\begin{bmatrix} 1 & \tfrac12 \\ 0 & 1 \end{bmatrix}
$$

## Explorations
- [EX07 - LDLT Factorization of a 2x2 Symmetric Matrix](../Explorations/EX07%20-%20LDLT%20Factorization%20of%20a%202x2%20Symmetric%20Matrix.md)

See also: [LU Decomposition](LU%20Decomposition.md), [Cholesky Factorization](Cholesky%20Factorization.md)
