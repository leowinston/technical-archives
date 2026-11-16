---
tags:
  - math-315
  - exploration
  - chapter-5
source: Textbook Section 5.2.4, Problems 5.2.26, 5.2.27 and 5.2.30
topics:
  - "[[../Topics 3/Gauss Rules]]"
  - "[[../Topics 3/Peano's Theorem]]"
---
# EX45 — Two- and Three-Point Gauss Rules
Back to [Index](../Index.md)

> [!question] Problem
> On $[-1, 1]$, choose points and weights to maximize the DOP.
> (a) Show that the 1-point Gauss rule is the midpoint rule.
> (b) Find the 2-point rule $w_0[f(x_0) + f(-x_0)]$, its DOP, and its Peano constant.
> (c) Find the 3-point rule $w_0[f(x_0) + f(-x_0)] + w_1f(0)$, its DOP, and its Peano constant.
> (d) Show that the Gauss-Kronrod extension of the 1-point rule is the 3-point Gauss rule.

## Setup
- Even moments $I(x^{2k}) = \tfrac{2}{2k+1}$. Odd moments vanish, and so does every odd $R(x^m)$ by symmetry.
- The equations are nonlinear in the points, but symmetry keeps them small.

## Strategy
1. Use only the even equations $m = 0, 2, 4, \dots$, one per unknown.
2. Check the next even power for the DOP and $\kappa$.

## Solution
**(a) One point**

$w_0f(x_0)$: $m = 0$ gives $w_0 = 2$, and $m = 1$ gives $2x_0 = 0$. So $R = 2f(0)$, the midpoint rule, with DOP $1$.

**(b) Two points**
$$
\begin{align*}
m = 0: &\quad 2w_0 = 2 \implies w_0 = 1 \\
m = 2: &\quad 2x_0^2 = \tfrac23 \implies x_0 = \tfrac{1}{\sqrt3}
\end{align*}
$$
$m = 4$: $R = \tfrac29 \ne \tfrac25$, so $\text{DOP} = 3$ and
$$
\kappa = \frac{\tfrac25 - \tfrac29}{4!} = \frac{8/45}{24} = \boxed{\,\frac1{135}\,}
$$

**(c) Three points**
$$
\begin{align*}
m = 0: &\quad 2w_0 + w_1 = 2 \\
m = 2: &\quad 2w_0x_0^2 = \tfrac23 \\
m = 4: &\quad 2w_0x_0^4 = \tfrac25
\end{align*}
$$
Dividing the third by the second gives $x_0^2 = \tfrac35$. Then $w_0 = \tfrac{1/3}{3/5} = \tfrac59$ and $w_1 = 2 - \tfrac{10}9 = \tfrac89$:
$$
\boxed{\,\int_{-1}^1f \approx \tfrac59f\big(-\sqrt{3/5}\big) + \tfrac89f(0) + \tfrac59f\big(\sqrt{3/5}\big)\,}
$$
$m = 6$: $R = 2\cdot\tfrac59\cdot\tfrac{27}{125} = \tfrac{6}{25} \ne \tfrac27$, so $\text{DOP} = 5$ and
$$
\kappa = \frac{\tfrac27 - \tfrac6{25}}{6!} = \frac{8/175}{720} = \frac{1}{15750}
$$

**(d) Kronrod extension of the midpoint rule**

Keep the point $0$, add $N + 2 = 2$ new points, symmetric $\pm y$, and choose the weight at $0$, the weight at $\pm y$, and $y$. These are the three unknowns of (c) with the same equations, so the answer is the 3-point Gauss rule, with DOP $5$. That beats the textbook's general guarantee of $3N + 2 = 2$ for $N = 0$, which is only a lower bound.

```python
np.polynomial.legendre.leggauss(3)
# (array([-0.7746, 0., 0.7746]), array([0.5556, 0.8889, 0.5556]))
```

## Result
| Points | Nodes | Weights | DOP | $\kappa$ |
|---|---|---|---|---|
| 1 | $0$ | $2$ | 1 | $\tfrac13$ |
| 2 | $\pm0.5774$ | $1$ | 3 | $\tfrac1{135}$ |
| 3 | $0, \pm0.7746$ | $\tfrac89, \tfrac59$ | 5 | $\tfrac1{15750}$ |

## Takeaways
- $n$ Gauss points buy DOP $2n - 1$.
- Gauss 2-point matches Simpson's DOP with one fewer evaluation and a smaller constant ($\tfrac1{135}$ against $\tfrac1{90}$).
- The weights are positive and sum to $2$, and the points interlace: $\pm0.577$ sits between $0$ and $\pm0.775$.

## Related topics
- [Gauss Rules](../Topics%203/Gauss%20Rules.md)
- [Peano's Theorem](../Topics%203/Peano%27s%20Theorem.md)
- [Degree of Precision](../Topics%203/Degree%20of%20Precision.md)
