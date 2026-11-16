---
tags: [math-315, topic, lecture-4]
---
# Lagrange Form
Back to [Index](../Index.md) · Section 4.1.3

## Formula
$$
p_N(x) = \sum_{k=0}^{N} f_k\,\ell_k(x), \qquad
\ell_k(x) = \prod_{j=0,\,j\neq k}^{N}\frac{x - x_j}{x_k - x_j}
$$
Each basis polynomial is $1$ at its own node and $0$ at the others, $\ell_k(x_j) = \delta_{kj}$. So $p_N(x_i) = f_i$ with no linear system to solve.

## Quadratic case
$$
\ell_0 = \frac{(x - x_1)(x - x_2)}{(x_0 - x_1)(x_0 - x_2)}, \quad
\ell_1 = \frac{(x - x_0)(x - x_2)}{(x_1 - x_0)(x_1 - x_2)}, \quad
\ell_2 = \frac{(x - x_0)(x - x_1)}{(x_2 - x_0)(x_2 - x_1)}
$$

## Evaluating at $z$
```text
p = 0
for k = 0..N:
  num = f_k ; den = 1
  for j != k:  num *= (z - x_j) ; den *= (x_k - x_j)
  p += num / den
```

## Newton vs Lagrange
| Newton | Lagrange |
|---|---|
| Coefficients are easy to get | No linear system, so it is useful in theory |
| Cheap nested evaluation | Shows how each $f_i$ affects $p$ |
| Easy to add a node | |

## Explorations
- [EX27 - Lagrange Form for Collinear Data](../Explorations%202/EX27%20-%20Lagrange%20Form%20for%20Collinear%20Data.md)

See also: [Newton Form](Newton%20Form.md), [Linear Splines](Linear%20Splines.md)
