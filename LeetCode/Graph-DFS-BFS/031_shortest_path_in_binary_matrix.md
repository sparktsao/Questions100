# 031. Shortest Path in Binary Matrix

**Difficulty:** MEDIUM
**Frequency:** 67.4%
**Acceptance Rate:** 49.8%
**LeetCode Link:** [Shortest Path in Binary Matrix](https://leetcode.com/problems/shortest-path-in-binary-matrix)

---

## Problem Description

Given an n x n binary matrix `grid`, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:
- All the visited cells of the path are 0
- All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner)
- The length of a clear path is the number of visited cells of this path

**Constraints:**
- n == grid.length
- n == grid[i].length
- 1 <= n <= 100
- grid[i][j] is 0 or 1

---

## Examples

### Example 1
**Input:** `grid = [[0,1],[1,0]]`
**Output:** `2`
**Explanation:** The path from top-left to bottom-right is clear with length 2

### Example 2
**Input:** `grid = [[0,0,0],[1,1,0],[1,1,0]]`
**Output:** `4`
**Explanation:** The shortest clear path has length 4

### Example 3
**Input:** `grid = [[1,0,0],[1,1,0],[1,1,0]]`
**Output:** `-1`
**Explanation:** No clear path exists since top-left cell is 1

### Example 4
**Input:** `grid = [[0]]`
**Output:** `1`
**Explanation:** Single cell grid, path length is 1

---

## Optimal Solution

### Implementation

```python
def shortestPathBinaryMatrix(grid: List[List[int]]) -> int:
    """
    BFS to find shortest path in binary matrix with 8-directional movement.

    Time: O(n^2), Space: O(n^2)
    """
    from collections import deque

    n = len(grid)

    # Check if start or end is blocked
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    # 8 directions: up, down, left, right, and 4 diagonals
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    # BFS
    queue = deque([(0, 0, 1)])  # (row, col, path_length)
    grid[0][0] = 1  # Mark as visited

    while queue:
        row, col, length = queue.popleft()

        # Check if reached destination
        if row == n-1 and col == n-1:
            return length

        # Explore all 8 directions
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # Check bounds and if cell is unvisited (0)
            if 0 <= new_row < n and 0 <= new_col < n and grid[new_row][new_col] == 0:
                queue.append((new_row, new_col, length + 1))
                grid[new_row][new_col] = 1  # Mark as visited

    return -1  # No path found
```

### Complexity Analysis

**Time: O(n^2) - visit each cell at most once. Space: O(n^2) - queue size in worst case**

**Why This is Optimal:**
- BFS guarantees shortest path in unweighted graphs
- Each cell visited at most once due to marking
- 8-directional movement handled efficiently
- Early termination when destination reached

---

## Categories & Tags

**Primary Topics:** Array, Breadth-First Search, Matrix

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/shortest-path-in-binary-matrix)*
