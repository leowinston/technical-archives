---
tags: [ergodic-theory, index]
---
# Ergodic Theory Index

Self-study notes on ergodic theory and information. Theory notes hold definitions, key results, and short proofs. Example notes hold worked problems and link back to the theory they use.

- Theory notes live in `Theory/`
- Example notes live in `Examples/`
- ✎ marks a place where I highlighted or wrote on the page

---

## Measure Theory Foundations
- [Sequence Spaces and Sigma-Fields](Theory/Sequence%20Spaces%20and%20Sigma-Fields.md) — state space $\rho$, doubly infinite sequences $\omega$, $\sigma$-fields, closure under $\bigcap$
- [Measures, Semirings, and Rings](Theory/Measures%2C%20Semirings%2C%20and%20Rings.md) — $\sigma$-additivity, probability / finite / $\sigma$-finite measures, $(a, b]$ semiring

## Information (ML notebook)
- [Noiseless and Memoryless Channels](Theory/Noiseless%20and%20Memoryless%20Channels.md) — $[Y, \nu_y, Z]$, channel kernel, stationary and invertible codes
- [Prefix Codes and Huffman Coding](Theory/Prefix%20Codes%20and%20Huffman%20Coding.md) — greedy proof, Kraft + entropy bound $H \le \E[L] < H + 1$

---

## Examples

| # | Example | Source | Theory |
|---|---|---|---|
| 1 | [EX01 - Huffman Code and the Entropy Bound](Examples/EX01%20-%20Huffman%20Code%20and%20the%20Entropy%20Bound.md) | ML notebook | [Prefix Codes and Huffman Coding](Theory/Prefix%20Codes%20and%20Huffman%20Coding.md) |

---

## Related
- A probability space $(\Omega, \mathscr F, \mu)$ with $\mu(\Omega) = 1$ is the measure-theoretic form of [Axioms of Probability](../probability/Notes/Axioms%20of%20Probability.md)
- The convex relaxation of the code-length problem and channel capacity as a concave maximization connect to [Convex Optimization Problems](../convex-optimization/topics/Convex%20Optimization%20Problems.md)

## Sources
- Measure theory notes, "Notes on Ergodic Theory and Information" (April 2026)
- ML notebook, handwritten iPad notes ("Codes", "Huffman Coding", "Noiseless Channel", "Channel w/o Memory")
