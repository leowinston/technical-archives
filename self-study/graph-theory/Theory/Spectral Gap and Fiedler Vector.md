---
tags: [graph-theory, theory, spectral-graph-theory]
source: Handwritten notes "Spectral Gap" / "Fiedler Value & Fiedler Vector"
---
# Spectral Gap and Fiedler Vector
Back to [Index](../Index.md) · Handwritten notes

Order the eigenvalues of $L_G$:
$$
0 = \lambda_1 \le \lambda_2 \le \lambda_3 \le \cdots \le \lambda_n
$$
✎ $\lambda_1$ is always zero, with eigenvector $\ones$.

## What $\lambda_2$ says
| $\lambda_2$ | Graph |
|---|---|
| $= 0$ | not connected |
| $> 0$, small | connected, but nearly disconnected |
| $> 0$, big | very connected |

More generally, the multiplicity of the eigenvalue $0$ equals the number of connected components.

## Fiedler value and vector
✎ $\lambda_2$ (the circled heart) is the **Fiedler value**. Its eigenvector is the **Fiedler vector**, and ✎ it "shows you where to make the cut".
$$
\boxed{\,\lambda_2 = \min_{x \perp \ones,\ x \ne 0} \frac{x^{\top}L_G\,x}{x^{\top}x}\,}
$$
The minimizer puts neighbours at close values, so a big jump in the sorted Fiedler entries marks the sparse part of the graph.
A long path hanging by one edge can pull the Fiedler vector onto itself. [Regularized Spectral Clustering](Regularized%20Spectral%20Clustering.md) fixes this ([EX08 - Whisker Cut Versus Regularized Clustering](../Examples/EX08%20-%20Whisker%20Cut%20Versus%20Regularized%20Clustering.md)).

## Examples
- [EX06 - Matrices and Spectrum of the Path P3](../Examples/EX06%20-%20Matrices%20and%20Spectrum%20of%20the%20Path%20P3.md)
- [EX07 - Sweep Cut on Two Joined Triangles](../Examples/EX07%20-%20Sweep%20Cut%20on%20Two%20Joined%20Triangles.md)

See also: [Laplacian of a Graph](Laplacian%20of%20a%20Graph.md), [Sparsest Cut](Sparsest%20Cut.md), [Spectral Clustering Algorithm](Spectral%20Clustering%20Algorithm.md)
