# 039. LRU Cache

**Difficulty:** MEDIUM
**Frequency:** 62.4%
**Acceptance Rate:** 45.2%
**LeetCode Link:** [LRU Cache](https://leetcode.com/problems/lru-cache)

---

## Problem Description

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
- `LRUCache(int capacity)` Initialize with positive size capacity
- `int get(int key)` Return value of key if exists, otherwise -1
- `void put(int key, int value)` Update or insert the key-value pair. If keys exceed capacity, evict the LRU key.

Both get and put must run in O(1) average time complexity.

**Constraints:**
- 1 <= capacity <= 3000
- 0 <= key <= 10^4
- 0 <= value <= 10^5
- At most 2 * 10^5 calls to get and put

---

## Examples

### Example 1
**Input:** `["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]\n[[2], [1,1], [2,2], [1], [3,3], [2], [4,4], [1], [3], [4]]`
**Output:** `[null, null, null, 1, null, -1, null, -1, 3, 4]`
**Explanation:** Cache capacity 2: operations show LRU eviction

### Example 2
**Input:** `put(1,1), put(2,2), get(1), put(3,3), get(2)`
**Output:** `[1, -1]`
**Explanation:** Key 2 evicted when adding 3

### Example 3
**Input:** `put(2,1), put(1,1), put(2,3), get(1), get(2)`
**Output:** `[1, 3]`
**Explanation:** Updates don't change capacity usage

---

## Optimal Solution

### Implementation

```python
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node
        # Doubly linked list for LRU ordering
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, value)
        self._add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            lru = self.head.next
            self._remove(lru)
            del self.cache[lru.key]

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add(self, node):
        # Add to tail (most recently used)
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
```

### Complexity Analysis

**Time: O(1) for get/put. Space: O(capacity)**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, Linked List, Design, Doubly-Linked List

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/lru-cache)*
