---
tags:
  - math-212
  - topic
  - chapter-3
---
# Forced Periodic Vibrations
Back to [Index](../Index.md) · Chapter 3.8

Undamped spring with periodic forcing:
$$
mx'' + kx = F_0\cos\omega_0t, \qquad \omega = \sqrt{k/m}
$$

## Non-resonant ($\omega_0 \neq \omega$)
$$
x = c_1\cos\omega t + c_2\sin\omega t + \frac{F_0}{m\left(\omega^2 - \omega_0^2\right)}\cos\omega_0t
$$
From rest, this gives **beats**:
$$
x = \frac{2F_0}{m(\omega^2 - \omega_0^2)}\sin\frac{(\omega - \omega_0)t}{2}\sin\frac{(\omega + \omega_0)t}{2}
$$

## Resonance ($\omega_0 = \omega$)
The forcing frequency is a characteristic root, so the trial needs an extra factor $t$:
$$
x_p = \frac{F_0}{2m\omega}\,t\sin\omega t
$$
The amplitude grows linearly without bound.

## With damping
The transient decays and only the steady state $x_p$ survives, so the amplitude stays bounded.

## Workbook problems
- [WB2 P19 - Trigonometric Forcing at Resonance](../Workbook%202/WB2%20P19%20-%20Trigonometric%20Forcing%20at%20Resonance.md)
- [WB2 P30 - Forced Undamped Oscillator](../Workbook%202/WB2%20P30%20-%20Forced%20Undamped%20Oscillator.md)
