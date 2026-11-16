---
tags:
  - math-315
  - exploration
  - chapter-7
source: Textbook Example 7.2.1
topics:
  - "[[../Topics 4/Golden Section Search]]"
  - "[[../Topics 4/Univariate Minimization]]"
---
# EX54 — Golden Section Search for -e^-x sin x
Back to [Index](../Index.md)

> [!question] Problem
> Find the minimum of $f(x) = -e^{-x}\sin x$ on $[0, 1.5]$ by golden section search, stopping when the bracket is shorter than $10^{-5}$.
> (a) Find the exact minimizer by calculus.
> (b) Do the first refinement by hand.
> (c) Predict the number of steps, then count them.

## Solution
**(a)** $f'(x) = e^{-x}(\sin x - \cos x) = 0$ gives $\tan x = 1$, so $x^* = \pi/4 = 0.785398$ and $f(x^*) = -0.322397$. At the endpoints $f(0) = 0$ and $f(1.5) = -0.2226$, so the interior point is the minimum.

**(b)** With $r = \tfrac{3 - \sqrt5}{2} = 0.381966$:
$$
c = 0 + r(1.5) = 0.572949, \qquad d = 1.5 - r(1.5) = 0.927051
$$
$$
f(c) = -0.305676, \qquad f(d) = -0.316517
$$
Since $f(c) > f(d)$, the minimum is in $[c, b] = [0.572949,\ 1.5]$. The old $d$ is the new $c$, so only one new evaluation is needed, at the new $d = 1.5 - r(0.927051) = 1.145898$.

**(c)** Each step multiplies the length by $1 - r = 0.618034$:
$$
n \ge \frac{\ln(10^{-5}/1.5)}{\ln 0.618034} = 24.8
$$

```python
r = (3 - 5**0.5) / 2
a, b = 0.0, 1.5
c, d = a + r*(b - a), b - r*(b - a)
fc, fd = f(c), f(d)
while b - a > 1e-5:
    if fc < fd:
        b, d, fd = d, c, fc
        c = a + r*(b - a); fc = f(c)
    else:
        a, c, fc = c, d, fd
        d = b - r*(b - a); fd = f(d)
```

The loop runs $25$ times and uses $27$ function evaluations: two to start and one per step. The midpoint of the final bracket is $0.7854006$, within $2.5\times10^{-6}$ of $\pi/4$.

## Takeaways
- The count of steps is known before starting. It depends only on the bracket and the tolerance, as with bisection.
- Reusing one interior point is the whole reason for the constant $r$: any other placement would cost two evaluations per step.
- $25$ steps for five digits is slow. [Quadratic Interpolation Search](../Topics%204/Quadratic%20Interpolation%20Search.md) uses the sizes of the values, not only their order, to do better.

## Related topics
- [Golden Section Search](../Topics%204/Golden%20Section%20Search.md)
- [Univariate Minimization](../Topics%204/Univariate%20Minimization.md)
