# 075. Word Break

**Difficulty:** MEDIUM
**Frequency:** 40.7%
**Acceptance Rate:** 48.3%
**LeetCode Link:** [Word Break](https://leetcode.com/problems/word-break)

---

## Problem Description

Given a string `s` and a dictionary of strings `wordDict`, return `true` if `s` can be segmented into a space-separated sequence of one or more dictionary words.

**Note:** The same word in the dictionary may be reused multiple times in the segmentation.

**Constraints:**
- `1 <= s.length <= 300`
- `1 <= wordDict.length <= 1000`
- `1 <= wordDict[i].length <= 20`
- `s` and `wordDict[i]` consist of only lowercase English letters
- All the strings of `wordDict` are unique

---

## Examples

### Example 1
**Input:** `s = "leetcode", wordDict = ["leet","code"]`
**Output:** `true`
**Explanation:** Return true because "leetcode" can be segmented as "leet code".

### Example 2
**Input:** `s = "applepenapple", wordDict = ["apple","pen"]`
**Output:** `true`
**Explanation:** Return true because "applepenapple" can be segmented as "apple pen apple". Note that you are allowed to reuse a dictionary word.

### Example 3
**Input:** `s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]`
**Output:** `false`
**Explanation:** No valid segmentation exists. "catsand" + "og" doesn't work because "og" is not in the dictionary.

### Example 4
**Input:** `s = "cars", wordDict = ["car","ca","rs"]`
**Output:** `true`
**Explanation:** Can be segmented as "car s" or "ca rs".

---

## Optimal Solution

### Implementation

```python
def wordBreak(s: str, wordDict: List[str]) -> bool:
    """
    Dynamic programming solution to check if string can be segmented.

    Time: O(n² × m), Space: O(n)
    where n is string length, m is average word length
    """
    word_set = set(wordDict)
    n = len(s)

    # dp[i] = True if s[0:i] can be segmented
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string is valid

    for i in range(1, n + 1):
        for j in range(i):
            # Check if s[0:j] is valid AND s[j:i] is in dictionary
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # Found valid segmentation for s[0:i]

    return dp[n]
```

### Alternative Implementation (Optimized)

```python
def wordBreak(s: str, wordDict: List[str]) -> bool:
    """
    Optimized DP with max word length constraint.

    Time: O(n × m × k), Space: O(n)
    where k is max word length
    """
    word_set = set(wordDict)
    max_len = max(len(word) for word in wordDict)
    n = len(s)

    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        # Only check substrings up to max word length
        for j in range(max(0, i - max_len), i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]
```

### Complexity Analysis

**Time: O(n² × m) - nested loops with substring operations. Space: O(n) - DP array plus set storage**

**Optimized Time: O(n × k × m) - where k is max word length, typically much better in practice**

**Why This is Optimal:**
- DP approach avoids redundant computation by memoizing subproblem solutions
- Converting wordDict to set provides O(1) average lookup time
- Early termination (break) once valid segmentation found for position i
- Bottom-up DP eliminates recursion overhead
- Optimization using max word length significantly reduces inner loop iterations

---

## Categories & Tags

**Primary Topics:** Array, Hash Table, String, Dynamic Programming, Trie, Memoization

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/word-break)*
