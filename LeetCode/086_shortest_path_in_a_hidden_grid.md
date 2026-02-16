# 086. Shortest Path in a Hidden Grid

**Difficulty:** MEDIUM
**Frequency:** 32.0%
**Acceptance Rate:** 44.3%
**LeetCode Link:** [Shortest Path in a Hidden Grid](https://leetcode.com/problems/shortest-path-in-a-hidden-grid)

---

## Problem Description

This is an interactive problem.

There is a robot in a hidden grid, and you are trying to get it from its starting position to the target cell in this grid. The grid is of size `m x n`, and each cell in the grid is either empty or blocked. It is guaranteed that the starting position and the target position are different, and neither of them is blocked.

You want to find the minimum distance to the target cell. However, you do not know the grid's dimensions, the starting position of the robot, or the target position. You are only allowed to ask queries to your GridMaster object.

**GridMaster API:**
- `boolean canMove(char direction)` - Returns true if the robot can move in that direction. Otherwise, it returns false.
- `void move(char direction)` - Moves the robot in that direction. If this move would move the robot off the grid or onto a blocked cell, the move will be ignored and the robot will remain in the same position.
- `boolean isTarget()` - Returns true if the robot is currently on the target cell. Otherwise, it returns false.

Directions: 'U' (up), 'D' (down), 'L' (left), 'R' (right)

Return the minimum distance between the robot's initial starting position and the target cell. If there is no valid path between the cells, return -1.

**Constraints:**
- 1 <= n, m <= 500
- m == grid.length
- n == grid[i].length
- grid[i][j] is either 0 or 1
- It is guaranteed that robot's starting position is grid[0][0] and grid[0][0] == 0

---

## Examples

### Example 1
**Input:** `grid = [[1,2],[-1,3]]`
**Output:** `2`
**Explanation:** One possible path from (0,0) to (1,1) has distance 2

### Example 2
**Input:** `grid = [[0,1,2],[-1,3,-1]]`
**Output:** `4`
**Explanation:** Shortest path navigates around blocked cells

### Example 3
**Input:** `grid = [[1,0],[0,2]]`
**Output:** `-1`
**Explanation:** No path exists to target

### Example 4
**Input:** `grid = [[0,0,0],[0,2,0]]`
**Output:** `3`
**Explanation:** Direct path of length 3

---

## Optimal Solution

### Implementation

```python
class Solution:
    def findShortestPath(self, master: 'GridMaster') -> int:
        """
        Find shortest path in hidden grid using DFS + BFS.

        Step 1: Use DFS to explore and map the grid
        Step 2: Use BFS to find shortest path to target

        Time: O(m*n), Space: O(m*n)
        """
        # Direction mappings
        directions = {
            'U': (-1, 0),
            'D': (1, 0),
            'L': (0, -1),
            'R': (0, 1)
        }

        # Opposite directions for backtracking
        opposite = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

        # Store explored grid: True = accessible, False = blocked
        grid = {}
        target = None

        def dfs(row, col):
            """Explore grid using DFS with backtracking"""
            nonlocal target

            # Check if current position is target
            if master.isTarget():
                target = (row, col)

            # Mark current position as accessible
            grid[(row, col)] = True

            # Try all four directions
            for direction, (dr, dc) in directions.items():
                new_row, new_col = row + dr, col + dc

                # Skip if already visited
                if (new_row, new_col) in grid:
                    continue

                # Check if we can move in this direction
                if master.canMove(direction):
                    # Move to new position
                    master.move(direction)

                    # Recursively explore
                    dfs(new_row, new_col)

                    # Backtrack
                    master.move(opposite[direction])
                else:
                    # Mark as blocked
                    grid[(new_row, new_col)] = False

        # Step 1: Explore the grid starting from (0, 0)
        dfs(0, 0)

        # Step 2: If no target found, return -1
        if target is None:
            return -1

        # Step 3: BFS to find shortest path
        from collections import deque

        queue = deque([(0, 0, 0)])  # (row, col, distance)
        visited = {(0, 0)}

        while queue:
            row, col, dist = queue.popleft()

            # Check if we reached target
            if (row, col) == target:
                return dist

            # Try all four directions
            for dr, dc in directions.values():
                new_row, new_col = row + dr, col + dc

                # Check if valid and not visited
                if (new_row, new_col) in grid and \
                   grid[(new_row, new_col)] and \
                   (new_row, new_col) not in visited:
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col, dist + 1))

        return -1
```

### Complexity Analysis

**Time: O(m*n) - explore all cells once with DFS, then BFS. Space: O(m*n) - store grid map**

**Why This is Optimal:**
- Two-phase approach: mapping + pathfinding
- DFS efficiently explores entire accessible grid with backtracking
- BFS guarantees shortest path once grid is known
- Handles unknown grid dimensions gracefully
- Correctly identifies blocked cells and unreachable targets

---

## Categories & Tags

**Primary Topics:** Array, Depth-First Search, Breadth-First Search, Matrix, Interactive

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/shortest-path-in-a-hidden-grid)*
