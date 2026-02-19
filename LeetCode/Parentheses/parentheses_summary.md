# Parentheses Problems - Comprehensive Analysis




## 📋 Problems in This Category

- [001. Minimum Remove to Make Valid Parentheses](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Parentheses/001_minimum_remove_to_make_valid_parentheses.md) - `Stack+Indices`
- [020. Valid Parentheses](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Parentheses/020_valid_parentheses.md) - `Stack+Matching`
- [052. Minimum Add to Make Parentheses Valid](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Parentheses/052_minimum_add_to_make_parentheses_valid.md) - `Greedy Count`
- [056. Remove Invalid Parentheses](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Parentheses/056_remove_invalid_parentheses.md) - `BFS+Removal`

---

## 🎯 Category Overview

**Total Problems:** 4
**Difficulty Range:** Easy → Medium → Hard
**Core Concept:** Stack-based tracking with evolving requirements

---

## 📊 Problem Progression Map

```
Level 1 (Easiest): Valid Parentheses (#020)
    ↓ Add: Return boolean → Now count needed additions
Level 2: Minimum Add to Make Valid (#052)
    ↓ Add: Count → Now actually build valid string by removing
Level 3: Minimum Remove to Make Valid (#001)
    ↓ Add: Single answer → Now find ALL possible answers
Level 4 (Hardest): Remove Invalid Parentheses (#056)
```

---

## 🔍 Problem-by-Problem Analysis

### 1️⃣ **Problem #020: Valid Parentheses** (EASY)

**🎯 Task:** Check if parentheses string is valid
**📥 Input:** String with only `()[]{}` characters
**📤 Output:** Boolean (true/false)
**🏷️ Tag:** Stack+Matching

#### Core Challenge
- Validate nesting and matching of different bracket types
- No modifications allowed—just check validity

#### Algorithm
```python
Stack approach:
1. Push opening brackets onto stack
2. For closing bracket, pop and check if matches
3. Valid if stack empty at end
```

#### Key Insight
> **Foundation Pattern**: This is the BASE algorithm for all parentheses problems. Master this first!

#### Complexity
- **Time:** O(n) - single pass
- **Space:** O(n) - stack storage
- **Why Simplest:** Only validation, no construction or counting

---

### 2️⃣ **Problem #052: Minimum Add to Make Valid** (MEDIUM)

**🎯 Task:** Count minimum additions needed to make valid
**📥 Input:** String with only `()` characters
**📤 Output:** Integer count
**🏷️ Tag:** Greedy Count

#### What Changed from #020?
```diff
+ Now we COUNT what's needed (not just validate)
+ Can be solved WITHOUT stack (optimization!)
+ Only handles one bracket type (simpler)
- Must track both unmatched '(' and ')'
```

#### Algorithm Evolution
```python
Counter approach (OPTIMAL):
1. open_needed = 0   # Count of unmatched ')'
2. close_needed = 0  # Count of unmatched '('
3. For each '(': increment close_needed
4. For each ')':
   - If close_needed > 0: decrement (matched!)
   - Else: increment open_needed (unmatched)
5. Return open_needed + close_needed
```

#### Can We Reuse #020's Algorithm?
**YES, but suboptimal:**
- #020 uses stack: O(n) space
- We can optimize to O(1) space using counters
- **Learning:** When you only need COUNT, use counters instead of stack

#### Key Insight
> **Space Optimization**: Stack → Counters
> When you don't need to track actual items, just count them!

#### Complexity
- **Time:** O(n) - single pass
- **Space:** O(1) - only two integers (vs O(n) for stack)
- **Why Harder than #020:** Requires understanding of what "minimum" means

---

### 3️⃣ **Problem #001: Minimum Remove to Make Valid** (MEDIUM)

**🎯 Task:** Remove minimum parentheses to make valid, return the string
**📥 Input:** String with `()` AND letters
**📤 Output:** Valid string
**🏷️ Tag:** Stack+Indices

#### What Changed from #052?
```diff
+ Must CONSTRUCT valid string (not just count)
+ String has LETTERS (must preserve them)
+ Must track WHICH parentheses to remove
- Need to remember positions (indices)
```

#### Algorithm Evolution
```python
Stack with indices approach:
1. to_remove = set()      # Track indices to remove
2. stack = []             # Track '(' indices
3. For each character at index i:
   - If '(': push index i onto stack
   - If ')':
      * If stack not empty: pop (matched!)
      * Else: add i to to_remove (unmatched ')')
4. Add remaining stack indices to to_remove (unmatched '(')
5. Build result: skip indices in to_remove
```

#### Can We Reuse #052's Algorithm?
**NO—counters aren't enough:**
- #052 only counted, here we need POSITIONS
- Must track WHERE to remove, not just how many
- **Learning:** When building output, need to track indices

#### Visual Example
```
Input:  "lee(t(c)o)de)"
Indices: 0123456789...

Stack tracking:
- i=3: '(' → stack=[3]
- i=5: '(' → stack=[3,5]
- i=7: ')' → pop(5), stack=[3]
- i=9: ')' → pop(3), stack=[]
- i=12: ')' → stack empty, add to_remove={12}

Result: Remove index 12 → "lee(t(c)o)de"
```

#### Key Insight
> **Index Tracking**: Need stack to remember POSITIONS, not just counts
> Use SET for O(1) lookup when building result

#### Complexity
- **Time:** O(n) - two passes (find + build)
- **Space:** O(n) - stack + set
- **Why Harder than #052:** Must construct actual output string

---

### 4️⃣ **Problem #056: Remove Invalid Parentheses** (HARD)

**🎯 Task:** Find ALL valid strings with minimum removals
**📥 Input:** String with `()` and letters
**📤 Output:** List of ALL valid strings
**🏷️ Tag:** BFS+Removal

#### What Changed from #001?
```diff
+ Find ALL possible solutions (not just one)
+ Must ensure MINIMUM removals across all
+ Explore multiple removal paths
- Exponential possibilities (2^n)
```

#### Algorithm Evolution
```python
BFS approach (Level-by-level exploration):
1. Start with original string in queue
2. For each level:
   - Check if current string is valid
   - If valid, add to results
   - If found any valid, STOP going deeper
3. Generate next level:
   - Try removing each '(' or ')' one at a time
   - Add to queue if not visited
4. Return all results
```

#### Why NOT Reuse #001's Algorithm?
**#001 gives ONE answer, we need ALL:**
- #001: Stack gives deterministic single result
- #056: Must explore ALL removal combinations
- **Learning:** Need graph search (BFS/DFS) for multiple solutions

#### Visual Example
```
Input: "()())()"

Level 0: "()())()"
         ↓ Remove one '('
Level 1: ")())()", "(())()", "())()", "()()(", ...
         ↓ Remove another '(' or ')'
Level 2: Multiple strings...
         ↓ Check validity
Valid at Level 1: "(())()", "()()()" ← STOP HERE (minimum removals)
```

#### Two Approaches

**Approach 1: BFS (Recommended)**
```python
Pros:
- Naturally finds minimum removal level
- Stop when first valid strings found
- Easy to understand

Cons:
- O(2^n) space for queue
```

**Approach 2: DFS with Pruning**
```python
Pros:
- O(n) space for recursion stack
- Can prune duplicates early

Cons:
- Must pre-calculate minimum removals
- More complex implementation
```

#### Key Insight
> **Search Space Explosion**: From single path → ALL paths
> BFS ensures minimum removals by level-order exploration

#### Complexity
- **Time:** O(2^n) - worst case try all subsets
- **Space:** O(2^n) - queue and visited set
- **Why Hardest:** Exponential search space, must find ALL solutions

---

## 🔄 Algorithm Relationships

### Can We Modify Previous Solutions?

| From → To | Can Modify? | What Changes? |
|-----------|-------------|---------------|
| #020 → #052 | ✅ YES | Replace stack with counters (optimization) |
| #052 → #001 | ❌ NO | Need indices, counters insufficient |
| #020 → #001 | ✅ YES | Add index tracking to stack approach |
| #001 → #056 | ❌ NO | Need BFS/DFS for multiple solutions |

### Core Algorithm Evolution

```
#020: Stack (boolean check)
        ↓
#052: Counters (count optimization)
        ↓ (back to stack for positions)
#001: Stack + Indices (single construction)
        ↓
#056: BFS/DFS (multiple solutions)
```

---

## 💡 Key Learning Insights

### 1. **Stack vs Counters Trade-off**
```
Use Stack when: Need positions/order
Use Counters when: Only need quantities
```

### 2. **Single vs Multiple Solutions**
```
Single solution: Stack/Greedy (deterministic)
Multiple solutions: BFS/DFS (exploration)
```

### 3. **Validation vs Construction**
```
Validation: Can optimize space
Construction: Must track indices
```

### 4. **Space Complexity Progression**
```
#020: O(n) - stack
#052: O(1) - optimized counters ⭐ Best space
#001: O(n) - stack + set
#056: O(2^n) - must track all paths
```

---

## 🎨 Visual Comparison Table

| Problem | Input Type | Output Type | Key Structure | Space | Difficulty Factor |
|---------|------------|-------------|---------------|-------|-------------------|
| #020 | Only `()[]{}` | Boolean | Stack | O(n) | Matching logic |
| #052 | Only `()` | Count | Counters | O(1) | Understanding "minimum" |
| #001 | `()` + letters | String | Stack + Indices | O(n) | Index tracking |
| #056 | `()` + letters | String[] | BFS/DFS | O(2^n) | Search explosion |

---

## 🚀 Recommended Study Order

1. **Start:** #020 (Valid Parentheses)
   - Master the basic stack pattern
   - Understand matching mechanism

2. **Then:** #052 (Minimum Add)
   - Learn space optimization technique
   - Understand counting vs tracking

3. **Next:** #001 (Minimum Remove)
   - Apply stack with index tracking
   - Practice string construction

4. **Finally:** #056 (Remove Invalid)
   - Learn BFS/DFS search patterns
   - Handle multiple solutions

---

## 🎯 Interview Tips

### Common Mistakes
1. **#020:** Forgetting to check empty stack on closing bracket
2. **#052:** Using O(n) space when O(1) possible
3. **#001:** Forgetting to handle letters in string
4. **#056:** Not ensuring MINIMUM removals (going too deep in search)

### Optimization Opportunities
```python
# #052: Can reduce space from O(n) to O(1)
Stack approach → Counter approach

# #056: Can prune duplicate paths
Use visited set to avoid reprocessing
Skip consecutive duplicate characters
```

### Time Limit Considerations
- #020, #052, #001: O(n) solutions exist ✅
- #056: O(2^n) is unavoidable, but pruning helps

---

## 🧩 Pattern Recognition

### When to Use Each Approach

**Stack (with matching):**
- Multiple bracket types
- Need to validate nesting
- Example: #020

**Counters (greedy):**
- Only counting needed
- Single bracket type
- Example: #052

**Stack + Indices:**
- Must construct output
- Need specific positions
- Example: #001

**BFS/DFS:**
- Multiple solutions required
- Minimum at specific level
- Example: #056

---

## 📝 Practice Progression

```
Week 1: Master #020
- Implement 3 times from scratch
- Test with edge cases
- Understand WHY stack works

Week 2: Solve #052
- First use stack (like #020)
- Then optimize to counters
- Compare both approaches

Week 3: Tackle #001
- Build on #020's stack concept
- Add index tracking
- Practice string building

Week 4: Challenge #056
- Implement BFS version
- Try DFS with pruning
- Analyze time/space trade-offs
```

---

## 🎓 Conceptual Evolution

### Problem Complexity Factors

1. **Input Complexity:** Pure brackets → Brackets + letters
2. **Output Complexity:** Boolean → Count → Single string → Multiple strings
3. **Algorithm Complexity:** Stack → Counters → Stack+Indices → Search
4. **Space Complexity:** O(1) → O(n) → O(2^n)

### The Meta-Pattern
```
Simple validation
    ↓
Quantification (how many?)
    ↓
Construction (build one)
    ↓
Exhaustive search (find all)
```

This progression appears in many problem categories, not just parentheses!

---

## 🔗 Related Problem Patterns

These parentheses patterns appear in:
- Expression validation
- Nested structure parsing
- Balancing problems
- Graph traversal (for multiple solutions)
- String manipulation with constraints

---

**Summary:** Start with validation (#020), learn optimization (#052), practice construction (#001), master search (#056). Each problem builds on previous concepts while introducing new challenges. Focus on understanding WHY each approach is chosen, not just memorizing solutions.
