# Heap Priority Queue - Comprehensive Guide

## Top-K Problems & Running Median

---

## 🎯 Overview

**Total Problems:** 7
**Difficulty:** Easy (0) • Medium (4) • Hard (3)

**Core Concept:**
Heap maintains min/max in O(log n), perfect for top-k and streaming data

**Key Insight:**
Min heap for top K largest (invert), max heap for top K smallest

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: Top K Elements (K Closest, K Frequent)
### Pattern 2: Merge K Sorted Lists
### Pattern 3: Running Median with Two Heaps
### Pattern 4: K-way Merge


---

## 🎓 Learning Path

Kth Largest → K Closest Points → Merge K Lists → Find Median

---

## ⚠️ Common Pitfalls

1. Wrong heap type 2. Not using negative for max heap 3. Not maintaining heap size 4. Forgetting heappush/heappop

---

## ✅ Testing Strategy

Test: empty, k=1, k=n, duplicates, single element

---

## 💡 Templates & Code Patterns


```python
import heapq

# Min heap (default)
heap = []
heapq.heappush(heap, val)
min_val = heapq.heappop(heap)

# Max heap (use negative)
max_heap = []
heapq.heappush(max_heap, -val)
max_val = -heapq.heappop(max_heap)

# Top K pattern
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
return heap[0]  # kth largest
```


---

## 💎 Mastery Tips

Python only has min heap. Use negative for max heap. Maintain size k for top-k.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 006 | [Kth Largest Element in an Array](./006_kth_largest_element_in_an_array.md) | MEDIUM | 86.9% |
| 012 | [Random Pick with Weight](./012_random_pick_with_weight.md) | MEDIUM | 80.5% |
| 015 | [Top K Frequent Elements](./015_top_k_frequent_elements.md) | MEDIUM | 77.9% |
| 019 | [Merge k Sorted Lists](./019_merge_k_sorted_lists.md) | HARD | 76.4% |
| 034 | [Sliding Window Median](./034_sliding_window_median.md) | HARD | 65.0% |
| 082 | [Find Median from Data Stream](./082_find_median_from_data_stream.md) | HARD | 40.7% |
| 091 | [Random Pick Index](./091_random_pick_index.md) | MEDIUM | 32.0% |

---

[← Back to Main](../README.md)
