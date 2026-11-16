---
tags:
  - math-315
  - exploration
  - chapter-5
source: Textbook Sections 5.2.4 and 5.3.2, Examples 5.3.9–5.3.11 and Problem 5.2.37, redone in Python
topics:
  - "[[../Topics 3/Improper Integrals]]"
  - "[[../Topics 3/Gauss Rules]]"
---
# EX51 — Singular Integrands sin x over x and cos x over sqrt x
Back to [Index](../Index.md)

> [!question] Problem
> (a) Compute $\int_{-0.5}^{1}\frac{\sin x}{x}dx$ and $\int_{-1}^{1}\frac{\sin x}{x}dx$ with `scipy.integrate.quad`. What goes wrong, and how do you fix it?
> (b) For $\int_0^1\frac{\cos x}{\sqrt x}dx$, replace $\cos x$ by $1 - \tfrac{x^2}{2}$ on $[0, \delta]$ and integrate $[\delta, 1]$ numerically. How accurate is this with $\delta = 0.1$?
> (c) How small must $\delta$ be for the two-term and three-term series to agree to four significant digits?

## Setup
- $\frac{\sin x}{x}$ has a **removable** singularity at $0$: the limit is $1$, but evaluating `np.sin(0)/0` gives `nan`
- $\frac{\cos x}{\sqrt x}$ has an **endpoint** singularity at $0$: it is unbounded, but the integral converges
- $\cos x = 1 - \tfrac{x^2}{2} + \tfrac{x^4}{24} - \cdots$ is alternating

## Strategy
1. Check whether a quadrature point lands on the singularity.
2. Integrate the series by hand near $0$ and let `quad` do the rest.

## Solution
**(a) The interior singularity**

```python
f = lambda x: np.sin(x)/x
quad(f, -0.5, 1)                    # (1.4391904884102, 1.6e-14)
quad(f, -1, 1)                      # (nan, nan) with a RuntimeWarning
quad(f, -1, 0)[0] + quad(f, 0, 1)[0]  # 1.892166140734366
```
On $[-0.5, 1]$ no point is at $0$, so `quad` succeeds. On $[-1, 1]$ the interval is symmetric, and the Gauss-Kronrod rule has a node at the center $x = 0$, so the first evaluation is `nan`.

Two fixes:
1. Split at $0$, so the singularity becomes an endpoint, which the open rule never evaluates.
2. Remove the singularity: `np.sinc(x/np.pi)` equals $\frac{\sin x}{x}$ with value $1$ at $0$.

**(b) The series near the endpoint**

On $[0, \delta]$:
$$
\int_0^\delta\frac{1 - x^2/2}{\sqrt x}dx = \int_0^\delta\big(x^{-1/2} - \tfrac12x^{3/2}\big)dx = 2\sqrt\delta - \frac{\delta^{5/2}}{5}
$$
With $\delta = 0.1$: $2(0.316228) - 0.000632 = 0.631823$. Adding `quad` on $[0.1, 1]$ gives
$$
0.631823 + 1.177225 = 1.8090482, \qquad \text{reference } 1.8090485
$$
The error is $2.9\times10^{-7}$. The next series term gives it exactly:
$$
\int_0^\delta\frac{x^4/24}{\sqrt x}dx = \frac{\delta^{9/2}}{108} = \frac{3.16\times10^{-5}}{108} = 2.9\times10^{-7} \ \checkmark
$$
Because the series alternates, the error is less than this first omitted term.

**(c) How small $\delta$ must be**

The two approximations differ by $\delta^{9/2}/108$. Four significant digits of $1.809$ means a difference under $5\times10^{-4}$:
$$
\frac{\delta^{9/2}}{108} < 5\times10^{-4} \implies \delta^{9/2} < 0.054 \implies \delta < 0.52
$$
Any $\delta \le 0.5$ works, and $\delta = 0.1$ is far more than enough.

## Result
- $\int_{-1}^1\frac{\sin x}{x}dx = 1.892166\ldots$, after splitting at $0$
- $\int_0^1\frac{\cos x}{\sqrt x}dx = 1.8090485\ldots$, and the series split with $\delta = 0.1$ is good to $3\times10^{-7}$

## Takeaways
- An interior singularity breaks `quad` only if a node lands on it, which is luck. Split at known singular points, or pass `points=[0]`.
- Open (Gauss) rules survive endpoint singularities. Closed (Lobatto) rules evaluate the endpoint and fail.
- An analytic series near the singularity plus numerical integration elsewhere is cheap and accurate.

## Related topics
- [Improper Integrals](../Topics%203/Improper%20Integrals.md)
- [Gauss Rules](../Topics%203/Gauss%20Rules.md)
- [Lobatto Rules](../Topics%203/Lobatto%20Rules.md)
