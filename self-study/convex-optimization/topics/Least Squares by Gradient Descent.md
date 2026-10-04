---
tags: [convex-optimization, topic, ml-notebook]
source: ML notebook "Gradient Descent"; Boyd & Vandenberghe §1.2.1, §9.3
---
# Least Squares by Gradient Descent
Back to [Index](../Index.md) · ML notebook

## Setup
Data $X \in \R^{n \times d}$, targets $y \in \R^n$, weights $w \in \R^d$. Prediction $\hat y = Xw$. Mean squared error:
$$
L(w) = \frac1n\lVert Xw - y\rVert_2^2 = \frac1n\big(w^{\top}X^{\top}Xw - 2y^{\top}Xw + y^{\top}y\big)
$$

## Gradient
Using $\nabla_w(w^{\top}Aw) = 2Aw$ and $\nabla_w(b^{\top}w) = b$:
$$
\boxed{\,\nabla_w L = \frac2n X^{\top}(\underbrace{Xw - y}_{\text{residual}})\,}
$$
$\nabla^2 L = \tfrac2n X^{\top}X \succeq 0$, so $L$ is convex and any stationary point is global.

## Iteration
```
w ← 0
repeat:
    w ← w − t · (2/n) Xᵀ(Xw − y)
until ‖∇L‖ small
```
It converges for a step $t < 2/\lambda_{\max}(\nabla^2 L)$. The limit solves the normal equations $X^{\top}Xw = X^{\top}y$.

## Explorations
- [EX08 - Least Squares by Gradient Descent](../explorations/EX08%20-%20Least%20Squares%20by%20Gradient%20Descent.md)

See also: [Least-Squares and Linear Programming](Least-Squares%20and%20Linear%20Programming.md), [Maximum Likelihood Estimation](Maximum%20Likelihood%20Estimation.md)
