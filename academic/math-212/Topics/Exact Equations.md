---
tags: [math-212, topic, chapter-2]
---
# Exact Equations
Back to [Index](../Index.md) · Chapter 2.6

## Definition
$M(x, y)\,dx + N(x, y)\,dy = 0$ is **exact** if there is a potential function $\psi$ with
$$
\psi_x = M, \qquad \psi_y = N
$$
The solutions are then the level curves $\psi(x, y) = c$.

## Theorem 2.6.1 (test for exactness)
If $M, N, M_y, N_x$ are continuous on a simply connected region $R$, then
$$
\text{exact on } R \iff M_y = N_x
$$

## Strategy for finding $\psi$
1. Check that $M_y = N_x$.
2. Integrate $M$ with respect to $x$: $\psi = \int M\,dx + h(y)$.
3. Differentiate with respect to $y$ and set $\psi_y = N$. This gives $h'(y)$, which must depend on $y$ alone.
4. Integrate to get $h(y)$ and write $\psi(x, y) = c$.

You can also start from $\int N\,dy + g(x)$ when that integral is easier.

## Workbook problems
- [WB1 P17 - Exact Equation 1](../Workbook%201/WB1%20P17%20-%20Exact%20Equation%201.md)
- [WB1 P18 - Exact Equation 2](../Workbook%201/WB1%20P18%20-%20Exact%20Equation%202.md)
- [WB1 P19 - Non-Exact Equation Made Exact by x](../Workbook%201/WB1%20P19%20-%20Non-Exact%20Equation%20Made%20Exact%20by%20x.md)

See also: [Integrating Factors for Exact Equations](Integrating%20Factors%20for%20Exact%20Equations.md)
