---
tags: [math-315, topic, lecture-4]
---
# Interpolation Error
Back to [Index](../Index.md) · Section 4.2

## Error formula
$$
f(x) - p_N(x) = \frac{\omega_{N+1}(x)}{(N+1)!}\,f^{(N+1)}(\xi_x), \qquad
\omega_{N+1}(x) = (x - x_0)(x - x_1)\cdots(x - x_N)
$$
The point $\xi_x \in [a, b]$ is unknown. It depends on $f$, on $x$, and on the nodes. The error is zero in two cases:
- **At a node** $x = x_i$: $\omega_{N+1}(x_i) = 0$, which is the interpolating condition $p_N(x_i) = f(x_i)$.
- **Everywhere, if $f$ is a polynomial of degree $\le N$**: $f$ already fits the data, and the interpolating polynomial of degree $\le N$ is unique, so $p_N = f$. Also $f^{(N+1)} \equiv 0$.

## Bound
$$
\max_{[a,b]}|f - p_N| \le \max_{[a,b]}|\omega_{N+1}|\cdot\frac{\max_{[a,b]}|f^{(N+1)}|}{(N+1)!}
$$

## Reducing the error
- Choose nodes that keep $|\omega_{N+1}|$ small on all of $[a, b]$.
- **Equally spaced** nodes can give large errors near the endpoints.
- **Chebyshev points** greatly reduce $\max|\omega_{N+1}|$.
- **Avoid extrapolation**, because $\omega_{N+1}$ grows quickly outside $[a, b]$.

## Runge's function
For $f(x) = 1/(1+x^2)$ on $[-5, 5]$, adding equally spaced nodes makes the endpoint oscillations **worse**. Chebyshev nodes make the error shrink.

## Toward splines
Since $|x - x_i| \le b - a$,
$$
\max|f - p_N| \le |b - a|^{N+1}\,\frac{\max|f^{(N+1)}|}{(N+1)!}
$$
Fixing $N$ and shrinking the interval drives the error to $0$. This motivates [Linear Splines](Linear%20Splines.md).

## Explorations
- [EX29 - Runge Function with Equispaced and Chebyshev Nodes](../Explorations%202/EX29%20-%20Runge%20Function%20with%20Equispaced%20and%20Chebyshev%20Nodes.md)
- [EX24 - Interpolating sin(x) at Three Collinear Points](../Explorations%202/EX24%20-%20Interpolating%20sin%28x%29%20at%20Three%20Collinear%20Points.md)

See also: [Chebyshev Polynomials](Chebyshev%20Polynomials.md), [Polynomial Interpolation](Polynomial%20Interpolation.md)
