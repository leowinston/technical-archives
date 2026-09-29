---
tags: [probability, topic, part-1]
---
# Stars and Bars
Back to [[self-study/probability/Index|Index]] · Part 1

## Result
The number of ways to put $k$ **indistinguishable** objects into $n$ **distinguishable** boxes is
$$
\boxed{\binom{n+k-1}{k}}
$$
**Encoding:** write the $k$ objects as stars and separate the boxes with $n-1$ bars. For example, $n = 4$ and $k = 5$ gives `* | ** | | **`. Choose which $k$ of the $n+k-1$ slots are stars.

## Equivalent forms
- Nonnegative integer solutions of $x_1 + \cdots + x_n = k$: $\binom{n+k-1}{k}$.
- **At least one per box:** give each box one first, then place the remaining $k-n$ objects. This gives $\binom{k-1}{n-1}$.

## Warning
Under random placement these configurations are **not** equally likely, so don't plug them into the naive definition.

## Problems
- [[P07 - Chocolate Bars, Gummy Bears, and Bootstrap Samples]]

See also: [[Sampling With and Without Replacement]]
