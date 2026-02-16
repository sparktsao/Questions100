# 035. Simplify Path

**Difficulty:** MEDIUM
**Frequency:** 65.0%
**Acceptance Rate:** 47.9%
**LeetCode Link:** [Simplify Path](https://leetcode.com/problems/simplify-path)

---

## Problem Description

You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

The rules of a Unix-style file system are as follows:
- A single period '.' represents the current directory
- A double period '..' represents the previous/parent directory
- Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'
- Any sequence of periods that does not match the rules above should be treated as a valid directory or file name (e.g., '...' and '....' are valid names)

The simplified canonical path should follow this format:
- The path must start with a single slash '/'
- Directories within the path must be separated by exactly one slash '/'
- The path must not end with a slash '/', unless it is the root directory
- The path must not have '.' or '..' as directory names

**Constraints:**
- 1 <= path.length <= 3000
- path consists of English letters, digits, period '.', slash '/', or underscore '_'
- path is a valid absolute Unix path

---

## Examples

### Example 1
**Input:** `path = "/home/"`
**Output:** `"/home"`
**Explanation:** The trailing slash should be removed

### Example 2
**Input:** `path = "/home//foo/"`
**Output:** `"/home/foo"`
**Explanation:** Multiple consecutive slashes are replaced by a single one

### Example 3
**Input:** `path = "/home/user/Documents/../Pictures"`
**Output:** `"/home/user/Pictures"`
**Explanation:** A double period ".." refers to the directory up a level

### Example 4
**Input:** `path = "/../"`
**Output:** `"/"`
**Explanation:** Going one level up from root is not possible, stay at root

---

## Optimal Solution

### Implementation

```python
def simplifyPath(path: str) -> str:
    """
    Use stack to handle directory navigation.

    Time: O(n), Space: O(n)
    """
    # Split by '/' and filter out empty strings and '.'
    components = path.split('/')
    stack = []

    for component in components:
        if component == '..' :
            # Go up one directory (pop from stack if possible)
            if stack:
                stack.pop()
        elif component and component != '.':
            # Valid directory name (not empty, not '.')
            stack.append(component)
        # Ignore empty strings and '.'

    # Build simplified path
    return '/' + '/'.join(stack)
```

### Alternative Implementation (More Explicit)

```python
def simplifyPath(path: str) -> str:
    """
    Explicit handling of each case.

    Time: O(n), Space: O(n)
    """
    stack = []
    parts = path.split('/')

    for part in parts:
        if part == '' or part == '.':
            # Empty or current directory - skip
            continue
        elif part == '..':
            # Parent directory - go back if possible
            if stack:
                stack.pop()
        else:
            # Valid directory name
            stack.append(part)

    # Join with '/' and prepend root '/'
    return '/' + '/'.join(stack)
```

### Complexity Analysis

**Time: O(n) - single pass through path. Space: O(n) - stack storage**

**Why This is Optimal:**
- Stack naturally handles directory navigation
- Single pass through the input
- Handles all special cases (., .., //, empty)
- Clean separation of parsing and path construction

---

## Categories & Tags

**Primary Topics:** String, Stack

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/simplify-path)*
