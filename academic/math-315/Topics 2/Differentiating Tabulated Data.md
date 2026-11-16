---
tags: [math-315, topic, chapter-5]
---
# Differentiating Tabulated Data
Back to [Index](../Index.md) · Section 5.1 (textbook)

Given data $\{(x_i, f_i)\}_{i=0}^{N}$ from an unknown smooth $f$, approximate $f_i' \approx f'(x_i)$. You cannot pick $h$; the mesh is fixed.

## Equal spacing
At interior points use the central difference $f_i' \approx \dfrac{f_{i+1} - f_{i-1}}{2h}$, which is $O(h^2)$. At the endpoints use one-sided differences.

## Unequal spacing: differentiate a local quadratic
Interpolate $p_2(x) = A(x - x_i)^2 + B(x - x_i) + C$ through $x_{i-1}, x_i, x_{i+1}$ and take $f_i' \approx p_2'(x_i) = B$. With $h_i = x_i - x_{i-1}$ and $h_{i+1} = x_{i+1} - x_i$:
$$
\boxed{\,B = \frac{h_i^2(f_{i+1} - f_i) + h_{i+1}^2(f_i - f_{i-1})}{h_ih_{i+1}(h_i + h_{i+1})}\,}
$$
When $h_i = h_{i+1}$ this is the central difference.

## The chord is not enough
The plain chord $\dfrac{f_{i+1} - f_{i-1}}{x_{i+1} - x_{i-1}}$ is second order only at the **midpoint** of $[x_{i-1}, x_{i+1}]$. At $x_i$ its leading error is
$$
f'(x_i) - \frac{f_{i+1} - f_{i-1}}{x_{i+1} - x_{i-1}} \approx -\frac{h_{i+1} - h_i}{2}f''(x_i)
$$
which is only first order on an uneven mesh.

## In Python
```python
fp = np.gradient(f, x)                  # central inside, one-sided at the ends
fp = np.gradient(f, x, edge_order=2)    # second-order one-sided ends
```
With an array `x`, `np.gradient` uses the unequal-spacing quadratic formula.

## Explorations
- [EX38 - Three-Point Derivative on an Unequal Mesh](../Explorations%202/EX38%20-%20Three-Point%20Derivative%20on%20an%20Unequal%20Mesh.md)
- [EX39 - np.gradient Versus a Cubic Spline Derivative of sin x](../Explorations%202/EX39%20-%20np.gradient%20Versus%20a%20Cubic%20Spline%20Derivative%20of%20sin%20x.md)

See also: [Differentiating a Cubic Spline](Differentiating%20a%20Cubic%20Spline.md), [Finite Difference Formulas](Finite%20Difference%20Formulas.md), [Lagrange Form](Lagrange%20Form.md)
