# 002. Valid Word Abbreviation

**Difficulty:** EASY
**Frequency:** 95.4%
**Acceptance Rate:** 36.9%
**LeetCode Link:** [Valid Word Abbreviation](https://leetcode.com/problems/valid-word-abbreviation)

---

## Problem Description

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. For example, "substitution" can be abbreviated as "s10n" ("s ubstitutio n"), "sub4u4" ("sub stit u tion"), and more.

Given a string `word` and an abbreviation `abbr`, return whether the abbreviation matches the string.

**Constraints:**
- 1 <= word.length <= 20
- word consists of only lowercase English letters
- 1 <= abbr.length <= 10
- abbr consists of lowercase English letters and digits
- All numbers in abbr will fit in 32-bit integer

---

## Examples

### Example 1
**Input:** `word = "internationalization", abbr = "i12iz4n"`
**Output:** `true`
**Explanation:** i + 12 chars + iz + 4 chars + n matches

### Example 2
**Input:** `word = "apple", abbr = "a2e"`
**Output:** `false`
**Explanation:** a + 2 chars should be 'pp', but next char is 'e' not 'l'

### Example 3
**Input:** `word = "substitution", abbr = "s10n"`
**Output:** `true`
**Explanation:** s + 10 chars + n matches

### Example 4
**Input:** `word = "hi", abbr = "1"`
**Output:** `false`
**Explanation:** Leading zeros not allowed (implicit)

---

## Optimal Solution

### Implementation

```python
def validWordAbbreviation(word: str, abbr: str) -> bool:
    """
    Two pointers to validate abbreviation.

    Time: O(n), Space: O(1)
    """
    i = j = 0

    while i < len(word) and j < len(abbr):
        if abbr[j].isdigit():
            # Leading zero check
            if abbr[j] == '0':
                return False

            # Parse number
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                j += 1
            i += num
        else:
            # Character must match
            if word[i] != abbr[j]:
                return False
            i += 1
            j += 1

    return i == len(word) and j == len(abbr)
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

*Problem source: [LeetCode](https://leetcode.com/problems/valid-word-abbreviation)*
