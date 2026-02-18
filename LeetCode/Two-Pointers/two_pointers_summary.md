# Two Pointers - Comprehensive Guide

## Opposite Direction vs Same Direction Techniques

---

## 🎯 Overview

**Total Problems:** 9
**Difficulty:** Easy (4) • Medium (5) • Hard (0)

**Core Concept:**
Use two pointers to traverse array/list in O(n) time instead of O(n²) nested loops

**Key Insight:**
Two pointers can move in OPPOSITE directions (start/end) or SAME direction (fast/slow). Choose based on problem requirements.

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: Opposite Direction (Converging)
**Use when:** Need to find pairs, check palindrome, or compare elements from both ends
**Template:**
```python
def two_pointer_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process arr[left] and arr[right]
        if condition:
            left += 1
        else:
            right -= 1
```
**Examples:** Two Sum in sorted array, Valid Palindrome, Container With Most Water

### Pattern 2: Same Direction (Fast-Slow)
**Use when:** Finding cycles, removing duplicates, or partitioning
**Template:**
```python
def two_pointer_same(arr):
    slow = 0
    for fast in range(len(arr)):
        if condition:
            arr[slow] = arr[fast]
            slow += 1
    return slow
```
**Examples:** Remove Duplicates, Move Zeros, Partition Array

### Pattern 3: Sliding Window (Special Case)
**Use when:** Finding subarrays with specific properties
**Template:**
```python
def sliding_window(arr):
    left = 0
    for right in range(len(arr)):
        # Expand window
        # ...
        while invalid_condition:
            # Shrink window
            left += 1
```
**Examples:** Longest Substring, Minimum Window


---

## 🎓 Learning Path


1. **Start:** Valid Palindrome - simple opposite direction
2. **Next:** Remove Duplicates - same direction with slow/fast
3. **Then:** Container With Most Water - optimize with greedy pointer movement
4. **Advanced:** 3Sum - nested pointers
5. **Master:** Trapping Rain Water - complex pointer logic


---

## ⚠️ Common Pitfalls


1. ❌ Moving both pointers simultaneously when should move one
2. ❌ Off-by-one errors with `left < right` vs `left <= right`
3. ❌ Not handling edge cases: empty array, single element
4. ❌ Using nested loops instead of two pointers (missing O(n) optimization)


---

## ✅ Testing Strategy


**Test Cases:**
- Empty: []
- Single: [1]
- Two elements: [1, 2]
- All same: [5, 5, 5]
- Already sorted/valid
- Reverse sorted
- With duplicates


---

## 💡 Templates & Code Patterns


```python
# Template 1: Opposite Direction
left, right = 0, len(arr) - 1
while left < right:
    if arr[left] + arr[right] == target:
        return [left, right]
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        right -= 1

# Template 2: Same Direction
slow = 0
for fast in range(len(arr)):
    if arr[fast] != val:
        arr[slow] = arr[fast]
        slow += 1
return slow
```


---

## 💎 Mastery Tips


1. **Recognize the pattern:** If problem mentions pairs, subarrays, or can be solved in O(n), consider two pointers
2. **Choose direction:** Opposite for pairs/symmetry, same for partitioning/duplicates
3. **Pointer movement rules:** Define clear conditions for when to move which pointer
4. **Invariant:** Always maintain what [left, right] represents


---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 002 | [Valid Word Abbreviation](./002_valid_word_abbreviation.md) | EASY | 95.4% |
| 028 | [Dot Product of Two Sparse Vectors](./028_dot_product_of_two_sparse_vectors.md) | MEDIUM | 69.5% |
| 030 | [Next Permutation](./030_next_permutation.md) | MEDIUM | 67.4% |
| 033 | [Merge Sorted Array](./033_merge_sorted_array.md) | EASY | 67.4% |
| 044 | [Squares of a Sorted Array](./044_squares_of_a_sorted_array.md) | EASY | 59.4% |
| 065 | [3Sum](./065_3sum.md) | MEDIUM | 47.0% |
| 073 | [Container With Most Water](./073_container_with_most_water.md) | MEDIUM | 40.7% |
| 078 | [Strobogrammatic Number](./078_strobogrammatic_number.md) | EASY | 40.7% |
| 088 | [Interval List Intersections](./088_interval_list_intersections.md) | MEDIUM | 32.0% |

---

[← Back to Main](../README.md)
