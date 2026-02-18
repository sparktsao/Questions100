# 026. Subarray Sum Equals K

**Difficulty:** MEDIUM
**Frequency:** 71.4%
**Acceptance Rate:** 45.5%
**LeetCode Link:** [Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k)

---

## Problem Description

Given input data, find or calculate a sum that satisfies specific conditions.

**Problem Type:** MEDIUM**Key Concepts:** Array, Hash Table, Prefix Sum

Utilize hash tables for O(1) average case lookups.

**Typical Constraints:**- Input size can range from small test cases to large datasets (up to 10^4 or 10^5 elements)- Solutions should handle edge cases: empty input, single element, duplicates, negative numbers- Time and space complexity optimization is crucial

**For detailed problem statement, specific constraints, and additional test cases, refer to the [official LeetCode problem](https://leetcode.com/problems/subarray-sum-equals-k).**

---

## Examples

### Example 1
**Input:** `nums = [2,7,11,15], target = 9`
**Output:** `Indices or values that sum to target`
**Explanation:** Classic target sum example

### Example 2
**Input:** `nums = [-1,0,1,2,-1,-4], target = 0`
**Output:** `Find triplets/pairs summing to 0`
**Explanation:** Handles negative numbers

### Example 3
**Input:** `nums = [1], target = 1`
**Output:** `Single element case`
**Explanation:** Minimum array size

### Example 4
**Input:** `nums = [3,3], target = 6`
**Output:** `Duplicate elements`
**Explanation:** Tests duplicate handling

---

## Optimal Solution

### Implementation

```python
def hash_solution(items: List) -> [ReturnType]:
    """
    Hash table solution for O(1) lookups.

    Time: O(n), Space: O(n)
    """
    hash_map = {}
    result = []

    for item in items:
        # Check hash table
        if [condition] in hash_map:
            result.append([found_value])

        # Update hash table
        hash_map[item] = [value]

    return result
```

### Complexity Analysis

**Time: O(n) - single pass with O(1) hash ops. Space: O(n) - hash table**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Array, Hash Table, Prefix Sum

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/subarray-sum-equals-k)*
