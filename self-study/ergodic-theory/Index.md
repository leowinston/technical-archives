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
- [[Sequence Spaces and Sigma-Fields]] — state space $\rho$, doubly infinite sequences $\omega$, $\sigma$-fields, closure under $\bigcap$
- [[Measures, Semirings, and Rings]] — $\sigma$-additivity, probability / finite / $\sigma$-finite measures, $(a, b]$ semiring

## Information (ML notebook)
- [[Noiseless and Memoryless Channels]] — $[Y, \nu_y, Z]$, channel kernel, stationary and invertible codes
- [[Prefix Codes and Huffman Coding]] — greedy proof, Kraft + entropy bound $H \le \E[L] < H + 1$

---

## Examples

| # | Example | Source | Theory |
|---|---|---|---|
| 1 | [[EX01 - Huffman Code and the Entropy Bound]] | ML notebook | [[Prefix Codes and Huffman Coding]] |

---

## Related
- A probability space $(\Omega, \mathscr F, \mu)$ with $\mu(\Omega) = 1$ is the measure-theoretic form of [[self-study/probability/Notes/Axioms of Probability|Axioms of Probability]]
- The convex relaxation of the code-length problem and channel capacity as a concave maximization connect to [[self-study/convex-optimization/topics/Convex Optimization Problems|Convex Optimization Problems]]

## Sources
- Measure theory notes, "Notes on Ergodic Theory and Information" (April 2026)
- ML notebook, handwritten iPad notes ("Codes", "Huffman Coding", "Noiseless Channel", "Channel w/o Memory")
