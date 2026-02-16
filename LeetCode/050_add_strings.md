# 050. Add Strings

**Difficulty:** EASY
**Frequency:** 51.9%
**Acceptance Rate:** 51.9%
**LeetCode Link:** [Add Strings](https://leetcode.com/problems/add-strings)

---

## Problem Description

Given two non-negative integers, `num1` and `num2` represented as string, return the sum of `num1` and `num2` as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

**Constraints:**
- 1 <= num1.length, num2.length <= 10^4
- num1 and num2 consist of only digits
- num1 and num2 don't have any leading zeros except for the zero itself

---

## Examples

### Example 1
**Input:** `num1 = "11", num2 = "123"`
**Output:** `"134"`
**Explanation:** 11 + 123 = 134

### Example 2
**Input:** `num1 = "456", num2 = "77"`
**Output:** `"533"`
**Explanation:** 456 + 77 = 533

### Example 3
**Input:** `num1 = "0", num2 = "0"`
**Output:** `"0"`
**Explanation:** 0 + 0 = 0

### Example 4
**Input:** `num1 = "9999", num2 = "1"`
**Output:** `"10000"`
**Explanation:** Tests carry propagation

---

## Optimal Solution

### Implementation

```python
def addStrings(num1: str, num2: str) -> str:
    """
    Elementary school addition with carry.

    Time: O(max(m,n)), Space: O(max(m,n))
    """
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0

        total = digit1 + digit2 + carry
        result.append(str(total % 10))
        carry = total // 10

        i -= 1
        j -= 1

    return ''.join(reversed(result))
```

### Complexity Analysis

**Time: O(max(m,n)) - process longer number. Space: O(max(m,n)) - result string**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Math, String, Simulation

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/add-strings)*
