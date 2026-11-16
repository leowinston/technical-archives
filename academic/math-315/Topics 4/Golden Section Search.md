---
tags: [math-315, topic, chapter-7]
---
# Golden Section Search
Back to [Index](../Index.md) · Section 7.2.1 (textbook)

[Bisection](Bisection%20Method.md) for a minimum. It compares function values and never uses their sizes.

## Search points
For a [bracket](Univariate%20Minimization.md) $[a, b]$ of a U-shaped $f$:
$$
c = a + r(b - a), \qquad d = b - r(b - a), \qquad \boxed{\,r = \frac{3 - \sqrt5}{2} \approx 0.382\,}
$$
If $f(c) \le f(d)$ the new bracket is $[a, d]$, otherwise $[c, b]$.

## Why this $r$
Either new bracket has length $(1 - r)(b - a)$, and the surviving interior point must be a golden section point of the new bracket, so its function value is reused. In $[a, d]$ the old $c$ has to be the new $d$:
$$
r = (1 - r)^2 \quad\Longrightarrow\quad r^2 - 3r + 1 = 0
$$
The ratio of old to new length is $\dfrac{1}{1 - r} = \dfrac{1 + \sqrt5}{2} \approx 1.618$, the golden ratio.

## Cost and convergence
- Two evaluations to start, then **one per step**.
- Each step multiplies the bracket length by $1 - r \approx 0.618$: linear convergence.
- Reaching length $\varepsilon$ takes $n \approx \dfrac{\ln(\varepsilon/(b - a))}{\ln 0.618}$ steps.

Bisection gains a factor $0.5$ per evaluation and golden section $0.618$. Finding a minimum by comparison is slightly harder than finding a sign change.

## Error check
If $f$ at an interior point is at least $\max\{f(a), f(b)\}$, then $f$ is not U-shaped on the bracket and there may be several local minima.

## Explorations
- [EX54 - Golden Section Search for -e^-x sin x](../Explorations%204/EX54%20-%20Golden%20Section%20Search%20for%20-e^-x%20sin%20x.md)

See also: [Quadratic Interpolation Search](Quadratic%20Interpolation%20Search.md), [Order of Convergence](Order%20of%20Convergence.md)
