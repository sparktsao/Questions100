# 061. Vertical Order Traversal of a Binary Tree

**Difficulty:** HARD
**Frequency:** 47.0%
**Acceptance Rate:** 51.3%
**LeetCode Link:** [Vertical Order Traversal of a Binary Tree](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree)

---

## Problem Description

Given the `root` of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position `(row, col)`, its left and right children will be at positions `(row + 1, col - 1)` and `(row + 1, col + 1)` respectively. The root of the tree is at `(0, 0)`.

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.

**Constraints:**
- The number of nodes in the tree is in the range [1, 1000]
- 0 <= Node.val <= 1000

---

## Examples

### Example 1
**Input:** `root = [3,9,20,null,null,15,7]`
**Output:** `[[9],[3,15],[20],[7]]`
**Explanation:** Column order: -1:[9], 0:[3,15], 1:[20], 2:[7]

### Example 2
**Input:** `root = [1,2,3,4,5,6,7]`
**Output:** `[[4],[2],[1,5,6],[3],[7]]`
**Explanation:** Same column nodes sorted by value

### Example 3
**Input:** `root = [1,2,3,4,6,5,7]`
**Output:** `[[4],[2],[1,5,6],[3],[7]]`
**Explanation:** Values are sorted when at same position

---

## Optimal Solution

### Implementation

```python
def verticalTraversal(root: TreeNode) -> List[List[int]]:
    """
    DFS to collect (col, row, val), then sort and group.

    Time: O(n log n), Space: O(n)
    """
    nodes = []

    def dfs(node, row, col):
        if not node:
            return

        nodes.append((col, row, node.val))
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)

    # Sort by column, then row, then value
    nodes.sort()

    result = []
    prev_col = float('-inf')

    for col, row, val in nodes:
        if col != prev_col:
            result.append([])
            prev_col = col
        result[-1].append(val)

    return result
```

### Complexity Analysis

**Time: O(n log n) - sorting nodes. Space: O(n) - storing all nodes**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, Tree, Depth-First Search, Breadth-First Search, Sorting, Binary Tree

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree)*
