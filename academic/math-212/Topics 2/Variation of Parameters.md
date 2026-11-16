---
tags:
  - math-212
  - topic
  - chapter-3
---
# Variation of Parameters
Back to [Index](../Index.md) · Chapter 3.6

For $P_0y'' + P_1y' + P_2y = F$ with a fundamental set $\{y_1, y_2\}$, look for $y_p = u_1y_1 + u_2y_2$ and impose $u_1'y_1 + u_2'y_2 = 0$:
$$
\begin{pmatrix} y_1 & y_2 \\ y_1' & y_2' \end{pmatrix}\begin{pmatrix} u_1' \\ u_2' \end{pmatrix} = \begin{pmatrix} 0 \\ F/P_0 \end{pmatrix}
$$
$$
\boxed{\,u_1' = -\frac{y_2F}{P_0W}, \qquad u_2' = \frac{y_1F}{P_0W}\,}
$$

## When to use it
- Variable coefficients (Euler equations, etc.), once $y_1, y_2$ are known.
- Forcing such as $\tan x$, $\sec x$, or $\ln x$, where undetermined coefficients has no trial form.

## Notes
- **Divide by $P_0$:** the formula needs $F/P_0$, not $F$.
- **Constants:** integration constants in $u_1, u_2$ only add $C_1y_1 + C_2y_2$.

## Workbook problems
- [WB2 P26 - Deriving Variation of Parameters](../Workbook%202/WB2%20P26%20-%20Deriving%20Variation%20of%20Parameters.md)
- [WB2 P27 - Variation of Parameters for an Euler Equation](../Workbook%202/WB2%20P27%20-%20Variation%20of%20Parameters%20for%20an%20Euler%20Equation.md)

See also: [Variation of Parameters](../Topics%201/Variation%20of%20Parameters.md) (first-order version)
