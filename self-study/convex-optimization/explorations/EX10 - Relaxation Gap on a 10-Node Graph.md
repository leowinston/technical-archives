---
tags: [convex-optimization, exploration, ml-notebook, relaxation]
source: ML notebook "Spectral Clustering" / "Sparsest Cut" (two-cluster sketch)
topics: ["[[Sparsest Cut as a Spectral Relaxation]]"]
---
# EX10 — Relaxation Gap on a 10-Node Graph
Back to [[self-study/convex-optimization/Index|Index]]

> [!question] Problem
> Two 5-node clusters, $\{1,\dots,5\}$ and $\{6,\dots,10\}$, are joined by a bridge $5$–$6$ of weight $t$ (like my sketch).
> Cluster edges: $1$–$2$, $1$–$3$, $2$–$3$, $2$–$4$, $3$–$5$, $4$–$5$, $1$–$5$ and $6$–$7$, $6$–$8$, $7$–$8$, $7$–$9$, $8$–$10$, $9$–$10$, $6$–$10$.
> (a) For $t = 1$, compare the relaxed value $\lambda_2$ with the true $\phi_G$ and the rounding bound.
> (b) Tabulate $\lambda_2(t)$ and check that it behaves concavely.

## Solution
```python
import numpy as np
E = [(1,2),(1,3),(2,3),(2,4),(3,5),(4,5),(1,5),
     (6,7),(6,8),(7,8),(7,9),(8,10),(9,10),(6,10)]
def lam2(t):
    A = np.zeros((10, 10))
    for i, j in E:
        A[i-1, j-1] = A[j-1, i-1] = 1
    A[4, 5] = A[5, 4] = t
    return np.linalg.eigvalsh(np.diag(A.sum(1)) - A)[1]
```

**(a)** At $t = 1$, the sweep (see [[Spectral Clustering Algorithm]]) returns $A = \{1,\dots,5\}$ with $\phi = 10 \cdot \frac{1}{5 \cdot 5} = 0.4$. Brute force over all $1022$ cuts confirms that this is $\phi_G$.
$$
\underbrace{\lambda_2 = 0.266}_{\text{relaxation}} \ \le\ \underbrace{\phi_G = 0.4}_{\text{true optimum}} \ \le\ \underbrace{4\sqrt{4(0.266)} = 4.13}_{\text{rounding bound}}
$$
The relaxation is within a factor $1.5$. The worst-case bound is much looser than what rounding actually achieves.

**(b)**

| $t$ | 0 | 0.5 | 1 | 2 | 4 |
|---|---|---|---|---|---|
| $\lambda_2$ | 0 | 0.161 | 0.266 | 0.389 | 0.500 |
| slope to next | 0.32 | 0.21 | 0.12 | 0.06 | — |

The slopes decrease, as a concave function's must. $\lambda_2(0) = 0$ because the graph is disconnected.

## Takeaways
- $\lambda_2$ is a cheap lower bound on an NP-hard minimum, and rounding its eigenvector recovers the optimum here.
- Strengthening the bridge raises connectivity with diminishing returns, which is concavity in $w$.

## Related topics
- [[Sparsest Cut as a Spectral Relaxation]]
- [[Operations That Preserve Convexity of Functions]]
- [[EX08 - Whisker Cut Versus Regularized Clustering]] (this graph with a dangling path added)
