---
tags: [probability, problem, part-6]
topics: ["[[Expected Present Value]]"]
---
# P24 — Expected Present Value of a Risky Company
Back to [Index](../Index.md)

> [!question] Problem
> A company will pay $\$10$M at the end of each of the next three years, but there is a 50% chance it shuts down right after the first payment. The discount rate is 10%.
> (a) What is the company worth today?
> (b) What would it be worth with no shutdown risk?
> (c) Would the answer change if each of the last two payments independently had a 50% chance of being missed?

## Strategy
Every valuation makes two moves: **discount for time** and **weight for probability**. Apply both to each payment, then add (linearity).

## Solution
**(a)** Payment 1 is certain. Payments 2 and 3 each happen with probability $1/2$.
$$
\text{EPV} = \frac{10}{1.1} + \frac12\left(\frac{10}{1.1^2} + \frac{10}{1.1^3}\right) = 9.09 + \frac12(8.26 + 7.51) = 9.09 + 7.89 = \boxed{\$16.98\text{M}}
$$

**(b)** $\dfrac{10}{1.1} + \dfrac{10}{1.21} + \dfrac{10}{1.331} = \$24.87$M. The shutdown risk costs about $\$7.9$M of value.

**(c)** **No.** Payments 2 and 3 are **not independent** in (a): one shutdown kills both. By linearity of expectation, the EPV only uses each payment's own probability, so it is $\$16.98$M either way. What changes is the **risk**. In (a) you get all or nothing of the last two payments. In (c) you often get one of them, so the outcome is less spread out.

## Takeaway
A firm that loses money now can have a huge valuation. The EPV sum is dominated by large, probability-weighted, discounted **future** terms.

## Related topics
- [Expected Present Value](../Notes/Expected%20Present%20Value.md)
- [Expected Value](../Notes/Expected%20Value.md) (linearity doesn't need independence)
