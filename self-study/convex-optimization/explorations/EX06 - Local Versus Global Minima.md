---
tags: [convex-optimization, exploration, ch-4]
source: Book §4.2.2 (p. 138, ✎ "any locally optimal point is also globally optimal" highlighted)
topics: ["[[Local and Global Optima]]", "[[Second-Order Conditions]]"]
---
# EX06 — Local Versus Global Minima
Back to [Index](../Index.md)

> [!question] Problem
> Let $f(x) = x^4 - 3x^2 + x$.
> (a) Find all stationary points and classify them.
> (b) Why does this not contradict §4.2.2?
> (c) Where does the proof of §4.2.2 break?

## Solution
**(a)** $f'(x) = 4x^3 - 6x + 1 = 0$ and $f''(x) = 12x^2 - 6$.

| $x$ | $f(x)$ | $f''(x)$ | Type |
|---|---|---|---|
| $-1.3008$ | $-3.5139$ | $14.31$ | **global** min |
| $0.1699$ | $0.0841$ | $-5.65$ | local max |
| $1.1309$ | $-1.0702$ | $9.35$ | local min, **not global** |

```python
import numpy as np
r = np.sort(np.roots([4, 0, -6, 1]).real)
print(r, r**4 - 3*r**2 + r)  # [-1.3008 0.1699 1.1309] [-3.5139 0.0841 -1.0702]
```

**(b)** $f''(0) = -6 < 0$, so $f$ is **not convex**. The theorem needs convexity.

**(c)** Take the local min $x = 1.1309$ and $y = -1.3008$. The proof steps to $z = (1-\theta)x + \theta y$ and needs $f(z) \le (1-\theta)f(x) + \theta f(y) < f(x)$. That first inequality is convexity, and it fails here: at the midpoint $z = -0.085$, $f(z) = -0.106$, which is above the chord value $-2.292$.

## Graph
```desmos-graph
left=-2.2; right=2.2; top=3; bottom=-4.5
---
y=x^{4}-3x^{2}+x|#2d70b3
(-1.3008,-3.5139)|#388c46
(1.1309,-1.0702)|#c74440
y=-1.0702+1.0049(x-1.1309)|x>-1.3008|x<1.1309|dashed|#c74440
```
Green: the global min. Red: the local min. The dashed chord between them passes **below** the graph.

## Takeaways
- For nonconvex $f$, gradient descent started at $x > 0.17$ gets stuck at $1.13$.
- For convex $f$, "stuck" is impossible, because every local min is global.

## Related topics
- [Local and Global Optima](../topics/Local%20and%20Global%20Optima.md)
- [Second-Order Conditions](../topics/Second-Order%20Conditions.md)
