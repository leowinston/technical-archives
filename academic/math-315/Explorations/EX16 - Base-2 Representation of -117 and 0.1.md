---
tags: [math-315, exploration, lecture-2, floating-point]
source: Lecture 2 slides, slides 24–28 (Example 2.2.2 and the Python demo)
topics: ["[[Floating-Point Number Systems]]", "[[Exponent and Mantissa]]"]
---
# EX16 — Base-2 Representation of −117 and 0.1
Back to [Index](../Index.md)

> [!question] Problem
> (a) Write $x = -117$ as a normalized floating-point number in base 10 and in base 2.
> (b) Use the three-step algorithm (exponent from logs, mantissa by scaling, digits by repeated doubling) to find the binary mantissa of $117$.
> (c) Repeat (b) for $x = 0.1$. What goes wrong?

## Setup
- **Normalized form:** $x = \pm m\beta^{E}$ with $1 \le m < \beta$
- **Digit rule** ($\beta = 2$): $f \leftarrow 2f$, $d_j = \lfloor f \rfloor$, $f \leftarrow f - d_j$
- **Sign:** handle separately, so work with $|x|$

## Strategy
1. Base 10 by inspection.
2. Base 2: $E = \lfloor \log_2 x \rfloor$, $m = x/2^{E}$, then peel off digits.
3. Check by expanding the binary mantissa.
4. Run the same loop on $0.1$ and look for a repeating pattern.

## Solution
**(a) Base 10**
$$
-117 = -(1.17) \times 10^{2}, \qquad m = 1 \times 10^{0} + 1 \times 10^{-1} + 7 \times 10^{-2}
$$
So $\beta = 10$, $p = 3$, $E = 2$.

**(b) Base 2**

*Step 1: exponent.*
$$
2^6 = 64 \le 117 < 128 = 2^7 \implies E = \lfloor \log_2 117 \rfloor = 6
$$

*Step 2: mantissa.*
$$
m = \frac{117}{2^6} = \frac{117}{64} = 1.828125
$$
So $d_0 = 1$ and $f = 0.828125$.

*Step 3: digits.*
| $j$ | $2f$ | $d_j$ | new $f$ |
|---|---|---|---|
| 1 | $1.65625$ | 1 | $0.65625$ |
| 2 | $1.3125$ | 1 | $0.3125$ |
| 3 | $0.625$ | 0 | $0.625$ |
| 4 | $1.25$ | 1 | $0.25$ |
| 5 | $0.5$ | 0 | $0.5$ |
| 6 | $1.0$ | 1 | $0$ |

The loop stops at $f = 0$:
$$
-117 = -(1.110101)_2 \times 2^{6}
$$

*Check.*
$$
(1.110101)_2 = 1 + \tfrac12 + \tfrac14 + \tfrac1{16} + \tfrac1{64} = \frac{64 + 32 + 16 + 4 + 1}{64} = \frac{117}{64} \ \checkmark
$$
The mantissa needs $p = 7$ bits.

**(c) Base 2 for $0.1$**

*Step 1.* $\log_2 0.1 \approx -3.32$, so $E = -4$.

*Step 2.* $m = 0.1 \times 2^{4} = 1.6$, so $d_0 = 1$ and $f = 0.6$.

*Step 3.*
| $j$ | $2f$ | $d_j$ | new $f$ |
|---|---|---|---|
| 1 | $1.2$ | 1 | $0.2$ |
| 2 | $0.4$ | 0 | $0.4$ |
| 3 | $0.8$ | 0 | $0.8$ |
| 4 | $1.6$ | 1 | $0.6$ |
| 5 | $1.2$ | 1 | $0.2$ |
| ⋮ | | | |

At $j = 4$ we are back to $f = 0.6$, so the digits repeat forever:
$$
0.1 = (1.\overline{1001})_2 \times 2^{-4}
$$
No finite $p$ represents $0.1$ exactly, so the computer stores $\operatorname{fl}(0.1)$, not $0.1$.

### The Python demo
The slide's `mantissa_2` implements the same loop:
```python
import math
def mantissa_2(x, p=20, tol=1e-12):
    e = math.floor(math.log2(x))
    m = x / (2**e)
    r = m - 1.0
    for i in range(1, p):
        double_r = 2 * r
        di = int(double_r)
        r = double_r - di
        print(f"Step {i} 2r={double_r:.5f} d_i={di} r={r:.5f}")
        if r < tol:
            break
```
`mantissa_2(117)` stops after step 6 with `r=0.00000`. `mantissa_2(0.1)` runs all `p` steps, printing $1, 0, 0, 1, 1, 0, 0, 1, \ldots$.

## Result
$$
-117 = -(1.17) \times 10^{2} = -(1.110101)_2 \times 2^{6}, \qquad 0.1 = (1.\overline{1001})_2 \times 2^{-4}
$$

## Takeaways
- A number with a short decimal expansion may have an infinite binary one. That is why `0.1 + 0.2 != 0.3` in Python.
- Doubling reads off binary digits the same way multiplying by 10 reads off decimal ones.
- In binary $d_0 = 1$ always, so IEEE doesn't store it (see [IEEE Floating-Point Standard](../Topics/IEEE%20Floating-Point%20Standard.md)).

## Related topics
- [Floating-Point Number Systems](../Topics/Floating-Point%20Number%20Systems.md)
- [Exponent and Mantissa](../Topics/Exponent%20and%20Mantissa.md)
- [Rounding and Machine Precision](../Topics/Rounding%20and%20Machine%20Precision.md)
