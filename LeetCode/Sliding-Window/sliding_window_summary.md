# Sliding Window - Comprehensive Guide

## Fixed Size vs Variable Size Windows

---

## 🎯 Overview

**Total Problems:** 6
**Difficulty:** Easy (1) • Medium (4) • Hard (1)

**Core Concept:**
Maintain a window of elements and slide it across array/string to find optimal subarray

**Key Insight:**
Window can be FIXED size (simpler) or VARIABLE size (more common). Variable uses while loop to shrink window.

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: Fixed Size Window
**Use when:** Problem specifies exact window size k
**Template:**
```python
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Pattern 2: Variable Size Window (Most Common!)
**Use when:** Find "longest/shortest substring/subarray that satisfies..."
**Template:**
```python
def variable_window(arr):
    left = 0
    result = 0
    window = {}  # Track window state

    for right in range(len(arr)):
        # Expand: add arr[right] to window
        window[arr[right]] = window.get(arr[right], 0) + 1

        # Shrink: while window invalid
        while window_invalid():
            window[arr[left]] -= 1
            left += 1

        # Update result with valid window
        result = max(result, right - left + 1)

    return result
```


---

## 🎓 Learning Path


1. Maximum Sum Subarray of Size K (fixed window)
2. Longest Substring Without Repeating Characters (variable)
3. Minimum Window Substring (variable with complex validation)
4. Longest Substring with At Most K Distinct Characters


---

## ⚠️ Common Pitfalls


1. ❌ Not properly maintaining window state when shrinking
2. ❌ Updating result outside valid window
3. ❌ Forgetting to handle empty input
4. ❌ Using nested loops (O(n²)) instead of sliding window (O(n))


---

## ✅ Testing Strategy

Test with: empty string, single char, all same, all unique, exactly k size, smaller than k

---

## 💡 Templates & Code Patterns

See sub-patterns above for complete templates

---

## 💎 Mastery Tips


1. Always expand right pointer in loop
2. Shrink left pointer in while loop when window becomes invalid
3. Use hash map to track window contents
4. Update result only when window is valid


---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 037 | [Minimum Window Substring](./037_minimum_window_substring.md) | HARD | 62.4% |
| 040 | [Max Consecutive Ones III](./040_max_consecutive_ones_iii.md) | MEDIUM | 62.4% |
| 059 | [Continuous Subarray Sum](./059_continuous_subarray_sum.md) | MEDIUM | 47.0% |
| 068 | [Contains Duplicate II](./068_contains_duplicate_ii.md) | EASY | 40.7% |
| 080 | [Longest Substring Without Repeating Characters](./080_longest_substring_without_repeating_characters.md) | MEDIUM | 40.7% |
| 090 | [Frequency of the Most Frequent Element](./090_frequency_of_the_most_frequent_element.md) | MEDIUM | 32.0% |

---

[← Back to Main](../README.md)
