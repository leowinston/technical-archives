---
tags: [ergodic-theory, topic, ml-notebook, information-theory]
source: ML notebook "Noiseless Channel" / "Channel w/o Memory" / "Codes"
---
# Noiseless and Memoryless Channels
Back to [[self-study/ergodic-theory/Index|Index]] · ML notebook

## Noiseless channel
Source (alphabet $\rho$, size $r$) → coder → sender (alphabet $\sigma$, size $s$) → receiver → decoder → addressee.

A one-to-one mapping $\rho \to \sigma$ exists **iff** $r \le s$.

## Channel without memory
The channel is a triple $[Y, \nu_y, Z]$ with sender space $(Y, \mathcal Y)$ and receiver space $(Z, \mathcal Z)$.
- For each $y \in Y$, $\nu_y(\cdot)$ is a probability measure on $\mathcal Z$: the chance the noisy output lands in $C$.
- For each $C \in \mathcal Z$, $\nu_y(C)$ is a measurable function of $y$.

$\nu_y$ is the **kernel** of the channel. With finite alphabets it is a matrix $C_{jk} \in \R^{s \times t}$ of transition probabilities.

## Codes
- **Stationary:** $\varphi T_{\mathcal X} x = T_{\mathcal Y}\varphi x$ (the code commutes with the shift).
- **Invertible:** there is $X_0$ with $\mu(X_0) = 1$, $T_{\mathcal X}X_0 = X_0$, and $\varphi$ one-to-one on it.
- Equivocation is lost information per letter. With entropy fixed, a higher transmission rate means lower equivocation.

## Convexity link
Channel capacity $\max_{p}\, I(p; C)$ maximizes mutual information, which is **concave** in the input distribution $p$ on the simplex. So it is a concave maximization, which is a convex problem.

See also: [[Prefix Codes and Huffman Coding]], [[self-study/convex-optimization/topics/Convex Optimization Problems|Convex Optimization Problems]]
