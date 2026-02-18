# 071. Managers with at Least 5 Direct Reports

**Difficulty:** MEDIUM
**Frequency:** 40.7%
**Acceptance Rate:** 48.9%
**LeetCode Link:** [Managers with at Least 5 Direct Reports](https://leetcode.com/problems/managers-with-at-least-5-direct-reports)

---

## Problem Description

SQL Schema:
```sql
Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
```

Write an SQL query to find managers with at least five direct reports.

Return the result table in any order.

**Constraints:**
- Each row indicates id, name, department, and manager's id
- If managerId is null, employee has no manager
- No employee will be their own manager

---

## Examples

### Example 1
**Input:** `Employee table:\n+-----+-------+------------+-----------+\n| id  | name  | department | managerId |\n+-----+-------+------------+-----------+\n| 101 | John  | A          | None      |\n| 102 | Dan   | A          | 101       |\n| 103 | James | A          | 101       |\n| 104 | Amy   | A          | 101       |\n| 105 | Anne  | A          | 101       |\n| 106 | Ron   | B          | 101       |`
**Output:** `+------+\n| name |\n+------+\n| John |\n+------+`
**Explanation:** John has 5 direct reports

### Example 2
**Input:** `3 managers with 4, 5, and 6 reports respectively`
**Output:** `Managers with 5 and 6 reports`
**Explanation:** Only those with >= 5 reports

### Example 3
**Input:** `All employees report to same manager`
**Output:** `That single manager`
**Explanation:** Flat organization structure

---

## Optimal Solution

### Implementation

```python
SELECT e1.name
FROM Employee e1
JOIN Employee e2 ON e1.id = e2.managerId
GROUP BY e1.id, e1.name
HAVING COUNT(e2.id) >= 5;

-- Alternative using subquery:
SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM Employee
    WHERE managerId IS NOT NULL
    GROUP BY managerId
    HAVING COUNT(*) >= 5
);
```

### Complexity Analysis

**Time: O(n²) worst case for join. Space: O(n) - grouping**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity for this problem class
- Minimal space overhead while maintaining code clarity
- Scales efficiently with large inputs
- Handles all edge cases correctly

---

## Categories & Tags

**Primary Topics:** Database

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/managers-with-at-least-5-direct-reports)*
