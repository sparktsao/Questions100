# 003. Binary Tree Vertical Order Traversal

**Difficulty:** MEDIUM
**Frequency:** 93.4%
**Acceptance Rate:** 57.1%
**LeetCode Link:** [Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal)

---

## Problem Description

Given the `root` of a binary tree, return the vertical order traversal of its nodes' values. (i.e., from top to bottom, column by column).

If two nodes are in the same row and column, the order should be from left to right.

**Constraints:**
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

---

## Examples

### Example 1
**Input:** `root = [3,9,20,null,null,15,7]`
**Output:** `[[9],[3,15],[20],[7]]`
**Explanation:** Column -1: [9], Column 0: [3,15], Column 1: [20], Column 2: [7]

### Example 2
**Input:** `root = [3,9,8,4,0,1,7]`
**Output:** `[[4],[9],[3,0,1],[8],[7]]`
**Explanation:** Level order within same column

### Example 3
**Input:** `root = [3,9,8,4,0,1,7,null,null,null,2,5]`
**Output:** `[[4],[9,5],[3,0,1],[8,2],[7]]`
**Explanation:** Node 5 comes before 0 in same column

---

## Optimal Solution

### Implementation

```python
def verticalOrder(root: TreeNode) -> List[List[int]]:
    """
    BFS with column tracking using hash table.

    Time: O(n), Space: O(n)
    """
    if not root:
        return []

    from collections import defaultdict, deque
    column_table = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
        node, col = queue.popleft()
        column_table[col].append(node.val)

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    # Sort by column index
    return [column_table[x] for x in sorted(column_table.keys())]
```

### Complexity Analysis

**Time: O(n log n) - BFS + sorting columns. Space: O(n) - queue and hash table**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, Tree, Depth-First Search, Breadth-First Search, Sorting, Binary Tree

**Difficulty Level:** MEDIUM

---

*Problem source: [LeetCode](https://leetcode.com/problems/binary-tree-vertical-order-traversal)*
