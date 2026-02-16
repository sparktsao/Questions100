# 094. Koko Eating Bananas

**Difficulty:** MEDIUM
**Frequency:** 32.0%
**Acceptance Rate:** 49.1%
**LeetCode Link:** [Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas)

---

## Problem Description

Koko loves to eat bananas. There are `n` piles of bananas, the `ith` pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

**Constraints:**
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9

---

## Examples

### Example 1
**Input:** `piles = [3,6,7,11], h = 8`
**Output:** `4`
**Explanation:** With speed k=4, Koko eats: 1hr (3), 2hrs (6), 2hrs (7), 3hrs (11) = 8 hours total

### Example 2
**Input:** `piles = [30,11,23,4,20], h = 5`
**Output:** `30`
**Explanation:** Minimum speed to finish in exactly 5 hours is 30 (one pile per hour)

### Example 3
**Input:** `piles = [30,11,23,4,20], h = 6`
**Output:** `23`
**Explanation:** With k=23, can finish in 6 hours

### Example 4
**Input:** `piles = [1,1,1,1], h = 4`
**Output:** `1`
**Explanation:** Minimum possible speed

---

## Optimal Solution

### Implementation

```python
def minEatingSpeed(piles: List[int], h: int) -> int:
    """
    Find minimum eating speed using binary search.

    Time: O(n log m) where m is max(piles)
    Space: O(1)
    """
    def can_finish(speed):
        """Check if Koko can finish all bananas at given speed"""
        hours_needed = 0

        for pile in piles:
            # Ceiling division: (pile + speed - 1) // speed
            hours_needed += (pile + speed - 1) // speed

            # Early termination if exceeds h
            if hours_needed > h:
                return False

        return hours_needed <= h

    # Binary search on eating speed
    # Minimum speed: 1, Maximum speed: max pile size
    left, right = 1, max(piles)

    while left < right:
        mid = left + (right - left) // 2

        if can_finish(mid):
            # Can finish with mid speed, try slower
            right = mid
        else:
            # Too slow, need faster speed
            left = mid + 1

    return left
```

### Alternative Implementation with Math.ceil

```python
import math

def minEatingSpeed(piles: List[int], h: int) -> int:
    """
    Binary search with explicit ceiling division.

    Time: O(n log m), Space: O(1)
    """
    def hours_to_eat(speed):
        """Calculate total hours needed at given speed"""
        return sum(math.ceil(pile / speed) for pile in piles)

    left, right = 1, max(piles)

    while left < right:
        mid = (left + right) // 2

        if hours_to_eat(mid) <= h:
            # Can finish in time, try slower speed
            right = mid
        else:
            # Too slow, need faster speed
            left = mid + 1

    return left
```

### Complexity Analysis

**Time: O(n log m) - binary search O(log m) with O(n) validation. Space: O(1) - constant space**

**Why This is Optimal:**
- Binary search on answer pattern (minimize maximum / maximize minimum)
- Search space is bounded by [1, max(piles)]
- Validation function is monotonic: if speed k works, all speeds > k work
- Logarithmic search reduces linear O(m*n) to O(n log m)
- No need to try every possible speed

---

## Categories & Tags

**Primary Topics:** Array, Binary Search

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/koko-eating-bananas)*
