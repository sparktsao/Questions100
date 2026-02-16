# 042. Find First and Last Position of Element in Sorted Array

**Difficulty:** MEDIUM
**Frequency:** 59.4%
**Acceptance Rate:** 46.8%
**LeetCode Link:** [Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)

---

## Problem Description

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with O(log n) runtime complexity.

**Constraints:**
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- nums is a non-decreasing array
- -10^9 <= target <= 10^9

---

## Examples

### Example 1
**Input:** `nums = [5,7,7,8,8,10], target = 8`
**Output:** `[3,4]`
**Explanation:** Target 8 appears at indices 3 and 4

### Example 2
**Input:** `nums = [5,7,7,8,8,10], target = 6`
**Output:** `[-1,-1]`
**Explanation:** Target 6 is not in the array

### Example 3
**Input:** `nums = [], target = 0`
**Output:** `[-1,-1]`
**Explanation:** Empty array, target cannot be found

### Example 4
**Input:** `nums = [1], target = 1`
**Output:** `[0,0]`
**Explanation:** Single element that matches target

---

## Optimal Solution

### Implementation

```python
def searchRange(nums: List[int], target: int) -> List[int]:
    """
    Find first and last position using two binary searches.

    Time: O(log n), Space: O(1)
    """
    def findBound(nums: List[int], target: int, isFirst: bool) -> int:
        """Helper to find left or right boundary"""
        left, right = 0, len(nums) - 1
        bound = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                bound = mid
                # Continue searching for first/last occurrence
                if isFirst:
                    right = mid - 1  # Search left half for first
                else:
                    left = mid + 1   # Search right half for last
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return bound

    if not nums:
        return [-1, -1]

    first = findBound(nums, target, True)
    if first == -1:
        return [-1, -1]

    last = findBound(nums, target, False)
    return [first, last]
```

### Alternative Concise Implementation

```python
def searchRange(nums: List[int], target: int) -> List[int]:
    """
    Using bisect library for cleaner code.

    Time: O(log n), Space: O(1)
    """
    import bisect

    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target) - 1

    if left <= right:
        return [left, right]
    return [-1, -1]
```

### Complexity Analysis

**Time: O(log n) - two binary searches. Space: O(1) - constant**

**Why This is Optimal:**
- Meets the required O(log n) time complexity constraint
- Two separate binary searches for first and last positions
- No extra space needed beyond variables
- Handles duplicates efficiently by continuing search after finding target

---

## Categories & Tags

**Primary Topics:** Array, Binary Search

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array)*
