---
tags: [math-315, topic, lecture-7]
---
# Bisection Method
Back to [Index](../Index.md) · Lecture 7

Halve a bracket and keep the half where the sign still changes. It uses only the signs of $f$.

## One step
Given $f$ continuous on $[a, b]$ with $f(a)\,f(b) < 0$, set $c = \tfrac{a+b}{2}$.
1. $f(c) = 0$: done.
2. $f(a)\,f(c) < 0$: the root is in $(a, c)$, so set $b = c$.
3. Otherwise the root is in $(c, b)$, so set $a = c$.

Stop when $\lvert f(c)\rvert \le \text{tol}_1$ or $b - a \le \text{tol}_2$.

```python
def bisection(f, a, b, tol=1e-6, max_iter=1000):
    for _ in range(max_iter):
        x = 0.5 * (a + b)
        fx = f(x)
        if abs(fx) < tol:
            break
        if f(a) * fx < 0:
            b = x
        else:
            a = x
    return x, fx
```

## Convergence
**Theorem.** The midpoints $c_n$ converge to a root $x^*$, and
$$
\boxed{\,\lvert c_n - x^*\rvert \le \frac{b - a}{2^{n}}\,}
$$
The error bound halves every step: [order](Order%20of%20Convergence.md) $1$ with constant $\tfrac12$. Reaching tolerance $\varepsilon$ takes about $\log_2\frac{b-a}{\varepsilon}$ steps, no matter what $f$ looks like.

## Trade-off
- **Global:** it cannot fail once a bracket is known.
- **Slow:** one bit per function evaluation.
- It cannot find a root of even multiplicity, because $f$ does not change sign there.

[Golden Section Search](Golden%20Section%20Search.md) is the same idea for a minimum instead of a root.

See also: [False Position Method](False%20Position%20Method.md), [Roots and Fixed Points](Roots%20and%20Fixed%20Points.md)
