# 025. Clone Graph

**Difficulty:** MEDIUM
**Frequency:** 71.4%
**Acceptance Rate:** 62.4%
**LeetCode Link:** [Clone Graph](https://leetcode.com/problems/clone-graph)

---

## Problem Description

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.

Each node in the graph contains a value (`int`) and a list (`List[Node]`) of its neighbors.

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```

**Test case format:**
The input is a serialized graph using adjacency list representation.

**Constraints:**
- The number of nodes in the graph is in the range [0, 100]
- 1 <= Node.val <= 100
- Node.val is unique for each node
- There are no repeated edges and no self-loops
- The Graph is connected and all nodes can be visited starting from the given node

---

## Examples

### Example 1
**Input:** `adjList = [[2,4],[1,3],[2,4],[1,3]]`
**Output:** `[[2,4],[1,3],[2,4],[1,3]]`
**Explanation:** 4 nodes forming a square graph

### Example 2
**Input:** `adjList = [[]]`
**Output:** `[[]]`
**Explanation:** Single node with no neighbors

### Example 3
**Input:** `adjList = []`
**Output:** `[]`
**Explanation:** Empty graph

### Example 4
**Input:** `adjList = [[2],[1,3],[2]]`
**Output:** `[[2],[1,3],[2]]`
**Explanation:** 3-node path graph

---

## Optimal Solution

### Implementation

```python
def cloneGraph(node: 'Node') -> 'Node':
    """
    DFS with hash map to track cloned nodes.

    Time: O(N + E), Space: O(N)
    """
    if not node:
        return None

    cloned = {}

    def dfs(node):
        if node in cloned:
            return cloned[node]

        # Create clone
        clone = Node(node.val)
        cloned[node] = clone

        # Clone neighbors
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))

        return clone

    return dfs(node)
```

### Complexity Analysis

**Time: O(N + E) - visit all nodes and edges. Space: O(N) - hash map + recursion**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, Depth-First Search, Breadth-First Search, Graph

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/clone-graph)*
