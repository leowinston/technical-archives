---
tags: [convex-optimization, topic, ch-4]
source: Boyd & Vandenberghe §4.5 (pp. 160–165)
---
# Geometric Programming
Back to [Index](../Index.md) · Section 4.5

## Monomials and posynomials
For $x \in \R^n_{++}$:
$$
\text{monomial } f(x) = c\,x_1^{a_1}\cdots x_n^{a_n},\ c > 0; \qquad \text{posynomial} = \text{sum of monomials}.
$$

## GP
$$
\begin{array}{ll}
\text{minimize} & f_0(x) \\
\text{subject to} & f_i(x) \le 1 \ \ (\text{posynomials}),\ \ h_i(x) = 1 \ \ (\text{monomials})
\end{array}
$$
Not convex as written.

## Convex form
Substitute $y_i = \log x_i$ and take logs. A monomial becomes affine, $\log f = a^{\top}y + b$, and a posynomial becomes log-sum-exp:
$$
\boxed{\,\log\sum_{k} e^{a_k^{\top}y + b_k}\,}
$$
This is convex, so the GP becomes a convex problem.

## Example: cantilever beam
Choose segment widths $w_i$ and heights $h_i$ to minimize the weight $\sum w_ih_i$, subject to stress, aspect-ratio, and tip-deflection limits. Each constraint is a posynomial, so the design is a GP.

See also: [Examples of Convex Functions](Examples%20of%20Convex%20Functions.md), [Log-Concave and Log-Convex Functions](Log-Concave%20and%20Log-Convex%20Functions.md)
