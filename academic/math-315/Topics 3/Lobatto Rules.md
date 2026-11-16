---
tags: [math-315, topic, chapter-5]
---
# Lobatto Rules
Back to [Index](../Index.md) · Section 5.2.4 (textbook)

Lobatto rules are the closed relatives of [Gauss rules](Gauss%20Rules.md): both endpoints $\pm1$ are always points, and the interior points and all weights are chosen to maximize the DOP.
$$
\int_{-1}^{1}f\,dx \approx w_0f(-1) + \sum_{i=1}^{N-1}w_if(x_i) + w_Nf(1)
$$

## Properties of the $(N+1)$-point rule
- All weights are positive, the interior points lie in $(-1, 1)$, and everything is symmetric.
- $2N$ unknowns give $\boxed{\,\text{DOP} = 2N - 1\,}$.

## Small rules
| Points | Interior nodes | Weights | DOP |
|---|---|---|---|
| 3 | $0$ | $\tfrac13, \tfrac43, \tfrac13$ ([Simpson](Simpson%27s%20Rule.md)) | 3 |
| 4 | $\pm\tfrac1{\sqrt5}$ | $\tfrac16, \tfrac56, \tfrac56, \tfrac16$ | 5 |
| 5 | $0, \pm\sqrt{3/7}$ | $\tfrac1{10}, \tfrac{49}{90}, \tfrac{32}{45}, \tfrac{49}{90}, \tfrac1{10}$ | 7 |

The 4-point Lobatto rule is not Weddle's rule: Weddle fixes equally spaced points and only reaches DOP $3$.

## Gauss versus Lobatto
| | Gauss | Lobatto |
|---|---|---|
| Same DOP | $N$ points | $N + 1$ points |
| Endpoint values | never used | shared with the next subinterval, so about the same cost |
| Peano constant | smaller (Gauss 2-point $\tfrac1{135}$) | larger (Simpson $\tfrac1{90}$) |
| Endpoint singularity | works | fails immediately |

## Explorations
- [EX46 - Four-Point Lobatto Rule](../Explorations%203/EX46%20-%20Four-Point%20Lobatto%20Rule.md)

See also: [Gauss Rules](Gauss%20Rules.md), [Adaptive Integration](Adaptive%20Integration.md), [Improper Integrals](Improper%20Integrals.md)
