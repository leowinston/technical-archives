---
tags: [math-315, topic, lecture-4]
---
# Conditioning of the Normal Equations
Back to [Index](../Index.md) · Section 4.5

## Squaring
Since $\sigma_i(V^{\top}V) = \sigma_i(V)^2$,
$$
\boxed{\,\kappa_2(V^{\top}V) = \kappa_2(V)^2\,}
$$
Forming $V^{\top}V$ squares the condition number before any solve begins. [QR](Least%20Squares%20via%20QR.md) works on $V$ itself and avoids this.

## Example
Equispaced points on $[0,1]$, degree-$12$ polynomial, exact coefficients $\mathbf{1}$:

| method | relative error |
|---|---|
| normal equations | $\approx 22$ (no correct digits) |
| QR | $\approx 2\times10^{-8}$ |

Here $\kappa(V) \approx 7\times10^{8}$, so $\kappa(V^{\top}V) \approx 10^{17} \gtrsim 1/u$.

## SPD does not mean well-conditioned
SPD guarantees Cholesky works and needs no pivoting, so the **solve** is stable. It says nothing about $\kappa$. The tridiagonal $(\tfrac14, 1, \tfrac14)$ B-spline matrix is SPD with $\kappa \to 3$, while $V^{\top}V$ is SPD with $\kappa \sim 10^{17}$. See [Cubic B-Splines](Cubic%20B-Splines.md).

See also: [Normal Equations](Normal%20Equations.md), [Condition Number](../Topics%201/Condition%20Number.md), [Symmetric Positive Definite Matrices](../Topics%201/Symmetric%20Positive%20Definite%20Matrices.md), [Lab 10](../lab/lab%2010/Lab%2010%20-%20Least%20Squares,%20General%20Bases,%20and%20QR.md)
