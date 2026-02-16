# 072. Maximum Swap

**Difficulty:** MEDIUM
**Frequency:** 40.7%
**Acceptance Rate:** 51.8%
**LeetCode Link:** [Maximum Swap](https://leetcode.com/problems/maximum-swap)

---

## Problem Description

You are given an integer `num`. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

**Constraints:**
- 0 <= num <= 10^8

---

## Examples

### Example 1
**Input:** `num = 2736`
**Output:** `7236`
**Explanation:** Swap 2 and 7 to get maximum

### Example 2
**Input:** `num = 9973`
**Output:** `9973`
**Explanation:** Already maximum, no swap needed

### Example 3
**Input:** `num = 98368`
**Output:** `98863`
**Explanation:** Swap 3 and 8 to maximize

### Example 4
**Input:** `num = 1993`
**Output:** `9913`
**Explanation:** Swap first 1 with last 9

---

## Optimal Solution

### Implementation

```python
def maximumSwap(num: int) -> int:
    """
    Find rightmost occurrence of each digit, greedy swap.

    Time: O(n), Space: O(1) - max 10 digits
    """
    digits = list(str(num))
    n = len(digits)

    # Record last occurrence of each digit
    last = {int(d): i for i, d in enumerate(digits)}

    # Try to find first digit that can be swapped with larger one
    for i in range(n):
        # Look for larger digit (9 down to current+1)
        for d in range(9, int(digits[i]), -1):
            if last.get(d, -1) > i:
                # Swap with rightmost occurrence of larger digit
                digits[i], digits[last[d]] = digits[last[d]], digits[i]
                return int(''.join(digits))

    return num
```

### Complexity Analysis

**Time: O(n) - single pass with constant digit checks. Space: O(1) - max 10 digits**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Math, Greedy

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/maximum-swap)*
