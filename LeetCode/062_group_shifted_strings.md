# 062. Group Shifted Strings

**Difficulty:** MEDIUM
**Frequency:** 47.0%
**Acceptance Rate:** 67.4%
**LeetCode Link:** [Group Shifted Strings](https://leetcode.com/problems/group-shifted-strings)

---

## Problem Description

We can shift a string by shifting each of its letters to its successive letter.

- For example, "abc" can be shifted to be "bcd".

We can keep shifting the string to form a sequence.

- For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".

Given an array of strings `strings`, group all `strings[i]` that belong to the same shifting sequence. You may return the answer in any order.

**Constraints:**
- 1 <= strings.length <= 200
- 1 <= strings[i].length <= 50
- strings[i] consists of lowercase English letters

---

## Examples

### Example 1
**Input:** `strings = ["abc","bcd","acef","xyz","az","ba","a","z"]`
**Output:** `[["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]`
**Explanation:**
- "abc", "bcd", "xyz" have the same shift pattern (each consecutive letter differs by 1)
- "az" and "ba" have the same shift pattern
- "acef" is unique
- "a" and "z" are single characters grouped together

### Example 2
**Input:** `strings = ["a"]`
**Output:** `[["a"]]`
**Explanation:** Single string forms its own group

### Example 3
**Input:** `strings = ["abc","bcd","xyz"]`
**Output:** `[["abc","bcd","xyz"]]`
**Explanation:** All three strings have identical shift patterns (differences of [1,1])

### Example 4
**Input:** `strings = ["az","ba","aa"]`
**Output:** `[["aa"],["az","ba"]]`
**Explanation:** "az" shifts to "ba" (z->a, wraps around), but "aa" has zero differences

---

## Optimal Solution

### Implementation

```python
def groupStrings(strings: List[str]) -> List[List[str]]:
    """
    Group strings by their shift pattern using hash table.

    Time: O(n * k), Space: O(n * k) where n = number of strings, k = avg string length
    """
    from collections import defaultdict

    def get_pattern(s):
        """
        Calculate the shift pattern as tuple of differences.
        For "abc": (1, 1) since b-a=1, c-b=1
        """
        if len(s) == 1:
            return (0,)

        pattern = []
        for i in range(len(s) - 1):
            # Calculate difference, handle wrap-around (a comes after z)
            diff = (ord(s[i + 1]) - ord(s[i])) % 26
            pattern.append(diff)

        return tuple(pattern)

    groups = defaultdict(list)

    for string in strings:
        pattern = get_pattern(string)
        groups[pattern].append(string)

    return list(groups.values())
```

### Alternative Implementation (Normalize to 'a')

```python
def groupStrings(strings: List[str]) -> List[List[str]]:
    """
    Alternative approach: normalize each string to start with 'a'.

    Time: O(n * k), Space: O(n * k)
    """
    from collections import defaultdict

    def normalize(s):
        """Shift string so it starts with 'a'"""
        if not s:
            return ""

        shift = ord(s[0]) - ord('a')
        normalized = []

        for char in s:
            # Shift each character back by the same amount
            new_char = chr((ord(char) - shift) % 26 + ord('a'))
            normalized.append(new_char)

        return ''.join(normalized)

    groups = defaultdict(list)

    for string in strings:
        key = normalize(string)
        groups[key].append(string)

    return list(groups.values())
```

### Complexity Analysis

**Time: O(n * k) - where n is number of strings and k is average string length. Space: O(n * k) - storing all strings in hash map**

**Why This is Optimal:**
- Single pass through all strings with O(k) work per string
- Hash table provides O(1) average lookup and insertion
- The shift pattern calculation is necessary to determine grouping
- Cannot do better than O(n * k) since we must examine every character
- Handles wrap-around correctly with modulo arithmetic

---

## Categories & Tags

**Primary Topics:** Array, Hash Table, String

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/group-shifted-strings)*
