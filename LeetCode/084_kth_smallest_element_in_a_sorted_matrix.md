# 084. Kth Smallest Element in a Sorted Matrix

**Difficulty:** MEDIUM
**Frequency:** 40.7%
**Acceptance Rate:** 63.6%
**LeetCode Link:** [Kth Smallest Element in a Sorted Matrix](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix)

---

## Problem Description

Given an `n x n` matrix where each of the rows and columns is sorted in ascending order, return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

You must find a solution with a memory complexity better than O(n²).

**Constraints:**
- n == matrix.length == matrix[i].length
- 1 <= n <= 300
- -10^9 <= matrix[i][j] <= 10^9
- All the rows and columns of matrix are guaranteed to be sorted in non-decreasing order
- 1 <= k <= n²

---

## Examples

### Example 1
**Input:** `matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8`
**Output:** `13`
**Explanation:** The elements in the matrix are [1,5,9,10,11,12,13,13,15], and the 8th smallest number is 13

### Example 2
**Input:** `matrix = [[-5]], k = 1`
**Output:** `-5`
**Explanation:** Single element matrix

### Example 3
**Input:** `matrix = [[1,2],[1,3]], k = 2`
**Output:** `1`
**Explanation:** Duplicate elements are counted separately

### Example 4
**Input:** `matrix = [[1,3,5],[6,7,12],[11,14,14]], k = 6`
**Output:** `11`
**Explanation:** Sorted order is [1,3,5,6,7,11,12,14,14], 6th element is 11

---

## Optimal Solution

### Implementation (Binary Search)

```python
def kthSmallest(matrix: List[List[int]], k: int) -> int:
    """
    Find kth smallest element using binary search on value range.

    Time: O(n log(max-min)), Space: O(1)
    """
    n = len(matrix)
    left, right = matrix[0][0], matrix[n-1][n-1]

    def count_less_equal(mid):
        """Count elements <= mid in sorted matrix"""
        count = 0
        # Start from bottom-left corner
        row, col = n - 1, 0

        while row >= 0 and col < n:
            if matrix[row][col] <= mid:
                # All elements in this column up to row are <= mid
                count += row + 1
                col += 1
            else:
                row -= 1

        return count

    # Binary search on value range
    while left < right:
        mid = left + (right - left) // 2

        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid

    return left
```

### Alternative Implementation (Min Heap)

```python
import heapq

def kthSmallest(matrix: List[List[int]], k: int) -> int:
    """
    Find kth smallest using min heap.

    Time: O(k log n), Space: O(n)
    """
    n = len(matrix)
    # Min heap: (value, row, col)
    min_heap = []

    # Add first element from each row
    for r in range(min(n, k)):
        heapq.heappush(min_heap, (matrix[r][0], r, 0))

    # Extract min k times
    result = 0
    for _ in range(k):
        result, r, c = heapq.heappop(min_heap)

        # Add next element from same row if available
        if c + 1 < n:
            heapq.heappush(min_heap, (matrix[r][c + 1], r, c + 1))

    return result
```

### Complexity Analysis

**Binary Search Approach:**
**Time: O(n log(max-min)) - binary search on range with O(n) counting. Space: O(1) - constant space**

**Min Heap Approach:**
**Time: O(k log n) - k heap operations. Space: O(n) - heap storage**

**Why This is Optimal:**
- Binary search achieves O(1) space, meeting the constraint
- Min heap is more efficient when k is small
- Both avoid sorting entire matrix (O(n² log n²))
- Leverage sorted property of rows and columns
- Handle duplicates correctly

---

## Categories & Tags

**Primary Topics:** Array, Binary Search, Sorting, Heap (Priority Queue), Matrix

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix)*
