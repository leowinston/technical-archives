---
tags: [convex-optimization, topic, ch-3]
source: Boyd & Vandenberghe §3.1.3 (pp. 69–70)
---
# First-Order Condition
Back to [Index](../Index.md) · Section 3.1.3

For differentiable $f$ with convex $\dom f$:
$$
\boxed{\,f \text{ convex} \iff f(y) \ge f(x) + \nabla f(x)^{\top}(y - x) \ \ \forall x, y \in \dom f\,}
$$
The first-order Taylor approximation is a **global underestimator**.

## Why it matters
Local information (the gradient at one point) gives a **global** bound. In particular
$$
\nabla f(x) = 0 \ \Rightarrow\ f(y) \ge f(x) \ \ \forall y,
$$
so any stationary point is a global minimizer.

## Geometry
$(\nabla f(x), -1)$ defines a supporting hyperplane to $\epi f$ at $(x, f(x))$.

```desmos-graph
left=-2; right=3; top=8; bottom=-2
---
y=e^{x}|#2d70b3
y=e^{1}+e^{1}(x-1)|dashed|#c74440
(1,e^{1})|#c74440
```

See also: [Convex Functions](Convex%20Functions.md), [Optimality Criterion for Differentiable Objectives](Optimality%20Criterion%20for%20Differentiable%20Objectives.md), [Separating and Supporting Hyperplanes](Separating%20and%20Supporting%20Hyperplanes.md)
