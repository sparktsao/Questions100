# 092. Kth Smallest Element in a BST

**Difficulty:** MEDIUM
**Frequency:** 32.0%
**Acceptance Rate:** 75.3%
**LeetCode Link:** [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst)

---

## Problem Description

Given the `root` of a binary search tree, and an integer `k`, return the `kth` smallest value (1-indexed) of all the values of the nodes in the tree.

**Constraints:**
- The number of nodes in the tree is n
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

**Follow up:** If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

---

## Examples

### Example 1
**Input:** `root = [3,1,4,null,2], k = 1`
**Output:** `1`
**Explanation:** Inorder traversal gives [1,2,3,4], 1st smallest is 1

### Example 2
**Input:** `root = [5,3,6,2,4,null,null,1], k = 3`
**Output:** `3`
**Explanation:** Inorder traversal gives [1,2,3,4,5,6], 3rd smallest is 3

### Example 3
**Input:** `root = [2,1,3], k = 2`
**Output:** `2`
**Explanation:** Middle element in sorted order

### Example 4
**Input:** `root = [1], k = 1`
**Output:** `1`
**Explanation:** Single node tree

---

## Optimal Solution

### Implementation (Iterative Inorder)

```python
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    """
    Find kth smallest using iterative inorder traversal.

    Time: O(H + k) where H is tree height, Space: O(H) for stack
    """
    stack = []
    current = root
    count = 0

    while current or stack:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Process node
        current = stack.pop()
        count += 1

        # Found kth smallest
        if count == k:
            return current.val

        # Move to right subtree
        current = current.right

    return -1  # Should never reach here with valid input
```

### Alternative Implementation (Recursive)

```python
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    """
    Recursive inorder traversal approach.

    Time: O(n), Space: O(H) for recursion stack
    """
    def inorder(node):
        if not node:
            return []

        # Inorder: left, root, right
        return inorder(node.left) + [node.val] + inorder(node.right)

    # Get sorted values and return kth element (1-indexed)
    sorted_vals = inorder(root)
    return sorted_vals[k - 1]
```

### Optimized Recursive with Early Stopping

```python
def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    """
    Optimized recursive with early stopping.

    Time: O(H + k), Space: O(H)
    """
    def inorder(node):
        nonlocal k, result

        if not node or k == 0:
            return

        # Traverse left
        inorder(node.left)

        # Process current node
        k -= 1
        if k == 0:
            result = node.val
            return

        # Traverse right
        inorder(node.right)

    result = -1
    inorder(root)
    return result
```

### Follow-up: Augmented BST

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 1  # Number of nodes in subtree (including self)

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    """
    Using augmented BST with subtree sizes.

    Each node stores count of nodes in its subtree.
    Time: O(H), Space: O(1)
    """
    # Size of left subtree
    left_size = root.left.size if root.left else 0

    if k <= left_size:
        # kth smallest is in left subtree
        return kthSmallest(root.left, k)
    elif k == left_size + 1:
        # Current node is the kth smallest
        return root.val
    else:
        # kth smallest is in right subtree
        return kthSmallest(root.right, k - left_size - 1)
```

### Complexity Analysis

**Iterative Inorder:**
**Time: O(H + k) - traverse to kth element. Space: O(H) - stack for tree height**

**Augmented BST (Follow-up):**
**Time: O(H) - direct path to kth element. Space: O(1) - no extra space**

**Why This is Optimal:**
- Inorder traversal naturally gives sorted order for BST
- Early stopping at kth element avoids processing entire tree
- Iterative version saves space compared to storing all values
- Augmented BST enables O(H) queries, optimal for frequent operations
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Tree, Depth-First Search, Binary Search Tree, Binary Tree

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/kth-smallest-element-in-a-bst)*
