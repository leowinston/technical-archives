---
tags: [math-212, topic, chapter-2]
---
# Separable Equations
Back to [Index](../Index.md) · Chapter 2.2

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
- [WB1 P13 - Separable Equation with an Implicit Solution](../Workbook%201/WB1%20P13%20-%20Separable%20Equation%20with%20an%20Implicit%20Solution.md)
- [WB1 P14 - Separable Equation with cos x](../Workbook%201/WB1%20P14%20-%20Separable%20Equation%20with%20cos%20x.md)
- [WB1 P15 - Separable Equation with an Explicit Solution](../Workbook%201/WB1%20P15%20-%20Separable%20Equation%20with%20an%20Explicit%20Solution.md)
- [WB1 P16 - Separable IVP with Interval of Validity](../Workbook%201/WB1%20P16%20-%20Separable%20IVP%20with%20Interval%20of%20Validity.md)
- [WB1 P18 - Exact Equation 2](../Workbook%201/WB1%20P18%20-%20Exact%20Equation%202.md) (also separable)

See also: [Homogeneous Substitution](Homogeneous%20Substitution.md), [Existence and Uniqueness Theorems](Existence%20and%20Uniqueness%20Theorems.md)
