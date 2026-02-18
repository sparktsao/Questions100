# 027. Range Sum of BST

**Difficulty:** EASY
**Frequency:** 69.5%
**Acceptance Rate:** 87.5%
**LeetCode Link:** [Range Sum of BST](https://leetcode.com/problems/range-sum-of-bst)

---

## Problem Description

Given the `root` node of a binary search tree and two integers `low` and `high`, return the sum of values of all nodes with a value in the **inclusive** range `[low, high]`.

**Constraints:**
- The number of nodes in the tree is in the range [1, 2 * 10^4]
- 1 <= Node.val <= 10^5
- 1 <= low <= high <= 10^5
- All Node.val are unique

---

## Examples

### Example 1
**Input:** `root = [10,5,15,3,7,null,18], low = 7, high = 15`
**Output:** `32`
**Explanation:** Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32

```
        10
       /  \
      5    15
     / \     \
    3   7    18
```

### Example 2
**Input:** `root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10`
**Output:** `23`
**Explanation:** Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23

```
           10
          /  \
         5    15
        / \   / \
       3   7 13 18
      /   /
     1   6
```

### Example 3
**Input:** `root = [10], low = 10, high = 10`
**Output:** `10`
**Explanation:** Single node in range

### Example 4
**Input:** `root = [3,1,5], low = 2, high = 4`
**Output:** `3`
**Explanation:** Only node with value 3 is in range [2, 4]

---

## Optimal Solution

### Implementation (Recursive DFS with Pruning)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    """
    DFS with BST property pruning for optimal performance.

    Time: O(n) worst case, O(log n) average, Space: O(h) for recursion stack
    """
    if not root:
        return 0

    # If current value is in range, include it
    if low <= root.val <= high:
        return (root.val +
                rangeSumBST(root.left, low, high) +
                rangeSumBST(root.right, low, high))

    # If current value is less than low, only check right subtree
    elif root.val < low:
        return rangeSumBST(root.right, low, high)

    # If current value is greater than high, only check left subtree
    else:  # root.val > high
        return rangeSumBST(root.left, low, high)
```

### Alternative Implementation (Iterative DFS)

```python
def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    """
    Iterative DFS using stack to avoid recursion overhead.

    Time: O(n) worst case, Space: O(h)
    """
    if not root:
        return 0

    stack = [root]
    total = 0

    while stack:
        node = stack.pop()

        if not node:
            continue

        # If node value in range, add to sum
        if low <= node.val <= high:
            total += node.val

        # Leverage BST property to prune search
        if node.val > low:
            stack.append(node.left)
        if node.val < high:
            stack.append(node.right)

    return total
```

### Alternative Implementation (BFS)

```python
def rangeSumBST(root: TreeNode, low: int, high: int) -> int:
    """
    BFS using queue for level-order traversal.

    Time: O(n) worst case, Space: O(w) where w is max width
    """
    from collections import deque

    if not root:
        return 0

    queue = deque([root])
    total = 0

    while queue:
        node = queue.popleft()

        if not node:
            continue

        if low <= node.val <= high:
            total += node.val

        # Use BST property to prune
        if node.val > low and node.left:
            queue.append(node.left)
        if node.val < high and node.right:
            queue.append(node.right)

    return total
```

### Complexity Analysis

**Time: O(n) worst case when all nodes in range, O(log n) average with pruning. Space: O(h) for recursion stack where h is tree height**

**Why This is Optimal:**
- Leverages BST property to prune entire subtrees
- If current node < low, no need to check left subtree (all values smaller)
- If current node > high, no need to check right subtree (all values larger)
- In balanced BST with small range, can skip majority of nodes
- O(h) space is optimal for tree traversal
- Early termination when subtrees can be pruned

---

## Categories & Tags

**Primary Topics:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/range-sum-of-bst)*
