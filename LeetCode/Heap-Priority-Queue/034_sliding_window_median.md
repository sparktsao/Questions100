# 034. Sliding Window Median

**Difficulty:** HARD
**Frequency:** 65.0%
**Acceptance Rate:** 38.7%
**LeetCode Link:** [Sliding Window Median](https://leetcode.com/problems/sliding-window-median)

---

## Problem Description

The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

You are given an integer array `nums` and an integer `k`. There is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the median array for each window in the original array. Answers within 10^-5 of the actual value will be accepted.

**Constraints:**
- 1 <= k <= nums.length <= 10^5
- -2^31 <= nums[i] <= 2^31 - 1

---

## Examples

### Example 1
**Input:** `nums = [1,3,-1,-3,5,3,6,7], k = 3`
**Output:** `[1.00000,-1.00000,-1.00000,3.00000,5.00000,6.00000]`
**Explanation:** Window [1,3,-1] median is 1, [-1,-3,5] median is -1, etc.

### Example 2
**Input:** `nums = [1,2,3,4,2,3,1,4,2], k = 3`
**Output:** `[2.00000,3.00000,3.00000,3.00000,2.00000,3.00000,2.00000]`
**Explanation:** Each window of size 3 has its median calculated

### Example 3
**Input:** `nums = [1,4,2,3], k = 4`
**Output:** `[2.50000]`
**Explanation:** Single window [1,4,2,3] has median (2+3)/2 = 2.5

### Example 4
**Input:** `nums = [1,3,-1,-3,5,3,6,7], k = 4`
**Output:** `[0.00000,1.00000,1.00000,4.00000,5.50000,6.50000]`
**Explanation:** Even-sized windows return average of two middle values

---

## Optimal Solution

### Implementation

```python
from heapq import heappush, heappop
from collections import defaultdict

def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    """
    Two heaps with lazy deletion for sliding window median.

    Time: O(n log k), Space: O(k)
    """
    # Max heap for smaller half (negate values for max heap behavior)
    small = []
    # Min heap for larger half
    large = []
    # Track elements to be removed (lazy deletion)
    to_remove = defaultdict(int)

    def add_num(num):
        if not small or num <= -small[0]:
            heappush(small, -num)
        else:
            heappush(large, num)

    def remove_num(num):
        to_remove[num] += 1
        if num <= -small[0]:
            balance[0] -= 1
        else:
            balance[0] += 1

    def rebalance():
        # Balance small and large heaps
        if balance[0] < 0:  # small has too few
            heappush(small, -heappop(large))
            balance[0] += 1
        elif balance[0] > 0:  # small has too many
            heappush(large, -heappop(small))
            balance[0] -= 1
        # Clean up tops of heaps
        while small and to_remove[-small[0]] > 0:
            to_remove[-small[0]] -= 1
            heappop(small)
        while large and to_remove[large[0]] > 0:
            to_remove[large[0]] -= 1
            heappop(large)

    def get_median():
        if k % 2 == 1:
            return float(-small[0])
        return (-small[0] + large[0]) / 2.0

    result = []
    balance = [0]  # Track balance: positive means small has more

    # Initialize first window
    for i in range(k):
        add_num(nums[i])

    rebalance()
    result.append(get_median())

    # Slide window
    for i in range(k, len(nums)):
        # Remove outgoing element
        out_num = nums[i - k]
        remove_num(out_num)

        # Add incoming element
        add_num(nums[i])

        rebalance()
        result.append(get_median())

    return result
```

### Alternative Implementation (Simpler but Slower)

```python
def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    """
    Brute force with sorting for each window.

    Time: O(n * k log k), Space: O(k)
    """
    result = []

    for i in range(len(nums) - k + 1):
        window = sorted(nums[i:i + k])
        if k % 2 == 1:
            result.append(float(window[k // 2]))
        else:
            result.append((window[k // 2 - 1] + window[k // 2]) / 2.0)

    return result
```

### Complexity Analysis

**Time: O(n log k) - heap operations for n windows. Space: O(k) - heap storage**

**Why This is Optimal:**
- Two heaps maintain median in O(log k) time per operation
- Lazy deletion avoids expensive heap removal
- Balanced heaps ensure quick median access
- Handles both odd and even window sizes efficiently

---

## Categories & Tags

**Primary Topics:** Array, Hash Table, Sliding Window, Heap (Priority Queue)

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/sliding-window-median)*
