# 100. Median of Two Sorted Arrays

**Difficulty:** HARD
**Frequency:** 32.0%
**Acceptance Rate:** 43.8%
**LeetCode Link:** [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays)

---

## Problem Description

Given two sorted arrays `nums1` and `nums2` of size `m` and `n` respectively, return **the median** of the two sorted arrays.

The overall run time complexity should be **O(log (m+n))**.

**Constraints:**
- nums1.length == m
- nums2.length == n
- 0 <= m <= 1000
- 0 <= n <= 1000
- 1 <= m + n <= 2000
- -10^6 <= nums1[i], nums2[i] <= 10^6

---

## Examples

### Example 1
**Input:** `nums1 = [1,3], nums2 = [2]`
**Output:** `2.00000`
**Explanation:** Merged array = [1,2,3] and median is 2

### Example 2
**Input:** `nums1 = [1,2], nums2 = [3,4]`
**Output:** `2.50000`
**Explanation:** Merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5

### Example 3
**Input:** `nums1 = [], nums2 = [1]`
**Output:** `1.00000`
**Explanation:** One array is empty, median is the single element

### Example 4
**Input:** `nums1 = [2], nums2 = []`
**Output:** `2.00000`
**Explanation:** One array is empty, median is the single element from the other array

---

## Optimal Solution

### Implementation (Binary Search on Partition)

```python
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Binary search on partition point to find median in O(log(min(m,n))).

    Time: O(log(min(m,n))), Space: O(1)
    """
    # Ensure nums1 is the smaller array for binary search optimization
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    left, right = 0, m

    while left <= right:
        # Partition nums1 at i, nums2 at j
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1

        # Handle edge cases where partition is at the boundary
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]

        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]

        # Check if we found the correct partition
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # We found the correct partition
            if (m + n) % 2 == 0:
                # Even total length - median is average of two middle elements
                return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
            else:
                # Odd total length - median is the max of left partition
                return max(maxLeft1, maxLeft2)
        elif maxLeft1 > minRight2:
            # nums1 partition is too far right, move left
            right = partition1 - 1
        else:
            # nums1 partition is too far left, move right
            left = partition1 + 1

    raise ValueError("Input arrays are not sorted")
```

### Alternative Implementation (Simple Merge - Not Optimal)

```python
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Merge both arrays and find median.

    Time: O(m+n), Space: O(m+n) - NOT optimal but easier to understand
    """
    # Merge two sorted arrays
    merged = []
    i, j = 0, 0

    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Add remaining elements
    merged.extend(nums1[i:])
    merged.extend(nums2[j:])

    # Find median
    n = len(merged)
    if n % 2 == 0:
        return (merged[n//2 - 1] + merged[n//2]) / 2
    else:
        return merged[n//2]
```

### Complexity Analysis

**Time: O(log(min(m,n))) - binary search on smaller array. Space: O(1) - constant space**

**Why This is Optimal:**
- Achieves required O(log(m+n)) time complexity using binary search
- Searching on smaller array minimizes search space
- Partition-based approach avoids merging arrays entirely
- O(1) space is optimal - no auxiliary data structures needed
- Elegantly handles odd/even total length and edge cases

---

## Categories & Tags

**Primary Topics:** Array, Binary Search, Divide and Conquer

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/median-of-two-sorted-arrays)*
