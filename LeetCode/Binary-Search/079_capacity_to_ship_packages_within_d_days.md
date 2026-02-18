# 079. Capacity To Ship Packages Within D Days

**Difficulty:** MEDIUM
**Frequency:** 40.7%
**Acceptance Rate:** 72.1%
**LeetCode Link:** [Capacity To Ship Packages Within D Days](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days)

---

## Problem Description

A conveyor belt has packages that must be shipped from one port to another within `days` days.

The `i-th` package on the conveyor belt has a weight of `weights[i]`. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.

Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within `days` days.

**Note:** Packages must be shipped in the order they appear in the array (you cannot rearrange them).

**Constraints:**
- `1 <= days <= weights.length <= 5 × 10^4`
- `1 <= weights[i] <= 500`

---

## Examples

### Example 1
**Input:** `weights = [1,2,3,4,5,6,7,8,9,10], days = 5`
**Output:** `15`
**Explanation:** A ship capacity of 15 is the minimum to ship all packages in 5 days:
- Day 1: 1, 2, 3, 4, 5 (total = 15)
- Day 2: 6, 7 (total = 13)
- Day 3: 8 (total = 8)
- Day 4: 9 (total = 9)
- Day 5: 10 (total = 10)

### Example 2
**Input:** `weights = [3,2,2,4,1,4], days = 3`
**Output:** `6`
**Explanation:** A ship capacity of 6:
- Day 1: 3, 2 (total = 5)
- Day 2: 2, 4 (total = 6)
- Day 3: 1, 4 (total = 5)

### Example 3
**Input:** `weights = [1,2,3,1,1], days = 4`
**Output:** `3`
**Explanation:** Capacity of 3:
- Day 1: 1, 2 (total = 3)
- Day 2: 3 (total = 3)
- Day 3: 1, 1 (total = 2)
- Day 4: 1 (total = 1)

### Example 4
**Input:** `weights = [10,50,100,100,50,100,100,100], days = 5`
**Output:** `200`
**Explanation:** Need capacity of 200 to ship the 100-weight packages, distributed across 5 days.

---

## Optimal Solution

### Implementation

```python
def shipWithinDays(weights: List[int], days: int) -> int:
    """
    Binary search on ship capacity to find minimum viable capacity.

    Time: O(n log(sum)), Space: O(1)
    where n is number of packages, sum is total weight
    """
    def can_ship_with_capacity(capacity):
        """Check if all packages can be shipped in 'days' with given capacity."""
        days_needed = 1
        current_load = 0

        for weight in weights:
            if current_load + weight > capacity:
                # Need a new day
                days_needed += 1
                current_load = weight
                if days_needed > days:
                    return False
            else:
                current_load += weight

        return True

    # Binary search bounds
    left = max(weights)   # Minimum: must fit heaviest package
    right = sum(weights)  # Maximum: ship everything in one day

    while left < right:
        mid = left + (right - left) // 2

        if can_ship_with_capacity(mid):
            # Can ship with this capacity, try smaller
            right = mid
        else:
            # Cannot ship, need larger capacity
            left = mid + 1

    return left
```

### Complexity Analysis

**Time: O(n × log(sum(weights))) - binary search with O(n) feasibility check. Space: O(1) - constant space**

**Why This is Optimal:**
- Binary search on answer reduces search from O(sum) to O(log sum)
- Cannot do better than O(n) for feasibility check (must examine all packages)
- Search space is minimized: [max(weights), sum(weights)]
- Monotonic property: if capacity C works, all C' > C also work
- Early termination in feasibility check when days_needed exceeds days

---

## Categories & Tags

**Primary Topics:** Array, Binary Search

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days)*
