---
tags: [convex-optimization, topic, ml-notebook, background]
source: ML notebook "Spectral Graph Theory + Multivariable Review"; Boyd & Vandenberghe App. A.4
---
# Gradient, Jacobian, and Hessian
Back to [[self-study/convex-optimization/Index|Index]] · ML notebook

| Object | Map | Entries |
|---|---|---|
| gradient $\nabla f$ | $f : \R^n \to \R$ gives $\R^n$ | $\partial f / \partial x_i$ |
| Jacobian $J$ | $f : \R^n \to \R^m$ gives $\R^{m \times n}$ | $\partial f_i / \partial x_j$ |
| Hessian $\nabla^2 f$ | $f : \R^n \to \R$ gives $\R^{n \times n}$ | $\partial^2 f / \partial x_i \partial x_j$ |
| Laplacian $\Delta f$ | $f : \R^n \to \R$ gives $\R$ | $\sum_i \partial^2 f / \partial x_i^2$ |

## Relations
$$
\nabla^2 f(x) = J\big(\nabla f(x)\big)^{\top}, \qquad \Delta f = \nabla^2 \!\cdot f = \tr\big(\nabla^2 f\big).
$$
The Hessian holds **all** second partials (mixed ones included). The Laplacian keeps only the **unmixed** ones.

## Gradient rules used in the notes
$$
\nabla_w (w^{\top}Aw) = 2Aw \ \ (A \text{ symmetric}), \qquad \nabla_w (b^{\top}w) = b.
$$

## Taylor
$$
f(x + v) \approx f(x) + \nabla f(x)^{\top}v + \tfrac12 v^{\top}\nabla^2 f(x)\,v
$$
The sign of the quadratic term is what [[Second-Order Conditions]] checks.

See also: [[Least Squares by Gradient Descent]], [[Graph Laplacian]]
