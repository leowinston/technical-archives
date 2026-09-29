---
tags: [math-315, exploration, lecture-3]
source: Constructed example for Section 3.3 (QR Factorization)
topics: ["[[QR Factorization]]"]
---
# EX09 — QR Factorization and Solve of a 2×2 System
Back to [[academic/math-315/Index|Index]]

> [!question] Problem
> Let $A = \begin{bmatrix} 3 & 0 \\ 4 & 5 \end{bmatrix}$ and $\mathbf{b} = \begin{bmatrix} 3 \\ 9 \end{bmatrix}$.
> (a) Compute $A = QR$ by Gram–Schmidt.
> (b) Verify that $Q$ is orthogonal and that it preserves length.
> (c) Solve $A\mathbf{x} = \mathbf{b}$ using $R\mathbf{x} = Q^{\top}\mathbf{b}$.

## Setup
- **Columns:** $\mathbf{a}_1 = (3, 4)^{\top}$, $\mathbf{a}_2 = (0, 5)^{\top}$, linearly independent ($\det A = 15$)
- **Goal:** orthonormal $\mathbf{q}_1, \mathbf{q}_2$ and upper triangular $R$ with $\mathbf{a}_j = \sum_{i \le j} r_{ij}\mathbf{q}_i$

## Strategy
1. Normalize $\mathbf{a}_1$ to get $\mathbf{q}_1$ and $r_{11}$.
2. Remove the $\mathbf{q}_1$ component from $\mathbf{a}_2$ to get $r_{12}$, then normalize what's left to get $\mathbf{q}_2$ and $r_{22}$.
3. Solve with $Q^{\top}$ and back substitution.

## Solution
**Why the formulas work.** Column $j$ of $A = QR$ reads $\mathbf{a}_j = r_{1j}\mathbf{q}_1 + \cdots + r_{jj}\mathbf{q}_j$. Dot both sides with $\mathbf{q}_i$ and use $\mathbf{q}_i^{\top}\mathbf{q}_k = \delta_{ik}$:
$$
\mathbf{q}_i^{\top}\mathbf{a}_j = r_{ij}
$$

**(a) Gram–Schmidt**

*Column 1:*
$$
r_{11} = \|\mathbf{a}_1\|_2 = \sqrt{9 + 16} = 5, \qquad
\mathbf{q}_1 = \frac{\mathbf{a}_1}{5} = \begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix}
$$

*Column 2:*
$$
\begin{align*}
r_{12} &= \mathbf{q}_1^{\top}\mathbf{a}_2 = 0.6(0) + 0.8(5) = 4 \\
\mathbf{v}_2 &= \mathbf{a}_2 - r_{12}\mathbf{q}_1 = \begin{bmatrix} 0 \\ 5 \end{bmatrix} - 4\begin{bmatrix} 0.6 \\ 0.8 \end{bmatrix} = \begin{bmatrix} -2.4 \\ 1.8 \end{bmatrix} \\
r_{22} &= \|\mathbf{v}_2\|_2 = \sqrt{5.76 + 3.24} = \sqrt{9} = 3 \\
\mathbf{q}_2 &= \frac{\mathbf{v}_2}{3} = \begin{bmatrix} -0.8 \\ 0.6 \end{bmatrix}
\end{align*}
$$
$$
\boxed{\,Q = \begin{bmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{bmatrix}, \qquad R = \begin{bmatrix} 5 & 4 \\ 0 & 3 \end{bmatrix}\,}
$$

**Check $QR = A$:**
$$
\begin{align*}
\text{col 1} &= 5\,\mathbf{q}_1 = (3, 4) \quad\checkmark \\
\text{col 2} &= 4\,\mathbf{q}_1 + 3\,\mathbf{q}_2 = (2.4 - 2.4,\ 3.2 + 1.8) = (0, 5) \quad\checkmark
\end{align*}
$$

**(b) $Q$ is orthogonal**
$$
Q^{\top}Q = \begin{bmatrix} 0.6 & 0.8 \\ -0.8 & 0.6 \end{bmatrix}\begin{bmatrix} 0.6 & -0.8 \\ 0.8 & 0.6 \end{bmatrix}
= \begin{bmatrix} 0.36 + 0.64 & -0.48 + 0.48 \\ -0.48 + 0.48 & 0.64 + 0.36 \end{bmatrix} = I \quad\checkmark
$$
$Q$ is a rotation by $\theta$ with $\cos\theta = 0.6$ and $\sin\theta = 0.8$, and $\det Q = 0.36 + 0.64 = 1$.

**Length preservation**, general argument and a numeric check with $\mathbf{x} = (1, 1)$:
$$
\|Q\mathbf{x}\|_2^2 = \mathbf{x}^{\top}Q^{\top}Q\mathbf{x} = \mathbf{x}^{\top}\mathbf{x}; \qquad
Q\begin{bmatrix} 1 \\ 1 \end{bmatrix} = \begin{bmatrix} -0.2 \\ 1.4 \end{bmatrix}, \quad
0.04 + 1.96 = 2 = 1^2 + 1^2 \quad\checkmark
$$
So $\|Q\|_2 = 1$, $\|Q^{-1}\|_2 = \|Q^{\top}\|_2 = 1$, and $\kappa_2(Q) = 1$.

**(c) Solve**
$$
A\mathbf{x} = \mathbf{b} \iff QR\mathbf{x} = \mathbf{b} \iff R\mathbf{x} = Q^{\top}\mathbf{b}
$$
$$
\mathbf{y} = Q^{\top}\mathbf{b} = \begin{bmatrix} 0.6(3) + 0.8(9) \\ -0.8(3) + 0.6(9) \end{bmatrix} = \begin{bmatrix} 9 \\ 3 \end{bmatrix}
$$
Back substitution on $\begin{bmatrix} 5 & 4 \\ 0 & 3 \end{bmatrix}\mathbf{x} = \begin{bmatrix} 9 \\ 3 \end{bmatrix}$:
$$
x_2 = \frac{3}{3} = 1, \qquad x_1 = \frac{9 - 4(1)}{5} = 1
$$
$$
\boxed{\,\mathbf{x} = (1, 1)^{\top}\,}
$$
Check: $A\mathbf{x} = (3, 4 + 5) = (3, 9)$. $\checkmark$

```
# solve A x = b via QR
Q, R = qr(A)
y = transpose(Q) * b          # O(n^2), no error growth since kappa(Q) = 1
x = back_substitute(R, y)     # O(n^2)
```

## Comparison with LU on the same matrix
$$
m_{21} = \frac43, \qquad A = \begin{bmatrix} 1 & 0 \\ \tfrac43 & 1 \end{bmatrix}\begin{bmatrix} 3 & 0 \\ 0 & 5 \end{bmatrix}
$$
Both factorizations work here. QR costs about twice as much ($\tfrac43n^3$ against $\tfrac23n^3$). In exchange it never amplifies errors through $Q$, and it extends to non-square least-squares problems.

## Takeaways
- $r_{ij} = \mathbf{q}_i^{\top}\mathbf{a}_j$ comes straight from orthonormality.
- Solving with QR is "multiply by $Q^{\top}$, then back substitute".
- By hand Gram–Schmidt is fine. Software uses Householder reflections, which stay orthogonal in floating point.

## Related topics
- [[QR Factorization]]
- [[Singular Value Decomposition]]
- [[Condition Number]]
