# 070. Swim in Rising Water

**Difficulty:** HARD
**Frequency:** 40.7%
**Acceptance Rate:** 62.9%
**LeetCode Link:** [Swim in Rising Water](https://leetcode.com/problems/swim-in-rising-water)

---

## Problem Description

You are given an `n x n` integer matrix `grid` where each value `grid[i][j]` represents the elevation at that point `(i, j)`.

The rain starts to fall. At time `t`, the depth of the water everywhere is `t`. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most `t`. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

Return the least time until you can reach the bottom right square `(n - 1, n - 1)` if you start at the top left square `(0, 0)`.

**Constraints:**
- n == grid.length
- n == grid[i].length
- 1 <= n <= 50
- 0 <= grid[i][j] < n^2
- Each value grid[i][j] is unique

---

## Examples

### Example 1
**Input:** `grid = [[0,2],[1,3]]`
**Output:** `3`
**Explanation:**
- At time 0, you are in grid location (0, 0)
- You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0
- At time 2, you can swim to (0, 1) because the elevation is 2
- At time 3, you can swim to (1, 1) because the elevation is 3
- The answer is 3

### Example 2
**Input:** `grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]`
**Output:** `16`
**Explanation:**
```
 0  1  2  3  4
24 23 22 21  5
12 13 14 15 16
11 17 18 19 20
10  9  8  7  6
```
The final route is marked in bold. We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

### Example 3
**Input:** `grid = [[0,1],[2,3]]`
**Output:** `3`
**Explanation:**
- Start at (0,0) with elevation 0
- Move to (0,1) at time 1
- Move to (1,1) at time 3
- Minimum time: 3

### Example 4
**Input:** `grid = [[0]]`
**Output:** `0`
**Explanation:** Already at destination, no movement needed

---

## Optimal Solution

### Implementation (Dijkstra's Algorithm)

```python
def swimInWater(grid: List[List[int]]) -> int:
    """
    Use Dijkstra's algorithm to find path with minimum maximum elevation.

    Time: O(n^2 log n), Space: O(n^2)
    """
    import heapq

    n = len(grid)
    visited = set()

    # Min heap: (max_elevation_so_far, row, col)
    heap = [(grid[0][0], 0, 0)]

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    while heap:
        max_elev, row, col = heapq.heappop(heap)

        # Reached destination
        if row == n - 1 and col == n - 1:
            return max_elev

        # Skip if already visited
        if (row, col) in visited:
            continue

        visited.add((row, col))

        # Explore neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check bounds
            if 0 <= new_row < n and 0 <= new_col < n:
                if (new_row, new_col) not in visited:
                    # New max elevation is the max of current path and neighbor
                    new_max_elev = max(max_elev, grid[new_row][new_col])
                    heapq.heappush(heap, (new_max_elev, new_row, new_col))

    return -1  # Should never reach here given constraints
```

### Alternative Implementation (Binary Search + BFS)

```python
def swimInWater(grid: List[List[int]]) -> int:
    """
    Binary search on time, use BFS to check if path exists.

    Time: O(n^2 log(n^2)), Space: O(n^2)
    """
    from collections import deque

    n = len(grid)

    def can_reach(time):
        """Check if we can reach destination at given time."""
        if grid[0][0] > time:
            return False

        visited = [[False] * n for _ in range(n)]
        queue = deque([(0, 0)])
        visited[0][0] = True

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col = queue.popleft()

            if row == n - 1 and col == n - 1:
                return True

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (0 <= new_row < n and 0 <= new_col < n and
                    not visited[new_row][new_col] and
                    grid[new_row][new_col] <= time):

                    visited[new_row][new_col] = True
                    queue.append((new_row, new_col))

        return False

    # Binary search on time
    left, right = grid[0][0], n * n - 1

    while left < right:
        mid = (left + right) // 2

        if can_reach(mid):
            right = mid
        else:
            left = mid + 1

    return left
```

### Alternative Implementation (Union-Find)

```python
def swimInWater(grid: List[List[int]]) -> int:
    """
    Union-Find approach: connect cells as time increases.

    Time: O(n^2 log n), Space: O(n^2)
    """
    n = len(grid)

    # Union-Find
    parent = list(range(n * n))

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px != py:
            parent[px] = py

    # Create list of (elevation, row, col)
    cells = []
    for i in range(n):
        for j in range(n):
            cells.append((grid[i][j], i, j))

    cells.sort()

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[False] * n for _ in range(n)]

    for elev, row, col in cells:
        visited[row][col] = True

        # Union with visited neighbors
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if (0 <= new_row < n and 0 <= new_col < n and
                visited[new_row][new_col]):

                union(row * n + col, new_row * n + new_col)

        # Check if start and end are connected
        if find(0) == find(n * n - 1):
            return elev

    return -1
```

### Complexity Analysis

**Time: O(n^2 log n) - Dijkstra with priority queue on n^2 cells. Space: O(n^2) - visited set and heap**

**Why This is Optimal:**
- Dijkstra's algorithm finds shortest path considering edge weights (max elevation)
- O(n^2 log n) is optimal for pathfinding on grid with n^2 cells
- Binary search approach also O(n^2 log(n^2)) with BFS checks
- Union-Find approach incrementally connects cells as time increases
- All approaches correctly handle the minimum maximum elevation constraint

---

## Categories & Tags

**Primary Topics:** Array, Binary Search, Depth-First Search, Breadth-First Search, Union Find, Heap (Priority Queue), Matrix

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/swim-in-rising-water)*
