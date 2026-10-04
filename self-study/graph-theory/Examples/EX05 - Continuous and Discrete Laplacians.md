---
tags: [graph-theory, example, spectral-graph-theory, background]
source: Constructed from the "Continuous functions" Laplacian column of my handwritten notes
topics: ["[[Laplace Operator and the Graph Laplacian]]", "[[Laplacian of a Graph]]"]
---
# EX05 — Continuous and Discrete Laplacians
Back to [Index](../Index.md)

> [!question] Problem
> (a) Sample $f(x) = x^2$ on the path $P_5$ as $x = (1, 4, 9, 16, 25)$. Compute $L_Gx$ and compare it with $f''$.
> (b) $g(x, y) = x^2 - y^2$ has $\Delta g = 2 - 2 = 0$. Sample it on the 3×3 grid $\{-1, 0, 1\}^2$. What is $(L_Gx)$ at the centre?

## Solution
**(a)** At an interior vertex $i$, $(L_Gx)_i = 2x_i - x_{i-1} - x_{i+1}$:

| $i$ | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| $x_i$ | 1 | 4 | 9 | 16 | 25 |
| $(L_Gx)_i$ | $-3$ | $-2$ | $-2$ | $-2$ | $9$ |

Interior values are $-2 = -f''$, as the boxed formula predicts. The endpoints differ because each has only one neighbour, a boundary effect.

**(b)** The centre $(0,0)$ has value $0$ and four grid neighbours with values $1, 1, -1, -1$:
$$
(L_Gx)_{\text{centre}} = 4 \cdot 0 - (1 + 1 - 1 - 1) = \boxed{0}.
$$
So $g$ is harmonic on the graph too: the centre equals the average of its neighbours.

## Takeaways
- $L_G$ is the negative second difference, so $L_G \approx -\Delta$ inside the graph.
- A harmonic function satisfies the mean-value property in both the continuous and the discrete setting.

## Related topics
- [Laplace Operator and the Graph Laplacian](../Theory/Laplace%20Operator%20and%20the%20Graph%20Laplacian.md)
- [Laplacian of a Graph](../Theory/Laplacian%20of%20a%20Graph.md)
