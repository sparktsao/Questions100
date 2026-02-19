# Array & Hashing - Comprehensive Mastery Guide




## 📋 Problems in This Category

- [016. Merge Intervals](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/016_merge_intervals.md) - `Sort+Merge`
- [017. Two Sum](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/017_two_sum.md) - `HashMap O(1)`
- [022. Buildings With Ocean View](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/022_buildings_with_an_ocean_view.md) - `Right-to-Left`
- [023. Custom Sort String](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/023_custom_sort_string.md) - `Count+Build`
- [024. K Closest Points](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/024_k_closest_points_to_origin.md) - `Max Heap`
- [026. Subarray Sum Equals K](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/026_subarray_sum_equals_k.md) - `Prefix Sum+Hash`
- [062. Group Shifted Strings](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/062_group_shifted_strings.md) - `Hash Pattern`
- [069. Zero Array Transformation](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/069_zero_array_transformation_iii.md) - `Heap+Greedy`
- [071. Managers with 5+ Reports](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/071_managers_with_at_least_5_direct_reports.md) - `SQL Aggregate`
- [077. Car Pooling](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/077_car_pooling.md) - `Difference Array`
- [087. Maximum Subarray](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/087_maximum_subarray.md) - `Kadane DP`
- [089. Range Sum Query](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Array-Hashing/089_range_sum_query_immutable.md) - `Prefix Sum`

---

## From O(n²) Brute Force to O(n) Hash Map Optimization

---

## 🎯 Category Overview

**Total Problems:** 12
**Difficulty Range:** Easy (2) → Medium (10)
**Core Concept:** Trade space for time using hash maps O(n) space for O(1) lookups, or use prefix sums for O(1) range queries

**🔑 Key Insight:** Most nested loops (O(n²)) can be optimized to O(n) using:
1. **Hash Maps** → Store complements, indices, or counts for O(1) lookups
2. **Prefix Sums** → Precompute cumulative sums for O(1) range queries
3. **Sorting** → Enable two-pointer or binary search techniques

---

## 📊 Problem Progression Map

```
LEVEL 1: Two Sum (#017) - Classic Hash Map Pattern (EASIEST)
    ↓
LEVEL 2: Range Sum Query (#089) - Prefix Sum Basics
    ↓
LEVEL 3: Maximum Subarray (#087) - Kadane's Algorithm (DP)
    ↓
LEVEL 4: Merge Intervals (#016) - Sorting + Greedy Merging
    ↓
LEVEL 5: K Closest Points (#024) - Sorting/Heap for Top-K
    ↓
LEVEL 6: Subarray Sum Equals K (#026) - Prefix Sum + Hash Map
    ↓
LEVEL 7: Group Shifted Strings (#062) - Hash Map Grouping
    ↓
LEVEL 8: Custom Sort String (#023) - Custom Comparators
    ↓
LEVEL 9: Buildings With Ocean View (#022) - Monotonic Traversal
    ↓
LEVEL 10: Car Pooling (#077) - Interval Scheduling
    ↓
LEVEL 11: Zero Array Transformation (#069) - Difference Array
    ↓
LEVEL 12: Managers with 5+ Reports (#071) - Aggregation (HARDEST)
```

---

## 🔍 The Four Core Patterns

### Pattern 1: Hash Map for O(1) Lookups

**When to Use:** Need to find complements, check existence, or group items
**Key Technique:** Store value→index or value→count mapping
**Space-Time Tradeoff:** O(n) space for O(1) lookup time

**Examples:** #017 Two Sum, #062 Group Shifted Strings

**Template:**
```python
def hash_map_pattern(arr, target):
    seen = {}  # or collections.defaultdict()

    for i, val in enumerate(arr):
        complement = target - val

        if complement in seen:  # O(1) lookup!
            return [seen[complement], i]

        seen[val] = i

    return []
```

### Pattern 2: Prefix Sum for Range Queries

**When to Use:** Multiple range sum queries, subarray problems
**Key Technique:** Precompute cumulative sums
**Formula:** `sum(arr[i:j]) = prefix[j] - prefix[i-1]`

**Examples:** #089 Range Sum Query, #026 Subarray Sum Equals K

**Template:**
```python
# Build prefix sum
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)

# Query in O(1)
def range_sum(left, right):
    return prefix[right + 1] - prefix[left]
```

**Advanced: Prefix Sum + Hash Map**
```python
def subarray_sum_k(arr, k):
    """Count subarrays with sum = k"""
    prefix_sum = 0
    count = 0
    seen = {0: 1}  # prefix_sum → frequency

    for num in arr:
        prefix_sum += num

        # Check if (prefix_sum - k) exists
        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]

        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count
```

### Pattern 3: Sorting + Greedy/Two-Pointer

**When to Use:** Intervals, pairs, or ordering-dependent problems
**Key Technique:** Sort first, then apply greedy or two-pointer
**Time:** O(n log n) for sort + O(n) for processing = O(n log n)

**Examples:** #016 Merge Intervals, #024 K Closest Points

**Template (Merge Intervals):**
```python
def merge_intervals(intervals):
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_end = merged[-1][1]

        if start <= last_end:  # Overlap
            merged[-1][1] = max(last_end, end)
        else:  # No overlap
            merged.append([start, end])

    return merged
```

### Pattern 4: Specialized Algorithms

**Kadane's Algorithm (Maximum Subarray):**
```python
def max_subarray(arr):
    """O(n) time, O(1) space"""
    max_sum = arr[0]
    current_sum = 0

    for num in arr:
        if current_sum < 0:  # Reset if negative
            current_sum = 0

        current_sum += num
        max_sum = max(max_sum, current_sum)

    return max_sum
```

**Difference Array (Range Updates):**
```python
def difference_array(arr, updates):
    """Apply multiple range updates efficiently"""
    diff = [0] * (len(arr) + 1)

    # Record differences
    for left, right, val in updates:
        diff[left] += val
        diff[right + 1] -= val

    # Build result from differences
    result = []
    current = 0
    for d in diff[:-1]:
        current += d
        result.append(current)

    return result
```

---

## 📖 Problem-by-Problem Deep Dive

### 1️⃣ **Problem #017: Two Sum** (EASY) - THE FOUNDATION

**🎯 Task:** Find two indices where nums[i] + nums[j] = target
**📥 Input:** `nums = [2,7,11,15], target = 9`
**📤 Output:** `[0, 1]`
**🏷️ Pattern:** Hash Map for Complement

#### Why This is THE Most Important Problem

```
This is the FOUNDATION of hash map thinking!
Every hash map problem is a variation of this:
1. What are you looking for? (complement)
2. What do you store? (value → index)
3. When do you check? (before adding to avoid self-pairing)
```

#### The Evolution of Solutions

**❌ Brute Force: O(n²)**
```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i, j]
```
**Problem:** Nested loops, checking every pair

**✅ Hash Map: O(n)**
```python
def twoSum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i  # Store AFTER checking!

    return []
```

#### Critical Implementation Details

**🚨 COMMON BUG:**
```python
# WRONG: Store before checking
seen[num] = i
if complement in seen:  # Might match with itself!
    return [seen[complement], i]
```

**✅ CORRECT: Check before storing**
```python
if complement in seen:  # Check first
    return [seen[complement], i]
seen[num] = i  # Store after
```

#### Key Insights

> **The Hash Map Mindset:**
> "I'm looking for X. Instead of searching for X every time (O(n)),
> let me store complements so I can check in O(1)!"

> **Why Store Index, Not Just Bool:**
> Problem asks for indices, not just "does pair exist"

#### Test Cases
```python
# Edge cases
[2, 7], target=9         # Two elements (minimum)
[3, 3], target=6         # Duplicate values
[-1, -2, -3], target=-5  # Negative numbers
[0, 4, 3, 0], target=0   # Zero values
[2, 5, 5, 11], target=10 # Duplicate, but different indices
```

#### Complexity
- **Time:** O(n) - single pass
- **Space:** O(n) - hash map storage
- **Optimal:** Yes, can't do better than O(n) since must examine all elements

---

### 2️⃣ **Problem #089: Range Sum Query** (EASY) - Prefix Sum Basics

**🎯 Task:** Answer multiple range sum queries efficiently
**📥 Input:** `nums = [-2,0,3,-5,2,-1]`, queries: `sumRange(0,2)`, `sumRange(2,5)`
**📤 Output:** `1, -1`
**🏷️ Pattern:** Prefix Sum Array

#### The Problem with Naive Approach

```python
# Naive: O(n) per query
def sumRange(left, right):
    return sum(nums[left:right+1])

# With 10^4 queries on 10^4 array = O(10^8) = TOO SLOW!
```

#### Prefix Sum Optimization

**Idea:** Precompute cumulative sums once, then answer queries in O(1)

```python
class NumArray:
    def __init__(self, nums):
        """O(n) preprocessing"""
        self.prefix = [0]  # prefix[0] = 0

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

        # prefix[i] = sum of nums[0:i]
        # nums = [-2, 0, 3, -5, 2, -1]
        # prefix = [0, -2, -2, 1, -4, -2, -3]

    def sumRange(self, left, right):
        """O(1) query"""
        return self.prefix[right + 1] - self.prefix[left]
```

#### Visual Understanding

```
nums:    [-2,  0,  3, -5,  2, -1]
index:     0   1   2   3   4   5

prefix: [0, -2, -2, 1, -4, -2, -3]
index:   0   1   2  3   4   5   6

sumRange(2, 5) = prefix[6] - prefix[2]
               = -3 - (-2)
               = -1
               = sum(3, -5, 2, -1) ✓
```

#### Why prefix[i] = sum(nums[0:i])?

**Alternative:** `prefix[i] = sum(nums[0:i+1])` also works, but:
- Requires checking `if left == 0` separately
- Less clean for general formula

**Our choice:** `prefix[0] = 0`, `prefix[i] = sum(nums[0:i])`
- Formula always works: `sum[left:right+1] = prefix[right+1] - prefix[left]`
- No special cases!

#### Key Insights

> **When to Use Prefix Sum:**
> Multiple queries on same array + queries are range sums

> **Space-Time Tradeoff:**
> O(n) space for O(1) queries (vs O(1) space for O(n) queries)

#### Common Bugs

**❌ Off-by-One Errors:**
```python
# WRONG
return self.prefix[right] - self.prefix[left]

# CORRECT
return self.prefix[right + 1] - self.prefix[left]
```

**❌ Not Handling Empty/Single Element:**
```python
# Test with nums = [1] or nums = []
```

---

### 3️⃣ **Problem #087: Maximum Subarray** (MEDIUM) - Kadane's Algorithm

**🎯 Task:** Find contiguous subarray with largest sum
**📥 Input:** `nums = [-2,1,-3,4,-1,2,1,-5,4]`
**📤 Output:** `6` (subarray [4,-1,2,1])
**🏷️ Pattern:** Dynamic Programming / Kadane's Algorithm

#### The Evolution of Thinking

**❌ Brute Force: O(n³)**
```python
max_sum = float('-inf')
for i in range(n):
    for j in range(i, n):
        current_sum = sum(nums[i:j+1])  # O(n) here!
        max_sum = max(max_sum, current_sum)
```

**Better: O(n²) with prefix sum**
```python
prefix = build_prefix_sum(nums)
max_sum = float('-inf')
for i in range(n):
    for j in range(i, n):
        current_sum = prefix[j+1] - prefix[i]  # O(1) here
        max_sum = max(max_sum, current_sum)
```

**✅ Kadane's Algorithm: O(n)**
```python
def maxSubArray(nums):
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        if current_sum < 0:  # KEY: Reset if negative!
            current_sum = 0

        current_sum += num
        max_sum = max(max_sum, current_sum)

    return max_sum
```

#### Why Kadane's Works - The Intuition

```
At each position, ask: "Should I extend previous subarray or start fresh?"

Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Position 0: current=0, add -2 → 0 (negative, reset) → current=0, then add -2=-2, max=-2
Position 1: current=-2 < 0, reset! Start fresh with 1 → current=1, max=1
Position 2: current=1, add -3 → -2, max=1
Position 3: current=-2 < 0, reset! Start with 4 → current=4, max=4
Position 4: current=4, add -1 → 3, max=4
Position 5: current=3, add 2 → 5, max=5
Position 6: current=5, add 1 → 6, max=6 ← ANSWER
Position 7: current=6, add -5 → 1, max=6
Position 8: current=1, add 4 → 5, max=6
```

**Key Decision:** If `current_sum < 0`, starting fresh is always better!

#### Alternative DP Formulation

```python
def maxSubArray(nums):
    """
    dp[i] = max sum ending at index i

    dp[i] = max(nums[i], dp[i-1] + nums[i])
            ^^^^^^^^^^  ^^^^^^^^^^^^^^^^^
            start fresh  extend previous
    """
    dp_prev = nums[0]  # Space optimized: only need previous
    max_sum = nums[0]

    for i in range(1, len(nums)):
        dp_curr = max(nums[i], dp_prev + nums[i])
        max_sum = max(max_sum, dp_curr)
        dp_prev = dp_curr

    return max_sum
```

#### Kadane's vs DP: Same Algorithm, Different Perspective

**Kadane's says:** "If my running sum goes negative, reset!"
**DP says:** "Take max of (start fresh) vs (extend previous)"

**They're equivalent!**

#### Edge Cases

```python
# All negative numbers
[-1, -2, -3]  # Answer: -1 (least negative)

# All positive
[1, 2, 3]  # Answer: 6 (entire array)

# Mixed with large negative
[5, -3, 5]  # Answer: 7 (entire array, negative is smaller)

# Single element
[42]  # Answer: 42
```

#### Key Insights

> **Kad's Greedy Insight:**
> A negative prefix can never help a future subarray

> **When Current Sum < 0:** Always better to start fresh than drag negative sum forward

---

### 4️⃣ **Problem #026: Subarray Sum Equals K** (MEDIUM) - Prefix Sum + Hash Map

**🎯 Task:** Count subarrays with sum equal to k
**📥 Input:** `nums = [1,1,1], k = 2`
**📤 Output:** `2` (subarrays [1,1] and [1,1])
**🏷️ Pattern:** Prefix Sum + Hash Map (COMBO!)

#### Why This is Hard

```
Can't use Kadane's (need specific sum, not maximum)
Can't use simple prefix sum (need COUNT, not just sum)
Need to check: "How many subarrays end at position i with sum k?"
```

#### The Breakthrough Insight

```
If prefix_sum[j] - prefix_sum[i] = k
Then subarray [i+1, j] has sum k

Rearranging:
prefix_sum[i] = prefix_sum[j] - k

So: At position j, if (current_prefix - k) exists in our hash map,
    we found subarrays ending at j!
```

#### The Algorithm

```python
def subarraySum(nums, k):
    """
    Use hash map to store: prefix_sum → count

    Time: O(n), Space: O(n)
    """
    count = 0
    prefix_sum = 0
    seen = {0: 1}  # CRITICAL: Handle subarrays starting from index 0

    for num in nums:
        prefix_sum += num

        # Check if (prefix_sum - k) exists
        # This means: there's a previous prefix that,
        # when subtracted from current, gives k
        if prefix_sum - k in seen:
            count += seen[prefix_sum - k]

        # Store current prefix sum
        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return count
```

#### Step-by-Step Walkthrough

```
nums = [1, 1, 1], k = 2

Initial: count=0, prefix=0, seen={0:1}

i=0, num=1:
    prefix = 1
    Check: (1-2) = -1 in seen? NO
    Store: seen = {0:1, 1:1}
    count = 0

i=1, num=1:
    prefix = 2
    Check: (2-2) = 0 in seen? YES! seen[0]=1
    count = 0 + 1 = 1  ← Found subarray [1,1]
    Store: seen = {0:1, 1:1, 2:1}

i=2, num=1:
    prefix = 3
    Check: (3-2) = 1 in seen? YES! seen[1]=1
    count = 1 + 1 = 2  ← Found subarray [1,1] (second one)
    Store: seen = {0:1, 1:1, 2:1, 3:1}

Answer: 2 ✓
```

#### Why seen[0] = 1 Initially?

```
WITHOUT {0:1}:
nums = [2, 2], k = 2
prefix=2, check (2-2)=0 in seen? NO → MISS subarray [2]!

WITH {0:1}:
prefix=2, check (2-2)=0 in seen? YES → COUNT subarray [2] ✓
```

**Meaning:** `seen[0]=1` represents "empty prefix" (before array starts)

#### Why Store Counts, Not Just Bool?

```
nums = [1, -1, 1, -1, 1], k = 0

Multiple prefix sums can be same:
prefix = [1, 0, 1, 0, 1]
         Duplicate 0's!

When prefix=0 appears again, we found TWO subarrays ending here!
```

#### Comparison to Two Sum

| Aspect | Two Sum | Subarray Sum K |
|--------|---------|----------------|
| Goal | Find pair | Count subarrays |
| Hash stores | value → index | prefix_sum → count |
| Check for | complement | prefix - k |
| Return when found | immediately | keep counting |
| Initial hash | empty {} | {0: 1} |

#### Key Insights

> **Prefix Sum Property:**
> sum(arr[i:j]) = prefix[j] - prefix[i-1]
> So if we want sum=k, look for prefix_sum that's k less than current

> **Why Hash Map:**
> Need to check "does this prefix exist?" in O(1), not O(n)

#### Common Bugs

**❌ Forgetting {0: 1}:**
```python
seen = {}  # WRONG: Misses subarrays from start
seen = {0: 1}  # CORRECT
```

**❌ Checking after storing:**
```python
seen[prefix_sum] += 1
if prefix_sum - k in seen:  # WRONG: Might count self!
```

**✅ CORRECT:**
```python
if prefix_sum - k in seen:  # Check first
    count += seen[prefix_sum - k]
seen[prefix_sum] += 1  # Store after
```

---

### 5️⃣ **Problem #016: Merge Intervals** (MEDIUM) - Sorting + Greedy

**🎯 Task:** Merge overlapping intervals
**📥 Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`
**📤 Output:** `[[1,6],[8,10],[15,18]]`
**🏷️ Pattern:** Sort + Greedy Merge

#### Why Sort First?

```
UNSORTED: [[2,6], [1,3], [8,10]]
Hard to know if [2,6] overlaps with something before it!

SORTED: [[1,3], [2,6], [8,10]]
Easy: Just compare current with LAST merged interval
```

#### Algorithm

```python
def merge(intervals):
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])

    merged = [intervals[0]]

    for start, end in intervals[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end:  # Overlap!
            # Merge: extend the end
            merged[-1][1] = max(last_end, end)
        else:  # No overlap
            merged.append([start, end])

    return merged
```

#### Visual Understanding

```
Input: [[1,3], [2,6], [8,10], [15,18]]

After sort: [[1,3], [2,6], [8,10], [15,18]]

Step 1: merged = [[1,3]]

Step 2: [2,6]
  2 <= 3? YES → Overlap
  merged = [[1, max(3,6)]] = [[1,6]]

Step 3: [8,10]
  8 <= 6? NO → No overlap
  merged = [[1,6], [8,10]]

Step 4: [15,18]
  15 <= 10? NO → No overlap
  merged = [[1,6], [8,10], [15,18]]
```

#### Edge Cases

```python
# Complete overlap
[[1,4], [2,3]]  # → [[1,4]]

# Touching intervals (not overlapping)
[[1,2], [3,4]]  # → [[1,2], [3,4]] (no merge)

# Nested intervals
[[1,10], [2,3], [4,5]]  # → [[1,10]]

# Single interval
[[1,3]]  # → [[1,3]]

# Empty
[]  # → []
```

#### Common Bugs

**❌ Forgetting to extend end:**
```python
if start <= last_end:
    # WRONG: Just update start
    merged[-1] = [last_start, end]

# CORRECT: Take max of ends
merged[-1][1] = max(last_end, end)
```

**Example why max() needed:**
```
[[1,10], [2,3]]
After merging [2,3]: Should be [1,10], not [1,3]!
```

#### Key Insights

> **Greedy Property:**
> After sorting, only need to compare with LAST merged interval, not all previous

> **Overlap Condition:**
> Intervals [a,b] and [c,d] overlap iff: c <= b (when sorted by start)

---

## 🔄 Algorithm Relationships & Comparisons

### Can We Reuse Solutions?

| From → To | Can Reuse? | What Changes? |
|-----------|------------|---------------|
| Two Sum → Subarray Sum K | ⚠️ Partial | Add prefix sum concept, change hash to count |
| Range Sum → Subarray Sum K | ✅ YES | Add hash map to prefix sum |
| Maximum Subarray → Subarray Sum K | ❌ NO | Different goal (max vs specific sum) |
| Merge Intervals → Car Pooling | ✅ YES | Similar interval merging logic |
| Two Sum → K Closest Points | ❌ NO | Different data structures (heap vs hash) |

### Pattern Recognition Decision Tree

```
Need to find pairs/complements?
    → Hash Map (#017 Two Sum)

Multiple range sum queries?
    → Prefix Sum (#089 Range Sum Query)

Need maximum/minimum of contiguous subarray?
    → Kadane's Algorithm (#087 Maximum Subarray)

Counting subarrays with property?
    → Prefix Sum + Hash Map (#026 Subarray Sum K)

Interval merging/overlapping?
    → Sort + Greedy (#016 Merge Intervals)

Top-K elements?
    → Heap or Sorting (#024 K Closest)

Custom ordering?
    → Custom Comparator (#023 Custom Sort)
```

---

## ⚠️ Universal Common Pitfalls

### 1. Hash Map: Checking After Storing

**❌ WRONG:**
```python
seen[value] = index
if complement in seen:  # Might match with self!
    return [seen[complement], index]
```

**✅ CORRECT:**
```python
if complement in seen:  # Check first
    return [seen[complement], index]
seen[value] = index  # Store after
```

**Why:** Avoid matching element with itself

### 2. Prefix Sum: Off-by-One Errors

**❌ WRONG:**
```python
# prefix[i] = sum(nums[0:i+1])
return prefix[right] - prefix[left]  # Off by one!
```

**✅ CORRECT:**
```python
# prefix[i] = sum(nums[0:i])
return prefix[right + 1] - prefix[left]
```

**Why:** Depends on how you define prefix[i]

### 3. Kadane's: Forgetting All-Negative Case

**❌ WRONG:**
```python
max_sum = 0  # WRONG if all negative!
current = 0
for num in nums:
    current = max(0, current + num)
    max_sum = max(max_sum, current)
```

**✅ CORRECT:**
```python
max_sum = nums[0]  # Initialize with first element
current = 0
for num in nums:
    if current < 0:
        current = 0
    current += num
    max_sum = max(max_sum, current)
```

### 4. Merge Intervals: Not Using max() for End

**❌ WRONG:**
```python
if start <= last_end:
    merged[-1][1] = end  # WRONG: Might shrink!
```

**✅ CORRECT:**
```python
if start <= last_end:
    merged[-1][1] = max(last_end, end)
```

**Why:** [[1,10], [2,3]] should merge to [1,10], not [1,3]

---

## ✅ Testing Strategy

### Comprehensive Test Cases for Each Pattern

#### Hash Map Problems (Two Sum):
```python
# Edge cases
[]  # Empty
[1]  # Single element
[3, 3], target=6  # Duplicates
[-1, -2, -3], target=-5  # Negatives
[0, 4, 0], target=0  # Zeros

# Boundary
First pair, last pair, middle pair
No solution exists
```

#### Prefix Sum Problems:
```python
# Edge cases
[]  # Empty
[1]  # Single element
[-2, -2, -2]  # All negative
[0, 0, 0]  # All zeros

# Boundary
Range at start: [0, 2]
Range at end: [n-3, n-1]
Full range: [0, n-1]
Single element range: [i, i]
```

#### Kadane's Algorithm:
```python
# Critical cases
[-1, -2, -3]  # All negative
[1, 2, 3]  # All positive
[5, -3, 5]  # Mixed
[-2, 1, -3, 4, -1, 2, 1, -5, 4]  # Classic example
```

#### Interval Problems:
```python
# Edge cases
[]  # Empty
[[1, 2]]  # Single
[[1, 3], [2, 6]]  # Overlap
[[1, 2], [3, 4]]  # No overlap
[[1, 10], [2, 3], [4, 5]]  # Nested
[[1, 4], [0, 4]]  # Reverse order (test sorting)
```

---

## 💎 Mastery Insights

### 1. The Hash Map Mental Model

**Brute Force Mindset:**
```
For each element, search through entire array for complement → O(n²)
```

**Hash Map Mindset:**
```
"Instead of searching every time, let me REMEMBER what I've seen"
Trade O(n) space for O(1) lookups → O(n) total
```

**When to Use Hash Map:**
- Looking for pairs/complements
- Counting occurrences
- Grouping by key
- Checking existence in O(1)

### 2. Prefix Sum: Precomputation Tradeoff

**Key Realization:**
```
If answering many queries, precompute once!

No preprocessing: O(1) space, O(n) per query
With prefix sum: O(n) space, O(1) per query

Crossover: Worth it after ~1 query (usually)
```

**When to Use Prefix Sum:**
- Multiple range sum queries
- Subarray sum problems
- Range update problems (with difference array)

### 3. Kadane's: The Greedy Insight

**The Breakthrough:**
```
Don't need to track ALL subarrays!
At each position, only ask: "Extend or start fresh?"

If current_sum < 0: Starting fresh is ALWAYS better
```

**Why It Works:**
```
Optimal substructure: max_ending_here[i] depends only on max_ending_here[i-1]
Greedy choice: Negative prefix never helps
```

### 4. Sorting: Enabling Simpler Algorithms

**Pattern:**
```
Unsorted data → Complex logic to handle all orders
Sorted data → Simple linear scan often works!

Cost: O(n log n) for sort
Benefit: O(n) algorithm instead of O(n²)
```

**When Sorting Helps:**
- Interval merging
- Finding pairs/triplets
- Top-K problems (with heap)
- Custom ordering requirements

---

## 🎯 Universal Templates

### Template 1: Hash Map Complement Pattern
```python
def hash_complement_pattern(arr, target):
    seen = {}

    for i, val in enumerate(arr):
        complement = target - val

        if complement in seen:
            return [seen[complement], i]

        seen[val] = i

    return []
```

### Template 2: Prefix Sum + Hash Map
```python
def prefix_sum_hash_pattern(arr, target):
    prefix_sum = 0
    seen = {0: 1}  # Handle subarrays from start
    result = 0

    for val in arr:
        prefix_sum += val

        if prefix_sum - target in seen:
            result += seen[prefix_sum - target]

        seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

    return result
```

### Template 3: Kadane's Algorithm
```python
def kadane_pattern(arr):
    max_sum = arr[0]
    current_sum = 0

    for num in arr:
        if current_sum < 0:
            current_sum = 0

        current_sum += num
        max_sum = max(max_sum, current_sum)

    return max_sum
```

### Template 4: Sort + Merge Intervals
```python
def merge_interval_pattern(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:  # Overlap
            merged[-1][1] = max(merged[-1][1], end)
        else:  # No overlap
            merged.append([start, end])

    return merged
```

---

## 🚀 Recommended Study Order (12 Levels)

1. **Two Sum (#017)** - Master hash map thinking (1-2 days)
2. **Range Sum Query (#089)** - Learn prefix sum basics (1 day)
3. **Maximum Subarray (#087)** - Understand Kadane's (2 days)
4. **Merge Intervals (#016)** - Sort + greedy pattern (1-2 days)
5. **K Closest Points (#024)** - Sorting/heap for top-K (1 day)
6. **Subarray Sum K (#026)** - Combine prefix + hash (2-3 days)
7. **Group Shifted Strings (#062)** - Hash map grouping (1 day)
8. **Custom Sort (#023)** - Custom comparators (1 day)
9. **Buildings Ocean View (#022)** - Monotonic traversal (1 day)
10. **Car Pooling (#077)** - Interval scheduling (1-2 days)
11. **Zero Array Transform (#069)** - Difference array (1-2 days)
12. **Managers 5+ Reports (#071)** - Aggregation (1 day)

**Total Time to Mastery: 2-3 weeks with daily practice**

---

## 📝 Interview Red Flags

### Mistakes That Signal Poor Understanding

1. **Using nested loops without considering hash map optimization**
   - Red flag: "Let me just check every pair..."
   - Fix: Ask "Can I store complements for O(1) lookup?"

2. **Recomputing range sums repeatedly**
   - Red flag: Calling `sum(arr[i:j])` in a loop
   - Fix: Use prefix sum for multiple queries

3. **Not initializing hash map properly**
   - Red flag: `seen = {}` for subarray sum problems
   - Fix: `seen = {0: 1}` to handle subarrays from start

4. **Checking hash map after storing**
   - Red flag: Store then check (matches with self)
   - Fix: Check then store

5. **Wrong Kadane's implementation**
   - Red flag: `max_sum = 0` (fails on all-negative)
   - Fix: `max_sum = arr[0]`

6. **Forgetting to sort intervals**
   - Red flag: Trying to merge unsorted intervals
   - Fix: Always sort by start time first

---

## 💪 Practice Progression (4-Week Plan)

### Week 1: Foundation
- Day 1-2: Two Sum (#017) - Write from scratch 5 times
- Day 3-4: Range Sum Query (#089) - Build prefix sum, test queries
- Day 5-6: Maximum Subarray (#087) - Kadane's + DP formulation
- Day 7: Review all three, compare patterns

### Week 2: Combinations
- Day 1-2: Subarray Sum K (#026) - Combine prefix + hash
- Day 3-4: Merge Intervals (#016) - Sort + greedy
- Day 5-6: K Closest Points (#024) - Heap/sort for top-K
- Day 7: Compare interval vs subarray problems

### Week 3: Advanced Patterns
- Day 1-2: Group Shifted Strings (#062) - Hash grouping
- Day 3-4: Custom Sort String (#023) - Comparators
- Day 5-6: Buildings Ocean View (#022) - Monotonic stack
- Day 7: Identify when to use each pattern

### Week 4: Mastery
- Day 1-2: Car Pooling (#077) - Interval scheduling
- Day 3-4: Zero Array Transform (#069) - Difference array
- Day 5: Managers (#071) - Aggregation
- Day 6-7: Solve all 12 from scratch, timed

---

**Summary:** Array & Hashing problems optimize O(n²) brute force to O(n) using hash maps (for O(1) lookups), prefix sums (for O(1) range queries), or Kadane's algorithm (for maximum subarray). The key patterns are: (1) Hash map for complement finding, (2) Prefix sum for range queries, (3) Prefix sum + hash map for subarray counting, (4) Sorting + greedy for intervals, (5) Kadane's for maximum subarray. Master Two Sum first (foundation), then Range Sum Query (prefix basics), then Maximum Subarray (Kadane's), then combine patterns (Subarray Sum K). Always check hash maps BEFORE storing, initialize prefix sum hash with {0:1}, and use max() when merging interval ends.
