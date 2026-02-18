# 055. Subsets

**Difficulty:** MEDIUM
**Frequency:** 47.0%
**Acceptance Rate:** 80.9%
**LeetCode Link:** [Subsets](https://leetcode.com/problems/subsets)

---

## Problem Description

Given an integer array `nums` of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

**Constraints:**
- 1 <= nums.length <= 10
- -10 <= nums[i] <= 10
- All the numbers of nums are unique

---

## Examples

### Example 1
**Input:** `nums = [1,2,3]`
**Output:** `[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]`
**Explanation:** All possible subsets of [1,2,3]

### Example 2
**Input:** `nums = [0]`
**Output:** `[[],[0]]`
**Explanation:** Single element has two subsets: empty set and the element itself

### Example 3
**Input:** `nums = [1,2]`
**Output:** `[[],[1],[2],[1,2]]`
**Explanation:** Two elements produce 2^2 = 4 subsets

### Example 4
**Input:** `nums = [9,0,3,5,7]`
**Output:** `All 2^5 = 32 possible subsets`
**Explanation:** Each element can be included or excluded independently

---

## Optimal Solution

### Implementation (Backtracking)

```python
def subsets(nums: List[int]) -> List[List[int]]:
    """
    Generate all subsets using backtracking.

    Time: O(2^n * n), Space: O(2^n * n)
    """
    result = []

    def backtrack(start: int, current: List[int]) -> None:
        """Build subsets by choosing to include or exclude each element."""
        # Add current subset to result
        result.append(current[:])  # Make a copy

        # Try adding each remaining element
        for i in range(start, len(nums)):
            current.append(nums[i])     # Include nums[i]
            backtrack(i + 1, current)   # Recurse with next elements
            current.pop()               # Backtrack (exclude nums[i])

    backtrack(0, [])
    return result
```

### Alternative Implementation (Iterative)

```python
def subsets(nums: List[int]) -> List[List[int]]:
    """
    Iterative approach: start with empty set, add each element to existing subsets.

    Time: O(2^n * n), Space: O(2^n * n)
    """
    result = [[]]  # Start with empty subset

    for num in nums:
        # For each existing subset, create a new subset by adding current number
        result += [curr + [num] for curr in result]

    return result
```

### Alternative Implementation (Bit Manipulation)

```python
def subsets(nums: List[int]) -> List[List[int]]:
    """
    Use bit manipulation: each subset corresponds to a binary number.

    Time: O(2^n * n), Space: O(2^n * n)
    """
    n = len(nums)
    result = []

    # There are 2^n possible subsets
    for i in range(1 << n):  # 2^n iterations
        subset = []
        for j in range(n):
            # Check if jth bit is set in i
            if i & (1 << j):
                subset.append(nums[j])
        result.append(subset)

    return result
```

### Complexity Analysis

**All approaches:**
- **Time:** O(2^n * n)
  - 2^n subsets to generate
  - Each subset takes O(n) time to copy/build
- **Space:** O(2^n * n)
  - Storing all subsets (output space)
  - Each subset can have up to n elements

**Why This is Optimal:**
- Cannot do better than O(2^n) since there are exactly 2^n subsets
- The factor of n comes from copying/building each subset
- This is an output-sensitive problem where the output size dominates

**Comparison of Approaches:**
- **Backtracking:** Most intuitive, mirrors the recursive nature of the problem
- **Iterative:** Simple and elegant, builds subsets incrementally
- **Bit Manipulation:** Clever use of binary representation, good for understanding the math

---

## Categories & Tags

**Primary Topics:** Array, Backtracking, Bit Manipulation

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/subsets)*
