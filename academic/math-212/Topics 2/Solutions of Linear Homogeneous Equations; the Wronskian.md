---
tags:
  - math-212
  - topic
  - chapter-3
---
# Solutions of Linear Homogeneous Equations; the Wronskian
Back to [Index](../Index.md) · Chapter 3.2

## Wronskian
$$
W(y_1, y_2)(x) = \begin{vmatrix} y_1 & y_2 \\ y_1' & y_2' \end{vmatrix} = y_1y_2' - y_1'y_2
$$

## Theorem 3.2.4 (fundamental set)
If $y_1, y_2$ solve $y'' + p y' + q y = 0$ on $I$ and $W(x_0) \neq 0$ for some $x_0 \in I$, then **every** solution is $c_1y_1 + c_2y_2$. The IVP system for $c_1, c_2$ is solvable because its determinant is $W(x_0)$.

## Abel's theorem
$$
W(x) = C\,e^{-\int p(x)\,dx}
$$
So $W$ is either identically $0$ or never $0$ on $I$.

## Useful formula
$W\left(e^{r_1x}, e^{r_2x}\right) = (r_2 - r_1)e^{(r_1 + r_2)x}$, which is nonzero iff $r_1 \neq r_2$.

## Workbook problems
- [WB2 P04 - Wronskian for y'' - y = 0](../Workbook%202/WB2%20P04%20-%20Wronskian%20for%20y%27%27%20-%20y%20=%200.md)
- [WB2 P05 - Wronskian for y'' + 6y' + 5y = 0](../Workbook%202/WB2%20P05%20-%20Wronskian%20for%20y%27%27%20+%206y%27%20+%205y%20=%200.md)
- [WB2 P06 - Wronskian for y'' + 5y' + 6y = 0](../Workbook%202/WB2%20P06%20-%20Wronskian%20for%20y%27%27%20+%205y%27%20+%206y%20=%200.md)
- [WB2 P26 - Deriving Variation of Parameters](../Workbook%202/WB2%20P26%20-%20Deriving%20Variation%20of%20Parameters.md)
- [WB2 P27 - Variation of Parameters for an Euler Equation](../Workbook%202/WB2%20P27%20-%20Variation%20of%20Parameters%20for%20an%20Euler%20Equation.md)
