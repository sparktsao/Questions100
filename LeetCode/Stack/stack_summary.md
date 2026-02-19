# Stack - Comprehensive Guide




## 📋 Problems in This Category

- [008. Basic Calculator II](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Stack/008_basic_calculator_ii.md) - `Stack+Operator`
- [035. Simplify Path](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Stack/035_simplify_path.md) - `Stack+Path`
- [049. Exclusive Time of Functions](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Stack/049_exclusive_time_of_functions.md) - `Stack+Time`
- [093. Decode String](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Stack/093_decode_string.md) - `Stack+Nested`
- [098. Remove Adjacent Duplicates II](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Stack/098_remove_all_adjacent_duplicates_in_string_ii.md) - `Stack+Count`

---

## LIFO for Nested Structures & Backtracking

---

## 🎯 Overview

**Total Problems:** 5
**Difficulty:** Easy (0) • Medium (5) • Hard (0)

**Core Concept:**
Stack (Last-In-First-Out) perfect for nested structures, parsing, and operations needing reversal

**Key Insight:**
Use stack when you need to process inner elements before outer (nested), or when you need to backtrack.

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: Matching Pairs (Parentheses, Brackets)
### Pattern 2: Expression Evaluation (Calculator, Postfix)
### Pattern 3: Monotonic Stack (Next Greater Element)
### Pattern 4: DFS Simulation with Explicit Stack


---

## 🎓 Learning Path

Valid Parentheses → Basic Calculator II → Exclusive Time → Simplify Path

---

## ⚠️ Common Pitfalls

1. Not checking empty before pop 2. Not clearing stack between operations 3. Wrong order of operations

---

## ✅ Testing Strategy

Test: empty, single element, nested, flat, invalid input

---

## 💡 Templates & Code Patterns


```python
stack = []
for char in s:
    if opening:
        stack.append(char)
    else:
        if not stack or not matches(stack[-1], char):
            return False
        stack.pop()
return len(stack) == 0
```


---

## 💎 Mastery Tips

Stack is LIFO - most recent first. Use for nesting, reversal, backtracking.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 008 | [Basic Calculator II](./008_basic_calculator_ii.md) | MEDIUM | 84.0% |
| 035 | [Simplify Path](./035_simplify_path.md) | MEDIUM | 65.0% |
| 049 | [Exclusive Time of Functions](./049_exclusive_time_of_functions.md) | MEDIUM | 56.0% |
| 093 | [Decode String](./093_decode_string.md) | MEDIUM | 32.0% |
| 098 | [Remove All Adjacent Duplicates in String II](./098_remove_all_adjacent_duplicates_in_string_ii.md) | MEDIUM | 32.0% |

---

[← Back to Main](../README.md)
