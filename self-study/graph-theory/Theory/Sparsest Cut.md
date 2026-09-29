---
tags: [graph-theory, theory, spectral-graph-theory]
source: Handwritten notes "Sparsest Cut" / "Thm ①"
---
# Sparsest Cut
Back to [[self-study/graph-theory/Index|Index]] · Handwritten notes

$$
\phi_G = \min_{\emptyset \ne A \subsetneq V} \phi(A, V - A)
$$
A cut with density $\phi_G$ is a **sparsest cut** of $G$ (see [[Cuts and Cut Density]]).

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

See also: [[Spectral Gap and Fiedler Vector]], [[Spectral Clustering Algorithm]], [[Regularized Spectral Clustering]] (a modified objective that ignores dangling trees), [[Sparsest Cut as a Spectral Relaxation]] (convex opt: relaxation view, concavity of $\lambda_2$)
