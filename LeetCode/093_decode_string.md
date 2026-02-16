# 093. Decode String

**Difficulty:** MEDIUM
**Frequency:** 32.0%
**Acceptance Rate:** 61.2%
**LeetCode Link:** [Decode String](https://leetcode.com/problems/decode-string)

---

## Problem Description

Given an encoded string, return its decoded string.

The encoding rule is: `k[encoded_string]`, where the `encoded_string` inside the square brackets is being repeated exactly `k` times. Note that `k` is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, `k`. For example, there will not be input like `3a` or `2[4]`.

The test cases are generated so that the length of the output will never exceed 10^5.

**Constraints:**
- 1 <= s.length <= 30
- s consists of lowercase English letters, digits, and square brackets '[]'
- s is guaranteed to be a valid input
- All the integers in s are in the range [1, 300]

---

## Examples

### Example 1
**Input:** `s = "3[a]2[bc]"`
**Output:** `"aaabcbc"`
**Explanation:** "a" is repeated 3 times, "bc" is repeated 2 times

### Example 2
**Input:** `s = "3[a2[c]]"`
**Output:** `"accaccacc"`
**Explanation:** "c" is repeated 2 times to get "cc", then "acc" is repeated 3 times

### Example 3
**Input:** `s = "2[abc]3[cd]ef"`
**Output:** `"abcabccdcdcdef"`
**Explanation:** Sequential encoded patterns with trailing characters

### Example 4
**Input:** `s = "abc3[cd]xyz"`
**Output:** `"abccdcdcdxyz"`
**Explanation:** Mix of regular and encoded characters

---

## Optimal Solution

### Implementation

```python
def decodeString(s: str) -> str:
    """
    Decode string using stack for nested patterns.

    Time: O(maxK * n) where maxK is max repetition count
    Space: O(n) for stack
    """
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            # Build multi-digit number
            current_num = current_num * 10 + int(char)

        elif char == '[':
            # Push current state to stack
            stack.append((current_string, current_num))
            # Reset for new context
            current_string = ""
            current_num = 0

        elif char == ']':
            # Pop previous context
            prev_string, num = stack.pop()
            # Decode: repeat current string num times
            current_string = prev_string + current_string * num

        else:
            # Regular character
            current_string += char

    return current_string
```

### Alternative Recursive Implementation

```python
def decodeString(s: str) -> str:
    """
    Recursive approach for decoding.

    Time: O(maxK * n), Space: O(n) for recursion
    """
    def helper(index):
        result = ""
        num = 0

        while index < len(s):
            char = s[index]

            if char.isdigit():
                num = num * 10 + int(char)

            elif char == '[':
                # Recursively decode substring
                decoded, index = helper(index + 1)
                result += decoded * num
                num = 0

            elif char == ']':
                # Return to previous level
                return result, index

            else:
                # Regular character
                result += char

            index += 1

        return result, index

    decoded, _ = helper(0)
    return decoded
```

### Complexity Analysis

**Time: O(maxK * n) - in worst case, repeat entire string maxK times. Space: O(n) - stack storage**

**Why This is Optimal:**
- Stack naturally handles nested bracket structures
- Single pass through input string
- Handles multi-digit numbers correctly
- No need to parse or preprocess string
- Efficiently builds result without repeated copying

---

## Categories & Tags

**Primary Topics:** String, Stack, Recursion

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/decode-string)*
