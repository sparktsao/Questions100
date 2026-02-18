# 060. Closest Binary Search Tree Value

**Difficulty:** EASY
**Frequency:** 47.0%
**Acceptance Rate:** 49.8%
**LeetCode Link:** [Closest Binary Search Tree Value](https://leetcode.com/problems/closest-binary-search-tree-value)

---

## Problem Description

Given the `root` of a binary search tree and a `target` value, return the value in the BST that is closest to the `target`.

**Constraints:**
- The number of nodes in the tree is in the range [1, 10^4]
- 0 <= Node.val <= 10^9
- -10^9 <= target <= 10^9

---

## Examples

### Example 1
**Input:** `root = [4,2,5,1,3], target = 3.714286`
**Output:** `4`
**Explanation:** 4 is closer to 3.714286 than 3

### Example 2
**Input:** `root = [1], target = 4.428571`
**Output:** `1`
**Explanation:** Only one node in tree

### Example 3
**Input:** `root = [5,3,7,2,4,6,8], target = 3.5`
**Output:** `3 or 4`
**Explanation:** Both 3 and 4 are equally close

### Example 4
**Input:** `root = [10,5,15,2,7], target = 6`
**Output:** `7 or 5`
**Explanation:** 5 and 7 are equally distant

---

## Optimal Solution

### Implementation

```python
def closestValue(root: TreeNode, target: float) -> int:
    """
    Binary search in BST to find closest value.

    Time: O(h), Space: O(1) for iterative
    """
    closest = root.val

    while root:
        # Update closest if current is closer
        if abs(root.val - target) < abs(closest - target):
            closest = root.val

        # Binary search based on BST property
        if target < root.val:
            root = root.left
        else:
            root = root.right

    return closest
```

### Complexity Analysis

**Time: O(h) - height of tree. Space: O(1) - iterative constant space**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Binary Search, Tree, Depth-First Search, Binary Search Tree, Binary Tree

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/closest-binary-search-tree-value)*
