---
tags: [math-315, topic, lecture-7]
---
# Roots and Fixed Points
Back to [Index](../Index.md) · Lecture 7

Two versions of the same problem.

## Definitions
- **Root finding:** find $x^*$ with $f(x^*) = 0$.
- **Fixed point:** find $x^*$ with $x^* = g(x^*)$, where the curve $y = g(x)$ crosses the line $y = x$.

## Converting between them
- Fixed point → root: take $f(x) = x - g(x)$.
- Root → fixed point: take $g(x) = x - c\,f(x)$ for any $c \neq 0$.

The conversion is not unique, and the choice decides everything. For $f(x) = \sin x - e^x$, all of these have the same fixed points:
$$
x = x + \sin x - e^x, \qquad x = x - \sin x + e^x, \qquad x = \ln(\sin x)
$$
but [fixed point iteration](Fixed%20Point%20Iteration.md) on one may converge while another diverges.

## Simple roots
$x^*$ is a **simple root** if $f(x^*) = 0$ and $f'(x^*) \neq 0$. Otherwise it is not simple: $f(x) = (x-1)^2$ touches the axis at $x = 1$ without crossing it. Simple roots are where the fast methods keep their speed.

## Does a root exist?
**Intermediate Value Theorem.** If $f$ is continuous on $[a, b]$ and $f(a)\,f(b) < 0$, there is at least one $x^* \in (a, b)$ with $f(x^*) = 0$. Such an interval is a **bracket**, and it is what the [Bisection Method](Bisection%20Method.md) keeps shrinking.

## The methods
| Global (bracket, always converge) | Local (need a good start, fast) |
|---|---|
| [Bisection Method](Bisection%20Method.md) | [Newton's Method](Newton's%20Method.md) |
| [False Position Method](False%20Position%20Method.md) | [Secant Method](Secant%20Method.md) |
| | [Inverse Quadratic Interpolation](Inverse%20Quadratic%20Interpolation.md) |

See also: [Order of Convergence](Order%20of%20Convergence.md), [Root Finding in Python](Root%20Finding%20in%20Python.md)
