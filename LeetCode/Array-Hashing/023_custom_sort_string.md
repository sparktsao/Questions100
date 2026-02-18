# 023. Custom Sort String

**Difficulty:** MEDIUM
**Frequency:** 73.2%
**Acceptance Rate:** 72.0%
**LeetCode Link:** [Custom Sort String](https://leetcode.com/problems/custom-sort-string)

---

## Problem Description

You are given two strings `order` and `s`. All the characters of `order` are unique and were sorted in some custom order previously.

Permute the characters of `s` so that they match the order that `order` was sorted. More specifically, if a character `x` occurs before a character `y` in `order`, then `x` should occur before `y` in the permuted string.

Return any permutation of `s` that satisfies this property.

**Constraints:**
- 1 <= order.length <= 26
- 1 <= s.length <= 200
- order and s consist of lowercase English letters
- All characters of order are unique

---

## Examples

### Example 1
**Input:** `order = "cba", s = "abcd"`
**Output:** `"dcba"`
**Explanation:** c comes before b and a, so order is d, c, b, a

### Example 2
**Input:** `order = "cbafg", s = "abcd"`
**Output:** `"cbad"`
**Explanation:** c, b, a are ordered, d is not in order so goes at end

### Example 3
**Input:** `order = "kqep", s = "pekeq"`
**Output:** `"kqeep"`
**Explanation:** k first, then q, then e's, then p

### Example 4
**Input:** `order = "abc", s = "zzz"`
**Output:** `"zzz"`
**Explanation:** Characters not in order maintain relative positions

---

## Optimal Solution

### Implementation

```python
def customSortString(order: str, s: str) -> str:
    """
    Count characters and build result based on custom order.

    Time: O(n + m), Space: O(1) - fixed alphabet size
    """
    from collections import Counter

    count = Counter(s)
    result = []

    # Add characters in custom order
    for char in order:
        if char in count:
            result.append(char * count[char])
            del count[char]

    # Add remaining characters
    for char, freq in count.items():
        result.append(char * freq)

    return ''.join(result)
```

### Complexity Analysis

**Time: O(n + m) - count + iterate. Space: O(1) - max 26 lowercase letters**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, String, Sorting

**Difficulty Level:** MEDIUM

---

*Problem source: [LeetCode](https://leetcode.com/problems/custom-sort-string)*
