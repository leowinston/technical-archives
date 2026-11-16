---
tags: [math-315, topic, lecture-4]
---
# Linear Splines
Back to [Index](../Index.md) · Section 4.3.1

## Definition
For $a = x_0 < x_1 < \cdots < x_N = b$ with $h = \max_i|x_i - x_{i-1}|$, the spline $S_{1,N}$ is the continuous broken line through the data. On $[x_{i-1}, x_i]$:
$$
S_{1,N}(x) = f_{i-1}\,\frac{x - x_i}{x_{i-1} - x_i} + f_i\,\frac{x - x_{i-1}}{x_i - x_{i-1}}
$$

## Error
$$
\max_{[a,b]}|f - S_{1,N}| \le \frac{h^2}{8}\max_{[a,b]}|f''|
$$
With equally spaced nodes, $h = (b - a)/N$, so the error goes to $0$ like $1/N^2$.

## Hat basis (linear B-splines)
$L_i(x_j) = \delta_{ij}$, and $L_i$ is nonzero only on $[x_{i-1}, x_{i+1}]$:
$$
L_i(x) = \begin{cases}
\dfrac{x - x_{i-1}}{x_i - x_{i-1}} & x \in [x_{i-1}, x_i] \\[1ex]
\dfrac{x - x_{i+1}}{x_i - x_{i+1}} & x \in [x_i, x_{i+1}] \\[1ex]
0 & \text{otherwise}
\end{cases}
\qquad
S_{1,N}(x) = \sum_{i=0}^{N} f_i\,L_i(x)
$$
$L_0$ and $L_N$ keep only their inner half.

## Limitation
$S_{1,N}'$ jumps at the knots. [Cubic Splines](Cubic%20Splines.md) fix this.

## Explorations
- [EX30 - Linear Spline in Two Bases](../Explorations%202/EX30%20-%20Linear%20Spline%20in%20Two%20Bases.md)

See also: [Interpolation Error](Interpolation%20Error.md), [Lagrange Form](Lagrange%20Form.md)
