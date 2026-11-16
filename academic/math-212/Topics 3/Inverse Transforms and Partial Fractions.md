---
tags:
  - math-212
  - topic
  - chapter-6
---
# Inverse Transforms and Partial Fractions
Back to [Index](../Index.md) · Chapter 6.2 · Enrichment handout, Part V and beyond

Going from $Y(s)$ back to $y(t)$ means reading the [transform table](The%20Laplace%20Transform.md) backward. Two continuous functions with the same transform are equal, so the answer is unique.

## Partial fractions
Split a rational $Y(s)$ into table entries. For a simple root $r$ of the denominator, the coefficient of $\dfrac{1}{s-r}$ is
$$
A = \Big[(s - r)\,Y(s)\Big]_{s=r}
$$
**Example.** $\dfrac{1}{s(s+2)}$: at $s = 0$, $A = \tfrac12$. At $s = -2$, $B = -\tfrac12$.

## First shift theorem
$$
\boxed{\mathcal{L}\{e^{at}f(t)\} = F(s-a)}
$$
Multiplying by $e^{at}$ slides the transform to the right by $a$.

## Poles decide the solution
| Factor in the denominator | Table entry | Term in $y(t)$ |
|---|---|---|
| $s - r$ | $\dfrac{1}{s-r}$ | $e^{rt}$ |
| $(s-r)^2$ | $\dfrac{1}{(s-r)^2}$ | $te^{rt}$ |
| $(s-\lambda)^2 + \mu^2$ | $\dfrac{s-\lambda}{(s-\lambda)^2+\mu^2}$, $\dfrac{\mu}{(s-\lambda)^2+\mu^2}$ | $e^{\lambda t}\cos\mu t$, $e^{\lambda t}\sin\mu t$ |

These are the distinct, repeated, and [complex root](../Topics%202/Complex%20Roots%20of%20the%20Characteristic%20Equation.md) cases of the characteristic equation.

**Example.** Complete the square:
$$
\frac{1}{s^2+4s+13} = \frac13\cdot\frac{3}{(s+2)^2+9} \quad\longmapsto\quad \tfrac13e^{-2t}\sin 3t
$$

See also: [Solving Initial Value Problems with the Laplace Transform](Solving%20Initial%20Value%20Problems%20with%20the%20Laplace%20Transform.md)
