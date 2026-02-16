# 082. Find Median from Data Stream

**Difficulty:** HARD
**Frequency:** 40.7%
**Acceptance Rate:** 53.3%
**LeetCode Link:** [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream)

---

## Problem Description

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

Implement the MedianFinder class:

- `MedianFinder()` initializes the object
- `void addNum(int num)` adds the integer `num` from the data stream
- `double findMedian()` returns the median of all elements so far

**Constraints:**
- -10^5 <= num <= 10^5
- There will be at least one element before calling findMedian
- At most 5 * 10^4 calls to addNum and findMedian

---

## Examples

### Example 1
**Input:** `["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]\n[[], [1], [2], [], [3], []]`
**Output:** `[null, null, null, 1.5, null, 2.0]`
**Explanation:** After adding 1,2: median=1.5. After adding 3: median=2.0

### Example 2
**Input:** `addNum(1), addNum(3), addNum(2), findMedian()`
**Output:** `2.0`
**Explanation:** Sorted: [1,2,3], median is 2

### Example 3
**Input:** `addNum(5), findMedian()`
**Output:** `5.0`
**Explanation:** Single element median

---

## Optimal Solution

### Implementation

```python
class MedianFinder:
    def __init__(self):
        """
        Two heaps: max heap for lower half, min heap for upper half.

        Time: O(log n) add, O(1) find. Space: O(n)
        """
        import heapq
        self.small = []  # max heap (invert values)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        # Add to max heap (small)
        heapq.heappush(self.small, -num)

        # Balance: move largest from small to large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Maintain size property (small can have at most 1 more)
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
```

### Complexity Analysis

**Time: O(log n) for addNum, O(1) for findMedian. Space: O(n) - two heaps**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Two Pointers, Design, Sorting, Heap (Priority Queue), Data Stream

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/find-median-from-data-stream)*
