# 017. Two Sum

**Difficulty:** EASY
**Frequency:** 76.4%
**Acceptance Rate:** 55.8%
**LeetCode Link:** [Two Sum](https://leetcode.com/problems/two-sum)

---

## Problem Description

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

**Constraints:**
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

---

## Examples

### Example 1
**Input:** `nums = [2,7,11,15], target = 9`
**Output:** `[0,1]`
**Explanation:** nums[0] + nums[1] == 9, so we return [0, 1]

### Example 2
**Input:** `nums = [3,2,4], target = 6`
**Output:** `[1,2]`
**Explanation:** nums[1] + nums[2] == 6

### Example 3
**Input:** `nums = [3,3], target = 6`
**Output:** `[0,1]`
**Explanation:** Both elements are 3, at different indices

### Example 4
**Input:** `nums = [-1,-2,-3,-4,-5], target = -8`
**Output:** `[2,4]`
**Explanation:** -3 + (-5) = -8, works with negative numbers

---

## Optimal Solution

### Implementation

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Find two numbers that add up to target using hash map.

    Time: O(n), Space: O(n)
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### Complexity Analysis

**Time: O(n) - single pass. Space: O(n) - hash map storage**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Array, Hash Table

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/two-sum)
