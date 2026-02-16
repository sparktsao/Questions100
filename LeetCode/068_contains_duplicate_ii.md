# 068. Contains Duplicate II

**Difficulty:** EASY
**Frequency:** 40.7%
**Acceptance Rate:** 49.0%
**LeetCode Link:** [Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii)

---

## Problem Description

Given an integer array `nums` and an integer `k`, return `true` if there are two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- 0 <= k <= 10^5

---

## Examples

### Example 1
**Input:** `nums = [1,2,3,1], k = 3`
**Output:** `true`
**Explanation:** nums[0] == nums[3] and abs(0 - 3) = 3 <= k

### Example 2
**Input:** `nums = [1,0,1,1], k = 1`
**Output:** `true`
**Explanation:** nums[2] == nums[3] and abs(2 - 3) = 1 <= k

### Example 3
**Input:** `nums = [1,2,3,1,2,3], k = 2`
**Output:** `false`
**Explanation:** No two equal numbers are within distance k of each other

### Example 4
**Input:** `nums = [1,2,1], k = 0`
**Output:** `false`
**Explanation:** k = 0 means indices must be identical, which is impossible for distinct indices

---

## Optimal Solution

### Implementation

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """
    Use hash map to track most recent index of each value.

    Time: O(n), Space: O(min(n, k))
    """
    seen = {}

    for i, num in enumerate(nums):
        # Check if we've seen this number before
        if num in seen:
            # Check if within distance k
            if i - seen[num] <= k:
                return True

        # Update/store the current index for this number
        seen[num] = i

    return False
```

### Alternative Implementation (Sliding Window with Set)

```python
def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    """
    Use sliding window with set to maintain window of size k.

    Time: O(n), Space: O(min(n, k))
    """
    window = set()

    for i, num in enumerate(nums):
        # If number already in window, we found duplicate within k distance
        if num in window:
            return True

        # Add current number to window
        window.add(num)

        # Maintain window size of k
        if len(window) > k:
            # Remove the element that's now outside the window
            window.remove(nums[i - k])

    return False
```

### Complexity Analysis

**Time: O(n) - single pass through array. Space: O(min(n, k)) - hash map/set stores at most k+1 elements**

**Why This is Optimal:**
- Must examine each element at least once, so O(n) is optimal
- Space is bounded by min(n, k) since we only need to track elements within window
- Hash table provides O(1) lookup and insertion
- Sliding window approach maintains only relevant elements
- Early termination when duplicate found

---

## Categories & Tags

**Primary Topics:** Array, Hash Table, Sliding Window

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/contains-duplicate-ii)*
