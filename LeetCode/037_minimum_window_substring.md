# 037. Minimum Window Substring

**Difficulty:** HARD
**Frequency:** 62.4%
**Acceptance Rate:** 45.4%
**LeetCode Link:** [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring)

---

## Problem Description

Given two strings `s` and `t` of lengths `m` and `n` respectively, return the minimum window substring of `s` such that every character in `t` (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

**Constraints:**
- m == s.length
- n == t.length
- 1 <= m, n <= 10^5
- s and t consist of uppercase and lowercase English letters

---

## Examples

### Example 1
**Input:** `s = "ADOBECODEBANC", t = "ABC"`
**Output:** `"BANC"`
**Explanation:** Minimum window containing all characters A, B, C

### Example 2
**Input:** `s = "a", t = "a"`
**Output:** `"a"`
**Explanation:** Single character match

### Example 3
**Input:** `s = "a", t = "aa"`
**Output:** `""`
**Explanation:** Impossible to find substring with 2 a's when s has only 1

### Example 4
**Input:** `s = "ADOBECODBANC", t = "ABCC"`
**Output:** `"CODBANC"`
**Explanation:** Must include duplicate C's from t

---

## Optimal Solution

### Implementation

```python
def minWindow(s: str, t: str) -> str:
    """
    Find minimum window substring using sliding window.

    Time: O(m+n), Space: O(k) where k is unique chars in t
    """
    if not s or not t:
        return ""

    # Count chars in t
    target = Counter(t)
    required = len(target)
    formed = 0
    window_counts = {}

    # Left, right pointers
    l, r = 0, 0
    # (window length, left, right)
    ans = float('inf'), 0, 0

    while r < len(s):
        # Expand window
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in target and window_counts[char] == target[char]:
            formed += 1

        # Contract window
        while l <= r and formed == required:
            # Update result
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            # Remove from left
            char = s[l]
            window_counts[char] -= 1
            if char in target and window_counts[char] < target[char]:
                formed -= 1
            l += 1

        r += 1

    return "" if ans[0] == float('inf') else s[ans[1]:ans[2]+1]
```

### Complexity Analysis

**Time: O(m+n) - each character visited at most twice. Space: O(k) - unique characters**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, String, Sliding Window

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/minimum-window-substring)*
