# Dynamic Programming - Comprehensive Guide

## From Recursion to Memoization to Tabulation

---

## 🎯 Overview

**Total Problems:** 4
**Difficulty:** Easy (1) • Medium (2) • Hard (1)

**Core Concept:**
Break problem into overlapping subproblems, solve each once, reuse results

**Key Insight:**
Start with recursion, add memoization, then convert to bottom-up DP

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: 1D DP (Fibonacci, House Robber, Jump Game)
### Pattern 2: 2D DP (Grid Paths, Edit Distance, LCS)
### Pattern 3: DP on Strings (Palindrome, Word Break)
### Pattern 4: DP on Stocks (Buy/Sell with Constraints)


---

## 🎓 Learning Path

Climbing Stairs → House Robber → Coin Change → Edit Distance → Stock Trading

---

## ⚠️ Common Pitfalls

1. Wrong base case 2. Wrong state transition 3. Not considering all previous states 4. Space not optimized

---

## ✅ Testing Strategy

Test: base cases, small inputs, edge values, impossible cases

---

## 💡 Templates & Code Patterns


```python
# Top-down (Memoization)
def dp(i, memo={}):
    if i in memo:
        return memo[i]
    if base_case:
        return base_value
    memo[i] = recurrence_relation
    return memo[i]

# Bottom-up (Tabulation)
dp = [0] * (n + 1)
dp[0] = base_value
for i in range(1, n + 1):
    dp[i] = recurrence_relation
return dp[n]
```


---

## 💎 Mastery Tips

1. Define state 2. Find recurrence 3. Identify base cases 4. Add memoization 5. Optimize space

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 018 | [Best Time to Buy and Sell Stock](./018_best_time_to_buy_and_sell_stock.md) | EASY | 76.4% |
| 055 | [Subsets](./055_subsets.md) | MEDIUM | 47.0% |
| 075 | [Word Break](./075_word_break.md) | MEDIUM | 40.7% |
| 099 | [Best Time to Buy and Sell Stock III](./099_best_time_to_buy_and_sell_stock_iii.md) | HARD | 32.0% |

---

[← Back to Main](../README.md)
