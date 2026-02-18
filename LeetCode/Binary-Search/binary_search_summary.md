# Binary Search Problems - Comprehensive Analysis

## 🎯 Category Overview

**Total Problems:** 8
**Difficulty Range:** Easy → Medium → Hard
**Core Concept:** Binary search on arrays vs search on answer space

**🔑 Key Insight:** This category reveals the FUNDAMENTAL difference between:
- **Searching FOR a target** (classical binary search)
- **Searching FOR an answer** (binary search on solution space)

---

## 📊 Problem Progression Map

```
Level 1: Find Peak Element (#010) - Binary Search on Array Property
    ↓
Level 2: Kth Missing Positive (#041) - Bridge: Array → Answer Space
    ↓
Level 3: Find First/Last Position (#042) - Dual Binary Search
    ↓
Level 4: Cutting Ribbons (#074) - Pure Answer Space Search
    ↓
Level 5: Ship Capacity (#079) - Answer Space with Validation
    ↓
Level 6: Kth Smallest in Matrix (#084) - Value Range Search
    ↓
Level 7: Koko Eating Bananas (#094) - Speed as Answer Space
    ↓
Level 8: Median of Two Arrays (#100) - Partition Point Search (HARDEST)
```

---

## 🔍 The Two Paradigms

### Paradigm A: Search FOR Target (Classical)
**Question:** "Is this element in the array?"
**Search Space:** Array indices
**Example:** #042

### Paradigm B: Search FOR Answer (Advanced)
**Question:** "What's the minimum/maximum value that satisfies a condition?"
**Search Space:** Possible answer values
**Examples:** #074, #079, #094

---

## 📖 Problem-by-Problem Analysis

### 1️⃣ **Problem #010: Find Peak Element** (MEDIUM)

**🎯 Task:** Find any peak element where nums[i] > nums[i±1]
**📥 Input:** Integer array
**📤 Output:** Index of any peak
**🏷️ Tag:** Search Peak

#### What Makes This Special?
```
This is NOT searching for a specific value!
We're searching for an INDEX with a PROPERTY (peak)
```

#### Algorithm
```python
Binary search on property:
1. mid = (left + right) // 2
2. If nums[mid] < nums[mid+1]:
   - Peak must be on right (go uphill)
   - left = mid + 1
3. Else:
   - Peak is mid or on left
   - right = mid
4. Return left
```

#### Why Binary Search Works Here?
```
Key insight: If nums[mid] < nums[mid+1], we're on upslope
→ Guaranteed to find peak on right side
This guarantees O(log n) without seeing all elements!
```

#### Complexity
- **Time:** O(log n)
- **Space:** O(1)

---

### 2️⃣ **Problem #041: Kth Missing Positive** (EASY)

**🎯 Task:** Find kth missing positive number in sorted array
**📥 Input:** Sorted array + k
**📤 Output:** Integer (the kth missing number)
**🏷️ Tag:** Search Answer

#### Bridge Problem! 🌉
```
This introduces "searching for answer" concept
We binary search to find WHERE the kth missing number would be
```

#### Algorithm
```python
Binary search on missing count:
1. For index i: missing_count = arr[i] - (i + 1)
2. Binary search to find where missing_count >= k
3. If not found in array: k + array_length
4. Else: calculate from position found
```

#### Key Pattern Shift
```diff
- Classical: "Is target at this index?"
+ New: "How many missing at this position?"
```

#### Complexity
- **Time:** O(log n)
- **Space:** O(1)

---

### 3️⃣ **Problem #042: Find First and Last Position** (MEDIUM)

**🎯 Task:** Find starting and ending position of target
**📥 Input:** Sorted array + target
**📤 Output:** [start, end] or [-1, -1]
**🏷️ Tag:** Dual Binary Search

#### What's New?
```
TWO binary searches!
1. Find leftmost occurrence
2. Find rightmost occurrence
```

#### Algorithm
```python
def searchRange(nums, target):
    def findFirst():
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                right = mid - 1  # Keep searching left
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    def findLast():
        left, right = 0, len(nums) - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                result = mid
                left = mid + 1  # Keep searching right
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return result

    return [findFirst(), findLast()]
```

#### Pattern Recognition
```
Template for "first/last occurrence":
- To find FIRST: right = mid - 1 when found
- To find LAST: left = mid + 1 when found
```

#### Complexity
- **Time:** O(log n) × 2 = O(log n)
- **Space:** O(1)

---

### 4️⃣ **Problem #074: Cutting Ribbons** (MEDIUM)

**🎯 Task:** Find maximum length to cut k pieces
**📥 Input:** ribbon lengths array + k pieces needed
**📤 Output:** Maximum possible length
**🏷️ Tag:** Search Answer

#### 🎯 Pure "Answer Space" Binary Search!
```
We're NOT searching the array!
We're searching all possible LENGTH values: [1, 2, ..., max_length]
```

#### The Key Question
```
Instead of: "Is X in the array?"
Ask: "Can I achieve length X?"
```

#### Algorithm
```python
def maxLength(ribbons, k):
    def can_cut(length):
        """Can we get k pieces of this length?"""
        pieces = sum(ribbon // length for ribbon in ribbons)
        return pieces >= k

    left, right = 1, max(ribbons)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_cut(mid):
            result = mid
            left = mid + 1  # Try longer
        else:
            right = mid - 1  # Try shorter

    return result
```

#### Pattern Template
```
Binary search on answer space:
1. Define search range: [min_answer, max_answer]
2. Create validation function: can_achieve(value)
3. Binary search:
   - If achievable: try better (increase/decrease based on goal)
   - If not: adjust opposite direction
```

#### Complexity
- **Time:** O(n log(max_length))
- **Space:** O(1)

---

### 5️⃣ **Problem #079: Capacity To Ship Packages** (MEDIUM)

**🎯 Task:** Find minimum ship capacity to ship in D days
**📥 Input:** weights array + D days
**📤 Output:** Minimum capacity
**🏷️ Tag:** Search Capacity

#### Same Pattern as #074!
```
Search space: [max(weights), sum(weights)]
Question: "Can ship with this capacity?"
```

#### Algorithm
```python
def shipWithinDays(weights, days):
    def can_ship(capacity):
        """Can we ship in 'days' days with this capacity?"""
        current_weight = 0
        days_needed = 1

        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = weight
            else:
                current_weight += weight

        return days_needed <= days

    left, right = max(weights), sum(weights)

    while left < right:
        mid = (left + right) // 2
        if can_ship(mid):
            right = mid  # Try smaller capacity
        else:
            left = mid + 1  # Need larger capacity

    return left
```

#### Key Insight
```
Minimum capacity has monotonic property:
- If capacity X works → all capacity > X works
- If capacity X fails → all capacity < X fails
→ Perfect for binary search!
```

#### Complexity
- **Time:** O(n log(sum))
- **Space:** O(1)

---

### 6️⃣ **Problem #084: Kth Smallest in Sorted Matrix** (MEDIUM)

**🎯 Task:** Find kth smallest element in row/col sorted matrix
**📥 Input:** n×n matrix (sorted) + k
**📤 Output:** kth smallest value
**🏷️ Tag:** Search Value Range

#### Mind-Bending Approach!
```
We're NOT searching in the matrix!
We're searching the VALUE RANGE: [matrix[0][0], matrix[n-1][n-1]]
```

#### Algorithm
```python
def kthSmallest(matrix, k):
    def count_less_equal(target):
        """Count elements <= target"""
        count = 0
        row = len(matrix) - 1
        col = 0

        while row >= 0 and col < len(matrix):
            if matrix[row][col] <= target:
                count += row + 1
                col += 1
            else:
                row -= 1

        return count

    left, right = matrix[0][0], matrix[-1][-1]

    while left < right:
        mid = (left + right) // 2
        count = count_less_equal(mid)

        if count < k:
            left = mid + 1
        else:
            right = mid

    return left
```

#### The Trick
```
We don't search FOR the element
We search FOR a value where:
- Exactly k-1 elements are smaller
- This value exists in matrix
```

#### Complexity
- **Time:** O(n log(max-min))
- **Space:** O(1)

---

### 7️⃣ **Problem #094: Koko Eating Bananas** (MEDIUM)

**🎯 Task:** Find minimum eating speed to finish in H hours
**📥 Input:** piles array + H hours
**📤 Output:** Minimum speed
**🏷️ Tag:** Search Speed

#### Same Pattern Again!
```
Search space: [1, max(piles)]
Question: "Can finish with this speed?"
```

#### Algorithm
```python
def minEatingSpeed(piles, h):
    def can_finish(speed):
        """Can finish all piles with this speed?"""
        hours = sum((pile + speed - 1) // speed for pile in piles)
        return hours <= h

    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2
        if can_finish(mid):
            right = mid  # Try slower speed
        else:
            left = mid + 1  # Need faster speed

    return left
```

#### Pattern Recognition
```
This is IDENTICAL structure to #079!
- Different domain (speed vs capacity)
- Same algorithm (answer space binary search)
```

#### Complexity
- **Time:** O(n log m) where m = max(piles)
- **Space:** O(1)

---

### 8️⃣ **Problem #100: Median of Two Sorted Arrays** (HARD)

**🎯 Task:** Find median of two sorted arrays in O(log(min(m,n)))
**📥 Input:** Two sorted arrays
**📤 Output:** Median value
**🏷️ Tag:** Search Partition

#### The Ultimate Challenge!
```
Binary search on PARTITION POINT
Not searching for value, not searching answer space
Searching for the RIGHT WAY to split arrays!
```

#### Core Idea
```
Partition both arrays so:
- Left half has (m+n+1)/2 elements
- All left elements ≤ all right elements
→ Median is at partition boundary
```

#### Algorithm
```python
def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is smaller (optimization)
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1

        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1-1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]

        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2-1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # Found correct partition
            if (m + n) % 2 == 0:
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            right = partition1 - 1
        else:
            left = partition1 + 1
```

#### Why This is HARD
```
1. Must binary search on smaller array
2. Partition point determines both arrays' splits
3. Four boundary values to check
4. Edge cases when partition at start/end
5. Different logic for odd/even total length
```

#### Complexity
- **Time:** O(log(min(m,n))) - only search smaller array
- **Space:** O(1)

---

## 🔄 Algorithm Progression

### Can We Reuse Previous Solutions?

| From → To | Can Modify? | What Changes? |
|-----------|-------------|---------------|
| #010 → #041 | ✅ Partial | Add "missing count" calculation |
| #042 → #074 | ❌ NO | Different paradigm: target → answer space |
| #074 → #079 | ✅ YES | Same template, different validation |
| #079 → #094 | ✅ YES | Identical structure, different domain |
| #084 → #100 | ❌ NO | Value range → partition point |

---

## 💡 Key Learning Insights

### 1. **Two Distinct Patterns**

**Pattern A: Search in Array**
```python
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```

**Pattern B: Search Answer Space**
```python
while left < right:
    mid = (left + right) // 2
    if can_achieve(mid):
        right = mid  # or left = mid + 1
    else:
        left = mid + 1  # or right = mid - 1
```

### 2. **Monotonicity is Key**
```
Binary search works when:
✓ If X works, all values > X work (or vice versa)
✓ If X fails, all values < X fail (or vice versa)
```

### 3. **The Magic Question**
```
For answer space problems, ask:
"Can I achieve result with value X?"
NOT "Is X in the data?"
```

### 4. **Validation Function Pattern**
```python
def can_achieve(value):
    """
    Simulates whether value is achievable
    Returns: boolean
    """
    # Simulate the process
    # Count, calculate, or validate
    return result satisfies constraint
```

---

## 🎨 Visual Comparison

| Problem | Search What? | Search Range | Validation | Complexity |
|---------|-------------|--------------|------------|------------|
| #010 | Array property | Indices | Compare neighbors | O(log n) |
| #041 | Answer | [1, n+k] | Missing count | O(log n) |
| #042 | Target | Indices (2×) | Value match | O(log n) |
| #074 | Length | [1, max] | Can cut k pieces | O(n log m) |
| #079 | Capacity | [max, sum] | Can ship in D days | O(n log sum) |
| #084 | Value | [min, max] | Count ≤ value | O(n log range) |
| #094 | Speed | [1, max] | Can finish in H | O(n log max) |
| #100 | Partition | [0, m] | Valid split | O(log min) |

---

## 🚀 Recommended Study Order

1. **Master Classical First:** #042
   - Understand standard binary search
   - Learn first/last occurrence pattern

2. **Bridge to Answer Space:** #041
   - Transition from "find target" to "find answer"

3. **Answer Space Trio:** #074 → #079 → #094
   - These use SAME template!
   - Practice validation functions

4. **Advanced Applications:** #010, #084
   - Non-standard search spaces

5. **Ultimate Challenge:** #100
   - Combines everything
   - Requires deep understanding

---

## 🎯 The Universal Template

```python
def binary_search_answer(data, constraint):
    """
    Template for answer space binary search
    """
    # 1. Define answer range
    left, right = min_possible_answer, max_possible_answer

    # 2. Define validation
    def can_achieve(value):
        # Simulate if 'value' satisfies constraint
        return True/False

    # 3. Binary search
    result = left  # or right, depending on min/max goal
    while left <= right:
        mid = (left + right) // 2
        if can_achieve(mid):
            result = mid
            # Adjust based on goal:
            # For minimum: right = mid - 1
            # For maximum: left = mid + 1
        else:
            # Opposite adjustment

    return result
```

---

## 📝 Interview Tips

### Red Flags (Common Mistakes)

1. **#010:** Forgetting that ANY peak works (not a specific one)
2. **#042:** Using one binary search for both first AND last
3. **#074-#094:** Not recognizing answer space pattern
4. **#100:** Searching on larger array (should search smaller!)

### Optimization Opportunities

```python
# Instead of:
hours = 0
for pile in piles:
    hours += (pile + speed - 1) // speed

# Use:
hours = sum((pile + speed - 1) // speed for pile in piles)
```

---

## 🧩 Pattern Recognition Guide

### When to Binary Search on Answer Space?

Ask these questions:
1. ✅ Am I looking for minimum/maximum value?
2. ✅ Can I validate if a value works?
3. ✅ Does the validation have monotonic property?
4. ✅ Is brute force too slow?

If all YES → Answer space binary search!

### Template Recognition
```
"Find minimum X such that..." → Binary search on X
"Find maximum X such that..." → Binary search on X
"Kth smallest/largest..." → Might be binary search on value range
```

---

**Summary:** Binary search has TWO paradigms: searching IN data vs searching FOR answer. Master classical binary search first (#042), then learn answer space template (#074, #079, #094). The key is recognizing monotonic properties and asking "Can I achieve X?" instead of "Is X here?". Problems #074, #079, #094 use IDENTICAL templates—once you master one, you can solve all three!
