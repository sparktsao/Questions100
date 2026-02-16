# 078. Strobogrammatic Number

**Difficulty:** EASY
**Frequency:** 40.7%
**Acceptance Rate:** 47.6%
**LeetCode Link:** [Strobogrammatic Number](https://leetcode.com/problems/strobogrammatic-number)

---

## Problem Description

Given a string `num` which represents an integer, return `true` if `num` is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

**Constraints:**
- 1 <= num.length <= 50
- num consists of only digits
- num does not contain any leading zeros except for zero itself

---

## Examples

### Example 1
**Input:** `num = "69"`
**Output:** `true`
**Explanation:** 69 rotated 180° is still 69

### Example 2
**Input:** `num = "88"`
**Output:** `true`
**Explanation:** 88 rotated 180° is still 88

### Example 3
**Input:** `num = "962"`
**Output:** `false`
**Explanation:** 962 rotated is not 962

### Example 4
**Input:** `num = "1"`
**Output:** `true`
**Explanation:** Single digit 1, 0, 8 are strobogrammatic

---

## Optimal Solution

### Implementation

```python
def isStrobogrammatic(num: str) -> bool:
    """
    Two pointers checking valid rotation pairs.

    Time: O(n), Space: O(1)
    """
    # Valid pairs when rotated 180°
    pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in pairs or pairs[num[left]] != num[right]:
            return False
        left += 1
        right -= 1

    return True
```

### Complexity Analysis

**Time: O(n) - single pass. Space: O(1) - constant mapping**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, Two Pointers, String

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/strobogrammatic-number)*
