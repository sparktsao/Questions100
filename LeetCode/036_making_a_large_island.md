# 036. Making A Large Island

**Difficulty:** HARD
**Frequency:** 65.0%
**Acceptance Rate:** 54.9%
**LeetCode Link:** [Making A Large Island](https://leetcode.com/problems/making-a-large-island)

---

## Problem Description

You are given an n x n binary matrix `grid`. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in `grid` after applying this operation.

An island is a 4-directionally connected group of 1s.

**Constraints:**
- n == grid.length
- n == grid[i].length
- 1 <= n <= 500
- grid[i][j] is either 0 or 1

---

## Examples

### Example 1
**Input:** `grid = [[1,0],[0,1]]`
**Output:** `3`
**Explanation:** Change one 0 to 1 and connect two 1s, then we get an island with area = 3

### Example 2
**Input:** `grid = [[1,1],[1,0]]`
**Output:** `4`
**Explanation:** Change the 0 to 1 and make the island bigger, only one island with area = 4

### Example 3
**Input:** `grid = [[1,1],[1,1]]`
**Output:** `4`
**Explanation:** Can't change any 0 to 1, only one island with area = 4

### Example 4
**Input:** `grid = [[0,0],[0,0]]`
**Output:** `1`
**Explanation:** Change any 0 to 1, creating an island of size 1

---

## Optimal Solution

### Implementation

```python
def largestIsland(grid: List[List[int]]) -> int:
    """
    Label islands with DFS, then check each 0 for potential connections.

    Time: O(n^2), Space: O(n^2)
    """
    n = len(grid)
    island_id = 2  # Start from 2 (0 and 1 are already used)
    island_sizes = {}

    def dfs(r, c, island_id):
        """DFS to label island and count size."""
        if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
            return 0

        grid[r][c] = island_id
        size = 1
        # Explore 4 directions
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            size += dfs(r + dr, c + dc, island_id)

        return size

    # Phase 1: Label all islands and record their sizes
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                size = dfs(r, c, island_id)
                island_sizes[island_id] = size
                island_id += 1

    # If entire grid is 1s, return n*n
    if not island_sizes:
        return 1
    if len(island_sizes) == 1 and sum(island_sizes.values()) == n * n:
        return n * n

    max_size = max(island_sizes.values())  # Best without changing any 0

    # Phase 2: Try changing each 0 to 1
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                # Find unique neighboring islands
                neighbors = set()
                for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                        neighbors.add(grid[nr][nc])

                # Calculate potential size
                potential_size = 1  # The 0 we're changing to 1
                for island_id in neighbors:
                    potential_size += island_sizes[island_id]

                max_size = max(max_size, potential_size)

    return max_size
```

### Alternative Implementation (Union-Find)

```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return
        if self.size[root_x] < self.size[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        self.size[root_x] += self.size[root_y]

def largestIsland(grid: List[List[int]]) -> int:
    """
    Union-Find approach for island merging.

    Time: O(n^2 * α(n)), Space: O(n^2)
    """
    n = len(grid)
    uf = UnionFind(n * n)

    # Union all adjacent 1s
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                idx = r * n + c
                for dr, dc in [(0,1), (1,0)]:
                    nr, nc = r + dr, c + dc
                    if nr < n and nc < n and grid[nr][nc] == 1:
                        uf.union(idx, nr * n + nc)

    max_size = max((uf.size[i] for i in range(n*n) if grid[i//n][i%n] == 1), default=0)

    # Try changing each 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                neighbors = set()
                for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        neighbors.add(uf.find(nr * n + nc))

                size = 1 + sum(uf.size[root] for root in neighbors)
                max_size = max(max_size, size)

    return max_size if max_size > 0 else 1
```

### Complexity Analysis

**Time: O(n^2) - visit each cell constant times. Space: O(n^2) - island labeling**

**Why This is Optimal:**
- Two-phase approach avoids redundant computation
- DFS labels islands in single pass per island
- Checking 0s only examines neighbors (constant time)
- Space efficient with in-place island labeling

---

## Categories & Tags

**Primary Topics:** Array, Depth-First Search, Breadth-First Search, Union Find, Matrix

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/making-a-large-island)*
