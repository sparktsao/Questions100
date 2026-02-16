# 090. Frequency of the Most Frequent Element

**Difficulty:** MEDIUM
**Frequency:** 32.0%
**Acceptance Rate:** 44.1%
**LeetCode Link:** [Frequency of the Most Frequent Element](https://leetcode.com/problems/frequency-of-the-most-frequent-element)

---

## Problem Description

The frequency of an element is the number of times it occurs in an array.

You are given an integer array `nums` and an integer `k`. In one operation, you can choose an index of `nums` and increment the element at that index by `1`.

Return the maximum possible frequency of an element after performing at most `k` operations.

**Constraints:**
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
- 1 <= k <= 10^5

---

## Examples

### Example 1
**Input:** `nums = [1,2,4], k = 5`
**Output:** `3`
**Explanation:** Increment the first element three times and the second element two times to make nums = [4,4,4]. 4 has a frequency of 3.

### Example 2
**Input:** `nums = [1,4,8,13], k = 5`
**Output:** `2`
**Explanation:** There are multiple ways to achieve maximum frequency 2

### Example 3
**Input:** `nums = [3,9,6], k = 2`
**Output:** `1`
**Explanation:** We can't make any two elements equal with k = 2

### Example 4
**Input:** `nums = [1,1,1,1], k = 0`
**Output:** `4`
**Explanation:** All elements are already equal

---

## Optimal Solution

### Implementation

```python
def maxFrequency(nums: List[int], k: int) -> int:
    """
    Find max frequency using sorting and sliding window.

    Time: O(n log n), Space: O(1)
    """
    # Sort array to group similar values
    nums.sort()

    left = 0
    max_freq = 1
    total = 0  # Sum of elements in current window

    # Sliding window
    for right in range(len(nums)):
        total += nums[right]

        # Cost to make all elements in window equal to nums[right]
        # = nums[right] * window_size - sum_of_window
        while nums[right] * (right - left + 1) - total > k:
            # Window invalid, shrink from left
            total -= nums[left]
            left += 1

        # Update max frequency
        max_freq = max(max_freq, right - left + 1)

    return max_freq
```

### Alternative Implementation with Prefix Sum

```python
def maxFrequency(nums: List[int], k: int) -> int:
    """
    Sliding window with explicit cost calculation.

    Time: O(n log n), Space: O(1)
    """
    nums.sort()
    max_freq = 1
    left = 0
    operations_used = 0

    for right in range(1, len(nums)):
        # Operations needed to increase all elements to nums[right]
        operations_needed = nums[right] - nums[right - 1]
        window_size = right - left
        operations_used += operations_needed * window_size

        # Shrink window if operations exceed k
        while operations_used > k:
            operations_used -= (nums[right] - nums[left])
            left += 1

        max_freq = max(max_freq, right - left + 1)

    return max_freq
```

### Complexity Analysis

**Time: O(n log n) - dominated by sorting. Space: O(1) - constant extra space**

**Why This is Optimal:**
- Sorting enables greedy selection of consecutive elements
- Sliding window finds maximum valid window in linear time after sorting
- Cost calculation is O(1) per window adjustment
- No need for complex data structures
- Handles all edge cases efficiently

---

## Categories & Tags

**Primary Topics:** Array, Binary Search, Greedy, Sliding Window, Sorting, Prefix Sum

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/frequency-of-the-most-frequent-element)*
