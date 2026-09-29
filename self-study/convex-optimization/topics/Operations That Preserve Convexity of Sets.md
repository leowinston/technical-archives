---
tags: [convex-optimization, topic, ch-2]
source: Boyd & Vandenberghe §2.3 (pp. 35–43)
---
# Operations That Preserve Convexity of Sets
Back to [[self-study/convex-optimization/Index|Index]] · Section 2.3

To show $C$ is convex, build it from simple convex sets with these operations.

| Operation | Result |
|---|---|
| intersection $\bigcap_\alpha S_\alpha$ | convex (even infinitely many) |
| affine image $f(S) = \{Ax + b \mid x \in S\}$ | convex |
| affine preimage $f^{-1}(S)$ | convex |
| perspective $P(z, t) = z/t$, $t > 0$ | convex |
| linear-fractional $\dfrac{Ax + b}{c^{\top}x + d}$ | convex |

## Example
$\Spsd{n} = \bigcap_{z \ne 0} \{X \in \Sym{n} \mid z^{\top}Xz \ge 0\}$ is an intersection of halfspaces, so it is convex.

Projection, scaling, translation, and sums $S_1 + S_2$ are all special affine maps.

See also: [[Operations That Preserve Convexity of Functions]], [[Important Convex Sets]]
