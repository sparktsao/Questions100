# 007. Binary Tree Right Side View

**Difficulty:** MEDIUM
**Frequency:** 86.0%
**Acceptance Rate:** 67.0%
**LeetCode Link:** [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view)

---

## Problem Description

Given the `root` of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

**Constraints:**
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

---

## Examples

### Example 1
**Input:** `root = [1,2,3,null,5,null,4]`
**Output:** `[1,3,4]`
**Explanation:** Right view: 1 (root), 3 (right of 1), 4 (rightmost at level 2)

### Example 2
**Input:** `root = [1,null,3]`
**Output:** `[1,3]`
**Explanation:** Only right children visible

### Example 3
**Input:** `root = []`
**Output:** `[]`
**Explanation:** Empty tree

### Example 4
**Input:** `root = [1,2,3,4]`
**Output:** `[1,3,4]`
**Explanation:** Node 4 visible from right even though it's left child

---

## Optimal Solution

### Implementation

```python
def rightSideView(root: TreeNode) -> List[int]:
    """
    BFS level order, take last node at each level.

    Time: O(n), Space: O(w) where w is max width
    """
    if not root:
        return []

    from collections import deque
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node = queue.popleft()
            # Last node at this level
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
```

### Complexity Analysis

**Time: O(n) - visit all nodes. Space: O(w) - max queue width**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/binary-tree-right-side-view)
