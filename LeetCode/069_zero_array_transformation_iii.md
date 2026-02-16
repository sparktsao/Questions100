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

### Implementation

```python
def maxRemoval(nums: List[int], queries: List[List[int]]) -> int:
    """
    Use greedy approach with heap to maximize query removals.

    Time: O(n log n + q log q), Space: O(n + q)
    """
    import heapq

    n = len(nums)
    queries.sort()  # Sort queries by start position

    # Priority queue to track available queries (by end position, descending)
    available = []
    # Track which queries we're using
    using = []

    query_idx = 0
    q_len = len(queries)

    for i in range(n):
        # Add all queries that start at or before position i
        while query_idx < q_len and queries[query_idx][0] <= i:
            # Push negative end to create max heap
            heapq.heappush(available, -queries[query_idx][1])
            query_idx += 1

        # Remove queries that can't cover position i anymore
        while using and using[0] < i:
            heapq.heappop(using)

        # Need to cover nums[i] decrements
        need = nums[i] - len(using)

        # Greedily select queries with largest end positions
        while need > 0 and available:
            end = -heapq.heappop(available)
            if end < i:
                continue  # This query can't cover position i

            # Use this query
            heapq.heappush(using, end)
            need -= 1

        # If we can't cover position i
        if need > 0:
            return -1

    # Maximum removals = total queries - queries we had to use
    return len(queries) - len(using)
```

### Alternative Implementation (Difference Array)

```python
def maxRemoval(nums: List[int], queries: List[List[int]]) -> int:
    """
    Alternative using difference array and greedy selection.

    Time: O(n + q log q), Space: O(n + q)
    """
    import heapq

    n = len(nums)
    queries.sort()

    available = []  # Max heap of query end positions
    active = []     # Min heap of active query end positions
    qi = 0

    diff = [0] * (n + 1)

    for i in range(n):
        # Add queries starting at position i
        while qi < len(queries) and queries[qi][0] <= i:
            heapq.heappush(available, -queries[qi][1])
            qi += 1

        # Apply difference array
        if i > 0:
            diff[i] += diff[i - 1]

        # Calculate current coverage
        current_coverage = diff[i]
        needed = nums[i] - current_coverage

        # Activate queries greedily
        while needed > 0 and available:
            end = -heapq.heappop(available)
            if end < i:
                continue

            # Activate this query
            diff[i] += 1
            diff[end + 1] -= 1
            current_coverage += 1
            heapq.heappush(active, end)
            needed -= 1

        if needed > 0:
            return -1

    return len(queries) - len(active)
```

### Complexity Analysis

**Time: O(n log q + q log q) - sorting queries and heap operations. Space: O(n + q) - heaps and auxiliary arrays**

**Why This is Optimal:**
- Greedy approach: always choose queries with largest end positions to maximize flexibility
- Heap provides efficient selection of best queries
- Must process each position, so O(n) is necessary
- Sorting ensures we consider queries in optimal order
- Binary heap gives O(log q) operations for query selection

---

## Categories & Tags

**Primary Topics:** Array, Greedy, Sorting, Heap (Priority Queue), Prefix Sum

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/zero-array-transformation-iii)*
