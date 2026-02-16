# 010. Find Peak Element

**Difficulty:** MEDIUM
**Frequency:** 82.9%
**Acceptance Rate:** 46.5%
**LeetCode Link:** [Find Peak Element](https://leetcode.com/problems/find-peak-element)

---

## Problem Description

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

**Constraints:**
- 1 <= nums.length <= 1000
- -2^31 <= nums[i] <= 2^31 - 1
- nums[i] != nums[i + 1] for all valid i

---

## Examples

### Example 1
**Input:** `nums = [1,2,3,1]`
**Output:** `2`
**Explanation:** 3 is a peak element, index 2

### Example 2
**Input:** `nums = [1,2,1,3,5,6,4]`
**Output:** `5`
**Explanation:** 6 is a peak at index 5 (or index 1 with value 2)

### Example 3
**Input:** `nums = [1]`
**Output:** `0`
**Explanation:** Single element is a peak

### Example 4
**Input:** `nums = [1,2]`
**Output:** `1`
**Explanation:** 2 is the peak

---

## Optimal Solution

### Implementation

```python
def findPeakElement(nums: List[int]) -> int:
    """
    Binary search to find peak in O(log n).

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] > nums[mid + 1]:
            # Peak is on the left side (or mid is peak)
            right = mid
        else:
            # Peak is on the right side
            left = mid + 1

    return left
```

### Complexity Analysis

**Time: O(log n) - binary search. Space: O(1) - constant**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Array, Binary Search

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/find-peak-element)
