# 030. Next Permutation

**Difficulty:** MEDIUM
**Frequency:** 67.4%
**Acceptance Rate:** 43.1%
**LeetCode Link:** [Next Permutation](https://leetcode.com/problems/next-permutation)

---

## Problem Description

A **permutation** of an array of integers is an arrangement of its members into a sequence or linear order.

- For example, for `arr = [1,2,3]`, the following are all the permutations of `arr`: `[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], [3,2,1]`.

The **next permutation** of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the **next permutation** of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.
- Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.
- While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because `[3,2,1]` does not have a lexicographical larger rearrangement.

Given an array of integers `nums`, find the next permutation of `nums`.

The replacement must be **in place** and use only constant extra memory.

**Constraints:**
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100

---

## Examples

### Example 1
**Input:** `nums = [1,2,3]`
**Output:** `[1,3,2]`
**Explanation:** Next lexicographically greater permutation

### Example 2
**Input:** `nums = [3,2,1]`
**Output:** `[1,2,3]`
**Explanation:** In descending order, no greater permutation exists, wrap to smallest

### Example 3
**Input:** `nums = [1,1,5]`
**Output:** `[1,5,1]`
**Explanation:** Handle duplicates correctly

### Example 4
**Input:** `nums = [1,3,2]`
**Output:** `[2,1,3]`
**Explanation:** Swap 1 with 2, reverse remaining

### Example 5
**Input:** `nums = [1,5,8,4,7,6,5,3,1]`
**Output:** `[1,5,8,5,1,3,4,6,7]`
**Explanation:** Find pivot (4), swap with next larger (5), reverse suffix

---

## Optimal Solution

### Implementation

```python
def nextPermutation(nums: List[int]) -> None:
    """
    Find next permutation in-place using optimal single-pass algorithm.

    Time: O(n), Space: O(1)
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)

    # Step 1: Find the first decreasing element from right (pivot)
    # This is the rightmost element that can be increased
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: If pivot found, find the smallest element larger than pivot
    if i >= 0:
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        # Swap pivot with this element
        nums[i], nums[j] = nums[j], nums[i]

    # Step 3: Reverse the suffix after pivot position
    # This gives us the smallest permutation of the suffix
    left, right = i + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

### Detailed Step-by-Step Example

```python
# Example: [1,5,8,4,7,6,5,3,1]

# Step 1: Find pivot (first decreasing from right)
# Scan: 1 < 3 < 5 < 6 < 7, but 4 < 7
# Pivot is at index 3 (value = 4)
# Array: [1,5,8,4,7,6,5,3,1]
#                 ^pivot

# Step 2: Find smallest element > pivot in suffix
# Scan suffix [7,6,5,3,1] from right
# Find 5 (smallest element > 4)
# Swap 4 and 5
# Array: [1,5,8,5,7,6,4,3,1]
#                 ^   ^

# Step 3: Reverse suffix after pivot position
# Suffix [7,6,4,3,1] becomes [1,3,4,6,7]
# Final: [1,5,8,5,1,3,4,6,7]
```

### Alternative Implementation (More Explicit)

```python
def nextPermutation(nums: List[int]) -> None:
    """
    Next permutation with explicit helper functions for clarity.

    Time: O(n), Space: O(1)
    """
    def reverse(nums, start, end):
        """Reverse nums[start:end+1] in place."""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

    n = len(nums)

    # Find the pivot: rightmost element where nums[i] < nums[i+1]
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break

    # If no pivot found, array is in descending order
    if pivot == -1:
        reverse(nums, 0, n - 1)
        return

    # Find smallest element in suffix that's larger than pivot
    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            break

    # Reverse the suffix
    reverse(nums, pivot + 1, n - 1)
```

### Complexity Analysis

**Time: O(n) - three passes at most: find pivot O(n), find swap target O(n), reverse suffix O(n). Space: O(1) - in-place swaps only**

**Why This is Optimal:**
- Single pass to find pivot (worst case n-1 comparisons)
- Single pass to find swap element (worst case n comparisons)
- Single pass to reverse suffix (n/2 swaps worst case)
- Total: O(n) time with O(1) space
- Cannot do better than O(n) - must examine elements to find pivot
- In-place swapping achieves O(1) space requirement
- No additional data structures needed

**Key Insights:**
- Suffix after pivot is always in descending order
- Swapping pivot with next larger element maintains partial order
- Reversing suffix gives smallest possible arrangement
- If no pivot exists, entire array is descending (largest permutation)

---

## Categories & Tags

**Primary Topics:** Array, Two Pointers

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/next-permutation)*
