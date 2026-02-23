# Binary Search Mastery

## 📋 Problems in This Category

- [010. Find Peak Element](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/010_find_peak_element.md) - `Search Peak`
- [041. Kth Missing Positive Number](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/041_kth_missing_positive_number.md) - `Search Answer`
- [042. Find First and Last Position](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/042_find_first_and_last_position_of_element_in_sorted_array.md) - `Dual Binary Search`
- [074. Cutting Ribbons](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/074_cutting_ribbons.md) - `Search Answer (MAX)`
- [079. Capacity To Ship Packages](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/079_capacity_to_ship_packages_within_d_days.md) - `Search Capacity (MIN)`
- [084. Kth Smallest Element in Matrix](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/084_kth_smallest_element_in_a_sorted_matrix.md) - `Search Value Range`
- [094. Koko Eating Bananas](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/094_koko_eating_bananas.md) - `Search Speed (MIN)`
- [100. Median of Two Sorted Arrays](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/100_median_of_two_sorted_arrays.md) - `Search Partition`

---

## From Array Search to Answer Space Optimization

---

## 🎯 Category Overview

**Total Problems:** 8

**Core Insight:**
The fundamental insight of binary search is MONOTONICITY - if we can check a condition
and know which half of the search space to eliminate, we can solve in O(log n) time. This applies to:
1. Sorted arrays (traditional)
2. Unsorted arrays with monotonic properties
3. Answer spaces where "if X works, all values > X work" (or vice versa)

---

## 🔍 Critical Insight: Minimize vs Maximize - Different Code Strategies!

### The Problem Classification

Binary search on answer space divides into TWO fundamentally different patterns:

| Type | Goal | Monotonicity | Examples | Loop Condition | Mid Update |
|------|------|--------------|----------|----------------|------------|
| **MINIMIZE** | Find smallest value that satisfies condition | If X works, all Y > X work | Koko (#094), Ship Capacity (#079) | `while left < right` | `right = mid` |
| **MAXIMIZE** | Find largest value that satisfies condition | If X works, all Y < X work | Cutting Ribbons (#074) | `while left <= right` | `left = mid + 1` |

**Why this matters:** Using the wrong template causes infinite loops or wrong answers!

---

## 📊 Side-by-Side Comparison: Minimize vs Maximize

### Template Comparison

```python
# ============================================
# MINIMIZE TEMPLATE (Find SMALLEST valid value)
# ============================================
def binary_search_minimize(constraints):
    """
    Find minimum value where is_valid(value) = True

    Monotonicity: If X works → all Y > X work
    Example: Minimum speed to finish in time
    """
    def is_valid(candidate):
        # Returns True if candidate satisfies constraints
        pass

    left = minimum_possible_value
    right = maximum_possible_value

    while left < right:  # NOTE: < not <=
        mid = left + (right - left) // 2

        if is_valid(mid):
            # mid works, but search for smaller
            right = mid  # KEEP mid as candidate
        else:
            # mid doesn't work, need larger
            left = mid + 1

    return left  # left == right at termination


# ============================================
# MAXIMIZE TEMPLATE (Find LARGEST valid value)
# ============================================
def binary_search_maximize(constraints):
    """
    Find maximum value where is_valid(value) = True

    Monotonicity: If X works → all Y < X work
    Example: Maximum length that yields k pieces
    """
    def is_valid(candidate):
        # Returns True if candidate satisfies constraints
        pass

    left = minimum_possible_value
    right = maximum_possible_value
    result = 0  # Track best answer found

    while left <= right:  # NOTE: <= not <
        mid = left + (right - left) // 2

        if is_valid(mid):
            # mid works, save it and search for larger
            result = mid  # SAVE current answer
            left = mid + 1  # EXCLUDE mid
        else:
            # mid doesn't work, need smaller
            right = mid - 1

    return result
```

---

### Key Differences Table

| Aspect | MINIMIZE Template | MAXIMIZE Template |
|--------|-------------------|-------------------|
| **Loop Condition** | `while left < right` | `while left <= right` |
| **Mid Calculation** | `(left + right) // 2` | `(left + right) // 2` |
| **When Valid** | `right = mid` | `result = mid; left = mid + 1` |
| **When Invalid** | `left = mid + 1` | `right = mid - 1` |
| **Return Value** | `left` (or `right`, same value) | `result` |
| **Needs Result Variable** | ❌ No | ✅ Yes |
| **Mid Included in Search** | ✅ Yes (`right = mid`) | ❌ No (saved in result, then excluded) |

---

### Why These Differences?

#### MINIMIZE: Keep Mid Inclusive (`right = mid`)

```python
# Example: Find minimum speed
speeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#         ❌ ❌ ❌ ✅ ✅ ✅ ✅ ✅ ✅ ✅
#                 ↑ Answer is 4 (first valid)

# If mid = 6 works, answer could be 4, 5, or 6
# Must keep mid=6 in search space → right = mid
# If we used right = mid - 1, we might skip the answer!
```

**Infinite loop prevention:** Using `right = mid` requires `while left < right`
- When `left + 1 == right`, mid = left, then `right = mid = left` → loop terminates
- If we used `left <= right`, infinite loop when left == right == mid

---

#### MAXIMIZE: Exclude Mid (`left = mid + 1`)

```python
# Example: Find maximum length
lengths = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#          ✅ ✅ ✅ ✅ ✅ ✅ ❌ ❌ ❌ ❌
#                         ↑ Answer is 6 (last valid)

# If mid = 4 works, answer could be 4, 5, or 6
# Save 4 as current best, then EXCLUDE it → left = mid + 1
# Search [5, 6, ...] for potentially better answer
```

**Why save result separately?**
- We exclude mid from search space (`left = mid + 1`)
- But mid might be the final answer if nothing larger works
- Must save it before moving on

**Why use `left <= right`?**
- We're excluding mid on both sides (`left = mid + 1`, `right = mid - 1`)
- Need `<=` to check the final remaining element
- With `<`, we'd miss the last element

---

## 🔬 Deep Dive: Problem-Specific Analysis

### MINIMIZE Problems

#### #094 Koko Eating Bananas - Minimize Speed

**Question:** What's the **minimum** speed to finish in h hours?

**Monotonicity:** If speed k works → all speeds > k work (faster = always ok)

**Search Direction:** Find leftmost valid speed

```python
def minEatingSpeed(piles, h):
    def can_finish(speed):
        hours = sum((pile + speed - 1) // speed for pile in piles)
        return hours <= h

    left, right = 1, max(piles)

    while left < right:  # Minimize template
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid  # Works, try slower
        else:
            left = mid + 1  # Too slow, need faster

    return left

# Trace: piles = [3,6,7,11], h = 8
# Search space: [1, 11]
# mid=6: can_finish(6)=True → right=6, search [1,6]
# mid=3: can_finish(3)=False → left=4, search [4,6]
# mid=5: can_finish(5)=True → right=5, search [4,5]
# mid=4: can_finish(4)=True → right=4, search [4,4]
# Return 4 ✓
```

---

#### #079 Capacity To Ship Packages - Minimize Capacity

**Question:** What's the **minimum** capacity to ship in days?

**Monotonicity:** If capacity c works → all capacities > c work (larger = always ok)

**Search Direction:** Find leftmost valid capacity

```python
def shipWithinDays(weights, days):
    def can_ship(capacity):
        days_needed, current_load = 1, 0
        for w in weights:
            if current_load + w > capacity:
                days_needed += 1
                current_load = w
                if days_needed > days:
                    return False
            else:
                current_load += w
        return True

    left, right = max(weights), sum(weights)

    while left < right:  # Minimize template
        mid = (left + right) // 2
        if can_ship(mid):
            right = mid  # Works, try smaller
        else:
            left = mid + 1  # Too small, need larger

    return left
```

**Key Insight:** Both minimize problems use identical template structure!

---

### MAXIMIZE Problems

#### #074 Cutting Ribbons - Maximize Length

**Question:** What's the **maximum** length to get k pieces?

**Monotonicity:** If length L works → all lengths < L work (shorter = easier to achieve k pieces)

**Search Direction:** Find rightmost valid length

```python
def maxLength(ribbons, k):
    def can_cut(length):
        count = sum(r // length for r in ribbons)
        return count >= k

    left, right = 1, max(ribbons)
    result = 0  # MUST track result!

    while left <= right:  # Maximize template
        mid = (left + right) // 2
        if can_cut(mid):
            result = mid  # Save answer
            left = mid + 1  # Try longer
        else:
            right = mid - 1  # Too long, try shorter

    return result

# Trace: ribbons = [9,7,5], k = 3
# Search space: [1, 9]
# mid=5: can_cut(5)=True → result=5, left=6, search [6,9]
# mid=7: can_cut(7)=True → result=7, left=8, search [8,9]
# mid=8: can_cut(8)=False → right=7, search [8,7] (invalid)
# Return result=7
#
# Wait, let me recalculate: [9,7,5] with length 5
# 9//5=1, 7//5=1, 5//5=1 → count=3 ✓
# With length 7: 9//7=1, 7//7=1, 5//7=0 → count=2 ✗
# So answer should be 5, not 7
```

---

## ⚠️ Common Mistakes When Mixing Templates

### Mistake 1: Using MINIMIZE template for MAXIMIZE problem

```python
# WRONG: Using minimize template for cutting ribbons
def maxLength(ribbons, k):
    def can_cut(length):
        return sum(r // length for r in ribbons) >= k

    left, right = 1, max(ribbons)

    while left < right:  # ← Minimize template
        mid = (left + right) // 2
        if can_cut(mid):
            right = mid  # ← WRONG! Should try larger, not smaller
        else:
            left = mid + 1

    return left  # Returns MINIMUM valid length, not maximum!
```

**Result:** Returns smallest valid length instead of largest. Correct answer: 5, Wrong answer: 1

---

### Mistake 2: Using MAXIMIZE template for MINIMIZE problem

```python
# WRONG: Using maximize template for Koko
def minEatingSpeed(piles, h):
    def can_finish(speed):
        return sum((p + speed - 1) // speed for p in piles) <= h

    left, right = 1, max(piles)
    result = 0

    while left <= right:  # ← Maximize template
        mid = (left + right) // 2
        if can_finish(mid):
            result = mid
            left = mid + 1  # ← WRONG! Should try smaller, not larger
        else:
            right = mid - 1

    return result  # Returns MAXIMUM valid speed, not minimum!
```

**Result:** Returns max(piles) when we want minimum speed. Correct: 4, Wrong: 11

---

### Mistake 3: Forgetting result variable in MAXIMIZE

```python
# WRONG: No result variable for maximize
def maxLength(ribbons, k):
    def can_cut(length):
        return sum(r // length for r in ribbons) >= k

    left, right = 1, max(ribbons)

    while left <= right:
        mid = (left + right) // 2
        if can_cut(mid):
            left = mid + 1  # mid is excluded!
        else:
            right = mid - 1

    return left  # ← WRONG! left points past last valid value
```

**Result:** Returns value that's too large. Must save result when found.

---

## 🎯 Decision Tree: Which Template?

```
Question asks for minimum/maximum value?
│
├─ MINIMIZE (smallest value where condition is true)
│  │
│  ├─ Keywords: "minimum capacity", "minimum speed", "minimum time"
│  ├─ Monotonicity: if X works → all Y > X work
│  ├─ Template:
│  │   while left < right:
│  │       if is_valid(mid): right = mid
│  │       else: left = mid + 1
│  └─ Examples: Koko (#094), Ship Capacity (#079)
│
└─ MAXIMIZE (largest value where condition is true)
   │
   ├─ Keywords: "maximum length", "maximum distance", "maximum value"
   ├─ Monotonicity: if X works → all Y < X work
   ├─ Template:
   │   result = 0
   │   while left <= right:
   │       if is_valid(mid): result = mid; left = mid + 1
   │       else: right = mid - 1
   │   return result
   └─ Examples: Cutting Ribbons (#074)
```

---

## 📋 Problem Classification by Template Type

### Minimize Template (Find Minimum)

| # | Problem | What We Minimize | Bounds | Monotonicity |
|---|---------|------------------|--------|--------------|
| 094 | Koko Eating Bananas | Speed | [1, max(piles)] | If speed k works → k+1 works |
| 079 | Ship Packages | Capacity | [max(w), sum(w)] | If cap c works → c+1 works |

### Maximize Template (Find Maximum)

| # | Problem | What We Maximize | Bounds | Monotonicity |
|---|---------|------------------|--------|--------------|
| 074 | Cutting Ribbons | Length | [1, max(ribbons)] | If length L works → L-1 works |

### Other Templates (Not Min/Max)

| # | Problem | Pattern | Template Used |
|---|---------|---------|---------------|
| 010 | Find Peak | Find ANY peak | Custom (compare neighbors) |
| 042 | First/Last Position | Find boundaries | Boundary search |
| 084 | Kth Smallest in Matrix | Find kth value | Value range search |
| 100 | Median of Two Arrays | Partition arrays | Partition search |

---

## 📚 Sub-Pattern Deep Dive

This category has **4 distinct sub-patterns**. Master each progressively:

### Pattern 1: Classic Binary Search

**Description:** Search for target in explicitly sorted array

**When to Use:** Array is sorted, looking for specific value or boundaries

**Examples in This Set:** #042 Find First and Last Position

**Code Template:**

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # NOTE: <=  for exact search
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Common Bugs:**

- ❌ Using < instead of <= (infinite loop or miss last element)
- ❌ Not using left + (right - left) // 2 (integer overflow in other languages)
- ❌ Forgetting to return after finding target (unnecessary iterations)
- ❌ Wrong boundary: right = mid instead of mid - 1

**Testing Strategy:**

```
Test cases:
- Empty array []
- Single element [1]
- Target at start [1,2,3] target=1
- Target at end [1,2,3] target=3
- Target in middle [1,2,3,4,5] target=3
- Target not found [1,3,5] target=2
- Duplicates [1,2,2,2,3] target=2
```

---

### Pattern 2: Binary Search for Boundaries

**Description:** Find leftmost/rightmost occurrence in sorted array with duplicates

**When to Use:** Need first or last position of value in sorted array

**Examples in This Set:** #042 Find First and Last Position

**Code Template:**

```python
def find_left_bound(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # KEY: Keep searching LEFT
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def find_right_bound(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # KEY: Keep searching RIGHT
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result
```

**Common Bugs:**

- ❌ Stopping at first match (not continuing search)
- ❌ Moving wrong pointer (left vs right after match)
- ❌ Not saving result before continuing search
- ❌ Using < instead of <= for comparison

**💡 Key Insight:**

The critical difference from classic binary search:
AFTER finding target, don't return immediately! Save it and keep searching in
the direction needed (left for first, right for last).

---

### Pattern 3: Binary Search on Implicit Array

**Description:** Search in array with monotonic property but not explicitly sorted

**When to Use:** Array has peaks/valleys, rotated sorted, or bitonic properties

**Examples in This Set:** #010 Find Peak Element

**Code Template:**

```python
def find_peak(arr):
    left, right = 0, len(arr) - 1
    while left < right:  # NOTE: < not <= !
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid + 1]:
            # Peak is at mid or to the left
            right = mid  # Keep mid as candidate
        else:
            # Peak is to the right
            left = mid + 1
    return left  # left == right at end
```

**Common Bugs:**

- ❌ Using left <= right (infinite loop with right = mid)
- ❌ Using right = mid - 1 (might skip the peak)
- ❌ Not checking mid+1 boundary (index out of bounds)
- ❌ Returning mid instead of left/right

**💡 Key Insight:**

Template difference: while left < right (not <=)
Because we use right = mid (not mid-1), need < to avoid infinite loop.
This template finds "first occurrence of condition" pattern.

---

### Pattern 4: Binary Search on Answer Space

**Description:** Search for optimal value, not array index. "Minimize maximum" or "Maximize minimum" problems.

**When to Use:** Problem asks "minimum capacity to...", "minimum speed to...", "maximum weight where...".
Key signal: Not searching IN array, but for a VALUE that satisfies conditions.

**Examples in This Set:** #079 Capacity To Ship Packages, #094 Koko Eating Bananas, #074 Cutting Ribbons

**Code Template:** See detailed minimize/maximize templates above in the "Critical Insight" section.

**Common Bugs:**

- ❌ Wrong search space bounds (must be [min_possible, max_possible])
- ❌ Inefficient is_valid() function (should short-circuit)
- ❌ Using wrong template (minimize vs maximize)
- ❌ Not using result variable for maximize problems
- ❌ Forgetting that is_valid() must be MONOTONIC

**💡 Key Insight:**

MENTAL MODEL SHIFT: You're not searching for an index!
You're binary searching over POSSIBLE ANSWERS.

The array defines constraints, but you're searching a conceptual number line:
[1, 2, 3, ..., max_capacity]
     ↑
  Looking for minimum value where is_valid(value) = True

Monotonicity requirement: If value X doesn't work, no value < X works.
                         If value X works, all values > X work.

This is why we can binary search - the condition splits space in half!

---

## 🎓 Learning Path: Easiest to Hardest

### Level 1: Start: Classic Binary Search

**Problems:** #042 Find First and Last Position

**Goal:** Master the basic template with <= comparison

**Practice:** Write from scratch 5 times without looking. Test all edge cases.

---

### Level 2: Boundaries: Left/Right Bound Search

**Problems:** #042 (boundary variation)

**Goal:** Understand when to continue searching after finding match

**Practice:** Modify classic template to find first/last occurrence. Compare both.

---

### Level 3: Implicit Monotonicity: Peak Finding

**Problems:** #010 Find Peak Element

**Goal:** Recognize monotonic property without explicit sorting

**Practice:** Draw array, mark mid, explain why one half can be eliminated

---

### Level 4: Answer Space: Minimize Problems

**Problems:** #094 Koko Eating Bananas, #079 Ship Packages

**Goal:** Mental shift from "search in array" to "search for value". Master minimize template.

**Practice:** Identify: What are we searching for? What is search space? What is is_valid()? Why does minimize template work here?

---

### Level 5: Answer Space: Maximize Problems

**Problems:** #074 Cutting Ribbons

**Goal:** Understand maximize template and why it differs from minimize

**Practice:** Compare minimize vs maximize templates side-by-side. Explain why result variable is needed. Test what happens if you use wrong template.

---

### Level 6: Advanced: 2D Binary Search

**Problems:** #084 Kth Smallest in Sorted Matrix

**Goal:** Combine binary search with 2D array properties

**Practice:** Identify what makes the search space monotonic in 2D

---

### Level 7: Master: Median of Two Sorted Arrays

**Problems:** #100 Median of Two Sorted Arrays

**Goal:** Binary search with partition logic and edge cases

**Practice:** This is HARD. Study solution, then implement without looking.

---

## ⚠️ Common Errors Across All Patterns

### Integer overflow in mid calculation

**❌ Wrong:**
```python
mid = (left + right) // 2
```

**✅ Correct:**
```python
mid = left + (right - left) // 2
```

**Why:** In Python not a problem, but in Java/C++ left+right can overflow

**Test:** left=2^30, right=2^30 → overflow in some languages

---

### Off-by-one errors with boundaries

**❌ Wrong:**
```python
if found: right = mid - 1
```

**✅ Correct:**
```python
if found: right = mid (when using while left < right)
```

**Why:** Template choice determines boundary update. Mixing templates causes bugs.

**Test:** Array of size 2, target is first element

---

### Infinite loop with wrong template

**❌ Wrong:**
```python
while left < right: ... right = mid
```

**✅ Correct:**
```python
Match loop condition with boundary update
```

**Why:** left < right requires right = mid (include mid). left <= right requires right = mid - 1

**Test:** Run with array [1,2], target=1. Does it terminate?

---

### Not checking array boundaries

**❌ Wrong:**
```python
if arr[mid] > arr[mid+1]
```

**✅ Correct:**
```python
if mid < len(arr) - 1 and arr[mid] > arr[mid+1]
```

**Why:** mid+1 can go out of bounds when mid = len-1

**Test:** Array of size 1

---

## ✅ Testing & Verification

## Unit Testing Strategy for Binary Search

### 1. Edge Cases (ALWAYS test these first)
- Empty array: []
- Single element: [1]
- Two elements: [1, 2]
- All same: [5, 5, 5, 5]

### 2. Position Cases
- Target at index 0
- Target at last index
- Target in middle
- Target not present (between elements)
- Target not present (before all)
- Target not present (after all)

### 3. Duplicate Cases (for boundary search)
- All duplicates of target: [2, 2, 2, 2]
- Target at boundaries: [2, 2, 3, 4] or [1, 2, 3, 3]
- Single occurrence: [1, 2, 3]

### 4. For Answer Space Problems
- Minimum possible answer
- Maximum possible answer
- Answer in middle of range
- Impossible case (if applicable)
- Test both MIN and MAX problem types

### 5. Property Testing
Write a test that:
1. Generates random sorted array
2. Picks random target
3. Runs your binary search
4. Verifies result with linear search
5. Repeat 1000 times

```python
import random

def test_binary_search_random():
    for _ in range(1000):
        size = random.randint(0, 100)
        arr = sorted([random.randint(-100, 100) for _ in range(size)])
        target = random.randint(-100, 100)

        result = binary_search(arr, target)
        expected = linear_search(arr, target)

        assert result == expected, f"Failed on arr={arr}, target={target}"
```

### 6. Invariant Checking
Add assertions in your binary search:
```python
def binary_search_with_invariants(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        # Invariant: if target exists, it's in [left, right]
        assert 0 <= left <= len(arr)
        assert -1 <= right < len(arr)
        assert left <= right + 1  # Allow left = right + 1 for termination

        mid = left + (right - left) // 2
        # ... rest of logic
```

---

## 💎 Mastery Insights

### Two Completely Different Mental Models

Binary search has TWO distinct use cases that require different thinking:

1. SEARCH IN ARRAY: Find index/position
   - Input: Sorted (or monotonic) array
   - Output: Index or -1
   - Template: Classic binary search

2. SEARCH ON ANSWER: Find optimal value
   - Input: Problem constraints (array defines constraints, not search space)
   - Output: Optimal value (not an index!)
   - Template: Binary search on answer (minimize or maximize)

Many students confuse these. #042 is type 1. #079, #094, and #074 are type 2.

---

### Why Binary Search Works: The Monotonicity Guarantee

Binary search ONLY works when checking mid tells us which half to eliminate.

For array search: If arr[mid] < target, we know target is in right half.
For answer search: If is_valid(mid) = True, we know all values > mid are also valid.

If this property doesn't hold, binary search fails!

Example where it FAILS:
Array: [3, 1, 4, 1, 5, 9, 2, 6]  ← Not monotonic!
Cannot eliminate half based on arr[mid] comparison.

---

### Template Choice: < vs <= and When It Matters

Two templates exist for good reasons:

TEMPLATE A (for exact match):
```python
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```
Use when: Looking for exact value, need to check all elements.
Boundary update: MUST be mid ± 1 (exclusive)

TEMPLATE B (for condition finding):
```python
while left < right:
    mid = (left + right) // 2
    if condition(mid):
        right = mid  # Keep mid as candidate
    else:
        left = mid + 1
```
Use when: Finding first/last position satisfying condition.
Boundary update: Can include mid (right = mid)

Mixing these causes infinite loops! If using right = mid, MUST use left < right.

---

### Answer Space Problems: Identifying the Pattern

How to recognize "binary search on answer" problems:

🚨 SIGNALS 🚨
- Problem asks for "minimum value that...", "maximum value where..."
- Keywords: "minimum capacity", "minimum speed", "maximum pages", "kth element"
- Array defines CONSTRAINTS, not the search space
- Brute force would be "try every possible value from min to max"

STEPS TO SOLVE:
1. Identify what you're minimizing/maximizing (this is your "answer")
2. Determine if it's MINIMIZE or MAXIMIZE (this chooses your template!)
3. Find bounds: [minimum_possible, maximum_possible]
4. Write is_valid(candidate): checks if candidate satisfies constraints
5. Verify monotonicity: if X works, does X+1 work? (or vice versa)
6. Apply correct binary search template on [min, max]

Example: "Minimum speed to eat all bananas in H hours"
- Answer: speed (integer from 1 to max(piles))
- Type: MINIMIZE (find smallest speed that works)
- is_valid(speed): returns true if can finish with this speed
- Monotonic: if speed K works, speed K+1 also works
- Binary search for smallest K where is_valid(K) = true
- Use MINIMIZE template (while left < right, right = mid)

---

## 📋 Complete Problem Reference

| # | Problem | Difficulty | Frequency | Type | Template | File |
|---|---------|------------|-----------|------|----------|------|
| 010 | Find Peak Element | MEDIUM | 82.9% | Implicit Array | Custom | [010_find_peak_element.md](./010_find_peak_element.md) |
| 041 | Kth Missing Positive Number | EASY | 59.4% | Answer Space | Custom | [041_kth_missing_positive_number.md](./041_kth_missing_positive_number.md) |
| 042 | Find First and Last Position | MEDIUM | 59.4% | Boundary | Boundary Search | [042_find_first_and_last_position_of_element_in_sorted_array.md](./042_find_first_and_last_position_of_element_in_sorted_array.md) |
| 074 | Cutting Ribbons | MEDIUM | 40.7% | Answer Space | **MAXIMIZE** | [074_cutting_ribbons.md](./074_cutting_ribbons.md) |
| 079 | Capacity To Ship Packages | MEDIUM | 40.7% | Answer Space | **MINIMIZE** | [079_capacity_to_ship_packages_within_d_days.md](./079_capacity_to_ship_packages_within_d_days.md) |
| 084 | Kth Smallest Element in Matrix | MEDIUM | 40.7% | Value Range | Custom | [084_kth_smallest_element_in_a_sorted_matrix.md](./084_kth_smallest_element_in_a_sorted_matrix.md) |
| 094 | Koko Eating Bananas | MEDIUM | 32.0% | Answer Space | **MINIMIZE** | [094_koko_eating_bananas.md](./094_koko_eating_bananas.md) |
| 100 | Median of Two Sorted Arrays | HARD | 32.0% | Partition | Partition Search | [100_median_of_two_sorted_arrays.md](./100_median_of_two_sorted_arrays.md) |

---

[← Back to All Categories](../README.md)
