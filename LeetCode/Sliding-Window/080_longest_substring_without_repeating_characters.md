# 080. Longest Substring Without Repeating Characters

**Difficulty:** MEDIUM
**Frequency:** 40.7%
**Acceptance Rate:** 36.9%
**LeetCode Link:** [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters)

---

## Problem Description

Given a string `s`, find the length of the longest substring without repeating characters.

**Constraints:**
- 0 <= s.length <= 5 * 10^4
- s consists of English letters, digits, symbols and spaces

---

## Examples

### Example 1
**Input:** `s = "abcabcbb"`
**Output:** `3`
**Explanation:** Longest substring is "abc", length 3

### Example 2
**Input:** `s = "bbbbb"`
**Output:** `1`
**Explanation:** Longest substring is "b", length 1

### Example 3
**Input:** `s = "pwwkew"`
**Output:** `3`
**Explanation:** Longest substring is "wke", length 3

### Example 4
**Input:** `s = ""`
**Output:** `0`
**Explanation:** Empty string

---

## Optimal Solution

### Implementation

```python
def lengthOfLongestSubstring(s: str) -> int:
    """
    Sliding window with hash set.

    Time: O(n), Space: O(min(m,n)) where m is charset size
    """
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        # Shrink window if duplicate found
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

### Complexity Analysis

**Time: O(n) - each char visited at most twice. Space: O(min(m,n)) - character set**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, String, Sliding Window

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters)*
