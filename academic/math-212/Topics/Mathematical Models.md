---
tags: [math-212, topic, chapter-1]
---
# Mathematical Models
Back to [[academic/math-212/Index|Index]] · Chapter 1.1

A differential equation relates an unknown quantity to its rate of change. Modeling means translating a physical law into that relationship.

## Classical models

| Phenomenon                  | Equation                                               | Notes                                          |
| --------------------------- | ------------------------------------------------------ | ---------------------------------------------- |
| Radioactive decay           | $\dfrac{dQ}{dt} = -rQ$                                 | $r > 0$, half-life $\tau$ with $r\tau = \ln 2$ |
| Newton's law of cooling     | $\dfrac{du}{dt} = -k(u - T)$                           | $T$ ambient temperature, $k > 0$               |
| RC circuit                  | $R\dfrac{dQ}{dt} + \dfrac{1}{C}Q = V$                  | $R$ resistance, $C$ capacitance                |
| Pendulum (nonlinear)        | $\dfrac{d^2\theta}{dt^2} + \dfrac{g}{L}\sin\theta = 0$ | nonlinear because of $\sin\theta$              |
| Pendulum (linearized)       | $\dfrac{d^2\theta}{dt^2} + \dfrac{g}{L}\theta = 0$     | valid for small $\theta$                       |
| Motion with linear friction | $\dfrac{dv}{dt} = -kv$                                 | velocity decays exponentially                  |

## Kinematics
$$
\begin{align*}
v &= \frac{dx}{dt}, & a &= \frac{dv}{dt} = \frac{d^2x}{dt^2}
\end{align*}
$$

## Workbook problems
- [[WB1 P01 - Car Slowing Down to a Stop]]

See also: [[Modeling with First-Order Equations]]
