---
tags: [math-212, topic, chapter-2]
---
# Existence and Uniqueness Theorems
Back to [[academic/math-212/Index|Index]] · Chapter 2.4

## Theorem 2.4.1 (linear)
If $p$ and $g$ are continuous on an open interval $I = (\alpha, \beta)$ containing $t_0$, then the IVP
$$
y' + p(t)y = g(t), \qquad y(t_0) = y_0
$$
has a unique solution $y = \phi(t)$ on **all of $I$**.

## Theorem 2.4.2 (nonlinear)
If $f$ and $\dfrac{\partial f}{\partial y}$ are continuous on an open rectangle containing $(t_0, y_0)$, then the IVP
$$
y' = f(t, y), \qquad y(t_0) = y_0
$$
has a unique solution on **some** interval $t_0 - h < t < t_0 + h$.

## Why 2.4.2 holds: Picard iteration
The IVP is equivalent to a fixed-point equation $\phi = T\phi$ for the map
$$
(T\phi)(t) = y_0 + \int_{t_0}^{t} f\big(s, \phi(s)\big)\,ds
$$
If $\lvert \partial f/\partial y \rvert \le K$, then $\max_t \lvert T\phi - T\psi \rvert \le Kh\,\max_t \lvert \phi - \psi \rvert$. For $Kh < 1$, $T$ is a contraction on the continuous functions on $[t_0 - h, t_0 + h]$, which form a complete space. [[archive/proofs/Explorations/Banach's Fixed Point Theorem|Banach's fixed point theorem]] then gives exactly one solution, and the iterates $\phi_{n+1} = T\phi_n$ converge to it. The requirement $h < 1/K$ is why the theorem only promises **some** interval.

Example: for $y' = y$, $y(0) = 1$, starting from $\phi_0 = 1$ gives $\phi_n = \sum_{k \le n} t^k/k!$, which converges to $e^t$.

## Linear vs nonlinear

| | Linear | Nonlinear |
|---|---|---|
| Where solutions break down | only where $p$ or $g$ is discontinuous, known in advance | depends on $y_0$ (vertical tangents, blow-up in finite time) |
| General solution | one formula with $c$ gives every solution | may miss **singular solutions** that no value of $c$ produces |
| Form of solution | explicit formula | often only implicit |

## Workbook problems
- [[WB1 P06 - General Solution of the Homogeneous Linear Equation]]
- [[WB1 P15 - Separable Equation with an Explicit Solution]] (the equilibrium $y = 1$ is missed by the formula)
- [[WB1 P16 - Separable IVP with Interval of Validity]]
- [[WB1 P26 - Critical Threshold Blow-Up]] (blow-up in finite time)

See also: [[Bernoulli Equations]]
