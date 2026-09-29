---
tags: [ergodic-theory, topic, ml-notebook, information-theory]
source: ML notebook "Codes" / "Huffman Coding" / "Greedy Algorithm to solve"
---
# Prefix Codes and Huffman Coding
Back to [[self-study/ergodic-theory/Index|Index]] · ML notebook

## Prefix codes
$\varphi : \mathcal A \to \{0, 1\}^{*}$ is **prefix-free** if no codeword $\varphi(a_i)$ is a prefix of another $\varphi(a_j)$. Codewords are the leaves of a binary tree. Goal:
$$
\text{minimize } \E[L] = \sum_{a \in \mathcal A} p_a\,\ell_a
$$
✎ If a node of the tree has only one child, you can promote the leaf below it, so that code could not be optimal.

## Huffman (greedy)
Repeatedly merge the two least likely symbols $b, d$ into one symbol $\alpha$ with $p_\alpha = p_b + p_d$.

**Lemma 1.** The smallest-probability symbol has (tied for) the longest codeword. If not, swap it with the longest one; the change $\Delta(p_b - p_c) < 0$ would lower $\E[L]$, a contradiction.

**Lemma 2.** The two least likely symbols can be taken as **siblings** at the deepest level.

**Optimal substructure.** If $T'$ is optimal for $\mathcal A' = (\mathcal A - \{b, d\}) \cup \{\alpha\}$, expanding $\alpha$ gives an optimal $T$, with $L = L' + p_b + p_d$.

## Convex relaxation
Drop integrality: minimize $\sum p_a\ell_a$ s.t. $\sum 2^{-\ell_a} \le 1$ (Kraft). This is a convex problem with solution $\ell_a = -\log_2 p_a$ and value the **entropy** $H(p)$. Huffman satisfies $H \le \E[L] < H + 1$.

## Examples
- [[EX01 - Huffman Code and the Entropy Bound]]

See also: [[Noiseless and Memoryless Channels]]
