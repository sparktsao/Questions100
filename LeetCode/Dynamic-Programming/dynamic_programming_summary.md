# Dynamic Programming - Comprehensive Mastery Guide

## 📋 Problems in This Category

- [018. Best Time to Buy and Sell Stock](./018_best_time_to_buy_and_sell_stock.md) - `Greedy/DP Hybrid` (EASY, 76.4%)
- [075. Word Break](./075_word_break.md) - `1D DP on Strings` (MEDIUM, 40.7%)
- [087. Maximum Subarray](./087_maximum_subarray.md) - `Kadane's Algorithm` (MEDIUM, 32.0%)
- [099. Best Time to Buy and Sell Stock III](./099_best_time_to_buy_and_sell_stock_iii.md) - `State Machine DP` (HARD, 32.0%)

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

## 🔍 Critical Insight: Problem Pattern Comparison

### The Four Patterns

| # | Problem | Pattern Type | Core DP Property | Time | Space |
|---|---------|--------------|------------------|------|-------|
| 018 | Buy/Sell Stock I | Greedy (DP mindset) | Track single state (min price) | O(n) | O(1) |
| 087 | Maximum Subarray | 1D DP (Kadane's) | dp[i] = max ending at i | O(n) | O(1) optimized |
| 075 | Word Break | 1D DP on Strings | dp[i] = can segment s[0:i]? | O(n²) | O(n) |
| 099 | Buy/Sell Stock III | State Machine DP | Multiple states with transitions | O(n) | O(1) |

**Key Observation:** All 4 are linear scan problems, but use fundamentally different DP approaches!

---

## 📊 Pattern Comparison Matrix

### Similarity Analysis

```
                    Single    Multiple   Decision    Dependency
                    Pass      Decisions  At Each     On Previous
                                         Step        Choices
─────────────────────────────────────────────────────────────────
Stock I (#018)      ✓         ✗          Simple      Min price so far
Max Subarray (#087) ✓         ✓          Reset/Cont  Previous sum
Word Break (#075)   ✗         ✓          Try splits  All previous dp[j]
Stock III (#099)    ✓         ✓          4 states    State machine
```

### What Makes Each Unique?

#### 1. Stock I: Simplest - Pure Greedy
**Why it's easy:** Only ONE decision variable (minimum price seen).

**No actual DP recurrence:** Just track running minimum.

```python
min_price = min(min_price, price)  # Update minimum
max_profit = max(max_profit, price - min_price)  # Calculate profit
```

**Could be written as DP (but overkill):**
```python
# dp[i] = max profit selling at or before day i
# dp[i] = max(dp[i-1], prices[i] - min_price_so_far)
# But we don't need the array!
```

**Pattern:** Running aggregation (min/max tracking)

---

#### 2. Maximum Subarray: Classic 1D DP
**Why it's intermediate:** Decision at each element - extend subarray or start new?

**Actual DP recurrence:**
```python
# dp[i] = maximum sum ending at index i
dp[i] = max(nums[i], dp[i-1] + nums[i])
       ↑             ↑
    Start new    Extend existing
```

**Key insight:** dp[i] **must include nums[i]** (ending at i, not "up to i").

**Space optimization:**
```python
# Only need previous value, not entire array
max_ending_here = max(num, max_ending_here + num)
max_so_far = max(max_so_far, max_ending_here)
```

**Pattern:** Local vs global optimization

---

#### 3. Word Break: Most "DP-Like"
**Why it's complex:** Must check ALL previous positions for valid splits.

**True DP recurrence:**
```python
# dp[i] = can we segment s[0:i]?
for j in range(i):
    if dp[j] and s[j:i] in wordDict:
        dp[i] = True
        break
```

**Key insight:** dp[i] depends on **any** dp[j] where j < i, not just dp[i-1].

**Overlapping subproblems:** Checking if s[0:5] valid requires knowing if s[0:2], s[0:3], s[0:4] are valid.

**Pattern:** Partition point search (try all split positions)

---

#### 4. Stock III: State Machine DP
**Why it's hard:** Multiple interdependent states, complex transitions.

**State machine recurrence:**
```python
# Four states: buy1, sell1, buy2, sell2
buy1 = max(buy1, -price)           # First purchase
sell1 = max(sell1, buy1 + price)   # First sale
buy2 = max(buy2, sell1 - price)    # Second purchase
sell2 = max(sell2, buy2 + price)   # Second sale
```

**Key insight:** States depend on each other **in order**. Update sequence matters!

**Why not array DP:** Fixed number of states (4), not variable with input size.

**Pattern:** Finite state machine with value tracking

---

## 🔬 Deep Dive: Why These Look Similar But Aren't

### Stock I vs Maximum Subarray

**Both:**
- Linear scan
- O(n) time, O(1) space
- Track running values

**Different:**

| Aspect | Stock I | Maximum Subarray |
|--------|---------|------------------|
| **Decision** | Buy at min, sell at current | Extend subarray or start new |
| **DP Nature** | Not really DP (greedy) | True DP (Kadane's) |
| **Recurrence** | None (just track min) | dp[i] = max(nums[i], dp[i-1] + nums[i]) |
| **Can reset?** | No (once bought, stuck) | Yes (can start fresh subarray) |

**Visual Comparison:**

```
Stock I:
prices = [7, 1, 5, 3, 6, 4]
          ↓  ↓  ↑     ↑
       Min found   Sell here

Just track: What's the cheapest I've seen?

Maximum Subarray:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
            ↑       ↑←─────────┘
         Reset    Extend subarray

Decision each step: Continue or restart?
```

---

### Word Break vs Maximum Subarray

**Both:**
- Build solution incrementally
- dp[i] represents "solution up to index i"

**Different:**

| Aspect | Word Break | Maximum Subarray |
|--------|------------|------------------|
| **dp[i] depends on** | ANY dp[j] < i | Only dp[i-1] |
| **Inner loop** | Must try all j | No inner loop |
| **Time complexity** | O(n²) | O(n) |
| **Space required** | Array dp[0..n] | Can use single variable |

**Why Word Break needs O(n²):**
```python
# Word Break: Must check ALL split points
for i in range(n):          # O(n)
    for j in range(i):      # O(i) average = O(n)
        if dp[j] and s[j:i] in dict:
            dp[i] = True

# Max Subarray: Only depends on previous
max_ending_here = max(num, max_ending_here + num)  # O(1)
```

---

### Stock I vs Stock III

**Both:**
- Process prices left to right
- Track state across iterations

**Different:**

| Aspect | Stock I (Greedy) | Stock III (State Machine) |
|--------|------------------|---------------------------|
| **Transactions** | 1 | 2 |
| **States** | 2 (min_price, max_profit) | 4 (buy1, sell1, buy2, sell2) |
| **Complexity** | Trivial (2 variables) | Complex (state dependencies) |
| **Approach** | Track minimum | Track all states |

**How Stock III generalizes Stock I:**
```python
# Stock I (1 transaction):
min_price = min(min_price, price)
max_profit = max(max_profit, price - min_price)

# Stock III (2 transactions):
buy1 = max(buy1, -price)           # Same as -min_price
sell1 = max(sell1, buy1 + price)   # Same as max_profit
buy2 = max(buy2, sell1 - price)    # Second transaction start
sell2 = max(sell2, buy2 + price)   # Second transaction end

# Stock I is just the first two lines of Stock III!
```

---

## 📚 Four Core Patterns Explained

### Pattern 1: Greedy with DP Mindset (Stock I)

**Recognition:**
- "Maximize/minimize with single pass"
- Only need to track aggregate (min/max/sum)
- No actual overlapping subproblems

**Template:**
```python
def greedy_optimize(arr):
    tracker = initial_value
    result = initial_result

    for val in arr:
        tracker = update_tracker(tracker, val)
        result = optimize(result, compute(tracker, val))

    return result
```

**When to use:** Problem seems like DP but only needs running min/max/sum.

---

### Pattern 2: Linear DP (Kadane's Algorithm)

**Recognition:**
- "Maximum/minimum subarray/subsequence"
- Decision: extend current or start new
- dp[i] depends only on dp[i-1]

**Template:**
```python
def kadane_pattern(arr):
    # dp[i] = max value ending at i
    max_ending_here = arr[0]
    max_so_far = arr[0]

    for i in range(1, len(arr)):
        # Extend or restart
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        # Update global max
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
```

**Key insight:** "Ending at i" vs "up to i" - crucial distinction!

**When to use:** Contiguous subarray problems with extend/restart decision.

---

### Pattern 3: Partition DP (Word Break)

**Recognition:**
- "Can we partition/segment sequence?"
- "Does there exist a way to split?"
- dp[i] depends on checking ALL dp[j] < i

**Template:**
```python
def partition_dp(s, options):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty is valid

    for i in range(1, n + 1):
        # Try all partition points
        for j in range(i):
            if dp[j] and s[j:i] in options:
                dp[i] = True
                break  # Early exit when found

    return dp[n]
```

**Optimization:** Use max option length to limit inner loop.

**When to use:** String/array segmentation, partition problems.

---

### Pattern 4: State Machine DP (Stock III)

**Recognition:**
- "At most K transactions/operations"
- Explicit states with transitions
- States depend on each other

**Template:**
```python
def state_machine_dp(arr):
    # Define states
    state1 = initial1
    state2 = initial2
    # ... more states

    for val in arr:
        # Update in dependency order!
        new_state1 = transition1(state1, val)
        new_state2 = transition2(state1, state2, val)
        # ... update remaining states

        # Apply updates
        state1, state2 = new_state1, new_state2

    return final_state
```

**Critical:** Update order matters! States must be updated in dependency order.

**When to use:** Limited operations, state transitions, constraints like "cooldown" or "at most K".

---

## 🎓 Learning Progression Path

### Stage 1: Foundation (Week 1)
**Problem:** #018 Best Time to Buy/Sell Stock

**Goal:** Understand greedy → DP connection

**What to learn:**
- How to track running minimum/maximum
- Why greedy works (optimal substructure)
- Difference between "true DP" and "DP thinking"

**Practice:** Can solve in < 10 minutes

---

### Stage 2: Classic DP (Week 2)
**Problem:** #087 Maximum Subarray

**Goal:** Master Kadane's algorithm and local/global optimization

**What to learn:**
- "Ending at i" vs "up to i" distinction
- When to reset vs extend
- Space optimization (array → variable)

**Key drill:** Implement 3 versions:
1. Brute force O(n²)
2. DP with array O(n) space
3. Optimized O(1) space

**Practice:** Can explain all 3 approaches in < 15 minutes

---

### Stage 3: String DP (Week 3)
**Problem:** #075 Word Break

**Goal:** Understand partition DP and O(n²) necessity

**What to learn:**
- Why we need O(n²) (checking all split points)
- Set vs list for O(1) lookups
- Max word length optimization
- Top-down vs bottom-up

**Key drill:** Implement both memoization and tabulation

**Practice:** Can solve in < 20 minutes

---

### Stage 4: Advanced State Machine (Week 4)
**Problem:** #099 Best Time to Buy/Sell Stock III

**Goal:** Master state machine DP with complex transitions

**What to learn:**
- How to identify states
- State transition rules
- Update order importance
- Alternative: two-pass DP approach

**Key drill:**
1. Draw state diagram first
2. Implement state machine
3. Implement two-pass alternative
4. Compare approaches

**Practice:** Can solve in < 30 minutes

---

## 🔄 Problem Relationships & Progression

```
Level 1: Greedy Foundation
  └─ #018 Buy/Sell Stock I
     ↓ [Add decision: reset or extend]
Level 2: Linear DP
  └─ #087 Maximum Subarray (Kadane's)
     ↓ [Add: check all previous positions]
Level 3: Partition DP
  └─ #075 Word Break
     ↓ [Add: multiple constrained operations]
Level 4: State Machine
  └─ #099 Buy/Sell Stock III
```

**Skill Building:**
- Stock I → Stock III: See how to generalize simple to complex
- Max Subarray → Word Break: Understand when O(n²) is needed
- Word Break → Stock III: Both need careful state management

---

## 🔍 Deep Comparison: All Four Side-by-Side

### Example Input Walkthrough

Let's trace how each algorithm processes similar-length arrays:

#### Stock I: prices = [7, 1, 5, 3, 6, 4]

```
i=0: min=7, profit=0
i=1: min=1, profit=0
i=2: min=1, profit=4  ← price(5) - min(1)
i=3: min=1, profit=4
i=4: min=1, profit=5  ← price(6) - min(1) ✓
i=5: min=1, profit=5

Result: 5 (buy at 1, sell at 6)
```

---

#### Maximum Subarray: nums = [-2, 1, -3, 4, -1, 2, 1]

```
i=0: max_end=-2, max_so_far=-2
i=1: max_end=1 (restart!), max_so_far=1
i=2: max_end=-2 (extend 1-3), max_so_far=1
i=3: max_end=4 (restart!), max_so_far=4
i=4: max_end=3 (extend 4-1), max_so_far=4
i=5: max_end=5 (extend 3+2), max_so_far=5
i=6: max_end=6 (extend 5+1), max_so_far=6 ✓

Result: 6 (subarray [4,-1,2,1])
```

---

#### Word Break: s = "leetcode", dict = ["leet", "code"]

```
dp[0] = True (empty)
dp[1] = False ("l" not in dict)
dp[2] = False ("le" not in dict)
dp[3] = False ("lee" not in dict)
dp[4] = True  ("leet" in dict, dp[0]=True) ✓
dp[5] = False ("c" not in dict from position 4)
dp[6] = False ("co" not in dict from position 4)
dp[7] = False ("cod" not in dict from position 4)
dp[8] = True  ("code" in dict, dp[4]=True) ✓

Result: True (can segment as "leet" + "code")
```

---

#### Stock III: prices = [3, 3, 5, 0, 0, 3, 1, 4]

```
Init: buy1=-∞, sell1=0, buy2=-∞, sell2=0

i=0 (p=3): buy1=-3, sell1=0, buy2=-3, sell2=0
i=1 (p=3): buy1=-3, sell1=0, buy2=-3, sell2=0
i=2 (p=5): buy1=-3, sell1=2, buy2=-3, sell2=2
i=3 (p=0): buy1=0, sell1=2, buy2=2, sell2=2  ← buy at 0!
i=4 (p=0): buy1=0, sell1=2, buy2=2, sell2=2
i=5 (p=3): buy1=0, sell1=3, buy2=2, sell2=5
i=6 (p=1): buy1=0, sell1=3, buy2=2, sell2=5
i=7 (p=4): buy1=0, sell1=4, buy2=2, sell2=6 ✓

Result: 6 (two transactions: profit 3 + profit 3)
```

---

### Complexity Breakdown

| Problem | Time | Why | Space | Why |
|---------|------|-----|-------|-----|
| Stock I | O(n) | Single pass, O(1) per element | O(1) | Two variables |
| Max Subarray | O(n) | Single pass, O(1) per element | O(1) | Two variables |
| Word Break | O(n²×m) | Nested loops + substring check | O(n) | DP array |
| Stock III | O(n) | Single pass, O(1) per element | O(1) | Four states |

**Why Word Break is slower:**
```
Stock I/Max/Stock III: for i in range(n):    # O(n)
                           O(1) work

Word Break:            for i in range(n):    # O(n)
                           for j in range(i): # O(n)
                               O(m) work      # substring
                       Total: O(n² × m)
```

---

## ⚠️ Common Pitfalls & How to Avoid

### Mistake 1: Confusing "ending at i" with "up to i"

**Wrong (Max Subarray):**
```python
# dp[i] = max sum in nums[0:i+1]  ← WRONG!
dp[i] = max(dp[i-1], nums[i], nums[i] + dp[i-1])
```

**Correct:**
```python
# dp[i] = max sum ENDING at i  ← CORRECT!
dp[i] = max(nums[i], nums[i] + dp[i-1])
```

**Why it matters:** If dp[i] can skip nums[i], you lose the local/global optimization structure.

---

### Mistake 2: Updating state machine in wrong order

**Wrong (Stock III):**
```python
# Updates sell1 before buy1 is updated!
sell1 = max(sell1, buy1 + price)  # Uses OLD buy1
buy1 = max(buy1, -price)          # Updates after
```

**Correct:**
```python
# Update in dependency order
buy1 = max(buy1, -price)
sell1 = max(sell1, buy1 + price)  # Uses NEW buy1
buy2 = max(buy2, sell1 - price)
sell2 = max(sell2, buy2 + price)
```

**Alternative: Simultaneous update:**
```python
new_buy1 = max(buy1, -price)
new_sell1 = max(sell1, buy1 + price)  # Uses OLD buy1
new_buy2 = max(buy2, sell1 - price)
new_sell2 = max(sell2, buy2 + price)
buy1, sell1, buy2, sell2 = new_buy1, new_sell1, new_buy2, new_sell2
```

---

### Mistake 3: Using list instead of set for Word Break

**Wrong:**
```python
if s[j:i] in wordDict:  # O(k) lookup if list!
```

**Impact:** O(n² × m × k) instead of O(n² × m)

**Correct:**
```python
word_set = set(wordDict)  # One-time conversion
if s[j:i] in word_set:    # O(1) average lookup
```

---

### Mistake 4: Forgetting dp[0] base case

**Wrong:**
```python
dp = [False] * n  # Missing dp[0]!
```

**Correct:**
```python
dp = [False] * (n + 1)  # dp[0] = empty string
dp[0] = True
```

**Why it matters:** dp[i] checks dp[j] for j < i, needs dp[0] for first word.

---

## ✅ Testing Strategy

### Test Matrix

| Test Type | Stock I | Max Subarray | Word Break | Stock III |
|-----------|---------|--------------|------------|-----------|
| **Empty/Single** | [5] → 0 | [5] → 5 | "" → true | [5] → 0 |
| **All negative** | N/A | [-1,-2,-3] → -1 | N/A | [5,4,3,2,1] → 0 |
| **All positive** | [1,2,3,4,5] → 4 | [1,2,3] → 6 | "aaa", ["a"] → true | [1,2,3,4,5] → 4 |
| **Descending** | [5,4,3,2,1] → 0 | [-1,-2,-3] → -1 | N/A | [5,4,3,2,1] → 0 |
| **No solution** | N/A | N/A | "aaab", ["aa"] → false | N/A |
| **Multiple solutions** | N/A | [1,-1,1,-1,1] | "aaa", ["a","aa"] | [1,2,3,4,5] |

### Edge Cases Checklist

**All problems:**
- [ ] Empty array/string
- [ ] Single element
- [ ] Two elements

**Stock problems:**
- [ ] Prices only increase
- [ ] Prices only decrease
- [ ] All same price

**Max Subarray:**
- [ ] All negative
- [ ] All positive
- [ ] Single negative

**Word Break:**
- [ ] Empty string (should be true)
- [ ] String not in any word
- [ ] Word can be reused
- [ ] Multiple valid segmentations

---

## 💎 Mastery Insights

### The DP Decision Tree

```
Can problem be solved in single pass?
│
├─ YES → Is decision at each step simple (min/max tracking)?
│  │
│  ├─ YES → Probably GREEDY (Stock I)
│  │
│  └─ NO → Does current decision depend on ALL previous?
│     │
│     ├─ NO → LINEAR DP (Max Subarray)
│     │
│     └─ YES → PARTITION DP (Word Break)
│           or STATE MACHINE (Stock III)
│
└─ NO → Likely need 2D DP or different approach
```

### When It's NOT DP

| Pattern | Actual Technique | Example |
|---------|------------------|---------|
| "Generate all" | Backtracking | Subsets, Permutations |
| "Find shortest path" | BFS/Dijkstra | Grid shortest path |
| "Is valid structure?" | Stack | Valid Parentheses |
| Single pass tracking | Greedy | Stock I (technically) |

### DP vs Greedy: The Definitive Guide

**Greedy works when:**
- Local optimal choice → global optimal
- No need to reconsider past decisions
- Example: Stock I (always buy at minimum)

**DP needed when:**
- Must consider multiple options at each step
- Past decisions affect future choices
- Example: Max Subarray (extend or restart?)

**Test:** Can you make choice without knowing future? If yes, try greedy first!

---

## 📈 Interview Communication Template

### For Linear DP (Kadane's):
> "I'll use Kadane's algorithm. I'll maintain two values: max_ending_here (max sum ending at current position) and max_so_far (global maximum). At each element, I decide whether to extend the current subarray or start fresh. If current sum becomes negative, I reset since any positive future elements would be better off starting fresh."

### For Partition DP (Word Break):
> "I'll use dynamic programming with dp[i] representing whether s[0:i] can be segmented. The base case is dp[0] = true for empty string. For each position i, I check all positions j < i to see if s[0:j] is valid AND s[j:i] is in the dictionary. I'll convert the dictionary to a set for O(1) lookups."

### For State Machine (Stock III):
> "I'll model this as a state machine with four states: buy1, sell1, buy2, sell2. Each represents the maximum profit after that action. I'll update them in order for each price, where buy1 represents buying first stock, sell1 represents selling it, buy2 represents buying second stock with profit from first, and sell2 is the final profit."

---

## 🎯 Quick Reference: Problem Selection Guide

**Need confidence builder?** → Start with Stock I (#018)
- Easiest, teaches DP thinking
- 10 minutes max

**Want to learn classic DP?** → Do Max Subarray (#087)
- Textbook Kadane's algorithm
- Teaches local vs global optimization
- 15 minutes

**Ready for real DP?** → Tackle Word Break (#075)
- True O(n²) DP
- Teaches partition pattern
- 25 minutes

**Want advanced challenge?** → Attempt Stock III (#099)
- State machine DP
- Multiple states, complex transitions
- 35 minutes

---

## 🏆 Mastery Checklist

### Foundation Level (Can solve Stock I, Max Subarray)
- [ ] Recognize when problem needs DP vs greedy
- [ ] Understand space optimization (array → variables)
- [ ] Can explain Kadane's algorithm intuitively
- [ ] Know difference between "ending at i" and "up to i"

### Intermediate Level (Can solve Word Break)
- [ ] Can write recurrence relation from problem description
- [ ] Understand when O(n²) is necessary
- [ ] Can implement both top-down and bottom-up
- [ ] Know common optimizations (max length, early break)

### Advanced Level (Can solve Stock III)
- [ ] Can identify states in state machine problems
- [ ] Understand state transition dependencies
- [ ] Can draw state diagram before coding
- [ ] Know alternative approaches (two-pass DP)

### Expert Level (Teaches others)
- [ ] Can compare different DP patterns
- [ ] Explains why certain approaches work/fail
- [ ] Recognizes DP variants in new problems
- [ ] Derives space optimizations independently

---

## 📋 Complete Problem Reference

| # | Problem | Difficulty | Frequency | Pattern | Time | Space | File |
|---|---------|------------|-----------|---------|------|-------|------|
| 018 | Buy/Sell Stock I | EASY | 76.4% | Greedy/DP Hybrid | O(n) | O(1) | [018_best_time_to_buy_and_sell_stock.md](./018_best_time_to_buy_and_sell_stock.md) |
| 075 | Word Break | MEDIUM | 40.7% | Partition DP | O(n²) | O(n) | [075_word_break.md](./075_word_break.md) |
| 087 | Maximum Subarray | MEDIUM | 32.0% | Kadane's (Linear DP) | O(n) | O(1) | [087_maximum_subarray.md](./087_maximum_subarray.md) |
| 099 | Buy/Sell Stock III | HARD | 32.0% | State Machine DP | O(n) | O(1) | [099_best_time_to_buy_and_sell_stock_iii.md](./099_best_time_to_buy_and_sell_stock_iii.md) |

---

[← Back to Main](../README.md)
