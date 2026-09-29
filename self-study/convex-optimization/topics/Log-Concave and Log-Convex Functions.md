---
tags: [convex-optimization, topic, ch-3]
source: Boyd & Vandenberghe §3.5 (pp. 104–108)
---
# Log-Concave and Log-Convex Functions
Back to [[self-study/convex-optimization/Index|Index]] · Section 3.5

## Definition
$f > 0$ is **log-concave** if $\log f$ is concave:
$$
f(\theta x + (1-\theta)y) \ge f(x)^{\theta} f(y)^{1-\theta}.
$$

## Examples
- The Gaussian density $\propto e^{-\frac12(x-\mu)^{\top}\Sigma^{-1}(x-\mu)}$ is log-concave.
- The Gaussian CDF $\Phi$ and $\det X$ on $\Spd{n}$ are log-concave.
- Most common densities (uniform on convex sets, exponential, Wishart) are log-concave.

## Properties
- Products of log-concave functions are log-concave. Sums need not be.
- If $f(x, y)$ is log-concave, the marginal $\int f(x, y)\,dy$ is log-concave.
- Convolutions of log-concave functions are log-concave.

## Why it matters
If the noise density is log-concave, then **maximizing the log-likelihood is a convex problem**.

See also: [[Maximum Likelihood Estimation]], [[Examples of Convex Functions]]
