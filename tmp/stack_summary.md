# Stack - Comprehensive Mastery Guide

## 📋 Problems in This Category

- [008. Basic Calculator II](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Stack/008_basic_calculator_ii.md) - `Stack+Operator`
- [035. Simplify Path](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Stack/035_simplify_path.md) - `Stack+Path`
- [049. Exclusive Time of Functions](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Stack/049_exclusive_time_of_functions.md) - `Stack+Time`
- [093. Decode String](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Stack/093_decode_string.md) - `Stack+Nested`
- [098. Remove Adjacent Duplicates II](https://github.com/sparktsao/Questions100/blob/main/LeetCode/Stack/098_remove_all_adjacent_duplicates_in_string_ii.md) - `Stack+Count`

---

## 🎯 Overview

**Total Problems:** 5
**Difficulty:** Easy (0) • Medium (5) • Hard (0)

**Core Concept:**
Stack (Last-In-First-Out/LIFO) is the go-to structure for problems requiring **temporal ordering**, **nested scope management**, **deferred processing**, and **backtracking**. Think of it as managing "what you saw most recently matters most."

**Key Insight:**
Use stack when:
1. **Recent context matters more** than older context (nested structures)
2. **You need to reverse or undo** operations
3. **Inner elements must be processed before outer** elements (recursion simulation)
4. **Matching pairs or boundaries** need tracking
5. **State must be saved and restored** (DFS, parsing)

---

## 🔄 Stack vs Other Data Structures: When to Use What

### Stack vs Queue (LIFO vs FIFO)

**Stack (LIFO - Last In First Out):**
- **When to use:** Recent items need priority, nested structures, backtracking
- **Mental model:** Stack of plates - take from top (most recent)
- **Access pattern:** Only top element accessible
- **Example:** Undo functionality, recursive parsing, expression evaluation

**Queue (FIFO - First In First Out):**
- **When to use:** Order matters, processing in arrival sequence, BFS traversal
- **Mental model:** Line at a store - first person served first
- **Access pattern:** Front and back accessible
- **Example:** Task scheduling, BFS level-order traversal, request processing

```python
# Stack example: Matching parentheses (recent opener matches)
stack = []
for char in "((()))":
    if char == '(':
        stack.append(char)  # Push recent opener
    else:
        stack.pop()  # Match with MOST RECENT opener

# Queue example: BFS level traversal (process nodes in order discovered)
from collections import deque
queue = deque([root])
while queue:
    node = queue.popleft()  # Process OLDEST discovered node
    queue.extend(node.children)
```

**Key Difference:** Stack prioritizes **recency** (nested context), Queue prioritizes **order** (fairness).

---

### Stack vs Two Pointers

**Stack (State History):**
- **When to use:** Need to remember multiple states, can't determine answer in single pass
- **Space:** O(n) - stores intermediate states
- **Traversal:** Single pass, forward only
- **Characteristic:** Can look back at ALL previous decisions, handle nesting

**Two Pointers (Direct Comparison):**
- **When to use:** Can make decisions by comparing current positions, sorted/monotonic data
- **Space:** O(1) - no extra storage needed
- **Traversal:** Can move bidirectionally or same direction
- **Characteristic:** Only sees two positions at a time, no memory of past

```python
# Stack: Remove adjacent duplicates (need history of all chars)
def removeDuplicates(s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # Need to remember previous char
        else:
            stack.append(char)
    return ''.join(stack)
# "abbaca" -> "ca" (need stack to track b removal, then a removal)

# Two Pointers: Remove duplicates from sorted array (direct comparison)
def removeDuplicates(nums: List[int]) -> int:
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]
    return slow + 1
# [1,1,2,2,3] -> [1,2,3] (only need current comparison)
```

**When Stack beats Two Pointers:**
- Adjacent elements can eliminate each other (cascading removals)
- Nested structures (parentheses matching)
- Order of operations matters (calculators)

**When Two Pointers beats Stack:**
- Sorted/monotonic input where you compare positions
- Palindrome checking, container problems
- When you don't need to "remember" intermediate states

---

### Stack vs Sliding Window

**Stack (Variable Window, History-Based):**
- **When to use:** Window size depends on content, need to track opening/closing boundaries
- **Window:** Variable size determined by nested structure depth
- **State:** Tracks all elements in current nested scope
- **Example:** Matching parentheses, decode nested strings

**Sliding Window (Fixed/Flexible Window, Range-Based):**
- **When to use:** Continuous subarray/substring problems, optimization over ranges
- **Window:** Fixed size or expands/contracts based on constraint
- **State:** Tracks aggregated info (count, sum) not individual elements
- **Example:** Max sum subarray, longest substring without repeats

```python
# Stack: Decode nested string (variable depth nesting)
def decodeString(s: str) -> str:
    stack = []
    for char in s:
        if char != ']':
            stack.append(char)  # Track ALL nested contexts
        else:
            # Pop until matching '['
            substr = ''
            while stack[-1] != '[':
                substr = stack.pop() + substr
            stack.pop()  # Remove '['
            # ... build result
# "3[a2[c]]" needs stack to track nested 2[c] inside 3[...]

# Sliding Window: Longest substring without repeats (range optimization)
def lengthOfLongestSubstring(s: str) -> int:
    seen = {}
    left = max_len = 0
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1  # Shrink window
        seen[char] = right
        max_len = max(max_len, right - left + 1)
    return max_len
# "abcabcbb" -> track window [left, right], no need for full history
```

**Key Difference:**
- **Stack:** "What nested scope am I in?" (depth-first, hierarchical)
- **Sliding Window:** "What's the best continuous range?" (breadth, linear optimization)

---

### Stack vs Array/HashMap State Management

**Stack (Temporal Order Matters):**
- **When:** Order of insertion determines processing order
- **Access:** Only most recent (top) accessible
- **Use case:** Undo/redo, parsing, recursion simulation

**Array (Random Access Needed):**
- **When:** Need to access any position, build result incrementally
- **Access:** Any index accessible O(1)
- **Use case:** Result building, lookups, sorting

**HashMap (Lookup Speed Priority):**
- **When:** Need fast existence checks or value retrieval by key
- **Access:** Any key accessible O(1)
- **Use case:** Frequency counting, memoization, deduplication

```python
# Stack: Calculator (operator precedence = temporal ordering)
def calculate(s: str) -> int:
    stack = []
    num = 0
    operator = '+'
    for char in s + '+':  # Process in order
        if char.isdigit():
            num = num * 10 + int(char)
        elif char in '+-*/':
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop() * num)
            elif operator == '/':
                stack.append(int(stack.pop() / num))
            operator = char
            num = 0
    return sum(stack)
# "3+2*2" -> stack tracks [3, 4] because * processes before +

# HashMap: Two Sum (need fast lookup, order doesn't matter)
def twoSum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i
# [2,7,11,15], target=9 -> {2:0, 7:1} lookup is O(1)
```

**Stack wins when:**
- Most recent elements dictate next action
- Need to "unwind" or backtrack
- Operator precedence or nested scopes exist

**Array/HashMap wins when:**
- Need random access or fast lookups
- Order doesn't affect correctness
- Building result that needs indexing

---

## 🧠 Deep Dive: How Stack Actually Works

### LIFO Mechanics

```python
stack = []

# Push O(1)
stack.append('A')  # ['A']
stack.append('B')  # ['A', 'B']
stack.append('C')  # ['A', 'B', 'C']
                   #   ↑    ↑    ↑
                   # old  middle top (most recent)

# Peek O(1) - look without removing
top = stack[-1]    # 'C' (most recent)

# Pop O(1) - remove most recent
stack.pop()        # Returns 'C', stack = ['A', 'B']
stack.pop()        # Returns 'B', stack = ['A']
stack.pop()        # Returns 'A', stack = []
```

### Why LIFO is Powerful

**1. Reverses Order Naturally**
```python
# Input: "hello"
# Stack after pushing: ['h', 'e', 'l', 'l', 'o']
# Popping order: 'o', 'l', 'l', 'e', 'h' = "olleh"
```

**2. Manages Nested Scopes**
```python
# Expression: "3 * (2 + (5 - 1))"
# Stack tracks nested context:
# Push '(' -> stack = ['(']
# Push '(' -> stack = ['(', '(']  # Nested deeper
# Hit ')' -> pop until '(' -> process inner (5-1)
# Hit ')' -> pop until '(' -> process middle (2+4)
# Process outer 3*6
```

**3. Deferred Processing**
```python
# Calculator: "3 + 2 * 2"
# Can't compute 3 + ? until we see what comes after 2
# Push 3, see *, realize 2*2 must be computed first
# Stack defers 3 until 2*2 = 4 is ready, then 3+4
```

---

## 📚 Sub-Patterns & Techniques

### Pattern 1: Matching Pairs (Parentheses, Brackets)

**Concept:** Track opening symbols, match with most recent when closing appears

```python
def isValid(s: str) -> bool:
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:  # Opening bracket
            stack.append(char)
        else:  # Closing bracket
            if not stack or pairs[stack[-1]] != char:
                return False
            stack.pop()

    return len(stack) == 0
```

**Why Stack:** Need to match closest opening bracket (recency matters)
**Time:** O(n), **Space:** O(n)

---

### Pattern 2: Expression Evaluation (Calculator, Postfix)

**Concept:** Process operators based on precedence, defer lower-precedence operations

```python
def calculate(s: str) -> int:
    stack = []
    num, operator = 0, '+'

    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)

        if char in '+-*/' or i == len(s) - 1:
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop() * num)
            elif operator == '/':
                stack.append(int(stack.pop() / num))
            operator = char
            num = 0

    return sum(stack)
```

**Why Stack:** Higher precedence (* /) must process before lower (+ -)
**Time:** O(n), **Space:** O(n)

---

### Pattern 3: Monotonic Stack (Next Greater Element)

**Concept:** Maintain stack in increasing/decreasing order to find next greater/smaller

```python
def nextGreaterElements(nums: List[int]) -> List[int]:
    n = len(nums)
    result = [-1] * n
    stack = []  # Stack stores indices

    for i in range(2 * n):  # Circular array
        while stack and nums[stack[-1]] < nums[i % n]:
            result[stack.pop()] = nums[i % n]
        if i < n:
            stack.append(i)

    return result
```

**Why Stack:** Track "pending" elements waiting for greater element
**Time:** O(n), **Space:** O(n)

---

### Pattern 4: DFS Simulation with Explicit Stack

**Concept:** Replace recursive calls with manual stack (avoid recursion depth limit)

```python
def dfsIterative(graph, start):
    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()  # Most recently added (DFS)
        if node in visited:
            continue

        visited.add(node)
        # Process node

        for neighbor in graph[node]:
            if neighbor not in visited:
                stack.append(neighbor)
```

**Why Stack:** DFS explores deeply before backtracking (LIFO mimics recursion)
**Time:** O(V + E), **Space:** O(V)

---

### Pattern 5: State Tracking with Additional Info

**Concept:** Stack stores tuples (element, metadata) for complex state

```python
def decodeString(s: str) -> str:
    stack = []
    current_num = 0
    current_str = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Save current state
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            # Restore and multiply
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str
```

**Why Stack:** Each `[` opens new nested context, `]` closes most recent
**Time:** O(n), **Space:** O(n)


---

## 🎓 Progressive Learning Path

### Level 1: Stack Basics (Understand LIFO)
**Start:** Simple matching problems
- Valid Parentheses (warmup)
- Remove All Adjacent Duplicates in String

**Learn:** Push/pop mechanics, checking before pop, single-type tracking

---

### Level 2: State + Stack (Track Additional Info)
**Next:** [098. Remove Adjacent Duplicates II](./098_remove_all_adjacent_duplicates_in_string_ii.md)
- Stack stores `(char, count)` tuples

**Learn:** Stack can hold complex data, not just single values

---

### Level 3: Operator Precedence & Parsing
**Then:** [008. Basic Calculator II](./008_basic_calculator_ii.md)
- Handle `+ - * /` with precedence

**Learn:** Deferred processing, when to evaluate vs when to stack

---

### Level 4: Nested Contexts
**After:** [093. Decode String](./093_decode_string.md)
- Nested `3[a2[c]]` patterns

**Learn:** Save/restore state at boundaries, recursive structure simulation

---

### Level 5: Timeline Management
**Then:** [049. Exclusive Time of Functions](./049_exclusive_time_of_functions.md)
- Track function call stack with timing

**Learn:** Stack mirrors real call stack, nested intervals

---

### Level 6: Path Normalization
**Finally:** [035. Simplify Path](./035_simplify_path.md)
- Handle `/a/../b/./c`

**Learn:** Stack as undo buffer, filtering logic

---

## ⚠️ Common Pitfalls & How to Avoid Them

### 1. **IndexError: pop from empty list**

```python
# ❌ WRONG: Forgot to check if stack is empty
stack = []
if some_condition:
    stack.pop()  # Crashes if stack is empty

# ✅ CORRECT: Always guard pop operations
if stack:  # or: if len(stack) > 0
    stack.pop()
```

**Why it happens:** Assuming stack always has elements (e.g., mismatched parentheses)

---

### 2. **Wrong Order of Operations (Precedence)**

```python
# ❌ WRONG: Process operators left-to-right without precedence
# "3 + 2 * 2" = 10 (wrong, treats as (3+2)*2)
result = 3 + 2
result = result * 2

# ✅ CORRECT: Stack defers low-precedence until high-precedence done
stack = [3]  # Defer 3 until we know what follows
# See *, compute 2*2=4 first
stack.append(4)
result = sum(stack)  # 3 + 4 = 7
```

**Why it happens:** Processing sequentially instead of considering precedence

---

### 3. **Not Clearing Stack Between Operations**

```python
# ❌ WRONG: Reusing stack without clearing
stack = []
for test_case in test_cases:
    # Process test case using stack
    result = process(stack)
    # Forgot to clear! Next iteration has leftover data

# ✅ CORRECT: Reset state between independent operations
for test_case in test_cases:
    stack = []  # Fresh stack for each case
    result = process(stack)
```

**Why it happens:** Treating stack as global when it should be local to each problem

---

### 4. **Off-by-One in String Building**

```python
# ❌ WRONG: Building result while processing
result = ""
for char in s:
    result += stack.pop()  # Builds in wrong order

# ✅ CORRECT: Build result from stack at the end
stack = []
# ... process ...
result = ''.join(stack)  # Or reverse if needed
```

**Why it happens:** Forgetting LIFO means reversed order

---

### 5. **Mutating While Iterating**

```python
# ❌ WRONG: Popping multiple items without checking
while stack[-1] != target:  # Crashes if target not in stack
    stack.pop()

# ✅ CORRECT: Check stack non-empty in loop condition
while stack and stack[-1] != target:
    stack.pop()
```

**Why it happens:** Assuming stack has enough elements

---

### 6. **Wrong Data Type on Stack**

```python
# ❌ WRONG: Mixing types without planning
stack = []
stack.append(3)        # int
stack.append('(')      # str
# Later: int(stack.pop()) crashes if it's '('

# ✅ CORRECT: Store consistent types or use tuples
stack = []
stack.append((3, 'number'))
stack.append(('(', 'paren'))
value, value_type = stack.pop()
```

**Why it happens:** Not planning what information stack needs to track

---

## ✅ Comprehensive Testing Strategy

### Test Case Categories

#### 1. **Empty/Minimal Input**
```python
# Empty string
assert process("") == expected_empty

# Single element
assert process("a") == expected_single
```

#### 2. **Nested Structures (Depth)**
```python
# Shallow nesting
assert isValid("()") == True

# Deep nesting
assert isValid("(((())))") == True

# Mixed depth
assert isValid("(()(()))") == True
```

#### 3. **Flat Structures (No Nesting)**
```python
# No nesting needed
assert simplifyPath("/a/b/c") == "/a/b/c"

# All operations at same level
assert calculate("1+2+3") == 6
```

#### 4. **Invalid/Malformed Input**
```python
# Mismatched pairs
assert isValid("(]") == False

# Extra closing
assert isValid("())") == False

# Extra opening
assert isValid("(()") == False
```

#### 5. **Edge Cases**
```python
# All same character
assert removeDuplicates("aaaa") == ""

# No operations needed
assert simplifyPath("/home") == "/home"

# Maximum nesting depth
assert decodeString("10[a]") == "a" * 10
```

#### 6. **Stress Tests**
```python
# Large input
assert len(process("(" * 10000 + ")" * 10000)) >= 0

# Complex nesting
assert decodeString("3[a2[c]]") == "accaccacc"
```

---

## 💡 Templates & Code Patterns

### Template 1: Basic Matching (Parentheses)

```python
def isValid(s: str) -> bool:
    """Match opening/closing pairs"""
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:  # Opening
            stack.append(char)
        else:  # Closing
            if not stack or pairs[stack[-1]] != char:
                return False
            stack.pop()

    return not stack  # True if all matched
```

---

### Template 2: Calculator with Precedence

```python
def calculate(s: str) -> int:
    """Evaluate expression with operator precedence"""
    stack = []
    num = 0
    operator = '+'

    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)

        if char in '+-*/' or i == len(s) - 1:
            if operator == '+':
                stack.append(num)
            elif operator == '-':
                stack.append(-num)
            elif operator == '*':
                stack.append(stack.pop() * num)
            elif operator == '/':
                stack.append(int(stack.pop() / num))

            operator = char
            num = 0

    return sum(stack)
```

---

### Template 3: Nested State Management

```python
def decodeString(s: str) -> str:
    """Handle nested structures with state save/restore"""
    stack = []
    current_num = 0
    current_str = ''

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            # Save state before entering nested scope
            stack.append((current_str, current_num))
            current_str = ''
            current_num = 0
        elif char == ']':
            # Restore state and apply operation
            prev_str, num = stack.pop()
            current_str = prev_str + current_str * num
        else:
            current_str += char

    return current_str
```

---

### Template 4: Monotonic Stack (Next Greater)

```python
def nextGreaterElement(nums: List[int]) -> List[int]:
    """Find next greater element for each position"""
    n = len(nums)
    result = [-1] * n
    stack = []  # Store indices

    for i in range(n):
        # Pop smaller elements - they found their next greater
        while stack and nums[stack[-1]] < nums[i]:
            result[stack.pop()] = nums[i]

        stack.append(i)

    return result
```

---

### Template 5: Stack with Tracking Info

```python
def removeKAdjacent(s: str, k: int) -> str:
    """Remove k adjacent duplicates with count tracking"""
    stack = []  # [(char, count)]

    for char in s:
        if stack and stack[-1][0] == char:
            stack[-1] = (char, stack[-1][1] + 1)
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append((char, 1))

    return ''.join(char * count for char, count in stack)
```

---

## 💎 Mastery Tips & Mental Models

### Mental Model 1: Stack as "Undo Buffer"
Think of Ctrl+Z in text editors - most recent action undone first.
- **Simplify Path:** `..` undoes the last directory entered
- **Text Editor:** Undo typing in reverse order

---

### Mental Model 2: Stack as "Call Stack"
Mimics how function calls work in programming.
- **Exclusive Time:** Track function enter/exit like debugger
- **DFS Traversal:** Replace recursion with explicit stack

---

### Mental Model 3: Stack as "Clipboard History"
Recent items are easier to access than old ones.
- **Matching Parentheses:** Match with most recent opening
- **Expression Parsing:** Most recent operator determines precedence

---

### Mental Model 4: Stack as "Plate Stack"
Physical stack of plates - only top plate accessible.
- **Can't reach middle:** If you need random access, stack is wrong choice
- **LIFO constraint:** Last plate added is first removed

---

### Recognition Patterns (When to Choose Stack)

✅ **Use Stack When You See:**
- "Matching" (parentheses, brackets, tags)
- "Adjacent" (duplicates, similar elements)
- "Nested" (structures within structures)
- "Evaluate" (expressions, formulas)
- "Simplify" (paths, expressions)
- "Backtrack" (undo, reverse)
- "Most recent" (temporal ordering matters)

❌ **Don't Use Stack When You See:**
- "Contiguous subarray sum" → Sliding Window or Prefix Sum
- "Two numbers that sum" → HashMap or Two Pointers
- "Sorted array" → Binary Search or Two Pointers
- "Level-order" → Queue (BFS)
- "Need to access middle elements" → Array or HashMap

---

### Complexity Patterns

**Time Complexity:**
- Push/Pop: O(1) per operation
- Total for n elements: O(n) - each element pushed and popped once
- Nested processing: Still O(n) if each char processed constant times

**Space Complexity:**
- Worst case: O(n) - all elements on stack (all opening parens)
- Best case: O(1) - immediately matching pairs
- Average: O(d) where d = max nesting depth

---

### Interview Strategy

1. **Identify stack signal words:** nested, adjacent, matching, recent, undo
2. **Clarify LIFO need:** "Does most recent element matter?"
3. **Design what stack stores:** Single value? Tuple? Index vs value?
4. **Plan push/pop conditions:** When to add? When to remove?
5. **Consider edge cases:** Empty stack checks, mismatched pairs
6. **Optimize space:** Sometimes can use input array as stack

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 008 | [Basic Calculator II](./008_basic_calculator_ii.md) | MEDIUM | 84.0% |
| 035 | [Simplify Path](./035_simplify_path.md) | MEDIUM | 65.0% |
| 049 | [Exclusive Time of Functions](./049_exclusive_time_of_functions.md) | MEDIUM | 56.0% |
| 093 | [Decode String](./093_decode_string.md) | MEDIUM | 32.0% |
| 098 | [Remove All Adjacent Duplicates in String II](./098_remove_all_adjacent_duplicates_in_string_ii.md) | MEDIUM | 32.0% |

---

[← Back to Main](../README.md)
