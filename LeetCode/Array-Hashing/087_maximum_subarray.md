# 087. Maximum Subarray

**Difficulty:** MEDIUM
**Frequency:** 32.0%
**Acceptance Rate:** 52.1%
**LeetCode Link:** [Maximum Subarray](https://leetcode.com/problems/maximum-subarray)

---

## Problem Description

Given an integer array `nums`, find the subarray with the largest sum, and return its sum.

A subarray is a contiguous non-empty sequence of elements within an array.

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

**Follow up:** If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

---

## Examples

### Example 1
**Input:** `nums = [-2,1,-3,4,-1,2,1,-5,4]`
**Output:** `6`
**Explanation:** The subarray [4,-1,2,1] has the largest sum 6

### Example 2
**Input:** `nums = [1]`
**Output:** `1`
**Explanation:** The subarray [1] has the largest sum 1

### Example 3
**Input:** `nums = [5,4,-1,7,8]`
**Output:** `23`
**Explanation:** The subarray [5,4,-1,7,8] has the largest sum 23

### Example 4
**Input:** `nums = [-1]`
**Output:** `-1`
**Explanation:** Single negative element

---

## Optimal Solution

### Implementation (Kadane's Algorithm)

```python
def maxSubArray(nums: List[int]) -> int:
    """
    Find maximum subarray sum using Kadane's Algorithm.

    Time: O(n), Space: O(1)
    """
    max_sum = nums[0]
    current_sum = 0

    for num in nums:
        # Reset if current sum becomes negative
        if current_sum < 0:
            current_sum = 0

        current_sum += num
        max_sum = max(max_sum, current_sum)

    return max_sum
```

### Alternative Implementation (DP Approach)

```python
def maxSubArray(nums: List[int]) -> int:
    """
    Dynamic programming approach.

    dp[i] = max sum ending at index i
    Time: O(n), Space: O(1) with optimization
    """
    max_ending_here = nums[0]
    max_so_far = nums[0]

    for i in range(1, len(nums)):
        # Either extend existing subarray or start new
        max_ending_here = max(nums[i], max_ending_here + nums[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far
```

### Divide and Conquer Solution

```python
def maxSubArray(nums: List[int]) -> int:
    """
    Divide and conquer approach.

    Time: O(n log n), Space: O(log n) for recursion
    """
    def max_crossing_sum(arr, left, mid, right):
        """Find max sum crossing the midpoint"""
        # Left side of mid
        left_sum = float('-inf')
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += arr[i]
            left_sum = max(left_sum, curr_sum)

        # Right side of mid
        right_sum = float('-inf')
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += arr[i]
            right_sum = max(right_sum, curr_sum)

        return left_sum + right_sum

    def max_subarray_helper(arr, left, right):
        if left == right:
            return arr[left]

        mid = (left + right) // 2

        # Max in left half, right half, or crossing mid
        return max(
            max_subarray_helper(arr, left, mid),
            max_subarray_helper(arr, mid + 1, right),
            max_crossing_sum(arr, left, mid, right)
        )

    return max_subarray_helper(nums, 0, len(nums) - 1)
```

### Complexity Analysis

**Kadane's Algorithm:**
**Time: O(n) - single pass. Space: O(1) - constant space**

**Divide and Conquer:**
**Time: O(n log n) - recursive splitting. Space: O(log n) - recursion stack**

**Why This is Optimal:**
- Kadane's algorithm achieves optimal O(n) time with O(1) space
- Single pass through array, no backtracking needed
- Handles all negative numbers correctly
- Simple to implement and understand
- Divide and conquer provides alternative approach with different insights

---

## Categories & Tags

**Primary Topics:** Array, Divide and Conquer, Dynamic Programming

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/maximum-subarray)*
