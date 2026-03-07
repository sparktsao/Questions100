# 099. Best Time to Buy and Sell Stock III

**Difficulty:** HARD
**Frequency:** 32.0%
**Acceptance Rate:** 51.1%
**LeetCode Link:** [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii)

---

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day.

Find the maximum profit you can achieve. You may complete **at most two transactions**.

**Note:** You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

**Constraints:**
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^5

---

## Examples

### Example 1
**Input:** `prices = [3,3,5,0,0,3,1,4]`
**Output:** `6`
**Explanation:** Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3. Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 3. Total profit = 3 + 3 = 6.

### Example 2
**Input:** `prices = [1,2,3,4,5]`
**Output:** `4`
**Explanation:** Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 4. Only one transaction is needed for maximum profit.

### Example 3
**Input:** `prices = [7,6,4,3,1]`
**Output:** `0`
**Explanation:** Prices are decreasing, so no profit can be made. Best strategy is not to trade at all.

### Example 4
**Input:** `prices = [1]`
**Output:** `0`
**Explanation:** Cannot complete any transaction with only one price, so profit is 0.

---

## Optimal Solution

### Key Insight: Four Decisions Chained as Profit States

At most 2 transactions = exactly 4 decisions in order: **buy1 → sell1 → buy2 → sell2**.

Instead of tracking prices, track **best profit achievable after each decision**:

| Variable | Meaning | Update rule |
|---|---|---|
| `a` | best profit after buy1 | `max(a, -p)` — pay price p |
| `b` | best profit after sell1 | `max(b, a + p)` — gain price p on top of a |
| `c` | best profit after buy2 | `max(c, b - p)` — pay price p, offset by b |
| `d` | best profit after sell2 | `max(d, c + p)` — gain price p on top of c |

Each variable builds on the previous one. `d` is the answer.

### Implementation

```python
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        a = b = c = d = float('-inf')

        for p in prices:
            a = max(a, -p)      # best profit after 1st buy  (pay p)
            b = max(b, a + p)   # best profit after 1st sell (gain p)
            c = max(c, b - p)   # best profit after 2nd buy  (pay p, already have b)
            d = max(d, c + p)   # best profit after 2nd sell (gain p)

        return d
```

### Why Initialize with `-inf`?

All four states start as "not yet reached". Using `-inf` ensures that until a real price is processed, no state can be mistakenly used in the chain.

Once the first `p` is seen:
- `a = max(-inf, -p)` → becomes `-p` (we've made one buy)
- `b`, `c`, `d` remain `-inf` until `a` is valid

### Why Updating In-Order Within the Same Loop Is Safe

You might worry that updating `a` first and then using `a` to update `b` in the same iteration means we're using today's buy to fund today's sell — a same-day buy+sell.

It's actually fine: same-day buy+sell yields zero profit. The `max` keeps the previous best anyway. No state degrades.

### Walkthrough: `prices = [3,3,5,0,0,3,1,4]`

```
       p    a         b         c         d
start  -  -inf      -inf      -inf      -inf
  3    3   -3        -inf      -inf      -inf
  3    3   -3         0        -inf      -inf
  5    5   -3         2        -inf      -inf
  0    0    0         2         2        -inf
  0    0    0         2         2         2
  3    3    0         3         2         5
  1    1    0         3         2         5
  4    4    0         4         2         6   ← answer

Output: 6  ✓  (buy@0, sell@3, profit=3) + (buy@1, sell@4, profit=3)
```

### Complexity Analysis

**Time: O(n)** — single pass

**Space: O(1)** — four scalar variables

---

## Categories & Tags

**Primary Topics:** Array, Dynamic Programming

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii)*
