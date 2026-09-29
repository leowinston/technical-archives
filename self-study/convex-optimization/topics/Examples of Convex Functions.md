---
tags: [convex-optimization, topic, ch-3]
source: Boyd & Vandenberghe §3.1.5 (pp. 71–75)
---
# Examples of Convex Functions
Back to [[self-study/convex-optimization/Index|Index]] · Section 3.1.5

## On $\R$
| Function | Convex / concave |
|---|---|
| $e^{ax}$ | convex |
| $x^a$ on $\R_{++}$ | convex for $a \ge 1$ or $a \le 0$; concave for $0 \le a \le 1$ |
| $\lvert x\rvert^p$, $p \ge 1$ | convex |
| $\log x$ | concave |
| $x \log x$ (negative entropy) | convex |

## On $\R^n$
| Function | Why |
|---|---|
| any norm | triangle inequality + homogeneity |
| $\max_i x_i$ | max of linear functions |
| $x^2/y$, $y > 0$ | $\nabla^2 f \succeq 0$ |
| $\log\sum_i e^{x_i}$ | $\nabla^2 f = \operatorname{diag}(z) - zz^{\top} \succeq 0$, $z = $ softmax |
| $\big(\prod x_i\big)^{1/n}$ | concave |
| $\log\det X$ on $\Spd{n}$ | concave |

Log-sum-exp is a smooth max: $\max_i x_i \le \log\sum e^{x_i} \le \max_i x_i + \log n$.

## $\log\det X$ is concave
Restrict to a line $X = Z + tV$ with $Z \succ 0$, and let $\lambda_i$ be the eigenvalues of $Z^{-1/2}VZ^{-1/2}$:
$$
g(t) = \log\det Z + \sum_i \log(1 + t\lambda_i)
$$
Each term is concave in $t$, so $g$ is concave.

**Evaluating it without eigenvalues.** Factor $X = GG^{\top}$ (Cholesky). Then $\det X = \prod_k g_{kk}^2$, so
$$
\boxed{\log\det X = 2\sum_k \log g_{kk}}
$$
This is exact and costs $\tfrac13 n^3$ flops, versus $n!$ terms for cofactor expansion. The factorization succeeds iff $X \succ 0$, so it also checks the domain. Summing logs also avoids the overflow you get from forming $\det X$ first.

## Explorations
- [[EX02 - Checking Convexity with the Hessian]]
- [[EX11 - Log Det via Cholesky]]

See also: [[Second-Order Conditions]], [[Operations That Preserve Convexity of Functions]], [[academic/math-315/Topics/Cholesky Factorization|Cholesky Factorization]]
