---
tags: [convex-optimization, exploration, ml-notebook, information-theory]
source: ML notebook "Huffman Coding" (symbols a–f, codes 10, 000, 110, 01, 001, 111)
topics: ["[[Prefix Codes and Huffman Coding]]"]
---
# EX11 — Huffman Code and the Entropy Bound
Back to [[self-study/convex-optimization/Index|Index]]

> [!question] Problem
> Your notebook code is $a{:}\,10,\ b{:}\,000,\ c{:}\,110,\ d{:}\,01,\ e{:}\,001,\ f{:}\,111$. Take
> $p = (p_a, \dots, p_f) = (0.25,\ 0.10,\ 0.15,\ 0.25,\ 0.10,\ 0.15)$.
> (a) Run Huffman and check that it gives these codeword lengths.
> (b) Compute $\E[L]$ and compare with the convex-relaxation bound $H(p)$.

## Solution
**(a)** Always merge the two smallest:
1. $b + e = 0.20$
2. $c + f = 0.30$
3. $(be) + a = 0.45$ (or $d$; it is a tie)
4. $d + (cf) = 0.55$
5. $0.45 + 0.55 = 1$

Depths: $a, d$ at 2 and $b, c, e, f$ at 3. That matches your lengths $(2, 3, 3, 2, 3, 3)$. Kraft: $2\cdot 2^{-2} + 4\cdot 2^{-3} = 1$, so the tree is full (✎ no node with a single child).

**(b)**
$$
\E[L] = 2(0.25 + 0.25) + 3(0.10 + 0.15 + 0.10 + 0.15) = \boxed{\,2.5 \text{ bits}\,}
$$
The relaxation "minimize $\sum p_a\ell_a$ s.t. $\sum 2^{-\ell_a} \le 1$, $\ell \in \R^6$" is convex. Its optimum is $\ell_a = -\log_2 p_a = (2,\ 3.32,\ 2.74,\ 2,\ 3.32,\ 2.74)$, with value
$$
H(p) = -\sum p_a\log_2 p_a = 2.485 \text{ bits}.
$$
```python
import numpy as np
p = np.array([.25, .10, .15, .25, .10, .15])
l = np.array([2, 3, 3, 2, 3, 3])
print((p * l).sum(), -(p * np.log2(p)).sum(), (2.0 ** -l).sum())  # 2.5 2.4855 1.0
```
$$
H = 2.485 \ \le\ \E[L] = 2.5 \ <\ H + 1 \ \checkmark
$$
Rounding forces integer lengths, and that costs only $0.015$ bits here.

## Takeaways
- Huffman solves the **integer** problem exactly by a greedy method (Lemmas 1–2 + optimal substructure).
- The **continuous** relaxation is convex, and its value (the entropy) is the lower bound.

## Related topics
- [[Prefix Codes and Huffman Coding]]
- [[Noiseless and Memoryless Channels]]
