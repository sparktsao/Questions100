# 006. Kth Largest Element in an Array

**Difficulty:** MEDIUM
**Frequency:** 86.9%
**Acceptance Rate:** 68.0%
**LeetCode Link:** [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array)

---

## Problem Description

Given an integer array `nums` and an integer `k`, return the `kth` largest element in the array.

Note that it is the `kth` largest element in the sorted order, not the `kth` distinct element.

Can you solve it without sorting?

**Constraints:**
- 1 <= k <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4

---

## Examples

### Example 1
**Input:** `nums = [3,2,1,5,6,4], k = 2`
**Output:** `5`
**Explanation:** Sorted: [1,2,3,4,5,6], 2nd largest is 5

### Example 2
**Input:** `nums = [3,2,3,1,2,4,5,5,6], k = 4`
**Output:** `4`
**Explanation:** Sorted: [1,2,2,3,3,4,5,5,6], 4th largest is 4

### Example 3
**Input:** `nums = [1], k = 1`
**Output:** `1`
**Explanation:** Single element

### Example 4
**Input:** `nums = [2,1], k = 1`
**Output:** `2`
**Explanation:** Largest of two elements

---

## Optimal Solution

### Implementation

```python
def findKthLargest(nums: List[int], k: int) -> int:
    """
    Use min heap of size k for optimal solution.

    Time: O(n log k), Space: O(k)
    """
    import heapq
    # Maintain min heap of k largest elements
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heapreplace(heap, num)

    return heap[0]
```

### Complexity Analysis

**Time: O(n log k) - heap operations. Space: O(k) - heap storage**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/kth-largest-element-in-an-array)
