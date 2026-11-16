---
tags: [math-315, topic, chapter-5]
---
# Improper Integrals
Back to [Index](../Index.md) · Section 5.3.2 (textbook)

An integral is improper if a limit is $\pm\infty$ or $f$ is singular somewhere in $[a, b]$.

## Endpoint singularity
Example $\int_0^1x^{-1/2}\,dx = 2$. Open rules ([Gauss](Gauss%20Rules.md)) never evaluate the endpoint, so adaptive codes cope, after many bisections near the singularity. Closed rules ([Lobatto](Lobatto%20Rules.md)) fail at once. To speed things up, integrate a Taylor series near the singularity:
$$
\int_0^1\frac{\cos x}{\sqrt x}dx \approx \int_0^\delta\frac{1 - x^2/2}{\sqrt x}dx + \int_\delta^1\frac{\cos x}{\sqrt x}dx
$$

## Interior singularity
If a quadrature point lands on it, the code returns `nan`. **Split the interval at the singularity** so it becomes an endpoint. For example, `quad(lambda x: np.sin(x)/x, -1, 1)` returns `nan`, because $0$ is a node, but splitting at $0$ gives $1.892166\ldots$.

## Infinite limits
- Substitute $x = 1/t$ to get a finite interval:
$$
\int_1^\infty\frac{x^3}{x^5 + 2}dx = \int_0^1\frac{dt}{1 + 2t^5}
$$
- **Do not** just truncate at a large $B$; the tail decays slowly.
- Or **subtract out** the slow part: $\frac{x^3}{x^5+2} = \frac1{x^2} - \frac{2}{x^2(x^5+2)}$. The remainder decays like $x^{-7}$.

## In Python
`quad` accepts `np.inf` limits and does the substitution itself. `points=[c]` marks a known interior trouble spot (finite limits only).

## Explorations
- [EX50 - An Infinite Integral by Substitution and Subtracting Out](../Explorations%203/EX50%20-%20An%20Infinite%20Integral%20by%20Substitution%20and%20Subtracting%20Out.md)
- [EX51 - Singular Integrands sin x over x and cos x over sqrt x](../Explorations%203/EX51%20-%20Singular%20Integrands%20sin%20x%20over%20x%20and%20cos%20x%20over%20sqrt%20x.md)

See also: [Adaptive Integration](Adaptive%20Integration.md), [Gauss Rules](Gauss%20Rules.md)
