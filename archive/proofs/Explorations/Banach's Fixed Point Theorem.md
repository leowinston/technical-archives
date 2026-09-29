---
tags: [proof, exploration, draft]
date: 2026-04
---
# Banach's Fixed Point Theorem
Back to [[archive/proofs/Index|Index]]

Leo Winston · April 2026

> [!note] Unfinished draft
> Transcribed as written. The second `align*` block and the last sentence ("By definition") stop mid-thought in the original TeX.

*Proof.* Let $f: X \rightarrow X$ be a contraction, where $X$ is a complete space. Suppose $\{x_n\}$ is a Cauchy sequence in $X$, where $n\in \mathbb{N}$. Let $a,b \in \mathbb{N}$, and let $\epsilon > 0$. By the Cauchy condition, there exists $N_1 \in \mathbb{N}$ such that $\forall a,b > N_1, d(x_a,x_b) < \epsilon$. So, the terms in the sequence $\{x_n\}$ get arbitrarily closer together as $n \rightarrow \infty$. By definition of a complete space, $\{x_n\}$ converges. That is, there exists $p \in X$, such that for every $\epsilon > 0$, there exists an $N_2 \in \mathbb{N}$ such that for every $n > N_2, d(x_n,p_1) < \epsilon$. Define a sequence $x_n$ such that $x_{n} = f(x_{n-1})$, with $x_1$ as the base case. Choose $N_1 =  \min(a,b) -2$, and $a,b>N_1$. By definition of contraction, $d(f(x_{a-1}),f(x_{b-1})) < qd(x_{a-1},x_{b-1})$ for some $q \in \mathbb{R}$ where $0<q<1$:
$$
\begin{align*}
d(f(x_{a-1}),f(x_{b-1})) &< qd(x_{a-1},x_{b-1}) \\
d(x_{a},x_{b}) &< qd(x_{a-1},x_{b-1})
\end{align*}
$$
$d(x_{a-1},x_{b-1})$.
$$
\begin{align*}
d(x_{N_1},<d(x_{a},x_{b}) &< qd(x_{a-1},x_{b-1})\\
qd(x_{a-1},x_{b-1}) \\
d(x_{a},x_{b}) &< \epsilon
\end{align*}
$$
Thus, $\{x_n\}$ is a Cauchy sequence. By definition $\square$
