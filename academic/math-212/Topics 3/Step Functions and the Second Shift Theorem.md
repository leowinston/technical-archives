---
tags:
  - math-212
  - topic
  - chapter-6
---
# Step Functions and the Second Shift Theorem
Back to [Index](../Index.md) · Chapter 6.3–6.4 · Beyond the enrichment handout

Forcing that switches on or off is awkward for undetermined coefficients and routine for the [Laplace transform](The%20Laplace%20Transform.md).

## Unit step
$$
u_c(t) = \begin{cases} 0, & t < c \\ 1, & t \ge c \end{cases}
\qquad
\mathcal{L}\{u_c\} = \int_c^\infty e^{-st}\,dt = \frac{e^{-cs}}{s}
$$
A pulse that is on only for $a \le t < b$ is $u_a(t) - u_b(t)$.

## Second shift theorem
$$
\boxed{\mathcal{L}\{u_c(t)\,f(t-c)\} = e^{-cs}F(s)}
$$
Delaying a signal by $c$ multiplies its transform by $e^{-cs}$. Compare the [first shift theorem](Inverse%20Transforms%20and%20Partial%20Fractions.md), where the exponential sits on the $t$ side.

## Example
$y' + 2y = u_1(t)$, $y(0) = 0$: the forcing turns on at $t = 1$.
$$
Y = \frac{e^{-s}}{s(s+2)} \quad\Longrightarrow\quad y(t) = u_1(t)\cdot\tfrac12\left(1 - e^{-2(t-1)}\right)
$$
This is the response to constant forcing from [Solving Initial Value Problems with the Laplace Transform](Solving%20Initial%20Value%20Problems%20with%20the%20Laplace%20Transform.md), started one unit late. Nothing happens before the switch, and $y$ stays continuous at $t = 1$ even though $y'$ jumps.

See also: [Impulses and the Dirac Delta](Impulses%20and%20the%20Dirac%20Delta.md)
