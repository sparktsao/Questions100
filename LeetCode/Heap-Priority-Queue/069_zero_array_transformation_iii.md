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

### Example 2
**Input:** `nums = [1,1,1,1], queries = [[1,3],[0,2],[1,3],[1,2]]`
**Output:** `2`

### Example 3
**Input:** `nums = [1,2,3,4], queries = [[0,3]]`
**Output:** `-1`

---

## Approach Progression: From Simple to Optimal

### Step 1 — Feasibility Check via Prefix Sum (Problem I)

**Question:** Given ALL queries applied, can the array become zero?

Use a **difference array**: `diff[l] += 1`, `diff[r+1] -= 1` for each query.
Prefix-sum `diff` gives the coverage count at each position.
If `coverage[i] >= nums[i]` everywhere → feasible.

```python
def isZeroArray(nums, queries):
    diff = [0] * (len(nums) + 1)
    for l, r in queries:
        diff[l] += 1
        diff[r + 1] -= 1
    coverage = 0
    for i in range(len(nums)):
        coverage += diff[i]
        if coverage < nums[i]:
            return False
    return True
```

**Time:** O(n + q) | **Space:** O(n)

This is the building block: it tells us whether a *given fixed set* of queries can zero the array.

---

### Step 2 — Binary Search on k (Problem II)

**Problem II variant:** Each query has value `val` (decrement by val). Find the **minimum k** such that using the first `k` queries is sufficient.

**Key insight:** The property is **monotonic** — if first `k` queries work, so does `k+1`.
→ Binary search on `k` ∈ `[0, m]`, use the prefix-sum feasibility check from Step 1.

```python
def minZeroArray(nums, queries):
    n, m = len(nums), len(queries)

    def can(k):
        diff = [0] * (n + 1)
        for i in range(k):
            l, r, val = queries[i]
            diff[l] += val
            diff[r + 1] -= val
        cur = 0
        for i in range(n):
            cur += diff[i]
            if cur < nums[i]:
                return False
        return True

    if all(x == 0 for x in nums):
        return 0
    left, right, ans = 1, m, -1
    while left <= right:
        mid = (left + right) // 2
        if can(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
```

**Time:** O((n + q) log q) | **Space:** O(n)

---

### Why Step 2 Fails for Problem III

Problem III asks: **which** queries can be removed to **maximize** removals while still keeping the array zeroable?

Binary search on k only works when "use first k queries" is the right framing.
Here, we need to **select the optimal subset** — we cannot assume the best subset is always a prefix of any sorted order.

- Sort by `l`? Doesn't help — two queries with same `l` but very different `r` need different treatment.
- Sort by `r`? Doesn't help — a query with large `r` might be redundant OR critical depending on what else is selected.
- Binary search on "how many to keep"? The subset isn't a prefix of any fixed ordering.

**Conclusion:** We need to decide, position by position, *which* queries to commit — and commit as few as possible.

---

### Step 3 — Two Heaps + Greedy (Problem III, Optimal)

**Core idea:** Walk positions left-to-right. At each position, only commit a query when forced (coverage falls short). When forced, always pick the query with the **furthest end** — it stays active longest and helps future positions most.

**Why furthest end is greedy-correct:**
At position `p`, all candidates in `available` have `l ≤ p`, so they all cover `p` equally.
A larger `r` means it stays in `active` longer → fewer forced commits later.
Picking a smaller `r` wastes a slot and forces an extra commit sooner.

| Heap | Type | Stores | Role |
|------|------|--------|------|
| `available` | max-heap (negated end) | not-yet-committed queries | candidates we CAN pick |
| `active` | min-heap (end) | committed queries | currently covering this position |

**Algorithm per position:**
1. Push all queries starting here into `available`
2. Pop expired queries from `active` (`end < position`)
3. While `len(active) < nums[position]`: commit from `available` (furthest end first)
4. If `available` empty before coverage met → return `-1`

```python
import heapq

def maxRemoval(nums, queries):
    queries.sort()          # sort by start index
    available = []          # max-heap: -(end), candidates not yet committed
    active = []             # min-heap: end, committed and still covering pos
    total_selected = 0
    q_index = 0

    for position in range(len(nums)):

        # 1. Enqueue newly eligible queries
        while q_index < len(queries) and queries[q_index][0] == position:
            heapq.heappush(available, -queries[q_index][1])
            q_index += 1

        # 2. Expire committed queries that no longer cover this position
        while active and active[0] < position:
            heapq.heappop(active)

        # 3. Commit greedily until coverage == nums[position]
        while len(active) < nums[position]:
            if not available:
                return -1
            furthest_end = -heapq.heappop(available)
            if furthest_end < position:     # already expired, skip
                continue
            heapq.heappush(active, furthest_end)
            total_selected += 1

    return len(queries) - total_selected
```

**Time:** O(n log q + q log q) | **Space:** O(q)

---

## Walkthrough

```
nums = [2, 0, 2], queries = [[0,2],[0,2],[1,1]]  (sorted already)

pos=0: available=[-2,-2], active=[]
  need 2 → commit end=2, commit end=2
  active=[2,2], total_selected=2

pos=1: available=[-1], active=[2,2]
  need 0 → nothing to do

pos=2: available=[-1], active=[2,2]
  need 2, len(active)=2 ✓

Answer: 3 - 2 = 1  ✓
```

---

## Summary: When to Use What

| Problem | Question | Approach | Why |
|---------|----------|----------|-----|
| I | Can ALL queries zero the array? | Prefix sum / diff array | Just check coverage ≥ need |
| II | Min k queries (first k) needed? | Binary search on k + prefix sum | Monotonic: more queries never hurt |
| III | Max queries removable? | Two heaps + greedy | Must choose optimal subset; greedy by furthest-end is provably optimal |

---

## Categories & Tags

**Primary Topics:** Array, Greedy, Sorting, Heap (Priority Queue)

**Difficulty Level:** MEDIUM

---

*Problem source: [LeetCode](https://leetcode.com/problems/zero-array-transformation-iii)*
