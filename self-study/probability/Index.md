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
- [Sample Spaces and Events](Notes/Sample%20Spaces%20and%20Events.md) — pebble world, events as subsets, De Morgan
- [Naive Definition of Probability](Notes/Naive%20Definition%20of%20Probability.md) — $\Pnaive(A) = \card{A}/\card{S}$, when equal likelihood is justified
- [Multiplication Rule](Notes/Multiplication%20Rule.md) — tree diagrams, $2^n$ subsets, ordered vs unordered pairs
- [Sampling With and Without Replacement](Notes/Sampling%20With%20and%20Without%20Replacement.md) — $n^k$, $n(n-1)\cdots(n-k+1)$, the four sampling cases
- [Binomial Coefficients](Notes/Binomial%20Coefficients.md) — $\binom{n}{k}$, adjusting for overcounting, words with repeated letters
- [Binomial Theorem](Notes/Binomial%20Theorem.md) — $(x+y)^n = \sum \binom{n}{k}x^k y^{n-k}$
- [Story Proofs](Notes/Story%20Proofs.md) — Pascal's rule, Vandermonde, hockey stick
- [Stars and Bars](Notes/Stars%20and%20Bars.md) — $\binom{n+k-1}{k}$ indistinguishable objects into $n$ boxes

## Part 2 — Axioms of Probability
- [Axioms of Probability](Notes/Axioms%20of%20Probability.md) — $\P(\emptyset) = 0$, $\P(S) = 1$, countable additivity, consequences, measure-theoretic $(S, \mathscr F, \P)$ (links to [Ergodic Theory](../ergodic-theory/Index.md))
- [Inclusion-Exclusion](Notes/Inclusion-Exclusion.md) — unions of events, de Montmort, $1 - 1/e$

## Part 3 — Conditional Probability
- [Conditional Probability](Notes/Conditional%20Probability.md) — $\P(A \mid B) = \P(A \cap B)/\P(B)$, prior vs posterior
- [Bayes' Rule](Notes/Bayes%27%20Rule.md) — $\P(A \mid B) = \P(B \mid A)\P(A)/\P(B)$, odds form
- [Law of Total Probability](Notes/Law%20of%20Total%20Probability.md) — partitions, weighted averages of conditional probabilities
- [Conditioning on Extra Evidence](Notes/Conditioning%20on%20Extra%20Evidence.md) — every probability is conditional, sequential updating
- [Independence of Events](Notes/Independence%20of%20Events.md) — $\P(A \cap B) = \P(A)\P(B)$, pairwise vs full independence
- [Conditional Independence](Notes/Conditional%20Independence.md) — neither implies nor is implied by independence

## Part 4 — Random Variables and Their Distributions
- [Random Variables and PMFs](Notes/Random%20Variables%20and%20PMFs.md) — $X : S \to \mathbb{R}$, support, PMF of $g(X)$
- [Bernoulli and Binomial](Notes/Bernoulli%20and%20Binomial.md) — $\Bern(p)$, $\Bin(n, p)$
- [Hypergeometric Distribution](Notes/Hypergeometric%20Distribution.md) — sampling without replacement, vs Binomial
- [Discrete Uniform Distribution](Notes/Discrete%20Uniform%20Distribution.md) — $\DUnif(C)$
- [Independence of Random Variables](Notes/Independence%20of%20Random%20Variables.md) — joint factorization, i.i.d., matching pennies

## Part 5 — Expectation and Limit Theorems
- [Expected Value](Notes/Expected%20Value.md) — linearity, indicators, the $(a+b)/2$ shortcut and when it fails
- [Variance](Notes/Variance.md) — $\E[X^2] - (\E X)^2$, $\Var(\bar X_n) = \sigma^2/n$
- [Law of Large Numbers](Notes/Law%20of%20Large%20Numbers.md) — $\bar X_n \to \mu$, no gambler's fallacy
- [Central Limit Theorem](Notes/Central%20Limit%20Theorem.md) — sums become normal, assumptions, why markets break them

## Part 6 — Valuation and Risk
- [Expected Present Value](Notes/Expected%20Present%20Value.md) — discount for time, weight for probability
- [Limits of Expected Value](Notes/Limits%20of%20Expected%20Value.md) — ensemble vs time averages, geometric growth, ruin

---

## Problems

| # | Problem | Topics |
|---|---|---|
| P01 | [P01 - Birthday Problem](Problems/P01%20-%20Birthday%20Problem.md) | [Sampling With and Without Replacement](Notes/Sampling%20With%20and%20Without%20Replacement.md), [Naive Definition of Probability](Notes/Naive%20Definition%20of%20Probability.md) |
| P02 | [P02 - Full House and the Newton-Pepys Problem](Problems/P02%20-%20Full%20House%20and%20the%20Newton-Pepys%20Problem.md) | [Binomial Coefficients](Notes/Binomial%20Coefficients.md), [Naive Definition of Probability](Notes/Naive%20Definition%20of%20Probability.md) |
| P03 | [P03 - Splitting Twelve People into Teams](Problems/P03%20-%20Splitting%20Twelve%20People%20into%20Teams.md) | [Binomial Coefficients](Notes/Binomial%20Coefficients.md) |
| P04 | [P04 - Lattice Paths](Problems/P04%20-%20Lattice%20Paths.md) | [Binomial Coefficients](Notes/Binomial%20Coefficients.md), [Multiplication Rule](Notes/Multiplication%20Rule.md) |
| P05 | [P05 - Proof of the Binomial Theorem by Induction](Problems/P05%20-%20Proof%20of%20the%20Binomial%20Theorem%20by%20Induction.md) | [Binomial Theorem](Notes/Binomial%20Theorem.md), [Story Proofs](Notes/Story%20Proofs.md) |
| P06 | [P06 - Story Proofs for Binomial Identities](Problems/P06%20-%20Story%20Proofs%20for%20Binomial%20Identities.md) | [Story Proofs](Notes/Story%20Proofs.md) |
| P07 | [P07 - Chocolate Bars, Gummy Bears, and Bootstrap Samples](Problems/P07%20-%20Chocolate%20Bars%2C%20Gummy%20Bears%2C%20and%20Bootstrap%20Samples.md) | [Stars and Bars](Notes/Stars%20and%20Bars.md), [Inclusion-Exclusion](Notes/Inclusion-Exclusion.md) |
| P08 | [P08 - de Montmort's Matching Problem](Problems/P08%20-%20de%20Montmort%27s%20Matching%20Problem.md) | [Inclusion-Exclusion](Notes/Inclusion-Exclusion.md) |
| P09 | [P09 - A Die Rolled n Times with a Missing Face](Problems/P09%20-%20A%20Die%20Rolled%20n%20Times%20with%20a%20Missing%20Face.md) | [Inclusion-Exclusion](Notes/Inclusion-Exclusion.md) |
| P10 | [P10 - Mixed Practice Comparisons](Problems/P10%20-%20Mixed%20Practice%20Comparisons.md) | [Binomial Coefficients](Notes/Binomial%20Coefficients.md), [Naive Definition of Probability](Notes/Naive%20Definition%20of%20Probability.md) |
| P11 | [P11 - Two Cards, a Heart and a Red](Problems/P11%20-%20Two%20Cards%2C%20a%20Heart%20and%20a%20Red.md) | [Conditional Probability](Notes/Conditional%20Probability.md) |
| P12 | [P12 - Recession and Falling Stocks](Problems/P12%20-%20Recession%20and%20Falling%20Stocks.md) | [Bayes' Rule](Notes/Bayes%27%20Rule.md), [Law of Total Probability](Notes/Law%20of%20Total%20Probability.md) |
| P13 | [P13 - The Two-Child Problem](Problems/P13%20-%20The%20Two-Child%20Problem.md) | [Conditional Probability](Notes/Conditional%20Probability.md) |
| P14 | [P14 - Random Coin, Fair or Biased](Problems/P14%20-%20Random%20Coin%2C%20Fair%20or%20Biased.md) | [Bayes' Rule](Notes/Bayes%27%20Rule.md), [Conditioning on Extra Evidence](Notes/Conditioning%20on%20Extra%20Evidence.md) |
| P15 | [P15 - Six-Fingered Man](Problems/P15%20-%20Six-Fingered%20Man.md) | [Bayes' Rule](Notes/Bayes%27%20Rule.md), [Conditioning on Extra Evidence](Notes/Conditioning%20on%20Extra%20Evidence.md) |
| P16 | [P16 - Monty Hall](Problems/P16%20-%20Monty%20Hall.md) | [Law of Total Probability](Notes/Law%20of%20Total%20Probability.md) |
| P17 | [P17 - Defense Attorney's Fallacy](Problems/P17%20-%20Defense%20Attorney%27s%20Fallacy.md) | [Bayes' Rule](Notes/Bayes%27%20Rule.md) |
| P18 | [P18 - Spam Filter](Problems/P18%20-%20Spam%20Filter.md) | [Bayes' Rule](Notes/Bayes%27%20Rule.md) |
| P19 | [P19 - Urn Chosen at Random](Problems/P19%20-%20Urn%20Chosen%20at%20Random.md) | [Law of Total Probability](Notes/Law%20of%20Total%20Probability.md) |
| P20 | [P20 - Even Number of Successes](Problems/P20%20-%20Even%20Number%20of%20Successes.md) | [Law of Total Probability](Notes/Law%20of%20Total%20Probability.md), [Independence of Events](Notes/Independence%20of%20Events.md) |
| P21 | [P21 - Random Slips of Paper](Problems/P21%20-%20Random%20Slips%20of%20Paper.md) | [Bernoulli and Binomial](Notes/Bernoulli%20and%20Binomial.md), [Hypergeometric Distribution](Notes/Hypergeometric%20Distribution.md), [Discrete Uniform Distribution](Notes/Discrete%20Uniform%20Distribution.md) |
| P22 | [P22 - Matching Pennies and Mystery Opponents](Problems/P22%20-%20Matching%20Pennies%20and%20Mystery%20Opponents.md) | [Conditional Independence](Notes/Conditional%20Independence.md), [Independence of Random Variables](Notes/Independence%20of%20Random%20Variables.md) |
| P23 | [P23 - Expected Value of a Die](Problems/P23%20-%20Expected%20Value%20of%20a%20Die.md) | [Expected Value](Notes/Expected%20Value.md), [Variance](Notes/Variance.md) |
| P24 | [P24 - Expected Present Value of a Risky Company](Problems/P24%20-%20Expected%20Present%20Value%20of%20a%20Risky%20Company.md) | [Expected Present Value](Notes/Expected%20Present%20Value.md) |
| P25 | [P25 - When Expected Value Misleads](Problems/P25%20-%20When%20Expected%20Value%20Misleads.md) | [Limits of Expected Value](Notes/Limits%20of%20Expected%20Value.md) |
| P26 | [P26 - Simulation and SPY Returns Lab](Problems/P26%20-%20Simulation%20and%20SPY%20Returns%20Lab.md) | [Law of Large Numbers](Notes/Law%20of%20Large%20Numbers.md), [Central Limit Theorem](Notes/Central%20Limit%20Theorem.md), [Independence of Random Variables](Notes/Independence%20of%20Random%20Variables.md) |

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
