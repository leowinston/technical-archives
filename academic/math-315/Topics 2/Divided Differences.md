---
tags: [math-315, topic, lecture-4]
---
# Divided Differences
Back to [Index](../Index.md) · Section 4.1.2

## Definition
$$
f[x_i] = f(x_i), \qquad
f[x_i, \dots, x_{i+k}] = \frac{f[x_{i+1}, \dots, x_{i+k}] - f[x_i, \dots, x_{i+k-1}]}{x_{i+k} - x_i}
$$
The Newton coefficients are the top diagonal of the table:
$$
\boxed{\,c_j = f[x_0, \dots, x_j]\,}
$$

## Storage ($n = 3$)
A lower-triangular array, row $i$ and column $j$, with $d_{i,j} = f[x_{i-j}, \dots, x_i]$:
$$
\begin{array}{c|c|cccc}
i & x_i & j = 0 & j = 1 & j = 2 & j = 3 \\
 & & f[x_i] & f[x_{i-1}, x_i] & f[x_{i-2}, \dots, x_i] & f[x_{i-3}, \dots, x_i] \\ \hline
0 & x_0 & \boxed{d_{0,0}} & & & \\
1 & x_1 & d_{1,0} & \boxed{d_{1,1}} & & \\
2 & x_2 & d_{2,0} & d_{2,1} & \boxed{d_{2,2}} & \\
3 & x_3 & d_{3,0} & d_{3,1} & d_{3,2} & \boxed{d_{3,3}}
\end{array}
$$
Each entry uses the entry to its left and the one above that.

## Algorithm
```text
for i = 0..n:                 d[i,0] = f(x_i)
for j = 1..n:
  for i = n down to j:        d[i,j] = (d[i,j-1] - d[i-1,j-1]) / (x_i - x_{i-j})
for j = 0..n:                 c_j = d[j,j]
```

## Example
For $(-1, 0)$, $(0, 1)$, $(1, 3)$, $(2, 9)$:
$$
\begin{array}{c|c|cccc}
i & x_i & j = 0 & j = 1 & j = 2 & j = 3 \\ \hline
0 & -1 & \boxed{0} & & & \\
1 & 0 & 1 & \boxed{1} & & \\
2 & 1 & 3 & 2 & \boxed{\tfrac12} & \\
3 & 2 & 9 & 6 & 2 & \boxed{\tfrac12}
\end{array}
\qquad
p_3(x) = (x + 1) + \tfrac12(x + 1)x + \tfrac12(x + 1)x(x - 1)
$$

## Adding a node
$$
p_{n+1}(x) = p_n(x) + f[x_0, \dots, x_{n+1}]\,N_{n+1}(x)
$$

## Explorations
- [EX35 - Filling the Divided Difference Table Loop by Loop](../Explorations%202/EX35%20-%20Filling%20the%20Divided%20Difference%20Table%20Loop%20by%20Loop.md)
- [EX26 - Newton Form and Divided Differences Through Three Points](../Explorations%202/EX26%20-%20Newton%20Form%20and%20Divided%20Differences%20Through%20Three%20Points.md)

See also: [Newton Form](Newton%20Form.md)
