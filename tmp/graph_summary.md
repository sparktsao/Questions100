# Graph Problems - Comprehensive Analysis




## 📋 Problems in This Category

- [025. Clone Graph](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Graph-DFS-BFS/025_clone_graph.md) - `DFS+Clone`
- [031. Shortest Path in Binary Matrix](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Graph-DFS-BFS/031_shortest_path_in_binary_matrix.md) - `BFS Shortest`
- [036. Making A Large Island](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Graph-DFS-BFS/036_making_a_large_island.md) - `DFS+Union-Find`
- [038. Accounts Merge](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Graph-DFS-BFS/038_accounts_merge.md) - `Union-Find`
- [053. Robot Room Cleaner](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Graph-DFS-BFS/053_robot_room_cleaner.md) - `DFS+Backtrack`
- [063. Course Schedule](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Graph-DFS-BFS/063_course_schedule.md) - `DFS Cycle Detect`
- [070. Swim in Rising Water](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Graph-DFS-BFS/070_swim_in_rising_water.md) - `Dijkstra`
- [081. Word Ladder](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Graph-DFS-BFS/081_word_ladder.md) - `BFS Transform`
- [086. Shortest Path in Hidden Grid](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Graph-DFS-BFS/086_shortest_path_in_a_hidden_grid.md) - `DFS+BFS Hybrid`

---

## 🎯 Category Overview

**Total Problems:** 9
**Difficulty Range:** Medium → Hard
**Core Concept:** Graph traversal using DFS (cycle detection, exploration) vs BFS (shortest paths)

**🔑 Key Insight:** Choose algorithm based on goal:
- **DFS** → Cycle detection, exploration, backtracking
- **BFS** → Shortest paths (unweighted graphs)
- **Union-Find** → Connected components, merging
- **Dijkstra** → Shortest paths (weighted graphs)

---

## 📊 Problem Progression Map

```
Level 1: Clone Graph (#025) - Basic DFS/BFS with Hash Map
    ↓
Level 2: Shortest Path in Binary Matrix (#031) - BFS Shortest Path
    ↓
Level 3: Accounts Merge (#038) - Union-Find / DFS Components
    ↓
Level 4: Course Schedule (#063) - Cycle Detection (3-State DFS)
    ↓
Level 5: Word Ladder (#081) - BFS Word Transformation (HARD)
    ↓
Level 6: Hidden Grid Shortest Path (#086) - DFS Explore + BFS Path
    ↓
Level 7: Robot Room Cleaner (#053) - DFS Backtracking (Blind)
    ↓
Level 8: Making Large Island (#036) - DFS Labeling + Merging
    ↓
Level 9: Swim in Rising Water (#070) - Dijkstra/Binary Search (HARDEST)
```

---

## 🔍 The Algorithm Types

### Type A: BFS (Shortest Path in Unweighted Graphs)
**When:** Find shortest distance
**Examples:** #031, #081, #086 (phase 2)

### Type B: DFS (Exploration & Cycle Detection)
**When:** Explore all paths, detect cycles, backtrack
**Examples:** #025, #053, #063, #086 (phase 1)

### Type C: Union-Find (Connected Components)
**When:** Merge groups, check connectivity
**Examples:** #038, #070

### Type D: Dijkstra (Shortest Path in Weighted Graphs)
**When:** Weighted edges, find minimum cost
**Examples:** #070

---

## 📖 Problem-by-Problem Analysis

### 1️⃣ **Problem #025: Clone Graph** (MEDIUM)

**🎯 Task:** Deep copy undirected graph
**📥 Input:** Node reference
**📤 Output:** Cloned graph root
**🏷️ Tag:** DFS, Hash Map

#### Algorithm
```python
def cloneGraph(node):
    if not node:
        return None

    cloned = {}  # old_node → new_node

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

#### Key Insight
> **Hash Map Prevents Cycles:** Track cloned nodes to avoid infinite loops

#### Complexity
- **Time:** O(N + E) - visit all nodes and edges
- **Space:** O(N) - hash map + recursion

---

### 2️⃣ **Problem #031: Shortest Path in Binary Matrix** (MEDIUM)

**🎯 Task:** Find shortest clear path (8-directional)
**📥 Input:** Binary matrix
**📤 Output:** Path length or -1
**🏷️ Tag:** BFS, Grid

#### Algorithm
```python
def shortestPathBinaryMatrix(grid):
    from collections import deque

    n = len(grid)
    if grid[0][0] == 1 or grid[n-1][n-1] == 1:
        return -1

    # 8 directions
    directions = [(-1,-1), (-1,0), (-1,1), (0,-1),
                  (0,1), (1,-1), (1,0), (1,1)]

    queue = deque([(0, 0, 1)])  # (row, col, length)
    grid[0][0] = 1  # Mark visited

    while queue:
        row, col, length = queue.popleft()

        if row == n-1 and col == n-1:
            return length

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                grid[nr][nc] = 1  # Mark visited
                queue.append((nr, nc, length + 1))

    return -1
```

#### Key Insight
> **BFS for Shortest:** BFS guarantees shortest path in unweighted graphs

#### Complexity
- **Time:** O(n²) - visit each cell once
- **Space:** O(n²) - queue size

---

### 3️⃣ **Problem #038: Accounts Merge** (MEDIUM)

**🎯 Task:** Merge accounts by shared emails
**📥 Input:** List of accounts
**📤 Output:** Merged accounts
**🏷️ Tag:** Union-Find, DFS

#### Algorithm (Union-Find)
```python
def accountsMerge(accounts):
    from collections import defaultdict

    parent = {}

    def find(x):
        if x not in parent:
            parent[x] = x
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    email_to_name = {}

    # Build union-find
    for account in accounts:
        name = account[0]
        first_email = account[1]
        for email in account[1:]:
            email_to_name[email] = name
            union(first_email, email)

    # Group by root
    components = defaultdict(list)
    for email in email_to_name:
        components[find(email)].append(email)

    # Build result
    return [[email_to_name[emails[0]]] + sorted(emails)
            for emails in components.values()]
```

#### Key Insight
> **Union-Find for Transitivity:** Efficiently handles A→B, B→C means A→C

#### Complexity
- **Time:** O(N×K×α(N)) - nearly constant per operation
- **Space:** O(N×K) - email storage

---

### 4️⃣ **Problem #063: Course Schedule** (MEDIUM)

**🎯 Task:** Detect cycles in directed graph
**📥 Input:** Courses + prerequisites
**📤 Output:** Boolean (can finish all?)
**🏷️ Tag:** Cycle Detection, Topological Sort

#### Algorithm (3-State DFS)
```python
def canFinish(numCourses, prerequisites):
    from collections import defaultdict

    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # States: 0=unvisited, 1=visiting, 2=visited
    state = [0] * numCourses

    def has_cycle(course):
        if state[course] == 1:  # Visiting → cycle!
            return True
        if state[course] == 2:  # Already done
            return False

        state[course] = 1  # Mark visiting

        for prereq in graph[course]:
            if has_cycle(prereq):
                return True

        state[course] = 2  # Mark visited
        return False

    return not any(has_cycle(c) for c in range(numCourses))
```

#### The 3 States
```
0 (White): Never visited
1 (Gray): Currently visiting (on recursion stack)
2 (Black): Fully explored

Cycle exists if we reach a GRAY node!
```

#### Key Insight
> **3-State Pattern:** Distinguishes "visiting" from "visited" for cycle detection

#### Complexity
- **Time:** O(V + E) - visit all vertices and edges
- **Space:** O(V + E) - graph + state array

---

### 5️⃣ **Problem #081: Word Ladder** (HARD)

**🎯 Task:** Shortest word transformation sequence
**📥 Input:** Start word, end word, word list
**📤 Output:** Shortest length or 0
**🏷️ Tag:** BFS, String

#### Algorithm
```python
def ladderLength(beginWord, endWord, wordList):
    from collections import deque

    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque([(beginWord, 1)])
    visited = {beginWord}

    while queue:
        word, length = queue.popleft()

        if word == endWord:
            return length

        # Try all one-letter changes
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]

                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))

    return 0
```

#### Key Insight
> **BFS on Implicit Graph:** Words are nodes, one-letter changes are edges

#### Complexity
- **Time:** O(M²×N) - M = word length, N = word count
- **Space:** O(M×N) - queue + visited

---

### 6️⃣ **Problem #086: Shortest Path in Hidden Grid** (MEDIUM)

**🎯 Task:** Find shortest path without knowing grid
**📥 Input:** GridMaster API
**📤 Output:** Shortest distance
**🏷️ Tag:** DFS Explore + BFS Path

#### Two-Phase Algorithm
```python
def findShortestPath(master):
    directions = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
    opposite = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

    grid = {}
    target = None

    # Phase 1: DFS to map grid
    def dfs(row, col):
        nonlocal target
        if master.isTarget():
            target = (row, col)
        grid[(row, col)] = True

        for dir, (dr, dc) in directions.items():
            nr, nc = row + dr, col + dc
            if (nr, nc) in grid:
                continue
            if master.canMove(dir):
                master.move(dir)
                dfs(nr, nc)
                master.move(opposite[dir])
            else:
                grid[(nr, nc)] = False

    dfs(0, 0)

    if target is None:
        return -1

    # Phase 2: BFS to find shortest path
    from collections import deque
    queue = deque([(0, 0, 0)])
    visited = {(0, 0)}

    while queue:
        row, col, dist = queue.popleft()
        if (row, col) == target:
            return dist

        for dr, dc in directions.values():
            nr, nc = row + dr, col + dc
            if (nr, nc) in grid and grid[(nr, nc)] and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

    return -1
```

#### Key Insight
> **Two Phases:** DFS explores unknown, BFS finds optimal path on known

#### Complexity
- **Time:** O(m×n) - explore + pathfind
- **Space:** O(m×n) - grid storage

---

### 7️⃣ **Problem #053: Robot Room Cleaner** (HARD)

**🎯 Task:** Clean entire room without map
**📥 Input:** Robot API
**📤 Output:** Clean all cells
**🏷️ Tag:** DFS, Backtracking

#### Algorithm
```python
def cleanRoom(robot):
    directions = [(-1,0), (0,1), (1,0), (0,-1)]  # URDL
    visited = set()

    def go_back():
        robot.turnRight()
        robot.turnRight()
        robot.move()
        robot.turnRight()
        robot.turnRight()

    def dfs(cell=(0,0), d=0):
        visited.add(cell)
        robot.clean()

        # Try all 4 directions
        for i in range(4):
            new_d = (d + i) % 4
            new_cell = (cell[0] + directions[new_d][0],
                       cell[1] + directions[new_d][1])

            if new_cell not in visited and robot.move():
                dfs(new_cell, new_d)
                go_back()  # Backtrack

            robot.turnRight()  # Turn to next direction

    dfs()
```

#### Key Insight
> **Backtracking Required:** Must return to explore other paths

#### Complexity
- **Time:** O(N - M) - visit accessible cells
- **Space:** O(N - M) - visited set

---

### 8️⃣ **Problem #036: Making a Large Island** (HARD)

**🎯 Task:** Max island size after changing one 0 to 1
**📥 Input:** Binary matrix
**📤 Output:** Largest possible island
**🏷️ Tag:** DFS, Island Labeling

#### Two-Phase Algorithm
```python
def largestIsland(grid):
    n = len(grid)
    island_id = 2
    island_sizes = {}

    def dfs(r, c, island_id):
        if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
            return 0
        grid[r][c] = island_id
        size = 1
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            size += dfs(r + dr, c + dc, island_id)
        return size

    # Phase 1: Label islands
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                island_sizes[island_id] = dfs(r, c, island_id)
                island_id += 1

    if not island_sizes:
        return 1
    max_size = max(island_sizes.values())

    # Phase 2: Try flipping each 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                neighbors = set()
                for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                        neighbors.add(grid[nr][nc])

                size = 1 + sum(island_sizes[id] for id in neighbors)
                max_size = max(max_size, size)

    return max_size
```

#### Key Insight
> **Label First:** DFS labels islands, then check merges in O(1)

#### Complexity
- **Time:** O(n²) - label + check each 0
- **Space:** O(n²) - modified grid

---

### 9️⃣ **Problem #070: Swim in Rising Water** (HARD)

**🎯 Task:** Minimum time to reach destination
**📥 Input:** Elevation grid
**📤 Output:** Minimum max elevation
**🏷️ Tag:** Dijkstra, Binary Search

#### Algorithm (Dijkstra)
```python
def swimInWater(grid):
    import heapq
    n = len(grid)
    visited = set()

    heap = [(grid[0][0], 0, 0)]  # (max_elev, row, col)
    directions = [(0,1), (1,0), (0,-1), (-1,0)]

    while heap:
        max_elev, row, col = heapq.heappop(heap)

        if row == n-1 and col == n-1:
            return max_elev

        if (row, col) in visited:
            continue
        visited.add((row, col))

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited:
                new_max = max(max_elev, grid[nr][nc])
                heapq.heappush(heap, (new_max, nr, nc))

    return -1
```

#### Key Insight
> **Dijkstra Variant:** Track maximum elevation on path instead of sum

#### Complexity
- **Time:** O(n² log n) - priority queue operations
- **Space:** O(n²) - heap + visited

---

## 🔄 Algorithm Selection Guide

| Goal | Algorithm | Problems |
|------|-----------|----------|
| Shortest path (unweighted) | BFS | #031, #081, #086 |
| Cycle detection | 3-State DFS | #063 |
| Graph cloning | DFS + Hash Map | #025 |
| Connected components | Union-Find / DFS | #038, #036 |
| Blind exploration | DFS + Backtracking | #053, #086 |
| Shortest path (weighted) | Dijkstra | #070 |

---

## 💡 Key Learning Insights

### 1. **BFS for Shortest Paths**
```python
from collections import deque
queue = deque([(start, 0)])  # (node, distance)
visited = {start}

while queue:
    node, dist = queue.popleft()
    if is_target(node):
        return dist
    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append((neighbor, dist + 1))
```

### 2. **3-State DFS for Cycle Detection**
```python
# 0=unvisited, 1=visiting, 2=visited
state = [0] * n

def dfs(node):
    if state[node] == 1:  # Cycle!
        return True
    if state[node] == 2:
        return False

    state[node] = 1
    for neighbor in graph[node]:
        if dfs(neighbor):
            return True
    state[node] = 2
    return False
```

### 3. **Union-Find Template**
```python
parent = {}

def find(x):
    if x not in parent:
        parent[x] = x
    if parent[x] != x:
        parent[x] = find(parent[x])  # Path compression
    return parent[x]

def union(x, y):
    root_x, root_y = find(x), find(y)
    if root_x != root_y:
        parent[root_x] = root_y
```

### 4. **Dijkstra Template**
```python
import heapq
heap = [(0, start)]  # (cost, node)
visited = set()

while heap:
    cost, node = heapq.heappop(heap)
    if node in visited:
        continue
    visited.add(node)

    if is_target(node):
        return cost

    for neighbor, edge_cost in get_neighbors(node):
        if neighbor not in visited:
            heapq.heappush(heap, (cost + edge_cost, neighbor))
```

---

## 🎨 Visual Comparison Table

| Problem | Algorithm | Key Technique | Complexity |
|---------|-----------|---------------|------------|
| #025 | DFS | Hash map for clones | O(N+E) |
| #031 | BFS | 8-directional grid | O(n²) |
| #038 | Union-Find | Email connectivity | O(N×K×α(N)) |
| #063 | DFS | 3-state cycle detection | O(V+E) |
| #081 | BFS | Implicit word graph | O(M²×N) |
| #086 | DFS+BFS | Explore then pathfind | O(m×n) |
| #053 | DFS | Backtracking | O(N-M) |
| #036 | DFS | Island labeling | O(n²) |
| #070 | Dijkstra | Min-max path | O(n² log n) |

---

## 🚀 Recommended Study Order

1. **Basic Graph Traversal:** #025 (Clone)
2. **BFS Shortest Path:** #031 (Binary Matrix)
3. **Union-Find:** #038 (Accounts Merge)
4. **Cycle Detection:** #063 (Course Schedule)
5. **Implicit Graphs:** #081 (Word Ladder)
6. **Two-Phase:** #086 (Hidden Grid)
7. **Backtracking:** #053 (Robot Cleaner)
8. **Island Problems:** #036 (Large Island)
9. **Dijkstra:** #070 (Swim in Water)

---

**Summary:** Graph problems require choosing the right algorithm: BFS for shortest paths (#031, #081), DFS for exploration (#025, #053), 3-state DFS for cycles (#063), Union-Find for components (#038), and Dijkstra for weighted graphs (#070). Master BFS template for unweighted shortest paths, understand 3-state cycle detection, learn Union-Find for connectivity, and practice two-phase approaches (DFS explore + BFS pathfind in #086). The key is recognizing problem type: shortest path → BFS, cycles → DFS with states, merging → Union-Find, weighted → Dijkstra.
