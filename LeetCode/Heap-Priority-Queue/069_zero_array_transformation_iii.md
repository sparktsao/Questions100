# 069. Zero Array Transformation III

**Difficulty:** MEDIUM
**Frequency:** 40.7%
**Acceptance Rate:** 55.4%
**LeetCode Link:** [Zero Array Transformation III](https://leetcode.com/problems/zero-array-transformation-iii)

---

## Problem Description

You are given an integer array `nums` of length `n` and a 2D array `queries` where `queries[i] = [li, ri]`.

For each query, you can perform the following operation:
- Decrement the value at each index in the range `[li, ri]` in `nums` by at most 1.
- The amount by which each value is decremented can be chosen independently for each index.

A Zero Array is an array with all its elements equal to 0.

Return the maximum number of elements that can be removed from `queries`, such that `nums` can still be converted to a zero array using the remaining queries. If it is not possible to convert `nums` to a zero array, return -1.

**Constraints:**
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
- 1 <= queries.length <= 10^5
- queries[i].length == 2
- 0 <= li <= ri < nums.length

---

## Examples

### Example 1
**Input:** `nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]`
**Output:** `1`
**Explanation:**
- After removing queries[2] (which is [1,1]), we still have [[0,2],[0,2]]
- Using query [0,2] twice, we can decrement each position by up to 2
- This is sufficient to zero out [2,0,2]
- Maximum removals: 1

### Example 2
**Input:** `nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]`
**Output:** `2`
**Explanation:**
- We can remove 2 queries and still convert nums to zero array
- For example, removing queries[2] and queries[3] leaves [[1,3],[0,2]]
- These remaining queries can cover all positions

### Example 3
**Input:** `nums = [1,2,3,4], queries = [[0,3]]`
**Output:** `-1`
**Explanation:**
- nums cannot be converted to zero array even using all queries
- We need at least 4 decrements at index 3, but only have 1 query covering it
- Return -1 since transformation is impossible

### Example 4
**Input:** `nums = [0,0,0], queries = [[0,2]]`
**Output:** `1`
**Explanation:**
- nums is already a zero array
- We can remove all queries, maximum removal is 1

---

## Optimal Solution

### Key Insight

The key insight is we don't need to track which specific queries we use - we only need to know the **maximum number of queries needed simultaneously** at any position. This maximum represents the minimum queries we must use. Therefore, maximum removals = total queries - maximum simultaneously needed.

### Algorithm Logic

For each position `idx` in `nums`:
1. **Add queries to active pool**: Include all queries starting at or before `idx`
2. **Remove expired queries**: Remove queries that end before `idx`
3. **Check if coverage is possible**: If active queries < `nums[idx]`, impossible → return -1
4. **Track maximum usage**: Record the maximum number of queries needed at any single position
5. **Return result**: `len(queries) - max_used`

### Implementation

```python
import heapq

def maxRemoval(nums, queries):
    """
    Cleaner approach: track maximum simultaneous query usage.

    Time: O(n log q + q log q), Space: O(q)
    """
    n = len(nums)
    queries.sort()  # Sort by start position

    active = []  # Max heap of query end positions (store negative for max heap)
    used = 0     # Maximum queries used simultaneously
    i = 0        # Query index

    for idx in range(n):
        # Step 1: Add all queries starting at or before idx
        while i < len(queries) and queries[i][0] <= idx:
            heapq.heappush(active, -queries[i][1])  # Negative for max heap
            i += 1

        # Step 2: Remove expired queries (those ending before idx)
        while active and -active[0] < idx:
            heapq.heappop(active)

        # Step 3: Check if we have enough active queries
        if len(active) < nums[idx]:
            return -1  # Not enough queries to cover position idx

        # Step 4: Track maximum simultaneous usage
        used = max(used, nums[idx])

    # Step 5: Maximum removals = total - minimum we must use
    return len(queries) - used
```

### Complexity Analysis

**Time: O(n log q + q log q)**
- Sorting queries: O(q log q)
- Processing each position: O(n)
- Heap operations: Each query pushed/popped at most once: O(q log q)
- Total: O(n log q + q log q)

**Space: O(q)** - Max heap of queries

### Why This Approach Works

**Greedy Insight:** At each position, we only care about having enough queries available, not which specific queries we use.

**Key Observations:**
1. If at any position we don't have enough active queries → impossible
2. The position requiring the most simultaneous queries determines minimum usage
3. Maximum removals = Total queries - Minimum required usage

**Example Walkthrough:**
```
nums = [2, 0, 2], queries = [[0,2], [0,2], [1,1]]

idx=0: active=[[0,2], [0,2]], need=2, used=max(0,2)=2
idx=1: active=[[0,2], [0,2], [1,1]], need=0, used=max(2,0)=2
idx=2: active=[[0,2], [0,2]], need=2, used=max(2,2)=2

Result: 3 - 2 = 1 (can remove 1 query)
```

---

## Categories & Tags

**Primary Topics:** Array, Greedy, Sorting, Heap (Priority Queue), Prefix Sum

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/zero-array-transformation-iii)*
