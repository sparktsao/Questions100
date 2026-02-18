# Stack Problems - Comprehensive Analysis

## 🎯 Category Overview

**Total Problems:** 5
**Difficulty Range:** All Medium
**Core Concept:** Using stacks for navigation, computation, state tracking, and nested structures

**🔑 Key Insight:** Stack pattern depends on purpose:
- **Navigation** → Push/pop for levels (#035)
- **Deferred Computation** → Handle operator precedence (#008)
- **State Tracking** → Track pause/resume (#049)
- **Nested Contexts** → Handle nested structures (#093)
- **Count Tracking** → Track frequencies with cascading (#098)

---

## 📊 Problem Progression Map

```
Level 1: Simplify Path (#035) - Navigation Stack (FOUNDATION)
    ↓
Level 2: Basic Calculator II (#008) - Deferred Computation
    ↓
Level 3: Exclusive Time of Functions (#049) - State Tracking
    ↓
Level 4: Decode String (#093) - Nested Contexts
    ↓
Level 5: Remove Adjacent Duplicates II (#098) - Count Stack (ADVANCED)
```

---

## 🔍 The Five Stack Patterns

### Pattern A: Navigation Stack
**When:** Need to go backward/undo (directory navigation, undo operations)
**Key:** Stack naturally handles "go back" with pop
**Example:** #035 (Simplify Path)

### Pattern B: Deferred Computation Stack
**When:** Expression evaluation with operator precedence
**Key:** Immediate evaluation for high-priority ops, defer low-priority
**Example:** #008 (Basic Calculator II)

### Pattern C: State Tracking Stack
**When:** Track pause/resume of nested states
**Key:** Stack tracks active contexts and their accumulated state
**Example:** #049 (Exclusive Time)

### Pattern D: Nested Context Stack
**When:** Handle nested structures (brackets, recursion)
**Key:** Push context on open, pop and process on close
**Example:** #093 (Decode String)

### Pattern E: Count Tracking Stack
**When:** Track element frequencies with cascading effects
**Key:** Stack stores (element, count) pairs
**Example:** #098 (Remove Duplicates II)

---

## 📖 Problem-by-Problem Analysis

### 1️⃣ **Problem #035: Simplify Path** (MEDIUM)

**🎯 Task:** Simplify Unix file path
**📥 Input:** Absolute path string
**📤 Output:** Canonical path
**🏷️ Tag:** Navigation Stack

#### The Navigation Pattern!
```
Split by '/' → Process each component:
  - ".." → go up (pop stack)
  - "." or empty → skip
  - valid name → go in (push stack)

Final path: join stack with '/'
```

#### Algorithm
```python
def simplifyPath(path: str) -> str:
    components = path.split('/')
    stack = []

    for component in components:
        if component == '..':
            # Go up one directory (if possible)
            if stack:
                stack.pop()
        elif component and component != '.':
            # Valid directory name
            stack.append(component)
        # Skip empty and '.'

    return '/' + '/'.join(stack)
```

#### Key Cases
```
"/a/./b/../../c/" → "/c"

Split: ['', 'a', '.', 'b', '', '', 'c', '']
Process:
  '' → skip
  'a' → push: ['a']
  '.' → skip
  'b' → push: ['a', 'b']
  '' → skip (multiple slashes)
  '..' → pop: ['a']
  '..' → pop: []
  'c' → push: ['c']
  '' → skip

Result: "/" + "c" = "/c" ✓
```

#### Key Insight
> **Stack for Backtracking:** Natural model for "go back" operations

#### Complexity
- **Time:** O(n) - single pass
- **Space:** O(n) - stack storage

---

### 2️⃣ **Problem #008: Basic Calculator II** (MEDIUM)

**🎯 Task:** Evaluate mathematical expression with +, -, *, /
**📥 Input:** Expression string
**📤 Output:** Result integer
**🏷️ Tag:** Deferred Computation Stack

#### The Operator Precedence Pattern!
```
Key Insight: Handle * and / immediately, defer + and -

+ or -: Push number to stack (with sign)
* or /: Pop previous, compute, push result

Final: Sum entire stack
```

#### Algorithm
```python
def calculate(s: str) -> int:
    stack = []
    num = 0
    sign = '+'

    for i, char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)

        # Process when we hit operator or end of string
        if char in '+-*/' or i == len(s) - 1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(int(stack.pop() / num))

            if char in '+-*/':
                sign = char
                num = 0

    return sum(stack)
```

#### Example Walkthrough
```
"3+2*2" → 7

Process:
  '3': num=3
  '+': sign='+', push 3, stack=[3]
  '2': num=2
  '*': sign='*', push 2, stack=[3,2]
  '2': num=2
  end: sign='*', compute 2*2=4, stack=[3,4]

Sum: 3+4 = 7 ✓

Why it works:
  + and - are deferred (just pushed)
  * and / are computed immediately (pop and compute)
  This respects operator precedence!
```

#### Key Insight
> **Deferred vs Immediate:** Low-priority operators deferred to stack, high-priority computed immediately

#### Complexity
- **Time:** O(n) - single pass
- **Space:** O(n) - stack for numbers

---

### 3️⃣ **Problem #049: Exclusive Time of Functions** (MEDIUM)

**🎯 Task:** Calculate exclusive execution time for functions
**📥 Input:** Number of functions + logs
**📤 Output:** Exclusive time array
**🏷️ Tag:** State Tracking Stack

#### The State Tracking Pattern!
```
Stack tracks: Currently executing functions
When function starts: Previous function pauses
When function ends: Previous function resumes

Track time intervals carefully!
```

#### Algorithm
```python
def exclusiveTime(n: int, logs: List[str]) -> List[int]:
    result = [0] * n
    stack = []  # Function IDs
    prev_time = 0

    for log in logs:
        func_id, action, timestamp = log.split(':')
        func_id = int(func_id)
        timestamp = int(timestamp)

        if action == "start":
            # Pause current function
            if stack:
                result[stack[-1]] += timestamp - prev_time

            # Start new function
            stack.append(func_id)
            prev_time = timestamp
        else:  # "end"
            # End current function (inclusive)
            result[stack[-1]] += timestamp - prev_time + 1
            stack.pop()

            # Resume previous function
            prev_time = timestamp + 1

    return result
```

#### Example Walkthrough
```
n=2, logs=["0:start:0","1:start:2","1:end:5","0:end:6"]

Timeline:
  0  1  2  3  4  5  6
  [--0--][----1----][-0-]

Process:
  "0:start:0": stack=[0], prev=0
  "1:start:2": result[0]+=2-0=2, stack=[0,1], prev=2
  "1:end:5": result[1]+=5-2+1=4, stack=[0], prev=6
  "0:end:6": result[0]+=6-6+1=1, stack=[]

Result: [3, 4] ✓
```

#### Key Insight
> **Pause/Resume Tracking:** Stack tracks active function; compute time when switching

#### Complexity
- **Time:** O(m) - m logs
- **Space:** O(n) - stack depth ≤ n

---

### 4️⃣ **Problem #093: Decode String** (MEDIUM)

**🎯 Task:** Decode nested string encoding like "3[a2[c]]"
**📥 Input:** Encoded string
**📤 Output:** Decoded string
**🏷️ Tag:** Nested Context Stack

#### The Nested Context Pattern!
```
'[' → Push current context (string, count) to stack
']' → Pop context, repeat current string, merge

Stack stores: (previous_string, repeat_count)
```

#### Algorithm
```python
def decodeString(s: str) -> str:
    stack = []
    current_string = ""
    current_num = 0

    for char in s:
        if char.isdigit():
            # Build multi-digit number
            current_num = current_num * 10 + int(char)

        elif char == '[':
            # Push context to stack
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0

        elif char == ']':
            # Pop context and decode
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * num

        else:
            # Regular character
            current_string += char

    return current_string
```

#### Example Walkthrough
```
"3[a2[c]]" → "accaccacc"

Process:
  '3': num=3
  '[': push ("", 3), reset: string="", num=0
  'a': string="a"
  '2': num=2
  '[': push ("a", 2), reset: string="", num=0
  'c': string="c"
  ']': pop ("a", 2), string="a"+"c"*2="acc"
  ']': pop ("", 3), string=""+"acc"*3="accaccacc"

Result: "accaccacc" ✓
```

#### Key Insight
> **Context Preservation:** Stack preserves outer context while processing inner

#### Complexity
- **Time:** O(maxK × n) - string repetition cost
- **Space:** O(n) - stack depth

---

### 5️⃣ **Problem #098: Remove All Adjacent Duplicates in String II** (MEDIUM)

**🎯 Task:** Remove k consecutive duplicate characters
**📥 Input:** String + k
**📤 Output:** String after all removals
**🏷️ Tag:** Count Tracking Stack

#### The Count Stack Pattern!
```
Stack stores: [character, count] pairs

Same char → increment count
Count reaches k → pop (remove)
Different char → push new entry

Cascading removals happen automatically!
```

#### Algorithm
```python
def removeDuplicates(s: str, k: int) -> str:
    # Stack stores [character, count]
    stack = []

    for char in s:
        if stack and stack[-1][0] == char:
            # Same character, increment count
            stack[-1][1] += 1

            # Remove if we reach k
            if stack[-1][1] == k:
                stack.pop()
        else:
            # New character
            stack.append([char, 1])

    # Rebuild string
    return ''.join(char * count for char, count in stack)
```

#### Example Walkthrough
```
s="deeedbbcccbdaa", k=3

Process:
  'd': stack=[['d',1]]
  'e': stack=[['d',1],['e',1]]
  'e': stack=[['d',1],['e',2]]
  'e': stack=[['d',1],['e',3]] → count==k, pop → [['d',1]]
  'd': stack=[['d',2]]
  'b': stack=[['d',2],['b',1]]
  'b': stack=[['d',2],['b',2]]
  'c': stack=[['d',2],['b',2],['c',1]]
  'c': stack=[['d',2],['b',2],['c',2]]
  'c': stack=[['d',2],['b',2],['c',3]] → pop → [['d',2],['b',2]]
  'b': stack=[['d',2],['b',3]] → pop → [['d',2]]
  'd': stack=[['d',3]] → pop → []
  'a': stack=[['a',1]]
  'a': stack=[['a',2]]

Result: "aa" ✓
```

#### Why Stack Handles Cascading?
```
After removing "ccc", we have "...bb"
Next 'b' makes it 3 b's → automatic removal!
Stack mechanism naturally handles cascading without re-scanning
```

#### Key Insight
> **Count Tracking + Stack:** Cascading removals happen automatically via stack

#### Complexity
- **Time:** O(n) - each char pushed/popped once
- **Space:** O(n) - stack storage

---

## 🔄 Algorithm Relationships

### Can Previous Solutions Be Modified?

| From | To | Possible? | How? |
|------|-----|-----------|------|
| #035 → #098 | No | Different patterns (navigation vs counting) |
| #008 → #049 | No | Different tracking (numbers vs time intervals) |
| #093 → #098 | Partial | Both track state, but different popping conditions |
| #049 → #093 | No | Different contexts (time vs string) |

### Common Template Elements
```python
# All use basic stack operations
stack = []

for element in input:
    # Condition-based push/pop/update
    if condition:
        stack.append(item)
    elif other_condition:
        stack.pop()
    # Process based on problem

# Build result from stack
result = construct_from_stack(stack)
```

---

## 💡 Key Learning Insights

### 1. **Navigation Stack Template**
```python
def navigate_with_stack(path):
    parts = path.split(separator)
    stack = []

    for part in parts:
        if is_go_back(part):
            if stack:
                stack.pop()
        elif is_valid(part):
            stack.append(part)
        # else skip

    return construct_result(stack)
```

### 2. **Deferred Computation Template**
```python
def compute_with_precedence(expression):
    stack = []
    num, prev_op = 0, '+'

    for i, char in enumerate(expression):
        if char.isdigit():
            num = num * 10 + int(char)

        if is_operator(char) or is_last(i):
            if prev_op in low_priority:
                stack.append(apply(prev_op, num))
            else:  # high priority
                stack[-1] = apply(prev_op, stack[-1], num)

            prev_op = char
            num = 0

    return aggregate(stack)
```

### 3. **State Tracking Template**
```python
def track_state_with_stack(events):
    stack = []  # Active states
    result = init_result()
    prev_time = 0

    for event in events:
        if is_start(event):
            # Pause current
            if stack:
                update_result(stack[-1], event.time - prev_time)
            # Start new
            stack.append(event.id)
            prev_time = event.time
        else:  # end
            # End current
            update_result(stack[-1], event.time - prev_time + 1)
            stack.pop()
            prev_time = event.time + 1

    return result
```

### 4. **Nested Context Template**
```python
def process_nested(input):
    stack = []
    current_state = init_state()

    for char in input:
        if char == open_bracket:
            # Save current context
            stack.append(current_state)
            current_state = init_state()

        elif char == close_bracket:
            # Restore and merge
            prev_state = stack.pop()
            current_state = merge(prev_state, current_state)

        else:
            # Process character
            update_state(current_state, char)

    return current_state
```

### 5. **Count Stack Template**
```python
def count_and_remove(items, k):
    stack = []  # [(item, count)]

    for item in items:
        if stack and stack[-1][0] == item:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()  # Remove k items
        else:
            stack.append([item, 1])

    return reconstruct(stack)
```

---

## 🎨 Visual Comparison Table

| Problem | Pattern | Stack Stores | Key Operation | Time | Space |
|---------|---------|--------------|---------------|------|-------|
| #035 | Navigation | Directories | Pop on ".." | O(n) | O(n) |
| #008 | Deferred Compute | Numbers | Immediate * / | O(n) | O(n) |
| #049 | State Tracking | Function IDs | Time intervals | O(m) | O(n) |
| #093 | Nested Context | (string, count) | Push/pop on brackets | O(maxK×n) | O(n) |
| #098 | Count Tracking | (char, count) | Pop when count==k | O(n) | O(n) |

---

## 🚀 Recommended Study Order

1. **Navigation Foundation:** #035 (Simplify Path)
2. **Deferred Computation:** #008 (Basic Calculator II)
3. **State Tracking:** #049 (Exclusive Time)
4. **Nested Structures:** #093 (Decode String)
5. **Advanced Counting:** #098 (Remove Duplicates II)

---

## 📝 Interview Tips

### Common Mistakes

1. **#035:** Forgetting to check if stack is empty before popping on ".."
2. **#008:** Not handling multi-digit numbers or forgetting to process last number
3. **#049:** Off-by-one errors (end timestamp is inclusive!)
4. **#093:** Not handling multi-digit repeat counts
5. **#098:** Not understanding cascading removals or trying to re-scan string

### Pattern Recognition
```
"navigate/undo" → Navigation Stack (#035)
"operator precedence" → Deferred Computation (#008)
"pause/resume" → State Tracking (#049)
"nested brackets" → Nested Context (#093)
"consecutive duplicates" → Count Stack (#098)
```

### Stack vs Other Structures
```
Need LIFO (Last In First Out) → Stack
Need hierarchy/nesting → Stack
Need to "go back" → Stack
Need order of all elements → Queue or Array
Need min/max quickly → Heap
```

---

## 🎓 Practice Progression

### Week 1: Basic Stack Operations
- Day 1-2: #035 (Navigation)
- Day 3: Understand push/pop patterns
- Day 4-5: Practice variants

### Week 2: Computation & State
- Day 1-2: #008 (Calculator)
- Day 3-4: #049 (Time Tracking)
- Day 5: Compare patterns

### Week 3: Advanced Patterns
- Day 1-2: #093 (Nested Decoding)
- Day 3-4: #098 (Count Stack)
- Day 5: Review all 5 patterns

---

**Summary:** Stack problems use five main patterns: navigation for backtracking (#035), deferred computation for operator precedence (#008), state tracking for pause/resume (#049), nested context for bracket structures (#093), and count tracking for cascading removals (#098). All achieve O(n) time complexity with O(n) space. Master the core insight: stacks excel at LIFO operations, making them ideal for nested structures, operator precedence, and "undo" behavior. Key templates: navigation (pop on back), deferred computation (immediate vs defer based on priority), state tracking (pause/resume with time), nested context (save/restore on brackets), count tracking (remove when threshold reached). Choose stack when you need to maintain hierarchy, handle nesting, or support backtracking operations.
