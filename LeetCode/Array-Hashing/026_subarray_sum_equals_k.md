# 026. Subarray Sum Equals K

**Difficulty:** MEDIUM
**Frequency:** 71.4%
**Acceptance Rate:** 45.5%
**LeetCode Link:** [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k)

---

## Problem Description

Given an integer array `nums` and an integer `k`, return the total number of subarrays whose sum equals `k`.

A subarray is a contiguous non-empty sequence of elements within an array.

**Constraints:**
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7

---

## Examples

### Example 1
**Input:** `nums = [1,1,1], k = 2`
**Output:** `2`
**Explanation:** `[1,1]` at indices 0-1 and `[1,1]` at indices 1-2 both sum to 2.

### Example 2
**Input:** `nums = [1,2,3], k = 3`
**Output:** `2`
**Explanation:** `[3]` at index 2 and `[1,2]` at indices 0-1 both sum to 3.

### Example 3
**Input:** `nums = [1,-1,1,-1,1], k = 1`
**Output:** `5`
**Explanation:** Many subarrays sum to 1 due to negative numbers.

---

## Optimal Solution

### Key Insight

Use prefix sum + frequency hashmap. If `cursum - k` appeared `m` times before index `i`, then there are `m` subarrays ending at `i` that sum to `k`.

```
cursum[i] - cursum[j] = k  →  cursum[j] = cursum[i] - k
```

For each `cursum`, look up how many times `cursum - k` has appeared before.

### Why Frequency (Not Index)

The hashmap stores **how many times** each prefix sum has occurred, not the index. The same prefix sum can appear multiple times (especially with negative numbers), and each occurrence represents a distinct valid starting point for a subarray.

| Approach | Hash value | Use case |
|---|---|---|
| 560 (this problem) | **frequency** | count all subarrays |
| 523 (Continuous Subarray Sum) | **first index** | existence check only |

### Why Sliding Window Fails

`nums` can contain negative numbers, so the prefix sum is not monotonically increasing. Sliding window requires monotonicity to know when to shrink — it cannot work here.

### Implementation

```python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # frequency map: prefix sum → how many times seen
        prefixsum = {0: 1}  # empty prefix (sum=0) seen once
        cursum = 0
        result = 0

        for e in nums:
            cursum += e

            # how many prior prefixes allow cursum - that_prefix = k
            if (cursum - k) in prefixsum:
                result += prefixsum[cursum - k]

            prefixsum[cursum] = prefixsum.get(cursum, 0) + 1

        return result
```

### Why `{0: 1}` (not `{0: -1}`)

Initializing with frequency 1 means: we've seen the empty prefix (sum = 0) once.

If `cursum == k` at some index, then `cursum - k == 0`, and we correctly count it as 1 subarray (from index 0 to current). Without `{0: 1}`, whole-array subarrays starting at index 0 would be missed.

### Walkthrough

```
nums = [1, 1, 1], k = 2

start: prefixsum = {0: 1}, cursum = 0, result = 0

i=0, e=1: cursum=1, lookup (1-2)=-1 → not found. prefixsum={0:1, 1:1}
i=1, e=1: cursum=2, lookup (2-2)=0  → found 1 time. result=1. prefixsum={0:1, 1:1, 2:1}
i=2, e=1: cursum=3, lookup (3-2)=1  → found 1 time. result=2. prefixsum={0:1, 1:1, 2:1, 3:1}

Output: 2  ✓
```

### Complexity Analysis

**Time: O(n)** — single pass, O(1) hash operations

**Space: O(n)** — prefix sum frequency map

---

## Categories & Tags

**Primary Topics:** Array, Hash Table, Prefix Sum

**Difficulty Level:** MEDIUM

---

*Problem source: [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k)*
