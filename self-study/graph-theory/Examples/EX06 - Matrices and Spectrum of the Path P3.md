---
tags: [graph-theory, example, spectral-graph-theory]
source: Constructed from the "Graphs" and "Laplacian of graph G" columns of my handwritten notes
topics: ["[[Degree and Adjacency Matrices]]", "[[Laplacian of a Graph]]", "[[Spectral Gap and Fiedler Vector]]"]
---
# EX06 — Matrices and Spectrum of the Path $P_3$
Back to [Index](../Index.md)

> [!question] Problem
> Let $G = P_3$, with edges $12$ and $23$.
> (a) Write $D$, $A$, and $L = D - A$. Check the row sums and the quadratic form.
> (b) Find the eigenvalues of $A$ and of $L$, and the Fiedler vector.
> (c) Add an isolated vertex $4$. What happens to $\lambda_2$?

## Solution
**(a)**
$$
D = \begin{bmatrix} 1&0&0\\0&2&0\\0&0&1 \end{bmatrix}, \quad
A = \begin{bmatrix} 0&1&0\\1&0&1\\0&1&0 \end{bmatrix}, \quad
L = \begin{bmatrix} 1&-1&0\\-1&2&-1\\0&-1&1 \end{bmatrix}.
$$
Every row of $L$ sums to $0$, and $x^{\top}Lx = (x_1 - x_2)^2 + (x_2 - x_3)^2 \ge 0$.

**(b)** Eigenvalues:

| Matrix | Eigenvalues |
|---|---|
| $A$ | $-\sqrt2,\ 0,\ \sqrt2$ |
| $L$ | $0,\ 1,\ 3$ |

- $A$ has a negative eigenvalue, so it is not PSD.
- $\lambda_{\max}(A) = \sqrt2 \approx 1.41$ lies between the average degree $4/3$ and $\Delta(G) = 2$. $P_3$ is not regular, so the inequalities are strict.
- $\lambda_2(L) = 1 > 0$, so $G$ is connected.

The Fiedler vector is $\tfrac{1}{\sqrt2}(-1, 0, 1)$. Sorting puts vertex $1$ first and vertex $3$ last, so the sweep cuts beside the middle vertex.

**(c)** The new graph has two components, so $0$ has multiplicity $2$ and $\boxed{\lambda_2 = 0}$. The eigenvector for the extra $0$ is constant on each component.

## Takeaways
- The Laplacian's spectrum is always $\ge 0$. The adjacency spectrum is not.
- $\lambda_2 = 0$ is the algebraic test for "disconnected".

## Related topics
- [Degree and Adjacency Matrices](../Theory/Degree%20and%20Adjacency%20Matrices.md)
- [Laplacian of a Graph](../Theory/Laplacian%20of%20a%20Graph.md)
- [Spectral Gap and Fiedler Vector](../Theory/Spectral%20Gap%20and%20Fiedler%20Vector.md)
