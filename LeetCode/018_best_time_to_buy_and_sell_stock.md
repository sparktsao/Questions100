# 018. Best Time to Buy and Sell Stock

**Difficulty:** EASY
**Frequency:** 76.4%
**Acceptance Rate:** 55.3%
**LeetCode Link:** [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)

---

## Problem Description

You are given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

**Constraints:**
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4

---

## Examples

### Example 1
**Input:** `prices = [7,1,5,3,6,4]`
**Output:** `5`
**Explanation:** Buy on day 2 (price=1), sell on day 5 (price=6), profit=5

### Example 2
**Input:** `prices = [7,6,4,3,1]`
**Output:** `0`
**Explanation:** No profitable transaction possible (prices only decrease)

### Example 3
**Input:** `prices = [2,4,1]`
**Output:** `2`
**Explanation:** Buy at 2, sell at 4, profit=2

### Example 4
**Input:** `prices = [3,2,6,5,0,3]`
**Output:** `4`
**Explanation:** Buy at 2, sell at 6, profit=4

---

## Optimal Solution

### Implementation

```python
def maxProfit(prices: List[int]) -> int:
    """
    Find maximum profit with single buy/sell.

    Time: O(n), Space: O(1)
    """
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        # Track minimum price seen so far
        min_price = min(min_price, price)
        # Calculate profit if selling today
        profit = price - min_price
        # Update maximum profit
        max_profit = max(max_profit, profit)

    return max_profit
```

### Complexity Analysis

**Time: O(n) - single pass. Space: O(1) - constant**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Array, Dynamic Programming

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock)
