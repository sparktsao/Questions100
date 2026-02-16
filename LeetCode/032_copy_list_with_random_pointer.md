# 032. Copy List with Random Pointer

**Difficulty:** MEDIUM
**Frequency:** 67.4%
**Acceptance Rate:** 60.5%
**LeetCode Link:** [Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer)

---

## Problem Description

A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.

Construct a deep copy of the list. The deep copy should consist of exactly `n` brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the `next` and `random` pointer of the new nodes should point to new nodes in the copied list.

Return the head of the copied linked list.

**Constraints:**
- 0 <= n <= 1000
- -10^4 <= Node.val <= 10^4
- Node.random is null or is pointing to some node in the linked list

---

## Examples

### Example 1
**Input:** `head = [[7,null],[13,0],[11,4],[10,2],[1,0]]`
**Output:** `[[7,null],[13,0],[11,4],[10,2],[1,0]]`
**Explanation:** 5 nodes with various random pointers

### Example 2
**Input:** `head = [[1,1],[2,1]]`
**Output:** `[[1,1],[2,1]]`
**Explanation:** 2 nodes, both random point to first node

### Example 3
**Input:** `head = [[3,null],[3,0],[3,null]]`
**Output:** `[[3,null],[3,0],[3,null]]`
**Explanation:** 3 nodes with same value

### Example 4
**Input:** `head = []`
**Output:** `[]`
**Explanation:** Empty list

---

## Optimal Solution

### Implementation

```python
def copyRandomList(head: 'Node') -> 'Node':
    """
    Two-pass approach with hash map.

    Time: O(n), Space: O(n)
    """
    if not head:
        return None

    # First pass: create all nodes
    old_to_new = {}
    curr = head
    while curr:
        old_to_new[curr] = Node(curr.val)
        curr = curr.next

    # Second pass: set next and random pointers
    curr = head
    while curr:
        if curr.next:
            old_to_new[curr].next = old_to_new[curr.next]
        if curr.random:
            old_to_new[curr].random = old_to_new[curr.random]
        curr = curr.next

    return old_to_new[head]
```

### Complexity Analysis

**Time: O(n) - two passes. Space: O(n) - hash map**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Hash Table, Linked List

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/copy-list-with-random-pointer)*
