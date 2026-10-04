---
tags: [convex-optimization, topic, ch-3]
source: Boyd & Vandenberghe §3.3 (pp. 90–95)
---
# Conjugate Function
Back to [Index](../Index.md) · Section 3.3

## Definition
$$
\boxed{\,f^{*}(y) = \sup_{x \in \dom f}\big(y^{\top}x - f(x)\big)\,}
$$
$f^{*}$ is always convex (a sup of affine functions of $y$), even if $f$ is not.

## Examples
| $f(x)$ | $f^{*}(y)$ |
|---|---|
| $ax + b$ | $-b$ at $y = a$, else $\infty$ |
| $e^{x}$ | $y\log y - y$ |
| $-\log x$ | $-1 - \log(-y)$, $y < 0$ |
| $\tfrac12 x^{\top}Qx$, $Q \succ 0$ | $\tfrac12 y^{\top}Q^{-1}y$ |
| $\lVert x\rVert$ | $0$ if $\lVert y\rVert_{*} \le 1$, else $\infty$ |

## Properties
- **Fenchel's inequality:** $f(x) + f^{*}(y) \ge x^{\top}y$.
- **Legendre transform:** for differentiable convex $f$, $f^{*}(y) = x^{\star\top}\nabla f(x^\star) - f(x^\star)$ where $y = \nabla f(x^\star)$.
- $f^{**} = f$ for closed convex $f$.

See also: [Operations That Preserve Convexity of Functions](Operations%20That%20Preserve%20Convexity%20of%20Functions.md)
