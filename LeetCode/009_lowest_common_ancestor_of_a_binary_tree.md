# 009. Lowest Common Ancestor of a Binary Tree

**Difficulty:** MEDIUM
**Frequency:** 82.9%
**Acceptance Rate:** 66.8%
**LeetCode Link:** [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree)

---

## Problem Description

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: "The lowest common ancestor is defined between two nodes `p` and `q` as the lowest node in T that has both `p` and `q` as descendants (where we allow a node to be a descendant of itself)."

**Constraints:**
- The number of nodes in the tree is in the range [2, 10^5]
- -10^9 <= Node.val <= 10^9
- All Node.val are unique
- p != q
- p and q will exist in the tree

---

## Examples

### Example 1
**Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`
**Output:** `3`
**Explanation:** LCA of nodes 5 and 1 is 3

### Example 2
**Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4`
**Output:** `5`
**Explanation:** LCA of nodes 5 and 4 is 5 (node can be ancestor of itself)

### Example 3
**Input:** `root = [1,2], p = 1, q = 2`
**Output:** `1`
**Explanation:** Root is LCA

---

## Optimal Solution

### Implementation

```python
def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Recursive DFS to find LCA.

    Time: O(n), Space: O(h)
    """
    if not root or root == p or root == q:
        return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If both sides return non-null, current node is LCA
    if left and right:
        return root

    # Return whichever side is non-null
    return left if left else right
```

### Complexity Analysis

**Time: O(n) - visit all nodes in worst case. Space: O(h) - recursion stack**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Tree, Depth-First Search, Binary Tree

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree)
