---
tags: [graph-theory, theory, spectral-graph-theory]
source: Amini et al. (2013); Qin & Rohe (2013); Zhang & Rohe (2018). Beyond my handwritten notes
---
# Regularized Spectral Clustering
Back to [Index](../Index.md) · Extension of the handwritten notes

## Vanilla vs regularized
| | Vanilla ([Spectral Clustering Algorithm](Spectral%20Clustering%20Algorithm.md)) | Regularized |
|---|---|---|
| Graph | $A$ | $A_\tau = A + \tfrac{\tau}{n}J$ (a faint $K_n$ added), $\tau \approx$ average degree |
| Degrees | $D$ | $D_\tau = D + \tau I$ |
| Matrix | $L_G = D - A$ | $\mathcal L_\tau = I - D_\tau^{-1/2}A_\tau D_\tau^{-1/2}$ |
| Vector used | Fiedler vector $v_2$ | $D_\tau^{-1/2}v_2$ |
| Weak spot | long dangling paths and trees | $\tau$ too large washes out real structure |

## The ridge term
Substitute $y = D_\tau^{1/2}x$ into the Rayleigh quotient:
$$
\boxed{\,\lambda_2(\mathcal L_\tau) = \min_{\sum_i (d_i + \tau)x_i = 0} \frac{\sum_{E}(x_i - x_j)^2 + \tau\sum_i (x_i - \bar x)^2}{\sum_i (d_i + \tau)\,x_i^2}\,}
$$
The new term $\tau\sum_i(x_i - \bar x)^2$ is a ridge penalty. For the indicator of a $k$-vertex set it adds $\tau k(n-k)/n \approx \tau k$ to the cut cost. So any piece of the graph hanging by one edge now pays for every vertex it contains, and stops looking like a cheap cut.

## Why vanilla gets fooled
A path $P_k$ hanging by one edge is a tree whose far end is a leaf. It is cut by a single edge, and its own $\lambda_2$ is tiny ($\approx \pi^2/k^2$), so the Fiedler vector concentrates on it. Normalizing by $D$ alone does not fix this, because the path's low degrees make $D^{-1/2}$ large there.

## Normalization is essential
For the unnormalized Laplacian, $L(A_\tau) = L_G + \tau\big(I - \tfrac1n J\big)$. On $\ones^{\perp}$ this adds exactly $\tau$ to every eigenvalue and leaves the eigenvectors unchanged. The regularization has an effect only through dividing by $D_\tau$.

## Examples
- [EX08 - Whisker Cut Versus Regularized Clustering](../Examples/EX08%20-%20Whisker%20Cut%20Versus%20Regularized%20Clustering.md)

See also: [Laplacian of a Graph](Laplacian%20of%20a%20Graph.md), [Spectral Gap and Fiedler Vector](Spectral%20Gap%20and%20Fiedler%20Vector.md), [Cuts and Cut Density](Cuts%20and%20Cut%20Density.md), [Sparsest Cut](Sparsest%20Cut.md), [Trees and Leaves](Trees%20and%20Leaves.md), [Bias-Variance Tradeoff](../../convex-optimization/topics/Bias-Variance%20Tradeoff.md) (convex opt: the same ridge penalty), [Sparsest Cut as a Spectral Relaxation](../../convex-optimization/topics/Sparsest%20Cut%20as%20a%20Spectral%20Relaxation.md) (convex opt)
