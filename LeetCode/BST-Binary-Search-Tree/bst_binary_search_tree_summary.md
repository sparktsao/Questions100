# BST Binary Search Tree - Comprehensive Guide

## 🎯 Overview

**Total Problems:** 4
**Difficulty:** Easy (2) • Medium (2) • Hard (0)

**Core Concept:**
BST property: `left < root < right`. In-order traversal gives sorted order.

**Key Insight:**
The BST property enables **O(log n) pruning** in balanced trees by eliminating entire subtrees. In-order traversal produces sorted sequences, which is the foundation for many BST algorithms.

---

## 📋 Problems in This Category

1. [027. Range Sum of BST](./027_range_sum_of_bst.md) - `DFS+Pruning` (EASY, 69.5%)
2. [051. Binary Search Tree Iterator](./051_binary_search_tree_iterator.md) - `Iterator+Stack` (MEDIUM, 51.9%)
3. [060. Closest Binary Search Tree Value](./060_closest_binary_search_tree_value.md) - `Binary Search` (EASY, 47.0%)
4. [092. Kth Smallest Element in a BST](./092_kth_smallest_element_in_a_bst.md) - `Inorder+Counter` (MEDIUM, 32.0%)

---

## 🔍 Deep Dive: Problem Comparison

### Pattern Analysis

| Problem | Core Pattern | BST Property Usage | Traversal Type | Time | Space |
|---------|-------------|-------------------|----------------|------|-------|
| **Range Sum** | DFS + Pruning | Prune subtrees outside range | Any (DFS/BFS) | O(n) worst, O(log n) avg | O(h) |
| **BST Iterator** | Lazy In-order | Controlled in-order simulation | In-order (iterative) | O(1) amortized | O(h) |
| **Closest Value** | Binary Search | Navigate left/right like binary search | Path traversal | O(h) | O(1) |
| **Kth Smallest** | In-order + Early Stop | In-order = sorted sequence | In-order (with counter) | O(h + k) | O(h) |

### Key Distinctions

#### 1. Range Sum of BST vs Others
**What makes it unique:** This is the only problem where you can **aggressively prune entire subtrees** based on range bounds.

```python
# If current node < low, skip entire left subtree
if root.val < low:
    return rangeSumBST(root.right, low, high)
# If current node > high, skip entire right subtree
if root.val > high:
    return rangeSumBST(root.left, low, high)
```

**Why it matters:** In a balanced BST with a narrow range, you can skip ~50% of nodes at each level, achieving O(log n) performance instead of O(n).

**When to use this pattern:** Any problem asking for values/sums/counts within a range in a BST.

---

#### 2. BST Iterator vs Kth Smallest
**Similar:** Both use in-order traversal to get sorted sequences.

**Different:**
- **BST Iterator** requires **lazy evaluation** (O(1) per operation) with state preservation across calls
- **Kth Smallest** can stop early after k elements and doesn't need state preservation

```python
# Iterator: Maintains stack across multiple next() calls
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)  # Setup

    def next(self):
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)  # Lazy: only process when needed
        return node.val

# Kth Smallest: Single-shot traversal with counter
def kthSmallest(root, k):
    stack, count = [], 0
    while current or stack:
        # ... in-order traversal
        count += 1
        if count == k:
            return current.val  # Early exit
```

**Trade-off:**
- Iterator optimizes for **multiple sequential accesses** (amortized O(1))
- Kth Smallest optimizes for **single query** (O(h + k) total)

**Follow-up insight:** Both can be optimized with augmented BST (storing subtree sizes) to achieve O(h) direct access.

---

#### 3. Closest Value: Pure Binary Search
**What makes it unique:** The only problem that treats BST like **classic binary search** on a sorted array.

```python
def closestValue(root, target):
    closest = root.val
    while root:
        # Update closest candidate
        if abs(root.val - target) < abs(closest - target):
            closest = root.val

        # Binary search decision: go left or right
        root = root.left if target < root.val else root.right
```

**Key insight:** You don't need full traversal. Just navigate to where the target **would be** if it existed, updating closest along the path.

**Comparison to Range Sum:** Range Sum must explore both subtrees when `low < root.val < high`. Closest Value only explores **one path** down the tree.

---

### Complexity Hierarchy

```
O(1) iterative           → Closest Value (single path)
O(h) single path         → Closest Value
O(h) amortized per call  → BST Iterator
O(h + k)                 → Kth Smallest (early stopping)
O(log n) avg with prune  → Range Sum (balanced + narrow range)
O(n) worst case          → All problems (skewed tree or full traversal)
```

---

## 📚 Core Sub-Patterns & When to Use

### Pattern 1: DFS with BST Pruning
**Use when:** Problem involves ranges, bounds, or conditional inclusion of nodes.

**Examples:** Range Sum, Range queries, Count nodes in range

**Key technique:**
```python
if node.val < low:
    # All left subtree values < node.val < low, skip left
    search(node.right)
elif node.val > high:
    # All right subtree values > node.val > high, skip right
    search(node.left)
else:
    # node.val in range, explore both
    search(node.left) + search(node.right)
```

---

### Pattern 2: Iterative In-Order Traversal
**Use when:** Need sorted sequence, kth element, or validation.

**Examples:** Kth Smallest, BST Iterator, Validate BST

**Key technique:**
```python
stack, curr = [], root
while curr or stack:
    # Phase 1: Go left as far as possible
    while curr:
        stack.append(curr)
        curr = curr.left

    # Phase 2: Process node (in sorted order)
    curr = stack.pop()
    process(curr.val)  # This happens in sorted order!

    # Phase 3: Move to right subtree
    curr = curr.right
```

**Why iterative?** More control than recursion - you can pause, resume, or stop early.

---

### Pattern 3: Binary Search on BST
**Use when:** Searching for single value, closest value, or insert/delete position.

**Examples:** Closest Value, Search BST, Insert/Delete node

**Key technique:**
```python
while root:
    if target == root.val:
        return root  # Found
    elif target < root.val:
        root = root.left  # Search left
    else:
        root = root.right  # Search right
```

**O(1) space!** No recursion stack, no auxiliary data structures.

---

### Pattern 4: Controlled/Lazy Traversal with Stack
**Use when:** Need to pause and resume traversal, maintain state across calls.

**Examples:** BST Iterator, Morris traversal

**Why use stack?**
- Simulate recursion iteratively
- Pause at any point and resume later
- O(h) space vs O(n) for pre-computing all values

---

## 🎓 Learning Path & Progression

### Stage 1: Basic Binary Search on BST
Start with: **060. Closest Binary Search Tree Value**
- **Why first:** Simplest pattern, pure binary search
- **Complexity:** O(h) time, O(1) space
- **Skill learned:** Navigate BST like sorted array

### Stage 2: Full Traversal with Pruning
Next: **027. Range Sum of BST**
- **Why second:** Introduces pruning optimization
- **Complexity:** O(n) worst, O(log n) average
- **Skill learned:** Leverage BST property to skip subtrees

### Stage 3: In-Order = Sorted Sequence
Then: **092. Kth Smallest Element in a BST**
- **Why third:** Master in-order traversal with early stopping
- **Complexity:** O(h + k) time, O(h) space
- **Skill learned:** Iterative in-order, counter-based early termination

### Stage 4: Advanced: Stateful Iterator
Finally: **051. Binary Search Tree Iterator**
- **Why last:** Most complex - requires maintaining state across calls
- **Complexity:** O(1) amortized, O(h) space
- **Skill learned:** Lazy evaluation, controlled traversal

---

## 🔄 Common Patterns Across Problems

### Pattern: When to Use Recursion vs Iteration

| Approach | Pros | Cons | Use When |
|----------|------|------|----------|
| **Recursive** | Clean, intuitive code | O(h) stack space, can't pause easily | One-shot computation (Range Sum) |
| **Iterative** | Control over traversal, can pause | More code, manual stack management | Need to pause/resume (Iterator, Kth) |
| **Morris** | O(1) space | Modifies tree temporarily, complex | Extreme space constraints |

### Pattern: Early Stopping Opportunities

```python
# Range Sum: Stop entire subtree
if node.val < low: return explore(node.right)

# Kth Smallest: Stop after k elements
count += 1
if count == k: return node.val

# Closest Value: Stop when found exact match (optional optimization)
if node.val == target: return node.val
```

---

## ⚠️ Common Pitfalls & How to Avoid

### Pitfall 1: Not Using BST Property
**Wrong:** Treat BST like regular binary tree
```python
# BAD: Explores entire tree unnecessarily
def rangeSumBST(root, low, high):
    if not root: return 0
    return (root.val if low <= root.val <= high else 0) + \
           rangeSumBST(root.left, low, high) + \
           rangeSumBST(root.right, low, high)
```

**Right:** Prune using BST property
```python
# GOOD: Skips subtrees outside range
def rangeSumBST(root, low, high):
    if not root: return 0
    if root.val < low: return rangeSumBST(root.right, low, high)
    if root.val > high: return rangeSumBST(root.left, low, high)
    return root.val + rangeSumBST(root.left, low, high) + \
                      rangeSumBST(root.right, low, high)
```

---

### Pitfall 2: Wrong In-Order Traversal Logic
**Wrong:** Forgetting the three phases
```python
# BAD: Incorrect order
while stack:
    node = stack.pop()
    process(node)  # Wrong order!
    if node.left: stack.append(node.left)
    if node.right: stack.append(node.right)
```

**Right:** Left → Root → Right
```python
# GOOD: Correct in-order
while curr or stack:
    while curr:  # 1. Go all the way left
        stack.append(curr)
        curr = curr.left
    curr = stack.pop()  # 2. Process root
    process(curr)
    curr = curr.right  # 3. Go right
```

---

### Pitfall 3: Iterator Not Maintaining State
**Wrong:** Re-traversing from root each time
```python
# BAD: O(n) per next() call
class BSTIterator:
    def next(self):
        # Re-traverse from root each time - SLOW!
        return self._inorder(self.root)[self.index]
```

**Right:** Maintain stack state
```python
# GOOD: O(1) amortized per next() call
class BSTIterator:
    def next(self):
        node = self.stack.pop()  # State preserved in stack
        if node.right: self._push_left(node.right)
        return node.val
```

---

### Pitfall 4: Handling Duplicates (If Allowed)
**Issue:** BST definition varies - some allow duplicates, some don't.

**Solution:** Clarify with interviewer, then adjust comparisons:
```python
# If duplicates allowed, decide: left or right?
# Convention: duplicates go RIGHT
if target < node.val:  # Strict inequality
    node = node.left
else:  # target >= node.val
    node = node.right
```

---

## ✅ Testing Strategy

### Edge Cases to Test

1. **Structure:**
   - Empty tree (null root)
   - Single node
   - Left-skewed (linked list going left)
   - Right-skewed (linked list going right)
   - Balanced tree

2. **Values:**
   - Target at root
   - Target at leaf
   - Target not in tree
   - All nodes in range (Range Sum)
   - No nodes in range (Range Sum)
   - k = 1 (smallest element)
   - k = n (largest element)

3. **Special Cases:**
   - Negative values (if allowed)
   - Duplicates (if allowed)
   - Float target (Closest Value)

---

## 💡 Templates & Code Patterns

### Template 1: Recursive DFS with Pruning
```python
def dfs_with_pruning(root, low, high):
    """Use for range queries, conditional processing."""
    if not root:
        return base_case

    # Prune left subtree
    if root.val < low:
        return dfs_with_pruning(root.right, low, high)

    # Prune right subtree
    if root.val > high:
        return dfs_with_pruning(root.left, low, high)

    # Process current + both subtrees
    return (root.val +
            dfs_with_pruning(root.left, low, high) +
            dfs_with_pruning(root.right, low, high))
```

---

### Template 2: Iterative In-Order Traversal
```python
def inorder_iterative(root):
    """Use for kth element, validation, sorted sequence."""
    stack, result = [], []
    curr = root

    while curr or stack:
        # Phase 1: Push all left nodes
        while curr:
            stack.append(curr)
            curr = curr.left

        # Phase 2: Process node (sorted order)
        curr = stack.pop()
        result.append(curr.val)

        # Phase 3: Move to right subtree
        curr = curr.right

    return result
```

---

### Template 3: Binary Search in BST
```python
def binary_search_bst(root, target):
    """Use for search, closest value, insert/delete position."""
    result = None

    while root:
        # Update result based on current node
        result = update_result(root, target, result)

        # Navigate based on BST property
        if target < root.val:
            root = root.left
        elif target > root.val:
            root = root.right
        else:
            return root  # Found exact match

    return result
```

---

### Template 4: BST Iterator Pattern
```python
class BSTIterator:
    """Use for stateful traversal, lazy evaluation."""

    def __init__(self, root):
        self.stack = []
        self._push_left(root)

    def _push_left(self, node):
        """Push all left children."""
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        """Return next smallest, O(1) amortized."""
        node = self.stack.pop()
        if node.right:
            self._push_left(node.right)
        return node.val

    def hasNext(self):
        """O(1) check."""
        return len(self.stack) > 0
```

---

## 💎 Mastery Tips

### Mental Model: BST as Sorted Array
Think of BST as a **sorted array** where:
- In-order traversal = reading array left to right
- Binary search = navigating tree based on comparisons
- Kth smallest = array[k-1]

### Optimization Checklist
Before implementing, ask:
1. **Can I prune?** (Range queries → Yes)
2. **Can I stop early?** (Kth smallest → Yes)
3. **Do I need all nodes?** (No → Use iterative for control)
4. **Is it one query or many?** (Many → Consider augmented BST)
5. **Is space critical?** (Yes → Avoid pre-computing, use O(1) or O(h))

### When BST Doesn't Help
BST property is **useless** for:
- Level-order traversal (use BFS)
- Path sum problems (must check all paths)
- Subtree problems (need full subtree exploration)
- Structural problems (shape matters, not values)

### Time Complexity Quick Reference
```
O(1)     → hasNext() in iterator
O(h)     → Single path (closest value, search)
O(h + k) → Kth smallest with early stop
O(log n) → Average case with pruning (balanced tree)
O(n)     → Worst case (skewed tree or must visit all nodes)
```

---

## 🔗 Connections to Other Patterns

### BST → Binary Search (Array)
- Both use divide-and-conquer
- BST: O(h) time, O(1) space (iterative)
- Array: O(log n) time, O(1) space
- **Trade-off:** BST allows O(log n) insert/delete, array doesn't

### BST → Heap
- Both are tree-based priority structures
- BST: In-order sorted, can find kth element
- Heap: Only root is guaranteed (max/min)
- **Use BST when:** Need sorted sequence or range queries
- **Use Heap when:** Only need top element

### BST → DFS on Trees
- In-order traversal is a type of DFS
- BST adds the constraint: left < root < right
- **Use BST techniques when:** Tree has BST property
- **Use general DFS when:** Regular tree without ordering

---

## 📊 Problem Difficulty & Frequency Analysis

### Why These Frequencies?
- **Range Sum (69.5%):** Very practical, common in databases (range queries)
- **BST Iterator (51.9%):** Tests design skills, common in interviews
- **Closest Value (47.0%):** Fundamental binary search application
- **Kth Smallest (32.0%):** Classic problem, but well-known solution

### Interview Preparation Priority
1. **Must Know:** Kth Smallest (teaches in-order)
2. **Important:** BST Iterator (tests design + algorithms)
3. **Good to Know:** Range Sum (teaches pruning)
4. **Nice to Have:** Closest Value (easiest, good warm-up)

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency | Key Pattern |
|---|---------|------------|-----------|-------------|
| 027 | [Range Sum of BST](./027_range_sum_of_bst.md) | EASY | 69.5% | DFS + Pruning |
| 051 | [Binary Search Tree Iterator](./051_binary_search_tree_iterator.md) | MEDIUM | 51.9% | Lazy In-order |
| 060 | [Closest Binary Search Tree Value](./060_closest_binary_search_tree_value.md) | EASY | 47.0% | Binary Search |
| 092 | [Kth Smallest Element in a BST](./092_kth_smallest_element_in_a_bst.md) | MEDIUM | 32.0% | In-order + Counter |

---

## 🎯 Quick Decision Tree

```
Need sorted sequence?
  → Use in-order traversal (Kth Smallest, Iterator)

Need single value?
  → Use binary search path (Closest Value)

Need range/conditional processing?
  → Use DFS with pruning (Range Sum)

Need multiple sequential accesses?
  → Use iterator with stack (BST Iterator)

Need one-time query?
  → Use optimized traversal with early stop (Kth Smallest)
```

---

[← Back to Main](../README.md)
