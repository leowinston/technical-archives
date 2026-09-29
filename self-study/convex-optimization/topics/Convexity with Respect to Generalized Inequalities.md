---
tags: [convex-optimization, topic, ch-3]
source: Boyd & Vandenberghe §3.6 (pp. 108–112)
---
# Convexity with Respect to Generalized Inequalities
Back to [[self-study/convex-optimization/Index|Index]] · Section 3.6

## $K$-convexity
$f : \R^n \to \R^m$ is **$K$-convex** for a proper cone $K \subseteq \R^m$ if
$$
f(\theta x + (1-\theta)y) \preceq_K \theta f(x) + (1-\theta) f(y).
$$

## Matrix convexity
With $K = \Spsd{m}$: $f$ is matrix convex iff $z^{\top}f(x)z$ is convex for every $z$.
- $X \mapsto XX^{\top}$ is matrix convex.
- $X \mapsto X^{p}$ on $\Spd{n}$ is matrix convex for $1 \le p \le 2$ or $-1 \le p \le 0$.

## Monotonicity
$f$ is **$K$-nondecreasing** if $x \preceq_K y \Rightarrow f(x) \le f(y)$. Example: $\tr(WX)$ is $\Spsd{n}$-nondecreasing when $W \succeq 0$.

For differentiable $f$ with convex domain, $f$ is $K$-nondecreasing iff $\nabla f(x) \succeq_{K^{*}} 0$.

See also: [[Generalized Inequalities and Minimal Elements]], [[Dual Cones]]
