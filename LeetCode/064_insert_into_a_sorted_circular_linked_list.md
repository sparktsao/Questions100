# 064. Insert into a Sorted Circular Linked List

**Difficulty:** MEDIUM
**Frequency:** 47.0%
**Acceptance Rate:** 38.1%
**LeetCode Link:** [Insert into a Sorted Circular Linked List](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list)

---

## Problem Description

Given a Circular Linked List node, which is sorted in non-descending order, write a function to insert a value `insertVal` into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list and may not necessarily be the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., the given node is `null`), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the originally given node.

**Constraints:**
- The number of nodes in the list is in the range [0, 5 * 10^4]
- -10^6 <= Node.val <= insertVal <= 10^6

---

## Examples

### Example 1
**Input:** `head = [3,4,1], insertVal = 2`
**Output:** `[3,4,1,2]`
**Explanation:** In the figure below, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should still be sorted.

### Example 2
**Input:** `head = [], insertVal = 1`
**Output:** `[1]`
**Explanation:** The list is empty (given head is null). We create a new single circular list and return the reference to that single node.

### Example 3
**Input:** `head = [1], insertVal = 0`
**Output:** `[1,0]`
**Explanation:** The list has one node. The new node should be inserted between the only node and itself to form a circular list.

### Example 4
**Input:** `head = [3,3,3], insertVal = 3`
**Output:** `[3,3,3,3]`
**Explanation:** When all values are the same, insert at any position maintains sorted order.

---

## Optimal Solution

### Implementation

```python
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

def insert(head: 'Node', insertVal: int) -> 'Node':
    """
    Insert value into sorted circular linked list.

    Time: O(n), Space: O(1)
    """
    new_node = Node(insertVal)

    # Case 1: Empty list
    if not head:
        new_node.next = new_node
        return new_node

    # Case 2: Single node or need to traverse
    prev, curr = head, head.next

    # Traverse to find insertion point
    while True:
        # Case 2a: Insert between prev and curr (normal case)
        if prev.val <= insertVal <= curr.val:
            break

        # Case 2b: Insert at the boundary (largest to smallest transition)
        # This handles: insertVal >= max OR insertVal <= min
        if prev.val > curr.val:
            # We're at the wrap-around point
            if insertVal >= prev.val or insertVal <= curr.val:
                break

        prev = curr
        curr = curr.next

        # Case 2c: Completed full circle (all values are same or insertVal fits anywhere)
        if prev == head:
            break

    # Insert new_node between prev and curr
    prev.next = new_node
    new_node.next = curr

    return head
```

### Alternative Implementation (More Explicit)

```python
def insert(head: 'Node', insertVal: int) -> 'Node':
    """
    Alternative implementation with explicit condition checking.

    Time: O(n), Space: O(1)
    """
    new_node = Node(insertVal)

    # Empty list
    if not head:
        new_node.next = new_node
        return new_node

    # Find insertion point
    prev = head
    curr = head.next

    insert_done = False

    while True:
        # Normal insertion: prev <= insertVal <= curr
        if prev.val <= insertVal <= curr.val:
            insert_done = True

        # Boundary case: we're at max->min transition
        elif prev.val > curr.val:
            # Insert if value is >= max or <= min
            if insertVal >= prev.val or insertVal <= curr.val:
                insert_done = True

        if insert_done:
            prev.next = new_node
            new_node.next = curr
            return head

        prev = curr
        curr = curr.next

        # Completed full circle - all values same
        if prev == head:
            break

    # Insert anywhere (all values are equal)
    prev.next = new_node
    new_node.next = curr

    return head
```

### Complexity Analysis

**Time: O(n) - worst case traverse entire circular list. Space: O(1) - only create one new node**

**Why This is Optimal:**
- Must potentially visit all nodes to find correct insertion point
- O(1) space since we only allocate the new node
- No additional data structures needed
- Handles all edge cases: empty list, single node, all same values, boundary conditions
- In-place insertion maintains circular structure

---

## Categories & Tags

**Primary Topics:** Linked List

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list)*
