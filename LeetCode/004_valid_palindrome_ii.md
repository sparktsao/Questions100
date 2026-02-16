# 004. Valid Palindrome II

**Difficulty:** EASY
**Frequency:** 92.7%
**Acceptance Rate:** 43.0%
**LeetCode Link:** [Valid Palindrome II](https://leetcode.com/problems/valid-palindrome-ii)

---

## Problem Description

Given a string `s`, return `true` if the `s` can be palindrome after deleting at most one character from it.

**Constraints:**
- 1 <= s.length <= 10^5
- s consists of lowercase English letters

---

## Examples

### Example 1
**Input:** `s = "aba"`
**Output:** `true`
**Explanation:** Already a palindrome, no deletion needed

### Example 2
**Input:** `s = "abca"`
**Output:** `true`
**Explanation:** Delete 'c' or 'b' to make palindrome

### Example 3
**Input:** `s = "abc"`
**Output:** `false`
**Explanation:** Cannot form palindrome with at most 1 deletion

### Example 4
**Input:** `s = "racecar"`
**Output:** `true`
**Explanation:** Already palindrome

---

## Optimal Solution

### Implementation

```python
def validPalindrome(s: str) -> bool:
    """
    Two pointers with one skip allowed.

    Time: O(n), Space: O(1)
    """
    def is_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try skipping either left or right
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1

    return True
```

### Complexity Analysis

**Time: O(n) - at most one extra scan. Space: O(1) - constant**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Two Pointers, String, Greedy

**Difficulty Level:** EASY

---

*Problem source: [LeetCode](https://leetcode.com/problems/valid-palindrome-ii)*
