# 067. String to Integer (atoi)

**Difficulty:** MEDIUM
**Frequency:** 40.7%
**Acceptance Rate:** 19.2%
**LeetCode Link:** [String to Integer (atoi)](https://leetcode.com/problems/string-to-integer-atoi)

---

## Problem Description

Implement the `myAtoi(string s)` function, which converts a string to a 32-bit signed integer (similar to C/C++'s `atoi` function).

The algorithm for `myAtoi(string s)` is as follows:

1. **Read in and ignore any leading whitespace.**
2. **Check if the next character (if not already at the end of the string) is '-' or '+'.** Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
3. **Read in next the characters until the next non-digit character or the end of the input is reached.** The rest of the string is ignored.
4. **Convert these digits into an integer** (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
5. **If the integer is out of the 32-bit signed integer range** [-2^31, 2^31 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -2^31 should be clamped to -2^31, and integers greater than 2^31 - 1 should be clamped to 2^31 - 1.
6. **Return the integer as the final result.**

**Note:**
- Only the space character ' ' is considered a whitespace character.
- Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

**Constraints:**
- 0 <= s.length <= 200
- s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'

---

## Examples

### Example 1
**Input:** `s = "42"`
**Output:** `42`
**Explanation:**
- Step 1: No whitespace
- Step 2: No sign, assume positive
- Step 3: Read "42"
- Result: 42

### Example 2
**Input:** `s = "   -42"`
**Output:** `-42`
**Explanation:**
- Step 1: Ignore leading whitespace
- Step 2: '-' detected, result will be negative
- Step 3: Read "42"
- Result: -42

### Example 3
**Input:** `s = "4193 with words"`
**Output:** `4193`
**Explanation:**
- Step 1: No whitespace
- Step 2: No sign
- Step 3: Read "4193", stop at space
- Result: 4193

### Example 4
**Input:** `s = "words and 987"`
**Output:** `0`
**Explanation:**
- Step 1: No leading whitespace
- Step 2: No sign
- Step 3: First character 'w' is not a digit, conversion stops
- Result: 0

### Example 5
**Input:** `s = "-91283472332"`
**Output:** `-2147483648`
**Explanation:**
- The number -91283472332 is out of range
- Clamp to -2^31 = -2147483648

---

## Optimal Solution

### Implementation

```python
def myAtoi(s: str) -> int:
    """
    Convert string to 32-bit signed integer following atoi rules.

    Time: O(n), Space: O(1)
    """
    # Constants for 32-bit signed integer range
    INT_MAX = 2**31 - 1  # 2147483647
    INT_MIN = -2**31      # -2147483648

    # Step 1: Skip leading whitespace
    i = 0
    n = len(s)
    while i < n and s[i] == ' ':
        i += 1

    # Check if we reached end
    if i == n:
        return 0

    # Step 2: Check for sign
    sign = 1
    if s[i] == '+':
        i += 1
    elif s[i] == '-':
        sign = -1
        i += 1

    # Step 3: Read digits and build number
    result = 0
    while i < n and s[i].isdigit():
        digit = int(s[i])

        # Step 4: Check for overflow before adding digit
        # If result > INT_MAX // 10, then result * 10 will overflow
        # If result == INT_MAX // 10, then result * 10 + digit might overflow
        if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
            return INT_MAX if sign == 1 else INT_MIN

        result = result * 10 + digit
        i += 1

    # Step 5: Apply sign
    return sign * result
```

### Alternative Implementation (More Concise)

```python
def myAtoi(s: str) -> int:
    """
    Alternative implementation with early boundary checking.

    Time: O(n), Space: O(1)
    """
    s = s.lstrip()  # Remove leading whitespace

    if not s:
        return 0

    # Determine sign
    sign = -1 if s[0] == '-' else 1
    if s[0] in ['+', '-']:
        s = s[1:]

    # Build result
    result = 0
    for char in s:
        if not char.isdigit():
            break
        result = result * 10 + int(char)

    # Apply sign and clamp
    result = sign * result
    INT_MAX, INT_MIN = 2**31 - 1, -2**31

    return max(INT_MIN, min(INT_MAX, result))
```

### Complexity Analysis

**Time: O(n) - single pass through string. Space: O(1) - constant extra space**

**Why This is Optimal:**
- Cannot do better than O(n) as we must examine each character
- O(1) space with no additional data structures
- Early termination on non-digit characters
- Overflow detection before it happens (crucial for correctness)
- Handles all edge cases: leading whitespace, signs, overflow, underflow, non-digit characters

---

## Categories & Tags

**Primary Topics:** String

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/string-to-integer-atoi)*
