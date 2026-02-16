# 015. Top K Frequent Elements

**Difficulty:** MEDIUM
**Frequency:** 77.9%
**Acceptance Rate:** 64.6%
**LeetCode Link:** [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements)

---

## Problem Description

Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. You may return the answer in any order.

**Constraints:**
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array]
- It is guaranteed that the answer is unique

**Follow-up:** Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

---

## Examples

### Example 1
**Input:** `nums = [1,1,1,2,2,3], k = 2`
**Output:** `[1,2]`
**Explanation:** Element 1 appears 3 times, element 2 appears 2 times, element 3 appears 1 time. The 2 most frequent are 1 and 2.

### Example 2
**Input:** `nums = [1], k = 1`
**Output:** `[1]`
**Explanation:** Only one element exists, so it's the most frequent

### Example 3
**Input:** `nums = [1,2,1,2,1,2,3,1,3,2], k = 2`
**Output:** `[1,2]`
**Explanation:** Both 1 and 2 appear 4 times each, making them the most frequent. Element 3 appears only 2 times.

### Example 4
**Input:** `nums = [4,1,-1,2,-1,2,3], k = 2`
**Output:** `[-1,2]`
**Explanation:** Elements -1 and 2 each appear 2 times, making them the most frequent (works with negative numbers)

---

## Optimal Solution

### Implementation (Bucket Sort - O(n) Time)

```python
from typing import List
from collections import Counter

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements using bucket sort.

    Time: O(n), Space: O(n)
    """
    # Count frequency of each element
    count = Counter(nums)

    # Create buckets where index represents frequency
    # bucket[i] contains all elements with frequency i
    bucket = [[] for _ in range(len(nums) + 1)]

    for num, freq in count.items():
        bucket[freq].append(num)

    # Collect k most frequent elements from highest frequency buckets
    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result

    return result
```

### Alternative Implementation (Min Heap - O(n log k) Time)

```python
from typing import List
from collections import Counter
import heapq

def topKFrequent(nums: List[int], k: int) -> List[int]:
    """
    Find k most frequent elements using min heap.

    Time: O(n log k), Space: O(n)
    """
    # Count frequency of each element
    count = Counter(nums)

    # Use min heap to keep top k frequent elements
    # Heap stores tuples of (frequency, number)
    return heapq.nlargest(k, count.keys(), key=count.get)
```

### Complexity Analysis

**Bucket Sort: Time O(n), Space O(n) - optimal for this problem**
**Min Heap: Time O(n log k), Space O(n) - better when k is small**

**Why Bucket Sort is Optimal:**
- Achieves O(n) time complexity, which is optimal for this problem
- Leverages the fact that maximum frequency cannot exceed n
- No sorting required, just bucket indexing
- Handles all edge cases including single element and all duplicates
- Meets the follow-up requirement of being better than O(n log n)

---

## Categories & Tags

**Primary Topics:** Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/top-k-frequent-elements)
