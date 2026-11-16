---
tags:
  - math-212
  - topic
  - chapter-3
---
# Mechanical and Electrical Vibrations
Back to [Index](../Index.md) · Chapter 3.7

## Spring–mass system
A mass $m$ on a spring with constant $k$ and damping $c$, displaced $x(t)$ from equilibrium:
$$
mx'' + cx' + kx = F(t)
$$
- **Hooke's law:** $k = \dfrac{\text{force}}{\text{stretch}}$
- **Natural frequency:** $\omega = \sqrt{k/m}$
- **Free undamped** ($c = 0$, $F = 0$): $x = c_1\cos\omega t + c_2\sin\omega t$, with period $2\pi/\omega$.

## Free damped: sign of $c^2 - 4mk$
| $c^2 - 4mk$ | Type | Motion |
|---|---|---|
| $> 0$ | overdamped | $c_1e^{r_1t} + c_2e^{r_2t}$, no oscillation |
| $= 0$ | critically damped | $(c_1 + c_2t)e^{-ct/2m}$ |
| $< 0$ | underdamped | decaying oscillation |

Example: $m = 2$, $k = 128$ gives $\omega = 8$.

## RLC circuits
The charge $Q(t)$ in a series circuit satisfies
$$
LQ'' + RQ' + \frac{1}{C}Q = E(t), \qquad I = Q'
$$
The spring analogy is $m \leftrightarrow L$, $c \leftrightarrow R$, $k \leftrightarrow 1/C$, $F \leftrightarrow E$, $x \leftrightarrow Q$, so the circuit is underdamped when $R^2 < 4L/C$. Impose $Q(0)$ and $Q'(0) = I(0)$ on the **full** solution $Q_c + Q_p$. With a battery $E$, $Q_p = CE$ and $I \to 0$.

## Workbook problems
- [WB2 P28 - Undamped Spring](../Workbook%202/WB2%20P28%20-%20Undamped%20Spring.md)
- [WB2 P29 - Overdamped Spring in a Fluid](../Workbook%202/WB2%20P29%20-%20Overdamped%20Spring%20in%20a%20Fluid.md)
- [WB2 P30 - Forced Undamped Oscillator](../Workbook%202/WB2%20P30%20-%20Forced%20Undamped%20Oscillator.md)
- [WB2 P31 - Damped Spring and Critical Damping](../Workbook%202/WB2%20P31%20-%20Damped%20Spring%20and%20Critical%20Damping.md)
- [WB2 P32 - RLC Circuit with AC Forcing](../Workbook%202/WB2%20P32%20-%20RLC%20Circuit%20with%20AC%20Forcing.md)
- [WB2 P33 - RLC Circuit with a Battery](../Workbook%202/WB2%20P33%20-%20RLC%20Circuit%20with%20a%20Battery.md)

See also: [Forced Periodic Vibrations](Forced%20Periodic%20Vibrations.md)
