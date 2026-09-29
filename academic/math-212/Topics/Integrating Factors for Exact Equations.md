---
tags: [math-212, topic, chapter-2]
---
# Integrating Factors for Exact Equations
Back to [[academic/math-212/Index|Index]] · Chapter 2.6

If $M_y \neq N_x$, look for $\mu$ with $(\mu M)_y = (\mu N)_x$:
$$
M\mu_y - N\mu_x + (M_y - N_x)\mu = 0
$$
This PDE is usually hard to solve. Two special cases are easy.

| Condition | Integrating factor |
|---|---|
| $\dfrac{M_y - N_x}{N} = Q(x)$ depends only on $x$ | $\mu(x) = \exp\left(\displaystyle\int Q(x)\,dx\right)$ |
| $\dfrac{N_x - M_y}{M} = P(y)$ depends only on $y$ | $\mu(y) = \exp\left(\displaystyle\int P(y)\,dy\right)$ |

### Strategy
1. Compute $M_y - N_x$.
2. Divide by $N$. If only $x$ remains, use $\mu(x)$.
3. Otherwise divide $N_x - M_y$ by $M$. If only $y$ remains, use $\mu(y)$.
4. Multiply the whole equation by $\mu$, confirm it is now exact, and solve as an [[Exact Equations|exact equation]].

## Workbook problems
- [[WB1 P19 - Non-Exact Equation Made Exact by x]]
- [[WB1 P20 - Integrating Factor mu(x)]]
- [[WB1 P21 - Integrating Factor mu(y)]]
