---
tags: [math-315, topic, lecture-7]
---
# Root Finding in Python
Back to [Index](../Index.md) · Lecture 7

## A general function: `root_scalar`
```python
import numpy as np
from scipy.optimize import root_scalar

f = lambda x: np.cos(x) - x
root_scalar(f, x0=0, fprime=lambda x: -np.sin(x) - 1, method='newton')
root_scalar(f, bracket=[-1, 1], method='bisect')
root_scalar(f, bracket=[-1, 1])        # Brent: bisection + secant + inverse quadratic
```
With a bracket, the default combines [bisection](Bisection%20Method.md), [secant](Secant%20Method.md), and [inverse quadratic interpolation](Inverse%20Quadratic%20Interpolation.md).

## When to give a bracket
1. **To pick which root.** For $f = \sin x$, Newton from $x_0 = 1$ finds $0$ and from $x_0 = 5$ finds $2\pi$. The bracket $[1, 5]$ finds $\pi$.
2. **Near a singularity.** For $f = x - \tan x$, Newton converges from $x_0 = 1$ and from few other places.

## Multiple roots
- Even multiplicity has no sign change, so there is no bracket: $x^2e^x$ on $[-1, 1]$ fails with `bisect`.
- [Newton](Newton's%20Method.md) still converges to a double root but only linearly, and stops near $10^{-8}$ instead of $10^{-16}$.
- Newton can also run away. For $xe^x$ the step is $x_{n+1} = x_n^2/(1 + x_n)$, so a start left of $-1$ moves further left every step until $e^x$ underflows and $f$ is reported as $0$ at a huge negative $x$ (the handout's run ends near $-925$).

## Polynomials: `numpy.roots`
```python
np.roots([1, -4, 4])     # x^2 - 4x + 4  ->  [2., 2.]
```
It builds the **companion matrix** of the polynomial and returns its eigenvalues. It finds all roots at once, complex and repeated ones included, with no starting guess.

See also: [Roots and Fixed Points](Roots%20and%20Fixed%20Points.md), [Order of Convergence](Order%20of%20Convergence.md)
