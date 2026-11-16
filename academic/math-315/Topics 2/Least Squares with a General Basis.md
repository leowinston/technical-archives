---
tags: [math-315, topic, lecture-4]
---
# Least Squares with a General Basis
Back to [Index](../Index.md) · Section 4.4

## Idea
Any basis $\phi_0, \dots, \phi_M$ works, not just powers of $x$. Build the design matrix $W_{ij} = \phi_j(x_i)$ and minimize $\|W\mathbf{a} - \mathbf{f}\|_2^2$:
$$
\boxed{\,W^{\top}W\,\mathbf{a} = W^{\top}\mathbf{f}\,}
$$
Only the matrix changes. The normal equations, Cholesky, and [QR](Least%20Squares%20via%20QR.md) are used exactly as before.

## Example
Basis $\{1,\ t,\ \cos2\pi t,\ \sin2\pi t\}$:
```python
W = np.column_stack([np.ones_like(t), t, np.cos(2*np.pi*t), np.sin(2*np.pi*t)])
```
Data built as $W\mathbf{a}_{\text{true}}$ is recovered to rounding error, since it lies in the column space of $W$.

## Notes
- $W^{\top}W$ is SPD when the columns of $W$ are independent.
- $\mathbf{f}$ in the column space gives residual $\|\mathbf{c}\|_2 = 0$.
- With $M = N$ the fit is interpolation and the residual is $0$.

## Explorations
- [EX33 - Least Squares Line and Quadratic for Four Points](../Explorations%202/EX33%20-%20Least%20Squares%20Line%20and%20Quadratic%20for%20Four%20Points.md)

See also: [Least Squares Fitting](Least%20Squares%20Fitting.md), [Normal Equations](Normal%20Equations.md), [Lab 10](../lab/lab%2010/Lab%2010%20-%20Least%20Squares,%20General%20Bases,%20and%20QR.md)
