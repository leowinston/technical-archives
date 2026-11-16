---
tags:
  - math-212
  - topic
  - chapter-6
---
# Convolution and the Transfer Function
Back to [Index](../Index.md) · Chapter 6.6 · Beyond the enrichment handout

A product on the $s$ side is not a product on the $t$ side. It is a convolution.

## Convolution theorem
$$
(f*g)(t) = \int_0^t f(t-\tau)\,g(\tau)\,d\tau, \qquad \boxed{\mathcal{L}\{f*g\} = F(s)\,G(s)}
$$

## Transfer function
For $ay'' + by' + cy = g(t)$ starting at rest, [the transformed equation](Solving%20Initial%20Value%20Problems%20with%20the%20Laplace%20Transform.md) is
$$
Y(s) = H(s)\,G(s), \qquad H(s) = \frac{1}{as^2+bs+c}
$$
$H$ depends only on the system. Its inverse $h(t) = \mathcal{L}^{-1}\{H\}$ is the **impulse response**, the solution when $g = \delta$ ([Impulses and the Dirac Delta](Impulses%20and%20the%20Dirac%20Delta.md)). So for any forcing,
$$
y(t) = \int_0^t h(t-\tau)\,g(\tau)\,d\tau
$$
The output is a sum of delayed hammer blows, each weighted by the forcing at that moment. [Variation of parameters](../Topics%202/Variation%20of%20Parameters.md) arrives at the same integral.

## Example: resonance
$y'' + y = \cos t$ from rest. Here $h(t) = \sin t$ and
$$
Y = \frac{1}{s^2+1}\cdot\frac{s}{s^2+1} = \frac{s}{(s^2+1)^2} \quad\Longrightarrow\quad y(t) = \tfrac12\,t\sin t
$$
The forcing puts its pole exactly on the system's pole. A double pole gives the factor $t$, which is the growing amplitude in [Forced Periodic Vibrations](../Topics%202/Forced%20Periodic%20Vibrations.md).
