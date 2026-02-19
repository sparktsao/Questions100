# Two-Pointers Problems - Comprehensive Analysis




## 📋 Problems in This Category

- [002. Valid Word Abbreviation](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Two-Pointers/002_valid_word_abbreviation.md) - `Same Dir`
- [028. Dot Product of Two Sparse Vectors](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Two-Pointers/028_dot_product_of_two_sparse_vectors.md) - `Same Dir`
- [029. Valid Palindrome](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Two-Pointers/029_valid_palindrome.md) - `Opposite Dir`
- [030. Next Permutation](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Two-Pointers/030_next_permutation.md) - `Same Dir+Greedy`
- [033. Merge Sorted Array](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Two-Pointers/033_merge_sorted_array.md) - `Opposite Dir`
- [044. Squares of a Sorted Array](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Two-Pointers/044_squares_of_a_sorted_array.md) - `Opposite Dir`
- [065. 3Sum](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Two-Pointers/065_3sum.md) - `Opposite Dir`
- [073. Container With Most Water](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Two-Pointers/073_container_with_most_water.md) - `Opposite Dir+Greedy`
- [078. Strobogrammatic Number](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Two-Pointers/078_strobogrammatic_number.md) - `Opposite Dir`
- [088. Interval List Intersections](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Two-Pointers/088_interval_list_intersections.md) - `Same Dir`

---

## 🎯 Category Overview

**Total Problems:** 9
**Difficulty Range:** Easy → Medium
**Core Concept:** Using two pointers moving in same or opposite directions to solve array/list problems efficiently

**🔑 Key Insight:** The FUNDAMENTAL choice is pointer direction:
- **Same Direction** (both move forward) → Merging, sequential processing
- **Opposite Direction** (converge from ends) → Shrinking search space, optimization

---

## 📊 Problem Progression Map

```
Level 1: Strobogrammatic Number (#078) - Basic Opposite Direction Validation
    ↓
Level 2: Valid Word Abbreviation (#002) - Same Direction with Parsing
    ↓
Level 3: Merge Sorted Array (#033) - Same Direction from End
    ↓
Level 4: Squares of Sorted Array (#044) - Opposite Direction Merge
    ↓
Level 5: Interval List Intersections (#088) - Same Direction Two-List Merge
    ↓
Level 6: Dot Product Sparse Vectors (#028) - Same Direction with Optimization
    ↓
Level 7: Container With Most Water (#073) - Opposite Direction Greedy
    ↓
Level 8: 3Sum (#065) - Nested Two-Pointer with Deduplication
    ↓
Level 9: Next Permutation (#030) - Multi-Step In-Place (HARDEST)
```

---

## 🔍 The Two Paradigms

### Paradigm A: Same Direction (Forward Movement)
**When:** Merging, comparing, or processing two sequences
**Key:** Both pointers move forward, never backward
**Examples:** #002, #028, #033, #088

### Paradigm B: Opposite Direction (Converging)
**When:** Optimization, search space reduction, symmetric validation
**Key:** Start at both ends, move toward each other
**Examples:** #044, #065, #073, #078

---

## 📖 Problem-by-Problem Analysis

### 1️⃣ **Problem #078: Strobogrammatic Number** (EASY)

**🎯 Task:** Check if number looks same when rotated 180°
**📥 Input:** String representing a number
**📤 Output:** Boolean
**🏷️ Tag:** 2-Ptr, Opposite

#### What Makes This Special?
```
Simplest two-pointer pattern!
Validate pairs from both ends converging to center
```

#### Algorithm
```python
Opposite direction validation:
1. Map: 0→0, 1→1, 6→9, 8→8, 9→6
2. left = 0, right = len-1
3. While left <= right:
   - Check if num[left] valid and maps to num[right]
   - Move left++, right--
4. Return true if all pairs valid
```

#### Key Insight
> **Foundation Pattern:** Simplest opposite-direction use case
> Perfect for understanding pointer convergence

#### Complexity
- **Time:** O(n) - single pass to center
- **Space:** O(1) - constant map
- **Why Simplest:** Direct pair validation, no complex logic

---

### 2️⃣ **Problem #002: Valid Word Abbreviation** (EASY)

**🎯 Task:** Validate if abbreviation matches word
**📥 Input:** word string + abbr string with numbers
**📤 Output:** Boolean
**🏷️ Tag:** 2-Ptr, Same Direction

#### What Changed from #078?
```diff
+ Same direction (not opposite)
+ Must parse multi-digit numbers
+ Two different strings (not one)
- More complex state (number accumulation)
```

#### Algorithm
```python
Same direction with parsing:
1. i = j = 0  # Both start at beginning
2. While i < len(word) and j < len(abbr):
   - If abbr[j] is digit:
      * Parse full number (while loop)
      * Skip that many in word: i += num
   - Else:
      * Check character match
      * Move both: i++, j++
3. Valid if both reach end
```

#### Can We Reuse #078's Algorithm?
**NO - Different paradigm:**
- #078: Opposite direction, symmetric check
- #002: Same direction, sequential processing
- **Learning:** Direction determines algorithm structure

#### Key Insight
> **Same Direction Intro:** First problem showing forward-moving pointers
> Must handle different speeds (number skipping)

#### Complexity
- **Time:** O(n) - single pass through both strings
- **Space:** O(1) - two pointers only
- **Why Harder than #078:** Number parsing adds complexity

---

### 3️⃣ **Problem #033: Merge Sorted Array** (EASY)

**🎯 Task:** Merge two sorted arrays into first array
**📥 Input:** nums1 (size m+n), nums2 (size n)
**📤 Output:** Modify nums1 in-place
**🏷️ Tag:** 2-Ptr, Backward Fill

#### What's New?
```
Same direction BUT from the END!
Fills backwards to avoid overwriting
```

#### Algorithm
```python
Same direction from end:
1. p1 = m-1, p2 = n-1, p = m+n-1
2. While p2 >= 0:
   - If p1 >= 0 and nums1[p1] > nums2[p2]:
      * nums1[p] = nums1[p1]
      * p1--
   - Else:
      * nums1[p] = nums2[p2]
      * p2--
   - p--
```

#### Why From End?
```
Forward fill: Must shift elements (expensive)
Backward fill: Empty space at end (free!)
→ O(1) space by clever pointer placement
```

#### Key Insight
> **Direction Matters:** Same-direction can go forward OR backward
> Choose based on where empty space is

#### Complexity
- **Time:** O(m+n) - single pass
- **Space:** O(1) - in-place merge
- **Why Clever:** Avoids O(n) shifting cost

---

### 4️⃣ **Problem #044: Squares of Sorted Array** (EASY)

**🎯 Task:** Return sorted squares of sorted array
**📥 Input:** Sorted array (can have negatives)
**📤 Output:** Sorted squares
**🏷️ Tag:** 2-Ptr, Opposite

#### What Changed from #033?
```diff
+ Opposite direction (not same)
+ Build result array (not in-place)
+ Negatives complicate ordering
- Largest squares at BOTH ends!
```

#### Algorithm
```python
Opposite direction fill:
1. result = [0] * n
2. left = 0, right = n-1, pos = n-1
3. While left <= right:
   - sq_left = nums[left]²
   - sq_right = nums[right]²
   - If sq_left > sq_right:
      * result[pos] = sq_left
      * left++
   - Else:
      * result[pos] = sq_right
      * right--
   - pos--
4. Return result
```

#### Key Insight
> **Largest at Ends:** Negative squares can be large!
> [-4,-1,0,3,10] → squares 16,1,0,9,100 → largest at ends

#### Complexity
- **Time:** O(n) - single pass
- **Space:** O(n) - output array
- **Why O(n) beats O(n log n):** Exploit sorted property

---

### 5️⃣ **Problem #088: Interval List Intersections** (MEDIUM)

**🎯 Task:** Find all intersections of two interval lists
**📥 Input:** Two sorted lists of intervals
**📤 Output:** List of intersection intervals
**🏷️ Tag:** 2-Ptr, Same Direction

#### What Changed from Previous?
```diff
+ Process TWO lists simultaneously
+ Find overlap regions (not just compare)
+ Decide which pointer to advance
- More complex intersection logic
```

#### Algorithm
```python
Same direction merge:
1. i = j = 0
2. While i < len(first) and j < len(second):
   - start = max(first[i][0], second[j][0])
   - end = min(first[i][1], second[j][1])
   - If start <= end:  # Valid intersection
      * result.append([start, end])
   - Advance pointer of interval that ends first:
      * If first[i][1] < second[j][1]: i++
      * Else: j++
3. Return result
```

#### The Trick
```
Intersection exists when: max(starts) <= min(ends)
Advance whichever interval ends first
→ Guarantees we don't miss any intersections
```

#### Key Insight
> **Merge Pattern:** Like merge sort, but finding overlaps
> Advance whichever exhausts first

#### Complexity
- **Time:** O(m+n) - single pass through both lists
- **Space:** O(1) - excluding output
- **Why Optimal:** Must check every interval pair

---

### 6️⃣ **Problem #028: Dot Product of Sparse Vectors** (MEDIUM)

**🎯 Task:** Compute dot product efficiently for sparse vectors
**📥 Input:** Two vectors (mostly zeros)
**📤 Output:** Dot product value
**🏷️ Tag:** 2-Ptr, Sparse Optimization

#### Design Challenge
```
Naive: O(n) time, O(n) space
Sparse: O(L) time, O(L) space where L = non-zeros
→ Huge savings when L << n
```

#### Algorithm (Two Approaches)

**Approach 1: Hash Map**
```python
class SparseVector:
    def __init__(self, nums):
        self.non_zero = {i: val for i, val in enumerate(nums) if val != 0}

    def dotProduct(self, vec):
        # Iterate smaller vector
        if len(self.non_zero) > len(vec.non_zero):
            return vec.dotProduct(self)

        result = 0
        for i, val in self.non_zero.items():
            if i in vec.non_zero:
                result += val * vec.non_zero[i]
        return result
```

**Approach 2: Two Pointers on Sorted Pairs**
```python
class SparseVector:
    def __init__(self, nums):
        self.pairs = [(i, val) for i, val in enumerate(nums) if val != 0]

    def dotProduct(self, vec):
        i = j = 0
        result = 0
        while i < len(self.pairs) and j < len(vec.pairs):
            if self.pairs[i][0] == vec.pairs[j][0]:
                result += self.pairs[i][1] * vec.pairs[j][1]
                i += 1
                j += 1
            elif self.pairs[i][0] < vec.pairs[j][0]:
                i += 1
            else:
                j += 1
        return result
```

#### Key Insight
> **Sparsity Optimization:** Store only non-zeros
> Two-pointer merge finds matching indices efficiently

#### Complexity
- **Time:** O(n) init, O(L) dot product
- **Space:** O(L) where L = non-zero count
- **Why Smart:** Skip all zero multiplications

---

### 7️⃣ **Problem #073: Container With Most Water** (MEDIUM)

**🎯 Task:** Find two lines forming container with max water
**📥 Input:** Array of heights
**📤 Output:** Maximum area
**🏷️ Tag:** 2-Ptr, Opposite, Greedy

#### Greedy Insight
```
Area = min(height[left], height[right]) × (right - left)
Key: Moving shorter line MIGHT find taller line
     Moving taller line CAN'T improve (width shrinks)
```

#### Algorithm
```python
Opposite direction greedy:
1. left = 0, right = n-1
2. max_area = 0
3. While left < right:
   - width = right - left
   - height = min(height[left], height[right])
   - area = width × height
   - max_area = max(max_area, area)
   - Move pointer pointing to shorter line:
      * If height[left] < height[right]: left++
      * Else: right--
4. Return max_area
```

#### Why Greedy Works?
```
Moving shorter line: Might find taller, could improve
Moving taller line: Width shrinks, height can't improve → no gain
→ Greedy choice is optimal!
```

#### Key Insight
> **Greedy + Two-Pointer:** Not all two-pointer is linear search
> Greedy elimination can find optimal in O(n)

#### Complexity
- **Time:** O(n) - single pass
- **Space:** O(1)
- **Why Surprising:** Greedy finds global optimum!

---

### 8️⃣ **Problem #065: 3Sum** (MEDIUM)

**🎯 Task:** Find all unique triplets that sum to zero
**📥 Input:** Integer array
**📤 Output:** List of triplets [a,b,c] where a+b+c=0
**🏷️ Tag:** 2-Ptr, Opposite, Nested

#### Nested Two-Pointer!
```
Outer loop: Fix first element
Inner: Two-pointer on remaining array
→ O(n²) instead of O(n³) brute force
```

#### Algorithm
```python
Sort + nested two-pointer:
1. Sort array
2. For i in range(n-2):
   - Skip duplicates: if nums[i] == nums[i-1] continue
   - target = -nums[i]
   - left = i+1, right = n-1
   - While left < right:
      * sum = nums[left] + nums[right]
      * If sum == target:
         - Add triplet
         - Skip duplicates for left and right
         - left++, right--
      * Elif sum < target: left++
      * Else: right--
```

#### Deduplication is Critical
```python
# Skip duplicate first element
if i > 0 and nums[i] == nums[i-1]:
    continue

# Skip duplicate second element
while left < right and nums[left] == nums[left+1]:
    left += 1

# Skip duplicate third element
while left < right and nums[right] == nums[right-1]:
    right -= 1
```

#### Key Insight
> **Nested Pattern:** Fix one element, two-pointer on rest
> Sorting enables duplicate skipping

#### Complexity
- **Time:** O(n²) - outer loop O(n), inner two-pointer O(n)
- **Space:** O(1) - excluding output
- **Why Optimal:** Can't do better than O(n²) for 3Sum

---

### 9️⃣ **Problem #030: Next Permutation** (MEDIUM)

**🎯 Task:** Find next lexicographically greater permutation
**📥 Input:** Array of integers
**📤 Output:** Modify in-place to next permutation
**🏷️ Tag:** 2-Ptr, Multi-Step

#### The Hardest Two-Pointer Problem!
```
Not just one two-pointer operation
Three distinct phases:
1. Find pivot (backward scan)
2. Find swap target (backward scan)
3. Reverse suffix (two-pointer)
```

#### Algorithm
```python
Multi-step approach:
# Step 1: Find pivot (first decreasing from right)
i = n - 2
while i >= 0 and nums[i] >= nums[i+1]:
    i -= 1

# Step 2: If pivot exists, swap with next larger
if i >= 0:
    j = n - 1
    while nums[j] <= nums[i]:
        j -= 1
    nums[i], nums[j] = nums[j], nums[i]

# Step 3: Reverse suffix
left, right = i + 1, n - 1
while left < right:
    nums[left], nums[right] = nums[right], nums[left]
    left += 1
    right -= 1
```

#### Example Walkthrough
```
Input: [1,5,8,4,7,6,5,3,1]

Step 1: Find pivot
Scan right: 1<3<5<6<7 but 4<7, so pivot=4 (index 3)

Step 2: Find next larger in suffix [7,6,5,3,1]
Next larger than 4 is 5, swap: [1,5,8,5,7,6,4,3,1]

Step 3: Reverse suffix [7,6,4,3,1]
Result: [1,5,8,5,1,3,4,6,7]
```

#### Why Three Steps?
```
1. Pivot: Rightmost position we can increase
2. Swap: Increase minimally (swap with next larger)
3. Reverse: Make suffix smallest (it's descending, reverse it)
→ Together: Minimal increase = next permutation
```

#### Key Insight
> **Complex In-Place:** Multiple two-pointer operations
> Each phase has different direction and purpose

#### Complexity
- **Time:** O(n) - three passes
- **Space:** O(1) - in-place
- **Why Hardest:** Requires understanding permutation structure

---

## 🔄 Algorithm Relationships

### Can We Reuse Previous Solutions?

| From → To | Can Modify? | What Changes? |
|-----------|-------------|---------------|
| #078 → #002 | ❌ NO | Opposite → Same direction |
| #002 → #033 | ✅ Partial | Add backward filling |
| #033 → #044 | ❌ NO | Same → Opposite direction |
| #044 → #088 | ✅ YES | Similar merge pattern |
| #088 → #028 | ✅ YES | Add sparsity optimization |
| #073 → #065 | ✅ Partial | Add nesting + dedup |
| Any → #030 | ❌ NO | Multi-step algorithm |

---

## 💡 Key Learning Insights

### 1. **Direction is Everything**

**Same Direction (Forward):**
```python
left = right = 0
while right < n:
    # Process elements
    # Move pointers forward
    left += condition
    right += 1
```
**Use when:** Merging, sequential processing

**Opposite Direction (Converging):**
```python
left, right = 0, n-1
while left < right:
    # Compare/process ends
    # Move one or both inward
    left += 1  # or
    right -= 1
```
**Use when:** Optimization, search space reduction

### 2. **Pointer Speed Matters**

```python
# Same speed (synchronous)
left += 1
right += 1

# Different speeds (asynchronous)
left += 1  # Maybe
right += condition  # Maybe

# Fast-slow pointers
slow += 1
fast += 2
```

### 3. **Direction Can Be Backward**

```python
# Forward fill (needs shifting)
for i in range(n):
    result[i] = process(...)

# Backward fill (uses empty space)
for i in range(n-1, -1, -1):
    result[i] = process(...)
```

**Key:** Choose direction based on empty space location

### 4. **Nested Two-Pointer**

```python
for i in range(n):
    left, right = i+1, n-1
    while left < right:
        # Inner two-pointer
        process(i, left, right)
```
**Result:** O(n²) instead of O(n³)

---

## 🎨 Visual Comparison Table

| Problem | Direction | Fill Order | Primary Operation | Complexity |
|---------|-----------|------------|-------------------|------------|
| #078 | ← → | N/A | Validation | O(n) |
| #002 | → → | Forward | Match + Skip | O(n) |
| #033 | ← ← | Backward | Merge | O(m+n) |
| #044 | ← → | Backward | Compare | O(n) |
| #088 | → → | Forward | Intersect | O(m+n) |
| #028 | → → | N/A | Merge Sparse | O(L) |
| #073 | ← → | N/A | Greedy Max | O(n) |
| #065 | Nested | N/A | Sum Search | O(n²) |
| #030 | Multiple | Mixed | Permutation | O(n) |

---

## 🚀 Recommended Study Order

1. **Start Simple Opposite:** #078 (Strobogrammatic)
   - Master opposite-direction convergence
   - Understand symmetric validation

2. **Learn Same Direction:** #002 (Valid Abbreviation)
   - Both pointers move forward
   - Handle different speeds

3. **Backward Fill:** #033 (Merge Sorted Array)
   - Same direction from end
   - In-place optimization

4. **Opposite Merge:** #044 (Squares)
   - Fill from both ends
   - Largest at extremes

5. **Two-List Merge:** #088 (Intervals)
   - Synchronize two inputs
   - Intersection logic

6. **Sparse Optimization:** #028 (Dot Product)
   - Skip unnecessary work
   - Trade space for time

7. **Greedy Optimization:** #073 (Container)
   - Opposite direction + greedy
   - Prune search space

8. **Nested Pattern:** #065 (3Sum)
   - Fix element + two-pointer
   - Deduplication

9. **Complex Multi-Step:** #030 (Next Permutation)
   - Multiple phases
   - Each phase uses two-pointer differently

---

## 🎯 The Universal Patterns

### Pattern 1: Same Direction Sequential
```python
def same_direction_sequential(arr1, arr2):
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        # Process current positions
        # Advance based on condition
        if condition:
            i += 1
        else:
            j += 1
```
**Use cases:** #002, #088

### Pattern 2: Same Direction From End
```python
def same_direction_backward(arr, m, n):
    p1, p2 = m-1, n-1
    p = m+n-1
    while p2 >= 0:
        # Fill backward
        if p1 >= 0 and arr[p1] > other[p2]:
            arr[p] = arr[p1]
            p1 -= 1
        else:
            arr[p] = other[p2]
            p2 -= 1
        p -= 1
```
**Use cases:** #033

### Pattern 3: Opposite Direction Converge
```python
def opposite_direction(arr):
    left, right = 0, len(arr)-1
    while left < right:
        # Process both ends
        if condition(arr[left], arr[right]):
            left += 1
        else:
            right -= 1
```
**Use cases:** #044, #073, #078

### Pattern 4: Nested Two-Pointer
```python
def nested_two_pointer(arr):
    arr.sort()
    for i in range(len(arr)):
        left, right = i+1, len(arr)-1
        while left < right:
            # Inner two-pointer
            if condition(arr[i], arr[left], arr[right]):
                left += 1
            else:
                right -= 1
```
**Use cases:** #065

---

## 📝 Interview Tips

### Red Flags (Common Mistakes)

1. **#002:** Forgetting leading zero check (abbr starts with '0')
2. **#033:** Filling forward (requires O(n²) shifts instead of O(n))
3. **#044:** Using O(n log n) sort when O(n) two-pointer possible
4. **#065:** Not handling duplicates properly (returns duplicate triplets)
5. **#073:** Moving taller line instead of shorter (misses optimal)
6. **#078:** Using string reversal instead of two-pointer (O(n) space)
7. **#030:** Not understanding why suffix must be reversed

### Optimization Opportunities

```python
# BAD: Create new array unnecessarily
result = []
for i in range(len(arr)):
    result.append(arr[i] * arr[i])
result.sort()

# GOOD: Two pointer from ends
result = [0] * len(arr)
left, right = 0, len(arr)-1
pos = len(arr)-1
while left <= right:
    # Fill from largest
```

### Time Limit Considerations
- #078, #002, #033, #044, #088: O(n) achievable ✅
- #028: O(L) where L << n for sparse ✅
- #073: O(n) with greedy ✅
- #065: O(n²) unavoidable, but must optimize dedup ✅
- #030: O(n) with three passes ✅

---

## 🧩 Pattern Recognition Guide

### When to Use Same Direction?

Ask these questions:
1. ✅ Merging two sorted sequences?
2. ✅ Processing elements sequentially?
3. ✅ Both pointers always move forward?
4. ✅ Need to synchronize two inputs?

If all YES → Same direction!

### When to Use Opposite Direction?

1. ✅ Comparing elements from both ends?
2. ✅ Shrinking search space?
3. ✅ Looking for optimal pairing?
4. ✅ Symmetric property to check?

If all YES → Opposite direction!

### Direction Decision Tree

```
Start
  ↓
Need to compare ends? → YES → Opposite direction (#044, #073, #078)
  ↓ NO
Multiple lists to merge? → YES → Same direction (#028, #033, #088)
  ↓ NO
Need to fix element + search? → YES → Nested (#065)
  ↓ NO
Complex multi-step? → YES → Multiple phases (#030)
```

---

## 🔗 Related Concepts

Two-pointer patterns appear in:
- **Sliding window** - Variable-size two-pointer
- **Fast-slow pointers** - Cycle detection (linked lists)
- **Merge algorithms** - Merge sort, merge intervals
- **Search space reduction** - Binary search alternative
- **In-place algorithms** - Space optimization
- **Greedy algorithms** - Combined with two-pointer (#073)

---

## 💪 Practice Progression

```
Week 1: Master Basics
- Day 1-2: #078 (Opposite validation)
- Day 3-4: #002 (Same direction)
- Day 5-6: #033 (Backward fill)
- Day 7: Review and compare

Week 2: Intermediate Patterns
- Day 1-2: #044 (Opposite merge)
- Day 3-4: #088 (Two-list merge)
- Day 5-6: #028 (Sparse optimization)
- Day 7: Implement both approaches for #028

Week 3: Advanced Techniques
- Day 1-2: #073 (Greedy)
- Day 3-5: #065 (Nested two-pointer)
- Day 6-7: Compare nested vs brute force

Week 4: Master Complexity
- Day 1-4: #030 (Multi-step)
- Day 5: Try all 9 problems from scratch
- Day 6-7: Identify patterns in new problems
```

---

## 🎓 Conceptual Evolution

### Complexity Factors

1. **Direction Complexity:** Opposite < Same < Nested
2. **Speed Complexity:** Synchronous < Asynchronous < Conditional
3. **Fill Complexity:** Forward < Backward < Multiple passes
4. **Logic Complexity:** Validation < Merge < Optimization < Multi-step

### The Meta-Pattern

```
Simple validation (opposite direction)
    ↓
Sequential processing (same direction)
    ↓
Backward optimization (same direction from end)
    ↓
Greedy elimination (opposite direction)
    ↓
Nested search (fix + two-pointer)
    ↓
Multi-step manipulation (multiple phases)
```

This progression shows increasing sophistication!

---

**Summary:** Two-pointer problems split into two paradigms: same direction (for merging/sequential processing) and opposite direction (for optimization/symmetric validation). Start with simple opposite-direction validation (#078), learn same-direction merging (#002, #033, #088), master backward filling (#033, #044), understand greedy optimization (#073), practice nested patterns (#065), and finally tackle multi-step complexity (#030). The key is recognizing which direction to use based on the problem structure: merge → same direction, optimize → opposite direction.
