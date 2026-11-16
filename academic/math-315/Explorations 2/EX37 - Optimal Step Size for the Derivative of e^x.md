---
tags:
  - math-315
  - exploration
  - chapter-5
source: Textbook Section 5.1, Problem 5.1.3
topics:
  - "[[../Topics 2/Step Size and Roundoff in Numerical Differentiation]]"
  - "[[../Topics 2/Finite Difference Formulas]]"
---
# EX37 — Optimal Step Size for the Derivative of e^x
Back to [Index](../Index.md)

> [!question] Problem
> Approximate $f'(1)$ for $f(x) = e^x$ with forward and central differences, $h = 10^{-n}$.
> (a) Derive the step size that minimizes truncation plus roundoff error for each formula.
> (b) Predict the smallest achievable error.
> (c) Compare with the computed errors. When does roundoff begin to dominate?

## Setup
- $f = f' = f'' = f''' = e^x$, so at $x = 1$ every derivative is $e \approx 2.718$
- Each computed value $\hat f = f(1 + \delta)$ with $|\delta| \le u = \varepsilon/2 \approx 1.1\times10^{-16}$

## Strategy
1. Bound the roundoff in the numerator, then divide by the denominator.
2. Add the truncation term and minimize over $h$.

## Solution
**(a) Optimal $h$**

*Forward.* The numerator $\hat f(1+h) - \hat f(1)$ carries an error up to $2u\,e = \varepsilon e$, and dividing by $h$ gives $\varepsilon e/h$:
$$
E_{\text{fwd}}(h) = \frac h2e + \frac{\varepsilon e}{h}, \qquad
E_{\text{fwd}}'(h) = \frac e2 - \frac{\varepsilon e}{h^2} = 0
\implies h^* = \sqrt{2\varepsilon} \approx 2.1\times10^{-8}
$$
*Central.* The denominator is $2h$, so the roundoff term is $\varepsilon e/(2h)$:
$$
E_{\text{cen}}(h) = \frac{h^2}{6}e + \frac{\varepsilon e}{2h}, \qquad
\frac{h}{3}e - \frac{\varepsilon e}{2h^2} = 0
\implies h^* = \Big(\frac{3\varepsilon}{2}\Big)^{1/3} \approx 6.9\times10^{-6}
$$
For $e^x$ the factors of $e$ cancel, so $h^*$ depends only on $\varepsilon$.

**(b) Best possible error**
$$
\begin{align*}
E_{\text{fwd}}(h^*) &= e\Big(\tfrac{2.1\times10^{-8}}{2} + \tfrac{2.2\times10^{-16}}{2.1\times10^{-8}}\Big) \approx e\,(2.1\times10^{-8}) \approx 5.7\times10^{-8} \\
E_{\text{cen}}(h^*) &= e\Big(\tfrac{(6.9\times10^{-6})^2}{6} + \tfrac{2.2\times10^{-16}}{2(6.9\times10^{-6})}\Big) \approx e\,(2.4\times10^{-11}) \approx 6.5\times10^{-11}
\end{align*}
$$

**(c) Computed errors**

| $n$ | Forward error | Central error |
|---|---|---|
| 1 | $1.4\times10^{-1}$ | $4.5\times10^{-3}$ |
| 2 | $1.4\times10^{-2}$ | $4.5\times10^{-5}$ |
| 3 | $1.4\times10^{-3}$ | $4.5\times10^{-7}$ |
| 4 | $1.4\times10^{-4}$ | $4.5\times10^{-9}$ |
| 5 | $1.4\times10^{-5}$ | $\mathbf{5.9\times10^{-11}}$ |
| 6 | $1.4\times10^{-6}$ | $1.6\times10^{-10}$ |
| 7 | $1.4\times10^{-7}$ | $5.9\times10^{-11}$ |
| 8 | $\mathbf{6.6\times10^{-9}}$ | $6.6\times10^{-9}$ |
| 10 | $1.5\times10^{-6}$ | $6.7\times10^{-7}$ |
| 12 | $4.3\times10^{-4}$ | $2.1\times10^{-4}$ |
| 16 | $2.7$ | $2.7$ |

- The central minimum, $5.9\times10^{-11}$ at $h = 10^{-5}$, matches the prediction.
- The forward minimum falls at $h = 10^{-8}$, as predicted. Its value is smaller than the bound because the two rounding errors partly cancelled. The bound is a worst case.
- Roundoff takes over after $n = 8$ for forward and after $n = 5$ for central.
- At $n = 16$, $1 \pm h$ rounds to $1$ and both formulas return $0$, so the error is $e$.

## Result
$$
\boxed{\,h^*_{\text{fwd}} = \sqrt{2\varepsilon} \approx 2\times10^{-8}, \qquad h^*_{\text{cen}} = (3\varepsilon/2)^{1/3} \approx 7\times10^{-6}\,}
$$

## Takeaways
- Balance the two error terms: the $h$ that makes them about equal is close to optimal.
- A higher-order formula wants a **larger** step and reaches a **smaller** error.
- Error bounds for rounding are worst cases. Single runs can do better, but not reliably.

## Related topics
- [Step Size and Roundoff in Numerical Differentiation](../Topics%202/Step%20Size%20and%20Roundoff%20in%20Numerical%20Differentiation.md)
- [Finite Difference Formulas](../Topics%202/Finite%20Difference%20Formulas.md)
- [Rounding and Machine Precision](../Topics%201/Rounding%20and%20Machine%20Precision.md)
