# 089. Range Sum Query - Immutable

**Difficulty:** EASY
**Frequency:** 32.0%
**Acceptance Rate:** 68.5%
**LeetCode Link:** [Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable)

---

## Problem Description

Given an integer array `nums`, handle multiple queries of the following type:

Calculate the sum of the elements of `nums` between indices `left` and `right` inclusive where `left <= right`.

Implement the `NumArray` class:
- `NumArray(int[] nums)` Initializes the object with the integer array `nums`.
- `int sumRange(int left, int right)` Returns the sum of the elements of `nums` between indices `left` and `right` inclusive (i.e., `nums[left] + nums[left + 1] + ... + nums[right]`).

**Constraints:**
- 1 <= nums.length <= 10^4
- -10^5 <= nums[i] <= 10^5
- 0 <= left <= right < nums.length
- At most 10^4 calls will be made to sumRange

---

## Examples

### Example 1
**Input:**
```
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
```
**Output:** `[null, 1, -1, -3]`
**Explanation:**
```
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```

### Example 2
**Input:**
```
["NumArray", "sumRange", "sumRange"]
[[[1]], [0, 0], [0, 0]]
```
**Output:** `[null, 1, 1]`
**Explanation:** Single element array

### Example 3
**Input:**
```
["NumArray", "sumRange"]
[[[5, -3, 4]], [1, 2]]
```
**Output:** `[null, 1]`
**Explanation:** sumRange(1, 2) = -3 + 4 = 1

### Example 4
**Input:**
```
["NumArray", "sumRange", "sumRange"]
[[[1, 2, 3, 4, 5]], [0, 4], [2, 3]]
```
**Output:** `[null, 15, 7]`
**Explanation:** Multiple range queries

---

## Optimal Solution

### Implementation

```python
class NumArray:
    """
    Range Sum Query using Prefix Sum.

    Time: O(n) initialization, O(1) per query
    Space: O(n) for prefix sum array
    """

    def __init__(self, nums: List[int]):
        """
        Initialize with prefix sum array.
        prefix_sum[i] = sum of nums[0..i-1]
        """
        self.prefix_sum = [0]

        # Build prefix sum array
        for num in nums:
            self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        """
        Return sum of elements from left to right inclusive.

        Sum[left, right] = prefix_sum[right+1] - prefix_sum[left]
        """
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
```

### Alternative Implementation

```python
class NumArray:
    """
    Alternative prefix sum implementation.
    """

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.n = len(nums)

        # Build prefix sum: prefix[i] = sum(nums[0:i+1])
        self.prefix = [0] * self.n

        self.prefix[0] = nums[0]
        for i in range(1, self.n):
            self.prefix[i] = self.prefix[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        """O(1) query time"""
        if left == 0:
            return self.prefix[right]

        return self.prefix[right] - self.prefix[left - 1]
```

### Complexity Analysis

**Initialization: O(n) - build prefix sum array. Query: O(1) - simple subtraction**
**Space: O(n) - store prefix sum array**

**Why This is Optimal:**
- Preprocessing with prefix sums enables O(1) queries
- Trade initialization time for fast repeated queries
- Optimal for scenarios with many sumRange calls
- Handles negative numbers correctly
- No complex data structures needed

---

## Categories & Tags

**Primary Topics:** Array, Design, Prefix Sum

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/range-sum-query-immutable)*
