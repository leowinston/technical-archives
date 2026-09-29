---
tags: [math-212, problem, workbook-1]
source: Workbook Part 1, Problem 1 (p. 2)
topics: ["[[Mathematical Models]]", "[[Linear First-Order Equations]]", "[[Modeling with First-Order Equations]]"]
---
# Problem 1 — A Car Slowing Down to a Stop (with Friction)
Back to [[academic/math-212/Index|Index]]

> [!question] Problem
> A car moves at initial velocity $v_0$, then slows to a stop because of friction.
> (a) How is the velocity related to the position?
> (b) How is the acceleration related to the velocity?
> (c) Write a first-order ODE for the velocity and the corresponding second-order ODE for the position.
> (d) Guess the solution of the first-order ODE, that is, find $v(t)$.
> (e) Find the position $x(t)$.

## Classification
- **Velocity equation:** ODE, first order, **linear**, **homogeneous**, constant coefficients
- **Position equation:** ODE, second order, linear, homogeneous, constant coefficients
- **Modeling assumption:** friction is proportional to velocity, $F = -kmv$ with $k > 0$ (viscous friction)

## Strategy
1. Use the kinematic definitions to connect $x$, $v$, and $a$.
2. Newton's second law with the friction assumption gives $a = -kv$.
3. The velocity equation says "the derivative is a constant times the function," so guess an exponential.
4. Integrate $v$ once, using $x(0) = x_0$, to get the position.

## Solution
**(a), (b)** Kinematics:
$$
\begin{align*}
v(t) &= \frac{dx}{dt}, & a(t) &= \frac{dv}{dt} = \frac{d^2x}{dt^2}
\end{align*}
$$

**(c)** Friction proportional to velocity gives
$$
\begin{align*}
\frac{dv}{dt} &= -kv, \quad v(0) = v_0 \\
\frac{d^2x}{dt^2} &= -k\frac{dx}{dt}, \quad x(0) = x_0,\ x'(0) = v_0
\end{align*}
$$

**(d)** We need a function whose derivative is $-k$ times itself:
$$
\begin{align*}
v(t) &= v_0 e^{-kt} \\
\text{check: } v'(t) &= -kv_0e^{-kt} = -kv(t) \checkmark
\end{align*}
$$

**(e)** Integrate the velocity:
$$
\begin{align*}
x(t) &= x_0 + \int_0^t v_0e^{-ks}\,ds \\
&= x_0 + \frac{v_0}{k}\left(1 - e^{-kt}\right)
\end{align*}
$$
As $t \to \infty$, $v \to 0$ and $x \to x_0 + \dfrac{v_0}{k}$. So the total stopping distance is $v_0/k$.

> [!note]
> With constant (Coulomb) friction $a = -\mu g$ instead, $v = v_0 - \mu g t$, and the car stops at the finite time $t = v_0/(\mu g)$.

## Solution set
- **General solution:** $v(t) = Ce^{-kt}$, $C \in \mathbb{R}$, $t \in \mathbb{R}$. The IVP picks $C = v_0$.
- **Position:** $x(t) = C_1 + C_2e^{-kt}$, $C_1, C_2 \in \mathbb{R}$. The IVP picks $C_1 = x_0 + \tfrac{v_0}{k}$, $C_2 = -\tfrac{v_0}{k}$.
- **Constant solutions:** $v \equiv 0$ (the car at rest), included at $C = 0$. For position, $x \equiv C_1$ (the $C_2 = 0$ case).
- **Note:** $C$ comes straight from the guess $v = Ce^{-kt}$, not from exponentiating, so $C = 0$ needs no special justification.

## Graph
Velocity (blue) and position (red), with $v_0 = 3$, $x_0 = 0$, and $k \in \{0.5, 1\}$. The dashed line is the stopping distance $v_0/k$ for $k = 0.5$.
```desmos-graph
left=-0.5; right=8; top=7; bottom=-0.5
xAxisLabel=t
---
y=v_0e^{-kx}|x>=0|#2d70b3
y=\frac{v_0}{k}\left(1-e^{-kx}\right)|x>=0|#c74440
v_0=3
k=[0.5,1]
y=6|dashed|#c74440
```

## Related topics
- [[Mathematical Models]]
- [[Linear First-Order Equations]]
- [[Systems of Differential Equations]] (the second-order equation as the system $x' = v$, $v' = -kv$)
