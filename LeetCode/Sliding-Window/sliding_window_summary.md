# Sliding Window Problems - Comprehensive Analysis



## 📋 Problems in This Category

- [037. Minimum Window Substring](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Sliding-Window/037_minimum_window_substring.md) - `Variable Size`
- [040. Max Consecutive Ones III](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Sliding-Window/040_max_consecutive_ones_iii.md) - `Variable Size`
- [059. Continuous Subarray Sum](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Sliding-Window/059_continuous_subarray_sum.md) - `HashMap+Mod`
- [068. Contains Duplicate II](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Sliding-Window/068_contains_duplicate_ii.md) - `Fixed Size`
- [080. Longest Substring Without Repeating](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Sliding-Window/080_longest_substring_without_repeating.md) - `Variable Size`
- [090. Frequency of Most Frequent Element](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Sliding-Window/090_frequency_of_most_frequent_element.md) - `Variable Size+Sort`

---

## 🎯 Category Overview

**Total Problems:** 6
**Difficulty Range:** Easy → Medium → Hard
**Core Concept:** Maintain a window of elements and slide it to find optimal subarray/substring

**🔑 Key Insight:** The FUNDAMENTAL choice is window type:
- **Fixed Size** → Window size known beforehand
- **Variable Size** → Expand until condition breaks, then shrink

---

## 📊 Problem Progression Map

```
Level 1: Contains Duplicate II (#068) - Fixed Window (EASIEST)
    ↓
Level 2: Max Consecutive Ones III (#040) - Variable Window, Simple Constraint
    ↓
Level 3: Longest Substring Without Repeating (#080) - Variable Window, Set Tracking
    ↓
Level 4: Continuous Subarray Sum (#059) - Prefix Sum + Modulo Math
    ↓
Level 5: Frequency of Most Frequent Element (#090) - Sort + Variable Window with Cost
    ↓
Level 6: Minimum Window Substring (#037) - Variable Window, Complex Tracking (HARDEST)
```

---

## 🔍 The Two Paradigms

### Paradigm A: Fixed Size Window
**When:** Window size is given or known
**Key:** Maintain exactly k elements
**Example:** #068

```python
window_size = k
for i in range(len(arr)):
    add arr[i] to window
    if window size > k:
        remove arr[i-k] from window
```

### Paradigm B: Variable Size Window
**When:** Find optimal window satisfying constraint
**Key:** Expand (right++) until invalid, then shrink (left++)
**Examples:** #040, #080, #037, #090

```python
left = 0
for right in range(len(arr)):
    add arr[right] to window
    while window invalid:
        remove arr[left] from window
        left++
    update answer
```

---

## 📖 Problem-by-Problem Analysis

### 1️⃣ **Problem #068: Contains Duplicate II** (EASY)

**🎯 Task:** Find duplicate within distance k
**📥 Input:** Integer array + distance k
**📤 Output:** Boolean (duplicate exists within k distance)
**🏷️ Tag:** Fixed Window

#### What Makes This Special?
```
Simplest sliding window!
Fixed size = k
Just check if duplicate in window
```

#### Algorithm (Two Approaches)

**Approach 1: Hash Map**
```python
def containsNearbyDuplicate(nums, k):
    seen = {}
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False
```

**Approach 2: Sliding Window with Set**
```python
def containsNearbyDuplicate(nums, k):
    window = set()
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        # Maintain window size k
        if len(window) > k:
            window.remove(nums[i - k])
    return False
```

#### Key Insight
> **Fixed Window Foundation:** Maintain exactly k elements
> Add right, remove left when size > k

#### Complexity
- **Time:** O(n) - single pass
- **Space:** O(min(n, k)) - window size bounded by k
- **Why Simplest:** Fixed size, simple duplicate check

---

### 2️⃣ **Problem #040: Max Consecutive Ones III** (MEDIUM)

**🎯 Task:** Find longest subarray of 1s with at most k flips
**📥 Input:** Binary array + k flips allowed
**📤 Output:** Maximum length
**🏷️ Tag:** Variable Window, Constraint

#### What Changed from #068?
```diff
+ Variable window size (not fixed)
+ Constraint: at most k zeros allowed
+ Track zero count (not just duplicates)
- Must find maximum (not just check existence)
```

#### Algorithm
```python
def longestOnes(nums, k):
    left = 0
    max_len = 0
    zeros_count = 0

    for right in range(len(nums)):
        # Expand window
        if nums[right] == 0:
            zeros_count += 1

        # Contract while invalid
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1

        # Update max
        max_len = max(max_len, right - left + 1)

    return max_len
```

#### The Expand-Shrink Pattern
```
right moves forward every iteration (expand)
left moves forward only when needed (shrink)
→ Both pointers move at most n times total
→ O(n) time guaranteed
```

#### Key Insight
> **Variable Window Intro:** Expand until constraint breaks
> Shrink until valid again, track maximum

#### Complexity
- **Time:** O(n) - each element visited at most twice
- **Space:** O(1) - just counter
- **Why Harder than #068:** Variable size, optimization goal

---

### 3️⃣ **Problem #080: Longest Substring Without Repeating** (MEDIUM)

**🎯 Task:** Find longest substring with all unique characters
**📥 Input:** String
**📤 Output:** Length of longest unique substring
**🏷️ Tag:** Variable Window, Set

#### What's New?
```
No fixed constraint value (not "k zeros" or "distance k")
Constraint: ALL characters must be unique
Must shrink until duplicate removed
```

#### Algorithm
```python
def lengthOfLongestSubstring(s):
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Shrink until no duplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        # Add current char
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

#### Why While Loop for Shrinking?
```
Example: "abcabcbb"
When right=3 (second 'a'), must remove chars until first 'a' gone
→ Remove 'a', 'b', 'c' (while loop runs 3 times)
→ Single if statement wouldn't work!
```

#### Key Insight
> **Set for Uniqueness:** Set provides O(1) duplicate check
> Shrink until specific element removed

#### Complexity
- **Time:** O(n) - each char added and removed once
- **Space:** O(min(n, m)) - m is charset size
- **Why Classic:** Pure sliding window with set

---

### 4️⃣ **Problem #059: Continuous Subarray Sum** (MEDIUM)

**🎯 Task:** Find subarray with sum divisible by k (length ≥ 2)
**📥 Input:** Integer array + integer k
**📤 Output:** Boolean
**🏷️ Tag:** Prefix Sum + Modulo

#### This is NOT Traditional Sliding Window!
```
Uses prefix sum + hash map
Key insight: (sum[j] - sum[i]) % k == 0
Means: sum[j] % k == sum[i] % k
→ Store remainders in hash map
```

#### Algorithm
```python
def checkSubarraySum(nums, k):
    # Store: remainder → earliest index
    remainder_map = {0: -1}  # Handle sum divisible from start
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num
        remainder = prefix_sum % k

        if remainder in remainder_map:
            # Check if length >= 2
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            remainder_map[remainder] = i

    return False
```

#### Example Walkthrough
```
nums = [23, 2, 4, 6, 7], k = 6

prefix_sum: 23, 25, 29, 35, 42
remainders: 5,  1,  5,  5,  0

At i=2: remainder 5 seen before at i=0
Length = 2-0 = 2 >= 2 ✓
Subarray [23,2,4] sum=29, but (29-23)=6 divisible by 6!
```

#### Why This is Different
```
Not maintaining window of elements
Using math property: modulo arithmetic
Hash map stores indices, not window contents
```

#### Key Insight
> **Math Trick:** Prefix sum + modulo transforms problem
> Same remainder at different indices → divisible subarray between them

#### Complexity
- **Time:** O(n) - single pass with hash ops
- **Space:** O(min(n, k)) - at most k different remainders
- **Why Tricky:** Requires mathematical insight

---

### 5️⃣ **Problem #090: Frequency of Most Frequent Element** (MEDIUM)

**🎯 Task:** Max frequency after at most k increments
**📥 Input:** Integer array + k operations
**📤 Output:** Maximum frequency achievable
**🏷️ Tag:** Sort + Variable Window

#### Sorting Enables Sliding Window!
```
After sorting: [1, 2, 4, 8, 13]
To make window [1,2,4] all equal to 4:
Cost = 4*3 - (1+2+4) = 12 - 7 = 5
```

#### Algorithm
```python
def maxFrequency(nums, k):
    nums.sort()  # Critical step!

    left = 0
    max_freq = 1
    total = 0  # Sum of window

    for right in range(len(nums)):
        total += nums[right]

        # Cost to make all elements = nums[right]
        # = nums[right] * window_size - window_sum
        while nums[right] * (right - left + 1) - total > k:
            # Too expensive, shrink window
            total -= nums[left]
            left += 1

        max_freq = max(max_freq, right - left + 1)

    return max_freq
```

#### Why Must Sort?
```
Unsorted: [4, 2, 1] with k=5
Can't efficiently check all combinations

Sorted: [1, 2, 4] with k=5
Greedy works! Best to make consecutive elements equal
Window [1,2,4] → all 4: cost = 3+2 = 5 ✓
```

#### Cost Calculation
```
To make window [..., a, b, c, d] all equal to d:
Cost = d * count - sum(window)
Example: [1,2,4] → all 4
Cost = 4*3 - 7 = 5
```

#### Key Insight
> **Sort + Slide:** Sorting enables greedy window approach
> Cost formula avoids recalculating entire window

#### Complexity
- **Time:** O(n log n) - dominated by sorting
- **Space:** O(1) - in-place sorting
- **Why Harder:** Requires sorting + cost calculation

---

### 6️⃣ **Problem #037: Minimum Window Substring** (HARD)

**🎯 Task:** Find minimum substring containing all characters from target
**📥 Input:** String s + target string t
**📤 Output:** Minimum window substring
**🏷️ Tag:** Variable Window, Complex Tracking

#### The Hardest Sliding Window!
```
Must track:
- Character counts for target
- Character counts in current window
- How many unique chars satisfied
→ Multiple hash maps + counter
```

#### Algorithm
```python
def minWindow(s, t):
    if not s or not t:
        return ""

    # What we need
    target = Counter(t)
    required = len(target)  # Unique chars needed

    # Current window state
    window_counts = {}
    formed = 0  # How many unique chars satisfied

    # Result: (length, left, right)
    ans = float('inf'), 0, 0
    left = 0

    for right in range(len(s)):
        # Expand: add right char
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if this char requirement satisfied
        if char in target and window_counts[char] == target[char]:
            formed += 1

        # Contract: try to shrink
        while left <= right and formed == required:
            # Update result if smaller
            if right - left + 1 < ans[0]:
                ans = (right - left + 1, left, right)

            # Remove left char
            char = s[left]
            window_counts[char] -= 1
            if char in target and window_counts[char] < target[char]:
                formed -= 1
            left += 1

        right += 1

    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
```

#### The Complex Logic
```
1. Expand window (right++)
   - Add char to window_counts
   - Check if requirement satisfied (count matches target)
   - Track how many unique chars satisfied

2. Contract window (left++)
   - Only shrink when ALL requirements met
   - Try to minimize window
   - Stop when window becomes invalid

3. Track minimum window seen
```

#### Example Walkthrough
```
s = "ADOBECODEBANC", t = "ABC"

right=0: A → formed=1 (need 3)
right=1: D → formed=1
right=2: O → formed=1
right=3: B → formed=2
right=4: E → formed=2
right=5: C → formed=3 ✓ Window valid!

Now shrink:
Remove A: left=1, "DOBEC", still valid
Remove D: left=2, "OBEC", still valid
Remove O: left=3, "BEC", still valid
Remove B: left=4, formed=2, INVALID, stop

Continue expanding...
Eventually find "BANC" as minimum
```

#### Key Insight
> **Complex State Tracking:** Multiple counters + validity check
> Must shrink WHILE valid (find minimum before breaking)

#### Complexity
- **Time:** O(m + n) - each char visited at most twice
- **Space:** O(k) - unique chars in t
- **Why Hardest:** Complex state, multiple hash maps, tricky shrink logic

---

## 🔄 Algorithm Relationships

### Can We Reuse Previous Solutions?

| From → To | Can Modify? | What Changes? |
|-----------|-------------|---------------|
| #068 → #040 | ✅ Partial | Fixed → Variable window |
| #040 → #080 | ✅ YES | Count constraint → Set constraint |
| #080 → #037 | ❌ NO | Simple set → Complex multi-char tracking |
| #068 → #059 | ❌ NO | Different paradigm (prefix sum) |
| #040 → #090 | ✅ Partial | Add sorting + cost formula |

---

## 💡 Key Learning Insights

### 1. **Fixed vs Variable Window**

**Fixed Size:**
```python
for i in range(len(arr)):
    window.add(arr[i])
    if len(window) > k:
        window.remove(arr[i - k])
    # Check window
```
**Use when:** k is given, window size is constant

**Variable Size:**
```python
left = 0
for right in range(len(arr)):
    window.add(arr[right])
    while invalid(window):
        window.remove(arr[left])
        left += 1
    # Update answer
```
**Use when:** Find optimal window

### 2. **The While Loop Pattern**

```python
# WRONG: Using if
if constraint_violated:
    left += 1  # Only removes ONE element!

# CORRECT: Using while
while constraint_violated:
    left += 1  # Removes MULTIPLE elements if needed!
```

**Why while?** May need to remove multiple elements to restore validity

### 3. **When to Update Answer**

```python
# Pattern 1: After expanding (before shrinking)
for right in range(n):
    expand()
    while invalid:
        shrink()
    update_answer()  # ← Update here if want VALID windows

# Pattern 2: While shrinking
for right in range(n):
    expand()
    while valid:
        update_answer()  # ← Update here if want MINIMUM valid window
        shrink()
```

### 4. **Common Data Structures**

```python
# For uniqueness
window = set()

# For counts
window = {}  # or Counter()

# For sum
window_sum = 0

# For min/max
from collections import deque  # For monotonic deque
```

---

## 🎨 Visual Comparison Table

| Problem | Window Type | Constraint | Tracking Structure | Complexity |
|---------|-------------|------------|-------------------|------------|
| #068 | Fixed (k) | Duplicate in window | Set or Hash Map | O(n) |
| #040 | Variable | ≤ k zeros | Counter | O(n) |
| #080 | Variable | No duplicates | Set | O(n) |
| #059 | N/A (Prefix) | Sum % k == 0 | Hash Map | O(n) |
| #090 | Variable | Cost ≤ k | Sum + Sort | O(n log n) |
| #037 | Variable | Contains all chars | Multiple Hash Maps | O(m+n) |

---

## 🚀 Recommended Study Order

1. **Master Fixed Window:** #068 (Contains Duplicate II)
   - Understand fixed size maintenance
   - Practice set-based window

2. **Learn Variable Window:** #040 (Max Consecutive Ones)
   - Expand-shrink pattern
   - Simple constraint (count zeros)

3. **Set-Based Window:** #080 (Longest Substring)
   - Uniqueness constraint
   - While loop for shrinking

4. **Mathematical Variant:** #059 (Continuous Sum)
   - Prefix sum + modulo
   - Not pure sliding window

5. **Sorting + Window:** #090 (Frequency)
   - Preprocessing enables sliding window
   - Cost calculation

6. **Ultimate Challenge:** #037 (Minimum Window)
   - Complex multi-character tracking
   - Multiple hash maps
   - Tricky shrink logic

---

## 🎯 The Universal Template

### Template 1: Fixed Size Window
```python
def fixed_window(arr, k):
    window = set()  # or dict, or sum

    for i in range(len(arr)):
        # Add right element
        window.add(arr[i])

        # Remove left element if window too large
        if len(window) > k:
            window.remove(arr[i - k])

        # Process window
        check_condition(window)
```

### Template 2: Variable Size Window (Maximum)
```python
def variable_window_max(arr, constraint):
    left = 0
    max_result = 0
    window_state = init_state()

    for right in range(len(arr)):
        # Expand: add arr[right]
        update_window(window_state, arr[right])

        # Contract: shrink while invalid
        while invalid(window_state, constraint):
            remove_from_window(window_state, arr[left])
            left += 1

        # Update maximum
        max_result = max(max_result, right - left + 1)

    return max_result
```

### Template 3: Variable Size Window (Minimum)
```python
def variable_window_min(arr, target):
    left = 0
    min_result = float('inf')
    window_state = init_state()

    for right in range(len(arr)):
        # Expand: add arr[right]
        update_window(window_state, arr[right])

        # Contract: shrink while VALID
        while valid(window_state, target):
            # Update minimum while valid
            min_result = min(min_result, right - left + 1)
            remove_from_window(window_state, arr[left])
            left += 1

    return min_result if min_result != float('inf') else 0
```

---

## 📝 Interview Tips

### Red Flags (Common Mistakes)

1. **#068:** Using O(n) space for window when O(k) sufficient
2. **#040:** Using `if` instead of `while` for shrinking (misses cases)
3. **#080:** Not removing characters until duplicate gone (partial shrink)
4. **#059:** Forgetting length ≥ 2 requirement
5. **#090:** Not sorting array first (greedy doesn't work unsorted)
6. **#037:** Updating result after shrinking makes window invalid (loses valid minimum)

### Optimization Patterns

```python
# BAD: Recalculate window sum every time
def bad(arr, k):
    for i in range(len(arr)):
        window_sum = sum(arr[max(0, i-k+1):i+1])  # O(k) each time!

# GOOD: Maintain running sum
def good(arr, k):
    window_sum = 0
    for i in range(len(arr)):
        window_sum += arr[i]
        if i >= k:
            window_sum -= arr[i-k]  # O(1) each time!
```

### When to Use Sliding Window?

✅ **Use sliding window when:**
- Looking for contiguous subarray/substring
- Need to track elements in a range
- Can maintain window state incrementally (add/remove O(1))

❌ **Don't use sliding window when:**
- Need non-contiguous elements (use DP or hash map)
- Window state can't be updated incrementally
- Random access required

---

## 🧩 Pattern Recognition Guide

### Decision Tree

```
Start: Contiguous subarray/substring problem?
  ↓ YES
Window size known? → YES → Fixed window (#068)
  ↓ NO
Need prefix math? → YES → Prefix sum + hash (#059)
  ↓ NO
Simple constraint (count/sum)? → YES → Variable window (#040, #090)
  ↓ NO
Complex multi-char tracking? → YES → Variable window + hash maps (#037)
```

### Key Phrases That Suggest Sliding Window

- "contiguous subarray"
- "substring"
- "window of size k"
- "at most k [flips/operations]"
- "longest/shortest/maximum/minimum subarray"
- "consecutive elements"

---

## 💪 Practice Progression

```
Week 1: Master Fixed Window
- Day 1-2: Implement #068 from scratch 3 times
- Day 3-4: Solve similar problems
- Day 5: Understand set vs hash map trade-offs
- Day 6-7: Practice edge cases (k=0, k>n, etc.)

Week 2: Variable Window Foundation
- Day 1-3: #040 (simple constraint)
- Day 4-5: #080 (set-based)
- Day 6-7: Compare when while vs if fails

Week 3: Advanced Patterns
- Day 1-2: #059 (math variant)
- Day 3-4: #090 (sorting + window)
- Day 5-7: Identify when preprocessing helps

Week 4: Master Complexity
- Day 1-4: #037 (hardest problem)
- Day 5: Try all 6 problems in one sitting
- Day 6-7: Create your own sliding window problems
```

---

## 🎓 Conceptual Evolution

### Complexity Factors

1. **Window Type:** Fixed < Variable
2. **Constraint:** Simple count < Uniqueness < Multi-character
3. **State Tracking:** Single variable < Set < Multiple hash maps
4. **Preprocessing:** None < Sort < Complex math

### The Meta-Pattern

```
Fixed window (add/remove at fixed positions)
    ↓
Variable window (expand all, shrink when invalid)
    ↓
Optimization (find maximum valid window)
    ↓
Minimization (shrink while valid to find minimum)
    ↓
Complex tracking (multiple constraints simultaneously)
```

---

## 🔗 Related Patterns

Sliding window appears in:
- **Two pointers** - Sliding window is specialized two-pointer
- **Prefix sum** - Combined in #059
- **Hash map** - For tracking counts
- **Monotonic deque** - For min/max in window (not in this set)
- **Binary search** - On answer space with sliding window validation

---

**Summary:** Sliding window problems split into fixed-size (easier) and variable-size (harder). Fixed-size (#068) maintains exactly k elements. Variable-size expands right pointer every iteration, shrinks left pointer when invalid. Key decisions: (1) Fixed or variable? (2) Update answer after expanding (maximum) or while shrinking (minimum)? (3) What data structure tracks window state? Start with #068 for fixed window, master #040 for variable window with simple constraint, practice #080 for set-based uniqueness, understand #059's math trick, learn #090's sorting optimization, and finally conquer #037's complex multi-character tracking. The expand-while-invalid-shrink pattern is the foundation of all variable-size sliding window problems.
