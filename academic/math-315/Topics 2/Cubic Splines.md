---
tags: [math-315, topic, lecture-4]
---
# Cubic Splines
Back to [Index](../Index.md) · Section 4.3.2

## Spline of degree $m$
A spline of degree $m$ on $[a, b]$ is a polynomial of degree $\le m$ on each $[x_{i-1}, x_i]$, with $S, S', \dots, S^{(m-1)}$ continuous. **Knots** are where the pieces switch. **Nodes** are where the spline interpolates. The two need not coincide.

## Cubic spline $S_{3,N}$
$S_{3,N} = p_i(x)$, a cubic, on $[x_{i-1}, x_i]$, and $S_{3,N}$ is $C^2$.

## Counting conditions
| | Count |
|---|---|
| Unknowns ($4$ per piece) | $4N$ |
| Interpolation, $p_i(x_{i-1}) = f_{i-1}$, $p_i(x_i) = f_i$ | $2N$ |
| $p_i' = p_{i+1}'$, $p_i'' = p_{i+1}''$ at interior knots | $2(N-1)$ |
| **Still needed** | $2$ |

## Boundary conditions
| Name | Conditions | Accuracy |
|---|---|---|
| Natural | $p_1''(x_0) = p_N''(x_N) = 0$ | $O(h^2)$, minimal energy, weaker at the ends |
| Second derivative | $p_1'' = f''$, $p_N'' = f''$ at the ends | $O(h^4)$ |
| First derivative (clamped) | $p_1' = f'$, $p_N' = f'$ at the ends | $O(h^4)$ |
| Not-a-knot | $p_1''' = p_2'''$ at $x_1$, $p_{N-1}''' = p_N'''$ at $x_{N-1}$ | $O(h^4)$ |

## In Python (`scipy.interpolate`)
- `CubicSpline` builds a $C^2$ cubic spline.
- `PchipInterpolator` builds a shape-preserving cubic that is only $C^1$.
- `InterpolatedUnivariateSpline` lets you choose the degree.
- `BSpline` evaluates a B-spline representation.

## Explorations
- [EX32 - Natural Cubic Spline from B-Splines](../Explorations%202/EX32%20-%20Natural%20Cubic%20Spline%20from%20B-Splines.md)
- [EX31 - Deriving the Cubic B-Spline](../Explorations%202/EX31%20-%20Deriving%20the%20Cubic%20B-Spline.md)

See also: [Cubic B-Splines](Cubic%20B-Splines.md), [Linear Splines](Linear%20Splines.md)
