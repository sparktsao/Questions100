# 028. Dot Product of Two Sparse Vectors

**Difficulty:** MEDIUM
**Frequency:** 69.5%
**Acceptance Rate:** 89.9%
**LeetCode Link:** [Dot Product of Two Sparse Vectors](https://leetcode.com/problems/dot-product-of-two-sparse-vectors)

---

## Problem Description

Given two sparse vectors, compute their dot product.

Implement class `SparseVector`:
- `SparseVector(nums)` Initializes the object with the vector `nums`
- `dotProduct(vec)` Compute the dot product between the instance of SparseVector and `vec`

A **sparse vector** is a vector that has mostly zero values, you should store the sparse vector **efficiently** and compute the dot product between two SparseVector.

**Follow up:** What if only one of the vectors is sparse?

**Constraints:**
- n == nums1.length == nums2.length
- 1 <= n <= 10^5
- 0 <= nums1[i], nums2[i] <= 100

---

## Examples

### Example 1
**Input:** `nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]`
**Output:** `8`
**Explanation:**
```
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
```

### Example 2
**Input:** `nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]`
**Output:** `0`
**Explanation:**
```
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0
```

### Example 3
**Input:** `nums1 = [0,1,0,0,2,0,0], nums2 = [1,0,0,0,3,0,4]`
**Output:** `6`
**Explanation:**
```
v1 = SparseVector(nums1)
v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*1 + 1*0 + 0*0 + 0*0 + 2*3 + 0*0 + 0*4 = 6
```

### Example 4
**Input:** `nums1 = [1,2,3,4,5], nums2 = [1,1,1,1,1]`
**Output:** `15`
**Explanation:** Dense vectors, all positions have values

---

## Optimal Solution

### Implementation (Hash Map Approach)

```python
class SparseVector:
    """
    Store only non-zero elements in hash map for space efficiency.

    Time: O(n) for init, O(L) for dotProduct where L is min non-zero elements
    Space: O(L) where L is number of non-zero elements
    """
    def __init__(self, nums: List[int]):
        # Store only non-zero values with their indices
        self.non_zero = {}
        for i, val in enumerate(nums):
            if val != 0:
                self.non_zero[i] = val

    def dotProduct(self, vec: 'SparseVector') -> int:
        # Iterate through the vector with fewer non-zero elements
        if len(self.non_zero) > len(vec.non_zero):
            return vec.dotProduct(self)

        result = 0
        # Only check indices where both vectors have non-zero values
        for i, val in self.non_zero.items():
            if i in vec.non_zero:
                result += val * vec.non_zero[i]

        return result


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
```

### Alternative Implementation (Two Pointers on Sorted Pairs)

```python
class SparseVector:
    """
    Store non-zero elements as sorted list of (index, value) pairs.
    Use two pointers for dot product calculation.

    Time: O(n) for init, O(L1 + L2) for dotProduct
    Space: O(L) where L is number of non-zero elements
    """
    def __init__(self, nums: List[int]):
        # Store as list of (index, value) tuples, already sorted by index
        self.pairs = [(i, val) for i, val in enumerate(nums) if val != 0]

    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        i, j = 0, 0

        # Two pointers to find matching indices
        while i < len(self.pairs) and j < len(vec.pairs):
            if self.pairs[i][0] == vec.pairs[j][0]:
                # Indices match, multiply values
                result += self.pairs[i][1] * vec.pairs[j][1]
                i += 1
                j += 1
            elif self.pairs[i][0] < vec.pairs[j][0]:
                i += 1
            else:
                j += 1

        return result
```

### Alternative Implementation (Index-Value Pairs with Binary Search)

```python
class SparseVector:
    """
    For cases where one vector is much sparser than the other.
    Use binary search for lookup.

    Time: O(n) for init, O(L * log M) for dotProduct
    Space: O(L)
    """
    def __init__(self, nums: List[int]):
        self.pairs = [(i, val) for i, val in enumerate(nums) if val != 0]

    def dotProduct(self, vec: 'SparseVector') -> int:
        # Use smaller vector to iterate, search in larger
        if len(self.pairs) > len(vec.pairs):
            return vec.dotProduct(self)

        result = 0
        for idx, val in self.pairs:
            # Binary search for matching index in vec
            left, right = 0, len(vec.pairs) - 1
            while left <= right:
                mid = (left + right) // 2
                if vec.pairs[mid][0] == idx:
                    result += val * vec.pairs[mid][1]
                    break
                elif vec.pairs[mid][0] < idx:
                    left = mid + 1
                else:
                    right = mid - 1

        return result
```

### Complexity Analysis

**Time: O(n) initialization, O(L) dot product where L = min(non-zero elements in both vectors). Space: O(L) for storing non-zero elements**

**Why Hash Map is Often Best:**
- O(1) lookup time for matching indices
- O(L) space only stores non-zero elements, huge savings for sparse vectors
- Dot product in O(min(L1, L2)) by iterating smaller vector
- Simple implementation with clear logic
- Handles arbitrary sparsity patterns efficiently

**When to Use Two Pointers:**
- When memory layout matters (cache-friendly sequential access)
- When indices need to be processed in order
- Slightly better cache locality than hash map

---

## Categories & Tags

**Primary Topics:** Array, Hash Table, Two Pointers, Design

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/dot-product-of-two-sparse-vectors)*
