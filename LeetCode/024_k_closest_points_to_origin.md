# 024. K Closest Points to Origin

**Difficulty:** MEDIUM
**Frequency:** 71.4%
**Acceptance Rate:** 67.9%
**LeetCode Link:** [K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin)

---

## Problem Description

Given an array of `points` where `points[i] = [xi, yi]` represents a point on the X-Y plane and an integer `k`, return the `k` closest points to the origin `(0, 0)`.

The distance between two points on the X-Y plane is the Euclidean distance (i.e., `√((x1 - x2)² + (y1 - y2)²)`).

You may return the answer in **any order**. The answer is **guaranteed** to be **unique** (except for the order that it is in).

**Constraints:**
- 1 <= k <= points.length <= 10^4
- -10^4 <= xi, yi <= 10^4

---

## Examples

### Example 1
**Input:** `points = [[1,3],[-2,2]], k = 1`
**Output:** `[[-2,2]]`
**Explanation:** The distance between (1, 3) and the origin is sqrt(10). The distance between (-2, 2) and the origin is sqrt(8). Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin. We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]]

### Example 2
**Input:** `points = [[3,3],[5,-1],[-2,4]], k = 2`
**Output:** `[[3,3],[-2,4]]`
**Explanation:** The answer [[-2,4],[3,3]] would also be accepted

### Example 3
**Input:** `points = [[1,3],[-2,2],[2,-2]], k = 2`
**Output:** `[[-2,2],[2,-2]]`
**Explanation:** Distance from origin: (1,3)=sqrt(10), (-2,2)=sqrt(8), (2,-2)=sqrt(8). The two closest are (-2,2) and (2,-2)

### Example 4
**Input:** `points = [[0,1],[1,0]], k = 2`
**Output:** `[[0,1],[1,0]]`
**Explanation:** Both points are equidistant from origin, return both

---

## Optimal Solution

### Implementation (Max-Heap Approach)

```python
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Use max-heap to maintain k closest points efficiently.

    Time: O(n log k), Space: O(k)
    """
    import heapq

    # Max-heap to store k closest points
    # We use negative distance for max-heap behavior
    max_heap = []

    for x, y in points:
        # Calculate squared distance (no need for sqrt for comparison)
        dist = -(x*x + y*y)

        if len(max_heap) < k:
            heapq.heappush(max_heap, (dist, [x, y]))
        else:
            # If current point is closer than farthest in heap
            if dist > max_heap[0][0]:
                heapq.heappushpop(max_heap, (dist, [x, y]))

    return [point for _, point in max_heap]
```

### Alternative Implementation (Quick Select)

```python
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Quick select approach for O(n) average time.

    Time: O(n) average, O(n²) worst, Space: O(1)
    """
    # Calculate distances
    distances = [(x*x + y*y, i) for i, (x, y) in enumerate(points)]

    def partition(left, right, pivot_idx):
        pivot_dist = distances[pivot_idx][0]
        # Move pivot to end
        distances[pivot_idx], distances[right] = distances[right], distances[pivot_idx]
        store_idx = left

        for i in range(left, right):
            if distances[i][0] < pivot_dist:
                distances[i], distances[store_idx] = distances[store_idx], distances[i]
                store_idx += 1

        # Move pivot to final position
        distances[store_idx], distances[right] = distances[right], distances[store_idx]
        return store_idx

    def quickselect(left, right, k):
        if left == right:
            return

        pivot_idx = left + (right - left) // 2
        pivot_idx = partition(left, right, pivot_idx)

        if k == pivot_idx:
            return
        elif k < pivot_idx:
            quickselect(left, pivot_idx - 1, k)
        else:
            quickselect(pivot_idx + 1, right, k)

    quickselect(0, len(distances) - 1, k - 1)

    return [points[i] for _, i in distances[:k]]
```

### Simple Sorting Approach

```python
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    """
    Simple sorting approach - clean and readable.

    Time: O(n log n), Space: O(n)
    """
    # Sort by distance from origin (no need for sqrt)
    points.sort(key=lambda p: p[0]**2 + p[1]**2)
    return points[:k]
```

### Complexity Analysis

**Time: O(n log k) for heap, O(n) average for quickselect, O(n log n) for sorting. Space: O(k) for heap, O(1) for quickselect, O(n) for sorting**

**Why Heap is Often Best:**
- O(n log k) time complexity, better than O(n log n) when k << n
- O(k) space complexity - only stores k points in memory
- Stable performance, no worst-case quadratic behavior like quickselect
- Easy to implement and understand
- Works well for streaming data

---

## Categories & Tags

**Primary Topics:** Array, Math, Divide and Conquer, Geometry, Sorting, Heap (Priority Queue), Quickselect

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/k-closest-points-to-origin)*
