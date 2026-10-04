---
tags: [proof, exploration]
---
# Inductive Proof of the Fibonacci Recurrence
Back to [Index](../Index.md)

**Statement:** Let $P(n)$ be the property that the $n$-th Fibonacci number is defined by the relation $F_n = F_{n-1} + F_{n-2}$ for all integers $n \geq 2$.

## 1. Base Cases
We define the initial values of the sequence as:
- $F_0 = 0$
- $F_1 = 1$

For $n=2$, the recurrence gives $F_2 = F_1 + F_0 = 1 + 0 = 1$. This matches the definition of the Fibonacci sequence, so $P(2)$ is true.

## 2. Inductive Hypothesis
Assume $P(k)$ is true for some integer $k \geq 2$. That is, we assume:
$$
F_k = F_{k-1} + F_{k-2}
$$
Using **strong induction**, we assume the relation holds for all integers $i$ such that $2 \leq i \leq k$.

## 3. Inductive Step
We want to show that $P(k+1)$ is true, specifically:
$$
\begin{align*}
F_{k+1} &= F_{(k-1)+1} + F_{(k-2)+1} \\
&= F_k + F_{k-1}
\end{align*}
$$
Now, using $P(k)$, we will perform some algebra:
$$
\begin{align*}
F_k &= F_{k-1} + F_{k-2} \\
F_k &= F_{k-1}+F_{k-2}
\end{align*}
$$
By the definition of the Fibonacci sequence, each term is the sum of the two preceding terms. Since we have established the truth of the sequence up to $F_k$, the next term $F_{k+1}$ must follow the same rule:
$$
F_{k+1} = F_k + F_{k-1}
$$

## 4. Matrix Representation
Following this inductive logic, we can represent the transition between states as a system of linear equations:
$$
\begin{align*}
F_{k+1} &= 1 \cdot F_k + 1 \cdot F_{k-1} \\
F_k &= 1 \cdot F_k + 0 \cdot F_{k-1}
\end{align*}
$$

This allows us to express the recurrence as a matrix transformation on a state vector:
$$
\begin{bmatrix}
F_{k+1} \\
F_k
\end{bmatrix} =
\begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix}
\begin{bmatrix}
F_k \\
F_{k-1}
\end{bmatrix}
$$

By the principle of induction, applying this transformation $n$ times to the base vector $\begin{bmatrix} F_1 \\ F_0 \end{bmatrix}$ yields:
$$
\begin{bmatrix}
F_{n+1} \\
F_n
\end{bmatrix} =
\begin{bmatrix}
1 & 1 \\
1 & 0
\end{bmatrix}^n
\begin{bmatrix}
F_1 \\
F_0 \end{bmatrix}
$$
$\square$
