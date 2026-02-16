# 020. Valid Parentheses

**Difficulty:** EASY
**Frequency:** 74.9%
**Acceptance Rate:** 42.3%
**LeetCode Link:** [Valid Parentheses](https://leetcode.com/problems/valid-parentheses)

---

## Problem Description

Given a string `s` containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets
2. Open brackets must be closed in the correct order
3. Every close bracket has a corresponding open bracket of the same type

**Constraints:**
- 1 <= s.length <= 10^4
- s consists of parentheses only '()[]{}'

---

## Examples

### Example 1
**Input:** `s = "()"`
**Output:** `true`
**Explanation:** Simple matching pair

### Example 2
**Input:** `s = "()[]{}"`
**Output:** `true`
**Explanation:** Multiple types of brackets, all matched correctly

### Example 3
**Input:** `s = "(]"`
**Output:** `false`
**Explanation:** Mismatched bracket types

### Example 4
**Input:** `s = "([)]"`
**Output:** `false`
**Explanation:** Incorrect nesting order

### Example 5
**Input:** `s = "{[]}"`
**Output:** `true`
**Explanation:** Properly nested brackets

---

## Optimal Solution

### Implementation

```python
def isValid(s: str) -> bool:
    """
    Check if parentheses are valid using stack.

    Time: O(n), Space: O(n)
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack
```

### Complexity Analysis

**Time: O(n) - single pass. Space: O(n) - stack storage**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** String, Stack

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/valid-parentheses)
