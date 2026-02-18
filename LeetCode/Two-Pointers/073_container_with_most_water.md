# 073. Container With Most Water

**Difficulty:** MEDIUM
**Frequency:** 40.7%
**Acceptance Rate:** 57.8%
**LeetCode Link:** [Container With Most Water](https://leetcode.com/problems/container-with-most-water)

---

## Problem Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Note:** You may not slant the container.

**Constraints:**
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

---

## Examples

### Example 1
**Input:** `height = [1,8,6,2,5,4,8,3,7]`
**Output:** `49`
**Explanation:** The vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. The max area of water the container can contain is 49, formed between indices 1 and 8: Area = min(8, 7) × (8 - 1) = 7 × 7 = 49

### Example 2
**Input:** `height = [1,1]`
**Output:** `1`
**Explanation:** Two lines of height 1 at distance 1 apart: Area = 1 × 1 = 1

### Example 3
**Input:** `height = [4,3,2,1,4]`
**Output:** `16`
**Explanation:** The maximum area is between indices 0 and 4: Area = min(4, 4) × (4 - 0) = 4 × 4 = 16

### Example 4
**Input:** `height = [1,2,1]`
**Output:** `2`
**Explanation:** Maximum area between indices 0 and 2: Area = min(1, 1) × (2 - 0) = 1 × 2 = 2

---

## Optimal Solution

### Implementation

```python
def maxArea(height: List[int]) -> int:
    """
    Two-pointer approach to find maximum water container area.

    Time: O(n), Space: O(1)
    """
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter line
        # Moving the taller line won't improve the result
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area
```

### Complexity Analysis

**Time: O(n) - single pass with two pointers. Space: O(1) - constant extra space**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Greedy approach guarantees finding the maximum by eliminating suboptimal configurations
- Area is limited by the shorter line, so we move that pointer inward
- Each iteration reduces search space without missing the optimal solution
- Minimal space overhead while maintaining code clarity

---

## Categories & Tags

**Primary Topics:** Array, Two Pointers, Greedy

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/container-with-most-water)*
