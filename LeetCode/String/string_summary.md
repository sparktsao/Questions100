# String - Comprehensive Guide


## 📋 Problems in This Category

- [043. Longest Common Prefix](043_longest_common_prefix.md) - `Vertical Scan`
- [046. Diagonal Traverse](046_diagonal_traverse.md) - `Diagonal Sim`
- [047. Missing Ranges](047_missing_ranges.md) - `Gap Check`
- [058. Valid Number](058_valid_number.md) - `DFA Validation`
- [067. String to Integer](067_string_to_integer.md) - `Parse+Validate`
- [095. Goat Latin](095_goat_latin.md) - `Transform`
- [097. Text Justification](097_text_justification.md) - `Greedy Pack`

---

## StringBuilder, Two Pointers, & Pattern Matching

---

## 🎯 Overview

**Total Problems:** 7
**Difficulty:** Easy (3) • Medium (2) • Hard (2)

**Core Concept:**
String manipulation using efficient techniques and pattern recognition

**Key Insight:**
Use StringBuilder for concatenation, two pointers for reversal, KMP for pattern matching

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: String Parsing & Transformation
### Pattern 2: Pattern Matching (KMP, Rabin-Karp)
### Pattern 3: String Compression & Encoding
### Pattern 4: Anagrams & Permutations


---

## 🎓 Learning Path

Reverse String → Add Strings → String to Integer → Group Anagrams

---

## ⚠️ Common Pitfalls

1. String immutability 2. Not handling empty 3. Unicode issues 4. Case sensitivity

---

## ✅ Testing Strategy

Test: empty, single char, spaces, special chars, unicode, very long

---

## 💡 Templates & Code Patterns


```python
# Use list for mutable string
chars = list(s)
# ... modify
result = ''.join(chars)

# Two pointers for reversal
def reverse(s):
    left, right = 0, len(s) - 1
    s = list(s)
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)
```


---

## 💎 Mastery Tips

Strings are immutable in Python. Use list for modifications. Join at end.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 043 | [Longest Common Prefix](./043_longest_common_prefix.md) | EASY | 59.4% |
| 046 | [Diagonal Traverse](./046_diagonal_traverse.md) | MEDIUM | 56.0% |
| 047 | [Missing Ranges](./047_missing_ranges.md) | EASY | 56.0% |
| 058 | [Valid Number](./058_valid_number.md) | HARD | 47.0% |
| 067 | [String to Integer (atoi)](./067_string_to_integer_atoi.md) | MEDIUM | 40.7% |
| 095 | [Goat Latin](./095_goat_latin.md) | EASY | 32.0% |
| 097 | [Text Justification](./097_text_justification.md) | HARD | 32.0% |

---

[← Back to Main](../README.md)
