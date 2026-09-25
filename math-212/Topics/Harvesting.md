---
tags: [math-212, topic, chapter-2, population-model]
---
# Harvesting
Back to [[Index]] · Chapter 2.5 · [[Autonomous Equations and Phase Lines]]

## Schaefer model (effort harvesting)
$$
\frac{dy}{dt} = r\left(1 - \frac{y}{K}\right)y - Ey
$$
- Equilibria are $y_1 = 0$ and $y_2 = K\left(1 - \dfrac{E}{r}\right)$. When $E < r$, $y_2$ is stable.
- The sustainable yield is $Y = Ey_2 = KE\left(1 - \dfrac{E}{r}\right)$. It is largest at $E = r/2$, giving $Y_{\max} = rK/4$.

## Constant-yield harvesting
$$
\frac{dy}{dt} = r\left(1 - \frac{y}{K}\right)y - h
$$
If $h > rK/4$, there are no equilibria and the population collapses (see [[Bifurcations|saddle-node bifurcation]]).
