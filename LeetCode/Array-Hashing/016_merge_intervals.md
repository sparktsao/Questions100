# 016. Merge Intervals

**Difficulty:** MEDIUM
**Frequency:** 77.9%
**Acceptance Rate:** 49.4%
**LeetCode Link:** [Merge Intervals](https://leetcode.com/problems/merge-intervals)

---

## Problem Description

Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

**Constraints:**
- 1 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i <= end_i <= 10^4

---

## Examples

### Example 1
**Input:** `intervals = [[1,3],[2,6],[8,10],[15,18]]`
**Output:** `[[1,6],[8,10],[15,18]]`
**Explanation:** [1,3] and [2,6] overlap, merge to [1,6]

### Example 2
**Input:** `intervals = [[1,4],[4,5]]`
**Output:** `[[1,5]]`
**Explanation:** Intervals touching at boundaries should merge

### Example 3
**Input:** `intervals = [[1,4],[0,4]]`
**Output:** `[[0,4]]`
**Explanation:** Unsorted input, [0,4] encompasses [1,4]

### Example 4
**Input:** `intervals = [[1,4],[2,3]]`
**Output:** `[[1,4]]`
**Explanation:** One interval completely inside another

---

## Optimal Solution

### Implementation

```python
def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals.

    Time: O(n log n), Space: O(n)
    """
    if not intervals:
        return []

    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            # Overlapping, merge
            last[1] = max(last[1], current[1])
        else:
            # Non-overlapping, add
            merged.append(current)

    return merged
```

### Complexity Analysis

**Time: O(n log n) - sorting. Space: O(n) - output array**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Array, Sorting

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/merge-intervals)
