# 005. Lowest Common Ancestor of a Binary Tree III

**Difficulty:** MEDIUM
**Frequency:** 89.6%
**Acceptance Rate:** 82.5%
**LeetCode Link:** [Lowest Common Ancestor of a Binary Tree III](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii)

---

## Problem Description

Given two nodes of a binary tree `p` and `q`, return their lowest common ancestor (LCA).

Each node will have a reference to its parent node. The definition for Node is:
```
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
```

**Constraints:**
- The number of nodes in the tree is in the range [2, 10^5]
- -10^9 <= Node.val <= 10^9
- All Node.val are unique
- p != q
- p and q exist in the tree

---

## Examples

### Example 1
**Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1`
**Output:** `3`
**Explanation:** LCA of 5 and 1 is 3

### Example 2
**Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4`
**Output:** `5`
**Explanation:** LCA of 5 and 4 is 5 (node can be ancestor of itself)

### Example 3
**Input:** `root = [1,2], p = 1, q = 2`
**Output:** `1`
**Explanation:** Root is LCA

---

## Optimal Solution

### Implementation

```python
def lowestCommonAncestor(p: 'Node', q: 'Node') -> 'Node':
    """
    Use parent pointers like finding intersection in linked lists.

    Time: O(h), Space: O(1)
    """
    # Get depths
    p1, p2 = p, q

    # Traverse to root, when reach None, switch to other node's path
    # They will meet at LCA
    while p1 != p2:
        p1 = p1.parent if p1.parent else q
        p2 = p2.parent if p2.parent else p

    return p1
```

### Complexity Analysis

**Time: O(h) - height of tree. Space: O(1) - constant**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, Two Pointers, Tree, Binary Tree

**Difficulty Level:** MEDIUM

---

*Problem source: [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii)*
