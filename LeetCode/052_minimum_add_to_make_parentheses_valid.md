# 052. Minimum Add to Make Parentheses Valid

**Difficulty:** MEDIUM
**Frequency:** 51.9%
**Acceptance Rate:** 74.7%
**LeetCode Link:** [Minimum Add to Make Parentheses Valid](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid)

---

## Problem Description

A parentheses string is valid if and only if:
- It is the empty string,
- It can be written as AB (A concatenated with B), where A and B are valid strings, or
- It can be written as (A), where A is a valid string.

You are given a parentheses string `s`. In one move, you can insert a parenthesis at any position of the string.

Return the minimum number of moves required to make `s` valid.

**Constraints:**
- 1 <= s.length <= 1000
- s[i] is either '(' or ')'

---

## Examples

### Example 1
**Input:** `s = "())"`
**Output:** `1`
**Explanation:** We can insert one opening parenthesis to make it "(())", or one closing parenthesis to make it "(()))".

### Example 2
**Input:** `s = "((("`
**Output:** `3`
**Explanation:** We need to add 3 closing parentheses to make it valid: "((()))"

### Example 3
**Input:** `s = "()"`
**Output:** `0`
**Explanation:** The string is already valid

### Example 4
**Input:** `s = "()))(("`
**Output:** `4`
**Explanation:** We need 2 opening parentheses at the start and 2 closing at the end

---

## Optimal Solution

### Implementation

```python
def minAddToMakeValid(s: str) -> int:
    """
    Count unmatched parentheses using counters.

    Time: O(n), Space: O(1)
    """
    open_needed = 0    # Count of unmatched ')'
    close_needed = 0   # Count of unmatched '('

    for char in s:
        if char == '(':
            close_needed += 1
        elif char == ')':
            if close_needed > 0:
                close_needed -= 1  # Match with previous '('
            else:
                open_needed += 1   # Need an '(' before this

    return open_needed + close_needed
```

### Alternative Implementation (Stack-Based)

```python
def minAddToMakeValid(s: str) -> int:
    """
    Stack-based solution for tracking unmatched parentheses.

    Time: O(n), Space: O(n) in worst case
    """
    stack = []
    unmatched = 0

    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                unmatched += 1

    return unmatched + len(stack)
```

### Complexity Analysis

**Optimal Counter Approach:**
- **Time:** O(n) - single pass through string
- **Space:** O(1) - only two counter variables

**Stack Approach:**
- **Time:** O(n) - single pass through string
- **Space:** O(n) - stack can grow up to n in worst case

**Why Counter Approach is Optimal:**
- Achieves same result with O(1) space instead of O(n)
- No need to store actual parentheses, just count them
- More cache-friendly due to no dynamic allocations
- Simpler and more intuitive logic

---

## Categories & Tags

**Primary Topics:** String, Stack, Greedy

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/minimum-add-to-make-parentheses-valid)*
