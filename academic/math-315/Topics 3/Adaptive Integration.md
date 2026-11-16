---
tags: [math-315, topic, chapter-5]
---
# Adaptive Integration
Back to [Index](../Index.md) · Section 5.2.3 (textbook)

Equal subintervals small enough for the worst part of $f$ waste evaluations where $f$ is smooth. Adaptive codes put short subintervals only where they are needed.

## Error estimate
Use two rules on each subinterval $T^*$, with $R_2$ more accurate than $R_1$:
$$
E(f, T^*) = |I - R_1| \approx |R_2 - R_1|
$$
$R_2$ is either a rule with higher DOP, or $R_1$ applied on both halves. If $R_1$ has DOP $p$, the halves together reduce the error by about $2\big(\tfrac12\big)^{p+2}$, so $\tfrac1{16}$ for Simpson.

## Global adaptive algorithm
```text
R := R1(f, [a,b]);  E := |R2 - R1|
while E > tol
    pick the subinterval T(i) with the largest error estimate
    bisect it into two halves
    compute R and E on each half
    R := R + (R_left + R_right - R_old)
    E := E + (E_left + E_right - E_old)
end
```
Updating by a small correction, rather than subtracting and re-adding whole sums, avoids [cancellation](../Topics%201/Cancellation%20Error.md).

## Notes
- The **estimate** ends up below `tol`, but the true error is not guaranteed to.
- `tol` must exceed about $\varepsilon$ times the size of the integral, or it can never be met.
- Each bisection usually lowers $E$, so the loop normally terminates for smooth $f$.

## In Python
`scipy.integrate.quad(f, a, b)` is a global adaptive code built on Gauss-Kronrod pairs. It returns `(value, error_estimate)`.

## Explorations
- [EX43 - Simpson's Rule on a Short Interval and the Composite Error](../Explorations%203/EX43%20-%20Simpson%27s%20Rule%20on%20a%20Short%20Interval%20and%20the%20Composite%20Error.md)

See also: [Gauss Rules](Gauss%20Rules.md), [Lobatto Rules](Lobatto%20Rules.md), [Transformation from a Canonical Interval](Transformation%20from%20a%20Canonical%20Interval.md)
