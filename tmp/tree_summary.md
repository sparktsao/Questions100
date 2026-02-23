# Tree Problems - Comprehensive Analysis




## 📋 Problems in This Category

- [003. Binary Tree Vertical Order](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Tree/003_binary_tree_vertical_order_traversal.md) - `BFS+Column Track`
- [005. Lowest Common Ancestor III](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Tree/005_lowest_common_ancestor_of_a_binary_tree_iii.md) - `DFS+Parent Ptr`
- [007. Binary Tree Right Side View](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Tree/007_binary_tree_right_side_view.md) - `BFS Level-Order`
- [009. Lowest Common Ancestor](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Tree/009_lowest_common_ancestor_of_a_binary_tree.md) - `DFS Recursive`
- [011. Nested List Weight Sum](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Tree/011_nested_list_weight_sum.md) - `DFS+Depth`
- [013. Sum Root to Leaf Numbers](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Tree/013_sum_root_to_leaf_numbers.md) - `DFS Path Track`
- [014. Diameter of Binary Tree](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Tree/014_diameter_of_binary_tree.md) - `DFS Bottom-Up`
- [061. Vertical Order Traversal](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Tree/061_vertical_order_traversal_of_a_binary_tree.md) - `DFS+Sort`
- [066. All Nodes Distance K](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Tree/066_all_nodes_distance_k_in_binary_tree.md) - `BFS+Parent Map`
- [076. Binary Tree Maximum Path Sum](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Tree/076_binary_tree_maximum_path_sum.md) - `DFS+Max Path`

---

## 🎯 Category Overview

**Total Problems:** 10
**Difficulty Range:** Easy → Medium → Hard
**Core Concept:** Binary tree traversal using DFS (recursive/path tracking) vs BFS (level-order/shortest distance)

**🔑 Key Insight:** Choose traversal based on what you need:
- **BFS** → Level information, shortest paths, left-to-right order
- **DFS** → Path information, bottom-up computation, subtree properties

---

## 📊 Problem Progression Map

```
Level 1: Diameter of Binary Tree (#014) - Simple DFS Height Tracking (EASIEST)
    ↓
Level 2: Right Side View (#007) - BFS Level Order
    ↓
Level 3: Nested List Weight Sum (#011) - DFS with Depth Parameter
    ↓
Level 4: Sum Root to Leaf Numbers (#013) - DFS Path Accumulation
    ↓
Level 5: Vertical Order Traversal (#003) - BFS + Column Tracking
    ↓
Level 6: LCA with Parent Pointers (#005) - Two-Pointer on Tree
    ↓
Level 7: LCA without Parent Pointers (#009) - Recursive DFS
    ↓
Level 8: Vertical Traversal with Sorting (#061) - DFS + Multi-Key Sort
    ↓
Level 9: Distance K from Target (#066) - Convert Tree to Graph + BFS
    ↓
Level 10: Maximum Path Sum (#076) - DFS with Global Max (HARDEST)
```

---

## 🔍 The Two Paradigms

### Paradigm A: DFS (Depth-First Search)
**When:** Need path information, subtree properties, bottom-up computation
**Key:** Recursion, process children before parent
**Examples:** #014, #013, #009, #076

```python
def dfs(node):
    if not node:
        return base_case
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node.val, left, right)
```

### Paradigm B: BFS (Breadth-First Search)
**When:** Need level information, shortest paths, left-to-right order
**Key:** Queue, process level by level
**Examples:** #007, #003, #066

```python
from collections import deque
queue = deque([root])
while queue:
    node = queue.popleft()
    process(node)
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)
```

---

## 📖 Problem-by-Problem Analysis

### 1️⃣ **Problem #014: Diameter of Binary Tree** (EASY)

**🎯 Task:** Find longest path between any two nodes
**📥 Input:** Tree root
**📤 Output:** Maximum diameter (number of edges)
**🏷️ Tag:** DFS, Height

#### What Makes This Special?
```
Simplest tree DFS!
Path doesn't have to go through root
Diameter = max(left_height + right_height)
```

#### Algorithm
```python
def diameterOfBinaryTree(root):
    max_diameter = 0

    def height(node):
        nonlocal max_diameter
        if not node:
            return 0

        left_h = height(node.left)
        right_h = height(node.right)

        # Diameter through this node
        max_diameter = max(max_diameter, left_h + right_h)

        # Return height of this subtree
        return 1 + max(left_h, right_h)

    height(root)
    return max_diameter
```

#### Key Insight
> **DFS Pattern:** Calculate subtree properties recursively
> Track global maximum while computing heights

#### Complexity
- **Time:** O(n) - visit each node once
- **Space:** O(h) - recursion stack
- **Why Simplest:** Single DFS pass, simple height calculation

---

### 2️⃣ **Problem #007: Binary Tree Right Side View** (MEDIUM)

**🎯 Task:** Return rightmost node at each level
**📥 Input:** Tree root
**📤 Output:** List of rightmost values
**🏷️ Tag:** BFS, Level Order

#### What Changed from #014?
```diff
+ Need level information (not just subtree)
+ BFS instead of DFS
+ Track rightmost per level
```

#### Algorithm
```python
def rightSideView(root):
    if not root:
        return []

    from collections import deque
    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # Rightmost node at this level
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result
```

#### Why BFS?
```
DFS: No natural way to know which is rightmost
BFS: Process level by level, last in level = rightmost
```

#### Key Insight
> **BFS for Levels:** When you need level information, use BFS
> Track level size to identify last node

#### Complexity
- **Time:** O(n) - visit all nodes
- **Space:** O(w) - max width of tree in queue
- **Why BFS:** Level-order naturally gives rightmost

---

### 3️⃣ **Problem #011: Nested List Weight Sum** (MEDIUM)

**🎯 Task:** Sum integers weighted by depth
**📥 Input:** Nested list structure
**📤 Output:** Weighted sum
**🏷️ Tag:** DFS, Depth Parameter

#### What's New?
```
Not binary tree, but nested structure
Must track current depth
Multiply value by depth
```

#### Algorithm
```python
def depthSum(nestedList):
    def dfs(nested_list, depth):
        total = 0
        for item in nested_list:
            if item.isInteger():
                total += item.getInteger() * depth
            else:
                # Recurse deeper with depth + 1
                total += dfs(item.getList(), depth + 1)
        return total

    return dfs(nestedList, 1)
```

#### Depth Tracking Pattern
```python
def dfs(node, depth):
    # Use depth in calculation
    result = node.val * depth

    # Pass depth + 1 to children
    left_result = dfs(node.left, depth + 1)
    right_result = dfs(node.right, depth + 1)

    return result + left_result + right_result
```

#### Key Insight
> **Depth as Parameter:** Pass depth down recursively
> Each level increments depth by 1

#### Complexity
- **Time:** O(n) - visit each element
- **Space:** O(d) - recursion depth
- **Why DFS:** Natural depth tracking through recursion

---

### 4️⃣ **Problem #013: Sum Root to Leaf Numbers** (MEDIUM)

**🎯 Task:** Sum all root-to-leaf path numbers
**📥 Input:** Tree root (digits 0-9)
**📤 Output:** Sum of all path numbers
**🏷️ Tag:** DFS, Path Accumulation

#### Path Accumulation!
```
Path [1,2,3] represents number 123
Must accumulate as we go down
Sum all complete paths
```

#### Algorithm
```python
def sumNumbers(root):
    def dfs(node, current_num):
        if not node:
            return 0

        # Accumulate: shift and add digit
        current_num = current_num * 10 + node.val

        # Leaf: return accumulated number
        if not node.left and not node.right:
            return current_num

        # Non-leaf: sum both paths
        return dfs(node.left, current_num) + dfs(node.right, current_num)

    return dfs(root, 0)
```

#### Example
```
Tree:    1
        / \
       2   3
      /
     4

Paths:
1 → 2 → 4: 124
1 → 3:     13
Sum = 124 + 13 = 137
```

#### Key Insight
> **Path Accumulation:** Build value as you traverse
> Leaf nodes return completed path value

#### Complexity
- **Time:** O(n) - visit all nodes
- **Space:** O(h) - recursion depth
- **Why DFS:** Need complete root-to-leaf paths

---

### 5️⃣ **Problem #003: Binary Tree Vertical Order Traversal** (MEDIUM)

**🎯 Task:** Group nodes by vertical column
**📥 Input:** Tree root
**📤 Output:** Lists grouped by column
**🏷️ Tag:** BFS, Column Tracking

#### Column Coordinate System
```
Root at column 0
Left child: column - 1
Right child: column + 1
```

#### Algorithm
```python
def verticalOrder(root):
    if not root:
        return []

    from collections import defaultdict, deque
    column_table = defaultdict(list)
    queue = deque([(root, 0)])  # (node, column)

    while queue:
        node, col = queue.popleft()
        column_table[col].append(node.val)

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    # Sort by column index
    return [column_table[col] for col in sorted(column_table.keys())]
```

#### Why BFS Not DFS?
```
BFS: Top-to-bottom order naturally (level by level)
DFS: Would need extra sorting by row within column
```

#### Key Insight
> **BFS + Coordinates:** Track (node, column) pairs
> BFS ensures top-to-bottom within each column

#### Complexity
- **Time:** O(n log n) - sorting columns
- **Space:** O(n) - queue + hash table
- **Why BFS:** Natural top-to-bottom ordering

---

### 6️⃣ **Problem #005: Lowest Common Ancestor III** (MEDIUM)

**🎯 Task:** Find LCA when nodes have parent pointers
**📥 Input:** Two nodes with .parent attribute
**📤 Output:** LCA node
**🏷️ Tag:** Two-Pointer, Parent Pointers

#### Like Linked List Intersection!
```
Use parent pointers like next pointers
Find where paths to root intersect
```

#### Algorithm
```python
def lowestCommonAncestor(p, q):
    # Like finding linked list intersection
    p1, p2 = p, q

    while p1 != p2:
        # Move up, switch to other path when reach None
        p1 = p1.parent if p1.parent else q
        p2 = p2.parent if p2.parent else p

    return p1
```

#### Why This Works?
```
Path A: p → ... → LCA → ... → root
Path B: q → ... → LCA → ... → root

After reaching root, switch paths:
Both will meet at LCA after same total distance
```

#### Key Insight
> **Tree as Linked List:** Parent pointers = linked list
> Use two-pointer technique from linked lists

#### Complexity
- **Time:** O(h) - height of tree
- **Space:** O(1) - no extra space
- **Why Clever:** Reuses linked list pattern

---

### 7️⃣ **Problem #009: Lowest Common Ancestor** (MEDIUM)

**🎯 Task:** Find LCA WITHOUT parent pointers
**📥 Input:** Root + two nodes p and q
**📤 Output:** LCA node
**🏷️ Tag:** DFS, Recursive

#### No Parent Pointers!
```
Must search from root
Recursive DFS approach
```

#### Algorithm
```python
def lowestCommonAncestor(root, p, q):
    # Base cases
    if not root or root == p or root == q:
        return root

    # Search in subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # Both found in different subtrees → current is LCA
    if left and right:
        return root

    # Return whichever side found something
    return left if left else right
```

#### The Logic
```
Case 1: Both in left → LCA in left
Case 2: Both in right → LCA in right
Case 3: One in each → Current node is LCA!
```

#### Key Insight
> **Post-Order Logic:** Process children first
> Current node is LCA if children in different subtrees

#### Complexity
- **Time:** O(n) - may visit all nodes
- **Space:** O(h) - recursion stack
- **Why DFS:** Need to explore all paths

---

### 8️⃣ **Problem #061: Vertical Order Traversal** (HARD)

**🎯 Task:** Vertical order with sorting at same (row, col)
**📥 Input:** Tree root
**📤 Output:** Column lists with sorting
**🏷️ Tag:** DFS, Multi-Key Sort

#### More Complex Than #003!
```diff
+ Must sort by VALUE when at same (row, col)
+ Track BOTH row and column
+ DFS + sort vs BFS
```

#### Algorithm
```python
def verticalTraversal(root):
    nodes = []  # (col, row, val)

    def dfs(node, row, col):
        if not node:
            return
        nodes.append((col, row, node.val))
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)

    # Sort by col, then row, then value
    nodes.sort()

    # Group by column
    result = []
    prev_col = float('-inf')
    for col, row, val in nodes:
        if col != prev_col:
            result.append([])
            prev_col = col
        result[-1].append(val)

    return result
```

#### Why DFS Here?
```
DFS collects all, then sort
BFS would need complex tie-breaking during traversal
Simpler to collect all + sort
```

#### Key Insight
> **DFS + Sort:** When need complex sorting, collect then sort
> Multi-key sort: (column, row, value)

#### Complexity
- **Time:** O(n log n) - sorting
- **Space:** O(n) - storing all nodes
- **Why HARD:** Complex sorting requirements

---

### 9️⃣ **Problem #066: All Nodes Distance K** (MEDIUM)

**🎯 Task:** Find all nodes at distance k from target
**📥 Input:** Root + target node + distance k
**📤 Output:** List of node values
**🏷️ Tag:** BFS, Parent Pointers, Graph Conversion

#### Tree → Graph!
```
Build parent pointers first
Then BFS from target (can go up or down)
Treat as undirected graph
```

#### Algorithm
```python
def distanceK(root, target, k):
    from collections import deque

    # Build parent map
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

        # Check all 3 neighbors: left, right, parent
        for neighbor in [node.left, node.right, parent[node]]:
            if neighbor and neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))

    return result
```

#### Two-Phase Approach
```
Phase 1: DFS to build parent pointers
Phase 2: BFS from target treating as graph
```

#### Key Insight
> **Tree to Graph:** Add parent pointers → undirected graph
> BFS for shortest distance (k steps)

#### Complexity
- **Time:** O(n) - DFS + BFS
- **Space:** O(n) - parent map + queue
- **Why Complex:** Must traverse in all directions

---

### 🔟 **Problem #076: Binary Tree Maximum Path Sum** (HARD)

**🎯 Task:** Find path with maximum sum (any path, not root-to-leaf)
**📥 Input:** Tree root (can have negative values)
**📤 Output:** Maximum path sum
**🏷️ Tag:** DFS, Global Max

#### The Hardest!
```
Path can start/end anywhere
May have negative nodes (ignore them)
Return single path, but track double path
```

#### Algorithm
```python
def maxPathSum(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum

        if not node:
            return 0

        # Get max from children (ignore negative)
        left = max(0, dfs(node.left))
        right = max(0, dfs(node.right))

        # Path THROUGH this node (can use both children)
        current_path = node.val + left + right
        max_sum = max(max_sum, current_path)

        # Return single path (can only use ONE child)
        return node.val + max(left, right)

    dfs(root)
    return max_sum
```

#### The Trick
```
Two different values at each node:
1. Path THROUGH node = val + left + right (update global max)
2. Path FROM node = val + max(left, right) (return to parent)

Parent can only extend ONE branch, not both!
```

#### Example
```
Tree:     10
         /  \
        2   10
       / \    \
      20  1   -25
                 \
                  6

Max path: 20 → 2 → 10 → 10 = 42
(Not through root initially!)
```

#### Key Insight
> **Two Values:** Track through-path (global) vs from-path (return)
> Ignore negative contributions (max with 0)

#### Complexity
- **Time:** O(n) - visit each node once
- **Space:** O(h) - recursion stack
- **Why HARDEST:** Two simultaneous calculations, global state

---

## 🔄 Algorithm Relationships

### Can We Reuse Previous Solutions?

| From → To | Can Modify? | What Changes? |
|-----------|-------------|---------------|
| #014 → #076 | ✅ Partial | Add global max tracking, handle negatives |
| #007 → #003 | ✅ YES | Add column tracking to BFS |
| #003 → #061 | ❌ NO | BFS → DFS + complex sorting |
| #005 → #009 | ❌ NO | Two-pointer → Recursive DFS |
| #009 → #066 | ✅ Partial | Add parent building + BFS |
| #011 → #013 | ✅ YES | Similar depth/accumulation pattern |

---

## 💡 Key Learning Insights

### 1. **BFS vs DFS Decision Tree**

```
Need level information? → BFS (#007, #003)
Need path information? → DFS (#013, #076)
Need distance? → BFS (#066)
Need subtree property? → DFS (#014, #076)
```

### 2. **DFS Return Value Patterns**

**Pattern A: Return Single Value**
```python
def dfs(node):
    if not node:
        return 0
    left = dfs(node.left)
    right = dfs(node.right)
    return node.val + max(left, right)
```

**Pattern B: Return + Track Global**
```python
max_result = init
def dfs(node):
    nonlocal max_result
    if not node:
        return base
    left = dfs(node.left)
    right = dfs(node.right)
    max_result = max(max_result, combine(left, right))
    return something_else
```

**Pattern C: Accumulate Parameter**
```python
def dfs(node, accumulated):
    if not node:
        return base
    accumulated = update(accumulated, node.val)
    if is_leaf(node):
        return accumulated
    return dfs(left, accumulated) + dfs(right, accumulated)
```

### 3. **BFS Level-Order Template**

```python
from collections import deque
queue = deque([root])

while queue:
    level_size = len(queue)  # CRITICAL for level tracking

    for i in range(level_size):
        node = queue.popleft()

        # Process node
        if i == level_size - 1:  # Last in level
            # Special handling for rightmost

        # Add children
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```

### 4. **Parent Pointer Building**

```python
parent = {}
def build_parent(node, par=None):
    if not node:
        return
    parent[node] = par
    build_parent(node.left, node)
    build_parent(node.right, node)

build_parent(root)
# Now can traverse upward!
```

---

## 🎨 Visual Comparison Table

| Problem | Traversal | Key Technique | Data Structure | Complexity |
|---------|-----------|---------------|----------------|------------|
| #014 | DFS | Height tracking | None | O(n), O(h) |
| #007 | BFS | Level rightmost | Queue | O(n), O(w) |
| #011 | DFS | Depth parameter | None | O(n), O(d) |
| #013 | DFS | Path accumulation | None | O(n), O(h) |
| #003 | BFS | Column tracking | Queue + Hash | O(n log n), O(n) |
| #005 | Two-Ptr | Parent pointers | None | O(h), O(1) |
| #009 | DFS | Recursive search | None | O(n), O(h) |
| #061 | DFS | Coordinate sort | Array | O(n log n), O(n) |
| #066 | BFS | Tree to graph | Parent map + Queue | O(n), O(n) |
| #076 | DFS | Global max | None | O(n), O(h) |

---

## 🚀 Recommended Study Order

1. **Start DFS Basics:** #014 (Diameter)
   - Master simple height tracking
   - Understand post-order processing

2. **Learn BFS Pattern:** #007 (Right Side View)
   - Level-order traversal
   - Track level boundaries

3. **DFS With Parameters:** #011 (Nested Weight Sum)
   - Pass depth down
   - Accumulate results

4. **Path Accumulation:** #013 (Sum Root to Leaf)
   - Build value as you traverse
   - Return at leaves

5. **BFS With Tracking:** #003 (Vertical Order)
   - Add coordinates to BFS
   - Use hash table for grouping

6. **Special Patterns:** #005 (LCA with Parents)
   - Tree as linked list
   - Two-pointer technique

7. **Recursive LCA:** #009 (LCA without Parents)
   - Post-order logic
   - Split search

8. **Complex Sorting:** #061 (Vertical with Sort)
   - DFS + collect all
   - Multi-key sorting

9. **Graph Conversion:** #066 (Distance K)
   - Build parent map
   - BFS in all directions

10. **Ultimate Challenge:** #076 (Max Path Sum)
    - Dual calculations
    - Global vs local

---

## 🎯 Universal Templates

### Template 1: Basic DFS
```python
def dfs(node):
    if not node:
        return base_case

    left_result = dfs(node.left)
    right_result = dfs(node.right)

    return combine(node.val, left_result, right_result)
```

### Template 2: BFS Level-Order
```python
from collections import deque
queue = deque([root])

while queue:
    level_size = len(queue)
    for i in range(level_size):
        node = queue.popleft()
        # Process
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```

### Template 3: DFS with Global State
```python
result = init_value

def dfs(node):
    nonlocal result
    if not node:
        return base

    left = dfs(node.left)
    right = dfs(node.right)

    # Update global
    result = update(result, left, right, node.val)

    # Return local
    return local_value
```

---

## 📝 Interview Tips

### Red Flags (Common Mistakes)

1. **#014:** Forgetting to track global max while computing heights
2. **#007:** Not tracking level size (processes wrong nodes)
3. **#013:** Not handling leaf nodes separately (adds extra zeros)
4. **#003:** Using DFS (loses top-to-bottom ordering)
5. **#009:** Returning left/right unconditionally (loses LCA)
6. **#076:** Returning through-path instead of from-path (parent can't extend both)

### When to Use Each Traversal?

**Use BFS when:**
- Need level information (#007)
- Need shortest distance (#066)
- Need left-to-right order (#003)
- Parent and child treated differently

**Use DFS when:**
- Need path information (#013)
- Need subtree properties (#014)
- Bottom-up computation (#076)
- Post-order processing (#009)

---

## 💪 Practice Progression

```
Week 1: Master DFS
- Day 1-2: #014 (height + diameter)
- Day 3-4: #011 (depth parameter)
- Day 5-6: #013 (path accumulation)
- Day 7: Compare three DFS patterns

Week 2: Master BFS
- Day 1-2: #007 (level rightmost)
- Day 3-4: #003 (column tracking)
- Day 5-6: Write BFS template from memory
- Day 7: When BFS vs DFS?

Week 3: Special Patterns
- Day 1-2: #005 (parent pointers)
- Day 3-4: #009 (recursive LCA)
- Day 5-6: #061 (DFS + sort)
- Day 7: #066 (tree to graph)

Week 4: Master Complexity
- Day 1-4: #076 (maximum path sum)
- Day 5: Solve all 10 from scratch
- Day 6-7: Identify BFS vs DFS in new problems
```

---

**Summary:** Tree problems split into BFS (for level information, shortest paths) and DFS (for path information, subtree properties). Start with simple DFS height tracking (#014), learn BFS level-order (#007), practice parameter passing (#011, #013), master BFS with tracking (#003), understand LCA patterns (#005, #009), handle complex sorting (#061), convert tree to graph (#066), and finally conquer the hardest pattern of dual calculations with global state (#076). The key decision is BFS vs DFS: use BFS when you need level/distance information, use DFS when you need paths or bottom-up computation.
