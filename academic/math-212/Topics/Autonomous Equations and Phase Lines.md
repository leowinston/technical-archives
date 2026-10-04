---
tags: [math-212, topic, chapter-2]
---
# Autonomous Equations and Phase Lines
Back to [Index](../Index.md) · Chapter 2.5

## Definition
$$
\frac{dy}{dt} = f(y)
$$
The independent variable $t$ does not appear on the right side.

## Qualitative analysis recipe
1. **Equilibria (critical points):** solve $f(y) = 0$. Each root gives a constant solution $y \equiv y_i$.
2. **Increasing and decreasing:** find the sign of $f(y)$ between equilibria. Solutions increase where $f > 0$ and decrease where $f < 0$.
3. **Phase line:** draw the $y$-axis with the equilibria marked and arrows showing the direction of motion.
4. **Concavity:** use
$$
\frac{d^2y}{dt^2} = f'(y)\,f(y)
$$
   Solutions are concave up where $f'f > 0$ and concave down where $f'f < 0$. Inflection points occur where $f'(y) = 0$.
5. **Sketch** solutions in the $ty$-plane. Solutions never cross an equilibrium, and a solution shifted in time is still a solution.
6. **Classify each equilibrium $y_1$:**
   - [Asymptotically stable](Stable%20Equilibrium.md) if $f'(y_1) < 0$ (arrows point toward it)
   - [Unstable](Unstable%20Equilibrium.md) if $f'(y_1) > 0$ (arrows point away)
   - [Semistable](Semistable%20Equilibrium.md) if $f$ has the same sign on both sides of $y_1$

## Standard population models

| Model | Equation | Behavior |
|---|---|---|
| [Exponential Growth](Exponential%20Growth.md) | $y' = ry$ | $y = y_0 e^{rt}$ |
| [Logistic Growth](Logistic%20Growth.md) | $y' = r\left(1 - \frac{y}{K}\right)y$ | $K$ stable, $0$ unstable |
| [Threshold Growth](Threshold%20Growth.md) | $y' = -r\left(1 - \frac{y}{T}\right)y$ | $T$ unstable, $0$ stable |
| [Logistic Growth with a Threshold](Logistic%20Growth%20with%20a%20Threshold.md) | $y' = -r\left(1 - \frac{y}{T}\right)\left(1 - \frac{y}{K}\right)y$ | $0, K$ stable; $T$ unstable |
| [Gompertz Growth](Gompertz%20Growth.md) | $y' = ry\ln\frac{K}{y}$ | $K$ stable |
| [Harvesting](Harvesting.md) | $y' = r\left(1 - \frac{y}{K}\right)y - Ey$ | $K(1 - E/r)$ stable |

## Workbook problems
- [WB1 P23 - Exponential Growth](../Workbook%201/WB1%20P23%20-%20Exponential%20Growth.md)
- [WB1 P24 - Logistic Growth](../Workbook%201/WB1%20P24%20-%20Logistic%20Growth.md)
- [WB1 P25 - A Critical Threshold](../Workbook%201/WB1%20P25%20-%20A%20Critical%20Threshold.md)
- [WB1 P27 - Logistic Growth with a Threshold](../Workbook%201/WB1%20P27%20-%20Logistic%20Growth%20with%20a%20Threshold.md)

See also: [Bifurcations](Bifurcations.md)
