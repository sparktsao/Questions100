# 085. Add Two Integers

**Difficulty:** EASY
**Frequency:** 32.0%
**Acceptance Rate:** 88.1%
**LeetCode Link:** [Add Two Integers](https://leetcode.com/problems/add-two-integers)

---

## Problem Description

Given two integers `num1` and `num2`, return the sum of the two integers.

**Constraints:**
- -100 <= num1, num2 <= 100

---

## Examples

### Example 1
**Input:** `num1 = 12, num2 = 5`
**Output:** `17`
**Explanation:** 12 + 5 = 17

### Example 2
**Input:** `num1 = -10, num2 = 4`
**Output:** `-6`
**Explanation:** -10 + 4 = -6

### Example 3
**Input:** `num1 = 0, num2 = 0`
**Output:** `0`
**Explanation:** 0 + 0 = 0

### Example 4
**Input:** `num1 = -100, num2 = 100`
**Output:** `0`
**Explanation:** Boundary case

---

## Optimal Solution

### Implementation

```python
def sum(num1: int, num2: int) -> int:
    """
    Simple addition operation.

    Time: O(1), Space: O(1)
    """
    return num1 + num2
```

### Complexity Analysis

**Time: O(1) - constant time addition. Space: O(1) - no extra space**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Math

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/add-two-integers)*
