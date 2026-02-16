# 074. Cutting Ribbons

**Difficulty:** MEDIUM
**Frequency:** 40.7%
**Acceptance Rate:** 52.6%
**LeetCode Link:** [Cutting Ribbons](https://leetcode.com/problems/cutting-ribbons)

---

## Problem Description

You are given an integer array `ribbons`, where `ribbons[i]` represents the length of the `i-th` ribbon, and an integer `k`. You may cut any of the ribbons into any number of segments of positive integer lengths, or perform no cuts at all.

Your goal is to obtain `k` ribbons of all the same positive integer length. You are allowed to throw away any excess ribbon as a result of cutting.

Return the maximum possible positive integer length that you can obtain `k` ribbons of, or `0` if you cannot obtain `k` ribbons of the same length.

**Note:** For example, if you have a ribbon of length 4, you can:
- Keep the ribbon of length 4
- Cut it into one ribbon of length 3 and one ribbon of length 1
- Cut it into two ribbons of length 2
- Cut it into one ribbon of length 2 and two ribbons of length 1
- Cut it into four ribbons of length 1

**Constraints:**
- `1 <= ribbons.length <= 10^5`
- `1 <= ribbons[i] <= 10^5`
- `1 <= k <= 10^9`

---

## Examples

### Example 1
**Input:** `ribbons = [9,7,5], k = 3`
**Output:** `5`
**Explanation:** Cut the first ribbon to two ribbons, one of length 5 and one of length 4. Cut the second ribbon to two ribbons, one of length 5 and one of length 2. Keep the third ribbon as it is. Now you have 3 ribbons of length 5.

### Example 2
**Input:** `ribbons = [7,5,9], k = 4`
**Output:** `4`
**Explanation:** Cut the first ribbon to two ribbons, one of length 4 and one of length 3. Cut the second ribbon to two ribbons, one of length 4 and one of length 1. Cut the third ribbon to three ribbons, two of length 4 and one of length 1. Now you have 4 ribbons of length 4.

### Example 3
**Input:** `ribbons = [5,7,9], k = 22`
**Output:** `0`
**Explanation:** You cannot obtain k ribbons of the same positive integer length.

### Example 4
**Input:** `ribbons = [1,2,3,4,9], k = 5`
**Output:** `3`
**Explanation:** Cut to get ribbons of length 3: [1], [2], [3], [4], [9→3,3,3]. Total of 5 ribbons of length 3.

---

## Optimal Solution

### Implementation

```python
def maxLength(ribbons: List[int], k: int) -> int:
    """
    Binary search on answer to find maximum ribbon length.

    Time: O(n log max_len), Space: O(1)
    """
    def can_cut(length):
        """Check if we can get k ribbons of given length."""
        count = 0
        for ribbon in ribbons:
            count += ribbon // length
            if count >= k:  # Early termination
                return True
        return count >= k

    # Binary search bounds
    left = 1
    right = max(ribbons)
    result = 0

    while left <= right:
        mid = left + (right - left) // 2

        if can_cut(mid):
            # Can achieve this length, try larger
            result = mid
            left = mid + 1
        else:
            # Cannot achieve, try smaller
            right = mid - 1

    return result
```

### Complexity Analysis

**Time: O(n log m) - where n is ribbons count and m is max ribbon length. Space: O(1) - constant space**

**Why This is Optimal:**
- Binary search on the answer space reduces search from O(max_len) to O(log max_len)
- For each candidate length, we verify in O(n) by counting achievable ribbons
- Monotonic property: if length x works, all lengths < x also work
- Early termination in counting function optimizes average case
- Cannot do better than O(n) per check since we must examine all ribbons

---

## Categories & Tags

**Primary Topics:** Array, Binary Search

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/cutting-ribbons)*
