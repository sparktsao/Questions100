# 077. Car Pooling

**Difficulty:** MEDIUM
**Frequency:** 40.7%
**Acceptance Rate:** 56.0%
**LeetCode Link:** [Car Pooling](https://leetcode.com/problems/car-pooling)

---

## Problem Description

There is a car with `capacity` empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer `capacity` and an array `trips` where `trips[i] = [numPassengers_i, from_i, to_i]` indicates that the `i-th` trip has `numPassengers_i` passengers and the locations to pick them up and drop them off are `from_i` and `to_i` respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return `true` if it is possible to pick up and drop off all passengers for all the given trips, or `false` otherwise.

**Constraints:**
- `1 <= trips.length <= 1000`
- `trips[i].length == 3`
- `1 <= numPassengers_i <= 100`
- `0 <= from_i < to_i <= 1000`
- `1 <= capacity <= 10^5`

---

## Examples

### Example 1
**Input:** `trips = [[2,1,5],[3,3,7]], capacity = 4`
**Output:** `false`
**Explanation:** At location 3, we have 2+3=5 passengers, which exceeds capacity of 4.

### Example 2
**Input:** `trips = [[2,1,5],[3,3,7]], capacity = 5`
**Output:** `true`
**Explanation:** At location 3, we have 5 passengers (exactly at capacity). At location 5, 2 passengers drop off, leaving 3 passengers until location 7.

### Example 3
**Input:** `trips = [[2,1,5],[3,5,7]], capacity = 3`
**Output:** `true`
**Explanation:** At location 1, pick up 2 passengers. At location 5, drop off 2 and pick up 3 (current = 3). At location 7, drop off 3.

### Example 4
**Input:** `trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11`
**Output:** `true`
**Explanation:** Maximum concurrent passengers is 11 (at location 3-7 and location 7-9).

---

## Optimal Solution

### Implementation (Difference Array Approach)

```python
def carPooling(trips: List[List[int]], capacity: int) -> bool:
    """
    Difference array approach to track passenger changes.

    Time: O(n + m), Space: O(m)
    where n is number of trips, m is max location (1000)
    """
    # Track passenger changes at each location
    passenger_changes = [0] * 1001

    for num_passengers, start, end in trips:
        passenger_changes[start] += num_passengers
        passenger_changes[end] -= num_passengers

    # Check if capacity is ever exceeded
    current_passengers = 0
    for change in passenger_changes:
        current_passengers += change
        if current_passengers > capacity:
            return False

    return True
```

### Alternative Implementation (Sorting Approach)

```python
def carPooling(trips: List[List[int]], capacity: int) -> bool:
    """
    Sorting approach tracking pickup/dropoff events.

    Time: O(n log n), Space: O(n)
    """
    changes = []

    for p, t1, t2 in trips:
        changes.append((t1, p))    # pickup:  positive
        changes.append((t2, -p))   # dropoff: negative

    # Sort by location first, then by change value.
    # At the same location, negative (dropoff) sorts before positive (pickup) —
    # passengers exit before new ones board, preventing false overflow.
    changes.sort(key=lambda x: (x[0], x[1]))

    current_passengers = 0
    for t, p in changes:
        current_passengers += p
        if current_passengers > capacity:
            return False

    return True
```

**Why the secondary sort key (`x[1]`) matters:**

Consider `trips = [[3,5,7],[2,5,9]], capacity = 3` with a dropoff and pickup both at location 5:

| Sort order at loc 5 | Sequence | Peak seen |
|---|---|---|
| Dropoff first `(5,-3)` then pickup `(5,+2)` | 3 → 0 → 2 | 3 ✓ (within capacity) |
| Pickup first `(5,+2)` then dropoff `(5,-3)` | 3 → 5 → 2 | 5 ✗ (false overflow) |

Without the secondary key, Python's default tuple sort on `(loc, change)` already puts negatives first — but making it explicit avoids subtle bugs if the tuple structure ever changes.

### Complexity Analysis

**Difference Array: Time: O(n + m) - where m is fixed at 1000. Space: O(m) - fixed size array**

**Sorting: Time: O(n log n) - sorting events. Space: O(n) - event storage**

**Why Difference Array is Optimal:**
- O(n) time when m is bounded (1000 locations)
- Avoids sorting overhead
- Simple prefix sum computation
- Fixed space regardless of number of trips
- Better for problems with bounded coordinate range

**Why Sorting Can Be Better:**
- When location range is very large (m >> n log n)
- More intuitive event-based simulation
- Only processes actual events, not empty locations
- Generalizes better to unbounded coordinates

---

## Categories & Tags

**Primary Topics:** Array, Sorting, Heap (Priority Queue), Simulation, Prefix Sum

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/car-pooling)*
