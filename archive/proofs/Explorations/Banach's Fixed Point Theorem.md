---
tags: [proof, exploration]
date: 2026-04
completed: 2026-09-28
---
# Banach's Fixed Point Theorem
Back to [Index](../Index.md)

Leo Winston · April 2026 (finished September 2026)

**Theorem:** Let $(X, d)$ be a nonempty complete metric space, and let $f: X \rightarrow X$ be a contraction. That is, there exists $q \in \mathbb{R}$ with $0 \le q < 1$ such that $d(f(x), f(y)) \le q\,d(x,y)$ for all $x, y \in X$. Then $f$ has exactly one fixed point $p \in X$. Moreover, for any starting point $x_0 \in X$, the sequence defined by $x_n = f(x_{n-1})$ converges to $p$.

*Proof.* Let $x_0 \in X$, and define a sequence $\{x_n\}$ by $x_n = f(x_{n-1})$ for every $n \in \mathbb{N}$. We will show that $\{x_n\}$ is a Cauchy sequence, that its limit is a fixed point of $f$, and that this fixed point is unique.

**Step 1 (consecutive terms):** We claim that $d(x_{n+1}, x_n) \le q^n d(x_1, x_0)$ for every $n \ge 0$. We proceed by induction on $n$. When $n = 0$, both sides equal $d(x_1, x_0)$, so the claim holds. Suppose the claim holds for some $k \ge 0$. By the definition of the sequence and the definition of a contraction, we have:
$$
\begin{align*}
d(x_{k+2}, x_{k+1}) &= d(f(x_{k+1}), f(x_k)) \\
&\le q\,d(x_{k+1}, x_k) \\
&\le q \cdot q^k d(x_1, x_0) \quad \text{(by the inductive hypothesis)} \\
&= q^{k+1} d(x_1, x_0)
\end{align*}
$$
Thus the claim holds for $k+1$, and by the principle of mathematical induction it holds for all $n \ge 0$.

**Step 2 (any two terms):** Let $m, n \in \mathbb{N}$ with $m > n$. By applying the triangle inequality repeatedly, then Step 1, and then bounding the finite geometric sum by the full geometric series, we obtain:
$$
\begin{align*}
d(x_m, x_n) &\le d(x_m, x_{m-1}) + d(x_{m-1}, x_{m-2}) + \cdots + d(x_{n+1}, x_n) \\
&\le \left(q^{m-1} + q^{m-2} + \cdots + q^n\right) d(x_1, x_0) \\
&= q^n\left(1 + q + \cdots + q^{m-n-1}\right) d(x_1, x_0) \\
&\le q^n \left(\frac{1}{1-q}\right) d(x_1, x_0)
\end{align*}
$$
The last step is valid because $0 \le q < 1$, so the geometric series $\sum_{j=0}^{\infty} q^j$ converges to $\frac{1}{1-q}$, and every partial sum is at most that value.

**Step 3 ($\{x_n\}$ is Cauchy):** Let $\epsilon > 0$. If $d(x_1, x_0) = 0$, then Step 2 gives $d(x_m, x_n) = 0 < \epsilon$ for all $m, n$, and we are done. Otherwise $d(x_1, x_0) > 0$. Since $0 \le q < 1$, we know $q^n \rightarrow 0$, so we may choose $N \in \mathbb{N}$ such that
$$
q^N < \frac{\epsilon(1-q)}{d(x_1, x_0)}.
$$
Suppose $m > n \ge N$. Since $q \le 1$, we know $q^n \le q^N$. Combining this with Step 2 yields:
$$
\begin{align*}
d(x_m, x_n) &\le q^n \left(\frac{1}{1-q}\right) d(x_1, x_0) \\
&\le q^N \left(\frac{1}{1-q}\right) d(x_1, x_0) \\
&< \frac{\epsilon(1-q)}{d(x_1, x_0)} \cdot \frac{d(x_1, x_0)}{1-q} \\
&= \epsilon
\end{align*}
$$
Thus $\{x_n\}$ is a Cauchy sequence.

**Step 4 (the limit is a fixed point):** Since $X$ is complete, the Cauchy sequence $\{x_n\}$ converges to some $p \in X$. We will show that $f(p) = p$. Let $\epsilon > 0$. Since $x_n \rightarrow p$, there exists $N_2 \in \mathbb{N}$ such that $d(x_n, p) < \frac{\epsilon}{2}$ for every $n > N_2$. Choose any $n > N_2$. Then $n+1 > N_2$ as well. By the triangle inequality and the definition of a contraction, we have:
$$
\begin{align*}
d(p, f(p)) &\le d(p, x_{n+1}) + d(x_{n+1}, f(p)) \\
&= d(p, x_{n+1}) + d(f(x_n), f(p)) \\
&\le d(p, x_{n+1}) + q\,d(x_n, p) \\
&< \frac{\epsilon}{2} + q \cdot \frac{\epsilon}{2} \\
&\le \frac{\epsilon}{2} + \frac{\epsilon}{2} = \epsilon
\end{align*}
$$
Since $d(p, f(p)) < \epsilon$ for every $\epsilon > 0$, and distances are non-negative, it follows that $d(p, f(p)) = 0$. By the definition of a metric, $f(p) = p$.

**Step 5 (uniqueness):** Suppose for the sake of contradiction that $r \in X$ is a fixed point of $f$ with $r \ne p$. Since $r \ne p$, $d(p, r) > 0$. Using $f(p) = p$ and $f(r) = r$ with the definition of a contraction, we have:
$$
\begin{align*}
d(p, r) &= d(f(p), f(r)) \\
&\le q\,d(p, r)
\end{align*}
$$
Since $d(p, r)$ is strictly positive, we may divide both sides by $d(p, r)$ without reversing the inequality sign, which gives $1 \le q$. This contradicts $q < 1$. Consequently, our assumption that a second fixed point exists must be false.

Therefore, $f$ has exactly one fixed point $p$, and the sequence $x_n = f(x_{n-1})$ converges to $p$ from any starting point $x_0 \in X$. $\blacksquare$

---

## Connection: existence and uniqueness for ODEs
The standard proof of the nonlinear existence and uniqueness theorem (Picard–Lindelöf) is this theorem. Take $X$ to be the continuous functions on $[t_0 - h, t_0 + h]$ with the max distance, which is complete. Take $f$ to be the map $\phi \mapsto y_0 + \int_{t_0}^{t} F(s, \phi(s))\,ds$. For small $h$ it is a contraction, and its unique fixed point is the unique solution of $y' = F(t, y)$, $y(t_0) = y_0$. See [Existence and Uniqueness Theorems](../../../academic/math-212/Topics/Existence%20and%20Uniqueness%20Theorems.md).
