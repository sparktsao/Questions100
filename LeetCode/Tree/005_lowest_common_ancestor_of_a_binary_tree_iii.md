# 005. Lowest Common Ancestor of a Binary Tree III

**Difficulty:** MEDIUM 🔴
**Frequency:** 89.6%
**Acceptance Rate:** 82.5%
**LeetCode Link:** [Lowest Common Ancestor of a Binary Tree III](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii)

---

## Problem Description

Given two nodes of a binary tree `p` and `q`, return their lowest common ancestor (LCA).

Each node has a reference to its parent node. The definition for Node is:
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

### Example 2
**Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4`
**Output:** `5`
**Explanation:** A node can be an ancestor of itself.

### Example 3
**Input:** `root = [1,2], p = 1, q = 2`
**Output:** `1`

---

## Key Insight: This is Linked List Intersection

Because every node has a `parent` pointer, the path from any node to the root is exactly a **linked list**.

```
p path:  D → C → B → A
q path:  B → A
```

LCA = the **intersection node** of two linked lists.

Use the classic pointer-switching trick.

---

## The Two-Path Visual

Tree:
```
    A
   /
  B
 /
C
/
D
```
`p = D`, `q = B`, **LCA = B**

Write out both full traversal sequences (each walks own path then the other's):

```
a walks: D  C  B  A  →  B  A
b walks: B  A  →  D  C  B  A
```

Align by step:

```
step:    1  2  3  4  5
a:       D  C  B  A  B
b:       B  A  D  C  B  ✅
```

They meet at **B** in step 5.

**Why:** both pointers travel `len(path_p) + len(path_q)` total steps — same distance, same destination.

---

## Optimal Solution

```python
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        a, b = p, q

        while a != b:
            a = a.parent if a else q   # walk own path; when None, jump to q's start
            b = b.parent if b else p   # walk own path; when None, jump to p's start

        return a
```

**Time: O(h) — each pointer walks at most 2h steps**
**Space: O(1) — no extra storage**

### Critical implementation note

The switch condition must be `if a` (check the pointer itself), **not** `if a.parent`:

```python
# WRONG — never actually switches (stops one step early at root)
a = a.parent if a.parent else q

# CORRECT — switches when a has become None (walked off root)
a = a.parent if a else q
```

---

## O(h) Space Alternative (Path Comparison)

Correct but not optimal — uses O(h) extra space for stored paths.

```python
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def findpath(node):
            path = []
            while node:
                path.append(node)
                node = node.parent
            return path  # child → root order

        pathtop = findpath(p)
        pathtoq = findpath(q)

        i = len(pathtop) - 1
        j = len(pathtoq) - 1

        while i >= 0 and j >= 0:
            if pathtop[i] == pathtoq[j]:
                i -= 1
                j -= 1
            else:
                break

        return pathtop[i + 1]
```

Scan from the root end (index -1) inward. The last matching node is the LCA.

| Solution | Time | Space | Interview |
|---|---|---|---|
| Path comparison (above) | O(h) | O(h) | Good |
| HashSet parent walk | O(h) | O(h) | Good |
| Two-pointer switch | O(h) | O(1) | ⭐ Best |

---

## Why Similar to Fast/Slow Pointer?

Not quite. Fast/slow pointers detect **cycles** by running at different speeds.

This problem uses **equal-speed pointer switching** to equalize path lengths — closer to Linked List Intersection (LeetCode 160) than Floyd's cycle detection.

The connection: both patterns exploit the structure of pointer chains to make two pointers converge without extra memory.

---

## Categories & Tags

**Primary Topics:** Two Pointers | Linked List Intersection (parent pointer chain)

**Difficulty Level:** MEDIUM 🔴

**Why Red:** The O(1) space solution requires recognizing the Linked List Intersection pattern — non-obvious without prior exposure. The pointer-switch condition (`if a` not `if a.parent`) is an easy bug trap.

---

*Problem source: [LeetCode](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii)*
