---
tags: [math-315, topic, lecture-2]
---
# IEEE Floating-Point Standard
Back to [[Index]] · Section 2.2 (slide 35)

Most computers follow the IEEE standard, with $\beta = 2$ and two main formats.

## Formats
| | Single | Double |
|---|---|---|
| Memory | 4 bytes (32 bits) | 8 bytes (64 bits) |
| Sign bits | 1 | 1 |
| Exponent bits | 8 | 11 |
| Mantissa bits | 23 | 52 |
| Precision $p$ | 24 | 53 |

$p$ is one more than the stored mantissa bits because the leading $1$ of a normalized binary mantissa is not stored (the **hidden bit**).

## Derived constants
| | Single | Double |
|---|---|---|
| $L,\ U$ | $-126,\ 127$ | $-1022,\ 1023$ |
| UFL $= 2^{L}$ | $1.18 \times 10^{-38}$ | $2.23 \times 10^{-308}$ |
| OFL $= 2^{U+1}(1 - 2^{-p})$ | $3.40 \times 10^{38}$ | $1.80 \times 10^{308}$ |
| $u = 2^{-p}$ | $5.96 \times 10^{-8}$ | $1.11 \times 10^{-16}$ |

So double precision carries about 16 significant decimal digits, and single about 7.

## Explorations
- [[EX18 - Exploration 2.2.9 - Overflow Level of IEEE Double Precision]]

See also: [[Overflow and Underflow]], [[Rounding and Machine Precision]]
