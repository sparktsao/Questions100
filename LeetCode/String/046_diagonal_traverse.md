# 046. Diagonal Traverse

**Difficulty:** MEDIUM
**Frequency:** 56.0%
**Acceptance Rate:** 63.2%
**LeetCode Link:** [Diagonal Traverse](https://leetcode.com/problems/diagonal-traverse)

---

## Problem Description

Given an m x n matrix `mat`, return an array of all the elements of the array in a diagonal order.

**Constraints:**
- m == mat.length
- n == mat[i].length
- 1 <= m, n <= 10^4
- 1 <= m * n <= 10^4
- -10^5 <= mat[i][j] <= 10^5

---

## Examples

### Example 1
**Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]]`
**Output:** `[1,2,4,7,5,3,6,8,9]`
**Explanation:** Start at (0,0), go diagonal up-right, then diagonal down-left, alternating

### Example 2
**Input:** `mat = [[1,2],[3,4]]`
**Output:** `[1,2,3,4]`
**Explanation:** 2x2 matrix traversed diagonally

### Example 3
**Input:** `mat = [[1]]`
**Output:** `[1]`
**Explanation:** Single element matrix

### Example 4
**Input:** `mat = [[1,2,3,4],[5,6,7,8]]`
**Output:** `[1,2,5,6,3,4,7,8]`
**Explanation:** Non-square matrix, 2x4 dimensions

---

## Optimal Solution

### Implementation

```python
def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    """
    Traverse matrix diagonally with direction alternation.

    Time: O(m*n), Space: O(1) excluding output
    """
    if not mat or not mat[0]:
        return []

    m, n = len(mat), len(mat[0])
    result = []
    row, col = 0, 0
    going_up = True

    for _ in range(m * n):
        result.append(mat[row][col])

        if going_up:
            # Moving up-right
            if col == n - 1:
                # Hit right boundary, move down and switch direction
                row += 1
                going_up = False
            elif row == 0:
                # Hit top boundary, move right and switch direction
                col += 1
                going_up = False
            else:
                # Continue diagonal up-right
                row -= 1
                col += 1
        else:
            # Moving down-left
            if row == m - 1:
                # Hit bottom boundary, move right and switch direction
                col += 1
                going_up = True
            elif col == 0:
                # Hit left boundary, move down and switch direction
                row += 1
                going_up = True
            else:
                # Continue diagonal down-left
                row += 1
                col -= 1

    return result
```

### Alternative Implementation Using Diagonal Groups

```python
def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    """
    Group elements by diagonal sum, then reverse alternating diagonals.

    Time: O(m*n), Space: O(m*n)
    """
    from collections import defaultdict

    if not mat or not mat[0]:
        return []

    m, n = len(mat), len(mat[0])
    diagonals = defaultdict(list)

    # Group elements by diagonal (row + col is same for each diagonal)
    for row in range(m):
        for col in range(n):
            diagonals[row + col].append(mat[row][col])

    result = []
    for key in sorted(diagonals.keys()):
        # Reverse every other diagonal (even indices go up, odd go down)
        if key % 2 == 0:
            result.extend(reversed(diagonals[key]))
        else:
            result.extend(diagonals[key])

    return result
```

### Complexity Analysis

**Time: O(m*n) - visit each element once. Space: O(1) - excluding output array**

**Why This is Optimal:**
- Must visit every element exactly once, so O(m*n) is optimal
- Direction switching logic handles boundary conditions elegantly
- No extra space needed beyond output array in simulation approach
- Handles non-square matrices correctly

---

## Categories & Tags

**Primary Topics:** Array, Matrix, Simulation

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/diagonal-traverse)*
