# Design - Comprehensive Guide

## Data Structure Design & API Implementation

---

## 🎯 Overview

**Total Problems:** 2
**Difficulty:** Easy (1) • Medium (1) • Hard (0)

**Core Concept:**
Design custom data structures with optimal time/space complexity

**Key Insight:**
Balance time complexity of operations with space requirements

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: Cache Design (LRU, LFU)
### Pattern 2: Stream Processing (Moving Average, Median)
### Pattern 3: Iterator Design (BST Iterator, Flatten)
### Pattern 4: Specialized Data Structures


---

## 🎓 Learning Path

Moving Average → LRU Cache → BST Iterator → Design Twitter

---

## ⚠️ Common Pitfalls

1. Not considering all operations 2. Wrong complexity 3. Not thread-safe 4. Memory leaks

---

## ✅ Testing Strategy

Test: edge operations, capacity limits, empty, sequential operations

---

## 💡 Templates & Code Patterns


```python
# LRU Cache pattern
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```


---

## 💎 Mastery Tips

Define all operations first. Analyze complexity. Consider tradeoffs.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 039 | [LRU Cache](./039_lru_cache.md) | MEDIUM | 62.4% |
| 048 | [Moving Average from Data Stream](./048_moving_average_from_data_stream.md) | EASY | 56.0% |

---

[← Back to Main](../README.md)
