# 012. Random Pick with Weight

**Difficulty:** MEDIUM
**Frequency:** 80.5%
**Acceptance Rate:** 48.3%
**LeetCode Link:** [Random Pick with Weight](https://leetcode.com/problems/random-pick-with-weight)

---

## Problem Description

You are given a 0-indexed array of positive integers `w` where `w[i]` describes the weight of the i-th index.

You need to implement the function `pickIndex()`, which randomly picks an index in the range `[0, w.length - 1]` (inclusive) and returns it. The probability of picking an index `i` is `w[i] / sum(w)`.

For example, if `w = [1, 3]`, the probability of picking index 0 is `1 / (1 + 3) = 0.25` (25%), and the probability of picking index 1 is `3 / (1 + 3) = 0.75` (75%).

**Constraints:**
- 1 <= w.length <= 10^4
- 1 <= w[i] <= 10^5
- pickIndex will be called at most 10^4 times

---

## Examples

### Example 1
**Input:** `["Solution","pickIndex"], [[[1]],[]]`
**Output:** `[null,0]`
**Explanation:** The only option is to return 0 since there is only one element in w.

### Example 2
**Input:** `["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"], [[[1,3]],[],[],[],[],[]]`
**Output:** `[null,1,1,1,1,0]`
**Explanation:**
- Solution(w = [1,3]) creates the Solution object
- pickIndex() should return index 1 with 75% probability (weight 3) and index 0 with 25% probability (weight 1)
- In this example, it returns 1 four times and 0 once, which is consistent with the expected probability distribution

### Example 3
**Input:** `["Solution","pickIndex"], [[[1,2,3,4]],[]]`
**Output:** `[null,3]`
**Explanation:** With weights [1,2,3,4], index 3 has the highest probability (4/10 = 40%) of being picked

### Example 4
**Input:** `["Solution","pickIndex","pickIndex"], [[[5,5,5,5]],[],[]]`
**Output:** `[null,2,0]`
**Explanation:** All weights are equal, so each index has equal 25% probability of being picked

---

## Optimal Solution

### Implementation

```python
import random
from typing import List

class Solution:
    def __init__(self, w: List[int]):
        """
        Initialize with weights array, computing prefix sums for weighted random selection.

        Time: O(n), Space: O(n)
        """
        self.prefix_sums = []
        prefix_sum = 0

        # Build prefix sum array
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)

        self.total_sum = prefix_sum

    def pickIndex(self) -> int:
        """
        Pick a random index based on weights using binary search.

        Time: O(log n), Space: O(1)
        """
        # Generate random number in range [1, total_sum]
        target = random.randint(1, self.total_sum)

        # Binary search for the target in prefix sums
        left, right = 0, len(self.prefix_sums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if self.prefix_sums[mid] < target:
                left = mid + 1
            else:
                right = mid

        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
```

### Complexity Analysis

**Time: O(n) for initialization, O(log n) for pickIndex. Space: O(n) - prefix sum array**

**Why This is Optimal:**
- Prefix sum array enables O(log n) weighted random selection via binary search
- Initialization is O(n), which is unavoidable since we must process all weights
- Space complexity is optimal for this approach
- Binary search efficiently finds the target index in the cumulative weight distribution
- Handles all edge cases including single element and equal weights correctly

---

## Categories & Tags

**Primary Topics:** Array, Math, Binary Search, Prefix Sum, Randomized

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/random-pick-with-weight)
