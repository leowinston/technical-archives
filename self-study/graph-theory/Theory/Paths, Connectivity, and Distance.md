---
tags: [graph-theory, theory, ch-1]
source: Kelly, Graph Theory §1.1.4–1.1.5 (pp. 5–8)
---
# Paths, Connectivity, and Distance
Back to [Index](../Index.md) · Sections 1.1.4–1.1.5

## Paths
A **$uv$ path** is a sequence $x_1 \dots x_l$ of **distinct** vertices with $x_1 = u$, $x_l = v$, and $x_i x_{i+1} \in E$.
✎ To check $u x_1 x_2 v$: $x_1 \in N(u)$, $x_2 \in N(x_1)$, $v \in N(x_2)$.

## Joining paths (✎ "transitive nature")
A $uv$ path followed by a $vw$ path **contains** a $uw$ path. Take the shortest subsequence from $u$ to $w$ whose consecutive vertices are adjacent. A repeated vertex $z$ would let you ✎ **short-circuit** the loop $z \dots z$, which contradicts minimality. Worked in [EX01 - Short-Circuiting a Joined Path](../Examples/EX01%20-%20Short-Circuiting%20a%20Joined%20Path.md).

## Components
$x \sim y \iff$ there is an $xy$ path. It is reflexive and symmetric, and it is transitive by joining paths, so $\sim$ is an equivalence relation. Its classes are the **connected components**.
✎ $G$ is **connected** if $u \sim v$ for all $u, v \in V$.

## Distance
$d(x, y)$ is the fewest edges on an $xy$ path, and $\infty$ if there is none. ✎ $d(x, y) = 2$ for $x - z - y$. $d(x, y) = \infty$ across two components.
On a connected graph, $(V, d)$ is a **metric space**:
$$
d(x, y) = 0 \iff x = y, \qquad d(x, y) = d(y, x), \qquad d(x, z) \le d(x, y) + d(y, z).
$$
✎ My correction: $d$ takes a **pair** of vertices, $d : V \times V \to \R_{\ge 0} \cup \{\infty\}$. It is not a function of $V$ alone.

See also: [Trees and Leaves](Trees%20and%20Leaves.md), [Neighbourhood, Degree, and Regularity](Neighbourhood%2C%20Degree%2C%20and%20Regularity.md)
