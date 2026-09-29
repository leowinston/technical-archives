---
tags: [convex-optimization, exploration, ml-notebook, spectral-graph-theory]
source: ML notebook "Spectral Clustering" / "Sparsest Cut" (two-cluster sketch and algorithm steps ①–④)
topics: ["[[Spectral Clustering and Sparsest Cut]]", "[[Graph Laplacian]]"]
---
# EX10 — Fiedler Vector Sparsest Cut on a 10-Node Graph
Back to [[self-study/convex-optimization/Index|Index]]

> [!question] Problem
> Two 5-node clusters, $\{1,\dots,5\}$ and $\{6,\dots,10\}$, are joined by the single edge $5$–$6$ (like your sketch).
> Cluster edges: $1$–$2$, $1$–$3$, $2$–$3$, $2$–$4$, $3$–$5$, $4$–$5$, $1$–$5$ and $6$–$7$, $6$–$8$, $7$–$8$, $7$–$9$, $8$–$10$, $9$–$10$, $6$–$10$.
> Run the four steps and check the theorem.

## Strategy
Follow your notebook:
1. Form $L_G$ and get the Fiedler vector.
2. Sort the vertices by their Fiedler entries.
3. Form the prefix sets $A_1 \subset A_2 \subset \cdots \subset A_9$.
4. Check the density of each set and keep the lowest.

## Solution
```python
import numpy as np

edges = [(1,2),(1,3),(2,3),(2,4),(3,5),(4,5),(1,5),
         (6,7),(6,8),(7,8),(7,9),(8,10),(9,10),(6,10),(5,6)]
n = 10
A = np.zeros((n, n))
for i, j in edges:
    A[i-1, j-1] = A[j-1, i-1] = 1
L = np.diag(A.sum(1)) - A

lam, V = np.linalg.eigh(L)
fiedler = V[:, 1]
order = np.argsort(fiedler)

def density(S):
    cut = sum((i-1 in S) != (j-1 in S) for i, j in edges)
    return n * cut / (len(S) * (n - len(S)))

dens = [density(set(order[:k])) for k in range(1, n)]
print(lam[1], order + 1, np.round(dens, 3))
```
**Step 1.** $\lambda_2 = 0.266$. The Fiedler vector is negative on $\{1,\dots,5\}$ ($\approx -0.33$, with vertex 5 at $-0.21$) and positive on $\{6,\dots,10\}$ ($\approx 0.33$, with vertex 6 at $0.20$).

**Steps 2–4.** Sorted order: $2, 1, 4, 3, 5, 6, 8, 10, 7, 9$.

| $k$ | $A_k$ | edges cut | density $\phi$ |
|---|---|---|---|
| 1 | $\{2\}$ | 3 | 3.333 |
| 2 | $\{1,2\}$ | 4 | 2.5 |
| 3 | $\{1,2,4\}$ | 4 | 1.905 |
| 4 | $\{1,2,3,4\}$ | 3 | 1.25 |
| **5** | $\{1,\dots,5\}$ | **1** | $\mathbf{0.4}$ |
| 6 | $\{1,\dots,6\}$ | 3 | 1.25 |
| 7–9 | … | 4, 3, 2 | 1.905, 1.875, 2.222 |

$$
\boxed{\,\text{best cut } A = \{1,\dots,5\},\quad \phi = 10\cdot\frac{1}{5\cdot 5} = 0.4\,}
$$

**Theorem check** (max degree $\Delta = 4$):
$$
\lambda_2 = 0.266 \ \le\ \phi_G \le 0.4 \ \le\ 4\sqrt{\Delta\lambda_2} = 4\sqrt{4(0.266)} = 4.13 \ \checkmark
$$

## Takeaways
- 9 cuts were checked instead of $2^{10} = 1024$ subsets.
- The sign of the Fiedler vector already separates the clusters. The bridge vertices 5 and 6 have the smallest magnitudes ($-0.21$, $0.20$), because they are the least sure which side they belong to.
- The sign of an eigenvector is arbitrary, so `eigh` may return $-v$. The sorted order just reverses and the cuts are the same.

## Related topics
- [[Spectral Clustering and Sparsest Cut]]
- [[Graph Laplacian]]
- [[Positive Semidefinite Matrices]]
