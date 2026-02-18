# 063. Course Schedule

**Difficulty:** MEDIUM
**Frequency:** 47.0%
**Acceptance Rate:** 49.2%
**LeetCode Link:** [Course Schedule](https://leetcode.com/problems/course-schedule)

---

## Problem Description

There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`.

For example, the pair `[0, 1]`, indicates that to take course `0` you have to first take course `1`.

Return `true` if you can finish all courses. Otherwise, return `false`.

**Constraints:**
- 1 <= numCourses <= 2000
- 0 <= prerequisites.length <= 5000
- prerequisites[i].length == 2
- 0 <= ai, bi < numCourses
- All the pairs prerequisites[i] are unique

---

## Examples

### Example 1
**Input:** `numCourses = 2, prerequisites = [[1,0]]`
**Output:** `true`
**Explanation:** Take course 0, then course 1

### Example 2
**Input:** `numCourses = 2, prerequisites = [[1,0],[0,1]]`
**Output:** `false`
**Explanation:** Circular dependency - impossible

### Example 3
**Input:** `numCourses = 3, prerequisites = [[1,0],[2,1]]`
**Output:** `true`
**Explanation:** Take 0, then 1, then 2

### Example 4
**Input:** `numCourses = 4, prerequisites = []`
**Output:** `true`
**Explanation:** No prerequisites - all can be taken

---

## Optimal Solution

### Implementation

```python
def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    """
    Cycle detection using DFS with three states.

    Time: O(V + E), Space: O(V + E)
    """
    from collections import defaultdict

    # Build adjacency list
    graph = defaultdict(list)
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    # 0 = unvisited, 1 = visiting, 2 = visited
    state = [0] * numCourses

    def has_cycle(course):
        if state[course] == 1:  # Currently visiting - cycle!
            return True
        if state[course] == 2:  # Already fully explored
            return False

        # Mark as visiting
        state[course] = 1

        # Check all prerequisites
        for prereq in graph[course]:
            if has_cycle(prereq):
                return True

        # Mark as visited
        state[course] = 2
        return False

    # Check each course
    for course in range(numCourses):
        if has_cycle(course):
            return False

    return True
```

### Complexity Analysis

**Time: O(V + E) - visit vertices and edges. Space: O(V + E) - graph storage**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Depth-First Search, Breadth-First Search, Graph, Topological Sort

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/course-schedule)*
