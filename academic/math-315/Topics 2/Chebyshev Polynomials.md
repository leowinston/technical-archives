---
tags: [math-315, topic, lecture-4]
---
# Chebyshev Polynomials
Back to [Index](../Index.md) · Section 4.1.4

## Definition
$$
T_j(x) = \cos\big(j\arccos x\big), \qquad -1 \le x \le 1
$$
A **Chebyshev series** of order $N$ is $b_0T_0(x) + b_1T_1(x) + \cdots + b_NT_N(x)$.

## First terms
$T_0 = 1$ and $T_1 = x$. Then $\cos 2\theta = 2\cos^2\theta - 1$ gives $T_2 = 2x^2 - 1$.

## Recurrence
$$
\boxed{\,T_{j+1}(x) = 2x\,T_j(x) - T_{j-1}(x)\,}
$$

## Zeros (Chebyshev points)
$$
x_i = \cos\!\left(\frac{2i - 1}{2j}\,\pi\right), \qquad i = 1, \dots, j
$$
Mapped to $[a, b]$ for $N + 1$ interpolation nodes:
$$
x_i = \frac{b + a}{2} - \frac{b - a}{2}\cos\!\left(\frac{2i + 1}{2N + 2}\,\pi\right), \qquad i = 0, \dots, N
$$
These nodes cluster near the endpoints, which is what makes $\max|\omega_{N+1}|$ small.

![L4-chebyshev-polynomials.png](../Assets/L4-chebyshev-polynomials.png)

## Explorations
- [EX28 - Chebyshev Polynomials T2 to T5 and Their Zeros](../Explorations%202/EX28%20-%20Chebyshev%20Polynomials%20T2%20to%20T5%20and%20Their%20Zeros.md)
- [EX29 - Runge Function with Equispaced and Chebyshev Nodes](../Explorations%202/EX29%20-%20Runge%20Function%20with%20Equispaced%20and%20Chebyshev%20Nodes.md)

See also: [Interpolation Error](Interpolation%20Error.md)
