---
tags: [convex-optimization, topic, ch-4]
source: Boyd & Vandenberghe §4.1 (pp. 127–136)
---
# Optimization Problems in Standard Form
Back to [[self-study/convex-optimization/Index|Index]] · Section 4.1

## Standard form
$$
\begin{array}{ll}
\text{minimize} & f_0(x) \\
\text{subject to} & f_i(x) \le 0, \quad i = 1, \dots, m \\
& h_i(x) = 0, \quad i = 1, \dots, p
\end{array}
$$
- **Optimal value:** $p^\star = \inf\{f_0(x) \mid x \text{ feasible}\}$, with $p^\star = \infty$ if infeasible and $-\infty$ if unbounded below.
- **Locally optimal:** $x$ minimizes $f_0$ over feasible $z$ with $\lVert z - x\rVert_2 \le R$.
- **Active constraint:** $f_i(x) = 0$ at a feasible $x$.

## Equivalent problems
Two problems are **equivalent** if a solution of one gives a solution of the other. Standard tricks:
- **Change of variables** $x = \phi(z)$.
- **Slack variables:** $f_i(x) \le 0 \iff f_i(x) + s_i = 0,\ s_i \ge 0$.
- **Epigraph form:** minimize $t$ subject to $f_0(x) - t \le 0$ and the original constraints. The objective becomes linear.

## Feasibility problem
Set $f_0 = 0$. Then $p^\star = 0$ if feasible and $\infty$ otherwise.

See also: [[Convex Optimization Problems]]
