# Array Hashing - Comprehensive Guide

## Hash Tables for O(1) Lookup & Prefix Sums for Range Queries

---

## 🎯 Overview

**Total Problems:** 12
**Difficulty:** Easy (2) • Medium (10) • Hard (0)

**Core Concept:**
Use hash maps for constant-time lookups and prefix sums for efficient range calculations

**Key Insight:**
Trade space for time: hash maps give O(1) access but use O(n) space. Prefix sums enable O(1) range queries after O(n) preprocessing.

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: Hash Map for Complement/Pair Finding
**Examples:** Two Sum, Group Anagrams
```python
seen = {}
for i, num in enumerate(arr):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### Pattern 2: Prefix Sum for Range Queries
**Examples:** Subarray Sum Equals K, Range Sum Query
```python
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)
# Sum of arr[i:j] = prefix[j] - prefix[i]
```

### Pattern 3: Counting with Hash Map
**Examples:** Top K Frequent Elements, Custom Sort
```python
from collections import Counter
count = Counter(arr)
```


---

## 🎓 Learning Path

Two Sum → Subarray Sum K → Top K Frequent → Group Anagrams

---

## ⚠️ Common Pitfalls

1. Not handling duplicates 2. Off-by-one in prefix sum 3. Modifying array while iterating

---

## ✅ Testing Strategy

Test: empty, single element, all same, all unique, with negatives

---

## 💡 Templates & Code Patterns

See patterns above

---

## 💎 Mastery Tips

Know when to use hash map vs prefix sum. Hash for lookups, prefix for ranges.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 016 | [Merge Intervals](./016_merge_intervals.md) | MEDIUM | 77.9% |
| 017 | [Two Sum](./017_two_sum.md) | EASY | 76.4% |
| 022 | [Buildings With an Ocean View](./022_buildings_with_an_ocean_view.md) | MEDIUM | 74.9% |
| 023 | [Custom Sort String](./023_custom_sort_string.md) | MEDIUM | 73.2% |
| 024 | [K Closest Points to Origin](./024_k_closest_points_to_origin.md) | MEDIUM | 71.4% |
| 026 | [Subarray Sum Equals K](./026_subarray_sum_equals_k.md) | MEDIUM | 71.4% |
| 062 | [Group Shifted Strings](./062_group_shifted_strings.md) | MEDIUM | 47.0% |
| 069 | [Zero Array Transformation III](./069_zero_array_transformation_iii.md) | MEDIUM | 40.7% |
| 071 | [Managers with at Least 5 Direct Reports](./071_managers_with_at_least_5_direct_reports.md) | MEDIUM | 40.7% |
| 077 | [Car Pooling](./077_car_pooling.md) | MEDIUM | 40.7% |
| 087 | [Maximum Subarray](./087_maximum_subarray.md) | MEDIUM | 32.0% |
| 089 | [Range Sum Query - Immutable](./089_range_sum_query_immutable.md) | EASY | 32.0% |

---

[← Back to Main](../README.md)
