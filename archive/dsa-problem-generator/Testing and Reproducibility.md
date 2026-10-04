---
tags:
  - data-structures-and-algorithms
  - project
course: CS 253
---
# Testing and Reproducibility
Back to [Index](Index.md) · how the answer keys are checked

An answer key is only useful if it is right. The point of this tool was to **check my own hand traces**, so a wrong key would be worse than no key at all. The test suite checks the output in four layers, from the algorithms up to the finished PDF.

```bash
python3 -B -m unittest discover -s tests -t .
```
> [!success] Last run
> **41 tests, all passing** (about 2 minutes, most of it in `pdflatex`). Run on 2026-09-29.

---

## Layer 1 · The algorithms agree with brute force
Every solver is checked against an **independent oracle**, a slow method that is obviously correct, on hundreds of random inputs (seeded with `random.Random(253)`).

| Solver | Oracle |
|---|---|
| 0/1 knapsack DP | try all $2^n$ subsets |
| LCS DP | try all subsequences of one string |
| Edit distance DP | the recursive definition |
| Dijkstra | Bellman–Ford |
| Prim, Kruskal | the output is a spanning tree **and** its weight equals a brute-force MST |
| Edmonds–Karp | the flow value equals the minimum over all $2^4$ cuts, flow stays within capacity, and flow is conserved at every vertex |
| Huffman | its cost equals the cheapest code-length vector satisfying Kraft; codes are prefix-free and decode back; the tie-break ignores input order |
| KMP failure function | the definition: longest proper prefix that is also a suffix |
| KMP, Boyer–Moore | naive matching at every shift |
| Radix sort | each pass is a stable sort by one digit |
| Topological sort | every edge points forward in the order |

The max-flow test is the max-flow min-cut theorem checked by computer (see the [Ford-Fulkerson problem](generated-problems/graphs/Ford-Fulkerson%20Max%20Flow%20Problem.md)). The Huffman test is the optimality theorem from [Prefix Codes and Huffman Coding](../../self-study/ergodic-theory/Theory/Prefix%20Codes%20and%20Huffman%20Coding.md), checked the same way.

## Layer 2 · The data structures keep their invariants
After 300 random sequences of inserts and deletes, each structure holds exactly the surviving keys in sorted order, and:
- **AVL**: every balance factor is in $\{-1, 0, 1\}$ and every stored height is current. Inserting $1, 2, 3$ causes exactly one rotation.
- **Red-black**: the root is black, no red node has a red child, black heights match under every node, and parent pointers agree. Deleting a missing key does nothing.
- **(2,4)**: every non-root node has 1–3 keys, keys are ordered between children, and all leaves are at the same depth. A fourth key splits the node and promotes the right-middle key.
- **Red-black → (2,4) conversion**: the result is a valid (2,4) tree with exactly the same keys.
- **Trie**: deleting a word keeps shared prefixes and prunes dead branches.
- **Union-find**: `union` reports whether two sets actually merged.

## Layer 3 · Every accepted problem meets its rule
For **all 20 topics** and **seeds 1–40**, the test generates the problem, reads the counts back from its `% key=value` comments, and checks them against the topic's rule. That is 800 problems per run. There is also a check that every topic *has* a rule, so a new topic can't skip this layer. The rules are listed in [How the Generator Works](How%20the%20Generator%20Works.md#2--rejection-sampling-keeps-only-instructive-instances).

## Layer 4 · The output is reproducible and compiles
| Property | How it is checked |
|---|---|
| **Same seed, same document** | generating seed 7 twice gives byte-identical `.tex` |
| **Different seeds, different problems** | seeds 1–5 don't all give the same problem (every topic except the fixed topological-sort DAG) |
| **CLI = library** | `--topic rb --seed 475845898` on the command line matches the library call |
| **Seed is recorded** | an unseeded run still prints `% seed=...` |
| **Solutions only on request** | the Instructor Reference appears only with `--with-solution` |
| **Aliases and errors** | `rb`, `ff`, `2-4`, … resolve to the right topic; an unknown topic exits with an error |
| **It compiles** | every document, with and without its solution, runs through `pdflatex -halt-on-error` |
| **Layout sanity** | long strings for KMP and Boyer–Moore are centered on their own line; skip-list arrows only point at occupied cells |

---

> [!warning] Before publishing: `output/` → `generated-problems/`
> Two tests in `tests/test_output.py` are tied to the old folder:
> - `test_output_matches_generators` regenerates *every* topic for seeds 1–3 and compares the result with `output/` file by file.
> - `test_every_topic_is_represented` expects one subfolder per topic.
>
> `generated-problems/` holds only the six showcase problems, so once `output/` is deleted those two tests will fail. Point them at the new folder and only compare the files it contains, or drop them. The `--write-all` help text and the comment on `OUTPUT_SEEDS` in `cli.py` also still mention `output/`.

## Related
- [How the Generator Works](How%20the%20Generator%20Works.md): what these tests are protecting.
