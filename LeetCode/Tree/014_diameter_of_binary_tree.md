# 014. Diameter of Binary Tree

**Difficulty:** EASY
**Frequency:** 79.2%
**Acceptance Rate:** 63.6%
**LeetCode Link:** [Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree)

---

## Problem Description

Given the `root` of a binary tree, return the **length of the diameter** of the tree.

The diameter is the length of the **longest path between any two nodes**. The path may or may not pass through the root. Length = number of **edges** on the path.

**Key Insight:** At each node, the longest path through that node = `left_height + right_height`. Track the global max across all nodes using post-order DFS.

**Constraints:** 1 ≤ number of nodes ≤ 10⁴, −100 ≤ Node.val ≤ 100

---

## Examples

### Example 1
**Input:** `root = [1,2,3,4,5]`
**Output:** `3`
**Explanation:** Longest path is 4→2→1→3 or 5→2→1→3, which has 3 edges.

### Example 2
**Input:** `root = [1,2]`
**Output:** `1`
**Explanation:** Only one edge between root and child.

### Example 3 (boundary)
**Input:** `root = [1]`
**Output:** `0`
**Explanation:** Single node, no edges.

---

## Optimal Solution

### Approach: Post-order DFS — height propagates up, diameter updated at each node

```python
from math import inf
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd = 0  # diameter is always >= 0 (single node = 0 edges)

        def dfs(node):
            nonlocal maxd
            if node is None:
                return 0
            d1 = dfs(node.left)
            d2 = dfs(node.right)
            maxd = max(maxd, d1 + d2)   # path through this node
            return max(d1, d2) + 1       # height of this subtree

        dfs(root)
        return maxd
```

### Complexity Analysis

**Time: O(n)** — visit each node exactly once.
**Space: O(h)** — recursion stack, h = tree height (O(log n) balanced, O(n) skewed).

---

## Spark Notes

**Why post-order?**
The parent needs `height` from both children before it can compute the diameter passing through itself. So children must return first → post-order (left → right → process node).

**What dfs returns vs what it updates:**
- **Returns** the height of the current subtree (for the parent to use).
- **Updates** `maxd` as a side effect (the global answer).
These are two different things. Conflating them is the most common mistake.

**Dead parameter warning (original version):**
```python
def dfs(node, depth):          # 'depth' is never read from caller
    depth = max(d1, d2)        # immediately overwritten — the passed value is discarded
    return depth + 1
```
The `depth` parameter passed from the caller is never used. The function computes height purely from its children's return values. Simplify to `def dfs(node)` with `return max(d1, d2) + 1`.

**Why initialize maxd = 0 (not -inf)?**
For a single-node tree: d1=0, d2=0, `maxd = max(0, 0+0) = 0`. Correct.
Using `-inf` also works for this problem since constraints guarantee ≥ 1 node, but `0` is cleaner and self-documenting.

---

## Test Cases (T1→T5)

| Type | Input | Expected | What It Tests |
|------|-------|----------|---------------|
| T1 Basic | `[1,2,3,4,5]` | 3 | Core post-order logic, path crosses root |
| T2 Boundary | `[1]` | 0 | Single node, no edges |
| T2 Boundary | `[1,2]` | 1 | Single edge |
| T3 Condition | `[1,2,3]` | 2 | Path through root: left_h + right_h = 1+1 |
| T3 Condition | `[1,2,null,3,4]` | 2 | Diameter inside subtree, not through root |
| T4 Corner | `[1,2,null,3,null,4]` | 3 | Left-linear: diameter = chain length |
| T4 Corner | `[1,null,2,null,3,null,4]` | 3 | Right-linear, same logic |
| T5 Others | `[1,2,3,4,5,6,7]` | 4 | Perfect tree: depth(left)=depth(right)=2 |

---

## Categories & Tags

**Primary Topics:** Tree · Depth-First Search · Post-order · Binary Tree

**Difficulty Level:** EASY

---

*Problem source: [LeetCode](https://leetcode.com/problems/diameter-of-binary-tree)*
