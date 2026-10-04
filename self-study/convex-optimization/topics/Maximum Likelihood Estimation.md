---
tags: [convex-optimization, topic, ml-notebook]
source: ML notebook "Maximum Likelihood Estimation"; Boyd & Vandenberghe §7.1 (preview)
---
# Maximum Likelihood Estimation
Back to [Index](../Index.md) · ML notebook

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
- [EX09 - Gaussian MLE Equals Least Squares](../explorations/EX09%20-%20Gaussian%20MLE%20Equals%20Least%20Squares.md)

See also: [Log-Concave and Log-Convex Functions](Log-Concave%20and%20Log-Convex%20Functions.md), [Least Squares by Gradient Descent](Least%20Squares%20by%20Gradient%20Descent.md)
