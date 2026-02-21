# 022. Buildings With an Ocean View

**Difficulty:** MEDIUM
**Frequency:** 74.9%
**Acceptance Rate:** 80.8%
**LeetCode Link:** [Buildings With an Ocean View](https://leetcode.com/problems/buildings-with-an-ocean-view)

---

## Problem Description

There are `n` buildings in a line. You are given an integer array `heights` of size `n` that represents the heights of the buildings in the line.

The ocean is to the **right** of the buildings. A building has an ocean view if the building can see the ocean without obstructions. Formally, a building has an ocean view if all the buildings to its **right** have a **smaller** height.

Return a list of indices (0-indexed) of buildings that have an ocean view, sorted in increasing order.

**Constraints:**
- 1 <= heights.length <= 10^5
- 1 <= heights[i] <= 10^9

---

## Examples

### Example 1
**Input:** `heights = [4,2,3,1]`
**Output:** `[0,2,3]`
**Explanation:** Building 1 (0-indexed) does not have an ocean view because building 2 is taller

### Example 2
**Input:** `heights = [4,3,2,1]`
**Output:** `[0,1,2,3]`
**Explanation:** All the buildings have an ocean view

### Example 3
**Input:** `heights = [1,3,2,4]`
**Output:** `[3]`
**Explanation:** Only building 3 has an ocean view

### Example 4
**Input:** `heights = [2,2,2,2]`
**Output:** `[3]`
**Explanation:** Buildings cannot see the ocean if there are buildings of the same height to its right

---

## Optimal Solution

### Implementation

```python
def findBuildings(heights: List[int]) -> List[int]:
    """
    Find buildings with ocean view using right-to-left traversal.

    Time: O(n), Space: O(1) excluding output
    """
    result = []
    max_height = 0

    # Traverse from right to left
    for i in range(len(heights) - 1, -1, -1):
        # If current building is taller than max seen so far, it has ocean view
        if heights[i] > max_height:
            result.append(i)
            max_height = heights[i]

    # Reverse to get indices in increasing order
    return result[::-1]
```

### Alternative Implementation (Using Monotonic Stack)

```python
def findBuildings(heights: List[int]) -> List[int]:
    """
    Monotonic decreasing stack approach (left-to-right scan).

    Key Insight: Maintain a stack where buildings are in DECREASING height order.
    When we encounter a taller building, all shorter buildings to its left
    cannot see the ocean (blocked by this taller one).

    Time: O(n), Space: O(n)
    """
    stack = []

    for i in range(len(heights)):
        # Remove buildings that are blocked by current building
        # (shorter or equal height buildings to the left)
        while stack and heights[stack[-1]] <= heights[i]:
            stack.pop()
        stack.append(i)

    # Buildings remaining in stack can all see the ocean
    # They're already in increasing index order
    return stack

# Trace Example 1: heights = [4,2,3,1]
# i=0: stack=[] → append 0 → [0]
# i=1: h[0]=4 > h[1]=2, don't pop → append 1 → [0,1]
# i=2: h[1]=2 <= h[2]=3, pop 1 → [0], h[0]=4 > h[2]=3 → append 2 → [0,2]
# i=3: h[2]=3 > h[3]=1, don't pop → append 3 → [0,2,3] ✓

# Trace Example 3: heights = [1,3,2,4]
# i=0: stack=[] → append 0 → [0]
# i=1: h[0]=1 <= h[1]=3, pop 0 → [], append 1 → [1]
# i=2: h[1]=3 > h[2]=2, don't pop → append 2 → [1,2]
# i=3: h[2]=2 <= h[3]=4, pop 2 → [1], h[1]=3 <= h[3]=4, pop 1 → []
#      append 3 → [3] ✓
```

**Why This Works:**
- We scan left-to-right, maintaining buildings in **monotonic decreasing height** order
- When we see a taller building, we pop all shorter ones (they're blocked)
- Buildings that remain in the stack are never blocked by anything to their right
- The last building is always included (nothing blocks it)

### Most Efficient Implementation

```python
def findBuildings(heights: List[int]) -> List[int]:
    """
    Optimal right-to-left scan with early termination.

    Time: O(n), Space: O(1)
    """
    n = len(heights)
    result = []
    max_right = 0

    # Scan from right to left
    for i in range(n - 1, -1, -1):
        if heights[i] > max_right:
            result.append(i)
            max_right = heights[i]

    result.reverse()
    return result
```

### Complexity Analysis

**Time: O(n) - single pass from right to left. Space: O(1) - only storing result indices**

**Why This is Optimal:**
- Achieves best possible time complexity with single pass
- Space complexity is O(1) excluding output array
- Leverages the insight that we only need to track max height seen so far
- No need for complex data structures - simple greedy approach works
- Handles all edge cases efficiently

---

## Categories & Tags

**Primary Topics:** Array, Stack, Monotonic Stack

**Difficulty Level:** MEDIUM

---

*Problem source: [LeetCode](https://leetcode.com/problems/buildings-with-an-ocean-view)*
