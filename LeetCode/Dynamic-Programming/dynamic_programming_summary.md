# Dynamic Programming - Comprehensive Mastery Guide




## 📋 Problems in This Category

- [018. Best Time to Buy and Sell Stock](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Dynamic-Programming/018_best_time_to_buy_and_sell_stock.md) - `1D DP`
- [055. Subsets](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Dynamic-Programming/055_subsets.md) - `Backtrack`
- [075. Word Break](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Dynamic-Programming/075_word_break.md) - `1D DP`
- [083. Valid Palindrome III](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Dynamic-Programming/083_valid_palindrome_iii.md) - `2D DP`
- [099. Best Time to Buy and Sell Stock III](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Dynamic-Programming/099_best_time_to_buy_and_sell_stock_iii.md) - `State Machine DP`

---

## 🎯 Category Overview

**Total Problems:** 4
**Difficulty Distribution:** Easy (1) • Medium (2) • Hard (1)
**Core Paradigm:** Optimal Substructure + Overlapping Subproblems

**What Makes This Category Special:**

Dynamic Programming transforms **exponential recursion** into **polynomial iteration** by remembering solutions to subproblems. The key insight: if a problem has optimal substructure (optimal solution contains optimal solutions to subproblems) and overlapping subproblems (same subproblems solved multiple times), DP can dramatically improve efficiency.

**The DP Philosophy:**

"Those who cannot remember the past are condemned to repeat it." — George Santayana

In algorithms: Those who don't memoize are condemned to O(2ⁿ).

---

## 📊 Problem Progression Map

```
Foundation (Greedy Disguised as DP)
├─ #018 Best Time to Buy/Sell Stock ⭐ START HERE
│  └─ Pattern: Track running minimum, update max profit
│  └─ Actually greedy, but teaches DP thinking
│
String DP (Classic 1D DP)
├─ #075 Word Break ⭐ CORE DP PROBLEM
│  └─ Pattern: dp[i] = can segment s[0:i]?
│  └─ Recurrence: dp[i] = any(dp[j] && s[j:i] in dict)
│
State Machine DP (Multi-Dimensional States)
├─ #099 Buy/Sell Stock III ⭐ ADVANCED
│  └─ Pattern: Track states (buy1, sell1, buy2, sell2)
│  └─ State transitions with constraints
│
Backtracking (Misclassified as DP)
└─ #055 Subsets
   └─ Pattern: Generate all 2ⁿ subsets
   └─ Not really DP - it's exhaustive search!

Difficulty: ⭐ = Must Master
```

---

## 🧬 Three Core Patterns

### Pattern 1: 1D DP (Linear Dependency)

**When to Use:** "Maximum/minimum over linear sequence", "can we reach position i?"

**Key Insight:** dp[i] depends only on dp[j] where j < i.

**Structure:**
1. **Define state:** What does dp[i] represent?
2. **Base case:** dp[0] = ?
3. **Recurrence:** dp[i] = f(dp[0], ..., dp[i-1])
4. **Answer:** dp[n] or max(dp)

**Template:**
```python
def solve(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = base_value

    for i in range(1, n + 1):
        for j in range(i):  # Check all previous positions
            dp[i] = max(dp[i], dp[j] + transition(j, i))

    return dp[n]
```

**Problems:** #018 (sort of), #075

---

### Pattern 2: State Machine DP (Discrete States)

**When to Use:** "Transitions between states with constraints", "at most K transactions"

**Key Insight:** Model problem as finite state machine. Each state has a value (max profit, min cost). Transitions update states based on current input.

**Structure:**
1. **Define states:** What states can we be in?
2. **Initial values:** What's the initial value for each state?
3. **Transitions:** How do we move between states?
4. **Answer:** Final state value

**Template:**
```python
def solve(arr):
    # Define states
    state1 = initial_value1
    state2 = initial_value2

    for val in arr:
        # Update states (order matters!)
        new_state1 = max(state1, transition1(val))
        new_state2 = max(state2, transition2(state1, val))

        state1, state2 = new_state1, new_state2

    return final_state
```

**Problems:** #099

---

### Pattern 3: Backtracking / Exhaustive Search

**When to Use:** "Generate all...", "find all subsets/permutations/combinations"

**Key Insight:** Not actually DP! Exhaustive search with O(2ⁿ) or O(n!) time. No overlapping subproblems.

**Template:**
```python
def generate_all(arr):
    result = []

    def backtrack(start, current):
        result.append(current[:])  # Add current state

        for i in range(start, len(arr)):
            current.append(arr[i])       # Choose
            backtrack(i + 1, current)    # Explore
            current.pop()                # Unchoose

    backtrack(0, [])
    return result
```

**Problems:** #055

---

## 🔍 Problem Deep Dive

### #018 Best Time to Buy and Sell Stock ⭐

**Difficulty:** Easy | **Frequency:** 76.4%

**Task:** Given stock prices array, find maximum profit from one buy-sell transaction.

**Input:** `prices = [7,1,5,3,6,4]`
**Output:** `5`
**Explanation:** Buy at 1, sell at 6 → profit = 5

**What Makes This Special:**

This is **not really DP** - it's a greedy algorithm! But it teaches DP thinking: "At each position, what's the best decision given past information?"

**The Greedy Insight:**

To maximize profit when selling at day i, we must have bought at the **minimum price before day i**.

**Three Approaches:**

1. **Brute Force:** O(n²) - try all pairs
   ```python
   max_profit = 0
   for i in range(len(prices)):
       for j in range(i+1, len(prices)):
           profit = prices[j] - prices[i]
           max_profit = max(max_profit, profit)
   return max_profit
   ```

2. **Greedy (Optimal):** O(n) ⭐
   ```python
   min_price = float('inf')
   max_profit = 0

   for price in prices:
       min_price = min(min_price, price)
       profit = price - min_price
       max_profit = max(max_profit, profit)

   return max_profit
   ```

3. **DP Formulation (Same as Greedy):**
   ```python
   # dp[i] = max profit selling at or before day i
   # But we don't need array - just track max_profit!
   ```

**Step-by-Step Example:**

```
prices = [7, 1, 5, 3, 6, 4]

Day 0 (price=7):
  min_price = 7
  profit = 7 - 7 = 0
  max_profit = 0

Day 1 (price=1):
  min_price = min(7, 1) = 1  ← New minimum!
  profit = 1 - 1 = 0
  max_profit = 0

Day 2 (price=5):
  min_price = 1
  profit = 5 - 1 = 4  ← Profit if we sell today
  max_profit = max(0, 4) = 4

Day 3 (price=3):
  min_price = 1
  profit = 3 - 1 = 2
  max_profit = max(4, 2) = 4  (no update)

Day 4 (price=6):
  min_price = 1
  profit = 6 - 1 = 5  ← Best profit!
  max_profit = max(4, 5) = 5

Day 5 (price=4):
  min_price = 1
  profit = 4 - 1 = 3
  max_profit = max(5, 3) = 5  (no update)

Final: 5 ✓
```

**Visual Understanding:**

```
Prices: 7  1  5  3  6  4
        │  └─ min (buy here)
        │     │
        └─────┼─────┘
              │     └── max profit = 6-1 = 5
              └──────── also good: 5-1 = 4
```

**Common Bugs:**

❌ **Wrong:** Calculate profit before updating min_price
```python
profit = price - min_price  # Using old min_price
min_price = min(min_price, price)  # Update after
# Bug: if price is new minimum, profit is negative!
```

✅ **Correct:** Update min_price first, then calculate profit
```python
min_price = min(min_price, price)
profit = price - min_price  # Now profit >= 0 always
```

**Key Insights:**
1. **Greedy choice is optimal** - always buy at historical minimum
2. **Single pass sufficient** - O(n) time, O(1) space
3. **Foundation for Stock II, III, IV** - understanding this is crucial
4. **Can't go negative** - profit is always >= 0 (option not to trade)

**Complexity:**
- **Time:** O(n) - single pass
- **Space:** O(1) - two variables

---

### #075 Word Break ⭐

**Difficulty:** Medium | **Frequency:** 40.7%

**Task:** Given string `s` and dictionary `wordDict`, can `s` be segmented into dictionary words?

**Input:** `s = "leetcode", wordDict = ["leet", "code"]`
**Output:** `true`
**Explanation:** "leetcode" = "leet" + "code"

**What Makes This Special:**

This is **textbook 1D DP**. Teaches the classic pattern: dp[i] represents "can we solve problem for s[0:i]?", and we check all ways to reach i from previous positions.

**The DP Insight:**

```
To know if s[0:i] is valid:
  Try all positions j < i
  Check if s[0:j] is valid AND s[j:i] is in dictionary
  If any j works, then dp[i] = true
```

**Two Approaches:**

1. **Top-Down (Memoization):**
   ```python
   def wordBreak(s, wordDict):
       word_set = set(wordDict)
       memo = {}

       def can_break(start):
           if start == len(s):
               return True
           if start in memo:
               return memo[start]

           for end in range(start + 1, len(s) + 1):
               if s[start:end] in word_set and can_break(end):
                   memo[start] = True
                   return True

           memo[start] = False
           return False

       return can_break(0)
   ```

2. **Bottom-Up (Tabulation) ⭐ Preferred:**
   ```python
   def wordBreak(s, wordDict):
       word_set = set(wordDict)
       n = len(s)

       # dp[i] = True if s[0:i] can be segmented
       dp = [False] * (n + 1)
       dp[0] = True  # Empty string is valid

       for i in range(1, n + 1):
           for j in range(i):
               # s[0:j] valid? AND s[j:i] in dictionary?
               if dp[j] and s[j:i] in word_set:
                   dp[i] = True
                   break  # Found one valid segmentation

       return dp[n]
   ```

**Step-by-Step Example:**

```
s = "leetcode"
wordDict = ["leet", "code"]

Build dp array:
dp[0] = True  (empty string)

i=1: s[0:1] = "l"
  j=0: dp[0]=True, "l" in dict? No
  dp[1] = False

i=2: s[0:2] = "le"
  j=0: dp[0]=True, "le" in dict? No
  j=1: dp[1]=False (skip)
  dp[2] = False

i=3: s[0:3] = "lee"
  j=0: dp[0]=True, "lee" in dict? No
  j=1: dp[1]=False (skip)
  j=2: dp[2]=False (skip)
  dp[3] = False

i=4: s[0:4] = "leet"
  j=0: dp[0]=True, "leet" in dict? YES! ✓
  dp[4] = True

i=5: s[0:5] = "leetc"
  j=0: dp[0]=True, "leetc" in dict? No
  j=4: dp[4]=True, "c" in dict? No
  dp[5] = False

i=6: s[0:6] = "leetco"
  j=4: dp[4]=True, "co" in dict? No
  dp[6] = False

i=7: s[0:7] = "leetcod"
  j=4: dp[4]=True, "cod" in dict? No
  dp[7] = False

i=8: s[0:8] = "leetcode"
  j=4: dp[4]=True, "code" in dict? YES! ✓
  dp[8] = True

Final: dp[8] = True ✓
```

**Visual Understanding:**

```
s = "leetcode"
     ┌───┐     ┌────┐
     │leet│     │code│
     └───┘     └────┘
     0   4     4    8

dp: [T, F, F, F, T, F, F, F, T]
     0  1  2  3  4  5  6  7  8

     ↑           ↑           ↑
   empty       "leet"    "leetcode"
```

**Optimization - Use Max Word Length:**

```python
def wordBreak(s, wordDict):
    word_set = set(wordDict)
    max_len = max(len(w) for w in wordDict)  # Optimization
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        # Only check last max_len characters
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]
```

**Why This Works:**

If max word length is 10, no need to check j < i-10. This reduces inner loop from O(i) to O(max_len), making overall complexity O(n × max_len × m) instead of O(n² × m).

**Common Bugs:**

❌ **Wrong:** Forget to convert wordDict to set
```python
# Linear search O(k) for each check
if s[j:i] in wordDict:  # List lookup is O(k)!
```

✅ **Correct:** Use set for O(1) lookup
```python
word_set = set(wordDict)  # O(1) average lookup
if s[j:i] in word_set:
```

❌ **Wrong:** Off-by-one on dp array size
```python
dp = [False] * n  # Wrong! Need n+1 for dp[0]
```

✅ **Correct:** Size n+1 for positions 0 to n
```python
dp = [False] * (n + 1)  # dp[0] represents empty string
```

**Key Insights:**
1. **dp[i] means s[0:i]** - represents prefix of length i
2. **dp[0] = True** - empty string base case is crucial
3. **Break early** - once dp[i] = True, no need to check more j
4. **Set for dictionary** - O(1) lookup vs O(k) for list
5. **Max word length optimization** - significant speedup in practice

**Complexity:**
- **Time:** O(n² × m) where m = average word length (substring operation)
- **Optimized:** O(n × k × m) where k = max word length
- **Space:** O(n) for dp array + O(total dict size) for set

---

### #099 Best Time to Buy and Sell Stock III ⭐

**Difficulty:** Hard | **Frequency:** 32.0%

**Task:** Find max profit with **at most 2 transactions**.

**Input:** `prices = [3,3,5,0,0,3,1,4]`
**Output:** `6`
**Explanation:** Buy at 0, sell at 3 (+3), buy at 1, sell at 4 (+3) → total 6

**What Makes This Special:**

This is **state machine DP** at its finest. You're not just tracking "what's the max profit at position i" - you're tracking **which state you're in** and how to transition between states.

**The States:**

```
Initial (no transactions)
    ↓ buy
[Buy 1] ← After first purchase (negative profit)
    ↓ sell
[Sell 1] ← After first sale (positive profit)
    ↓ buy
[Buy 2] ← After second purchase (profit minus new cost)
    ↓ sell
[Sell 2] ← After second sale (final profit)
```

**The State Machine:**

```python
buy1 = -inf   # Max profit after buying first stock
sell1 = 0     # Max profit after selling first stock
buy2 = -inf   # Max profit after buying second stock
sell2 = 0     # Max profit after selling second stock

For each price:
    buy1 = max(buy1, -price)           # Buy first stock
    sell1 = max(sell1, buy1 + price)   # Sell first stock
    buy2 = max(buy2, sell1 - price)    # Buy second stock
    sell2 = max(sell2, buy2 + price)   # Sell second stock
```

**Why This Works:**

- `buy1 = max(buy1, -price)`: Either keep previous buy1, or buy today at cost -price
- `sell1 = max(sell1, buy1 + price)`: Either keep previous sell1, or sell today (profit = buy1 + price)
- `buy2 = max(buy2, sell1 - price)`: Buy second stock using profit from sell1
- `sell2 = max(sell2, buy2 + price)`: Sell second stock for final profit

**Step-by-Step Example:**

```
prices = [3, 3, 5, 0, 0, 3, 1, 4]

Initial:
  buy1 = -∞, sell1 = 0, buy2 = -∞, sell2 = 0

Day 0 (price=3):
  buy1 = max(-∞, -3) = -3      ← Buy at 3
  sell1 = max(0, -3+3) = 0     ← Sell immediately (no profit)
  buy2 = max(-∞, 0-3) = -3     ← Buy second at 3
  sell2 = max(0, -3+3) = 0     ← Sell second immediately

Day 1 (price=3):
  buy1 = max(-3, -3) = -3      ← No change
  sell1 = max(0, -3+3) = 0     ← No change
  buy2 = max(-3, 0-3) = -3     ← No change
  sell2 = max(0, -3+3) = 0     ← No change

Day 2 (price=5):
  buy1 = max(-3, -5) = -3      ← Keep previous buy
  sell1 = max(0, -3+5) = 2     ← Sell for profit 2!
  buy2 = max(-3, 2-5) = -3     ← Keep previous buy2
  sell2 = max(0, -3+5) = 2     ← Could sell for 2

Day 3 (price=0):
  buy1 = max(-3, -0) = 0       ← Buy at 0! (profit 0)
  sell1 = max(2, 0+0) = 2      ← Keep previous sell1
  buy2 = max(-3, 2-0) = 2      ← Buy second at 0 (profit 2)!
  sell2 = max(2, 2+0) = 2      ← Keep

Day 4 (price=0):
  buy1 = max(0, -0) = 0        ← No change
  sell1 = max(2, 0+0) = 2      ← No change
  buy2 = max(2, 2-0) = 2       ← No change
  sell2 = max(2, 2+0) = 2      ← No change

Day 5 (price=3):
  buy1 = max(0, -3) = 0        ← Keep previous
  sell1 = max(2, 0+3) = 3      ← Sell for profit 3!
  buy2 = max(2, 3-3) = 2       ← Keep previous
  sell2 = max(2, 2+3) = 5      ← Sell second for 5!

Day 6 (price=1):
  buy1 = max(0, -1) = 0        ← Keep
  sell1 = max(3, 0+1) = 3      ← Keep
  buy2 = max(2, 3-1) = 2       ← Buy at 1 with profit 2
  sell2 = max(5, 2+1) = 5      ← Keep

Day 7 (price=4):
  buy1 = max(0, -4) = 0        ← Keep
  sell1 = max(3, 0+4) = 4      ← Sell for 4!
  buy2 = max(2, 4-4) = 2       ← Keep
  sell2 = max(5, 2+4) = 6      ← Sell second for 6! ✓

Final: sell2 = 6 ✓
```

**Visual Understanding:**

```
Prices:  3   3   5   0   0   3   1   4
             └───┘       └───────────┘
             Txn 1       Txn 2
           Buy at 0   Buy at 0/1
           Sell at 5  Sell at 4
           Profit: ?  Total: 6

Actually optimal:
Prices:  3   3   5   0   0   3   1   4
                 └───┘       └───────┘
                 Buy at 0    Buy at 1
                 Sell at 3   Sell at 4
                 Profit: 3   Profit: 3
```

**Alternative: Two-Pass Approach**

```python
def maxProfit(prices):
    n = len(prices)

    # Pass 1: Max profit with 1 transaction ending at or before i
    left = [0] * n
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        left[i] = max(left[i-1], prices[i] - min_price)

    # Pass 2: Max profit with 1 transaction starting at or after i
    right = [0] * n
    max_price = prices[-1]
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        right[i] = max(right[i+1], max_price - prices[i])

    # Combine: partition at position i
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, left[i] + right[i])

    return max_profit
```

**Why Two-Pass Works:**

- `left[i]` = max profit from one transaction in `prices[0:i+1]`
- `right[i]` = max profit from one transaction in `prices[i:]`
- At partition i: total profit = left[i] + right[i]
- Try all partitions, take maximum

**Common Bugs:**

❌ **Wrong:** Update states in wrong order
```python
buy1 = max(buy1, -price)
buy2 = max(buy2, sell1 - price)  # Using OLD sell1!
sell1 = max(sell1, buy1 + price) # Should update before buy2
```

✅ **Correct:** Update in order: buy1 → sell1 → buy2 → sell2
```python
buy1 = max(buy1, -price)
sell1 = max(sell1, buy1 + price)   # Use updated buy1
buy2 = max(buy2, sell1 - price)    # Use updated sell1
sell2 = max(sell2, buy2 + price)   # Use updated buy2
```

Or update simultaneously:
```python
new_buy1 = max(buy1, -price)
new_sell1 = max(sell1, buy1 + price)
new_buy2 = max(buy2, sell1 - price)
new_sell2 = max(sell2, buy2 + price)
buy1, sell1, buy2, sell2 = new_buy1, new_sell1, new_buy2, new_sell2
```

❌ **Wrong:** Initialize buy states to 0
```python
buy1 = buy2 = 0  # Wrong! Can't have positive profit after buying
```

✅ **Correct:** Initialize to -∞ (or very negative)
```python
buy1 = buy2 = float('-inf')  # Buying costs money!
```

**Key Insights:**
1. **State machine models transactions** - explicit states for each action
2. **Order matters** - update states in dependency order
3. **buy states are negative** - represent cost of holding stock
4. **sell states are positive** - represent profit realized
5. **Generalizes to k transactions** - just add more states!

**Complexity:**
- **State Machine:** Time O(n), Space O(1)
- **Two-Pass:** Time O(n), Space O(n)

---

### #055 Subsets

**Difficulty:** Medium | **Frequency:** 47.0%

**Task:** Generate all possible subsets of array (power set).

**Input:** `nums = [1,2,3]`
**Output:** `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`

**What Makes This Special:**

This is **NOT a DP problem** - it's combinatorics/backtracking! No overlapping subproblems, no optimal substructure. We must generate all 2ⁿ subsets explicitly.

**Three Approaches:**

1. **Backtracking (Most Intuitive):**
   ```python
   def subsets(nums):
       result = []

       def backtrack(start, current):
           result.append(current[:])  # Add current subset

           for i in range(start, len(nums)):
               current.append(nums[i])       # Choose
               backtrack(i + 1, current)     # Explore
               current.pop()                 # Unchoose

       backtrack(0, [])
       return result
   ```

2. **Iterative (Clever):**
   ```python
   def subsets(nums):
       result = [[]]  # Start with empty set

       for num in nums:
           # For each existing subset, create new subset with num
           result += [curr + [num] for curr in result]

       return result
   ```

3. **Bit Manipulation (Mathematical):**
   ```python
   def subsets(nums):
       n = len(nums)
       result = []

       # 2^n possible subsets
       for mask in range(1 << n):
           subset = []
           for i in range(n):
               # Check if ith bit is set
               if mask & (1 << i):
                   subset.append(nums[i])
           result.append(subset)

       return result
   ```

**Step-by-Step (Iterative):**

```
nums = [1, 2, 3]

Initial: result = [[]]

Add 1:
  For each existing subset, add version with 1:
  [] → [1]
  result = [[], [1]]

Add 2:
  [] → [2]
  [1] → [1, 2]
  result = [[], [1], [2], [1, 2]]

Add 3:
  [] → [3]
  [1] → [1, 3]
  [2] → [2, 3]
  [1, 2] → [1, 2, 3]
  result = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Done! 2³ = 8 subsets ✓
```

**Bit Manipulation Explanation:**

```
nums = [1, 2, 3]

Binary representation of 0 to 7:
000 → include nothing      → []
001 → include nums[0]      → [1]
010 → include nums[1]      → [2]
011 → include nums[0,1]    → [1,2]
100 → include nums[2]      → [3]
101 → include nums[0,2]    → [1,3]
110 → include nums[1,2]    → [2,3]
111 → include nums[0,1,2]  → [1,2,3]

Each bit position corresponds to whether to include that element!
```

**Key Insights:**
1. **Not DP** - exhaustive search required
2. **2ⁿ subsets always** - cannot be optimized below this
3. **Three equivalent approaches** - pick whichever is clearest
4. **Backtracking pattern** - useful for permutations, combinations too

**Complexity:**
- **Time:** O(2ⁿ × n) - generate 2ⁿ subsets, each takes O(n) to copy
- **Space:** O(2ⁿ × n) - output size dominates

---

## 🔗 Algorithm Relationships

| If You Can Solve... | Then You Can Solve... | By Adding... |
|---------------------|----------------------|--------------|
| #018 Stock I | #099 Stock III | State machine with 2 transactions |
| #075 Word Break | Palindrome Partitioning | Similar DP structure |
| #099 Stock III | Stock IV (k transactions) | Generalize to k states |
| #055 Subsets | Permutations | Change backtracking to use visited array |

---

## ⚠️ Universal Common Pitfalls

### 1. Wrong DP Array Size

❌ **Wrong:**
```python
dp = [0] * n  # Missing dp[0] for base case!
```

✅ **Correct:**
```python
dp = [0] * (n + 1)  # dp[0] represents empty/base case
```

### 2. Forget Base Case

❌ **Wrong:**
```python
dp = [False] * (n + 1)
# Forgot dp[0] = True!
```

✅ **Correct:**
```python
dp = [False] * (n + 1)
dp[0] = True  # Empty string/zero elements base case
```

### 3. Using List Instead of Set for Lookup

❌ **Wrong:**
```python
if word in wordDict:  # O(k) lookup if list!
```

✅ **Correct:**
```python
word_set = set(wordDict)
if word in word_set:  # O(1) average lookup
```

### 4. State Machine Update Order

❌ **Wrong:**
```python
sell1 = max(sell1, buy1 + price)  # Uses new buy1!
buy1 = max(buy1, -price)          # Updated after
```

✅ **Correct:**
```python
buy1 = max(buy1, -price)          # Update first
sell1 = max(sell1, buy1 + price)  # Use updated buy1
```

---

## ✅ Testing Strategy

### Test Categories:

1. **Size Edge Cases:**
   - Empty: `arr = []`
   - Single element: `arr = [x]`
   - Two elements: `arr = [x, y]`

2. **Value Edge Cases:**
   - All same: `arr = [5,5,5,5]`
   - Monotonic increasing: `arr = [1,2,3,4]`
   - Monotonic decreasing: `arr = [4,3,2,1]`

3. **DP-Specific:**
   - Base case: Does dp[0] work correctly?
   - No solution: e.g., prices only decrease
   - Optimal solution requires all elements

---

## 💎 Mastery Insights

### The DP Recipe:

1. **Define subproblem**: What does dp[i] or dp[i][j] represent?
2. **Find recurrence**: How does dp[i] relate to smaller subproblems?
3. **Identify base cases**: What are the trivial cases?
4. **Determine computation order**: Bottom-up or top-down?
5. **Optimize space**: Can you reduce dimensions?

### When is it DP?

✅ **Yes:**
- "Maximum/minimum value"
- "Number of ways"
- "Is it possible"
- Overlapping subproblems
- Optimal substructure

❌ **No:**
- "Generate all" (unless counting)
- No overlapping subproblems
- Greedy works

### DP vs Greedy:

| DP | Greedy |
|----|--------|
| Considers all options at each step | Makes locally optimal choice |
| O(n²) or higher typical | O(n) typical |
| Word Break, Stock III | Stock I, Activity Selection |

---

## 📚 Study Order & Practice Progression

### Week 1: Foundation
1. **#018 Stock I** - Understand greedy → DP connection (< 10 min)
2. Practice similar: Climbing Stairs, Min Cost Climbing Stairs

### Week 2: Classic DP
3. **#075 Word Break** - Master 1D DP pattern (< 20 min)
4. Practice similar: Coin Change, House Robber

### Week 3: Advanced
5. **#099 Stock III** - State machine DP (< 30 min)
6. Practice similar: Stock IV, Best Time to Buy/Sell with Cooldown

### Week 4: Mastery
7. **#055 Subsets** - Recognize non-DP patterns
8. Practice: Combination Sum, Permutations

### Mastery Criteria:
- ✅ Can identify DP pattern in problem statement
- ✅ Can derive recurrence relation from problem description
- ✅ Can implement both top-down and bottom-up
- ✅ Can optimize space complexity
- ✅ Know when NOT to use DP

---

## 🎯 Interview Tips

### Communication Template:

**For 1D DP:**
> "I'll use dynamic programming. I'll define dp[i] as [meaning]. The base case is dp[0] = [value] because [reason]. The recurrence relation is dp[i] = [formula] because [reasoning]. The answer will be dp[n]."

**For State Machine:**
> "I'll model this as a state machine with states [list states]. Each state represents [meaning]. Transitions occur when [action], updating state values according to [rules]. The final answer is [final state]."

### Common Follow-Ups:

1. **"Can you optimize space?"**
   - Check if dp[i] only depends on recent values
   - If dp[i] depends only on dp[i-1], dp[i-2], use variables instead of array

2. **"What if constraints change?"**
   - Stock I → Stock II: Unlimited transactions
   - Stock II → Stock III: Limit to 2 transactions
   - Stock III → Stock IV: Generalize to k transactions

3. **"Can you do it recursively?"**
   - Show top-down with memoization
   - Explain bottom-up avoids recursion overhead

### Time Budgets (45-min interview):

- Easy (#018): 10-15 min
- Medium (#075): 15-25 min
- Hard (#099): 25-35 min

---

## 📈 Complexity Summary

| Problem | Time | Space | Pattern |
|---------|------|-------|---------|
| #018 Stock I | O(n) | O(1) | Greedy (DP mindset) |
| #075 Word Break | O(n² × m) | O(n) | 1D DP on strings |
| #099 Stock III | O(n) | O(1) | State machine DP |
| #055 Subsets | O(2ⁿ × n) | O(2ⁿ × n) | Backtracking (not DP) |

---

## 🏆 From Good to Great

### Good: Implement the DP solution
### Great: Understand why DP works

**Master these insights:**

1. **Optimal substructure**: Global optimum contains local optima
2. **Overlapping subproblems**: Same problems solved repeatedly
3. **Memoization = top-down**: Cache recursive results
4. **Tabulation = bottom-up**: Build table iteratively
5. **State machine**: Model problem as transitions between states

### DP Patterns Cheat Sheet:

| Pattern | Keywords | Example |
|---------|----------|---------|
| 1D Linear | "Maximum/minimum in sequence" | Stock I, Climbing Stairs |
| 1D on Strings | "Can segment/match string" | Word Break, Palindrome |
| 2D Grid | "Paths in grid" | Unique Paths, Min Path Sum |
| State Machine | "Transitions with constraints" | Stock III, Best Time with Cooldown |
| Interval DP | "Subproblems on contiguous intervals" | Burst Balloons, MCM |

---

[← Back to Main](../README.md)
