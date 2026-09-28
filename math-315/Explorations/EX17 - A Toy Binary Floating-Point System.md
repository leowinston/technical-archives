---
tags: [math-315, exploration, lecture-2, floating-point]
source: Constructed example for Section 2.2 (slides 23, 29–30, 33–34)
topics: ["[[Floating-Point Number Systems]]", "[[Overflow and Underflow]]", "[[Rounding and Machine Precision]]"]
---
# EX17 — A Toy Binary Floating-Point System
Back to [[Index]]

> [!question] Problem
> Let $F$ be the normalized system with $\beta = 2$, $p = 3$, $L = -1$, $U = 1$.
> (a) List every positive number in $F$ and count all of $F$ (including $0$ and negatives).
> (b) Find UFL and OFL, and check the OFL formula.
> (c) Is $F$ equally spaced? (Slide 29's True or False.)
> (d) Find $u$ for rounding to nearest, and compute $\operatorname{fl}(2.2)$ and $\operatorname{fl}(1.125)$.

## Setup
- **Mantissas:** $m = (1.d_1d_2)_2$ with $d_1, d_2 \in \{0, 1\}$
- **Exponents:** $E \in \{-1, 0, 1\}$
- **Formulas:** $\text{UFL} = \beta^{L}$, $\text{OFL} = \beta^{U+1}(1 - \beta^{-p})$, $u = \tfrac12\beta^{1-p}$

## Strategy
1. List the 4 mantissas, then scale by each $2^{E}$.
2. Read off the smallest and largest.
3. Compute the gaps within each exponent range.
4. Round two test values.

## Solution
**(a) The numbers**

Mantissas: $(1.00)_2 = 1$, $(1.01)_2 = 1.25$, $(1.10)_2 = 1.5$, $(1.11)_2 = 1.75$.

| $E$ | $m \times 2^{E}$ | Gap |
|---|---|---|
| $-1$ | $0.5,\ 0.625,\ 0.75,\ 0.875$ | $0.125$ |
| $0$ | $1,\ 1.25,\ 1.5,\ 1.75$ | $0.25$ |
| $1$ | $2,\ 2.5,\ 3,\ 3.5$ | $0.5$ |

That is 12 positive numbers. In general,
$$
|F| = 2\underbrace{(\beta - 1)}_{d_0}\underbrace{\beta^{p-1}}_{d_1,\dots,d_{p-1}}\underbrace{(U - L + 1)}_{E} + 1 = 2(1)(4)(3) + 1 = \boxed{\,25\,}
$$
The factor $2$ is the sign and the $+1$ is zero.

**(b) UFL and OFL**
$$
\text{UFL} = 2^{-1} = 0.5, \qquad \text{OFL} = (1.11)_2 \times 2^{1} = 3.5
$$
Formula check:
$$
\beta^{U+1}(1 - \beta^{-p}) = 2^{2}\left(1 - \tfrac18\right) = 4 \cdot \tfrac78 = 3.5 \ \checkmark
$$
Anything in $(0, 0.5)$ underflows. Anything above $3.5$ (after rounding) overflows.

**(c) Spacing**

**False.** The gap doubles each time $E$ goes up by one: $0.125$, $0.25$, $0.5$. In general the gap in $[\beta^{E}, \beta^{E+1})$ is $\beta^{E-p+1}$. There is also a large hole $(0, 0.5)$ next to zero, since normalization forbids smaller mantissas. Subnormals fill that hole.

```desmos-graph
left=-0.25; right=4; top=0.6; bottom=-0.6
---
([0.5,0.625,0.75,0.875],0)|#2d70b3
([1,1.25,1.5,1.75],0)|#388c46
([2,2.5,3,3.5],0)|#c74440
(0,0)|#000000
```

The *relative* gap stays roughly constant:
$$
\frac{0.125}{0.5} = \frac{0.25}{1} = \frac{0.5}{2} = 0.25
$$
at the left end of each range, and it drops to about $0.14$ at the right end.

**(d) Unit roundoff and rounding**
$$
u = \tfrac12 \cdot 2^{1-3} = \boxed{\,0.125\,}
$$

*$\operatorname{fl}(2.2)$.* The neighbors are $2$ and $2.5$. $2.2$ is closer to $2$:
$$
\operatorname{fl}(2.2) = 2, \qquad \frac{|2 - 2.2|}{2.2} \approx 0.0909 \le 0.125 \ \checkmark
$$

*$\operatorname{fl}(1.125)$.* The neighbors are $1 = (1.00)_2$ and $1.25 = (1.01)_2$, and $1.125$ is exactly halfway. Ties go to the even last digit, so
$$
\operatorname{fl}(1.125) = (1.00)_2 = 1, \qquad \frac{0.125}{1.125} \approx 0.111 \le 0.125 \ \checkmark
$$
With chopping, $u = 2^{1-3} = 0.25$. For example $\operatorname{fl}(1.24) = 1$ with relative error $0.19$.

## Result
- $F$ has 25 numbers: 12 positive, 12 negative, and $0$.
- $\text{UFL} = 0.5$, $\text{OFL} = 3.5$, $u = 0.125$ (nearest) or $0.25$ (chopping).
- Spacing is **not** uniform: gaps are $0.125$, $0.25$, $0.5$.

## Takeaways
- Floating point controls **relative** error, not absolute error. That is why the gaps grow with $|x|$.
- The same picture scales to IEEE double, with $2^{52}$ numbers per exponent instead of 4.

## Related topics
- [[Floating-Point Number Systems]]
- [[Overflow and Underflow]]
- [[Rounding and Machine Precision]]
