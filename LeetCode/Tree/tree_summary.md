# Tree - Comprehensive Guide

## DFS for Paths vs BFS for Levels

---

## 🎯 Overview

**Total Problems:** 10
**Difficulty:** Easy (1) • Medium (7) • Hard (2)

**Core Concept:**
Choose DFS (recursion/stack) for path problems, BFS (queue) for level/distance problems

**Key Insight:**
DFS: paths & subtree properties. BFS: levels & shortest distance.

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: DFS Recursive (Height, Diameter, Path Sum)
### Pattern 2: BFS Level Order (Right Side View, Zigzag)
### Pattern 3: DFS Iterative with Stack
### Pattern 4: Parent Pointers for Upward Traversal


---

## 🎓 Learning Path

Max Depth → Diameter → Right Side View → LCA → Max Path Sum

---

## ⚠️ Common Pitfalls

1. Not checking None 2. Confusing pre/in/post order 3. Not tracking global state 4. DFS when need BFS

---

## ✅ Testing Strategy

Test: null, single node, left skewed, right skewed, balanced

---

## 💡 Templates & Code Patterns


```python
# DFS Template
def dfs(node):
    if not node:
        return base_case
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node.val, left, right)

# BFS Template
from collections import deque
queue = deque([root])
while queue:
    size = len(queue)
    for _ in range(size):
        node = queue.popleft()
        # process
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```


---

## 💎 Mastery Tips

BFS for levels, DFS for paths. Always check None first.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 003 | [Binary Tree Vertical Order Traversal](./003_binary_tree_vertical_order_traversal.md) | MEDIUM | 93.4% |
| 005 | [Lowest Common Ancestor of a Binary Tree III](./005_lowest_common_ancestor_of_a_binary_tree_iii.md) | MEDIUM | 89.6% |
| 007 | [Binary Tree Right Side View](./007_binary_tree_right_side_view.md) | MEDIUM | 86.0% |
| 009 | [Lowest Common Ancestor of a Binary Tree](./009_lowest_common_ancestor_of_a_binary_tree.md) | MEDIUM | 82.9% |
| 011 | [Nested List Weight Sum](./011_nested_list_weight_sum.md) | MEDIUM | 81.7% |
| 013 | [Sum Root to Leaf Numbers](./013_sum_root_to_leaf_numbers.md) | MEDIUM | 80.5% |
| 014 | [Diameter of Binary Tree](./014_diameter_of_binary_tree.md) | EASY | 79.2% |
| 061 | [Vertical Order Traversal of a Binary Tree](./061_vertical_order_traversal_of_a_binary_tree.md) | HARD | 47.0% |
| 066 | [All Nodes Distance K in Binary Tree](./066_all_nodes_distance_k_in_binary_tree.md) | MEDIUM | 47.0% |
| 076 | [Binary Tree Maximum Path Sum](./076_binary_tree_maximum_path_sum.md) | HARD | 40.7% |

---

[← Back to Main](../README.md)
