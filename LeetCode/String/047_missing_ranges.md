# 047. Missing Ranges

**Difficulty:** EASY
**Frequency:** 56.0%
**Acceptance Rate:** 35.3%
**LeetCode Link:** [Missing Ranges](https://leetcode.com/problems/missing-ranges)

---

## Problem Description

You are given an inclusive range `[lower, upper]` and a sorted unique integer array `nums`, where all elements are in the inclusive range.

A number `x` is considered missing if `x` is in the range `[lower, upper]` and `x` is not in `nums`.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of `nums` is in any of the ranges, and each missing number is in one of the ranges.

Each range `[a,b]` in the list should be output as:
- "a->b" if a != b
- "a" if a == b

**Constraints:**
- -10^9 <= lower <= upper <= 10^9
- 0 <= nums.length <= 100
- lower <= nums[i] <= upper
- All the values of nums are unique

---

## Examples

### Example 1
**Input:** `nums = [0,1,3,50,75], lower = 0, upper = 99`
**Output:** `["2","4->49","51->74","76->99"]`
**Explanation:** The ranges are: [2,2] -> "2", [4,49] -> "4->49", [51,74] -> "51->74", [76,99] -> "76->99"

### Example 2
**Input:** `nums = [], lower = 1, upper = 1`
**Output:** `["1"]`
**Explanation:** The only missing range is [1,1], which becomes "1"

### Example 3
**Input:** `nums = [], lower = -3, upper = -1`
**Output:** `["-3->-1"]`
**Explanation:** The only missing range is [-3,-1], which becomes "-3->-1"

### Example 4
**Input:** `nums = [-1], lower = -1, upper = -1`
**Output:** `[]`
**Explanation:** There are no missing ranges since there are no missing numbers

---

## Optimal Solution

### Implementation

```python
def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
    """
    Find missing ranges by checking gaps between consecutive numbers.

    Time: O(n), Space: O(1) excluding output
    """
    def formatRange(start: int, end: int) -> str:
        """Format range as string"""
        if start == end:
            return str(start)
        return f"{start}->{end}"

    result = []
    prev = lower - 1  # Start one before lower bound

    # Process each number and the final gap
    for num in nums + [upper + 1]:
        # Check if there's a gap between prev and current num
        if num - prev >= 2:
            result.append(formatRange(prev + 1, num - 1))
        prev = num

    return result
```

### Alternative Implementation

```python
def findMissingRanges(nums: List[int], lower: int, upper: int) -> List[str]:
    """
    Explicit gap checking approach.

    Time: O(n), Space: O(1)
    """
    def addRange(result: List[str], start: int, end: int):
        if start == end:
            result.append(str(start))
        else:
            result.append(f"{start}->{end}")

    result = []

    # Check gap before first element
    if not nums:
        addRange(result, lower, upper)
        return result

    # Gap before first element
    if nums[0] > lower:
        addRange(result, lower, nums[0] - 1)

    # Gaps between consecutive elements
    for i in range(len(nums) - 1):
        if nums[i + 1] - nums[i] > 1:
            addRange(result, nums[i] + 1, nums[i + 1] - 1)

    # Gap after last element
    if nums[-1] < upper:
        addRange(result, nums[-1] + 1, upper)

    return result
```

### Complexity Analysis

**Time: O(n) - single pass through array. Space: O(1) - constant extra space**

**Why This is Optimal:**
- Must examine all elements to find gaps, so O(n) is optimal
- Clever trick: append upper+1 to handle final gap uniformly
- No extra space needed beyond output list
- Handles edge cases elegantly (empty array, no gaps, negative numbers)

---

## Categories & Tags

**Primary Topics:** Array

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/missing-ranges)*
