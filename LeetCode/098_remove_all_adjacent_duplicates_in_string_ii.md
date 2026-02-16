# 098. Remove All Adjacent Duplicates in String II

**Difficulty:** MEDIUM
**Frequency:** 32.0%
**Acceptance Rate:** 59.6%
**LeetCode Link:** [Remove All Adjacent Duplicates in String II](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii)

---

## Problem Description

You are given a string `s` and an integer `k`, a k duplicate removal consists of choosing `k` adjacent and equal letters from `s` and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make `k` duplicate removals on `s` until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

**Constraints:**
- 1 <= s.length <= 10^5
- 2 <= k <= 10^4
- s only contains lowercase English letters

---

## Examples

### Example 1
**Input:** `s = "abcd", k = 2`
**Output:** `"abcd"`
**Explanation:** There are no k consecutive equal characters, so nothing is deleted

### Example 2
**Input:** `s = "deeedbbcccbdaa", k = 3`
**Output:** `"aa"`
**Explanation:**
- First delete "eee" and "ccc", get "ddbbbdaa"
- Then delete "bbb", get "dddaa"
- Finally delete "ddd", get "aa"

### Example 3
**Input:** `s = "pbbcggttciiippooaais", k = 2`
**Output:** `"ps"`
**Explanation:**
- Remove "bb" → "pcggttciiippooaais"
- Remove "gg" → "pcttciiippooaais"
- Remove "tt" → "pcciiippooaais"
- Remove "cc" → "piiippooaais"
- Remove "ii" → "ppippooaais"
- Remove "pp" → "ippooaais"
- Remove "pp" → "iooaais"
- Remove "oo" → "iaais"
- Remove "aa" → "iis"
- Remove "ii" → "s"
- Final: "ps" (after removing all consecutive duplicates)

### Example 4
**Input:** `s = "aaaaa", k = 3`
**Output:** `"aa"`
**Explanation:** Remove "aaa" from the middle, leaving "aa"

---

## Optimal Solution

### Implementation

```python
def removeDuplicates(s: str, k: int) -> str:
    """
    Stack-based solution to remove k adjacent duplicates.

    Time: O(n), Space: O(n)
    """
    # Stack stores [character, count] pairs
    stack = []

    for char in s:
        if stack and stack[-1][0] == char:
            # Same character, increment count
            stack[-1][1] += 1

            # Remove if we reach k duplicates
            if stack[-1][1] == k:
                stack.pop()
        else:
            # New character, add to stack
            stack.append([char, 1])

    # Rebuild string from stack
    return ''.join(char * count for char, count in stack)
```

### Alternative Implementation (Two Pointers)

```python
def removeDuplicates(s: str, k: int) -> str:
    """
    Two-pointer approach using list as stack.

    Time: O(n), Space: O(n)
    """
    # Convert to list for in-place modification
    chars = list(s)
    counts = [0] * len(s)
    i = 0  # Stack pointer

    for j in range(len(s)):
        chars[i] = chars[j]
        counts[i] = 1 if i == 0 or chars[i] != chars[i-1] else counts[i-1] + 1

        # Remove k duplicates
        if counts[i] == k:
            i -= k

        i += 1

    return ''.join(chars[:i])
```

### Complexity Analysis

**Time: O(n) - each character pushed/popped at most once. Space: O(n) - stack storage**

**Why This is Optimal:**
- Single pass through the string - cannot do better than O(n)
- Stack ensures efficient removal of k consecutive characters
- Each character is processed exactly once
- Space complexity is optimal as we need to store the result
- Handles cascading removals automatically through stack mechanism

---

## Categories & Tags

**Primary Topics:** String, Stack

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii)*
