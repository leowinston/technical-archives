---
tags:
  - math-212
  - topic
  - chapter-6
---
# Transforms of Derivatives
Back to [Index](../Index.md) · Chapter 6.2 · Enrichment handout, Part IV

Differentiating in $t$ becomes multiplying by $s$. This is the one identity that makes the [Laplace transform](The%20Laplace%20Transform.md) useful for differential equations.

## First derivative
$$
\boxed{\mathcal{L}\{f'\}(s) = sF(s) - f(0)}
$$
**Proof.** Integrate by parts with $u = e^{-st}$, $dv = f'(t)\,dt$:
$$
\int_0^\infty e^{-st}f'(t)\,dt = \Big[e^{-st}f(t)\Big]_0^\infty + s\int_0^\infty e^{-st}f(t)\,dt = -f(0) + sF(s)
$$
The boundary term at $\infty$ vanishes because $f$ is of exponential order and $s$ is large enough. The term at $0$ is where the initial value enters.

## Second derivative
Apply the identity to $f'$:
$$
\mathcal{L}\{f''\} = s\,\mathcal{L}\{f'\} - f'(0) = s^2F(s) - sf(0) - f'(0)
$$

## In general
$$
\mathcal{L}\{f^{(n)}\} = s^nF(s) - s^{n-1}f(0) - \cdots - f^{(n-1)}(0)
$$

## What happened
- The derivative is gone. An ODE in $t$ turns into an algebraic equation in $s$.
- The initial conditions are built in. There are no constants $c_1, c_2$ to fit afterward.

See also: [Solving Initial Value Problems with the Laplace Transform](Solving%20Initial%20Value%20Problems%20with%20the%20Laplace%20Transform.md)
