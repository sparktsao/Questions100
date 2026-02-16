# 033. Merge Sorted Array

**Difficulty:** EASY
**Frequency:** 67.4%
**Acceptance Rate:** 52.9%
**LeetCode Link:** [Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array)

---

## Problem Description

You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in nums1 and nums2 respectively.

Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. `nums2` has a length of n.

**Constraints:**
- nums1.length == m + n
- nums2.length == n
- 0 <= m, n <= 200
- 1 <= m + n <= 200
- -10^9 <= nums1[i], nums2[j] <= 10^9

---

## Examples

### Example 1
**Input:** `nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3`
**Output:** `[1,2,2,3,5,6]`
**Explanation:** The arrays we are merging are [1,2,3] and [2,5,6]. Result is [1,2,2,3,5,6]

### Example 2
**Input:** `nums1 = [1], m = 1, nums2 = [], n = 0`
**Output:** `[1]`
**Explanation:** The arrays we are merging are [1] and []. Result is [1]

### Example 3
**Input:** `nums1 = [0], m = 0, nums2 = [1], n = 1`
**Output:** `[1]`
**Explanation:** The arrays we are merging are [] and [1]. Result is [1]

### Example 4
**Input:** `nums1 = [4,5,6,0,0,0], m = 3, nums2 = [1,2,3], n = 3`
**Output:** `[1,2,3,4,5,6]`
**Explanation:** Merge [4,5,6] and [1,2,3] into [1,2,3,4,5,6]

---

## Optimal Solution

### Implementation

```python
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Merge two sorted arrays using three-pointer approach from end.

    Time: O(m + n), Space: O(1)
    """
    # Start from the end of both arrays
    p1 = m - 1  # Pointer for nums1's actual elements
    p2 = n - 1  # Pointer for nums2
    p = m + n - 1  # Pointer for final position in nums1

    # Merge from right to left
    while p2 >= 0:
        # If nums1 is exhausted or nums2[p2] is larger
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
```

### Alternative Implementation

```python
def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Simplified version with explicit condition.

    Time: O(m + n), Space: O(1)
    """
    p1, p2, p = m - 1, n - 1, m + n - 1

    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # Copy remaining elements from nums2 if any
    nums1[:p2 + 1] = nums2[:p2 + 1]
```

### Complexity Analysis

**Time: O(m + n) - single pass through both arrays. Space: O(1) - in-place merge**

**Why This is Optimal:**
- Avoids shifting elements by filling from the end
- No extra space required beyond input arrays
- Single pass through both arrays
- Handles all edge cases including empty arrays

---

## Categories & Tags

**Primary Topics:** Array, Two Pointers, Sorting

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/merge-sorted-array)*
