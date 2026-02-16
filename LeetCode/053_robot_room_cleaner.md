# 053. Robot Room Cleaner

**Difficulty:** HARD
**Frequency:** 51.9%
**Acceptance Rate:** 77.5%
**LeetCode Link:** [Robot Room Cleaner](https://leetcode.com/problems/robot-room-cleaner)

---

## Problem Description

You are controlling a robot that is located somewhere in a room. The room is modeled as an `m x n` binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API `Robot`.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects an obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

```
interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
```

**Constraints:**
- m == room.length
- n == room[i].length
- 1 <= m <= 100
- 1 <= n <= 200
- room[i][j] is either 0 or 1
- 0 <= row < m
- 0 <= col < n
- room[row][col] == 1
- All the empty cells can be visited from the starting position

---

## Examples

### Example 1
**Input:** `room = [[1,1,1,1,1,0,1,1],[1,1,1,1,1,0,1,1],[1,0,1,1,1,1,1,1],[0,0,0,1,0,0,0,0],[1,1,1,1,1,1,1,1]], row = 1, col = 3`
**Output:** `Robot cleaned all cells`
**Explanation:** All reachable cells are cleaned

### Example 2
**Input:** `room = [[1]], row = 0, col = 0`
**Output:** `Robot cleaned cell`
**Explanation:** Single cell room

### Example 3
**Input:** `room = [[1,1,1],[1,0,1],[1,1,1]], row = 1, col = 1`
**Output:** `Cannot start (wall)`
**Explanation:** But constraints guarantee start is empty

---

## Optimal Solution

### Implementation

```python
def cleanRoom(robot):
    """
    DFS with backtracking, tracking visited cells.

    Time: O(N - M), Space: O(N - M) where N is cells, M is obstacles
    """
    # Directions: up, right, down, left
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set()

    def go_back():
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def backtrack(cell=(0, 0), d=0):
        visited.add(cell)
        robot.clean()

        # Try all 4 directions
        for i in range(4):
            new_d = (d + i) % 4
            new_cell = (cell[0] + directions[new_d][0],
                       cell[1] + directions[new_d][1])

            if new_cell not in visited and robot.move():
                backtrack(new_cell, new_d)
                go_back()

            # Turn robot clockwise
            robot.turnRight()

    backtrack()
```

### Complexity Analysis

**Time: O(N - M) - visit each accessible cell once. Space: O(N - M) - visited set**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Backtracking, Interactive

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/robot-room-cleaner)*
