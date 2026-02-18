# 008. Basic Calculator II

**Difficulty:** MEDIUM
**Frequency:** 84.0%
**Acceptance Rate:** 45.8%
**LeetCode Link:** [Basic Calculator II](https://leetcode.com/problems/basic-calculator-ii)

---

## Problem Description

Given a string `s` which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-2^31, 2^31 - 1].

**Note:** You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

**Constraints:**
- 1 <= s.length <= 3 * 10^5
- s consists of integers and operators ('+', '-', '*', '/') separated by spaces
- s represents a valid expression
- All integers are non-negative
- The answer is guaranteed to fit in 32-bit integer

---

## Examples

### Example 1
**Input:** `s = "3+2*2"`
**Output:** `7`
**Explanation:** Multiplication has higher precedence

### Example 2
**Input:** `s = " 3/2 "`
**Output:** `1`
**Explanation:** Division truncates toward zero

### Example 3
**Input:** `s = " 3+5 / 2 "`
**Output:** `5`
**Explanation:** 5/2 = 2, then 3+2 = 5

### Example 4
**Input:** `s = "42"`
**Output:** `42`
**Explanation:** Single number

---

## Optimal Solution

### Implementation

```python
def calculate(s: str) -> int:
    """
    Stack-based calculator with operator precedence.

    Time: O(n), Space: O(n)
    """
    if not s:
        return 0

    stack = []
    num = 0
    sign = '+'

    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)

        if char in '+-*/' or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))

            if char in '+-*/':
                sign = char
                num = 0

    return sum(stack)
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

**Primary Topics:** Math, String, Stack

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/basic-calculator-ii)
