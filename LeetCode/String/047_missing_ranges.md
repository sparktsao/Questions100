# 047. Missing Ranges

**Difficulty:** EASY
**Frequency:** 56.0%
**Acceptance Rate:** 35.3%
**LeetCode Link:** [Missing Ranges](https://leetcode.com/problems/missing-ranges)

---

## Problem Description

You are given an inclusive range `[lower, upper]` and a sorted unique integer array `nums`, where all elements are within `[lower, upper]`.

Return the smallest sorted list of ranges that cover every missing number exactly.

**Note:** LeetCode has two versions of this problem:
- **Old version** (LC 163): return `List[str]`, format as `"a->b"` or `"a"`
- **New version** (LC 2200): return `List[List[int]]`, format as `[a, b]`

The logic is identical — only the output format differs.

**Constraints:**
- -10^9 <= lower <= upper <= 10^9
- 0 <= nums.length <= 100
- lower <= nums[i] <= upper
- All values of nums are unique

---

## Examples

### Example 1
**Input:** `nums = [0,1,3,50,75], lower = 0, upper = 99`
**Output:** `[[2,2],[4,49],[51,74],[76,99]]`

### Example 2
**Input:** `nums = [], lower = 1, upper = 1`
**Output:** `[[1,1]]`

### Example 3
**Input:** `nums = [-1], lower = -1, upper = -1`
**Output:** `[]` — no missing numbers

---

## Core Insight: 3 Structural Cases

The number line looks like:

```
lower ... [nums[0] nums[1] ... nums[n-1]] ... upper
```

There are exactly **3 regions** where gaps can appear:

```
Case 0: nums is empty → entire [lower, upper] is missing
Case 1: left gap  → between lower and nums[0]
Case 2: middle gaps → between consecutive nums[i] and nums[i+1]
Case 3: right gap → between nums[-1] and upper
```

Handle each case explicitly. This is more code than the sentinel trick, but it maps directly to the structure of the problem — easier to reason about correctness.

---

## Solution: Explicit 3-Case

```python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:

        # Case 0: empty array
        if len(nums) == 0:
            return [[lower, upper]]

        result = []

        # Case 1: left gap — between lower and nums[0]
        if lower < nums[0]:
            result.append([lower, nums[0] - 1])

        # Case 2: middle gaps — between consecutive elements
        prev = nums[0] + 1
        for e in nums[1:]:
            if prev < e:
                result.append([prev, e - 1])
            prev = e + 1          # always advance past e

        # Case 3: right gap — between nums[-1] and upper
        if prev <= upper:
            result.append([prev, upper])

        return result
```

**Time: O(n) — single pass. Space: O(1) excluding output.**

### Trace on Example 1: `nums=[0,1,3,50,75], lower=0, upper=99`

```
Case 1: lower(0) == nums[0](0) → no left gap
Case 2:
  prev=1, e=1: prev==e → prev=2
  prev=2, e=3: prev<e  → append [2,2], prev=4
  prev=4, e=50: prev<e → append [4,49], prev=51
  prev=51, e=75: prev<e → append [51,74], prev=76
Case 3: prev(76) <= upper(99) → append [76,99]

Output: [[2,2],[4,49],[51,74],[76,99]] ✓
```

---

## Alternative: Sentinel Trick (Compact)

Append `upper+1` as a fake sentinel so all three cases collapse into one uniform loop:

```python
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        result = []
        prev = lower - 1    # sentinel before lower

        for num in nums + [upper + 1]:   # sentinel after upper
            if num - prev >= 2:          # gap of 1 means no missing numbers
                result.append([prev + 1, num - 1])
            prev = num

        return result
```

### Why `num - prev >= 2`?

- `prev` tracks the last seen number
- If `num == prev + 1`, they are adjacent — no gap
- If `num >= prev + 2`, there's at least one missing number between them

### Trace on Example 1 with sentinels:

```
prev = -1 (lower-1 = 0-1)
nums + [100] = [0, 1, 3, 50, 75, 100]

num=0:   0-(-1)=1  < 2 → no gap. prev=0
num=1:   1-0=1     < 2 → no gap. prev=1
num=3:   3-1=2    >= 2 → append [2,2].   prev=3
num=50:  50-3=47  >= 2 → append [4,49].  prev=50
num=75:  75-50=25 >= 2 → append [51,74]. prev=75
num=100: 100-75=25>= 2 → append [76,99]. prev=100

Output: [[2,2],[4,49],[51,74],[76,99]] ✓
```

---

## Comparison

| | Explicit 3-case | Sentinel trick |
|---|---|---|
| Code length | longer | 6 lines |
| Readability | mirrors problem structure | requires understanding `prev=lower-1` and `upper+1` |
| Bug risk | more branches to get right | fewer branches, easier to verify |
| Interview preference | shows structured thinking | shows cleverness |

**Which to choose:** The sentinel trick is compact and elegant once you see it, but requires explaining *why* `lower-1` and `upper+1` are valid sentinels. The explicit 3-case version is self-documenting.

---

## Edge Cases

| Input | Expected | Trap |
|---|---|---|
| `nums=[]` | `[[lower, upper]]` | explicit empty check needed in 3-case version |
| `nums=[-1], lower=-1, upper=-1` | `[]` | no gap anywhere |
| `nums=[lower], upper=lower` | `[]` | nums covers the entire range |
| `lower=upper` and nums is empty | `[[lower,lower]]` | single-element range |

---

## Categories & Tags

**Primary Topics:** Array | Linear Scan (3-case gap detection)

**Difficulty Level:** EASY

**Why tricky despite EASY label:** 34% acceptance rate — the 3 structural cases (left gap, middle gaps, right gap) are easy to miss or conflate, especially the empty-array edge case. The sentinel trick hides this but requires understanding why the sentinels are valid.

---

*Problem source: [LeetCode](https://leetcode.com/problems/missing-ranges)*
