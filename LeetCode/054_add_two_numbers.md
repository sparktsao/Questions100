# 054. Add Two Numbers

**Difficulty:** MEDIUM
**Frequency:** 47.0%
**Acceptance Rate:** 46.2%
**LeetCode Link:** [Add Two Numbers](https://leetcode.com/problems/add-two-numbers)

---

## Problem Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

**Constraints:**
- The number of nodes in each linked list is in the range [1, 100]
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading zeros

---

## Examples

### Example 1
**Input:** `l1 = [2,4,3], l2 = [5,6,4]`
**Output:** `[7,0,8]`
**Explanation:** 342 + 465 = 807. The digits are stored in reverse order.

### Example 2
**Input:** `l1 = [0], l2 = [0]`
**Output:** `[0]`
**Explanation:** 0 + 0 = 0

### Example 3
**Input:** `l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]`
**Output:** `[8,9,9,9,0,0,0,1]`
**Explanation:** 9999999 + 9999 = 10009998

### Example 4
**Input:** `l1 = [2,4,3], l2 = [5,6]`
**Output:** `[7,0,4]`
**Explanation:** 342 + 65 = 407. Different length lists handled correctly.

---

## Optimal Solution

### Implementation

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Add two numbers represented as linked lists with carry handling.

    Time: O(max(m, n)), Space: O(max(m, n))
    """
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        # Get values from current nodes (0 if None)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        # Calculate sum and new carry
        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        # Create new node with the digit
        current.next = ListNode(digit)
        current = current.next

        # Move to next nodes if they exist
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next
```

### Alternative Implementation (More Concise)

```python
def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    Cleaner version with similar logic.

    Time: O(max(m, n)), Space: O(max(m, n))
    """
    dummy = current = ListNode(0)
    carry = 0

    while l1 or l2 or carry:
        val = carry
        if l1:
            val += l1.val
            l1 = l1.next
        if l2:
            val += l2.val
            l2 = l2.next

        carry, val = divmod(val, 10)
        current.next = ListNode(val)
        current = current.next

    return dummy.next
```

### Complexity Analysis

**Time:** O(max(m, n)) where m and n are the lengths of the two linked lists
- We iterate through both lists once
- Each node is visited exactly once

**Space:** O(max(m, n)) for the result linked list
- In the worst case (with carry), the result has max(m, n) + 1 nodes
- Not counting the output, space is O(1) as we only use a few variables

**Why This is Optimal:**
- Cannot do better than O(max(m, n)) time since we must process all digits
- Space complexity is optimal as we need to create the output list
- Single pass solution - no need for multiple iterations
- Handles different length lists naturally
- Properly handles carry propagation including final carry

---

## Categories & Tags

**Primary Topics:** Linked List, Math, Recursion

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/add-two-numbers)*
