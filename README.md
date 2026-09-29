# Technical Archives

I chose applied math because it lets me study what I love as far as I want to take it. I fell for it through the thrill of solving hard problems, and I keep falling deeper. The deeper I go, the clearer it gets what I want to become an expert in. The best moments are the clicks, when ideas from different places suddenly fit together.

This repo is where that happens on paper and in code. I write proofs out until they make sense to me, build algorithms and measure whether the theory holds, and work through hard topics on my own instead of skimming them.

## Coursework

| Course | What's here |
|---|---|
| [CS 253: Data Structures & Algorithms](academic/cs-253-dsa) | Experimental analyses of a hash map (load factor vs. collisions and resizing), a hybrid sorting algorithm, and trie vs. list autocomplete. Write-ups and plots only; the implementations aren't included. |
| [Math 250: Foundations](academic/math-250-foundations) | Proof portfolios: direct, contrapositive, contradiction, induction, and set-theoretic proofs, plus equivalence relations, injectivity and surjectivity, and continuity. |

## Self-study

| Topic | What's here |
|---|---|
| [Ergodic theory & measure theory](self-study/ergodic-theory) | Notes working through *Ergodic Theory and Information*: σ-fields, measures, and approximating measures with semirings and rings. |
| [Convex optimization](self-study/convex-optimization) | Theory notes, written exercise solutions, and a CVXPY script testing convex and conic hull membership (Boyd, *Additional Exercises*, 2.5). |

## Building

LaTeX files compile with `pdflatex` from inside their own folder, since the DSA write-ups pull in plots from the same directory. The Python exercise needs `pip install -r self-study/convex-optimization/Exercises/requirements.txt`.
