---
tags: [math-315, topic, chapter-5]
---
# Gauss Rules
Back to [Index](../Index.md) · Section 5.2.4 (textbook)

Gauss rules choose **both** the points and the weights on $[-1, 1]$ to maximize the [DOP](Degree%20of%20Precision.md). With $2(N+1)$ unknowns, they satisfy $2(N+1)$ equations of precision.

## Properties of the $(N+1)$-point rule
1. All weights $w_i > 0$, and all points lie in the open interval $(-1, 1)$.
2. Points and weights are symmetric about $0$.
3. The points of consecutive rules interlace.
4. It is interpolatory at its own points.
5. $\boxed{\,\text{DOP} = 2N + 1\,}$, almost twice the number of points.

## Small rules
| Points | Nodes | Weights | DOP | $\kappa$ |
|---|---|---|---|---|
| 1 | $0$ | $2$ | 1 | $\tfrac13$ (midpoint) |
| 2 | $\pm\tfrac1{\sqrt3}$ | $1, 1$ | 3 | $\tfrac1{135}$ |
| 3 | $0, \pm\sqrt{3/5}$ | $\tfrac89, \tfrac59$ | 5 | $\tfrac1{15750}$ |

## Gauss-Kronrod
To estimate the error, keep the $N + 1$ Gauss points, add $N + 2$ new ones, and reoptimize all $2N + 3$ weights. The Kronrod rule has DOP at least $3N + 2$ for the cost of $N + 2$ new evaluations.

## Why positive weights inside the interval
Weights sum to $2$, so positive weights mean no [cancellation](../Topics%201/Cancellation%20Error.md). Interior points mean the rule never evaluates $f$ at an endpoint singularity.

## In Python
```python
t, w = np.polynomial.legendre.leggauss(n)       # nodes and weights on [-1, 1]
val, _ = scipy.integrate.fixed_quad(f, a, b, n=n)
```

## Explorations
- [EX45 - Two- and Three-Point Gauss Rules](../Explorations%203/EX45%20-%20Two-%20and%20Three-Point%20Gauss%20Rules.md)
- [EX47 - Gauss Two-Point Rule on a General Interval](../Explorations%203/EX47%20-%20Gauss%20Two-Point%20Rule%20on%20a%20General%20Interval.md)

See also: [Lobatto Rules](Lobatto%20Rules.md), [Adaptive Integration](Adaptive%20Integration.md), [Chebyshev Polynomials](../Topics%202/Chebyshev%20Polynomials.md)
