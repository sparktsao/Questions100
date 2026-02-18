# Heap/Priority Queue Problems - Comprehensive Analysis

## 🎯 Category Overview

**Total Problems:** 7
**Difficulty Range:** Medium → Hard
**Core Concept:** Using heaps for efficient min/max operations, k-th elements, and median tracking

**🔑 Key Insight:** Choose heap type based on what you track:
- **Min Heap** → Track K largest elements (top is smallest of the large)
- **Max Heap** → Track K smallest elements (top is largest of the small)
- **Dual Heap** → Track median dynamically

---

## 📊 Problem Progression Map

```
Level 1: Kth Largest Element (#006) - Min Heap Size K (EASIEST)
    ↓
Level 2: Top K Frequent Elements (#015) - Heap + Hash Map
    ↓
Level 3: Merge K Sorted Lists (#019) - Min Heap Merging
    ↓
Level 4: Find Median from Data Stream (#082) - Dual Heap (HARD)
    ↓
Level 5: Sliding Window Median (#034) - Dual Heap + Lazy Deletion (HARDEST)
```

---

## 🔍 The Three Patterns

### Pattern A: Min Heap for Top K Largest
**When:** Find k-th largest or top K largest
**Key:** Heap size = k, top = k-th largest
**Examples:** #006, #015

### Pattern B: Dual Heap for Median
**When:** Dynamic median queries
**Key:** Max heap (lower half) + Min heap (upper half)
**Examples:** #082, #034

### Pattern C: Heap for Merging
**When:** Merge multiple sorted streams
**Key:** Track smallest current from each stream
**Examples:** #019

---

## 📖 Problem-by-Problem Analysis

### 1️⃣ **Problem #006: Kth Largest Element** (MEDIUM)

**🎯 Task:** Find kth largest element
**📥 Input:** Array + k
**📤 Output:** kth largest value
**🏷️ Tag:** Min Heap

#### The Counter-Intuitive Insight!
```
Use MIN HEAP (not max heap!) of size k
Why? Top of min heap = smallest of k largest = kth largest!
```

#### Algorithm
```python
def findKthLargest(nums, k):
    import heapq
    # Min heap of k largest elements
    heap = nums[:k]
    heapq.heapify(heap)  # O(k)

    # For remaining elements
    for num in nums[k:]:
        if num > heap[0]:  # Larger than kth largest?
            heapq.heapreplace(heap, num)  # O(log k)

    return heap[0]  # kth largest
```

#### Why Min Heap Not Max Heap?
```
Max heap tracks k smallest → gives k-th smallest
Min heap tracks k largest → gives k-th largest ✓

Example: [3,2,1,5,6,4], k=2
Min heap of 2 largest: [5,6]
Top of min heap: 5 = 2nd largest ✓
```

#### Key Insight
> **Min Heap for Top K Largest:** Heap size = k, smallest in heap = answer

#### Complexity
- **Time:** O(n log k) - better than O(n log n) sort when k << n
- **Space:** O(k) - only store k elements

---

### 2️⃣ **Problem #015: Top K Frequent Elements** (MEDIUM)

**🎯 Task:** Find k most frequent elements
**📥 Input:** Array + k
**📤 Output:** K most frequent elements
**🏷️ Tag:** Heap + Hash Map

#### Algorithm
```python
def topKFrequent(nums, k):
    from collections import Counter
    import heapq

    # Count frequencies
    counts = Counter(nums)

    # Min heap of k most frequent
    # Heap stores (frequency, element)
    return heapq.nlargest(k, counts.keys(), key=counts.get)

    # Or manually with min heap:
    heap = []
    for num, freq in counts.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]
```

#### Key Insight
> **Two-Phase:** Count frequencies → Heap for top K

#### Complexity
- **Time:** O(n + m log k) where m = unique elements
- **Space:** O(m) for counter

---

### 3️⃣ **Problem #019: Merge K Sorted Lists** (HARD)

**🎯 Task:** Merge k sorted linked lists
**📥 Input:** Array of k list heads
**📤 Output:** Merged sorted list
**🏷️ Tag:** Min Heap, Merging

#### Algorithm
```python
def mergeKLists(lists):
    import heapq

    # Min heap: (node.val, index, node)
    heap = []

    # Initialize with first node from each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    dummy = ListNode(0)
    current = dummy

    while heap:
        val, i, node = heapq.heappop(heap)

        # Add to result
        current.next = node
        current = current.next

        # Add next node from same list
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))

    return dummy.next
```

#### Why Heap?
```
Compare only K elements at a time (not all N)
Always pick smallest current → sorted result
```

#### Key Insight
> **Heap for Merging:** Track smallest from each stream simultaneously

#### Complexity
- **Time:** O(N log k) where N = total nodes, k = number of lists
- **Space:** O(k) - heap size

---

### 4️⃣ **Problem #082: Find Median from Data Stream** (HARD)

**🎯 Task:** Dynamic median with add() and findMedian()
**📥 Input:** Stream of numbers
**📤 Output:** Current median
**🏷️ Tag:** Dual Heap

#### The Dual Heap Pattern!
```
Max Heap (lower half)  |  Min Heap (upper half)
      [1,2,3]          |        [5,6,7]
        ↑              |          ↑
    largest of small   |    smallest of large
                   median = between these!
```

#### Algorithm
```python
class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (negate values)
        self.large = []  # min heap

    def addNum(self, num):
        import heapq

        # Always add to small first
        heapq.heappush(self.small, -num)

        # Balance: largest of small should ≤ smallest of large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Maintain size: small can have at most 1 extra
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

#### The Two Invariants
```
1. Size: len(small) = len(large) OR len(small) = len(large) + 1
2. Value: max(small) ≤ min(large)

Median:
- Odd total: top of larger heap
- Even total: average of both tops
```

#### Key Insight
> **Dual Heap:** Split data in half, track both halves' boundaries

#### Complexity
- **Time:** O(log n) add, O(1) find median
- **Space:** O(n) - store all elements

---

### 5️⃣ **Problem #034: Sliding Window Median** (HARD)

**🎯 Task:** Median in sliding window
**📥 Input:** Array + window size k
**📤 Output:** Median for each window
**🏷️ Tag:** Dual Heap + Lazy Deletion

#### What Makes This HARDEST?
```
#082: Only add elements
#034: Must add AND remove elements!

Problem: Heap doesn't support arbitrary deletion
Solution: Lazy deletion (track removed, skip when popped)
```

#### Algorithm (Simplified)
```python
def medianSlidingWindow(nums, k):
    from collections import Counter
    import heapq

    small = []  # max heap
    large = []  # min heap
    removed = Counter()  # lazy deletion tracker

    def add(num):
        if not small or num <= -small[0]:
            heapq.heappush(small, -num)
        else:
            heapq.heappush(large, num)

    def remove(num):
        removed[num] += 1
        # Actual removal happens lazily during rebalance

    def rebalance():
        # Remove invalid tops
        while small and removed[-small[0]]:
            removed[-small[0]] -= 1
            heapq.heappop(small)
        while large and removed[large[0]]:
            removed[large[0]] -= 1
            heapq.heappop(large)

        # Balance sizes
        while len(small) > len(large) + 1:
            heapq.heappush(large, -heapq.heappop(small))
        while len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))

    # Initialize first window
    for i in range(k):
        add(nums[i])
    rebalance()

    result = []
    for i in range(k, len(nums) + 1):
        # Get median
        if k % 2:
            result.append(-small[0])
        else:
            result.append((-small[0] + large[0]) / 2)

        if i < len(nums):
            # Slide window
            remove(nums[i - k])
            add(nums[i])
            rebalance()

    return result
```

#### Key Insight
> **Lazy Deletion:** Track removed elements, skip when encountered at top

#### Complexity
- **Time:** O(n log k) - k elements in heaps
- **Space:** O(k) - heap + removal tracker

---

## 💡 Key Learning Insights

### 1. **Min vs Max Heap Decision**
```python
# For k-th LARGEST: use MIN heap
heap = []  # size k
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)  # Remove smallest
# heap[0] = k-th largest

# For k-th SMALLEST: use MAX heap (negate)
heap = []  # size k
for num in nums:
    heapq.heappush(heap, -num)  # Negate for max heap
    if len(heap) > k:
        heapq.heappop(heap)
# -heap[0] = k-th smallest
```

### 2. **Dual Heap Template**
```python
class DualHeap:
    def __init__(self):
        self.small = []  # max heap (lower half)
        self.large = []  # min heap (upper half)

    def add(self, num):
        # Add to appropriate heap
        if not self.small or num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        else:
            heapq.heappush(self.large, num)

        # Rebalance
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def get_median(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2
```

### 3. **Python Heap Tricks**
```python
import heapq

# Min heap (default)
heap = []
heapq.heappush(heap, 5)

# Max heap (negate values)
max_heap = []
heapq.heappush(max_heap, -5)
max_val = -heapq.heappop(max_heap)

# heapq.nlargest / heapq.nsmallest
top_k = heapq.nlargest(k, nums)  # O(n log k)

# heapreplace (pop + push atomically)
heapq.heapreplace(heap, new_val)  # Faster than pop + push
```

---

## 🎨 Visual Comparison Table

| Problem | Heap Type | Key Technique | Complexity |
|---------|-----------|---------------|------------|
| #006 | Min (size k) | Track k largest | O(n log k) |
| #015 | Min (size k) | Count + heap | O(n + m log k) |
| #019 | Min (size k) | Merge k streams | O(N log k) |
| #082 | Dual (max+min) | Dynamic median | O(log n) add |
| #034 | Dual + lazy | Window median | O(n log k) |

---

## 🚀 Recommended Study Order

1. **Min Heap Basics:** #006 (Kth Largest)
2. **Heap + Hash:** #015 (Top K Frequent)
3. **Merging:** #019 (Merge K Lists)
4. **Dual Heap:** #082 (Median Stream)
5. **Advanced:** #034 (Sliding Median)

---

## 📝 Interview Tips

### Common Mistakes
1. **#006:** Using max heap instead of min heap
2. **#082:** Forgetting to maintain size balance
3. **#034:** Trying to directly delete from heap (can't!)

### Pattern Recognition
```
"k-th largest" → Min heap size k
"k-th smallest" → Max heap size k
"median" → Dual heap
"merge k sorted" → Min heap
"streaming" → Heap maintains invariant
```

---

**Summary:** Heap problems use min heaps for top K largest (counter-intuitive!), dual heaps (max + min) for dynamic median, and heaps for efficient merging. Master the pattern: min heap tracks k largest elements, with top = k-th largest. For median, split data into two halves with max heap (lower) and min heap (upper). Key insight: heaps maintain partial order efficiently in O(log n), perfect for "k-th" queries and streaming data where we don't need full sort.
