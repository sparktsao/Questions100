# 003. Binary Tree Vertical Order Traversal

**Difficulty:** MEDIUM
**Frequency:** 93.4%
**Acceptance Rate:** 57.1%
**LeetCode Link:** [Binary Tree Vertical Order Traversal](https://leetcode.com/problems/binary-tree-vertical-order-traversal)

---

## Problem Description

Given the `root` of a binary tree, return the vertical order traversal of its nodes' values — from top to bottom, column by column.

If two nodes are in the **same row and column**, the order should be from **left to right**.

**Constraints:**
- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

---

## Examples

### Example 1
**Input:** `root = [3,9,20,null,null,15,7]`
**Output:** `[[9],[3,15],[20],[7]]`

### Example 2
**Input:** `root = [3,9,8,4,0,1,7]`
**Output:** `[[4],[9],[3,0,1],[8],[7]]`

### Example 3
**Input:** `root = [3,9,8,4,0,1,7,null,null,null,2,5]`
**Output:** `[[4],[9,5],[3,0,1],[8,2],[7]]`

---

## Core Insight: DFS Does Not Guarantee Row Order

This is the central trap of this problem.

Every node needs two coordinates:
- `col` — horizontal position (left child: col-1, right child: col+1)
- `row` — depth from root (child: row+1)

**DFS visits nodes in depth-first order, not level order.**

Example tree:
```
        3          row=0, col=0
       / \
      9   20       row=1, col=-1 and col=1
         /  \
        15   7     row=2, col=0 and col=2
```

DFS preorder visits: 3, 9, 20, 15, 7

For column 0, DFS would collect: `[3, 15]` in that order — correct here.

But consider a deeper case where a right subtree node at col=0 is visited before a left subtree node at col=0. DFS gives no row-order guarantee within a column. The within-column order must come from `row`, not from traversal order.

**Two approaches arise from this insight:**

| Approach | Row guarantee source | Sort needed? |
|---|---|---|
| BFS (level order) | BFS visits row by row naturally | Only sort by `col` |
| DFS | DFS has no row order | Sort by `(col, row)` both |

---

## Approach 1: BFS — O(n log n), simpler

BFS processes level by level. Within each column, nodes are naturally appended in top-to-bottom order. No row tracking needed.

```python
from collections import defaultdict, deque

def verticalOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    col_map = defaultdict(list)
    queue = deque([(root, 0)])         # (node, col)

    while queue:
        node, col = queue.popleft()
        col_map[col].append(node.val)  # BFS guarantees top-to-bottom within col

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    return [col_map[c] for c in sorted(col_map)]
```

**Time: O(n log n)** — BFS O(n) + sorting columns O(k log k) where k ≤ n

**Why no row sort:** BFS dequeues level 0 before level 1 before level 2... so within each column the list is already in row order.

---

## Approach 2: DFS — must track (col, row) and sort both

DFS visits nodes in an arbitrary order relative to depth. If you only track `col`, nodes in the same column may be appended out of row order.

You must store `(row, val)` per column, then sort by `row` before output.

```python
from collections import defaultdict

def verticalOrder(root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    col_map = defaultdict(list)   # col -> [(row, val)]

    def dfs(node, row, col):
        if not node:
            return
        col_map[col].append((row, node.val))
        dfs(node.left,  row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)

    result = []
    for col in sorted(col_map):
        # Sort by row to restore top-to-bottom order DFS didn't give us
        result.append([val for row, val in sorted(col_map[col])])

    return result
```

**Time: O(n log n)** — DFS O(n) + sort per column (total O(n log n))

**The extra sort on `row` is the cost of using DFS.**

---

## Why the Distinction Matters

```
        3          (row=0, col=0)
       / \
      9   20       (row=1, col=-1), (row=1, col=1)
     /   /
    4   15         (row=2, col=-2), (row=2, col=0)
```

DFS preorder: 3, 9, 4, 20, 15

Column 0 in DFS order: [3, 15] — appended as 3 first, then 15.
Happens to be correct here because 3 is row=0 and 15 is row=2.

But if the tree shape causes a deeper left-subtree node and a shallower right-subtree node to share a column, DFS order would append the deeper one first — wrong output without the row sort.

**BFS eliminates this problem entirely by construction.**

---

## Which to Use in Interviews

- **BFS** is the cleaner, less error-prone solution for this problem. Prefer it.
- **DFS** requires storing `(row, val)` pairs and a secondary sort. More code, same asymptotic complexity.
- The sister problem **061 Vertical Order Traversal of a Binary Tree** has an explicit same-row tiebreak rule → DFS with `(row, col, val)` sort is the natural fit there.

---

## Categories & Tags

**Primary Topics:** BFS | Column tracking (DFS requires extra row sort)

**Difficulty Level:** MEDIUM

**Why tricky:** DFS is the instinct for tree problems, but DFS order ≠ level order. Recognizing that row order must come from BFS (or explicit row tracking in DFS) is the key insight.

---

*Problem source: [LeetCode](https://leetcode.com/problems/binary-tree-vertical-order-traversal)*
