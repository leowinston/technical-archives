---
tags: [math-315, topic, lecture-2]
---
# Exponent and Mantissa
Back to [[Index]] · Section 2.2 (slides 26–28)

Goal: given $x > 0$, find the normalized $E$ and $m$ with $x = m\beta^{E}$, $1 \le m < \beta$.

## Step 1: exponent from logs
$$
\log_\beta x = \log_\beta m + E, \quad \log_\beta m \in [0, 1) \implies E = \lfloor \log_\beta x \rfloor
$$

## Step 2: mantissa by scaling
$$
m = \frac{x}{\beta^{E}}, \qquad 1 \le m < \beta
$$

## Step 3: base-$\beta$ digits of $m$
Write $m = d_0 + \sum_{j \ge 1} d_j\beta^{-j}$ and let $f = m - d_0$. Repeat "multiply by $\beta$, peel off the integer part":
```
for j from 1 to p-1:
    f = beta * f
    d[j] = floor(f)
    f = f - d[j]
```
If $f$ never reaches $0$, the expansion does not terminate and $x$ must be rounded.

## Notes
$x = 0$ is stored with $m = 0$. Very small nonzero values may be **subnormal**, which relaxes $1 \le m < \beta$.

## Example
$x = 117$, $\beta = 2$: $E = \lfloor \log_2 117 \rfloor = 6$, $m = 117/64 = 1.828125 = (1.110101)_2$.

## Explorations
- [[EX16 - Base-2 Representation of -117 and 0.1]]

See also: [[Floating-Point Number Systems]], [[Rounding and Machine Precision]]
