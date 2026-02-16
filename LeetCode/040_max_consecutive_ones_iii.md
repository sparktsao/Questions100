# 040. Max Consecutive Ones III

**Difficulty:** MEDIUM
**Frequency:** 62.4%
**Acceptance Rate:** 65.9%
**LeetCode Link:** [Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii)

---

## Problem Description

Given a binary array `nums` and an integer `k`, return the maximum number of consecutive 1's in the array if you can flip at most `k` 0's.

**Constraints:**
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1
- 0 <= k <= nums.length

---

## Examples

### Example 1
**Input:** `nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2`
**Output:** `6`
**Explanation:** [1,1,1,0,0,**1**,1,1,1,1,**1**] - Bolded numbers were flipped from 0 to 1. Maximum consecutive 1's is 6

### Example 2
**Input:** `nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3`
**Output:** `10`
**Explanation:** [0,0,1,1,**1**,**1**,1,1,1,**1**,1,1,0,0,0,1,1,1,1] - Bolded numbers were flipped from 0 to 1. Maximum consecutive 1's is 10

### Example 3
**Input:** `nums = [1,1,1,1], k = 0`
**Output:** `4`
**Explanation:** No flips needed, all elements are already 1

### Example 4
**Input:** `nums = [0,0,0,0], k = 2`
**Output:** `2`
**Explanation:** Flip any two consecutive 0s to get 2 consecutive 1s

---

## Optimal Solution

### Implementation

```python
def longestOnes(nums: List[int], k: int) -> int:
    """
    Sliding window to find max consecutive 1s with at most k flips.

    Time: O(n), Space: O(1)
    """
    left = 0
    max_len = 0
    zeros_count = 0

    for right in range(len(nums)):
        # Expand window
        if nums[right] == 0:
            zeros_count += 1

        # Contract window if too many zeros
        while zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1

        # Update max length
        max_len = max(max_len, right - left + 1)

    return max_len
```

### Alternative Implementation (Optimized)

```python
def longestOnes(nums: List[int], k: int) -> int:
    """
    Optimized sliding window - never shrink window, only expand or slide.

    Time: O(n), Space: O(1)
    """
    left = 0
    zeros_count = 0

    for right in range(len(nums)):
        # Expand window
        if nums[right] == 0:
            zeros_count += 1

        # Slide window if too many zeros (maintain max window size)
        if zeros_count > k:
            if nums[left] == 0:
                zeros_count -= 1
            left += 1

    # Window size at end is the maximum length found
    return len(nums) - left
```

### Alternative Implementation (Explicit)

```python
def longestOnes(nums: List[int], k: int) -> int:
    """
    More explicit version with clear logic.

    Time: O(n), Space: O(1)
    """
    left = right = 0
    flips_used = 0
    max_consecutive = 0

    while right < len(nums):
        # Try to expand window
        if nums[right] == 0:
            flips_used += 1

        # Contract if we exceeded k flips
        while flips_used > k:
            if nums[left] == 0:
                flips_used -= 1
            left += 1

        # Update maximum
        max_consecutive = max(max_consecutive, right - left + 1)
        right += 1

    return max_consecutive
```

### Complexity Analysis

**Time: O(n) - single pass through array with two pointers. Space: O(1) - constant extra space**

**Why This is Optimal:**
- Each element visited at most twice (once by right, once by left)
- Maintains valid window with at most k zeros
- No extra data structures needed
- Handles all edge cases efficiently

---

## Categories & Tags

**Primary Topics:** Array, Binary Search, Sliding Window, Prefix Sum

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii)*
