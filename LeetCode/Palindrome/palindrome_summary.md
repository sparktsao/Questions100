# Palindrome Problems - Comprehensive Analysis

## 🎯 Category Overview

**Total Problems:** 5
**Difficulty Range:** Easy → Hard
**Core Concept:** Palindrome validation, finding, and counting using two-pointers, expand-around-center, and dynamic programming

**🔑 Key Insight:** Choose approach based on task:
- **Two-Pointers** → Validation (O(n) time, O(1) space)
- **Expand Around Center** → Counting/Finding (O(n²) time, O(1) space)
- **Dynamic Programming** → Complex validation with k deletions (O(n²) time/space)

---

## 📊 Problem Progression Map

```
Level 1: Valid Palindrome (#029) - Basic Validation (EASIEST)
    ↓
Level 2: Valid Palindrome II (#004) - Validation with 1 Deletion
    ↓
Level 3: Palindromic Substrings (#057) - Count All Palindromes
    ↓
Level 4: Longest Palindromic Substring (#096) - Find Longest
    ↓
Level 5: Valid Palindrome III (#083) - Validation with K Deletions (HARDEST)
```

---

## 🔍 The Three Paradigms

### Paradigm A: Two-Pointers Validation
**When:** Check if string is palindrome or can become one with limited deletions
**Key:** Opposite-direction pointers, try skipping on mismatch
**Examples:** #029, #004
**Complexity:** O(n) time, O(1) space

### Paradigm B: Expand Around Center
**When:** Count palindromes or find longest palindrome
**Key:** Try all possible centers (n centers for odd, n-1 for even)
**Examples:** #057, #096
**Complexity:** O(n²) time, O(1) space

### Paradigm C: Dynamic Programming
**When:** Complex validation with multiple deletions allowed
**Key:** Find longest palindromic subsequence (LPS)
**Examples:** #083
**Complexity:** O(n²) time, O(n²) or O(n) space

---

## 📖 Problem-by-Problem Analysis

### 1️⃣ **Problem #029: Valid Palindrome** (EASY)

**🎯 Task:** Check if string is palindrome (ignore non-alphanumeric, case-insensitive)
**📥 Input:** String with mixed characters
**📤 Output:** Boolean
**🏷️ Tag:** Two Pointers, Validation

#### Algorithm
```python
def isPalindrome(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric from left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric from right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

#### Key Insight
> **Character Filtering:** Use inner while loops to skip invalid characters in-place

#### Complexity
- **Time:** O(n) - single pass
- **Space:** O(1) - constant

---

### 2️⃣ **Problem #004: Valid Palindrome II** (EASY)

**🎯 Task:** Check if string can be palindrome after deleting at most 1 character
**📥 Input:** String
**📤 Output:** Boolean
**🏷️ Tag:** Two Pointers, Greedy

#### The Key Insight!
```
When mismatch found at s[left] != s[right]:
Try BOTH options:
  1. Skip left character: check s[left+1...right]
  2. Skip right character: check s[left...right-1]

If EITHER forms palindrome → return True
```

#### Algorithm
```python
def validPalindrome(s: str) -> bool:
    def is_palindrome(left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    left, right = 0, len(s) - 1

    while left < right:
        if s[left] != s[right]:
            # Try skipping either left OR right
            return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)
        left += 1
        right -= 1

    return True
```

#### Key Insight
> **Greedy Choice:** On first mismatch, try both skip options; if either works, answer is True

#### Complexity
- **Time:** O(n) - at most one extra scan
- **Space:** O(1) - constant

---

### 3️⃣ **Problem #057: Palindromic Substrings** (MEDIUM)

**🎯 Task:** Count all palindromic substrings
**📥 Input:** String
**📤 Output:** Count of palindromes
**🏷️ Tag:** Expand Around Center

#### The Expand Around Center Technique!
```
For each position i:
  1. Odd-length palindromes: expand from (i, i)
  2. Even-length palindromes: expand from (i, i+1)

Total centers: 2n - 1
Time per center: O(n) worst case
Total: O(n²)
```

#### Algorithm
```python
def countSubstrings(s: str) -> int:
    def expand_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    total = 0

    for i in range(len(s)):
        # Odd length palindromes (single center)
        total += expand_around_center(i, i)

        # Even length palindromes (two centers)
        total += expand_around_center(i, i + 1)

    return total
```

#### Why Expand Around Center?
```
Example: "aaa"
i=0: center 'a' → finds "a"
     center "aa" → finds "aa"
i=1: center 'a' → finds "a"
     center "aa" → finds "aa"
i=2: center 'a' → finds "a"
     (no even center after last char)

Also finds "aaa" when expanding from i=1 center

Total: 6 palindromes ✓
```

#### Key Insight
> **All Centers:** Try all 2n-1 possible centers to count all palindromes

#### Complexity
- **Time:** O(n²) - n centers × O(n) expansion
- **Space:** O(1) - constant

---

### 4️⃣ **Problem #096: Longest Palindromic Substring** (MEDIUM)

**🎯 Task:** Find longest palindromic substring
**📥 Input:** String
**📤 Output:** Longest palindrome substring
**🏷️ Tag:** Expand Around Center

#### Algorithm
```python
def longestPalindrome(s: str) -> str:
    if not s:
        return ""

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1  # Length

    start = 0
    max_len = 0

    for i in range(len(s)):
        # Odd length palindromes
        len1 = expand_around_center(i, i)
        # Even length palindromes
        len2 = expand_around_center(i, i + 1)

        current_max = max(len1, len2)
        if current_max > max_len:
            max_len = current_max
            start = i - (current_max - 1) // 2

    return s[start:start + max_len]
```

#### Difference from #057
```
#057 (Count):     Increment count during expansion
#096 (Longest):   Track max length and start position

Same technique, different tracking!
```

#### Key Insight
> **Track Maximum:** Same expand-around-center, but track longest found

#### Complexity
- **Time:** O(n²) - n centers × O(n) expansion
- **Space:** O(1) - constant (result string not counted)

---

### 5️⃣ **Problem #083: Valid Palindrome III** (HARD)

**🎯 Task:** Check if string can become palindrome by removing at most k characters
**📥 Input:** String + k
**📤 Output:** Boolean
**🏷️ Tag:** Dynamic Programming, Longest Palindromic Subsequence

#### The DP Insight!
```
Key Question: How many characters must be removed?
Answer: n - LPS (n = length, LPS = longest palindromic subsequence)

If (n - LPS) <= k → True
```

#### What is Longest Palindromic Subsequence (LPS)?
```
String: "abcdeca"
LPS: "acdca" (length 5)
Characters to remove: 7 - 5 = 2

If k >= 2 → can make palindrome ✓
```

#### Algorithm
```python
def isValidPalindrome(s: str, k: int) -> bool:
    n = len(s)

    # dp[i][j] = length of LPS in s[i:j+1]
    dp = [[0] * n for _ in range(n)]

    # Single characters are palindromes
    for i in range(n):
        dp[i][i] = 1

    # Fill for substrings of increasing length
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                # Characters match → add 2 to inner LPS
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                # Don't match → take max of removing left or right
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    # LPS of entire string
    lps = dp[0][n - 1]

    # Check if removals needed <= k
    return n - lps <= k
```

#### DP Recurrence Relation
```python
if s[i] == s[j]:
    dp[i][j] = dp[i+1][j-1] + 2  # Include both characters
else:
    dp[i][j] = max(dp[i+1][j], dp[i][j-1])  # Skip one character
```

#### Example Walkthrough
```
s = "abcdeca", k = 2

DP table (LPS lengths):
    a b c d e c a
a   1 1 1 1 1 3 5
  b   1 1 1 1 3 3
    c   1 1 1 3 3
      d   1 1 1 1
        e   1 1 1
          c   1 1
            a   1

LPS = dp[0][6] = 5 ("acdca")
Removals needed = 7 - 5 = 2
2 <= 2 → True ✓
```

#### Key Insight
> **LPS via DP:** Find longest palindromic subsequence, check if removals <= k

#### Complexity
- **Time:** O(n²) - fill DP table
- **Space:** O(n²) - DP table (can optimize to O(n))

---

## 🔄 Algorithm Relationships

### Can Previous Solutions Be Modified?

| From | To | Possible? | How? |
|------|-----|-----------|------|
| #029 → #004 | Yes | Add helper + try both skips on mismatch |
| #004 → #083 | No | Different approach (greedy → DP) |
| #057 → #096 | Yes | Same technique, track max instead of count |
| #029 → #057 | No | Validation → counting requires expansion |

---

## 💡 Key Learning Insights

### 1. **Two-Pointers Validation Template**
```python
# Basic palindrome check
def is_palindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# With character filtering
def is_palindrome_filtered(s):
    left, right = 0, len(s) - 1
    while left < right:
        # Skip invalid characters
        while left < right and not valid(s[left]):
            left += 1
        while left < right and not valid(s[right]):
            right -= 1

        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

### 2. **Expand Around Center Template**
```python
def expand_around_center(s, left, right):
    """Returns length or count depending on usage"""
    count = 0
    while left >= 0 and right < len(s) and s[left] == s[right]:
        count += 1  # For counting
        left -= 1
        right += 1
    return count

# Apply to all centers
for i in range(len(s)):
    # Odd length
    result += expand_around_center(s, i, i)
    # Even length
    result += expand_around_center(s, i, i + 1)
```

### 3. **Longest Palindromic Subsequence DP**
```python
def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    # Base case: single characters
    for i in range(n):
        dp[i][i] = 1

    # Fill table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]
```

### 4. **Pattern Recognition**
```
Task: Validate → Two-Pointers
Task: Count all → Expand Around Center
Task: Find longest → Expand Around Center
Task: K deletions → DP (LPS)

Constraint: O(1) space → Two-Pointers or Expand
Constraint: Need subsequence → DP
```

---

## 🎨 Visual Comparison Table

| Problem | Approach | Key Technique | Time | Space |
|---------|----------|---------------|------|-------|
| #029 | Two-Pointers | Skip non-alphanumeric | O(n) | O(1) |
| #004 | Two-Pointers | Try both skip options | O(n) | O(1) |
| #057 | Expand Center | Count at each center | O(n²) | O(1) |
| #096 | Expand Center | Track max length | O(n²) | O(1) |
| #083 | DP | LPS, check removals | O(n²) | O(n²) |

---

## 🚀 Recommended Study Order

1. **Basic Validation:** #029 (Valid Palindrome)
2. **Greedy Extension:** #004 (Valid Palindrome II)
3. **Expand Technique:** #057 (Count Palindromes)
4. **Expand Variant:** #096 (Longest Palindrome)
5. **DP Approach:** #083 (K Deletions)

---

## 📝 Interview Tips

### Common Mistakes

1. **#029:** Forgetting case-insensitive comparison or alphanumeric check
2. **#004:** Only trying to skip one side instead of both
3. **#057:** Forgetting even-length palindromes (center between chars)
4. **#096:** Incorrect start position calculation: `i - (max_len - 1) // 2`
5. **#083:** Computing LCS instead of LPS, or wrong base cases

### Pattern Recognition
```
"is palindrome" → Two-Pointers O(n)
"count palindromes" → Expand Around Center O(n²)
"longest palindrome" → Expand Around Center O(n²)
"k deletions" → DP (LPS) O(n²)

Space: O(1) → Two-Pointers or Expand
Space: O(n²) → DP
```

### Optimization Notes
```
Expand Around Center:
- Can't do better than O(n²) for counting/finding
- Already O(1) space

DP for K Deletions:
- Can optimize space to O(n) using rolling arrays
- Time O(n²) is optimal for this problem
```

---

## 🎓 Practice Progression

### Week 1: Master Two-Pointers
- Day 1-2: #029 (Basic validation)
- Day 3-4: #004 (With deletion)
- Day 5: Combine and practice variants

### Week 2: Expand Around Center
- Day 1-2: #057 (Count all)
- Day 3-4: #096 (Find longest)
- Day 5: Compare approaches, edge cases

### Week 3: Advanced DP
- Day 1-3: #083 (K deletions, LPS)
- Day 4: Space optimization
- Day 5: Review all 5 problems

---

**Summary:** Palindrome problems use three main approaches: two-pointers for O(n) validation (#029, #004), expand-around-center for O(n²) counting/finding (#057, #096), and dynamic programming for complex validation with k deletions (#083). Master the two-pointers template for basic checks, understand the 2n-1 centers for expansion (n odd + n-1 even), and learn LPS (longest palindromic subsequence) DP for advanced problems. Key insight: validation is O(n) with two-pointers, but counting/finding all requires O(n²) expansion. The progression shows evolution from simple validation to greedy extension to comprehensive counting to DP-based subsequence problems.
