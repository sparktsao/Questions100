# Heap & Priority Queue - Comprehensive Mastery Guide




## 📋 Problems in This Category

- [006. Kth Largest Element](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Heap-Priority-Queue/006_kth_largest_element_in_an_array.md) - `Min Heap`
- [012. Random Pick with Weight](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Heap-Priority-Queue/012_random_pick_with_weight.md) - `Binary Search+Prefix`
- [015. Top K Frequent Elements](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Heap-Priority-Queue/015_top_k_frequent_elements.md) - `Bucket Sort`
- [019. Merge k Sorted Lists](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Heap-Priority-Queue/019_merge_k_sorted_lists.md) - `Min Heap`
- [034. Sliding Window Median](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Heap-Priority-Queue/034_sliding_window_median.md) - `Dual Heap+Lazy`
- [082. Find Median from Data Stream](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Heap-Priority-Queue/082_find_median_from_data_stream.md) - `Dual Heap`
- [091. Random Pick Index](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Heap-Priority-Queue/091_random_pick_index.md) - `Reservoir Sampling`

---

## 🎯 Category Overview

**Total Problems:** 7
**Difficulty Distribution:** Medium (4) • Hard (3)
**Core Data Structure:** Binary Heap (Min/Max)

**What Makes This Category Special:**

Heap problems teach you to **maintain order dynamically** - finding top-K elements, merging sorted streams, or tracking medians as data arrives. Unlike sorting (O(n log n) for all n elements), heaps let you maintain partial order in O(log k) time, where k << n.

The beauty of heaps lies in their **selective ordering**: you don't need to sort everything, just keep track of what matters (the K largest, the median, the next minimum from K sources).

---

## 📊 Problem Progression Map

```
Foundation (Top-K Basics)
├─ #006 Kth Largest Element ⭐ START HERE
│  └─ Pattern: Min heap of size K for top-K largest
│
├─ #015 Top K Frequent Elements
│  └─ Adds: Counting + Heap (or clever bucket sort)
│
Advanced (K-Way Merge)
├─ #019 Merge K Sorted Lists ⭐ KEY PROBLEM
│  └─ Pattern: Heap tracks minimum from K sources
│
Two-Heap Technique (Median Finding)
├─ #082 Find Median from Data Stream ⭐ FOUNDATION
│  └─ Pattern: Max heap (lower half) + Min heap (upper half)
│
├─ #034 Sliding Window Median
│  └─ Adds: Window sliding + Lazy deletion
│
Randomization (Not Pure Heap)
├─ #012 Random Pick with Weight
│  └─ Prefix sum + Binary search
│
└─ #091 Random Pick Index
   └─ Reservoir sampling

Difficulty: ⭐ = Must Master | 🔥 = Interview Favorite
```

---

## 🔥 Critical Insight: Python's Min Heap Limitation & Negation Strategy

### The Python Heap Problem

**Python's `heapq` only supports MIN heap** - there's no built-in max heap. This creates confusion for problems that conceptually need max heaps.

**The Solution:** Negate values to simulate max heap behavior.

```python
# Min heap (natural)
import heapq
min_heap = []
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)
print(min_heap[0])  # 3 ← smallest value at root

# Max heap (via negation)
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
print(-max_heap[0])  # 8 ← largest value (negated)
```

---

## 🎯 Decision Framework: When to Negate?

### The Golden Rule

**Ask yourself: "What do I want at the root of the heap?"**

| Want at Root | Heap Type | Python Implementation |
|--------------|-----------|----------------------|
| **Smallest** value | Min heap | Use heapq **directly** (no negation) |
| **Largest** value | Max heap | **Negate** values: `-num` |

### Problem Pattern Analysis

| Problem Type | What You Want | Heap Type | Negate? | Why |
|--------------|---------------|-----------|---------|-----|
| **K Largest** elements | Kth largest (boundary) | Min heap | ❌ NO | Root = smallest of top K = Kth largest |
| **K Smallest** elements | Kth smallest (boundary) | Max heap | ✅ YES | Root = largest of bottom K = Kth smallest |
| **Find Maximum** repeatedly | Maximum value | Max heap | ✅ YES | Root = largest overall |
| **Find Minimum** repeatedly | Minimum value | Min heap | ❌ NO | Root = smallest overall |
| **Median** (lower half) | Max of lower half | Max heap | ✅ YES | Root = boundary between halves |
| **Median** (upper half) | Min of upper half | Min heap | ❌ NO | Root = boundary between halves |
| **Merge K sorted** (ascending) | Minimum across K sources | Min heap | ❌ NO | Root = next smallest to add |

---

## 📊 Side-by-Side: When to Negate

### Case 1: Kth Largest Element (NO Negation)

**Problem:** Find Kth largest from [3,2,1,5,6,4], k=2

**Intuition:** Want **2nd largest** → Need **boundary** between top 2 and rest

**Solution:** Min heap of size k

```python
def findKthLargest(nums, k):
    import heapq
    heap = []

    for num in nums:
        heapq.heappush(heap, num)  # ← NO negation!
        if len(heap) > k:
            heapq.heappop(heap)  # Remove smallest

    return heap[0]  # Min of top k = kth largest

# Trace: nums = [3,2,1,5,6,4], k=2
# After 3: heap = [3]
# After 2: heap = [2,3]         ← size = k, stop growing
# After 1: heap = [2,3] → [2,3] ← 1 < heap[0], not added
# Actually: heap = [1,2,3] → pop 1 → [2,3]
# After 5: heap = [2,3,5] → pop 2 → [3,5]
# After 6: heap = [3,5,6] → pop 3 → [5,6]
# After 4: heap = [4,5,6] → pop 4 → [5,6]
# Result: heap[0] = 5 ✓
```

**Why no negation?**
- Want min heap root = Kth largest
- Min heap naturally keeps smallest at root
- Root = "weakest survivor" of top K

---

### Case 2: Kth Smallest Element (YES Negation)

**Problem:** Find Kth smallest from [3,2,1,5,6,4], k=2

**Intuition:** Want **2nd smallest** → Need **boundary** between bottom 2 and rest

**Solution:** Max heap of size k (negate!)

```python
def findKthSmallest(nums, k):
    import heapq
    heap = []

    for num in nums:
        heapq.heappush(heap, -num)  # ← Negate for max heap!
        if len(heap) > k:
            heapq.heappop(heap)  # Remove largest (most negative)

    return -heap[0]  # ← Negate back!

# Trace: nums = [3,2,1,5,6,4], k=2
# After 3: heap = [-3]
# After 2: heap = [-3,-2]       ← size = k
# After 1: heap = [-3,-2,-1] → pop -3 → [-2,-1]
# After 5: heap = [-2,-1] (5 > -(-2), don't add)
# After 6: heap = [-2,-1] (6 > -(-2), don't add)
# After 4: heap = [-2,-1] (4 > -(-2), don't add)
# Result: -heap[0] = -(-2) = 2 ✓
```

**Why negate?**
- Want max heap root = Kth smallest
- Python only has min heap
- Negating values inverts order: `min(-a, -b) = -max(a, b)`

---

### Case 3: Two Heaps for Median (BOTH!)

**Problem:** Find median of streaming data

**Intuition:**
- Lower half: Want max (largest of lower half)
- Upper half: Want min (smallest of upper half)

**Solution:** Max heap (negate) + Min heap (no negate)

```python
class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (NEGATE) - lower half
        self.large = []  # Min heap (NO NEGATE) - upper half

    def addNum(self, num):
        # Add to max heap (small) - NEGATE!
        heapq.heappush(self.small, -num)

        # Balance: ensure all small ≤ all large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)  # NEGATE back
            heapq.heappush(self.large, val)

        # Balance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)  # NEGATE back
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)  # NEGATE

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]  # NEGATE back
        return (-self.small[0] + self.large[0]) / 2.0  # NEGATE small

# Why this works:
# small (max heap): [-3, -1]  → actual values: [3, 1] → max = 3
# large (min heap): [5, 7]    → actual values: [5, 7] → min = 5
# All in small (1,3) ≤ All in large (5,7) ✓
# Median boundary: between 3 and 5
```

**Why both?**
- `small` needs max heap (negate) → track largest of lower half
- `large` needs min heap (direct) → track smallest of upper half
- Roots are the two median candidates!

---

## 🔍 How to Identify if Negation is Needed

### Step-by-Step Decision Process

```
1. Read problem requirements
   ↓
2. Identify what operation you need repeatedly
   │
   ├─ "Find/remove LARGEST repeatedly"
   │  → Need MAX heap → NEGATE
   │
   ├─ "Find/remove SMALLEST repeatedly"
   │  → Need MIN heap → NO NEGATION
   │
   ├─ "Find Kth LARGEST"
   │  → Counter-intuitive: MIN heap of size K → NO NEGATION
   │  → Because min heap root = Kth largest (boundary)
   │
   ├─ "Find Kth SMALLEST"
   │  → Counter-intuitive: MAX heap of size K → NEGATE
   │  → Because max heap root = Kth smallest (boundary)
   │
   └─ "Find MEDIAN"
      → Need BOTH max (lower) and min (upper)
      → NEGATE for lower, NO NEGATE for upper
```

### Quick Reference Table

| Problem Keyword | Heap Configuration | Negation Needed? |
|-----------------|-------------------|------------------|
| "K largest" | Min heap size K | ❌ No |
| "K smallest" | Max heap size K | ✅ Yes (negate) |
| "Top K frequent" | Min heap size K (on frequencies) | ❌ No |
| "Merge K sorted lists" (ascending) | Min heap | ❌ No |
| "Merge K sorted lists" (descending) | Max heap | ✅ Yes |
| "Find maximum repeatedly" | Max heap | ✅ Yes |
| "Find minimum repeatedly" | Min heap | ❌ No |
| "Median lower half" | Max heap | ✅ Yes |
| "Median upper half" | Min heap | ❌ No |

---

## ⚠️ Common Negation Mistakes

### Mistake 1: Negating for "K Largest"

**❌ WRONG:**
```python
# "Find K largest" - WRONG approach!
def findKLargest(nums, k):
    max_heap = []
    for num in nums:
        heapq.heappush(max_heap, -num)  # ❌ Creating max heap!
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    # Returns K smallest, not K largest!
    return [-x for x in max_heap]
```

**Why wrong?** Max heap of size K keeps **K smallest** elements, not K largest!

**✅ CORRECT:**
```python
def findKLargest(nums, k):
    min_heap = []
    for num in nums:
        heapq.heappush(min_heap, num)  # ✅ Min heap!
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return list(min_heap)  # K largest elements
```

---

### Mistake 2: Forgetting to Negate Back

**❌ WRONG:**
```python
# Max heap for largest element
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
largest = max_heap[0]  # ❌ Returns -8, not 8!
```

**✅ CORRECT:**
```python
# Max heap for largest element
max_heap = []
heapq.heappush(max_heap, -5)
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -8)
largest = -max_heap[0]  # ✅ Negate back! Returns 8
```

**Rule:** If you negate on push, you MUST negate on access/pop!

---

### Mistake 3: Inconsistent Negation in Two Heaps

**❌ WRONG:**
```python
class MedianFinder:
    def __init__(self):
        self.small = []  # Should be max heap
        self.large = []  # Should be min heap

    def addNum(self, num):
        heapq.heappush(self.small, num)  # ❌ Forgot to negate!
        # ... rest of logic

    def findMedian(self):
        return (self.small[0] + self.large[0]) / 2  # ❌ Wrong!
```

**✅ CORRECT:**
```python
class MedianFinder:
    def __init__(self):
        self.small = []  # Max heap (negate)
        self.large = []  # Min heap (no negate)

    def addNum(self, num):
        heapq.heappush(self.small, -num)  # ✅ Negate!
        # ... rest of logic

    def findMedian(self):
        return (-self.small[0] + self.large[0]) / 2  # ✅ Negate small!
```

---

### Mistake 4: Negating When Not Needed

**❌ WRONG:**
```python
# Merge K sorted lists (ascending order)
def mergeKLists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (-lst[0], i, 0))  # ❌ Why negate?
    # Want MINIMUM across K lists → Use min heap directly!
```

**✅ CORRECT:**
```python
def mergeKLists(lists):
    heap = []
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # ✅ No negation!
    # Min heap naturally gives smallest value
```

---

## 💡 Mental Model: The "Root Purpose" Test

**Before writing any heap code, ask:**

> "What do I need to ACCESS at the heap root?"

- **Need SMALLEST?** → Min heap → **No negation**
- **Need LARGEST?** → Max heap → **Negate**

**Then ask:**

> "Do I need all top K, or just the Kth?"

- **Just Kth largest** → Min heap of size K (root = Kth largest) → **No negation**
- **Just Kth smallest** → Max heap of size K (root = Kth smallest) → **Negate**

**Examples:**

```python
# Example 1: Keep removing largest element
# Root purpose: Access LARGEST → Max heap → NEGATE
max_heap = []
heapq.heappush(max_heap, -num)
largest = -heapq.heappop(max_heap)  # ✅

# Example 2: Keep removing smallest element
# Root purpose: Access SMALLEST → Min heap → NO NEGATE
min_heap = []
heapq.heappush(min_heap, num)
smallest = heapq.heappop(min_heap)  # ✅

# Example 3: Find 3rd largest
# Root purpose: Access boundary (3rd largest) → Min heap size 3 → NO NEGATE
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > 3:
        heapq.heappop(heap)
third_largest = heap[0]  # ✅

# Example 4: Find 3rd smallest
# Root purpose: Access boundary (3rd smallest) → Max heap size 3 → NEGATE
heap = []
for num in nums:
    heapq.heappush(heap, -num)
    if len(heap) > 3:
        heapq.heappop(heap)
third_smallest = -heap[0]  # ✅
```

---

## 📋 Problem-Specific Negation Map

| # | Problem | Heap Type | Negate? | Why |
|---|---------|-----------|---------|-----|
| 006 | Kth Largest Element | Min heap (size K) | ❌ No | Root = Kth largest (boundary) |
| 015 | Top K Frequent | Min heap (size K on freq) | ❌ No | Root = Kth most frequent (boundary) |
| 019 | Merge K Sorted Lists | Min heap (K sources) | ❌ No | Root = next minimum to merge |
| 082 | Find Median | Max (lower) + Min (upper) | ✅ Yes (lower only) | Lower half needs max heap |
| 034 | Sliding Window Median | Max (lower) + Min (upper) | ✅ Yes (lower only) | Same as #082 |

**Pattern observed:**
- **Single heap problems:** Usually **no negation** (min heap is enough)
- **Two heap problems:** Lower half **needs negation** (max heap)
- **Top-K problems:** Counter-intuitive! Use **opposite** heap type

---

## 🧪 Testing Your Understanding

### Quiz: Do You Need Negation?

For each problem, decide: Negate or not?

1. **Find the maximum element from a stream**
   - Need: Max at root
   - Answer: **Negate** (max heap)

2. **Find 5th largest element**
   - Need: Min heap size 5, root = 5th largest
   - Answer: **No negation** (min heap)

3. **Find 10th smallest element**
   - Need: Max heap size 10, root = 10th smallest
   - Answer: **Negate** (max heap)

4. **Merge K sorted arrays (ascending)**
   - Need: Min across K arrays at root
   - Answer: **No negation** (min heap)

5. **Track median (lower half)**
   - Need: Max of lower half at root
   - Answer: **Negate** (max heap)

---

## 🧬 Four Core Patterns

### Pattern 1: Top-K Elements (Maintain K Best)

**When to Use:** "Find the K largest/smallest/most frequent elements"

**Key Insight:** Use the **opposite** heap type!
- For K largest → Use **min heap** of size K
- For K smallest → Use **max heap** of size K

**Why?** The heap root is your "gatekeeper". For K largest, the min heap's root is the Kth largest - anything smaller gets rejected.

**Template:**
```python
import heapq

def kth_largest(nums, k):
    # Min heap for K largest
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)  # Remove smallest
    return heap[0]  # Kth largest
```

**Problems:** #006, #015

---

### Pattern 2: K-Way Merge (Combine K Sorted Sources)

**When to Use:** "Merge K sorted arrays/lists/streams"

**Key Insight:** Heap tracks the **current minimum** from each source. Always extract the global minimum, then advance that source.

**Complexity:** O(N log K) where N = total elements, K = number of sources
- Each of N elements: 1 heap pop + 1 heap push = O(log K)
- Much better than naive O(NK) or sorting all O(N log N)

**Template:**
```python
def merge_k_sorted(lists):
    heap = []
    # Initialize: add first element from each list
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(heap, (lst[0], i, 0))  # (value, list_idx, elem_idx)

    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)

        # Add next element from same list
        if elem_idx + 1 < len(lists[list_idx]):
            next_val = lists[list_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, list_idx, elem_idx + 1))

    return result
```

**Problems:** #019

---

### Pattern 3: Two Heaps for Median (Balanced Halves)

**When to Use:** "Find median in streaming data" or "Maintain median as elements arrive"

**Key Insight:** Split data into two halves:
- **Max heap** (small): Stores lower half - root is largest of lower half
- **Min heap** (large): Stores upper half - root is smallest of upper half

**Invariant:**
- `len(small) == len(large)` or `len(small) == len(large) + 1`
- All elements in small ≤ all elements in large

**Median:**
- Odd total: `median = -small[0]` (max heap root, negated)
- Even total: `median = (-small[0] + large[0]) / 2`

**Template:**
```python
class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (negate values)
        self.large = []  # min heap

    def addNum(self, num):
        # Always add to small first
        heapq.heappush(self.small, -num)

        # Balance: ensure all in small ≤ all in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Rebalance sizes
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return -self.small[0]
        return (-self.small[0] + self.large[0]) / 2.0
```

**Problems:** #082, #034

---

### Pattern 4: Randomization (Binary Search on Prefix Sum)

**When to Use:** "Randomly select with weighted probability"

**Key Insight:** Build prefix sum array, generate random number in [1, total], binary search for target.

**Not actually a heap problem**, but grouped here in LeetCode.

**Template:**
```python
class WeightedRandom:
    def __init__(self, weights):
        self.prefix = []
        total = 0
        for w in weights:
            total += w
            self.prefix.append(total)
        self.total = total

    def pick(self):
        target = random.randint(1, self.total)
        # Binary search for first prefix >= target
        left, right = 0, len(self.prefix) - 1
        while left < right:
            mid = (left + right) // 2
            if self.prefix[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
```

**Problems:** #012, #091

---

## 🔍 Problem Deep Dive

### #006 Kth Largest Element in an Array ⭐

**Difficulty:** Medium | **Frequency:** 86.9%

**Task:** Given array `nums` and integer `k`, return the kth largest element.

**Input:** `nums = [3,2,1,5,6,4], k = 2`
**Output:** `5`
**Explanation:** Sorted: [1,2,3,4,5,6] → 2nd largest is 5

**What Makes This Special:**

This is the **foundation problem** for Top-K pattern. It teaches you the counterintuitive insight: use a **min heap** for finding largest elements!

**Three Approaches:**

1. **Sorting:** O(n log n) time, O(1) or O(n) space
   ```python
   def findKthLargest(nums, k):
       return sorted(nums, reverse=True)[k-1]
   ```
   *Simple but wasteful - sorts all elements when we only need K*

2. **Quickselect:** O(n) average, O(n²) worst, O(1) space
   - Partition like quicksort, but recurse only on the side containing kth largest
   - Expected O(n): n + n/2 + n/4 + ... ≈ 2n
   - Best for **single query**, but interview often expects heap solution

3. **Min Heap of Size K:** O(n log k) time, O(k) space ⭐
   ```python
   def findKthLargest(nums, k):
       heap = []
       for num in nums:
           heapq.heappush(heap, num)
           if len(heap) > k:
               heapq.heappop(heap)
       return heap[0]
   ```

**Step-by-Step Example:**

```
nums = [3,2,1,5,6,4], k = 2

Process each element:
3: heap = [3]
2: heap = [2, 3]            (size = k = 2, stop growing)
1: heap = [2, 3] → pop 1    (1 < heap[0], don't add)
   Wait, that's wrong! Let me trace correctly:

3: heappush(3) → [3]
2: heappush(2) → [2, 3]     (size = k, stop growing)
1: heappush(1) → [1, 2, 3]  (size > k, pop smallest)
   heappop() → [2, 3]
5: heappush(5) → [2, 3, 5]  (size > k, pop smallest)
   heappop() → [3, 5]
6: heappush(6) → [3, 5, 6]  (size > k, pop smallest)
   heappop() → [5, 6]
4: heappush(4) → [4, 5, 6]  (size > k, pop smallest)
   heappop() → [5, 6]

Final heap = [5, 6]
heap[0] = 5 ← 2nd largest! ✓
```

**Visual Understanding:**

```
Min Heap (size = 2) keeps "top 2 largest"
Root = smallest of the top 2 = 2nd largest

After processing all:
      5          ← root = 2nd largest
     /
    6            ← 1st largest (child)

Heap property: parent ≤ children (for min heap)
```

**Common Bugs:**

❌ **Wrong:** `max_heap = []` then negate values (makes it max heap)
```python
heapq.heappush(max_heap, -num)  # Wrong for K largest!
```

✅ **Correct:** Use min heap directly
```python
heapq.heappush(heap, num)  # Min heap for K largest
```

**Why Min Heap for K Largest?**

Think of it as a **bouncer at an exclusive club** (capacity K):
- Min heap root = the weakest member currently in the club
- New candidate arrives:
  - If weaker than bouncer → rejected
  - If stronger → kicks out bouncer, enters club
- After everyone: bouncer = Kth strongest ✓

**Key Insights:**
1. **Opposite heap type** - counterintuitive but correct
2. **Maintain size K** - bounded space, bounded time per operation
3. **Alternative: Max heap** - Use max heap on all elements, pop K-1 times. O(n + k log n). Worse when k is small.

**Complexity:**
- **Time:** O(n log k) - n insertions, each O(log k)
- **Space:** O(k) - heap stores only K elements

---

### #015 Top K Frequent Elements

**Difficulty:** Medium | **Frequency:** 77.9%

**Task:** Given array `nums` and integer `k`, return the k most frequent elements.

**Input:** `nums = [1,1,1,2,2,3], k = 2`
**Output:** `[1, 2]`
**Explanation:** 1 appears 3×, 2 appears 2×, 3 appears 1× → top 2 are [1,2]

**What Makes This Special:**

Two-phase problem: **count frequencies**, then **find top K**. Teaches you to combine hash map + heap, or use clever **bucket sort** for O(n) solution!

**Two Approaches:**

1. **Min Heap (O(n log k)):**
   ```python
   def topKFrequent(nums, k):
       from collections import Counter
       count = Counter(nums)
       # heapq.nlargest is a min heap under the hood
       return heapq.nlargest(k, count.keys(), key=count.get)
   ```

2. **Bucket Sort (O(n)) ⭐ Optimal:**
   ```python
   def topKFrequent(nums, k):
       from collections import Counter
       count = Counter(nums)

       # Bucket[i] = elements with frequency i
       bucket = [[] for _ in range(len(nums) + 1)]
       for num, freq in count.items():
           bucket[freq].append(num)

       # Collect from highest frequency down
       result = []
       for i in range(len(bucket) - 1, 0, -1):
           for num in bucket[i]:
               result.append(num)
               if len(result) == k:
                   return result
       return result
   ```

**Why Bucket Sort Wins:**

- **Key observation:** Max possible frequency = n (all elements same)
- **Bucket index = frequency** → no comparisons needed!
- **Time:** O(n) to count, O(n) to build buckets, O(n) to collect → O(n) total
- **Better than O(n log k) heap** when k is not tiny

**Step-by-Step Example:**

```
nums = [1,1,1,2,2,3], k = 2

Step 1: Count frequencies
count = {1: 3, 2: 2, 3: 1}

Step 2: Build buckets (index = frequency)
bucket[0] = []
bucket[1] = [3]        ← elements with frequency 1
bucket[2] = [2]        ← elements with frequency 2
bucket[3] = [1]        ← elements with frequency 3
bucket[4] = []
bucket[5] = []
bucket[6] = []

Step 3: Collect from high frequency down
i=6: bucket[6] = [] → skip
i=5: bucket[5] = [] → skip
i=4: bucket[4] = [] → skip
i=3: bucket[3] = [1] → result = [1]
i=2: bucket[2] = [2] → result = [1, 2] → len = k, stop!

Output: [1, 2] ✓
```

**Common Bugs:**

❌ **Wrong:** Bucket size = max(frequencies) → might miss valid indices
```python
max_freq = max(count.values())
bucket = [[] for _ in range(max_freq + 1)]  # Correct size
```

✅ **Correct:** Bucket size = n + 1 (frequencies range from 1 to n)
```python
bucket = [[] for _ in range(len(nums) + 1)]
```

**Key Insights:**
1. **Counting phase is required** - can't skip it
2. **Bucket sort exploits bounded frequencies** - max frequency ≤ n
3. **O(n) is optimal** for this problem (must read all elements once)
4. **Follow-up:** If multiple queries with different k → precompute buckets once

**Complexity:**
- **Heap:** Time O(n log k), Space O(n)
- **Bucket Sort:** Time O(n), Space O(n)

---

### #019 Merge K Sorted Lists ⭐

**Difficulty:** Hard | **Frequency:** 76.4%

**Task:** Merge k sorted linked lists into one sorted list.

**Input:** `lists = [[1,4,5], [1,3,4], [2,6]]`
**Output:** `[1,1,2,3,4,4,5,6]`

**What Makes This Special:**

This is the **quintessential K-way merge problem**. Appears in merge sort, external sorting, log aggregation, time-series merging. Must know cold!

**Two Approaches:**

1. **Min Heap (O(N log k)):**
   ```python
   def mergeKLists(lists):
       import heapq
       heap = []

       # Initialize: add first node from each list
       for i, node in enumerate(lists):
           if node:
               heapq.heappush(heap, (node.val, i, node))

       dummy = ListNode(0)
       current = dummy

       while heap:
           val, i, node = heapq.heappop(heap)
           current.next = node
           current = current.next

           if node.next:
               heapq.heappush(heap, (node.next.val, i, node.next))

       return dummy.next
   ```

2. **Divide and Conquer (O(N log k)):**
   ```python
   def mergeKLists(lists):
       if not lists:
           return None

       # Merge pairs repeatedly until one list remains
       while len(lists) > 1:
           merged = []
           for i in range(0, len(lists), 2):
               l1 = lists[i]
               l2 = lists[i + 1] if i + 1 < len(lists) else None
               merged.append(mergeTwoLists(l1, l2))
           lists = merged

       return lists[0]
   ```

**Why O(N log k)?**

- **N** = total nodes across all lists
- **k** = number of lists
- **Heap approach:** Each of N nodes: 1 pop + 1 push = 2 log k operations → O(N log k)
- **D&C approach:** log k levels (each level merges pairs), each level processes all N nodes → O(N log k)

**Step-by-Step Example (Heap):**

```
lists = [[1,4,5], [1,3,4], [2,6]]
         L0      L1       L2

Step 1: Initialize heap with first node from each list
heap = [(1, 0, L0.node1), (1, 1, L1.node1), (2, 2, L2.node2)]
       ↑ value  ↑ list_idx ↑ node object

Step 2: Extract minimum (1 from L0)
Pop: (1, 0, L0.node1)
Result: [1]
Add next from L0: (4, 0, L0.node4)
heap = [(1, 1, L1.node1), (2, 2, L2.node2), (4, 0, L0.node4)]

Step 3: Extract minimum (1 from L1)
Pop: (1, 1, L1.node1)
Result: [1, 1]
Add next from L1: (3, 1, L1.node3)
heap = [(2, 2, L2.node2), (4, 0, L0.node4), (3, 1, L1.node3)]

Step 4: Extract minimum (2 from L2)
Pop: (2, 2, L2.node2)
Result: [1, 1, 2]
Add next from L2: (6, 2, L2.node6)
heap = [(4, 0, L0.node4), (3, 1, L1.node3), (6, 2, L2.node6)]

Continue until heap empty...
Final: [1, 1, 2, 3, 4, 4, 5, 6] ✓
```

**Visual Understanding (Heap State):**

```
Three sorted lists:
L0: 1 → 4 → 5
L1: 1 → 3 → 4
L2: 2 → 6

Heap tracks "current head" of each list:
Initially: heap = [1(L0), 1(L1), 2(L2)]
           Root = min(1,1,2) = 1(L0)

After pop 1(L0): heap = [1(L1), 2(L2), 4(L0)]
                 Root = min(1,2,4) = 1(L1)

Pattern: Heap always contains ≤ k nodes (one per list)
```

**Common Bugs:**

❌ **Wrong:** Can't push ListNode directly to heap (Python can't compare nodes)
```python
heapq.heappush(heap, node)  # Error if values are equal!
```

✅ **Correct:** Use tuple with index to break ties
```python
heapq.heappush(heap, (node.val, i, node))
```

**Why Include Index?**

When two nodes have same value, Python compares next tuple element (the node object). Nodes aren't comparable → crash! Adding index ensures tie-breaking.

**Key Insights:**
1. **Heap size = k, not N** - very space-efficient
2. **Each element processed once** - optimal O(N) work
3. **Log k factor unavoidable** - must maintain order among k sources
4. **Dummy head pattern** - simplifies linked list construction

**Complexity:**
- **Heap:** Time O(N log k), Space O(k)
- **D&C:** Time O(N log k), Space O(log k) recursion

---

### #082 Find Median from Data Stream ⭐

**Difficulty:** Hard | **Frequency:** 40.7%

**Task:** Design a data structure that supports adding numbers and finding median.

**Operations:**
- `addNum(num)` - Add integer to data structure
- `findMedian()` - Return median of all elements

**Example:**
```
addNum(1)
addNum(2)
findMedian() → 1.5
addNum(3)
findMedian() → 2.0
```

**What Makes This Special:**

This is the **foundation for two-heap technique**. Once you master this, sliding window median (#034) is just an extension. The insight - split data into two balanced halves - is profound!

**The Two-Heap Invariant:**

```
Max Heap (small)     Min Heap (large)
Lower half          Upper half
     3                   5
    / \                 / \
   1   2               7   8

Invariants:
1. len(small) == len(large) OR len(small) == len(large) + 1
2. All elements in small ≤ All elements in large

Median:
- If odd (small has one more): median = -small[0]
- If even (same size): median = (-small[0] + large[0]) / 2
```

**Full Implementation with Comments:**

```python
class MedianFinder:
    def __init__(self):
        self.small = []  # max heap (store negatives)
        self.large = []  # min heap

    def addNum(self, num):
        # Step 1: Add to max heap (small)
        heapq.heappush(self.small, -num)

        # Step 2: Balance values (ensure all small ≤ all large)
        # If largest of small > smallest of large → swap
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # Step 3: Balance sizes
        # small can have at most 1 more than large
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # large should never have more than small
        if len(self.large) > len(self.small):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self):
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0
```

**Step-by-Step Example:**

```
addNum(1):
  small = [-1], large = []
  Sizes: 1 vs 0 ✓ (allowed)

addNum(2):
  heappush(small, -2) → small = [-2, -1]
  Check values: -small[0] = 2, large is empty ✓
  Sizes: 2 vs 0 → too imbalanced!
  Move: large.add(2) → small = [-1], large = [2]
  Sizes: 1 vs 1 ✓

findMedian():
  Even total: (-small[0] + large[0]) / 2 = (1 + 2) / 2 = 1.5 ✓

addNum(3):
  heappush(small, -3) → small = [-3, -1]
  Check values: -small[0] = 3, large[0] = 2 → 3 > 2! Swap!
  Move 3 to large → small = [-1], large = [2, 3]
  Sizes: 1 vs 2 → large too big!
  Move 2 to small → small = [-2, -1], large = [3]
  Sizes: 2 vs 1 ✓

findMedian():
  Odd total: -small[0] = 2 ✓
```

**Visual Understanding:**

```
After addNum(1), addNum(2), addNum(3):

small (max heap)    large (min heap)
     2                   3
    /
   1

All in small ≤ All in large: {1,2} ≤ {3} ✓
Sizes: 2 vs 1 ✓
Median = max(small) = 2 ✓
```

**Common Bugs:**

❌ **Wrong:** Forget to negate when adding to max heap
```python
heapq.heappush(self.small, num)  # Wrong! This makes it min heap
```

✅ **Correct:** Negate for max heap behavior
```python
heapq.heappush(self.small, -num)  # Correct max heap
```

❌ **Wrong:** Forget to negate when popping from max heap
```python
val = heapq.heappop(self.small)  # Wrong! val is negative
```

✅ **Correct:** Negate to get original value
```python
val = -heapq.heappop(self.small)  # Correct positive value
```

**Key Insights:**
1. **Always add to small first** - simplifies logic
2. **Two-phase balancing** - first balance values, then balance sizes
3. **Max heap via negation** - Python only has min heap
4. **Odd vs even handling** - store extra element in small

**Complexity:**
- **addNum:** O(log n) - heap operations
- **findMedian:** O(1) - just peek at roots
- **Space:** O(n) - store all elements

---

### #034 Sliding Window Median

**Difficulty:** Hard | **Frequency:** 65.0%

**Task:** Given array `nums` and integer `k`, return median of each sliding window of size k.

**Input:** `nums = [1,3,-1,-3,5,3,6,7], k = 3`
**Output:** `[1.0, -1.0, -1.0, 3.0, 5.0, 6.0]`

**What Makes This Special:**

Combines two-heap technique (#082) with **lazy deletion**. You can't efficiently remove arbitrary elements from heap, so you mark them for deletion and clean up lazily!

**The Challenge:**

In #082, we only add elements. Here, we must:
1. Add new element (entering window)
2. Remove old element (leaving window) ← THE HARD PART

**Heap Removal Problem:**

```python
# Can't do this efficiently!
heap = [1, 2, 3, 4, 5]
heap.remove(3)  # O(n) time - must search + reheapify!
```

**Solution: Lazy Deletion:**

Instead of removing immediately, **mark for deletion** in a hash map. Clean up when deleted element reaches heap top.

```python
to_remove = {3: 1}  # element → count to remove

# When popping:
while heap and to_remove[heap[0]] > 0:
    val = heappop(heap)
    to_remove[val] -= 1
```

**Key Implementation Snippets:**

```python
def medianSlidingWindow(nums, k):
    small, large = [], []
    to_remove = defaultdict(int)
    balance = [0]  # Track size imbalance

    def add_num(num):
        if not small or num <= -small[0]:
            heappush(small, -num)
            balance[0] += 1
        else:
            heappush(large, num)
            balance[0] -= 1

    def remove_num(num):
        to_remove[num] += 1
        if num <= -small[0]:
            balance[0] -= 1  # Will be removed from small later
        else:
            balance[0] += 1  # Will be removed from large later

    def rebalance():
        # Move between heaps to balance sizes
        if balance[0] < 0:  # small too small
            heappush(small, -heappop(large))
            balance[0] += 2
        elif balance[0] > 0:  # small too large
            heappush(large, -heappop(small))
            balance[0] -= 2

        # Clean up heap tops
        while small and to_remove[-small[0]] > 0:
            to_remove[-small[0]] -= 1
            heappop(small)
        while large and to_remove[large[0]] > 0:
            to_remove[large[0]] -= 1
            heappop(large)

    def get_median():
        if k % 2 == 1:
            return float(-small[0])
        return (-small[0] + large[0]) / 2.0

    # Initialize first window
    for i in range(k):
        add_num(nums[i])
    rebalance()
    result = [get_median()]

    # Slide window
    for i in range(k, len(nums)):
        remove_num(nums[i - k])  # Remove outgoing
        add_num(nums[i])         # Add incoming
        rebalance()
        result.append(get_median())

    return result
```

**Why Lazy Deletion Works:**

1. **Deleted elements don't affect correctness** - they're not in current window
2. **Cleaned up before accessing** - rebalance() cleans heap tops before get_median()
3. **Amortized efficiency** - each element cleaned once when it reaches top

**Complexity:**
- **Time:** O(n log k) - n windows, each O(log k) for add/remove
- **Space:** O(k) - heaps + deletion map

**Key Insights:**
1. **Can't remove from heap efficiently** - O(n) operation
2. **Lazy deletion trades space for time** - O(k) extra space for O(log k) operations
3. **Balance tracking crucial** - know which heap has "true" size advantage
4. **Clean before accessing** - ensure heap tops are valid

---

## 🔗 Algorithm Relationships

| If You Can Solve... | Then You Can Solve... | By Adding... |
|---------------------|----------------------|--------------|
| #006 Kth Largest | #015 Top K Frequent | Counting phase + bucket sort optimization |
| #082 Find Median | #034 Sliding Window Median | Window sliding + lazy deletion |
| #019 Merge K Lists | External merge sort | Same K-way merge pattern |
| #006 Kth Largest | Kth smallest in matrix | Same min heap technique |

**Conceptual Hierarchy:**

```
Heap Basics (#006)
    ↓
Top-K Variants (#015)
    ↓
K-Way Merge (#019)

Separate Branch:
Two Heaps (#082)
    ↓
Two Heaps + Sliding (#034)
```

---

## ⚠️ Universal Common Pitfalls

### 1. Wrong Heap Type for Top-K

❌ **Wrong:**
```python
# Want K largest, using max heap
max_heap = []
for num in nums:
    heappush(max_heap, -num)  # Max heap
    if len(max_heap) > k:
        heappop(max_heap)
# Wrong! You'll keep K smallest, not K largest
```

✅ **Correct:**
```python
# Want K largest, use MIN heap
min_heap = []
for num in nums:
    heappush(min_heap, num)
    if len(min_heap) > k:
        heappop(min_heap)  # Remove smallest
# Correct! Min heap root = Kth largest
```

**Why?** Min heap's root is the "weakest survivor" of top K.

---

### 2. Forgetting to Negate for Max Heap

❌ **Wrong:**
```python
# Want max heap
heappush(heap, num)  # This is min heap!
max_val = heap[0]    # Wrong! This is minimum
```

✅ **Correct:**
```python
# Python only has min heap, negate for max
heappush(heap, -num)
max_val = -heap[0]   # Negate back to get maximum
```

---

### 3. Comparing Uncomparable Objects in Heap

❌ **Wrong:**
```python
# Merge K lists
heap = []
for node in lists:
    if node:
        heappush(heap, (node.val, node))  # Error if two nodes have same val!
```

✅ **Correct:**
```python
# Add index to break ties
for i, node in enumerate(lists):
    if node:
        heappush(heap, (node.val, i, node))  # i breaks ties
```

---

### 4. Not Maintaining Two-Heap Invariant

❌ **Wrong:**
```python
# Two heaps
def addNum(num):
    heappush(small, -num)
    # Forget to check if small's max > large's min!
```

✅ **Correct:**
```python
def addNum(num):
    heappush(small, -num)

    # MUST ensure all small ≤ all large
    if small and large and (-small[0] > large[0]):
        val = -heappop(small)
        heappush(large, val)

    # THEN balance sizes
    if len(small) > len(large) + 1:
        val = -heappop(small)
        heappush(large, val)
```

---

## ✅ Testing Strategy

### Test Case Categories:

1. **Size Edge Cases:**
   - Empty array: `nums = [], k = 0`
   - Single element: `nums = [1], k = 1`
   - K = 1: `k = 1`
   - K = n: `k = len(nums)`

2. **Value Edge Cases:**
   - All duplicates: `nums = [5,5,5,5,5]`
   - Negative numbers: `nums = [-1,-2,-3]`
   - Mixed signs: `nums = [-2,0,3,-1,4]`

3. **Order Edge Cases:**
   - Already sorted: `nums = [1,2,3,4,5]`
   - Reverse sorted: `nums = [5,4,3,2,1]`
   - Random order: `nums = [3,1,4,1,5]`

4. **Two-Heap Specific:**
   - Odd count: `nums = [1,2,3]` → median = 2
   - Even count: `nums = [1,2,3,4]` → median = 2.5

### Example Test Suite:

```python
def test_kth_largest():
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([2,1], 1) == 2
    assert findKthLargest([-1,-1], 2) == -1

def test_median_finder():
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
```

---

## 💎 Mastery Insights

### When to Use Each Pattern:

| Pattern | Signal Words | Problems |
|---------|-------------|----------|
| Top-K | "K largest/smallest/most frequent" | #006, #015 |
| K-Way Merge | "Merge K sorted..." | #019 |
| Two Heaps | "Median", "streaming data" | #082, #034 |
| Prefix Sum + Binary Search | "Weighted random" | #012 |

### The Counterintuitive Nature of Heaps:

**For beginners:** "Want largest? Use max heap!"
**Reality:** Want K largest? Use **min heap** of size K!

**Why counterintuitive?**
- **Max heap** tracks largest element (global maximum)
- **Min heap of size K** tracks Kth largest (boundary element)

**Analogy:** Finding "top K students" vs "cutoff score"
- Max heap → finds valedictorian (top 1)
- Min heap → finds cutoff (top K boundary)

### Python Heap Quirk:

Python's `heapq` only provides **min heap**. For max heap:
```python
# Option 1: Negate values
heappush(max_heap, -val)
max_val = -heappop(max_heap)

# Option 2: Use (-val, val) tuple
heappush(max_heap, (-val, val))
_, val = heappop(max_heap)
```

### Time Complexity Cheat Sheet:

| Operation | Min/Max Heap | Sorted Array | Balanced BST |
|-----------|--------------|--------------|--------------|
| Find min/max | O(1) | O(1) | O(log n) |
| Insert | O(log n) | O(n) | O(log n) |
| Delete min/max | O(log n) | O(n) | O(log n) |
| Delete arbitrary | O(n) | O(n) | O(log n) |
| Build from n items | O(n) | O(n log n) | O(n log n) |

**When to choose heap:**
- ✅ Need **repeated** find/delete min/max
- ✅ Don't need to search arbitrary elements
- ❌ Need to find median frequently → Use two heaps
- ❌ Need sorted order → Use sort or BST

---

## 📚 Study Order & Practice Progression

### Phase 1: Foundation (Week 1)
1. **#006 Kth Largest Element** - Master Top-K pattern
   - Implement with min heap
   - Compare to quickselect
   - Time yourself: < 10 minutes

### Phase 2: Variations (Week 1-2)
2. **#015 Top K Frequent Elements** - Add counting phase
   - Implement heap solution
   - Implement bucket sort
   - Understand when each is better

3. **#019 Merge K Sorted Lists** - K-way merge
   - Implement heap solution
   - Implement divide-and-conquer
   - Practice with arrays, then lists

### Phase 3: Advanced (Week 2-3)
4. **#082 Find Median from Data Stream** - Two heaps foundation
   - Draw heap state for every operation
   - Practice balancing logic until automatic
   - This is the key problem!

5. **#034 Sliding Window Median** - Add lazy deletion
   - Build on #082
   - Understand balance tracking
   - Implement lazy cleanup

### Phase 4: Mastery (Week 3-4)
6. **#012 Random Pick with Weight** - Binary search review
7. **#091 Random Pick Index** - Reservoir sampling

### Mastery Criteria:
- ✅ Can implement #006 in < 5 minutes
- ✅ Can explain why min heap for K largest (< 1 minute)
- ✅ Can implement #082 from memory (< 15 minutes)
- ✅ Can identify heap pattern from problem statement immediately
- ✅ Can debug off-by-one errors in two-heap balancing

---

## 🎯 Interview Tips

### Communication Script:

**When you see Top-K problem:**
> "This is a classic Top-K problem. I'll use a min heap of size K to track the K largest elements. The counterintuitive insight is that we need a min heap, not a max heap, because the heap's root will be the Kth largest - the boundary element."

**When you see two-heap median:**
> "I'll use two heaps - a max heap for the lower half and a min heap for the upper half. The key invariant is that all elements in the max heap are less than or equal to all elements in the min heap, and the heaps differ in size by at most one. This gives us O(log n) insertion and O(1) median queries."

### Common Interview Follow-ups:

1. **"What if we need Kth smallest instead?"**
   - Use max heap of size K (opposite type)

2. **"What if K is very large, say K = n/2?"**
   - Quickselect might be better (O(n) average)
   - Or find (n-K)th largest instead

3. **"Can you do better than O(n log k) for Top-K?"**
   - Bucket sort can achieve O(n) if frequencies bounded
   - Linear-time selection (BFPRT algorithm) for exact Kth

4. **"How would you handle updates to the median finder?"**
   - Two heaps already handle insertions
   - Deletions require lazy deletion (see #034)

### Red Flags to Avoid:

❌ "I'll sort the array" → Interviewer wants you to use heap
❌ "I'll use a max heap for K largest" → Shows misunderstanding
❌ "Heap operations are O(1)" → They're O(log n)
❌ Implementing heap from scratch → Use built-in unless asked

### Time Budgets (45-min interview):

- Problem clarification: 3-5 min
- Approach explanation: 3-5 min
- Coding: 15-20 min
- Testing: 5-10 min
- Follow-ups: 5-10 min

**Aim to finish #006 in 10-15 minutes** to leave time for follow-ups.

---

## 📈 Complexity Summary

| Problem | Time | Space | Key Technique |
|---------|------|-------|---------------|
| #006 Kth Largest | O(n log k) | O(k) | Min heap size K |
| #015 Top K Frequent | O(n) | O(n) | Bucket sort |
| #019 Merge K Lists | O(N log k) | O(k) | K-way merge heap |
| #082 Find Median | O(log n) add, O(1) find | O(n) | Two heaps |
| #034 Sliding Window Median | O(n log k) | O(k) | Two heaps + lazy deletion |
| #012 Random Pick | O(log n) pick | O(n) | Prefix sum + binary search |
| #091 Random Pick Index | O(n) pick | O(n) | Reservoir sampling |

---

## 🏆 From Good to Great

### Good: You can solve the problems
### Great: You understand the why

**Master these concepts:**

1. **Why opposite heap?**
   Root of min heap = weakest survivor of top K = Kth largest

2. **Why two heaps for median?**
   Median = boundary between halves. Two heaps track this boundary explicitly.

3. **Why lazy deletion?**
   Can't remove from heap efficiently (O(n)). Lazily cleaning when element reaches top is O(log n) amortized.

4. **Why O(N log k) not O(N log N) for merge K?**
   Heap size = k, not N. Each of N elements: O(log k) operation.

### Challenge Problems:

Once you've mastered these 7:
- **LeetCode 295** (same as #082)
- **LeetCode 480** (same as #034)
- **LeetCode 347** (same as #015)
- **LeetCode 23** (same as #019)
- **LeetCode 215** (same as #006)
- **LeetCode 373** - Find K Pairs with Smallest Sums
- **LeetCode 378** - Kth Smallest Element in Sorted Matrix
- **LeetCode 502** - IPO (two heaps + greedy)

---

[← Back to Main](../README.md)
