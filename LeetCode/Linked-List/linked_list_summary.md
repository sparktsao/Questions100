# Linked List - Comprehensive Guide

## Pointer Manipulation & Fast-Slow Techniques

---

## 🎯 Overview

**Total Problems:** 4
**Difficulty:** Easy (0) • Medium (4) • Hard (0)

**Core Concept:**
Master pointer manipulation, dummy nodes, and fast-slow pointer for cycles

**Key Insight:**
Dummy node simplifies edge cases. Fast-slow pointers detect cycles and find middle.

---

## 📚 Sub-Patterns & Techniques


### Pattern 1: Dummy Node for Edge Cases
### Pattern 2: Fast-Slow Pointers (Cycle Detection, Middle Finding)
### Pattern 3: Reverse Linked List (Iterative & Recursive)
### Pattern 4: Merge Sorted Lists


---

## 🎓 Learning Path

Reverse List → Merge Two Lists → Remove Nth from End → Detect Cycle

---

## ⚠️ Common Pitfalls

1. Losing reference to head 2. Not handling None 3. Off-by-one in pointer movement 4. Cycle in reversal

---

## ✅ Testing Strategy

Test: null, single node, two nodes, cycle, no cycle

---

## 💡 Templates & Code Patterns


```python
# Dummy node pattern
dummy = ListNode(0)
dummy.next = head
current = dummy
# ...
return dummy.next

# Fast-slow pattern
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # Cycle detected
```


---

## 💎 Mastery Tips

Always use dummy node. Draw diagrams. Check None cases.

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 032 | [Copy List with Random Pointer](./032_copy_list_with_random_pointer.md) | MEDIUM | 67.4% |
| 045 | [Remove Nth Node From End of List](./045_remove_nth_node_from_end_of_list.md) | MEDIUM | 56.0% |
| 054 | [Add Two Numbers](./054_add_two_numbers.md) | MEDIUM | 47.0% |
| 064 | [Insert into a Sorted Circular Linked List](./064_insert_into_a_sorted_circular_linked_list.md) | MEDIUM | 47.0% |

---

[← Back to Main](../README.md)
