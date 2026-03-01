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

### Why `dp` Has Length `len(s) + 1`

`dp[i]` represents **"can the first `i` characters of `s` be segmented?"** — not the character at index `i`.

```
s:    l  e  e  t  c  o  d  e
idx:  0  1  2  3  4  5  6  7

dp:  [T  ?  ?  ?  ?  ?  ?  ?  ?]
      0  1  2  3  4  5  6  7  8
      ↑                         ↑
    dp[0]=""               dp[8]="leetcode"
```

`dp[i]` corresponds to the prefix `s[0:i]` (Python left-closed, right-open). So for a string of length 8 we need indices 0 through 8 — **9 slots total = `len(s) + 1`**.

### Why `dp[0] = True` (The Base Case)

`dp[0]` represents the empty string `""`. An empty string is trivially segmentable — this is the anchor the whole DP depends on.

Without `dp[0] = True`, the transition can never fire at all:

```python
if dp[j] and s[j:i] in word_set:   # dp[0] must be True for j=0 to ever trigger
    dp[i] = True
```

When `j=0`, `s[0:i]` is the whole prefix from the start. If that word is in the dictionary, `dp[i]` becomes `True` — but only if `dp[0]` is `True`.

### Transition Logic

```
if dp[j] is True  →  s[0:j] is a valid segmentation
and s[j:i] is in wordDict
then dp[i] = True  →  s[0:i] is a valid segmentation
```

Visually for `s = "leetcode"`, `wordDict = ["leet", "code"]`:

```
i=4: j=0, dp[0]=T, s[0:4]="leet" ✓  →  dp[4]=True
i=8: j=4, dp[4]=T, s[4:8]="code" ✓  →  dp[8]=True  ← answer
```

### This Pattern Appears Everywhere in DP

Any DP that defines `dp[i]` as "the first `i` elements" needs `n+1` size and a `dp[0]` base case:

| Problem | `dp[i]` means | Base case |
|---|---|---|
| Word Break | first `i` chars segmentable | `dp[0]=True` (empty string) |
| Decode Ways | first `i` digits decodable | `dp[0]=1` (empty = 1 way) |
| Coin Change | min coins for amount `i` | `dp[0]=0` (0 coins for 0) |
| Climbing Stairs | ways to reach step `i` | `dp[0]=1` |
| Partition Equal Subset | sum `i` achievable | `dp[0]=True` |

### Complexity Analysis

**Time: O(n²)** — for each `i` (n positions), inner loop checks all `j < i`; substring check is O(n) via set lookup after hashing

**Optimized Time: O(n × maxWordLen)** — inner loop only goes back `maxWordLen` steps instead of all the way to 0

**Space: O(n)** — DP array; set storage is O(total chars in wordDict)

---

## Categories & Tags

**Primary Topics:** Array, Hash Table, String, Dynamic Programming, Trie, Memoization

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/word-break)*
