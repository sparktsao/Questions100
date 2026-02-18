# Graph DFS BFS - Comprehensive Guide

## DFS for Paths & Cycles, BFS for Shortest Distance

---

## 🎯 Overview

**Total Problems:** 9
**Difficulty:** Easy (0) • Medium (5) • Hard (4)

**Core Concept:**
DFS (stack/recursion) for connectivity & cycles, BFS (queue) for shortest paths

**Key Insight:**
Always need visited set. DFS for deep exploration, BFS for level-by-level.

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: DFS with Visited Set (Connected Components, Cycle Detection)
### Pattern 2: BFS for Shortest Path (Unweighted)
### Pattern 3: Union-Find for Connected Components
### Pattern 4: Topological Sort (DFS or BFS)


---

## 🎓 Learning Path

Clone Graph → Course Schedule → Word Ladder → Accounts Merge

---

## ⚠️ Common Pitfalls

1. Forgetting visited set 2. Not building adjacency list 3. Modifying during iteration 4. Infinite loops

---

## ✅ Testing Strategy

Test: single node, disconnected, cycle, DAG, empty

---

## 💡 Templates & Code Patterns


```python
# DFS
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)

# BFS
from collections import deque
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```


---

## 💎 Mastery Tips

Build adjacency list first. Always use visited. DFS=deep, BFS=level.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 025 | [Clone Graph](./025_clone_graph.md) | MEDIUM | 71.4% |
| 031 | [Shortest Path in Binary Matrix](./031_shortest_path_in_binary_matrix.md) | MEDIUM | 67.4% |
| 036 | [Making A Large Island](./036_making_a_large_island.md) | HARD | 65.0% |
| 038 | [Accounts Merge](./038_accounts_merge.md) | MEDIUM | 62.4% |
| 053 | [Robot Room Cleaner](./053_robot_room_cleaner.md) | HARD | 51.9% |
| 063 | [Course Schedule](./063_course_schedule.md) | MEDIUM | 47.0% |
| 070 | [Swim in Rising Water](./070_swim_in_rising_water.md) | HARD | 40.7% |
| 081 | [Word Ladder](./081_word_ladder.md) | HARD | 40.7% |
| 086 | [Shortest Path in a Hidden Grid](./086_shortest_path_in_a_hidden_grid.md) | MEDIUM | 32.0% |

---

[← Back to Main](../README.md)
