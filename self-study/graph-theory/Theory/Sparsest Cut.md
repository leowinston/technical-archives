---
tags: [graph-theory, theory, spectral-graph-theory]
source: Handwritten notes "Sparsest Cut" / "Thm ①"
---
# Sparsest Cut
Back to [Index](../Index.md) · Handwritten notes

$$
\phi_G = \min_{\emptyset \ne A \subsetneq V} \phi(A, V - A)
$$
A cut with density $\phi_G$ is a **sparsest cut** of $G$ (see [Cuts and Cut Density](Cuts%20and%20Cut%20Density.md)).

## Hardness
Brute force checks every subset in the power set: $\card{\mathcal{P}(V)} = 2^n$ ✎ ☹ bad. The problem is NP-hard. ✎ "⇒ Approximations are awesome."

## Spectral lower bound
$$
\boxed{\,\phi_G \ge \lambda_2\,}
$$
Key step: for a cut $(A, B)$, plug the centered indicator $x = \ones_A - \tfrac{\card{A}}{n}\ones$ into the Rayleigh quotient. Then $x \perp \ones$, and
$$
x^{\top}L_Gx = \card{E(A, B)}, \qquad x^{\top}x = \frac{\card{A}\card{B}}{n},
$$
so $\lambda_2 \le \frac{x^{\top}L_Gx}{x^{\top}x} = \phi(A, B)$. Minimizing over $A$ gives the bound.

See also: [Spectral Gap and Fiedler Vector](Spectral%20Gap%20and%20Fiedler%20Vector.md), [Spectral Clustering Algorithm](Spectral%20Clustering%20Algorithm.md), [Regularized Spectral Clustering](Regularized%20Spectral%20Clustering.md) (a modified objective that ignores dangling trees), [Sparsest Cut as a Spectral Relaxation](../../convex-optimization/topics/Sparsest%20Cut%20as%20a%20Spectral%20Relaxation.md) (convex opt: relaxation view, concavity of $\lambda_2$)
