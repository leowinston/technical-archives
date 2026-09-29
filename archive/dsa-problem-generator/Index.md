---
tags:
  - data-structures-and-algorithms
  - project
  - index
course: CS 253
---
# DSA Problem Generator
*CS 253* · Leo Winston · a command-line tool that turns a seed into a solved study problem

> [!abstract] Abstract
> A Python command-line tool that generates **unlimited, reproducible, non-trivial** practice problems for a data structures and algorithms course, each with a full worked solution typeset in LaTeX/TikZ. Each problem comes from a seed. The generator runs the real algorithm on random input and **rejects** instances that would be boring or ambiguous. It then writes a standalone `.tex` document with the problem, and optionally the answer key with tables and drawn trees and graphs. It covers **20 topics** in six families, from red-black trees to max flow.

---

## Why I built it
I built this to study for my **CS 253 – Data Structures and Algorithms** final.
1. **Not enough problems.** I started by looking up practice problems online, but I ran out of good ones quickly.
2. **RNG drills.** Then I started generating random insertion and deletion sequences myself, since that is what most tracing problems come down to.
3. **The problems were trivial, and I couldn't check them.** Random sequences often skip the interesting cases (no rotation, no tie, greedy happens to work). And after tracing an algorithm by hand, I had no answer key to check against.
4. **LaTeX.** I was already using LaTeX for my other classes, and I figured there had to be a way to generate these structures with good visuals so the solutions would look good too.
5. **A CLI.** I wanted a problem the moment I asked for one, so it's a single terminal command.

So the goal became: **generate the problem, solve it, and typeset both.**

```bash
python3 cs253_problem_generator.py --topic rb --seed 42 --with-solution > problem.tex
```

---

## The showcase problems
One problem from each of the six families, all from **seed 1**. Each note follows the same arc: the problem as generated, why the generator kept it, the big idea, the trace, the solution diagram, and how it connects to the rest of the vault.

| Family | Problem | Why it is non-trivial | Connects to |
|---|---|---|---|
| `trees` | [[archive/dsa-problem-generator/generated-problems/trees/Red-Black Tree Problem\|Red-Black Tree]] | 5 rotations and 17 recolorings across 10 inserts and 2 deletes | [[self-study/graph-theory/Theory/Trees and Leaves\|Trees and Leaves]], [[archive/proofs/Foundations of Math/Proof by Induction\|Proof by Induction]] |
| `data_structures` | [[archive/dsa-problem-generator/generated-problems/data_structures/Skip List Problem\|Skip List]] | prescribed tower heights up to 5, and deletes that need pointer updates | [[self-study/probability/Notes/Bernoulli and Binomial\|Bernoulli and Binomial]], [[self-study/probability/Notes/Expected Value\|Expected Value]] |
| `sorting` | [[archive/dsa-problem-generator/generated-problems/sorting/LSD Radix Sort Problem\|LSD Radix Sort]] | repeated digits, so stability decides the order | [[archive/experiments/Data Structures and Algorithms/Best Sorting Algorithm Experimental Analysis\|BestSort experiment]] |
| `text_processing` | [[archive/dsa-problem-generator/generated-problems/text_processing/Huffman Coding Problem\|Huffman Coding]] | forced frequency ties, and 3 distinct codeword lengths | [[self-study/ergodic-theory/Theory/Prefix Codes and Huffman Coding\|Prefix Codes and Huffman Coding]] |
| `dynamic_programming` | [[archive/dsa-problem-generator/generated-problems/dynamic_programming/0-1 Knapsack Problem\|0/1 Knapsack]] | greedy by ratio gets 28, but the optimum is 33 | [[self-study/convex-optimization/topics/Linear Programs\|Linear Programs]] |
| `graphs` | [[archive/dsa-problem-generator/generated-problems/graphs/Ford-Fulkerson Max Flow Problem\|Ford-Fulkerson Max Flow]] | 4 augmenting paths, certified by a min cut | [[self-study/graph-theory/Theory/Matchings and Augmenting Paths\|Matchings and Augmenting Paths]] |

```mermaid
flowchart LR
    subgraph GEN[Generated problems]
        RB[Red-Black Tree]
        SL[Skip List]
        RX[Radix Sort]
        HF[Huffman Coding]
        KS[0/1 Knapsack]
        FF[Max Flow]
    end
    GT([Graph Theory])
    ET([Ergodic Theory])
    CO([Convex Optimization])
    PR([Probability])
    PF([Proofs])
    EX([CS 253 Experiments])
    RB --> GT
    RB --> PF
    FF --> GT
    FF --> CO
    HF --> ET
    KS --> CO
    KS -.relaxation.-> HF
    SL --> PR
    RX --> EX
    RX --> PF
```

---

## Project notes
- [[archive/dsa-problem-generator/How the Generator Works|How the Generator Works]]: the pipeline from seed to PDF. Covers rejection sampling, canonical answers, instrumented solvers, and the TikZ layout engine.
- [[archive/dsa-problem-generator/Testing and Reproducibility|Testing and Reproducibility]]: how I know the answer keys are right. Covers brute-force checks, rule checks over 40 seeds, compile tests, and byte-identical reruns.

## All 20 topics

| Family | Topics (`--topic` name) |
|---|---|
| `trees` | `avl`, `red_black` (`rb`), `two_four` (`2-4`), `rb_to_24` |
| `data_structures` | `hashing`, `skip_list` |
| `sorting` | `counting_sort`, `radix_sort` |
| `text_processing` | `boyer_moore`, `kmp`, `trie`, `huffman` |
| `dynamic_programming` | `knapsack`, `lcs`, `edit_distance` |
| `graphs` | `dijkstra`, `topological_sort`, `prim`, `kruskal`, `ford_fulkerson` (`ff`) |

## Quick start
```bash
python3 cs253_problem_generator.py --list-topics                  # the 20 topics
python3 cs253_problem_generator.py --topic huffman                # random seed, problem only
python3 cs253_problem_generator.py --topic ff --seed 7 --with-solution > ff.tex
pdflatex ff.tex                                                   # standalone, no image files needed
python3 cs253_problem_generator.py --write-all DIR                # every topic, seeds 1–3, with solutions
```
With no `--seed`, the tool picks one and records it in the document as `% seed=...`, so any problem can be regenerated later.

## Layout
```
dsa-problem-generator/
├── Index.md                        ← this note
├── How the Generator Works.md
├── Testing and Reproducibility.md
├── cs253_problem_generator.py      ← CLI entry point
├── problemgen/
│   ├── cli.py  problem.py  latex.py  render.py
│   ├── generators/                 ← one module per topic (20)
│   └── structures/                 ← AVL, red-black, (2,4), skip list, trie, union-find
├── tests/                          ← 41 tests
└── generated-problems/
    └── <family>/                   ← note + .tex + .pdf + solution .svg
```

---

## Related
- [[archive/experiments/Data Structures and Algorithms/Index|Data Structures and Algorithms experiments]]: my three CS 253 experimental analyses (HashMap, BestSort, trie autocomplete).
