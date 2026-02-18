# 001. Minimum Remove to Make Valid Parentheses

**Difficulty:** MEDIUM
**Frequency:** 100.0%
**Acceptance Rate:** 70.7%
**LeetCode Link:** [Minimum Remove to Make Valid Parentheses](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses)

---

## Problem Description

Given a string `s` of '(' , ')' and lowercase English characters, remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

A string is valid if:
- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.

**Constraints:**
- 1 <= s.length <= 10^5
- s[i] is either '(' , ')', or lowercase English letter

---

## Examples

### Example 1
**Input:** `s = "lee(t(c)o)de)"`
**Output:** `"lee(t(c)o)de"`
**Explanation:** Remove the extra ) at the end

### Example 2
**Input:** `s = "a)b(c)d"`
**Output:** `"ab(c)d"`
**Explanation:** Remove the extra ) at index 1

### Example 3
**Input:** `s = "))(("`
**Output:** `""`
**Explanation:** All parentheses are invalid, remove all

### Example 4
**Input:** `s = "(a(b(c)d)"`
**Output:** `"a(b(c)d)" or "(a(b(c)d))"`
**Explanation:** Multiple valid answers possible

---

## Optimal Solution

### Implementation

```python
def minRemoveToMakeValid(s: str) -> str:
    """
    Remove minimum parentheses using stack to track indices.

    Time: O(n), Space: O(n)
    """
    to_remove = set()
    stack = []

    # Find indices to remove
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                to_remove.add(i)

    # Add unmatched '(' to remove set
    to_remove.update(stack)

    # Build result
    return ''.join(char for i, char in enumerate(s) if i not in to_remove)
```

### Complexity Analysis

**Time: O(n) - single pass. Space: O(n) - stack and set storage**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** String, Stack

**Difficulty Level:** MEDIUM

---

*Problem source: [LeetCode](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses)*
