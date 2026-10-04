---
tags: [graph-theory, theory, spectral-graph-theory]
source: Handwritten notes "Thm" / "Algo" steps ①–④
---
# Spectral Clustering Algorithm
Back to [Index](../Index.md) · Handwritten notes

## Theorem
1. $\phi_G \ge \lambda_2$ (the Fiedler value; see [Sparsest Cut](Sparsest%20Cut.md)).
2. The algorithm below finds a cut with density at most $4\sqrt{\Delta(G)\,\lambda_2}$.

$$
\boxed{\,\lambda_2 \le \phi_G \le \phi(\text{sweep cut}) \le 4\sqrt{\Delta(G)\,\lambda_2}\,}
$$

## Algorithm (✎ steps ①–④)
```
① M ← n×2 matrix [Fiedler vector | vertex label 1..n]
② sort the rows of M by the Fiedler value
③ A_k ← first k labels, for k = 1..n−1
④ return the A_k with the lowest density φ(A_k, V − A_k)
```
The sweep checks only $n - 1$ cuts instead of $2^n$.
✎ My notes list $A_1 = \{9\}, \dots, A_{10} = V$. Stop at $A_{n-1}$, because $A_n = V$ is not a cut.

## Examples
- [EX07 - Sweep Cut on Two Joined Triangles](../Examples/EX07%20-%20Sweep%20Cut%20on%20Two%20Joined%20Triangles.md)
- [EX10 - Relaxation Gap on a 10-Node Graph](../../convex-optimization/explorations/EX10%20-%20Relaxation%20Gap%20on%20a%2010-Node%20Graph.md) (convex opt)
- [EX08 - Whisker Cut Versus Regularized Clustering](../Examples/EX08%20-%20Whisker%20Cut%20Versus%20Regularized%20Clustering.md) (where this vanilla version cuts off a dangling path)

## Regularized variant
On graphs with long dangling paths the sweep returns the path. [Regularized Spectral Clustering](Regularized%20Spectral%20Clustering.md) adds $\tfrac{\tau}{n}$ to every pair and normalizes by $D + \tau I$ to prevent this.

See also: [Spectral Gap and Fiedler Vector](Spectral%20Gap%20and%20Fiedler%20Vector.md), [Cuts and Cut Density](Cuts%20and%20Cut%20Density.md)
