# 029. Valid Palindrome

**Difficulty:** EASY
**Frequency:** 69.5%
**Acceptance Rate:** 51.0%
**LeetCode Link:** [Valid Palindrome](https://leetcode.com/problems/valid-palindrome)

---

## Problem Description

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

**Constraints:**
- 1 <= s.length <= 2 * 10^5
- s consists only of printable ASCII characters

---

## Examples

### Example 1
**Input:** `s = "A man, a plan, a canal: Panama"`
**Output:** `true`
**Explanation:** After cleaning: "amanaplanacanalpanama" is palindrome

### Example 2
**Input:** `s = "race a car"`
**Output:** `false`
**Explanation:** After cleaning: "raceacar" is not palindrome

### Example 3
**Input:** `s = " "`
**Output:** `true`
**Explanation:** Empty string after cleaning is palindrome

### Example 4
**Input:** `s = "0P"`
**Output:** `false`
**Explanation:** 0p is not palindrome

---

## Optimal Solution

### Implementation

```python
def isPalindrome(s: str) -> bool:
    """
    Two pointers with in-place character validation.

    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

### Complexity Analysis

**Time: O(n) - single pass. Space: O(1) - constant**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Two Pointers, String

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/valid-palindrome)*
