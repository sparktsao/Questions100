# 091. Random Pick Index

**Difficulty:** MEDIUM
**Frequency:** 32.0%
**Acceptance Rate:** 64.5%
**LeetCode Link:** [Random Pick Index](https://leetcode.com/problems/random-pick-index)

---

## Problem Description

Given an integer array `nums` with possible duplicates, randomly output the index of a given `target` number. You can assume that the given target number must exist in the array.

Implement the `Solution` class:

- `Solution(int[] nums)` Initializes the object with the array `nums`
- `int pick(int target)` Picks a random index `i` from `nums` where `nums[i] == target`. If there are multiple valid indices, each index should have equal probability of returning

**Constraints:**
- 1 <= nums.length <= 2 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- target is an integer from nums
- At most 10^4 calls to pick

---

## Examples

### Example 1
**Input:** `["Solution", "pick", "pick", "pick"]\n[[[1,2,3,3,3]], [3], [1], [3]]`
**Output:** `[null, 4, 0, 2]`
**Explanation:** pick(3) can return 2, 3, or 4 with equal probability

### Example 2
**Input:** `nums = [1,1,1], pick(1)`
**Output:** `0, 1, or 2`
**Explanation:** All indices equally likely

### Example 3
**Input:** `nums = [1,2,3], pick(2)`
**Output:** `1`
**Explanation:** Only one occurrence of 2

---

## Optimal Solution

### Implementation

```python
class Solution:
    def __init__(self, nums: List[int]):
        """
        Store array for reservoir sampling.

        Time: O(1), Space: O(n)
        """
        self.nums = nums

    def pick(self, target: int) -> int:
        """
        Reservoir sampling for uniform random selection.

        Time: O(n), Space: O(1)
        """
        import random
        result = -1
        count = 0

        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                # Reservoir sampling: replace with probability 1/count
                if random.randint(1, count) == 1:
                    result = i

        return result
```

### Complexity Analysis

**Time: O(n) for pick. Space: O(n) - storing array**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, Math, Reservoir Sampling, Randomized

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/random-pick-index)*
