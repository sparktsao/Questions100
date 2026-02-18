# Parentheses - Comprehensive Guide

## Stack for Matching & Counting for Validation

---

## 🎯 Overview

**Total Problems:** 4
**Difficulty:** Easy (1) • Medium (2) • Hard (1)

**Core Concept:**
Use stack for matching pairs, counter for simple validation

**Key Insight:**
Stack tracks opening brackets, counter tracks balance

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: Valid Parentheses (Stack)
### Pattern 2: Remove Invalid Parentheses (BFS or Backtracking)
### Pattern 3: Minimum Add/Remove (Counter + Stack)
### Pattern 4: Generate Parentheses (Backtracking)


---

## 🎓 Learning Path

Valid Parentheses → Minimum Remove → Minimum Add → Generate Parentheses

---

## ⚠️ Common Pitfalls

1. Not checking stack empty 2. Wrong matching logic 3. Not handling edge cases 4. Counter overflow

---

## ✅ Testing Strategy

Test: empty, single, balanced, unbalanced, nested, interleaved

---

## 💡 Templates & Code Patterns


```python
# Stack matching
def is_valid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0
```


---

## 💎 Mastery Tips

Stack for matching pairs. Counter for balance. Always check empty before pop.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 001 | [Minimum Remove to Make Valid Parentheses](./001_minimum_remove_to_make_valid_parentheses.md) | MEDIUM | 100.0% |
| 020 | [Valid Parentheses](./020_valid_parentheses.md) | EASY | 74.9% |
| 052 | [Minimum Add to Make Parentheses Valid](./052_minimum_add_to_make_parentheses_valid.md) | MEDIUM | 51.9% |
| 056 | [Remove Invalid Parentheses](./056_remove_invalid_parentheses.md) | HARD | 47.0% |

---

[← Back to Main](../README.md)
