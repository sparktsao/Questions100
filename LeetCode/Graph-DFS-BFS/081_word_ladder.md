# 081. Word Ladder

**Difficulty:** HARD
**Frequency:** 40.7%
**Acceptance Rate:** 42.8%
**LeetCode Link:** [Word Ladder](https://leetcode.com/problems/word-ladder)

---

## Problem Description

A transformation sequence from word `beginWord` to word `endWord` using a dictionary `wordList` is a sequence of words `beginWord -> s1 -> s2 -> ... -> sk` such that:

- Every adjacent pair of words differs by a single letter
- Every `si` for `1 <= i <= k` is in `wordList`. Note that `beginWord` does not need to be in `wordList`
- `sk == endWord`

Given two words, `beginWord` and `endWord`, and a dictionary `wordList`, return the number of words in the shortest transformation sequence from `beginWord` to `endWord`, or `0` if no such sequence exists.

**Constraints:**
- 1 <= beginWord.length <= 10
- endWord.length == beginWord.length
- 1 <= wordList.length <= 5000
- wordList[i].length == beginWord.length
- All words consist of lowercase English letters
- beginWord != endWord
- All words in wordList are unique

---

## Examples

### Example 1
**Input:** `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]`
**Output:** `5`
**Explanation:** Shortest: "hit" -> "hot" -> "dot" -> "dog" -> "cog"

### Example 2
**Input:** `beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]`
**Output:** `0`
**Explanation:** endWord not in wordList

### Example 3
**Input:** `beginWord = "a", endWord = "c", wordList = ["a","b","c"]`
**Output:** `2`
**Explanation:** a -> c (differ by one letter)

### Example 4
**Input:** `beginWord = "hot", endWord = "dog", wordList = ["hot","dog"]`
**Output:** `0`
**Explanation:** hot and dog differ by 2 letters

---

## Optimal Solution

### Implementation

```python
def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    """
    BFS to find shortest transformation path.

    Time: O(M² × N), Space: O(M² × N)
    where M is word length, N is wordList size
    """
    from collections import deque

    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque([(beginWord, 1)])
    visited = {beginWord}

    while queue:
        word, length = queue.popleft()

        if word == endWord:
            return length

        # Try all possible one-letter changes
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = word[:i] + c + word[i+1:]

                if next_word in word_set and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))

    return 0
```

### Complexity Analysis

**Time: O(M² × N) - for each word try M positions × 26 letters. Space: O(M × N) - queue + visited**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, String, Breadth-First Search

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/word-ladder)*
