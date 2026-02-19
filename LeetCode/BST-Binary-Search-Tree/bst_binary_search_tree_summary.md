# BST Binary Search Tree - Comprehensive Guide




## 📋 Problems in This Category

- [027. Range Sum of BST](https://github.com/sparktsao/Questions100/blob/main/LeetCode/BST-Binary-Search-Tree/027_range_sum_of_bst.md) - `DFS+Pruning`
- [051. Binary Search Tree Iterator](https://github.com/sparktsao/Questions100/blob/main/LeetCode/BST-Binary-Search-Tree/051_binary_search_tree_iterator.md) - `Iterator+Stack`
- [060. Closest Binary Search Tree Value](https://github.com/sparktsao/Questions100/blob/main/LeetCode/BST-Binary-Search-Tree/060_closest_binary_search_tree_value.md) - `Binary Search`
- [092. Kth Smallest Element in a BST](https://github.com/sparktsao/Questions100/blob/main/LeetCode/BST-Binary-Search-Tree/092_kth_smallest_element_in_a_bst.md) - `Inorder+Counter`

---

## Leverage In-Order Traversal = Sorted Sequence

---

## 🎯 Overview

**Total Problems:** 4
**Difficulty:** Easy (2) • Medium (2) • Hard (0)

**Core Concept:**
BST property: left < root < right. In-order traversal gives sorted order.

**Key Insight:**
Use BST property to prune search space. In-order gives sorted sequence.

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: BST Search (O(log n) average, O(n) worst)
### Pattern 2: In-Order Traversal (Iterative & Recursive)
### Pattern 3: BST Validation
### Pattern 4: Range Queries


---

## 🎓 Learning Path

Validate BST → Kth Smallest → BST Iterator → Range Sum

---

## ⚠️ Common Pitfalls

1. Not handling duplicates 2. Wrong in-order logic 3. Not using BST property 4. Treating as regular tree

---

## ✅ Testing Strategy

Test: null, single, left-skewed, right-skewed, balanced, with duplicates

---

## 💡 Templates & Code Patterns


```python
# In-order iterative
def inorder_iterative(root):
    stack, result = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result
```


---

## 💎 Mastery Tips

Remember: in-order = sorted. Use BST property to skip branches.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 027 | [Range Sum of BST](./027_range_sum_of_bst.md) | EASY | 69.5% |
| 051 | [Binary Search Tree Iterator](./051_binary_search_tree_iterator.md) | MEDIUM | 51.9% |
| 060 | [Closest Binary Search Tree Value](./060_closest_binary_search_tree_value.md) | EASY | 47.0% |
| 092 | [Kth Smallest Element in a BST](./092_kth_smallest_element_in_a_bst.md) | MEDIUM | 32.0% |

---

[← Back to Main](../README.md)
