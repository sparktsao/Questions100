# 045. Remove Nth Node From End of List

**Difficulty:** MEDIUM
**Frequency:** 56.0%
**Acceptance Rate:** 49.0%
**LeetCode Link:** [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list)

---

## Problem Description

Given the `head` of a linked list, remove the nth node from the end of the list and return its head.

**Constraints:**
- The number of nodes in the list is sz
- 1 <= sz <= 30
- 0 <= Node.val <= 100
- 1 <= n <= sz

**Follow up:** Could you do this in one pass?

---

## Examples

### Example 1
**Input:** `head = [1,2,3,4,5], n = 2`
**Output:** `[1,2,3,5]`
**Explanation:** Remove the 2nd node from the end (node with value 4)

### Example 2
**Input:** `head = [1], n = 1`
**Output:** `[]`
**Explanation:** Remove the only node, resulting in empty list

### Example 3
**Input:** `head = [1,2], n = 1`
**Output:** `[1]`
**Explanation:** Remove the last node

### Example 4
**Input:** `head = [1,2], n = 2`
**Output:** `[2]`
**Explanation:** Remove the first node

---

## Optimal Solution

### Implementation

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    One-pass solution using two pointers with gap of n.

    Time: O(L) where L is length, Space: O(1)
    """
    # Dummy node to handle edge case of removing head
    dummy = ListNode(0)
    dummy.next = head

    # Initialize two pointers
    first = dummy
    second = dummy

    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next

    # Remove the nth node from end
    second.next = second.next.next

    return dummy.next
```

### Alternative Two-Pass Solution

```python
def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """
    Two-pass solution: count length, then remove.

    Time: O(L), Space: O(1)
    """
    # First pass: count length
    length = 0
    current = head
    while current:
        length += 1
        current = current.next

    # Edge case: remove head
    if length == n:
        return head.next

    # Second pass: find node before target
    current = head
    for _ in range(length - n - 1):
        current = current.next

    # Remove target node
    current.next = current.next.next

    return head
```

### Complexity Analysis

**Time: O(L) - single pass through list. Space: O(1) - constant extra space**

**Why This is Optimal:**
- One-pass solution meets the follow-up requirement
- Dummy node elegantly handles edge case of removing head
- Two-pointer technique with fixed gap is a classic pattern
- No extra space needed beyond pointers

---

## Categories & Tags

**Primary Topics:** Linked List, Two Pointers

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/remove-nth-node-from-end-of-list)*
