---
tags: [convex-optimization, topic, ml-notebook]
source: ML notebook "Maximum Likelihood Estimation"; Boyd & Vandenberghe §7.1 (preview)
---
# Maximum Likelihood Estimation
Back to [[self-study/convex-optimization/Index|Index]] · ML notebook

## Model
$$
y_i = w^{\top}x_i + \epsilon_i, \qquad \epsilon_i \sim \Normal(0, \sigma^2)
$$
$$
p(y_i \mid x_i, w) = \frac{1}{\sqrt{2\pi\sigma^2}}\exp\!\left(-\frac{(y_i - w^{\top}x_i)^2}{2\sigma^2}\right)
$$

## Likelihood
With independent data points the likelihood is a product, and the log turns it into a sum:
$$
\log L(w) = \sum_{i=1}^{n}\left[-\tfrac12\log(2\pi\sigma^2) - \frac{(y_i - w^{\top}x_i)^2}{2\sigma^2}\right]
$$
$$
\boxed{\,\log L(w) = \text{const} - \frac{1}{2\sigma^2}\sum_{i=1}^{n}(y_i - w^{\top}x_i)^2\,}
$$
**Maximizing likelihood = minimizing squared error.** Gaussian MLE is least-squares.

## Convexity link
$-\log L$ is convex in $w$ whenever the noise density is **log-concave** (Gaussian, Laplacian, uniform). Laplacian noise gives $\ell_1$ regression instead.

## Explorations
- [[EX09 - Gaussian MLE Equals Least Squares]]

See also: [[Log-Concave and Log-Convex Functions]], [[Least Squares by Gradient Descent]]
