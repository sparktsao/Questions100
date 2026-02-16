# 019. Merge k Sorted Lists

**Difficulty:** HARD
**Frequency:** 76.4%
**Acceptance Rate:** 56.8%
**LeetCode Link:** [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists)

---

## Problem Description

You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

**Constraints:**
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order
- The sum of lists[i].length will not exceed 10^4

---

## Examples

### Example 1
**Input:** `lists = [[1,4,5],[1,3,4],[2,6]]`
**Output:** `[1,1,2,3,4,4,5,6]`
**Explanation:** The linked-lists are:
- 1->4->5
- 1->3->4
- 2->6
Merging them into one sorted list: 1->1->2->3->4->4->5->6

### Example 2
**Input:** `lists = []`
**Output:** `[]`
**Explanation:** Empty input, return empty list

### Example 3
**Input:** `lists = [[]]`
**Output:** `[]`
**Explanation:** Single empty list

### Example 4
**Input:** `lists = [[-2,-1,-1,-1],[]]`
**Output:** `[-2,-1,-1,-1]`
**Explanation:** One non-empty list with duplicates and negative numbers, one empty list

---

## Optimal Solution

### Implementation (Min Heap Approach)

```python
from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted linked lists using min heap.

    Time: O(N log k) where N is total nodes, k is number of lists
    Space: O(k) for heap
    """
    # Min heap to track smallest current node from each list
    # Tuple format: (node.val, index, node) - index prevents comparison of nodes
    min_heap = []

    # Initialize heap with first node from each list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))

    # Dummy head for result list
    dummy = ListNode(0)
    current = dummy

    # Process nodes in sorted order
    while min_heap:
        val, i, node = heapq.heappop(min_heap)

        # Add node to result
        current.next = node
        current = current.next

        # Add next node from same list to heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next
```

### Alternative Implementation (Divide and Conquer)

```python
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merge k sorted lists using divide and conquer.

    Time: O(N log k), Space: O(log k) for recursion stack
    """
    if not lists:
        return None

    def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """Merge two sorted linked lists."""
        dummy = ListNode(0)
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 if l1 else l2
        return dummy.next

    # Divide and conquer: repeatedly merge pairs
    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged_lists.append(mergeTwoLists(l1, l2))

        lists = merged_lists

    return lists[0]
```

### Complexity Analysis

**Min Heap Approach: Time O(N log k), Space O(k)**
**Divide and Conquer: Time O(N log k), Space O(log k)**

**Why This is Optimal:**
- Both approaches achieve O(N log k) time complexity, which is optimal
- Min heap maintains k elements, processing each of N nodes once with log k operations
- Divide and conquer reduces problem by half each iteration (log k levels)
- Handles all edge cases: empty lists, single list, duplicate values, negative numbers
- Space complexity is minimal - only k pointers in heap or log k recursion depth

---

## Categories & Tags

**Primary Topics:** Linked List, Divide and Conquer, Heap (Priority Queue), Merge Sort

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/merge-k-sorted-lists)
