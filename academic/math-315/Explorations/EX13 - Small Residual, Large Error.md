---
tags: [math-315, exploration, lecture-3]
source: Lecture 3 handout, pp. 21–22 (Section 3.4.1 Condition Number, Parts 2–4)
topics: ["[[Forward and Backward Error]]", "[[Condition Number]]", "[[Vector Norms]]"]
---
# EX13 — Small Residual, Large Error
Back to [[academic/math-315/Index|Index]]

> [!question] Problem
> For
> $$
> A = \begin{bmatrix} 0.913 & 0.659 \\ 0.457 & 0.330 \end{bmatrix}, \qquad \mathbf{b} = \begin{bmatrix} 0.254 \\ 0.127 \end{bmatrix}
> $$
> compare two approximations, $\hat{\mathbf{x}}_1 = (-0.0827,\ 0.5)^{\top}$ and $\hat{\mathbf{x}}_2 = (0.999,\ -1.001)^{\top}$.
> (a) Compute both residuals and both forward errors in the 1-norm.
> (b) Explain the paradox using $\kappa_1(A)$ and the bound $\dfrac{\|\mathbf{x} - \hat{\mathbf{x}}\|}{\|\mathbf{x}\|} \le \kappa(A)\dfrac{\|\mathbf{b} - A\hat{\mathbf{x}}\|}{\|\mathbf{b}\|}$.

## Setup
- **Exact solution:** $\mathbf{x} = (1, -1)^{\top}$. Check: $0.913 - 0.659 = 0.254$ and $0.457 - 0.330 = 0.127$. $\checkmark$
- **Residual** (handout convention): $\hat{\mathbf{r}} = A\hat{\mathbf{x}} - \mathbf{b}$, which is computable
- **Forward error:** $\|\mathbf{x} - \hat{\mathbf{x}}\|_1 / \|\mathbf{x}\|_1$, which needs the unknown $\mathbf{x}$

## Strategy
1. Compute $A\hat{\mathbf{x}}_k - \mathbf{b}$ and its 1-norm.
2. Compute the true relative errors.
3. Find $A^{-1}$ and $\kappa_1(A)$.
4. Show that $\mathbf{e} = -A^{-1}\hat{\mathbf{r}}$ explains how a tiny $\hat{\mathbf{r}}$ turns into a large $\mathbf{e}$.

## Solution
**(a) Residuals**

*For $\hat{\mathbf{x}}_1$:*
$$
\begin{align*}
0.913(-0.0827) + 0.659(0.5) &= -0.0755051 + 0.3295 = 0.2539949 \\
0.457(-0.0827) + 0.330(0.5) &= -0.0377939 + 0.165 = 0.1272061 \\
\hat{\mathbf{r}}_1 &= \begin{bmatrix} 0.2539949 - 0.254 \\ 0.1272061 - 0.127 \end{bmatrix} = \begin{bmatrix} -0.0000051 \\ 0.0002061 \end{bmatrix}, \qquad \|\hat{\mathbf{r}}_1\|_1 = 2.112 \times 10^{-4}
\end{align*}
$$

*For $\hat{\mathbf{x}}_2$:*
$$
\begin{align*}
0.913(0.999) + 0.659(-1.001) &= 0.912087 - 0.659659 = 0.252428 \\
0.457(0.999) + 0.330(-1.001) &= 0.456543 - 0.33033 = 0.126213 \\
\hat{\mathbf{r}}_2 &= \begin{bmatrix} -0.001572 \\ -0.000787 \end{bmatrix}, \qquad \|\hat{\mathbf{r}}_2\|_1 = 2.359 \times 10^{-3}
\end{align*}
$$
Judging by residuals, $\hat{\mathbf{x}}_1$ looks **ten times better**.

**Forward errors** ($\|\mathbf{x}\|_1 = 2$):
$$
\begin{align*}
\mathbf{x} - \hat{\mathbf{x}}_1 &= (1.0827,\ -1.5) &&\implies \frac{2.5827}{2} = \boxed{\,1.291\,} \quad (129\%) \\
\mathbf{x} - \hat{\mathbf{x}}_2 &= (0.001,\ 0.001) &&\implies \frac{0.002}{2} = \boxed{\,0.001\,} \quad (0.1\%)
\end{align*}
$$
In fact $\hat{\mathbf{x}}_2$ is **1000 times better**. The residual pointed the wrong way.

**(b) The explanation**

*Near-singularity.* The columns are almost parallel:
$$
\frac{0.913}{0.457} \approx 1.998, \qquad \frac{0.659}{0.330} \approx 1.997
$$
$$
\det A = 0.913(0.330) - 0.659(0.457) = 0.30129 - 0.301163 = 0.000127
$$

*Inverse.*
$$
A^{-1} = \frac{1}{0.000127}\begin{bmatrix} 0.330 & -0.659 \\ -0.457 & 0.913 \end{bmatrix}
\approx \begin{bmatrix} 2598.4 & -5189.0 \\ -3598.4 & 7189.0 \end{bmatrix}
$$

*Condition number (1-norm).*
$$
\begin{align*}
\|A\|_1 &= \max(0.913 + 0.457,\ 0.659 + 0.330) = 1.370 \\
\|A^{-1}\|_1 &= \max(2598.4 + 3598.4,\ 5189.0 + 7189.0) = 12378.0 \\
\kappa_1(A) &= 1.370 \times 12378.0 \approx \boxed{\,1.70 \times 10^4\,}
\end{align*}
$$

*How the error comes from the residual.* Since $A\mathbf{x} = \mathbf{b}$,
$$
\mathbf{x} - \hat{\mathbf{x}} = A^{-1}(\mathbf{b} - A\hat{\mathbf{x}}) = -A^{-1}\hat{\mathbf{r}}
$$
Check for $\hat{\mathbf{x}}_1$:
$$
A^{-1}\hat{\mathbf{r}}_1 \approx \begin{bmatrix} 2598.4(-0.0000051) - 5189.0(0.0002061) \\ -3598.4(-0.0000051) + 7189.0(0.0002061) \end{bmatrix}
= \begin{bmatrix} -0.0133 - 1.0694 \\ 0.0184 + 1.4816 \end{bmatrix}
= \begin{bmatrix} -1.0827 \\ 1.5 \end{bmatrix}
$$
The negative of this is $\mathbf{x} - \hat{\mathbf{x}}_1$. $\checkmark$ A residual of about $2 \times 10^{-4}$ was magnified about $5000$-fold. That is possible because $\|A^{-1}\|_1 \approx 12378$.

*Proof of the bound.*
$$
\begin{align*}
\|\mathbf{x} - \hat{\mathbf{x}}\| &= \|A^{-1}\hat{\mathbf{r}}\| \le \|A^{-1}\|\,\|\hat{\mathbf{r}}\| \\
\|\mathbf{b}\| &= \|A\mathbf{x}\| \le \|A\|\,\|\mathbf{x}\| \implies \frac{1}{\|\mathbf{x}\|} \le \frac{\|A\|}{\|\mathbf{b}\|} \\
\frac{\|\mathbf{x} - \hat{\mathbf{x}}\|}{\|\mathbf{x}\|} &\le \|A\|\,\|A^{-1}\|\,\frac{\|\hat{\mathbf{r}}\|}{\|\mathbf{b}\|} = \kappa(A)\frac{\|\hat{\mathbf{r}}\|}{\|\mathbf{b}\|}
\end{align*}
$$

*Evaluate the bound* with $\|\mathbf{b}\|_1 = 0.381$:
| | Relative residual | $\kappa_1 \times$ rel. residual | Actual rel. error |
|---|---|---|---|
| $\hat{\mathbf{x}}_1$ | $5.54 \times 10^{-4}$ | $9.40$ | $1.291$ |
| $\hat{\mathbf{x}}_2$ | $6.19 \times 10^{-3}$ | $105$ | $0.001$ |

Both bounds hold. They are also very loose: with $\kappa \approx 1.7 \times 10^4$, a relative residual of $10^{-3}$ is compatible with anything from a perfect answer to a completely wrong one.

## Result
- $\hat{\mathbf{x}}_1$: small residual ($2.1 \times 10^{-4}$), large error ($129\%$).
- $\hat{\mathbf{x}}_2$: larger residual ($2.4 \times 10^{-3}$), tiny error ($0.1\%$).
- The reason is $\kappa_1(A) \approx 1.7 \times 10^4$: $A$ is ill-conditioned, so the residual is **not** a reliable proxy for the error.

## Takeaways
- relative error $\le \kappa \times$ relative residual. Only when $\kappa$ is small does a small residual mean a small error.
- $\det A = 1.27 \times 10^{-4}$ happens to be small here, but see [[EX14 - Determinant Versus Condition Number|EX14]]. The determinant is not the right measure in general.

## Related topics
- [[Forward and Backward Error]]
- [[Condition Number]]
- [[Vector Norms]]
