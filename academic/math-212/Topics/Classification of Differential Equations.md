---
tags: [math-212, topic, chapter-1]
---
# Classification of Differential Equations
Back to [Index](../Index.md) · Chapter 1.3

## Checklist
1. **Type:** ordinary (ODE, one independent variable) or partial (PDE)
2. **Order:** the order of the highest derivative
3. **Linearity:** linear or nonlinear
4. **Homogeneity (linear only):** homogeneous if $g = 0$, otherwise nonhomogeneous
5. **Coefficients:** constant or variable
6. **Single equation or system** (see [Systems of Differential Equations](Systems%20of%20Differential%20Equations.md))

## General forms
$$
\begin{align*}
\text{Implicit: } & F\left(t, y, y', \dots, y^{(n)}\right) = 0 \\
\text{Explicit: } & y^{(n)} = f\left(t, y, y', \dots, y^{(n-1)}\right)
\end{align*}
$$

## Linear ODE of order $n$
$$
a_0(t)y^{(n)} + a_1(t)y^{(n-1)} + \cdots + a_n(t)y = g(t)
$$

An equation is **linear** when $y$ and its derivatives
- appear only to the first power
- are never multiplied by each other
- never appear inside a function like $\sin y$, $e^y$, or $\ln y$

The coefficients may be any functions of $t$.

## PDE examples
$$
\begin{align*}
\text{Heat: } & \alpha^2 u_{xx} = u_t \\
\text{Wave: } & a^2 u_{xx} = u_{tt} \\
\text{Laplace: } & u_{xx} + u_{yy} = 0
\end{align*}
$$

## Workbook problems
- [WB1 P02 - Direct Integration of y'' = 3x + 1](../Workbook%201/WB1%20P02%20-%20Direct%20Integration%20of%20y%27%27%20%3D%203x%20%2B%201.md)
- [WB1 P03 - Classifying Linear and Nonlinear Equations](../Workbook%201/WB1%20P03%20-%20Classifying%20Linear%20and%20Nonlinear%20Equations.md)
