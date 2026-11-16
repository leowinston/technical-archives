---
tags: [math-315, topic, lecture-7]
---
# False Position Method
Back to [Index](../Index.md) · Lecture 7

Regula falsi. [Bisection](Bisection%20Method.md) uses only the signs of $f(a)$ and $f(b)$. False position also uses their sizes.

## Idea
Interpolate $f$ at the endpoints of the bracket with a line:
$$
m(x) = \frac{f(b) - f(a)}{b - a}(x - a) + f(a)
$$
Since $f(a)\,f(b) < 0$, the line crosses zero inside $(a, b)$. Take that crossing as the new point:
$$
\boxed{\,x_n = a - f(a)\,\frac{b - a}{f(b) - f(a)}\,}
$$
Then keep the half that still brackets the root, exactly as in bisection.

## Convergence
- **Global:** the bracket is kept, so it always converges.
- **Linear, and sometimes slow:** if $f$ is convex or concave near the root, one endpoint never moves and the bracket does not shrink to zero.
- A small modification (halving the stale endpoint's function value) restores superlinear convergence.

## Versus the secant method
| | False position | [Secant Method](Secant%20Method.md) |
|---|---|---|
| Bracket required | yes | no |
| Points used | the two bracket endpoints | the two latest iterates |
| Convergence | guaranteed | only near the root |
| Rate | linear | superlinear, $\approx 1.618$ |

Same formula, different bookkeeping. Keeping the bracket buys safety and costs speed.

See also: [Order of Convergence](Order%20of%20Convergence.md)
