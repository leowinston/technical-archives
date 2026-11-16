---
tags: [math-315, topic, lecture-3, appendix-b]
---
# Norm of an Orthogonal Matrix
Back to [Index](../Index.md) · Appendix B.13.2

**Claim.** If $Q \in \mathbb{R}^{n \times n}$ and $Q^{\top}Q = QQ^{\top} = I$, then $\|Q\|_2 = 1$.

## Proof
Let $\langle \mathbf{u}, \mathbf{v}\rangle = \mathbf{u}^{\top}\mathbf{v}$, so $\|\mathbf{x}\| = \sqrt{\langle \mathbf{x}, \mathbf{x}\rangle}$. For any $\mathbf{x} \in \mathbb{R}^n$,
$$
\|Q\mathbf{x}\|^2 = (Q\mathbf{x})^{\top}Q\mathbf{x} = \mathbf{x}^{\top}Q^{\top}Q\,\mathbf{x} = \mathbf{x}^{\top}\mathbf{x} = \|\mathbf{x}\|^2
$$
Hence $Q$ preserves length, and the scaling factor is $1$ for every $\mathbf{x} \neq \mathbf{0}$:
$$
\|Q\| = \max_{\mathbf{x} \neq \mathbf{0}} \frac{\|Q\mathbf{x}\|}{\|\mathbf{x}\|} = \max_{\mathbf{x} \neq \mathbf{0}} 1 = 1 \qquad \blacksquare
$$

## The norm must be the 2-norm
For the rotation $R_\theta = \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$, the column and row sums are both $|\cos\theta| + |\sin\theta|$:
$$
\|R_\theta\|_1 = \|R_\theta\|_\infty = |\cos\theta| + |\sin\theta| \in [1, \sqrt2], \qquad \|R_{\pi/4}\|_1 = \sqrt2 \neq 1
$$
Also $\|Q\|_F = \sqrt n$. Only $\|\cdot\|_2$ gives $1$ for every orthogonal $Q$.

## Explorations
- [EX23 - Orthogonal Matrices Have 2-Norm 1](../Explorations%201/EX23%20-%20Orthogonal%20Matrices%20Have%202-Norm%201.md)

See also: [Matrix Norms](Matrix%20Norms.md), [Vector Norms](Vector%20Norms.md), [QR Factorization](QR%20Factorization.md)
