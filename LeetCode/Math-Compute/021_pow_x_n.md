# 021. Pow(x, n)

**Difficulty:** MEDIUM
**Frequency:** 74.9%
**Acceptance Rate:** 37.0%
**LeetCode Link:** [Pow(x, n)](https://leetcode.com/problems/powx-n)

---

## Problem Description

Implement `pow(x, n)`, which calculates `x` raised to the power `n` (i.e., `x^n`).

**Constraints:**
- -100.0 < x < 100.0
- -2^31 <= n <= 2^31-1
- -10^4 <= x^n <= 10^4

---

## Examples

### Example 1
**Input:** `x = 2.00000, n = 10`
**Output:** `1024.00000`
**Explanation:** 2^10 = 1024

### Example 2
**Input:** `x = 2.10000, n = 3`
**Output:** `9.26100`
**Explanation:** 2.1^3 = 9.261

### Example 3
**Input:** `x = 2.00000, n = -2`
**Output:** `0.25000`
**Explanation:** 2^-2 = 1/4 = 0.25

### Example 4
**Input:** `x = 0.00001, n = 2147483647`
**Output:** `0.00000`
**Explanation:** Very small number with large exponent

---

## Optimal Solution

### Implementation

```python
def myPow(x: float, n: int) -> float:
    """
    Fast power using binary exponentiation (divide and conquer).

    Time: O(log n), Space: O(log n) for recursion
    """
    def helper(x, n):
        if n == 0:
            return 1.0

        # Calculate half power
        half = helper(x, n // 2)

        if n % 2 == 0:
            return half * half
        else:
            return half * half * x

    result = helper(x, abs(n))
    return result if n >= 0 else 1 / result
```

### Complexity Analysis

**Time: O(log n) - divide problem by 2 each step. Space: O(log n) - recursion depth**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Math, Recursion

**Difficulty Level:** MEDIUM

---

*Problem source: [LeetCode](https://leetcode.com/problems/powx-n)*
