# 088. Interval List Intersections

**Difficulty:** MEDIUM
**Frequency:** 32.0%
**Acceptance Rate:** 72.7%
**LeetCode Link:** [Interval List Intersections](https://leetcode.com/problems/interval-list-intersections)

---

## Problem Description

You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [starti, endi]` and `secondList[j] = [startj, endj]`. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval `[a, b]` (with `a <= b`) denotes the set of real numbers `x` with `a <= x <= b`.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of `[1, 3]` and `[2, 4]` is `[2, 3]`.

**Constraints:**
- 0 <= firstList.length, secondList.length <= 1000
- firstList.length + secondList.length >= 1
- 0 <= starti < endi <= 10^9
- endi < starti+1
- 0 <= startj < endj <= 10^9
- endj < startj+1

---

## Examples

### Example 1
**Input:** `firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]`
**Output:** `[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]`
**Explanation:** Multiple overlapping intervals

### Example 2
**Input:** `firstList = [[1,3],[5,9]], secondList = []`
**Output:** `[]`
**Explanation:** One list is empty

### Example 3
**Input:** `firstList = [[1,7]], secondList = [[3,10]]`
**Output:** `[[3,7]]`
**Explanation:** Single interval intersection

### Example 4
**Input:** `firstList = [[1,2],[3,4]], secondList = [[5,6],[7,8]]`
**Output:** `[]`
**Explanation:** No overlapping intervals

---

## Optimal Solution

### Implementation

```python
def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    """
    Find all interval intersections using two pointers.

    Time: O(m + n), Space: O(1) excluding output
    """
    result = []
    i, j = 0, 0

    while i < len(firstList) and j < len(secondList):
        # Get current intervals
        start1, end1 = firstList[i]
        start2, end2 = secondList[j]

        # Calculate intersection
        # Intersection exists if intervals overlap
        intersection_start = max(start1, start2)
        intersection_end = min(end1, end2)

        # Check if valid intersection
        if intersection_start <= intersection_end:
            result.append([intersection_start, intersection_end])

        # Move pointer for interval that ends first
        if end1 < end2:
            i += 1
        else:
            j += 1

    return result
```

### Alternative Implementation (More Explicit)

```python
def intervalIntersection(firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
    """
    Two pointer approach with explicit overlap check.

    Time: O(m + n), Space: O(1)
    """
    result = []
    i, j = 0, 0
    m, n = len(firstList), len(secondList)

    while i < m and j < n:
        a_start, a_end = firstList[i]
        b_start, b_end = secondList[j]

        # Check if intervals overlap
        # Two intervals [a_start, a_end] and [b_start, b_end] overlap if:
        # a_start <= b_end AND b_start <= a_end
        if a_start <= b_end and b_start <= a_end:
            # Add intersection
            result.append([max(a_start, b_start), min(a_end, b_end)])

        # Advance the pointer of interval that ends earlier
        if a_end < b_end:
            i += 1
        else:
            j += 1

    return result
```

### Complexity Analysis

**Time: O(m + n) - single pass through both lists. Space: O(1) - constant extra space (output not counted)**

**Why This is Optimal:**
- Each interval visited exactly once (two pointer technique)
- No sorting needed (lists already sorted)
- Minimal space overhead
- Handles all edge cases: empty lists, no overlaps, complete overlaps
- Linear time is optimal since we must examine all intervals

---

## Categories & Tags

**Primary Topics:** Array, Two Pointers, Line Sweep

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/interval-list-intersections)*
