---
tags: [probability, problem, part-5, lab]
topics: ["[[Law of Large Numbers]]", "[[Central Limit Theorem]]", "[[Independence of Random Variables]]", "[[Limits of Expected Value]]"]
---
# P26 — Simulation and SPY Returns Lab
Back to [[self-study/probability/Index|Index]]

Two simulations check this unit's answers by brute force. Then the same ideas are applied to ten years of real daily SPY (S&P 500 ETF) returns. The real-data half asks whether daily returns are **independent**, which almost every textbook market model quietly assumes. **Q8 is the one to read most carefully.**

> [!question] Questions
> **Simulation 1: this unit's problems**
> 1. Roll a die 100,000 times. Plot the running average. When does it settle near $3.5$?
> 2. Simulate a million two-child families. Estimate $\P(GG \mid \text{at least one } G)$ and $\P(GG \mid \text{older is } G)$.
> 3. Simulate the recession model and estimate $\P(\text{recession} \mid \text{fall})$ by counting.
>
> **Simulation 2: sums vs products**
> 4. (a) Standardize sums of 30 dice. How often is $\abs{Z} > 3$? (b) Run the $1.5\times / 0.6\times$ bet for 10,000 players over 100 rounds. Compare the mean and median wealth.
>
> **Real data: ten years of SPY**
> 5. Compute daily log returns $r_t = \ln(P_t/P_{t-1})$. Find the mean, SD, and annualized SD ($\times\sqrt{252}$).
> 6. **Tails.** What fraction of days are beyond 3 SD? Compare with the normal $0.27\%$. Compute the excess kurtosis.
> 7. **Conditional probability.** Compare $\P(\text{down})$ with $\P(\text{down} \mid \text{down yesterday})$, and $\P(\text{big move})$ with $\P(\text{big} \mid \text{big yesterday})$, where "big" means $\abs{Z} > 2$.
> 8. **Independence.** Compute the autocorrelation of $r_t$ and of $\abs{r_t}$ at lags 1, 2, 5, 10. If the returns were i.i.d., both would sit inside the noise band $\pm 2/\sqrt{n}$. Do they?

## Code
Requires `numpy`. The SPY section uses `yfinance` if it is installed. Otherwise it reads a `SPY.csv` with columns `Date,Close`.
```python
import numpy as np
rng = np.random.default_rng(0)

# ---------- Simulation 1: tonight's problems ----------
# Q1  Law of large numbers: running average of die rolls
rolls = rng.integers(1, 7, size=100_000)
running = np.cumsum(rolls) / np.arange(1, rolls.size + 1)
print("Q1 average after 10, 1000, 100000 rolls:", running[[9, 999, -1]].round(3))

# Q2  Two-child problem
kids = rng.integers(0, 2, size=(1_000_000, 2))       # 1 = girl, column 0 = older
both = kids.all(axis=1)
at_least_one = kids.any(axis=1)
older_girl = kids[:, 0] == 1
print("Q2 P(GG | at least one G) =", both[at_least_one].mean().round(3),
      "  P(GG | older G) =", both[older_girl].mean().round(3))

# Q3  Recession and falling stocks (Bayes by counting)
rec = rng.random(1_000_000) < 0.1
fall = np.where(rec, rng.random(rec.size) < 0.9, rng.random(rec.size) < 0.3)
print("Q3 P(recession | fall) =", rec[fall].mean().round(3))

# ---------- Simulation 2: sums and products ----------
# Q4  CLT for sums vs a compounding bet
sums = rng.integers(1, 7, size=(100_000, 30)).sum(axis=1)
z = (sums - 30 * 3.5) / np.sqrt(30 * 35 / 12)
print("Q4 dice sums: P(|Z| > 3) =", (np.abs(z) > 3).mean().round(4), "(normal: 0.0027)")
mult = np.where(rng.random((10_000, 100)) < 0.5, 1.5, 0.6)
wealth = mult.prod(axis=1)
print("   bet after 100 rounds: mean =", wealth.mean().round(1), " median =", np.median(wealth).round(4))

# ---------- Real data: ten years of SPY ----------
def load_spy():
    try:
        import yfinance as yf
        px = yf.download("SPY", period="10y", auto_adjust=True, progress=False)["Close"]
        return np.asarray(px).ravel()
    except Exception:
        return np.loadtxt("SPY.csv", delimiter=",", skiprows=1, usecols=1)  # Date,Close

prices = load_spy()
r = np.diff(np.log(prices))

# Q5  Mean and spread
print(f"Q5 days={r.size}  mean={r.mean():.5f}  sd={r.std():.4f}  annualized sd={r.std()*np.sqrt(252):.3f}")

# Q6  Tails: how often is a day beyond 3 SD?
zr = (r - r.mean()) / r.std()
kurt = (zr**4).mean() - 3
print(f"Q6 P(|Z|>3) = {(np.abs(zr) > 3).mean():.4f} (normal: 0.0027)   excess kurtosis = {kurt:.1f}")

# Q7  Conditional probability: does yesterday tell you about today?
down = r < 0
big = np.abs(zr) > 2
print(f"Q7 P(down)={down[1:].mean():.3f}  P(down | down yesterday)={down[1:][down[:-1]].mean():.3f}")
print(f"   P(big)={big[1:].mean():.3f}   P(big | big yesterday)={big[1:][big[:-1]].mean():.3f}")

# Q8  Independence: autocorrelation of returns vs of their size
def acf(x, lag):
    x = x - x.mean()
    return (x[:-lag] * x[lag:]).sum() / (x * x).sum()
band = 2 / np.sqrt(r.size)
print(f"Q8 noise band ±{band:.3f}")
for lag in (1, 2, 5, 10):
    print(f"   lag {lag:2d}: acf(r)={acf(r, lag):+.3f}   acf(|r|)={acf(np.abs(r), lag):+.3f}")
```

## What to look for
**Q1–Q3** should reproduce the exact answers: $3.5$ ([[P23 - Expected Value of a Die]]), $1/3$ and $1/2$ ([[P13 - The Two-Child Problem]]), and $0.25$ ([[P12 - Recession and Falling Stocks]]). The running average in Q1 wanders early on and then gets pinned down. That is the [[Law of Large Numbers]].

**Q4.** The dice sums are independent with finite variance, so $\P(\abs{Z} > 3)$ should be close to the normal $0.27\%$ ([[Central Limit Theorem]]). For the bet, the median is near $0.9^{50} \approx 0.005$. The simulated mean is usually far **below** the theoretical $1.05^{100} \approx 131$. The rare paths that carry the expectation almost never show up among 10,000 players, which is another way of seeing [[Limits of Expected Value]].

**Q5–Q6.** Equity returns typically have fat tails. Expect several times more $3\sigma$ days than the normal model predicts, and an excess kurtosis far above 0. The CLT's "finite, stable variance" condition is where this breaks down.

**Q7–Q8. The key question.** Two different kinds of dependence can show up:
- **Direction:** $\P(\text{down} \mid \text{down yesterday})$ vs $\P(\text{down})$, and $\text{acf}(r_t)$. Near zero means yesterday's **sign** tells you little about today's.
- **Size:** $\P(\text{big} \mid \text{big yesterday})$ vs $\P(\text{big})$, and $\text{acf}(\abs{r_t})$. Values well above the band mean **volatility clusters**: big days follow big days.

Returns can be close to **uncorrelated** and still **far from independent**. Independence requires $\P(X = x, Y = y) = \P(X = x)\P(Y = y)$ for every pair of values, including the sizes, not just a zero correlation of the signs. Any model that treats daily returns as i.i.d. (a random walk with constant volatility, or normal sums via the CLT) will understate how often large losses come in runs.

## Related topics
- [[Law of Large Numbers]]
- [[Central Limit Theorem]]
- [[Independence of Random Variables]]
- [[Conditional Probability]]
- [[Limits of Expected Value]]
