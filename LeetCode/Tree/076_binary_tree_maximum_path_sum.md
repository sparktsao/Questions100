# 076. Binary Tree Maximum Path Sum

**Difficulty:** HARD
**Frequency:** 40.7%
**Acceptance Rate:** 41.2%
**LeetCode Link:** [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum)

---

## Problem Description

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the `root` of a binary tree, return the maximum path sum of any non-empty path.

**Constraints:**
- The number of nodes in the tree is in the range [1, 3 * 10^4]
- -1000 <= Node.val <= 1000

---

## Examples

### Example 1
**Input:** `root = [1,2,3]`
**Output:** `6`
**Explanation:** Path: 2 -> 1 -> 3, sum = 2 + 1 + 3 = 6

### Example 2
**Input:** `root = [-10,9,20,null,null,15,7]`
**Output:** `42`
**Explanation:** Path: 15 -> 20 -> 7, sum = 15 + 20 + 7 = 42

### Example 3
**Input:** `root = [-3]`
**Output:** `-3`
**Explanation:** Single negative node

### Example 4
**Input:** `root = [5,4,8,11,null,13,4,7,2,null,null,null,1]`
**Output:** `48`
**Explanation:** Path goes through multiple levels

---

## Optimal Solution

### Implementation

```python
def maxPathSum(root: TreeNode) -> int:
    """
    DFS with path sum tracking through each node.

    Time: O(n), Space: O(h) for recursion
    """
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum

        if not node:
            return 0

        # Get max path sum from left and right (ignore negative)
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        # Max path through this node
        current_max = node.val + left + right
        max_sum = max(max_sum, current_max)

        # Return max single path through this node
        return node.val + max(left, right)

    dfs(root)
    return max_sum
```

### Complexity Analysis

**Time: O(n) - visit each node once. Space: O(h) - recursion stack height**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Dynamic Programming, Tree, Depth-First Search, Binary Tree

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/binary-tree-maximum-path-sum)*
