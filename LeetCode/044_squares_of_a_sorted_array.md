# 044. Squares of a Sorted Array

**Difficulty:** EASY
**Frequency:** 59.4%
**Acceptance Rate:** 73.2%
**LeetCode Link:** [Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array)

---

## Problem Description

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order

**Follow up:** Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

---

## Examples

### Example 1
**Input:** `nums = [-4,-1,0,3,10]`
**Output:** `[0,1,9,16,100]`
**Explanation:** After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].

### Example 2
**Input:** `nums = [-7,-3,2,3,11]`
**Output:** `[4,9,9,49,121]`
**Explanation:** After squaring: [49,9,4,9,121], after sorting: [4,9,9,49,121]

### Example 3
**Input:** `nums = [-5,-3,-2,-1]`
**Output:** `[1,4,9,25]`
**Explanation:** All negative numbers, squares in reverse order

### Example 4
**Input:** `nums = [1,2,3,4,5]`
**Output:** `[1,4,9,16,25]`
**Explanation:** All positive numbers, squares maintain order

---

## Optimal Solution

### Implementation

```python
def sortedSquares(nums: List[int]) -> List[int]:
    """
    Two-pointer approach to merge squared values from both ends.

    Time: O(n), Space: O(n) for output array
    """
    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    pos = n - 1  # Fill result from right to left

    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2

        if left_square > right_square:
            result[pos] = left_square
            left += 1
        else:
            result[pos] = right_square
            right -= 1

        pos -= 1

    return result
```

### Brute Force Solution (For Comparison)

```python
def sortedSquares(nums: List[int]) -> List[int]:
    """
    Naive approach: square and sort.

    Time: O(n log n), Space: O(n)
    """
    return sorted(num ** 2 for num in nums)
```

### Alternative Implementation

```python
def sortedSquares(nums: List[int]) -> List[int]:
    """
    Find split point and merge like merge sort.

    Time: O(n), Space: O(n)
    """
    # Find the split point between negative and positive
    n = len(nums)
    split = 0

    while split < n and nums[split] < 0:
        split += 1

    # Merge two sorted arrays
    result = []
    left, right = split - 1, split

    while left >= 0 and right < n:
        left_sq = nums[left] ** 2
        right_sq = nums[right] ** 2

        if left_sq < right_sq:
            result.append(left_sq)
            left -= 1
        else:
            result.append(right_sq)
            right += 1

    # Append remaining elements
    while left >= 0:
        result.append(nums[left] ** 2)
        left -= 1

    while right < n:
        result.append(nums[right] ** 2)
        right += 1

    return result
```

### Complexity Analysis

**Time: O(n) - single pass with two pointers. Space: O(n) - output array**

**Why This is Optimal:**
- Achieves O(n) time by exploiting sorted property
- Key insight: largest squares are at either end of array
- No sorting needed, just merge from both ends
- Space is optimal since we must return output array

---

## Categories & Tags

**Primary Topics:** Array, Two Pointers, Sorting

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/squares-of-a-sorted-array)*
