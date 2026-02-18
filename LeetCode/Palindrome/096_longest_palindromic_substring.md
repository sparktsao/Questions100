# 096. Longest Palindromic Substring

**Difficulty:** MEDIUM
**Frequency:** 32.0%
**Acceptance Rate:** 35.8%
**LeetCode Link:** [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring)

---

## Problem Description

Given a string `s`, return the longest palindromic substring in `s`.

**Constraints:**
- 1 <= s.length <= 1000
- s consist of only digits and English letters

---

## Examples

### Example 1
**Input:** `s = "babad"`
**Output:** `"bab" or "aba"`
**Explanation:** Both are valid longest palindromes

### Example 2
**Input:** `s = "cbbd"`
**Output:** `"bb"`
**Explanation:** Only palindrome of length > 1

### Example 3
**Input:** `s = "a"`
**Output:** `"a"`
**Explanation:** Single character is palindrome

### Example 4
**Input:** `s = "racecar"`
**Output:** `"racecar"`
**Explanation:** Entire string is palindrome

---

## Optimal Solution

### Implementation

```python
def longestPalindrome(s: str) -> str:
    """
    Expand around center for all possible centers.

    Time: O(n²), Space: O(1)
    """
    if not s:
        return ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start = 0
    max_len = 0

    for i in range(len(s)):
        # Odd length palindromes
        len1 = expand_around_center(i, i)
        # Even length palindromes
        len2 = expand_around_center(i, i + 1)

        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2

    return s[start:start + max_len]
```

### Complexity Analysis

**Time: O(n²) - expand from each center. Space: O(1) - constant**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Two Pointers, String, Dynamic Programming

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/longest-palindromic-substring)*
