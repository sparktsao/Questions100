# 011. Nested List Weight Sum

**Difficulty:** MEDIUM
**Frequency:** 81.7%
**Acceptance Rate:** 85.5%
**LeetCode Link:** [Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum)

---

## Problem Description

Given a nested list of integers, return the sum of all integers in the list weighted by their depth.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

**Constraints:**
- 1 <= nestedList.length <= 50
- The values of the integers in the nested list is in the range [-100, 100]
- The maximum depth of any integer is less than or equal to 50

---

## Examples

### Example 1
**Input:** `[[1,1],2,[1,1]]`
**Output:** `10`
**Explanation:** (1*2 + 1*2) + (2*1) + (1*2 + 1*2) = 4 + 2 + 4 = 10

### Example 2
**Input:** `[1,[4,[6]]]`
**Output:** `27`
**Explanation:** 1*1 + 4*2 + 6*3 = 1 + 8 + 18 = 27

### Example 3
**Input:** `[0]`
**Output:** `0`
**Explanation:** Single element at depth 1

### Example 4
**Input:** `[[1,1],[2,2]]`
**Output:** `8`
**Explanation:** All at depth 2: (1+1+2+2)*2 = 12

---

## Optimal Solution

### Implementation

```python
def depthSum(nestedList: List[NestedInteger]) -> int:
    """
    DFS recursive approach with depth tracking.

    Time: O(n), Space: O(d) where d is max depth
    """
    def dfs(nested_list, depth):
        total = 0
        for item in nested_list:
            if item.isInteger():
                total += item.getInteger() * depth
            else:
                total += dfs(item.getList(), depth + 1)
        return total

    return dfs(nestedList, 1)
```

### Complexity Analysis

**Time: O(n) - visit each element once. Space: O(d) - recursion depth**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Depth-First Search, Breadth-First Search

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/nested-list-weight-sum)
