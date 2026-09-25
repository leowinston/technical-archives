---
tags: [math-212, topic, chapter-2]
---
# Bernoulli Equations
Back to [[Index]] · Chapter 2.4

$$
\frac{dy}{dt} + p(t)y = q(t)y^n \qquad (n \neq 0, 1)
$$
This is nonlinear, but the substitution $v = y^{1-n}$ makes it linear:
$$
\begin{align*}
\frac{dv}{dt} &= (1 - n)y^{-n}\frac{dy}{dt} \\
\frac{dv}{dt} + (1 - n)p(t)v &= (1 - n)q(t)
\end{align*}
$$
Solve for $v$ with an [[Linear First-Order Equations|integrating factor]], then recover $y = v^{1/(1-n)}$.

The logistic equation is a Bernoulli equation with $n = 2$ (see [[Logistic Growth]]).
