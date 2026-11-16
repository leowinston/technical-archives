---
tags: [ergodic-theory, topic, hashing, string-matching]
source: Data structures (Rabin–Karp string matching), recast on the shift space
---
# Rabin–Karp and Horner's Rule
Back to [Index](../Index.md) · Hashing as a stationary code

## Text as a shift space
Read a text as a sequence $\omega = (\omega_0, \omega_1, \dots)$ over the state space $\rho$, with the left shift $(T\omega)_i = \omega_{i+1}$. Window $i$ is the first $m$ letters of $T^i\omega$.

## Horner's rule
Hash the first $m$ letters as a polynomial in base $b$, reducing mod a prime $q$ after each step:
$$
h(\omega) = \sum_{k=0}^{m-1} \omega_k\, b^{m-1-k} = \big(\cdots((\omega_0 b + \omega_1)b + \omega_2)\cdots\big)b + \omega_{m-1} \pmod q
$$
This takes $m$ multiplications and no powers. It is the same nested multiplication that evaluates the [Newton form](../../../academic/math-315/Topics%202/Newton%20Form.md).

## Rolling hash = one step of the shift
$$
\boxed{\,h(T\omega) = \big(b\,(h(\omega) - \omega_0\, b^{m-1}) + \omega_m\big) \bmod q\,}
$$
Each step costs $O(1)$. The window hashes $\varphi(\omega)_i = h(T^i\omega)$ form a sliding block code with $\varphi T = T\varphi$, which is a **stationary code**.

## Rabin–Karp
```text
hp = horner(P);  hw = horner(text[0..m))
for i = 0..n-m:
  if hw == hp and text[i..i+m) == P: report i
  hw = roll(hw, text[i], text[i+m])
```
The expected cost is $O(n + m)$. The worst case is $O(nm)$, when every window collides.

## Ergodic view of false hits
With $b$ random mod $q$, two distinct $m$-strings collide with probability at most $\frac{m-1}{q}$, because their difference polynomial has at most $m - 1$ roots. If the text comes from a stationary ergodic source $\mu$, Birkhoff's theorem gives the spurious-hit rate along a single text:
$$
\frac1N \sum_{i<N} \Ind\{h(T^i\omega) = h(P),\ \omega_{[i,\,i+m)} \ne P\} \;\longrightarrow\; \mu\{h = h(P),\ \omega_{[0,m)} \ne P\} \quad \text{a.s.}
$$
The time average over one long text equals the space average over all texts.

See also: [Sequence Spaces and Sigma-Fields](Sequence%20Spaces%20and%20Sigma-Fields.md), [Noiseless and Memoryless Channels](Noiseless%20and%20Memoryless%20Channels.md)
