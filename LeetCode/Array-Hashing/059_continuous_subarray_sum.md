# 059. Continuous Subarray Sum

**Difficulty:** MEDIUM
**Frequency:** 47.0%
**Acceptance Rate:** 30.9%
**LeetCode Link:** [Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum)

---

## Problem Description

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a **good subarray** or `false` otherwise.

A good subarray is a subarray where:
- Its length is **at least two**, and
- The sum of the elements of the subarray is a multiple of `k`.

**Note:** A subarray is a contiguous part of the array. An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. `0` is always a multiple of `k`.

**Key Concepts:** Array, Hash Table, Math, Prefix Sum

**Typical Constraints:**
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= sum(nums[i]) <= 2^31 - 1`
- `1 <= k <= 2^31 - 1`

**For detailed problem statement, specific constraints, and additional test cases, refer to the [official LeetCode problem](https://leetcode.com/problems/continuous-subarray-sum).**

---

## Examples

### Example 1
**Input:** `nums = [23,2,4,6,7], k = 6`
**Output:** `true`
**Explanation:** `[2, 4]` is a continuous subarray of size 2 whose sum equals 6.

### Example 2
**Input:** `nums = [23,2,6,4,7], k = 6`
**Output:** `true`
**Explanation:** `[23, 2, 6, 4, 7]` is a continuous subarray of size 5 whose sum equals 42. 42 is a multiple of 6.

### Example 3
**Input:** `nums = [23,2,6,4,7], k = 13`
**Output:** `false`
**Explanation:** No valid subarray exists.

### Example 4
**Input:** `nums = [23,2,4,6,6], k = 7`
**Output:** `true`
**Explanation:** `[23, 2, 4, 6, 6]` sums to 41, which is not a multiple of 7, but `[2,4]` sums to 6, and then continuing `[2,4,6,6]` sums to 18, which is not a multiple of 7. However, `[23,2,4]` sums to 29, and `[4,6,6]` sums to 16. But wait, let me recalculate: we need at least 2 elements. `[6,6]` = 12, which is not divisible by 7. But `[2,4]` = 6, not divisible by 7. Actually `[23, 2, 4, 6]` = 35 = 5*7, so this is true!

---

## Optimal Solution

### Implementation

```python
def checkSubarraySum(nums: List[int], k: int) -> bool:
    """
    Use prefix sum with modulo k and hash table to track remainders.

    Key insight: If two prefix sums have the same remainder when divided by k,
    then the subarray between them has a sum that's a multiple of k.

    Time: O(n), Space: O(min(n, k))
    """
    # Store remainder -> earliest index where this remainder appears
    remainder_map = {0: -1}  # Initialize with 0 to handle subarrays from start
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum += num

        # Calculate remainder
        remainder = prefix_sum % k

        # Check if we've seen this remainder before
        if remainder in remainder_map:
            # Check if the subarray length is at least 2
            if i - remainder_map[remainder] >= 2:
                return True
        else:
            # Store the first occurrence of this remainder
            remainder_map[remainder] = i

    return False
```

### Complexity Analysis

**Time: O(n)** - Single pass through array with O(1) hash map operations
**Space: O(min(n, k))** - Hash map stores at most min(n, k) unique remainders

**Why This is Optimal:**
- Achieves linear time complexity using prefix sum technique
- Hash map allows O(1) lookup for previously seen remainders
- Only stores first occurrence of each remainder (greedy approach for longest subarray)
- Handles edge cases: k=1 (always true if length >= 2), remainder 0, single element
- The key insight: `(prefix_sum[j] - prefix_sum[i]) % k == 0` is equivalent to `prefix_sum[j] % k == prefix_sum[i] % k`

### Key Insights

1. **Prefix Sum Modulo:** If two prefix sums have the same remainder mod k, the elements between them sum to a multiple of k
2. **Hash Map for O(1) Lookup:** Store remainder -> index to quickly check if we've seen this remainder before
3. **Index Difference >= 2:** Ensures subarray length requirement
4. **Initialize with {0: -1}:** Handles cases where prefix sum from start is divisible by k

---

## Categories & Tags

**Primary Topics:** Array, Hash Table, Math, Prefix Sum

**Difficulty Level:** MEDIUM

**Problem Type:** Subarray Sum with Modulo Constraint

---

*Problem source: [LeetCode](https://leetcode.com/problems/continuous-subarray-sum)*
