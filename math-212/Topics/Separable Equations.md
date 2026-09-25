---
tags: [math-212, topic, chapter-2]
---
# Separable Equations
Back to [[Index]] · Chapter 2.2

## Definition
$y' = f(x, y)$ is **separable** if it can be written as
$$
M(x)\,dx + N(y)\,dy = 0 \qquad\text{equivalently}\qquad \frac{dy}{dx} = g(x)\,h(y)
$$

## Solution
$$
\int M(x)\,dx + \int N(y)\,dy = c \implies H_1(x) + H_2(y) = c
$$

### Strategy
1. Move every $y$ term to the side with $dy$ and every $x$ term to the side with $dx$.
2. **Before dividing by $h(y)$**, find the roots of $h(y) = 0$. They are equilibrium solutions that the division would lose.
3. Integrate both sides. This usually gives an **implicit** solution.
4. Solve for $y$ if you can (an explicit solution). Apply any initial condition.
5. Find the **interval of validity**. It ends where the solution stops existing, for example at a vertical tangent where $N(y) = 0$ or where a square root's radicand hits zero.

## Workbook problems
- [[WB1 P13 - Separable Equation with an Implicit Solution]]
- [[WB1 P14 - Separable Equation with cos x]]
- [[WB1 P15 - Separable Equation with an Explicit Solution]]
- [[WB1 P16 - Separable IVP with Interval of Validity]]
- [[WB1 P18 - Exact Equation 2]] (also separable)

See also: [[Homogeneous Substitution]], [[Existence and Uniqueness Theorems]]
