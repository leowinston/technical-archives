---
tags:
  - math-315
  - exploration
  - lecture-4
source: Lecture 4 handout, pp. 12–13 (Section 4.2, Runge's function)
topics:
  - "[[../Topics 2/Interpolation Error]]"
  - "[[../Topics 2/Chebyshev Polynomials]]"
---
# EX29 — Runge Function with Equispaced and Chebyshev Nodes
Back to [Index](../Index.md)

> [!question] Problem
> Interpolate $f(x) = \dfrac{1}{1 + x^2}$ on $[-5, 5]$.
> (a) Use $11$ equally spaced points.
> (b) Use $20$ equally spaced points.
> (c) Use $11$ Chebyshev points.
> Compare the maximum errors, and explain them with the bound $\max|\omega_{N+1}|\cdot\max|f^{(N+1)}|/(N+1)!$.

## Setup
- Measure the maximum error on a fine grid of $20001$ points in $[-5, 5]$.
- The Chebyshev nodes are $x_i = -5\cos\big(\tfrac{2i+1}{2N+2}\pi\big)$, as in [EX28](EX28%20-%20Chebyshev%20Polynomials%20T2%20to%20T5%20and%20Their%20Zeros.md).

```python
f = lambda t: 1 / (1 + t**2)
xx = np.linspace(-5, 5, 20001)
def max_err(nodes):
    c = np.polyfit(nodes, f(nodes), len(nodes) - 1)
    return np.max(np.abs(f(xx) - np.polyval(c, xx)))
eq = np.linspace(-5, 5, 11)
ch = -5 * np.cos((2 * np.arange(11) + 1) / 22 * np.pi)
```

## Strategy
1. Compute the errors numerically.
2. Split the bound into a node factor $\max|\omega_{N+1}|$ and a function factor.
3. See which factor each node choice controls.

## Solution
**Maximum errors**

| Nodes | $n$ points | $\max\lvert f - p\rvert$ |
|---|---|---|
| equally spaced | 11 | $1.92$ |
| equally spaced | 20 | $8.58$ |
| equally spaced | 21 | $59.8$ |
| Chebyshev | 11 | $0.109$ |
| Chebyshev | 21 | $0.0153$ |

With equal spacing, adding points makes the error **worse**, and it peaks near $x = \pm5$. With Chebyshev nodes the error decreases steadily.

**The node factor $\max_{[-5,5]}|\omega_{N+1}|$**

| $n$ points | equally spaced | Chebyshev |
|---|---|---|
| 11 | $4.2 \times 10^{5}$ | $4.8 \times 10^{4}$ |
| 21 | $1.1 \times 10^{11}$ | $4.5 \times 10^{8}$ |

Chebyshev nodes give the smallest possible value, $2\big(\tfrac{b - a}{4}\big)^{N+1}$. For $N = 10$ that is $2(2.5)^{11} \approx 47{,}684$, as in the table. Equally spaced nodes leave $\omega_{N+1}$ huge near the endpoints, where every factor $|x - x_i|$ is large at once.

**The function factor**

For Runge's function, $f(x) = \sum_k(-1)^kx^{2k}$ near $0$, so $|f^{(n)}(0)|/n! = 1$ for every even $n$. The function factor $\max|f^{(N+1)}|/(N+1)!$ therefore never shrinks. This is because $f$ has complex poles at $\pm i$, close to the interval. On $[-5, 5]$ both node factors still grow with $N$, so the bound alone cannot guarantee convergence for either choice. The bound is not sharp.

What the node factor does explain is the comparison. Chebyshev nodes make $\max|\omega_{N+1}|$ about $9\times$ smaller at $11$ points and about $245\times$ smaller at $21$ points. They also spread $|\omega_{N+1}|$ evenly, instead of piling it up at $\pm5$ where the equally spaced error explodes. In practice Chebyshev interpolation of Runge's function converges, which needs a sharper analytic argument beyond this lecture, while equally spaced interpolation diverges.

## Result
- With $11$ equally spaced points the error is $1.92$. With $20$ it is $8.58$.
- With $11$ Chebyshev points the error is $0.109$, and with $21$ it is $0.015$.

## Takeaways
- A higher degree is not automatically better. With equally spaced nodes it can diverge.
- The choice of nodes controls only $\omega_{N+1}$, and Chebyshev nodes minimize its maximum.
- The other fix is to keep the degree low and shrink the interval, which is the idea behind [Linear Splines](../Topics%202/Linear%20Splines.md).

## Related topics
- [Interpolation Error](../Topics%202/Interpolation%20Error.md)
- [Chebyshev Polynomials](../Topics%202/Chebyshev%20Polynomials.md)
