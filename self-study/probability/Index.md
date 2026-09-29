---
tags: [probability, index]
---
# Probability Index

Topic notes hold definitions, key results, and one-line examples. Problem notes hold full worked solutions and link back to the topics they use.

- Topic notes live in `Notes/`
- Problem notes live in `Problems/`
- Macros such as $\P$, $\E$, $\Var$, $\Bin$, and $\indep$ are defined in `preamble.sty` (Extended MathJax). LaTeX Suite snippets type them for you (see the table at the bottom).

---

## Part 1 — Counting and the Naive Definition
- [[Sample Spaces and Events]] — pebble world, events as subsets, De Morgan
- [[Naive Definition of Probability]] — $\Pnaive(A) = \card{A}/\card{S}$, when equal likelihood is justified
- [[Multiplication Rule]] — tree diagrams, $2^n$ subsets, ordered vs unordered pairs
- [[Sampling With and Without Replacement]] — $n^k$, $n(n-1)\cdots(n-k+1)$, the four sampling cases
- [[Binomial Coefficients]] — $\binom{n}{k}$, adjusting for overcounting, words with repeated letters
- [[Binomial Theorem]] — $(x+y)^n = \sum \binom{n}{k}x^k y^{n-k}$
- [[Story Proofs]] — Pascal's rule, Vandermonde, hockey stick
- [[Stars and Bars]] — $\binom{n+k-1}{k}$ indistinguishable objects into $n$ boxes

## Part 2 — Axioms of Probability
- [[Axioms of Probability]] — $\P(\emptyset) = 0$, $\P(S) = 1$, countable additivity, consequences, measure-theoretic $(S, \mathscr F, \P)$ (links to [[self-study/ergodic-theory/Index|Ergodic Theory]])
- [[Inclusion-Exclusion]] — unions of events, de Montmort, $1 - 1/e$

## Part 3 — Conditional Probability
- [[Conditional Probability]] — $\P(A \mid B) = \P(A \cap B)/\P(B)$, prior vs posterior
- [[Bayes' Rule]] — $\P(A \mid B) = \P(B \mid A)\P(A)/\P(B)$, odds form
- [[Law of Total Probability]] — partitions, weighted averages of conditional probabilities
- [[Conditioning on Extra Evidence]] — every probability is conditional, sequential updating
- [[Independence of Events]] — $\P(A \cap B) = \P(A)\P(B)$, pairwise vs full independence
- [[Conditional Independence]] — neither implies nor is implied by independence

## Part 4 — Random Variables and Their Distributions
- [[Random Variables and PMFs]] — $X : S \to \mathbb{R}$, support, PMF of $g(X)$
- [[Bernoulli and Binomial]] — $\Bern(p)$, $\Bin(n, p)$
- [[Hypergeometric Distribution]] — sampling without replacement, vs Binomial
- [[Discrete Uniform Distribution]] — $\DUnif(C)$
- [[Independence of Random Variables]] — joint factorization, i.i.d., matching pennies

## Part 5 — Expectation and Limit Theorems
- [[Expected Value]] — linearity, indicators, the $(a+b)/2$ shortcut and when it fails
- [[Variance]] — $\E[X^2] - (\E X)^2$, $\Var(\bar X_n) = \sigma^2/n$
- [[Law of Large Numbers]] — $\bar X_n \to \mu$, no gambler's fallacy
- [[Central Limit Theorem]] — sums become normal, assumptions, why markets break them

## Part 6 — Valuation and Risk
- [[Expected Present Value]] — discount for time, weight for probability
- [[Limits of Expected Value]] — ensemble vs time averages, geometric growth, ruin

---

## Problems

| # | Problem | Topics |
|---|---|---|
| P01 | [[P01 - Birthday Problem]] | [[Sampling With and Without Replacement]], [[Naive Definition of Probability]] |
| P02 | [[P02 - Full House and the Newton-Pepys Problem]] | [[Binomial Coefficients]], [[Naive Definition of Probability]] |
| P03 | [[P03 - Splitting Twelve People into Teams]] | [[Binomial Coefficients]] |
| P04 | [[P04 - Lattice Paths]] | [[Binomial Coefficients]], [[Multiplication Rule]] |
| P05 | [[P05 - Proof of the Binomial Theorem by Induction]] | [[Binomial Theorem]], [[Story Proofs]] |
| P06 | [[P06 - Story Proofs for Binomial Identities]] | [[Story Proofs]] |
| P07 | [[P07 - Chocolate Bars, Gummy Bears, and Bootstrap Samples]] | [[Stars and Bars]], [[Inclusion-Exclusion]] |
| P08 | [[P08 - de Montmort's Matching Problem]] | [[Inclusion-Exclusion]] |
| P09 | [[P09 - A Die Rolled n Times with a Missing Face]] | [[Inclusion-Exclusion]] |
| P10 | [[P10 - Mixed Practice Comparisons]] | [[Binomial Coefficients]], [[Naive Definition of Probability]] |
| P11 | [[P11 - Two Cards, a Heart and a Red]] | [[Conditional Probability]] |
| P12 | [[P12 - Recession and Falling Stocks]] | [[Bayes' Rule]], [[Law of Total Probability]] |
| P13 | [[P13 - The Two-Child Problem]] | [[Conditional Probability]] |
| P14 | [[P14 - Random Coin, Fair or Biased]] | [[Bayes' Rule]], [[Conditioning on Extra Evidence]] |
| P15 | [[P15 - Six-Fingered Man]] | [[Bayes' Rule]], [[Conditioning on Extra Evidence]] |
| P16 | [[P16 - Monty Hall]] | [[Law of Total Probability]] |
| P17 | [[P17 - Defense Attorney's Fallacy]] | [[Bayes' Rule]] |
| P18 | [[P18 - Spam Filter]] | [[Bayes' Rule]] |
| P19 | [[P19 - Urn Chosen at Random]] | [[Law of Total Probability]] |
| P20 | [[P20 - Even Number of Successes]] | [[Law of Total Probability]], [[Independence of Events]] |
| P21 | [[P21 - Random Slips of Paper]] | [[Bernoulli and Binomial]], [[Hypergeometric Distribution]], [[Discrete Uniform Distribution]] |
| P22 | [[P22 - Matching Pennies and Mystery Opponents]] | [[Conditional Independence]], [[Independence of Random Variables]] |
| P23 | [[P23 - Expected Value of a Die]] | [[Expected Value]], [[Variance]] |
| P24 | [[P24 - Expected Present Value of a Risky Company]] | [[Expected Present Value]] |
| P25 | [[P25 - When Expected Value Misleads]] | [[Limits of Expected Value]] |
| P26 | [[P26 - Simulation and SPY Returns Lab]] | [[Law of Large Numbers]], [[Central Limit Theorem]], [[Independence of Random Variables]] |

---

## LaTeX Suite snippets (math mode, auto-expand)

| Type | Get |
|---|---|
| `Pr` | $\P(\,)$ |
| `Ex` | $\E[\,]$ |
| `Var`, `Cov` | $\Var(\,)$, $\Cov(\,,\,)$ |
| `gvn` | $\mid$ (conditioning bar) |
| `cmp` | $A^{c}$ |
| `bnm` | $\binom{n}{k}$ |
| `idp`, `iid` | $\indep$, $\iid$ |
| `Bern`, `Bin`, `HGeom`, `Nml` | $\Bern(p)$, $\Bin(n,p)$, $\HGeom(w,b,n)$, $\Normal(\mu,\sigma^2)$ |
