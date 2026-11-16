---
tags:
  - math-315
  - exploration
  - lecture-7
source: Lecture 7 handout, pp. 4 and 11
topics:
  - "[[../Topics 4/Fixed Point Iteration]]"
  - "[[../Topics 4/Order of Convergence]]"
---
# EX52 — Fixed Point Iteration for e^-x and -ln x
Back to [Index](../Index.md)

> [!question] Problem
> $g(x) = e^{-x}$ and $h(x) = -\ln x$ have the same fixed point $x^* = 0.56714329\ldots$
> (a) Run $x_{n+1} = g(x_n)$ and $x_{n+1} = h(x_n)$ from $x_0 = 0.5$.
> (b) Explain the two behaviors with $g'(x^*)$ and $h'(x^*)$.
> (c) Predict how many steps $g$ needs to reach an error of $10^{-10}$.

## Setup
- Same fixed point: $x = e^{-x} \iff \ln x = -x \iff x = -\ln x$.
- $g'(x) = -e^{-x}$ and $h'(x) = -1/x$.
- At the fixed point $e^{-x^*} = x^*$, so $g'(x^*) = -x^* = -0.5671$ and $h'(x^*) = -1/x^* = -1.7632$.

## Solution
**(a)**

```python
import numpy as np
x = 0.5
for n in range(8):
    x = np.exp(-x)
```

| $n$ | $x_n = e^{-x_{n-1}}$ | $\lvert e_n\rvert$ | $\lvert e_n\rvert / \lvert e_{n-1}\rvert$ |
|---|---|---|---|
| 1 | 0.60653066 | 3.94e-02 | 0.5866 |
| 2 | 0.54523921 | 2.19e-02 | 0.5561 |
| 3 | 0.57970309 | 1.26e-02 | 0.5734 |
| 4 | 0.56006463 | 7.08e-03 | 0.5636 |
| 5 | 0.57117215 | 4.03e-03 | 0.5692 |
| 6 | 0.56486295 | 2.28e-03 | 0.5660 |
| 7 | 0.56843805 | 1.29e-03 | 0.5678 |
| 8 | 0.56640945 | 7.34e-04 | 0.5668 |

The same loop with $h$:

| $n$ | $x_n = -\ln x_{n-1}$ | $\lvert e_n\rvert$ |
|---|---|---|
| 1 | 0.693147 | 0.126 |
| 2 | 0.366513 | 0.201 |
| 3 | 1.003722 | 0.437 |
| 4 | -0.003715 | 0.571 |
| 5 | `nan` | |

The error grows every step until an iterate goes negative and the logarithm fails.

**(b)** The error obeys $e_{n+1} = g'(\eta)\,e_n$.
- For $g$: $\lvert g'(x^*)\rvert = 0.5671 < 1$. The measured ratios settle at $0.567$, exactly $x^*$. Because $g'(x^*) < 0$, the iterates alternate sides: $0.6065 > x^* > 0.5452 < \ldots$
- For $h$: $\lvert h'(x^*)\rvert = 1.7632 > 1$. The first ratio is $0.201/0.126 = 1.6$, close to the predicted $1.76$. The fixed point repels.

$g$ and $h$ are inverse functions, so $h'(x^*) = 1/g'(x^*)$. One of an inverse pair always contracts and the other expands.

**(c)** With $\lvert e_n\rvert \approx (0.5671)^n\,\lvert e_0\rvert$ and $\lvert e_0\rvert = 0.0671$:
$$
n \approx \frac{\ln(10^{-10}/0.0671)}{\ln 0.5671} = 35.8
$$
The loop takes $36$ steps.

## Takeaways
- The same fixed point can attract under one rearrangement and repel under another. Only $\lvert g'(x^*)\rvert$ decides.
- The linear rate is not a bound here, it is what you measure: the ratio converges to $\lvert g'(x^*)\rvert$.
- On $[0.45, 0.7]$, $\lvert g'\rvert \le e^{-0.45} = 0.638 < 1$, and $g$ maps the interval into itself ($g$ is decreasing, with $g(0.45) = 0.638$ and $g(0.7) = 0.497$). So $g$ is a contraction there. [Banach's Fixed Point Theorem](../../../archive/proofs/Explorations/Banach's%20Fixed%20Point%20Theorem.md) then guarantees the unique fixed point without ever computing it.

## Related topics
- [Fixed Point Iteration](../Topics%204/Fixed%20Point%20Iteration.md)
- [Order of Convergence](../Topics%204/Order%20of%20Convergence.md)
