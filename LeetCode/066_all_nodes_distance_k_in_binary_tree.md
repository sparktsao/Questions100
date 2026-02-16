# 066. All Nodes Distance K in Binary Tree

**Difficulty:** MEDIUM
**Frequency:** 47.0%
**Acceptance Rate:** 66.4%
**LeetCode Link:** [All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree)

---

## Problem Description

Given the `root` of a binary tree, the value of a target node `target`, and an integer `k`, return an array of the values of all nodes that have a distance `k` from the target node.

You can return the answer in any order.

**Constraints:**
- The number of nodes in the tree is in the range [1, 500]
- 0 <= Node.val <= 500
- All the values Node.val are unique
- target is the value of one of the nodes in the tree
- 0 <= k <= 1000

---

## Examples

### Example 1
**Input:** `root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2`
**Output:** `[7,4,1]`
**Explanation:** Nodes at distance 2 from node 5

### Example 2
**Input:** `root = [1], target = 1, k = 3`
**Output:** `[]`
**Explanation:** No nodes at distance 3 from root

### Example 3
**Input:** `root = [0,1,2,null,3], target = 3, k = 1`
**Output:** `[1]`
**Explanation:** Node 1 is parent, distance 1 from 3

### Example 4
**Input:** `root = [0,1,2,3,null,null,null,4], target = 1, k = 2`
**Output:** `[0,4]`
**Explanation:** Both parent and grandchild at distance 2

---

## Optimal Solution

### Implementation

```python
def distanceK(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    """
    Build parent pointers, then BFS from target.

    Time: O(n), Space: O(n)
    """
    from collections import deque, defaultdict

    # Build parent mapping
    parent = {}
    def build_parent(node, par=None):
        if not node:
            return
        parent[node] = par
        build_parent(node.left, node)
        build_parent(node.right, node)

    build_parent(root)

    # BFS from target
    queue = deque([(target, 0)])
    visited = {target}
    result = []

    while queue:
        node, dist = queue.popleft()

        if dist == k:
            result.append(node.val)
            continue

        # Check all neighbors: left, right, parent
        for neighbor in [node.left, node.right, parent[node]]:
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return result
```

### Complexity Analysis

**Time: O(n) - visit all nodes. Space: O(n) - parent map + queue**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, Tree, Depth-First Search, Breadth-First Search, Binary Tree

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree)*
