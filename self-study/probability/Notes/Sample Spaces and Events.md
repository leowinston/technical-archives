---
tags: [probability, topic, part-1]
---
# Sample Spaces and Events
Back to [Index](../Index.md) · Part 1

## Definitions
- The **sample space** $S$ is the set of all possible outcomes of an experiment.
- An **event** is a subset $A \subseteq S$. $A$ **occurs** if the actual outcome lands in $A$.
- **Pebble world:** picture each outcome as a pebble. An event is a pile of pebbles, and its probability is the pile's total mass.

## Sets as language
| English | Sets |
|---|---|
| $A$ or $B$ | $A \cup B$ |
| $A$ and $B$ | $A \cap B$ |
| not $A$ | $A^c$ |
| $A$ implies $B$ | $A \subseteq B$ |
| $A$ and $B$ can't both happen | $A \cap B = \emptyset$ |

**De Morgan:** $(A \cup B)^c = A^c \cap B^c$ and $(A \cap B)^c = A^c \cup B^c$.

## Example
Flip a coin 3 times: $\card{S} = 2^3 = 8$. "At least one Heads" is $A = \{TTT\}^c$, so it is easier to describe through its complement.

See also: [Naive Definition of Probability](Naive%20Definition%20of%20Probability.md), [Axioms of Probability](Axioms%20of%20Probability.md)
