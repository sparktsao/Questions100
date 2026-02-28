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

At each position, we need exactly `nums[position]` queries actively covering it. We greedily **commit** queries only when forced, always picking the one with the furthest end — it stays useful for future positions longest. The total committed queries is the minimum we must keep, so:

```
max removals = len(queries) - total_selected
```

### Two Heaps

| Heap | Type | Stores | Meaning |
|------|------|--------|---------|
| `available` | max-heap (negated) | query end positions | Candidates not yet committed |
| `active` | min-heap | query end positions | Committed queries still covering current position |

### Algorithm

For each `position` in `nums`:
1. **Enqueue** all queries whose `start == position` into `available`
2. **Expire** committed queries from `active` whose `end < position`
3. **Commit** greedily from `available` until `len(active) == nums[position]`
   - If `available` is empty before coverage is met → return `-1`
   - Skip any available query already expired (`end < position`)
4. After all positions: return `len(queries) - total_selected`

### Why Greedy (Pick Furthest End) is Correct

When forced to commit a new query at position `p`, picking the one with the largest `r` is optimal because:
- All candidates in `available` share `l <= p`, so they all cover the current position equally
- A larger `r` means the query remains in `active` longer, reducing how many new commits future positions need
- Picking a shorter `r` wastes a slot — it expires sooner and forces an extra commit later

### Implementation

```python
import heapq
from typing import List

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:

        # Sort queries by start index
        queries.sort()

        n = len(nums)

        # available: max-heap (store -end)
        # Meaning: queries we CAN choose but haven't chosen yet
        available = []

        # active: min-heap (store end)
        # Meaning: queries we HAVE chosen and still cover current position
        active = []

        total_selected = 0  # total number of queries we permanently select
        q_index = 0         # pointer for queries

        for position in range(n):

            # --------------------------------------------------
            # 1. Add newly available queries into candidate pool
            # --------------------------------------------------
            while q_index < len(queries) and queries[q_index][0] == position:
                end = queries[q_index][1]
                heapq.heappush(available, -end)  # max-heap via negation
                q_index += 1

            # --------------------------------------------------
            # 2. Remove expired active queries
            # These queries were selected before,
            # but no longer cover this position.
            # NOTE: removing from active does NOT unselect them —
            # they are still counted in total_selected.
            # --------------------------------------------------
            while active and active[0] < position:
                heapq.heappop(active)

            # --------------------------------------------------
            # 3. Ensure coverage is enough
            # If current coverage < nums[position],
            # we are FORCED to commit more queries.
            # --------------------------------------------------
            while len(active) < nums[position]:

                # No available query left to save us
                if not available:
                    return -1

                # Greedy: pick the query that ends furthest —
                # it helps future positions most
                furthest_end = -heapq.heappop(available)

                # If it already expired, skip it
                if furthest_end < position:
                    continue

                # Commit this query permanently
                heapq.heappush(active, furthest_end)
                total_selected += 1  # never decreased

        # Maximum removable = total queries - minimum selected
        return len(queries) - total_selected
```

### Complexity Analysis

**Time: O(n log q + q log q)**
- Sorting queries: O(q log q)
- Each query pushed/popped from `available` at most once: O(q log q)
- Each query pushed/popped from `active` at most once: O(q log q)

**Space: O(q)** — both heaps hold at most all queries

### Walkthrough

```
nums = [1, 1, 1], queries = [[0,0], [1,1], [2,2]]

position=0: available=[0], active=[]
  need 1, commit end=0 → active=[0], total_selected=1

position=1: available=[1], active=[] (0 expired)
  need 1, commit end=1 → active=[1], total_selected=2

position=2: available=[2], active=[] (1 expired)
  need 1, commit end=2 → active=[2], total_selected=3

Result: 3 - 3 = 0  ✓ (each query covers exactly one unique index)
```

```
nums = [2, 0, 2], queries = [[0,2], [0,2], [1,1]]
Sorted: [[0,2], [0,2], [1,1]]

position=0: available=[-2,-2], active=[]
  need 2, commit end=2 → active=[2], total_selected=1
         commit end=2 → active=[2,2], total_selected=2

position=1: available=[-1], active=[2,2]
  need 0, no commits needed

position=2: available=[-1], active=[2,2]  ([1] expired from available but never committed)
  need 2, len(active)=2 already ✓

Result: 3 - 2 = 1  ✓
```

---

## Categories & Tags

**Primary Topics:** Array, Greedy, Sorting, Heap (Priority Queue)

**Difficulty Level:** MEDIUM

---

*Problem source: [LeetCode](https://leetcode.com/problems/zero-array-transformation-iii)*
