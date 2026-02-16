# 057. Palindromic Substrings

**Difficulty:** MEDIUM
**Frequency:** 47.0%
**Acceptance Rate:** 71.7%
**LeetCode Link:** [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings)

---

## Problem Description

Given a string `s`, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

**Constraints:**
- 1 <= s.length <= 1000
- s consists of lowercase English letters

---

## Examples

### Example 1
**Input:** `s = "abc"`
**Output:** `3`
**Explanation:** Three palindromic substrings: "a", "b", "c"

### Example 2
**Input:** `s = "aaa"`
**Output:** `6`
**Explanation:** Six palindromic substrings: "a", "a", "a", "aa", "aa", "aaa"

### Example 3
**Input:** `s = "racecar"`
**Output:** `10`
**Explanation:** r, a, c, e, c, a, r, cec, aceca, racecar

### Example 4
**Input:** `s = "noon"`
**Output:** `6`
**Explanation:** n, o, o, n, oo, noon

---

## Optimal Solution

### Implementation

```python
def countSubstrings(s: str) -> int:
    """
    Expand around center for all possible centers.

    Time: O(n²), Space: O(1)
    """
    def expand_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    total = 0

    for i in range(len(s)):
        # Odd length palindromes (single center)
        total += expand_around_center(i, i)

        # Even length palindromes (two centers)
        total += expand_around_center(i, i + 1)

    return total
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

*Problem source: [LeetCode](https://leetcode.com/problems/palindromic-substrings)*
