# 043. Longest Common Prefix

**Difficulty:** EASY
**Frequency:** 59.4%
**Acceptance Rate:** 45.5%
**LeetCode Link:** [Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix)

---

## Problem Description

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string `""`.

**Constraints:**
- 1 <= strs.length <= 200
- 0 <= strs[i].length <= 200
- strs[i] consists of only lowercase English letters

---

## Examples

### Example 1
**Input:** `strs = ["flower","flow","flight"]`
**Output:** `"fl"`
**Explanation:** "fl" is the longest common prefix among all three strings

### Example 2
**Input:** `strs = ["dog","racecar","car"]`
**Output:** `""`
**Explanation:** There is no common prefix among the input strings

### Example 3
**Input:** `strs = ["interspecies","interstellar","interstate"]`
**Output:** `"inters"`
**Explanation:** All three words share the prefix "inters"

### Example 4
**Input:** `strs = ["alone"]`
**Output:** `"alone"`
**Explanation:** Single string, entire string is the common prefix

---

## Optimal Solution

### Implementation

```python
def longestCommonPrefix(strs: List[str]) -> str:
    """
    Vertical scanning approach - compare characters column by column.

    Time: O(S) where S is sum of all characters, Space: O(1)
    """
    if not strs:
        return ""

    # Compare character by character across all strings
    for i in range(len(strs[0])):
        char = strs[0][i]

        # Check if this character matches in all other strings
        for j in range(1, len(strs)):
            # If we've reached end of string or character doesn't match
            if i >= len(strs[j]) or strs[j][i] != char:
                return strs[0][:i]

    # First string is the common prefix
    return strs[0]
```

### Alternative Horizontal Scanning

```python
def longestCommonPrefix(strs: List[str]) -> str:
    """
    Horizontal scanning - reduce prefix by comparing pairs.

    Time: O(S), Space: O(1)
    """
    if not strs:
        return ""

    prefix = strs[0]

    for i in range(1, len(strs)):
        # Reduce prefix until it matches start of current string
        while not strs[i].startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix
```

### Using Sorting Optimization

```python
def longestCommonPrefix(strs: List[str]) -> str:
    """
    Sort and compare first and last strings only.

    Time: O(n log n + m) where n=number of strings, m=min length
    Space: O(1) excluding sort
    """
    if not strs:
        return ""

    strs.sort()
    first, last = strs[0], strs[-1]

    i = 0
    while i < len(first) and i < len(last) and first[i] == last[i]:
        i += 1

    return first[:i]
```

### Complexity Analysis

**Time: O(S) - where S is sum of all characters in all strings. Space: O(1) - constant**

**Why This is Optimal:**
- Vertical scanning can terminate early when mismatch found
- No extra space needed for storage
- Each character examined at most once
- Handles edge cases efficiently (empty array, single string, no common prefix)

---

## Categories & Tags

**Primary Topics:** String, Trie

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/longest-common-prefix)*
