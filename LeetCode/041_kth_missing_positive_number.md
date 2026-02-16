# 041. Kth Missing Positive Number

**Difficulty:** EASY
**Frequency:** 59.4%
**Acceptance Rate:** 62.3%
**LeetCode Link:** [Kth Missing Positive Number](https://leetcode.com/problems/kth-missing-positive-number)

---

## Problem Description

Given an array `arr` of positive integers sorted in a strictly increasing order, and an integer `k`.

Return the kth positive integer that is missing from this array.

**Constraints:**
- 1 <= arr.length <= 1000
- 1 <= arr[i] <= 1000
- 1 <= k <= 1000
- arr[i] < arr[j] for 1 <= i < j <= arr.length

---

## Examples

### Example 1
**Input:** `arr = [2,3,4,7,11], k = 5`
**Output:** `9`
**Explanation:** The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

### Example 2
**Input:** `arr = [1,2,3,4], k = 2`
**Output:** `6`
**Explanation:** The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

### Example 3
**Input:** `arr = [5,6,7,8,9], k = 9`
**Output:** `14`
**Explanation:** The missing positive integers are [1,2,3,4,10,11,12,13,14,...]. The 9th missing positive integer is 14.

### Example 4
**Input:** `arr = [1,10,21,22,25], k = 12`
**Output:** `14`
**Explanation:** Missing numbers include [2,3,4,5,6,7,8,9,11,12,13,14,...]. The 12th missing number is 14.

---

## Optimal Solution

### Implementation

```python
def findKthPositive(arr: List[int], k: int) -> int:
    """
    Binary search to find kth missing positive number.

    Time: O(log n), Space: O(1)
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        # Number of missing integers before arr[mid]
        missing = arr[mid] - (mid + 1)

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1

    # At the end, left is the insertion point
    # k missing numbers = left + k
    return left + k
```

### Alternative Linear Solution

```python
def findKthPositive(arr: List[int], k: int) -> int:
    """
    Linear scan approach for comparison.

    Time: O(n), Space: O(1)
    """
    # Count missing numbers
    for num in arr:
        if num <= k:
            k += 1
        else:
            break

    return k
```

### Complexity Analysis

**Time: O(log n) - binary search. Space: O(1) - constant**

**Why This is Optimal:**
- Binary search achieves logarithmic time complexity
- Key insight: arr[mid] - (mid + 1) gives count of missing numbers before index mid
- No extra space needed beyond variables
- Handles all edge cases efficiently

---

## Categories & Tags

**Primary Topics:** Array, Binary Search

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/kth-missing-positive-number)*
