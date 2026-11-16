---
tags:
  - math-212
  - topic
  - chapter-3
---
# Complex Roots of the Characteristic Equation
Back to [Index](../Index.md) · Chapter 3.3

If $ar^2 + br + c = 0$ has roots $r = \lambda \pm i\mu$ ($b^2 < 4ac$), Euler's formula
$$
e^{(\lambda + i\mu)x} = e^{\lambda x}\left(\cos\mu x + i\sin\mu x\right)
$$
gives two **real** solutions, the real and imaginary parts:
$$
y = e^{\lambda x}\left(c_1\cos\mu x + c_2\sin\mu x\right)
$$

## Amplitude–phase form
$$
c_1\cos\mu x + c_2\sin\mu x = R\cos(\mu x - \delta), \qquad R = \sqrt{c_1^2 + c_2^2},\ \tan\delta = \frac{c_2}{c_1}
$$
- $\lambda < 0$: decaying oscillation inside the envelope $\pm Re^{\lambda x}$.
- $\lambda = 0$: pure oscillation (undamped spring).
- $\lambda > 0$: growing oscillation.

Example: $y'' + 4y' + 13y = 0$ gives $r = -2 \pm 3i$.

## Workbook problems
- [WB2 P08 - Complex Root IVP y'' + 4y' + 13y = 0](../Workbook%202/WB2%20P08%20-%20Complex%20Root%20IVP%20y%27%27%20+%204y%27%20+%2013y%20=%200.md)
- [WB2 P09 - Constant Forcing y'' + y = 1](../Workbook%202/WB2%20P09%20-%20Constant%20Forcing%20y%27%27%20+%20y%20=%201.md)
- [WB2 P19 - Trigonometric Forcing at Resonance](../Workbook%202/WB2%20P19%20-%20Trigonometric%20Forcing%20at%20Resonance.md)
- [WB2 P28 - Undamped Spring](../Workbook%202/WB2%20P28%20-%20Undamped%20Spring.md)
- [WB2 P32 - RLC Circuit with AC Forcing](../Workbook%202/WB2%20P32%20-%20RLC%20Circuit%20with%20AC%20Forcing.md)
- [WB2 P33 - RLC Circuit with a Battery](../Workbook%202/WB2%20P33%20-%20RLC%20Circuit%20with%20a%20Battery.md)
