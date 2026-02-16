# 049. Exclusive Time of Functions

**Difficulty:** MEDIUM
**Frequency:** 56.0%
**Acceptance Rate:** 64.8%
**LeetCode Link:** [Exclusive Time of Functions](https://leetcode.com/problems/exclusive-time-of-functions)

---

## Problem Description

On a single-threaded CPU, we execute a program containing `n` functions. Each function has a unique ID between `0` and `n-1`.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list `logs`, where `logs[i]` represents the ith log message formatted as a string `"{function_id}:{"start" | "end"}:{timestamp}"`. For example, `"0:start:3"` means a function call with function ID `0` started at the beginning of timestamp `3`, and `"1:end:2"` means a function call with function ID `1` ended at the end of timestamp `2`. Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for `2` time units and another call executing for `1` time unit, the exclusive time is `2 + 1 = 3`.

Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID `i`.

**Constraints:**
- 1 <= n <= 100
- 1 <= logs.length <= 500
- 0 <= function_id < n
- 0 <= timestamp <= 10^9
- No two start events will happen at the same timestamp
- No two end events will happen at the same timestamp
- Each function has an "end" log for each "start" log

---

## Examples

### Example 1
**Input:** `n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]`
**Output:** `[3,4]`
**Explanation:**
- Function 0 starts at timestamp 0, executes from 0-1 (2 units)
- Function 1 starts at 2, executes from 2-5 (4 units)
- Function 0 resumes at 6, executes from 6-6 (1 unit)
- Total: Function 0 = 2 + 1 = 3, Function 1 = 4

### Example 2
**Input:** `n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]`
**Output:** `[8]`
**Explanation:**
- Function 0 is called recursively
- Total execution time: 8 units

### Example 3
**Input:** `n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]`
**Output:** `[7,1]`
**Explanation:**
- Function 0: executes at 0-1, 2-5, 7-7 = 2 + 4 + 1 = 7 units
- Function 1: executes at 6-6 = 1 unit

---

## Optimal Solution

### Implementation

```python
def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    """
    Calculate exclusive execution time using stack to track call hierarchy.

    Time: O(m) where m is number of logs, Space: O(n) for stack
    """
    result = [0] * n
    stack = []  # Stack to track (function_id, start_time)
    prev_time = 0

    for log in logs:
        func_id, action, timestamp = log.split(':')
        func_id = int(func_id)
        timestamp = int(timestamp)

        if action == "start":
            # If there's a function running, add its execution time
            if stack:
                result[stack[-1]] += timestamp - prev_time

            # Push current function to stack
            stack.append(func_id)
            prev_time = timestamp
        else:  # action == "end"
            # Add execution time for ending function (inclusive of end time)
            result[stack[-1]] += timestamp - prev_time + 1

            # Pop the function from stack
            stack.pop()

            # Update prev_time to after the ended function
            prev_time = timestamp + 1

    return result
```

### Alternative Implementation with Clearer State

```python
def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    """
    Alternative with explicit time tracking.

    Time: O(m), Space: O(n)
    """
    result = [0] * n
    stack = []

    for log in logs:
        parts = log.split(':')
        func_id = int(parts[0])
        action = parts[1]
        timestamp = int(parts[2])

        if action == "start":
            if stack:
                # Current function is paused
                prev_id, prev_start = stack[-1]
                result[prev_id] += timestamp - prev_start

            stack.append([func_id, timestamp])
        else:  # end
            curr_id, curr_start = stack.pop()
            result[curr_id] += timestamp - curr_start + 1

            if stack:
                # Resume previous function at timestamp + 1
                stack[-1][1] = timestamp + 1

    return result
```

### Complexity Analysis

**Time: O(m) - single pass through logs. Space: O(n) - stack depth at most n functions**

**Why This is Optimal:**
- Must process each log entry, so O(m) is optimal
- Stack naturally models the call hierarchy
- Key insight: "end" timestamp is inclusive, "start" is the beginning
- Tracks execution time incrementally as functions pause/resume

---

## Categories & Tags

**Primary Topics:** Array, Stack

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/exclusive-time-of-functions)*
