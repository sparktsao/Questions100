# Binary Search Mastery



## 📋 Problems in This Category

- [010. Find Peak Element](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/010_find_peak_element.md) - `Search Peak`
- [041. Kth Missing Positive Number](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/041_kth_missing_positive_number.md) - `Search Answer`
- [042. Find First and Last Position](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/042_find_first_and_last_position.md) - `Dual Binary Search`
- [074. Cutting Ribbons](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/074_cutting_ribbons.md) - `Search Answer`
- [079. Capacity To Ship Packages](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/079_capacity_to_ship_packages.md) - `Search Capacity`
- [084. Kth Smallest Element in Matrix](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/084_kth_smallest_element_in_matrix.md) - `Search Value Range`
- [094. Koko Eating Bananas](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Binary-Search/094_koko_eating_bananas.md) - `Search Speed`
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
3. Answer spaces where "if X works, all values > X work"

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

**Code Template:**

```python
def binary_search_on_answer(problem_constraints):
    """
    Core pattern: Find minimum value that satisfies condition
    OR: Find maximum value that satisfies condition
    """
    def is_valid(candidate_value):
        """
        Check if candidate_value satisfies problem constraints.
        This is O(n) typically - must check all elements.
        """
        # Problem-specific validation logic
        pass

    # Define search space based on problem
    left = minimum_possible_answer
    right = maximum_possible_answer

    while left < right:  # Use < for "minimize" problems
        mid = left + (right - left) // 2

        if is_valid(mid):
            # mid works, try smaller (for minimize problems)
            right = mid
        else:
            # mid doesn't work, need larger value
            left = mid + 1

    return left  # Final answer

# For "maximize" problems, flip the logic:
def binary_search_maximize(problem_constraints):
    def is_valid(candidate_value):
        pass

    left, right = min_val, max_val

    while left < right:
        mid = left + (right - left + 1) // 2  # NOTE: +1 for maximize!

        if is_valid(mid):
            # mid works, try larger
            left = mid  # Use left = mid for maximize
        else:
            # mid doesn't work, need smaller
            right = mid - 1

    return left
```

**Common Bugs:**

- ❌ Wrong search space bounds (must be [min_possible, max_possible])
- ❌ Inefficient is_valid() function (should short-circuit)
- ❌ Not using +1 in mid calculation for maximize (infinite loop)
- ❌ Confusing minimize vs maximize templates
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

**Problems:** #094 Koko Eating Bananas

**Goal:** Mental shift from "search in array" to "search for value"

**Practice:** Identify: What are we searching for? What is search space? What is is_valid()?

---

### Level 5: Answer Space: Capacity Problems

**Problems:** #079 Capacity To Ship Packages, #074 Cutting Ribbons

**Goal:** Apply pattern to capacity/resource allocation problems

**Practice:** Before coding, write down: [min, max] bounds and is_valid() logic

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
   - Template: Binary search on answer

Many students confuse these. #042 is type 1. #079 and #094 are type 2.


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
2. Find bounds: [minimum_possible, maximum_possible]
3. Write is_valid(candidate): checks if candidate satisfies constraints
4. Verify monotonicity: if X works, does X+1 work? (or vice versa)
5. Apply binary search template on [min, max]

Example: "Minimum speed to eat all bananas in H hours"
- Answer: speed (integer from 1 to max(piles))
- is_valid(speed): returns true if can finish with this speed
- Monotonic: if speed K works, speed K+1 also works
- Binary search for smallest K where is_valid(K) = true


---

## 📋 Complete Problem Reference

| # | Problem | Difficulty | Frequency | File |
|---|---------|------------|-----------|------|
| 010 | Find Peak Element | MEDIUM | 82.9% | [010_find_peak_element.md](./010_find_peak_element.md) |
| 041 | Kth Missing Positive Number | EASY | 59.4% | [041_kth_missing_positive_number.md](./041_kth_missing_positive_number.md) |
| 042 | Find First and Last Position of Element in Sorted Array | MEDIUM | 59.4% | [042_find_first_and_last_position_of_element_in_sorted_array.md](./042_find_first_and_last_position_of_element_in_sorted_array.md) |
| 074 | Cutting Ribbons | MEDIUM | 40.7% | [074_cutting_ribbons.md](./074_cutting_ribbons.md) |
| 079 | Capacity To Ship Packages Within D Days | MEDIUM | 40.7% | [079_capacity_to_ship_packages_within_d_days.md](./079_capacity_to_ship_packages_within_d_days.md) |
| 084 | Kth Smallest Element in a Sorted Matrix | MEDIUM | 40.7% | [084_kth_smallest_element_in_a_sorted_matrix.md](./084_kth_smallest_element_in_a_sorted_matrix.md) |
| 094 | Koko Eating Bananas | MEDIUM | 32.0% | [094_koko_eating_bananas.md](./094_koko_eating_bananas.md) |
| 100 | Median of Two Sorted Arrays | HARD | 32.0% | [100_median_of_two_sorted_arrays.md](./100_median_of_two_sorted_arrays.md) |


---

[← Back to All Categories](../README.md)
