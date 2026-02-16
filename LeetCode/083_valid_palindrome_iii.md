# 083. Valid Palindrome III

**Difficulty:** HARD
**Frequency:** 40.7%
**Acceptance Rate:** 49.1%
**LeetCode Link:** [Valid Palindrome III](https://leetcode.com/problems/valid-palindrome-iii)

---

## Problem Description

Given a string `s` and an integer `k`, return `true` if `s` is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most `k` characters from it.

**Constraints:**
- 1 <= s.length <= 1000
- s consists only of lowercase English letters
- 1 <= k <= s.length

---

## Examples

### Example 1
**Input:** `s = "abcdeca", k = 2`
**Output:** `true`
**Explanation:** Remove 'b' and 'e' characters to get "acdca" which is a palindrome

### Example 2
**Input:** `s = "abbababa", k = 1`
**Output:** `true`
**Explanation:** Remove one 'b' to create a palindrome

### Example 3
**Input:** `s = "abcde", k = 1`
**Output:** `false`
**Explanation:** Need to remove at least 2 characters to make palindrome

### Example 4
**Input:** `s = "racecar", k = 0`
**Output:** `true`
**Explanation:** Already a palindrome, no removal needed

---

## Optimal Solution

### Implementation

```python
def isValidPalindrome(s: str, k: int) -> bool:
    """
    Check if string can become palindrome by removing at most k characters.

    Uses DP to find longest palindromic subsequence.
    Time: O(n²), Space: O(n²)
    """
    n = len(s)

    # dp[i][j] = length of longest palindromic subsequence in s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Single characters are palindromes of length 1
    for i in range(n):
        dp[i][i] = 1

    # Fill DP table for substrings of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                # Characters match, add 2 to inner subsequence
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # Characters don't match, take max of removing left or right
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # Longest palindromic subsequence length
    lps = dp[0][n - 1]

    # Need to remove (n - lps) characters
    # Check if removals needed <= k
    return n - lps <= k
```

### Alternative Space-Optimized Solution

```python
def isValidPalindrome(s: str, k: int) -> bool:
    """
    Space-optimized version using 2 rows.

    Time: O(n²), Space: O(n)
    """
    n = len(s)
    prev = [0] * n
    curr = [0] * n

    for i in range(n):
        prev[i] = 1

    for i in range(n - 1, -1, -1):
        curr[i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                curr[j] = prev[j - 1] + 2
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev

    return n - prev[n - 1] <= k
```

### Complexity Analysis

**Time: O(n²) - fill DP table. Space: O(n²) - DP table storage**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Dynamic programming avoids exponential recalculation
- Each subproblem solved exactly once
- Handles all edge cases correctly including empty strings and full removals

---

## Categories & Tags

**Primary Topics:** String, Dynamic Programming

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/valid-palindrome-iii)*
