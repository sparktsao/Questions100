# Palindrome - Comprehensive Guide

## Expand from Center vs Two Pointers

---

## 🎯 Overview

**Total Problems:** 5
**Difficulty:** Easy (2) • Medium (2) • Hard (1)

**Core Concept:**
Check symmetry using expand-from-center or two-pointer techniques

**Key Insight:**
Two pointers from edges or expand from each possible center

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: Two Pointers from Edges (Verification)
### Pattern 2: Expand from Center (Finding All)
### Pattern 3: DP for Palindrome Substrings
### Pattern 4: Manacher's Algorithm (Advanced)


---

## 🎓 Learning Path

Valid Palindrome → Longest Palindromic Substring → Palindrome Partitioning

---

## ⚠️ Common Pitfalls

1. Not handling even/odd length 2. Case sensitivity 3. Special characters 4. Empty string

---

## ✅ Testing Strategy

Test: empty, single, even length, odd length, no palindrome, all same

---

## 💡 Templates & Code Patterns


```python
# Expand from center
def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

# Two pointers
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```


---

## 💎 Mastery Tips

Expand from every index (both odd and even centers). Two pointers for validation.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 004 | [Valid Palindrome II](./004_valid_palindrome_ii.md) | EASY | 92.7% |
| 029 | [Valid Palindrome](./029_valid_palindrome.md) | EASY | 69.5% |
| 057 | [Palindromic Substrings](./057_palindromic_substrings.md) | MEDIUM | 47.0% |
| 083 | [Valid Palindrome III](./083_valid_palindrome_iii.md) | HARD | 40.7% |
| 096 | [Longest Palindromic Substring](./096_longest_palindromic_substring.md) | MEDIUM | 32.0% |

---

[← Back to Main](../README.md)
