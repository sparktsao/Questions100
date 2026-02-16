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

### Implementation (State Machine DP)

```python
def maxProfit(prices: List[int]) -> int:
    """
    Dynamic Programming with O(1) space using state tracking.

    Time: O(n), Space: O(1)
    """
    # Track the maximum profit for each state
    # buy1: max profit after first buy
    # sell1: max profit after first sell
    # buy2: max profit after second buy
    # sell2: max profit after second sell

    buy1 = buy2 = float('-inf')
    sell1 = sell2 = 0

    for price in prices:
        # Update in reverse order to avoid using updated values
        buy1 = max(buy1, -price)          # Best profit after buying first time
        sell1 = max(sell1, buy1 + price)  # Best profit after selling first time
        buy2 = max(buy2, sell1 - price)   # Best profit after buying second time
        sell2 = max(sell2, buy2 + price)  # Best profit after selling second time

    return sell2
```

### Alternative Implementation (Two-Pass DP)

```python
def maxProfit(prices: List[int]) -> int:
    """
    Two-pass approach: calculate max profit for one transaction from left and right.

    Time: O(n), Space: O(n)
    """
    if not prices:
        return 0

    n = len(prices)

    # First pass: calculate max profit for one transaction ending at or before each day
    left_profits = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left_profits[i] = max(left_profits[i-1], prices[i] - min_price)

    # Second pass: calculate max profit for one transaction starting at or after each day
    right_profits = [0] * n
    max_price = prices[-1]
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        right_profits[i] = max(right_profits[i+1], max_price - prices[i])

    # Combine: find maximum profit from two transactions
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, left_profits[i] + right_profits[i])

    return max_profit
```

### Complexity Analysis

**Time: O(n) - single pass through prices. Space: O(1) - constant space for state variables**

**Why This is Optimal:**
- Achieves best possible time complexity - must examine each price at least once
- State machine approach elegantly tracks all possible states
- O(1) space is optimal - no need for additional arrays
- Handles all edge cases: no transactions, one transaction, two transactions
- Generalizable to k transactions with similar state machine pattern

---

## Categories & Tags

**Primary Topics:** Array, Dynamic Programming

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii)*
