# 056. Remove Invalid Parentheses

**Difficulty:** HARD
**Frequency:** 47.0%
**Acceptance Rate:** 49.2%
**LeetCode Link:** [Remove Invalid Parentheses](https://leetcode.com/problems/remove-invalid-parentheses)

---

## Problem Description

Given a string `s` that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

**Constraints:**
- 1 <= s.length <= 25
- s consists of lowercase English letters and parentheses '(' and ')'
- There will be at most 20 parentheses in s

---

## Examples

### Example 1
**Input:** `s = "()())()"`
**Output:** `["(())()","()()()"]`
**Explanation:** Remove one ')' to make it valid. Two possible results.

### Example 2
**Input:** `s = "(a)())()"`
**Output:** `["(a())()","(a)()()"]`
**Explanation:** Remove one ')' at index 4 or 5

### Example 3
**Input:** `s = ")("`
**Output:** `[""]`
**Explanation:** Both parentheses are invalid, remove both

### Example 4
**Input:** `s = "()"`
**Output:** `["()"]`
**Explanation:** String is already valid

---

## Optimal Solution

### Implementation (BFS)

```python
from collections import deque

def removeInvalidParentheses(s: str) -> List[str]:
    """
    BFS to find all valid strings with minimum removals.

    Time: O(2^n) worst case, Space: O(2^n)
    """
    def is_valid(s: str) -> bool:
        """Check if string has valid parentheses."""
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    # BFS to generate strings by removing one char at a time
    queue = deque([s])
    visited = {s}
    result = []
    found = False

    while queue:
        current = queue.popleft()

        if is_valid(current):
            result.append(current)
            found = True

        # If we found valid strings, don't go deeper
        if found:
            continue

        # Generate next level by removing one parenthesis
        for i in range(len(current)):
            if current[i] not in '()':
                continue

            next_str = current[:i] + current[i+1:]
            if next_str not in visited:
                visited.add(next_str)
                queue.append(next_str)

    return result
```

### Alternative Implementation (DFS with Pruning)

```python
def removeInvalidParentheses(s: str) -> List[str]:
    """
    DFS with early pruning based on minimum removals needed.

    Time: O(2^n), Space: O(n) for recursion stack
    """
    def calc_removals(s: str) -> tuple:
        """Calculate minimum left and right parentheses to remove."""
        left_remove = right_remove = 0
        for char in s:
            if char == '(':
                left_remove += 1
            elif char == ')':
                if left_remove > 0:
                    left_remove -= 1
                else:
                    right_remove += 1
        return left_remove, right_remove

    def is_valid(s: str) -> bool:
        """Check if string has valid parentheses."""
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def dfs(s: str, start: int, left_rem: int, right_rem: int, result: set) -> None:
        """DFS to find all valid strings."""
        if left_rem == 0 and right_rem == 0:
            if is_valid(s):
                result.add(s)
            return

        for i in range(start, len(s)):
            # Skip duplicates
            if i > start and s[i] == s[i-1]:
                continue

            if s[i] == '(' and left_rem > 0:
                dfs(s[:i] + s[i+1:], i, left_rem - 1, right_rem, result)
            elif s[i] == ')' and right_rem > 0:
                dfs(s[:i] + s[i+1:], i, left_rem, right_rem - 1, result)

    left_rem, right_rem = calc_removals(s)
    result = set()
    dfs(s, 0, left_rem, right_rem, result)
    return list(result)
```

### Complexity Analysis

**BFS Approach:**
- **Time:** O(2^n) in worst case where we try removing each character
  - Each string can generate up to n new strings
  - Validation takes O(n) per string
- **Space:** O(2^n) for queue and visited set in worst case

**DFS Approach:**
- **Time:** O(2^n) but with better pruning in practice
  - Pre-calculating removals reduces search space significantly
  - Skip duplicate characters for optimization
- **Space:** O(n) for recursion stack, plus O(n * 2^n) for result storage

**Why BFS is Often Preferred:**
- Naturally finds minimum removal level (breadth-first)
- Once valid strings found at a level, stop going deeper
- Easier to understand and implement
- Better for finding all solutions at minimum removal count

---

## Categories & Tags

**Primary Topics:** String, Backtracking, Breadth-First Search

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/remove-invalid-parentheses)*
