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

## Core Insight: `findmiss(pos)`

At any index `pos`, the count of positive integers missing **before** `arr[pos]` is:

```
findmiss(pos) = arr[pos] - pos - 1
```

**Why:** In a perfect world with no gaps, `arr[pos]` should equal `pos + 1`.
Every unit of excess means one missing number.

```
pos:      0  1  2  3  4
arr:      2  3  4  7  11
ideal:    1  2  3  4  5
gap:      1  1  1  3  6   ← arr[pos] - pos - 1
```

---

## 3-Case Analysis

The answer lives in exactly one of three zones:

```
[ before arr[0] ] [ inside the array ] [ after arr[-1] ]
   Case 1              Case 3              Case 2
```

**Case 1 — gap is entirely before the array starts:**
`findmiss(0) >= k` means `k` missing numbers all lie before `arr[0]`.
Answer = `k` directly (1st missing is 1, 2nd is 2, ...).

**Case 2 — gap extends past the end of the array:**
`findmiss(n-1) < k` means even with all array gaps counted, we need `remain = k - findmiss(n-1)` more after `arr[-1]`.
Answer = `arr[-1] + remain`.

**Case 3 — gap falls inside the array:**
Binary search for the leftmost index where `findmiss(mid) >= k`.
At that index, back up one step to the last index with `findmiss < k`, then count the remaining needed.

```
remain = k - findmiss(left - 1)
answer = arr[left - 1] + remain
```

---

## Implementation

```python
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        def findmiss(pos):
            return arr[pos] - pos - 1

        # Case 1: all k missing numbers are before arr[0]
        # e.g. arr=[4,5,6], k=3 → findmiss(0)=3 >= 3 → return 3
        if findmiss(0) >= k:
            return k

        # Case 2: k-th missing falls after the entire array
        # e.g. arr=[1,2,3], k=6 → findmiss(2)=0 < 6 → remain=6, return 3+6=9
        if findmiss(len(arr) - 1) < k:
            remain = k - findmiss(len(arr) - 1)
            return arr[-1] + remain

        # Case 3: binary search — find leftmost index where findmiss(mid) >= k
        # Invariant: findmiss(left-1) < k <= findmiss(right)
        left, right = 0, len(arr) - 1
        while left < right:
            mid = left + (right - left) // 2
            if findmiss(mid) < k:
                left = mid + 1
            else:
                right = mid - 1   # ← must use mid-1, not right-1

        # left is now the first index where findmiss(left) >= k
        # the k-th missing sits between arr[left-1] and arr[left]
        remain = k - findmiss(left - 1)
        return arr[left - 1] + remain
```

---

## Trace: `arr = [2,3,4,7,11], k = 5`

```
findmiss(0) = 2-0-1 = 1  < 5  → not Case 1
findmiss(4) = 11-4-1 = 6 >= 5 → not Case 2 → Case 3

BS: left=0, right=4
  mid=2, findmiss(2)=4-2-1=1 < 5  → left=3
  mid=3, findmiss(3)=7-3-1=3 < 5  → left=4
  mid=4, findmiss(4)=6 >= 5       → right=3
  left=4 > right=3 → exit

remain = 5 - findmiss(3) = 5 - 3 = 2
answer = arr[3] + 2 = 7 + 2 = 9  ✓
```

---

## Corner Cases

| Scenario | Example | Expected | Explanation |
|---|---|---|---|
| k before array starts | `arr=[4,5,6], k=3` | `3` | Case 1: `findmiss(0)=3 >= 3` |
| k just before array | `arr=[4,5,6], k=2` | `2` | Case 1: `findmiss(0)=3 >= 2` |
| k past array end | `arr=[1,2,3], k=6` | `9` | Case 2: `findmiss(2)=0`, `remain=6`, `3+6=9` |
| k lands right at array gap | `arr=[1,2,4], k=2` | `5` | Case 3: `findmiss(2)=1 < 2` stays, no index qualifies early; Case 2 fires, `remain=1`, `4+1=5` |
| dense array, single gap | `arr=[1,3], k=1` | `2` | Case 3: `findmiss(0)=0 < 1`, `findmiss(1)=1 >= 1`, `left=1`, `remain=1-0=1`, `arr[0]+1=2` |
| k=1, arr starts at 2 | `arr=[2], k=1` | `1` | Case 1: `findmiss(0)=1 >= 1` |

---

## The `right = mid - 1` vs `right = right - 1` Pitfall

In Case 3, the update must be `right = mid - 1`, **not** `right = right - 1`.

If `mid < right`, using `right = right - 1` skips only the rightmost element, not the midpoint — the binary search degenerates to linear scan and can skip the correct boundary.

---

## Complexity

**Time: O(log n)** — binary search on array indices.
**Space: O(1)** — no extra storage.

---

## Categories & Tags

**Primary Topics:** BS on Array | Lower Bound (missing count)

**Search type:** Data space — binary search on array indices. Count missing before `arr[mid]` = `arr[mid] - (mid+1)`.
**Key:** 3-case split (before array / after array / inside), then binary search for leftmost index where `findmiss >= k`.

**Difficulty Level:** EASY

---

*Problem source: [LeetCode](https://leetcode.com/problems/kth-missing-positive-number)*
