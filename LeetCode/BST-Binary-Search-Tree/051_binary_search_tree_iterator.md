# 051. Binary Search Tree Iterator

**Difficulty:** MEDIUM
**Frequency:** 51.9%
**Acceptance Rate:** 74.9%
**LeetCode Link:** [Binary Search Tree Iterator](https://leetcode.com/problems/binary-search-tree-iterator)

---

## Problem Description

Implement the `BSTIterator` class that represents an iterator over the in-order traversal of a binary search tree (BST):

- `BSTIterator(TreeNode root)` Initializes an object of the BSTIterator class. The root of the BST is given as part of the constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
- `boolean hasNext()` Returns true if there exists a number in the traversal to the right of the pointer, otherwise returns false.
- `int next()` Moves the pointer to the right, then returns the number at the pointer.

Notice that by initializing the pointer to a non-existent smallest number, the first call to `next()` will return the smallest element in the BST.

You may assume that `next()` calls will always be valid. That is, there will be at least a next number in the in-order traversal when `next()` is called.

**Constraints:**
- The number of nodes in the tree is in the range [1, 10^5]
- 0 <= Node.val <= 10^6
- At most 10^5 calls will be made to hasNext, and next

**Follow up:**
- Could you implement next() and hasNext() to run in average O(1) time and use O(h) memory, where h is the height of the tree?

---

## Examples

### Example 1
**Input:**
```
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
```
**Output:**
```
[null, 3, 7, true, 9, true, 15, true, 20, false]
```
**Explanation:**
```
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
```

### Example 2
**Input:**
```
["BSTIterator", "hasNext", "next"]
[[[1]], [], []]
```
**Output:**
```
[null, true, 1]
```
**Explanation:** Single node tree, hasNext() returns true, next() returns 1

### Example 3
**Input:**
```
["BSTIterator", "next", "next", "next"]
[[[5, 3, 7, 2, 4, 6, 8]], [], [], []]
```
**Output:**
```
[null, 2, 3, 4]
```
**Explanation:** In-order traversal returns elements in sorted order: 2, 3, 4, 5, 6, 7, 8

---

## Optimal Solution

### Implementation

```python
class BSTIterator:
    """
    BST Iterator using controlled in-order traversal with stack.

    Time: O(1) average for next/hasNext, Space: O(h) where h is tree height
    """

    def __init__(self, root: Optional[TreeNode]):
        """Initialize iterator with leftmost path."""
        self.stack = []
        self._push_left(root)

    def _push_left(self, node: Optional[TreeNode]) -> None:
        """Push all left children onto stack."""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Returns next smallest number in BST.

        Time: O(1) average - amortized analysis
        """
        # Pop the next node (leftmost unvisited)
        node = self.stack.pop()

        # If it has a right child, push all left children of right subtree
        if node.right:
            self._push_left(node.right)

        return node.val

    def hasNext(self) -> bool:
        """
        Returns whether we have a next smallest number.

        Time: O(1)
        """
        return len(self.stack) > 0
```

### Alternative Implementation (Pre-compute All Values)

```python
class BSTIterator:
    """
    Pre-compute all values using in-order traversal.

    Time: O(1) for next/hasNext, Space: O(n) for storing all nodes
    """

    def __init__(self, root: Optional[TreeNode]):
        """Perform complete in-order traversal."""
        self.nodes = []
        self.index = -1
        self._inorder(root)

    def _inorder(self, node: Optional[TreeNode]) -> None:
        """In-order traversal to collect all node values."""
        if not node:
            return
        self._inorder(node.left)
        self.nodes.append(node.val)
        self._inorder(node.right)

    def next(self) -> int:
        """Time: O(1)"""
        self.index += 1
        return self.nodes[self.index]

    def hasNext(self) -> bool:
        """Time: O(1)"""
        return self.index + 1 < len(self.nodes)
```

### Complexity Analysis

**Stack-based approach (Optimal):**
- **Time:** O(1) average for both next() and hasNext()
  - Amortized O(1) because each node is pushed and popped exactly once
  - Over n operations, total time is O(n), so average is O(1)
- **Space:** O(h) where h is the height of the tree
  - Stack stores at most h nodes (the height of the tree)
  - Best case O(log n) for balanced tree, worst case O(n) for skewed tree

**Pre-compute approach:**
- **Time:** O(1) for both operations (true constant time)
- **Space:** O(n) to store all node values

**Why Stack-Based is Optimal:**
- Achieves the follow-up requirement: average O(1) time with O(h) space
- More memory efficient than pre-computing all values
- Simulates controlled in-order traversal
- Only computes values as needed (lazy evaluation)

---

## Categories & Tags

**Primary Topics:** Stack, Tree, Design, Binary Search Tree, Binary Tree, Iterator

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/binary-search-tree-iterator)*
