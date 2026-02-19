# Math Compute - Comprehensive Guide



## 📋 Problems in This Category

- [021. Pow(x, n)](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Math-Compute/021_powx_n.md) - `Recursive`
- [050. Add Strings](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Math-Compute/050_add_strings.md) - `Iterative+Carry`
- [072. Maximum Swap](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Math-Compute/072_maximum_swap.md) - `Greedy+Digit`
- [085. Add Two Integers](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Math-Compute/085_add_two_integers.md) - `Direct`

---

## Mathematical Properties & Number Theory

---

## 🎯 Overview

**Total Problems:** 4
**Difficulty:** Easy (2) • Medium (2) • Hard (0)

**Core Concept:**
Leverage mathematical properties for optimal solutions

**Key Insight:**
Look for formulas, patterns, and mathematical properties before brute force

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: Number Operations (Pow, GCD, Prime)
### Pattern 2: Digit Manipulation
### Pattern 3: Mathematical Formulas
### Pattern 4: Bit Manipulation


---

## 🎓 Learning Path

Power(x, n) → Add Strings → Maximum Swap → Strobogrammatic Number

---

## ⚠️ Common Pitfalls

1. Integer overflow 2. Negative numbers 3. Division by zero 4. Floating point precision

---

## ✅ Testing Strategy

Test: 0, 1, negative, max int, min int, edge values

---

## 💡 Templates & Code Patterns


```python
# Fast power
def pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    half = pow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x
```


---

## 💎 Mastery Tips

Look for O(log n) solutions. Use bit manipulation when possible.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 021 | [Pow(x, n)](./021_pow_x_n.md) | MEDIUM | 74.9% |
| 050 | [Add Strings](./050_add_strings.md) | EASY | 51.9% |
| 072 | [Maximum Swap](./072_maximum_swap.md) | MEDIUM | 40.7% |
| 085 | [Add Two Integers](./085_add_two_integers.md) | EASY | 32.0% |

---

[← Back to Main](../README.md)
