# 058. Valid Number

**Difficulty:** HARD
**Frequency:** 47.0%
**Acceptance Rate:** 21.6%
**LeetCode Link:** [Valid Number](https://leetcode.com/problems/valid-number)

---

## Problem Description

Given a string `s`, return true if `s` is a valid number.

A valid number can be split into these components (in order):
1. A decimal number or an integer
2. (Optional) An 'e' or 'E', followed by an integer

A decimal number can be split into these components (in order):
1. (Optional) A sign character (either '+' or '-')
2. One of the following formats:
   - One or more digits, followed by a dot '.'
   - One or more digits, followed by a dot '.', followed by one or more digits
   - A dot '.', followed by one or more digits

An integer can be split into these components (in order):
1. (Optional) A sign character (either '+' or '-')
2. One or more digits

**Constraints:**
- 1 <= s.length <= 20
- s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'

---

## Examples

### Example 1
**Input:** `s = "0"`
**Output:** `true`
**Explanation:** Valid integer

### Example 2
**Input:** `s = "e"`
**Output:** `false`
**Explanation:** 'e' alone is not a valid number

### Example 3
**Input:** `s = "."`
**Output:** `false`
**Explanation:** Dot without digits is invalid

### Example 4
**Input:** `s = "2e10"`
**Output:** `true`
**Explanation:** Valid scientific notation: 2 * 10^10

### Example 5
**Input:** `s = "-90E3"`
**Output:** `true`
**Explanation:** Valid: -90 * 10^3

### Example 6
**Input:** `s = "6e-1"`
**Output:** `true`
**Explanation:** Valid: 6 * 10^-1 = 0.6

### Example 7
**Input:** `s = "99e2.5"`
**Output:** `false`
**Explanation:** Exponent must be integer, not decimal

### Example 8
**Input:** `s = "53.5e93"`
**Output:** `true`
**Explanation:** Valid scientific notation with decimal base

### Example 9
**Input:** `s = "--6"`
**Output:** `false`
**Explanation:** Double sign is invalid

### Example 10
**Input:** `s = ".1"`
**Output:** `true`
**Explanation:** Valid decimal: 0.1

---

## Optimal Solution

### Implementation (State Machine)

```python
def isNumber(s: str) -> bool:
    """
    Validate number using deterministic finite automaton (DFA).

    Time: O(n), Space: O(1)
    """
    seen_digit = False
    seen_exponent = False
    seen_dot = False

    for i, char in enumerate(s):
        if char.isdigit():
            seen_digit = True

        elif char in ['+', '-']:
            # Sign can only appear at start or immediately after 'e'/'E'
            if i > 0 and s[i-1] not in ['e', 'E']:
                return False

        elif char in ['e', 'E']:
            # Can't have multiple exponents or exponent without preceding number
            if seen_exponent or not seen_digit:
                return False
            seen_exponent = True
            seen_digit = False  # Must have digits after exponent

        elif char == '.':
            # Can't have multiple dots or dot after exponent
            if seen_dot or seen_exponent:
                return False
            seen_dot = True

        else:
            # Invalid character
            return False

    return seen_digit
```

### Alternative Implementation (Comprehensive Validation)

```python
def isNumber(s: str) -> bool:
    """
    More explicit validation with clear state tracking.

    Time: O(n), Space: O(1)
    """
    i = 0
    n = len(s)

    # Skip leading spaces (if allowed)
    # while i < n and s[i] == ' ':
    #     i += 1

    # Check for sign
    if i < n and s[i] in '+-':
        i += 1

    # Track if we've seen digits or dot
    num_digits = 0
    num_dots = 0

    # Process number before exponent
    while i < n and (s[i].isdigit() or s[i] == '.'):
        if s[i] == '.':
            num_dots += 1
        else:
            num_digits += 1
        i += 1

    # Must have at least one digit, and at most one dot
    if num_digits == 0 or num_dots > 1:
        return False

    # Check for exponent
    if i < n and s[i] in 'eE':
        i += 1

        # Check for sign after exponent
        if i < n and s[i] in '+-':
            i += 1

        # Must have at least one digit in exponent
        num_exp_digits = 0
        while i < n and s[i].isdigit():
            num_exp_digits += 1
            i += 1

        if num_exp_digits == 0:
            return False

    # Must have consumed entire string
    return i == n
```

### Complexity Analysis

**Time:** O(n) where n is the length of the string
- Single pass through the string
- Each character checked once

**Space:** O(1)
- Only a few boolean flags and counters
- No additional data structures needed

**Why This is Optimal:**
- Cannot do better than O(n) as we must check every character
- O(1) space is minimal possible
- State machine approach handles all edge cases systematically
- No need for regular expressions or complex parsing

---

## Categories & Tags

**Primary Topics:** String

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/valid-number)*
