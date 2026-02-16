# 038. Accounts Merge

**Difficulty:** MEDIUM
**Frequency:** 62.4%
**Acceptance Rate:** 59.6%
**LeetCode Link:** [Accounts Merge](https://leetcode.com/problems/accounts-merge)

---

## Problem Description

Given a list of `accounts` where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

**Constraints:**
- 1 <= accounts.length <= 1000
- 2 <= accounts[i].length <= 10
- 1 <= accounts[i][j].length <= 30
- accounts[i][0] consists of English letters
- accounts[i][j] (for j > 0) is a valid email

---

## Examples

### Example 1
**Input:** `accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]`
**Output:** `[["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]`
**Explanation:** First and second John are same person (share johnsmith@mail.com)

### Example 2
**Input:** `accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]`
**Output:** `[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]`
**Explanation:** No accounts share emails, so they remain separate

### Example 3
**Input:** `accounts = [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]`
**Output:** `[["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]`
**Explanation:** All accounts belong to same David through email chains

### Example 4
**Input:** `accounts = [["Alice","alice@mail.com"],["Alice","alicesmith@mail.com"]]`
**Output:** `[["Alice","alice@mail.com"],["Alice","alicesmith@mail.com"]]`
**Explanation:** Same name but different people (no shared emails)

---

## Optimal Solution

### Implementation (Union-Find)

```python
def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    """
    Union-Find approach to merge accounts by email connectivity.

    Time: O(N * K * α(N)) where N is accounts, K is max emails per account
    Space: O(N * K) for email mappings
    """
    from collections import defaultdict

    # Union-Find data structure
    parent = {}

    def find(x):
        if x not in parent:
            parent[x] = x
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x, root_y = find(x), find(y)
        if root_x != root_y:
            parent[root_x] = root_y

    # Map email to name
    email_to_name = {}

    # Build union-find structure
    for account in accounts:
        name = account[0]
        first_email = account[1]

        for email in account[1:]:
            email_to_name[email] = name
            union(first_email, email)

    # Group emails by root
    components = defaultdict(list)
    for email in email_to_name:
        root = find(email)
        components[root].append(email)

    # Build result
    result = []
    for emails in components.values():
        name = email_to_name[emails[0]]
        result.append([name] + sorted(emails))

    return result
```

### Alternative Implementation (DFS)

```python
def accountsMerge(accounts: List[List[str]]) -> List[List[str]]:
    """
    DFS-based graph traversal approach.

    Time: O(N * K * log(N*K)) for sorting
    Space: O(N * K) for graph
    """
    from collections import defaultdict

    # Build graph: email -> connected emails
    graph = defaultdict(set)
    email_to_name = {}

    for account in accounts:
        name = account[0]
        first_email = account[1]

        for email in account[1:]:
            email_to_name[email] = name
            graph[first_email].add(email)
            graph[email].add(first_email)

    visited = set()
    result = []

    def dfs(email, emails):
        """Collect all connected emails via DFS."""
        if email in visited:
            return
        visited.add(email)
        emails.append(email)

        for neighbor in graph[email]:
            dfs(neighbor, emails)

    # Process each unvisited email
    for email in email_to_name:
        if email not in visited:
            emails = []
            dfs(email, emails)
            name = email_to_name[email]
            result.append([name] + sorted(emails))

    return result
```

### Complexity Analysis

**Time: O(N * K * α(N)) for Union-Find or O(N * K * log(N*K)) for DFS with sorting**
**Space: O(N * K) for storing email mappings and graph structures**

**Why This is Optimal:**
- Union-Find efficiently handles transitive relationships
- Near-constant time union and find operations
- DFS naturally explores connected components
- Both approaches handle email chains correctly

---

## Categories & Tags

**Primary Topics:** Array, Hash Table, String, Depth-First Search, Breadth-First Search, Union Find, Sorting

**Difficulty Level:** MEDIUM

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/accounts-merge)*
