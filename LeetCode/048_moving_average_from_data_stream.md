# 048. Moving Average from Data Stream

**Difficulty:** EASY
**Frequency:** 56.0%
**Acceptance Rate:** 79.9%
**LeetCode Link:** [Moving Average from Data Stream](https://leetcode.com/problems/moving-average-from-data-stream)

---

## Problem Description

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Implement the `MovingAverage` class:
- `MovingAverage(int size)` Initializes the object with the size of the window
- `double next(int val)` Returns the moving average of the last `size` values of the stream

**Constraints:**
- 1 <= size <= 1000
- -10^5 <= val <= 10^5
- At most 10^4 calls will be made to next

---

## Examples

### Example 1
**Input:**
```
["MovingAverage", "next", "next", "next", "next"]
[[3], [1], [10], [3], [5]]
```
**Output:**
```
[null, 1.0, 5.5, 4.66667, 6.0]
```
**Explanation:**
```
MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1); // return 1.0 = 1 / 1
movingAverage.next(10); // return 5.5 = (1 + 10) / 2
movingAverage.next(3); // return 4.66667 = (1 + 10 + 3) / 3
movingAverage.next(5); // return 6.0 = (10 + 3 + 5) / 3
```

### Example 2
**Input:**
```
["MovingAverage", "next", "next"]
[[1], [5], [10]]
```
**Output:**
```
[null, 5.0, 10.0]
```
**Explanation:** Window size 1, so each next() returns the current value

### Example 3
**Input:**
```
["MovingAverage", "next", "next", "next", "next", "next"]
[[2], [1], [2], [3], [4], [5]]
```
**Output:**
```
[null, 1.0, 1.5, 2.5, 3.5, 4.5]
```
**Explanation:** Window size 2, sliding window averages

---

## Optimal Solution

### Implementation

```python
from collections import deque

class MovingAverage:
    """
    Moving average using queue and running sum.

    Time: O(1) per operation, Space: O(size)
    """

    def __init__(self, size: int):
        """Initialize with window size"""
        self.size = size
        self.queue = deque()
        self.window_sum = 0

    def next(self, val: int) -> float:
        """Add new value and return current average"""
        # Add new value
        self.queue.append(val)
        self.window_sum += val

        # Remove oldest value if window is full
        if len(self.queue) > self.size:
            self.window_sum -= self.queue.popleft()

        # Return average
        return self.window_sum / len(self.queue)
```

### Alternative Implementation Using Circular Buffer

```python
class MovingAverage:
    """
    Moving average using circular buffer (array).

    Time: O(1) per operation, Space: O(size)
    """

    def __init__(self, size: int):
        """Initialize with fixed-size circular buffer"""
        self.size = size
        self.buffer = [0] * size
        self.count = 0
        self.index = 0
        self.window_sum = 0

    def next(self, val: int) -> float:
        """Add new value and return current average"""
        # Remove old value at current index
        self.window_sum -= self.buffer[self.index]

        # Add new value
        self.buffer[self.index] = val
        self.window_sum += val

        # Move to next position (circular)
        self.index = (self.index + 1) % self.size
        self.count = min(self.count + 1, self.size)

        # Return average
        return self.window_sum / self.count
```

### Naive Implementation (For Comparison)

```python
class MovingAverage:
    """
    Naive implementation recalculating sum each time.

    Time: O(size) per operation, Space: O(size)
    """

    def __init__(self, size: int):
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        self.queue.append(val)
        if len(self.queue) > self.size:
            self.queue.pop(0)
        return sum(self.queue) / len(self.queue)
```

### Complexity Analysis

**Time: O(1) per next() call. Space: O(size) - window storage**

**Why This is Optimal:**
- Maintaining running sum avoids recalculating on each call
- Deque provides O(1) append and popleft operations
- Space usage is bounded by window size
- Each operation is constant time regardless of window size

---

## Categories & Tags

**Primary Topics:** Array, Design, Queue, Data Stream

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/moving-average-from-data-stream)*
