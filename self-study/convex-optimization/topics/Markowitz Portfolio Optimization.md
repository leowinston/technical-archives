---
tags: [convex-optimization, topic, ch-4]
source: Boyd & Vandenberghe §4.4.1 (pp. 155–156)
---
# Markowitz Portfolio Optimization
Back to [Index](../Index.md) · Section 4.4.1

> [!note] ✎ Your most-annotated page (p. 155)
> You wrote **"Algory"** in red next to the heading. You marked $x_i$ as a vector, and $x \in \R^n$ as "how much asset$_1$ … asset$_n$". You labelled $x^{\top}\Sigma x$ as **Cov** $\Sigma$ and $x \succeq 0$ as **"long every stock"**.

## Setup
- $x \in \R^n$: dollars in each asset. $x_i < 0$ is a short position.
- Price changes $p$ are random with mean $\bar p$ and covariance $\Sigma$.
- Return $r = p^{\top}x$ has mean $\bar p^{\top}x$ and variance $x^{\top}\Sigma x$.

## The QP
$$
\boxed{
\begin{array}{ll}
\text{minimize} & x^{\top}\Sigma x \\
\text{subject to} & \bar p^{\top}x \ge r_{\min} \\
& \ones^{\top}x = 1,\ \ x \succeq 0
\end{array}}
$$
Minimize risk (variance) subject to a minimum mean return, the budget, and no shorting.

## Extensions
- **Shorting:** $x = x_{\text{long}} - x_{\text{short}}$ with $\ones^{\top}x_{\text{short}} \le \eta\,\ones^{\top}x_{\text{long}}$.
- **Transaction costs:** $x = x_{\text{init}} + u_{\text{buy}} - u_{\text{sell}}$, $u \succeq 0$, with fees in the budget.

## Explorations
- [EX07 - Markowitz Three-Asset Portfolio](../explorations/EX07%20-%20Markowitz%20Three-Asset%20Portfolio.md)

See also: [Quadratic Programs](Quadratic%20Programs.md), [Positive Semidefinite Matrices](Positive%20Semidefinite%20Matrices.md)
