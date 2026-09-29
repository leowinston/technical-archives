---
tags: [probability, topic, part-6]
---
# Expected Present Value
Back to [[self-study/probability/Index|Index]] · Part 6

## Formula
A cash flow $C_t$ received at time $t$, with discount rate $r$ and probability $p_t$ of actually being paid, has
$$
\boxed{\text{EPV} = \sum_t p_t \,\frac{C_t}{(1 + r)^t}}
$$

## Two moves
Every valuation does the same two things:
1. **Discount for time:** a dollar later is worth $1/(1+r)^t$ dollars now.
2. **Weight for probability:** multiply by the chance the payment happens.

## Notes
- By **linearity of expectation**, EPV works even when the payments are dependent, for example when one shutdown kills all future payments. Dependence changes the **risk**, not the expected value.
- A company that loses money today can still be worth a lot if its expected discounted future cash flows are large. Its value is a bet on the later terms of the sum.

## Example
Pay $\$10$M at the end of each of years 1–3, $r = 10\%$, with a 50% chance of shutdown after year 1:
$$
\text{EPV} = \frac{10}{1.1} + \frac12\left(\frac{10}{1.1^2} + \frac{10}{1.1^3}\right) \approx 9.09 + 7.89 = \$16.98\text{M}
$$

## Problems
- [[P24 - Expected Present Value of a Risky Company]]

See also: [[Expected Value]], [[Limits of Expected Value]]
