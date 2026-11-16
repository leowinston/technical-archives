---
tags:
  - math-212
  - topic
  - chapter-6
---
# Impulses and the Dirac Delta
Back to [Index](../Index.md) · Chapter 6.5 · Beyond the enrichment handout

A hammer blow: a very large force over a very short time, with total impulse $1$.

## Definition
$\delta(t - c)$ is the limit of pulses of width $2\tau$ and height $\dfrac{1}{2\tau}$ centered at $c$ as $\tau \to 0$. It is defined by what it does inside an integral:
$$
\int_{-\infty}^{\infty}\delta(t-c)\,f(t)\,dt = f(c)
$$

## Transform
$$
\boxed{\mathcal{L}\{\delta(t-c)\} = e^{-cs}}, \qquad \mathcal{L}\{\delta(t)\} = 1
$$
It is the derivative of the [unit step](Step%20Functions%20and%20the%20Second%20Shift%20Theorem.md): $s\cdot\dfrac{e^{-cs}}{s} = e^{-cs}$.

## Example
An undamped [spring](../Topics%202/Mechanical%20and%20Electrical%20Vibrations.md) at rest, struck at $t = c$: $y'' + y = \delta(t-c)$, $y(0) = y'(0) = 0$.
$$
Y = \frac{e^{-cs}}{s^2+1} \quad\Longrightarrow\quad y(t) = u_c(t)\,\sin(t-c)
$$

## What the impulse does
- $y$ stays continuous, and $y'$ jumps by $1$ at $t = c$.
- For $my'' + \cdots = \delta(t-c)$ the jump is $1/m$: the blow hands over one unit of momentum instantly.
- An impulse at $t = 0$ on a system at rest is the same as starting with $y(0) = 0$, $y'(0) = 1/m$.

See also: [Convolution and the Transfer Function](Convolution%20and%20the%20Transfer%20Function.md)
