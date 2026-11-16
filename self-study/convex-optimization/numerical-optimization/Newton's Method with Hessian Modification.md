---
tags: [convex-optimization, topic, numerical-optimization]
source: Nocedal & Wright, §3.4, Algorithms 3.2 and 3.3
---
# Newton's Method with Hessian Modification
Back to [Index](../Index.md) · Nocedal & Wright §3.4

Away from a minimizer the Hessian can be indefinite, and then the [Newton step](Newton's%20Method%20for%20Optimization.md) may point uphill. The fix is to change the matrix, not the method.

## Algorithm
```
for k = 0, 1, 2, ...
    B_k ← ∇²f_k + E_k        # E_k = 0 if ∇²f_k is safely positive definite
    solve B_k p_k = −∇f_k
    x_{k+1} ← x_k + α_k p_k   # α_k satisfies the Wolfe conditions
```
$B_k$ positive definite makes $p_k$ a [descent direction](Line%20Search%20Methods.md).

## Choosing $E_k$
**Eigenvalue modification.** From $\nabla^2 f_k = Q\Lambda Q^{\top}$, replace every eigenvalue below $\delta > 0$ by $\delta$. Clean, but an eigendecomposition is expensive, and a tiny $\delta$ produces a huge step along that eigenvector.

**Adding a multiple of the identity.** $E_k = \tau I$ with $\tau > -\lambda_{\min}$. Without knowing $\lambda_{\min}$, let the factorization decide:
```
τ ← 0 if min diagonal entry > 0, else −min(a_ii) + β
repeat:
    attempt the Cholesky factorization of A + τI
    if it succeeds: stop
    τ ← max(2τ, β)
```
[Cholesky](../../../academic/math-315/Topics%201/Cholesky%20Factorization.md) succeeds exactly when the matrix is [positive definite](../../../academic/math-315/Topics%201/Symmetric%20Positive%20Definite%20Matrices.md), so a failed factorization is the test.

**Modified Cholesky.** Increase diagonal entries during the factorization itself, so one pass gives $LDL^{\top} = A + E$ with bounded factors.

## Why it still converges
If the modified matrices have bounded condition number, $\kappa(B_k) \le C$, then $\cos\theta_k \ge 1/C$ and [Zoutendijk's Theorem](Zoutendijk's%20Theorem.md) gives $\lVert\nabla f_k\rVert \to 0$ from any start. Near a minimizer with positive definite Hessian, $E_k = 0$ and the quadratic rate of pure Newton returns.

See also: [EX11 - Log Det via Cholesky](../explorations/EX11%20-%20Log%20Det%20via%20Cholesky.md), [Levenberg-Marquardt Method](Levenberg-Marquardt%20Method.md) (the same $+\lambda I$ idea for least squares), [Trust-Region Methods](Trust-Region%20Methods.md)
