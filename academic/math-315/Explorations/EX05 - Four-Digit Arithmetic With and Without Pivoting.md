---
tags: [math-315, exploration, lecture-3, floating-point]
source: Lecture 3 handout, pp. 7–8 (Section 3.2.5 Example)
topics: ["[[Partial Pivoting]]", "[[Gaussian Elimination]]"]
---
# EX05 — Four-Digit Arithmetic With and Without Pivoting
Back to [[academic/math-315/Index|Index]]

> [!question] Problem
> Solve
> $$
> \begin{aligned}
> 0.003x_1 + 59.14x_2 &= 59.17 \\
> 5.291x_1 - 6.130x_2 &= 46.78
> \end{aligned}
> $$
> using 4-digit arithmetic with rounding. The exact solution is $x_1 = 10$, $x_2 = 1$. Report the relative error. Then repeat with partial pivoting.

## Setup
- **Matrix:** $A = \begin{bmatrix} 0.003 & 59.14 \\ 5.291 & -6.130 \end{bmatrix}$, $\mathbf{b} = \begin{bmatrix} 59.17 \\ 46.78 \end{bmatrix}$
- **Arithmetic:** $\operatorname{fl}_4(\cdot)$ rounds **every** intermediate result to 4 significant digits
- **Issue:** the pivot $a_{11} = 0.003$ is tiny compared with $a_{21} = 5.291$

## Strategy
1. Eliminate without pivoting, rounding after every operation.
2. Back substitute and measure the error.
3. Explain the failure with error propagation.
4. Swap the rows (partial pivoting) and redo the calculation.

## Solution
### Without pivoting
**Multiplier:**
$$
m_{21} = \operatorname{fl}_4\!\left(\frac{5.291}{0.003}\right) = \operatorname{fl}_4(1763.666\ldots) = 1764
$$

**Update $a_{22}$:**
$$
\begin{align*}
\operatorname{fl}_4(1764 \times 59.14) &= \operatorname{fl}_4(104322.96) = 104300 \\
a_{22}^{(2)} &= \operatorname{fl}_4(-6.130 - 104300) = \operatorname{fl}_4(-104306.13) = -1.043 \times 10^5
\end{align*}
$$
The original $-6.130$ disappeared completely in the rounding. It is **swamped**.

**Update $b_2$:**
$$
\begin{align*}
\operatorname{fl}_4(1764 \times 59.17) &= \operatorname{fl}_4(104375.88) = 104400 \\
b_2^{(2)} &= \operatorname{fl}_4(46.78 - 104400) = \operatorname{fl}_4(-104353.22) = -1.044 \times 10^5
\end{align*}
$$
The reduced system is
$$
\left[\begin{array}{cc|c} 0.003 & 59.14 & 59.17 \\ 0 & -1.043 \times 10^5 & -1.044 \times 10^5 \end{array}\right]
$$

**Back substitution:**
$$
x_2 = \operatorname{fl}_4\!\left(\frac{-1.044 \times 10^5}{-1.043 \times 10^5}\right) = \operatorname{fl}_4(1.000958\ldots) = 1.001
$$
$$
\begin{align*}
\operatorname{fl}_4(59.14 \times 1.001) &= \operatorname{fl}_4(59.19914) = 59.20 \\
\operatorname{fl}_4(59.17 - 59.20) &= -0.03000 \\
x_1 &= \operatorname{fl}_4\!\left(\frac{-0.03000}{0.003}\right) = -10.00
\end{align*}
$$
(The handout keeps $59.19914$ unrounded and gets $-9.711 \to -10$. The conclusion is the same.)

**Relative errors:**
$$
E_{\text{rel}}(x_2) = \frac{|1.001 - 1|}{1} = 0.001, \qquad
E_{\text{rel}}(x_1) = \frac{|-10 - 10|}{|10|} = \boxed{\,2\,} = 200\%
$$

### Why it failed: error amplification
From the first equation,
$$
x_1 = \frac{59.17 - 59.14\,x_2}{0.003}
$$
A small error $\delta x_2$ in $x_2$ becomes
$$
\delta x_1 = -\frac{59.14}{0.003}\,\delta x_2 \approx -19713\,\delta x_2
$$
With $\delta x_2 = 0.001$ this gives $\delta x_1 \approx -19.7$, so $x_1 \approx 10 - 19.7 = -9.7$. That is exactly what the handout computed. The **large multiplier** $m_{21} = 1764$ also wiped out $a_{22} = -6.130$ and the digits of $b_2$. Both effects come from dividing by the tiny pivot.

In general, the update $a_{ik}^{(j+1)} = a_{ik}^{(j)} - m_{ij}a_{jk}^{(j)}$ multiplies the rounding error $\epsilon$ in $a_{jk}^{(j)}$ by $|m_{ij}|$:
$$
\operatorname{error}\big(a_{ik}^{(j+1)}\big) \approx |m_{ij}|\,\epsilon
$$

### With partial pivoting
Column 1 has $|0.003| < |5.291|$, so **swap $R_1 \leftrightarrow R_2$**:
$$
\left[\begin{array}{cc|c} 5.291 & -6.130 & 46.78 \\ 0.003 & 59.14 & 59.17 \end{array}\right]
$$

**Multiplier**, now with $|m| \le 1$:
$$
m_{21} = \operatorname{fl}_4\!\left(\frac{0.003}{5.291}\right) = \operatorname{fl}_4(0.000566995\ldots) = 5.670 \times 10^{-4}
$$

**Update $a_{22}$:**
$$
\begin{align*}
\operatorname{fl}_4\big(5.670 \times 10^{-4} \times (-6.130)\big) &= \operatorname{fl}_4(-0.00347571) = -0.003476 \\
a_{22}^{(2)} &= \operatorname{fl}_4(59.14 + 0.003476) = \operatorname{fl}_4(59.143476) = 59.14
\end{align*}
$$

**Update $b_2$:**
$$
\begin{align*}
\operatorname{fl}_4\big(5.670 \times 10^{-4} \times 46.78\big) &= \operatorname{fl}_4(0.02652426) = 0.02652 \\
b_2^{(2)} &= \operatorname{fl}_4(59.17 - 0.02652) = \operatorname{fl}_4(59.14348) = 59.14
\end{align*}
$$

**Back substitution:**
$$
\begin{align*}
x_2 &= \operatorname{fl}_4\!\left(\frac{59.14}{59.14}\right) = 1.000 \\
x_1 &= \operatorname{fl}_4\!\left(\frac{46.78 - (-6.130)(1.000)}{5.291}\right) = \operatorname{fl}_4\!\left(\frac{52.91}{5.291}\right) = 10.00
\end{align*}
$$
$$
\boxed{\,x_1 = 10.00,\quad x_2 = 1.000\,}, \qquad E_{\text{rel}} = 0
$$

Now the back-substitution amplification factor is $6.130/5.291 \approx 1.16$ instead of $19713$.

## Comparison
| | Without pivoting | With pivoting |
|---|---|---|
| $\lvert m_{21}\rvert$ | 1764 | $5.67 \times 10^{-4}$ |
| $a_{22}^{(2)}$ | $-1.043 \times 10^5$ (swamped) | $59.14$ |
| $x_2$ | $1.001$ | $1.000$ |
| $x_1$ | $-10.00$ | $10.00$ |
| $E_{\text{rel}}(x_1)$ | $200\%$ | $0\%$ |

## Takeaways
- The matrix is fine: $\det A \approx -312.9$, far from zero. The **algorithm** was unstable.
- Partial pivoting keeps $|m_{ij}| \le 1$, so errors are not amplified during elimination.
- The extra cost is one comparison per candidate row, which is negligible.

## Related topics
- [[Partial Pivoting]]
- [[Gaussian Elimination]]
- [[Forward and Backward Error]]
