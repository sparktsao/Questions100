#!/usr/bin/env python3
"""
Generate comprehensive mastery summaries for ALL 16 LeetCode categories.
Replaces existing {category}_summary.md files.
"""

import os
import glob

BASE_DIR = '/Users/sparkt/2026C/Questions100/LeetCode'

def read_problems(category_path):
    """Read problem metadata from category folder."""
    files = sorted(glob.glob(os.path.join(category_path, '[0-9]*.md')))
    problems = []

    for filepath in files:
        try:
            with open(filepath, 'r') as f:
                lines = f.readlines()

            num = os.path.basename(filepath)[:3]
            title = lines[0].replace('#', '').strip() if lines else 'Unknown'
            if title.startswith(num):
                title = title[len(num):].lstrip('.').strip()

            difficulty = 'MEDIUM'
            frequency = 'N/A'

            for line in lines[:20]:
                if '**Difficulty:**' in line:
                    difficulty = line.split('**Difficulty:**')[1].strip()
                elif '**Frequency:**' in line:
                    frequency = line.split('**Frequency:**')[1].strip()

            problems.append({
                'num': num,
                'title': title,
                'difficulty': difficulty,
                'frequency': frequency,
                'filename': os.path.basename(filepath)
            })
        except:
            pass

    return problems


def generate_binary_search_summary(problems, output_path):
    """Generate Binary Search mastery guide."""
    content = """# Binary Search Mastery

## From Array Search to Answer Space Optimization

---

## 🎯 Category Overview

**Total Problems:** {total}

**Core Insight:**
The fundamental insight of binary search is MONOTONICITY - if we can check a condition
and know which half of the search space to eliminate, we can solve in O(log n) time. This applies to:
1. Sorted arrays (traditional)
2. Unsorted arrays with monotonic properties
3. Answer spaces where "if X works, all values > X work"

---

## 📚 The Four Sub-Patterns

This category has **4 distinct sub-patterns**. Master each progressively:

### Pattern 1: Classic Binary Search on Sorted Array

**When to Use:** Array is explicitly sorted, searching for exact value or checking existence

**Key Problems:** #042 Find First and Last Position

**Template:**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # NOTE: <= for exact search
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

**Common Bugs:**
- ❌ Using `<` instead of `<=` (misses last element or infinite loop)
- ❌ Not handling empty array
- ❌ Wrong mid calculation causing overflow (use `left + (right - left) // 2`)
- ❌ Incorrect boundary updates (must be `mid ± 1` with `<=`)

**Testing Checklist:**
```python
# Edge cases
[], [1], [1,2]

# Position cases
[1,2,3] target=1  # start
[1,2,3] target=3  # end
[1,2,3,4,5] target=3  # middle

# Not found
[1,3,5] target=2  # between
[1,2,3] target=0  # before all
[1,2,3] target=5  # after all
```

---

### Pattern 2: Boundary Search (First/Last Occurrence)

**When to Use:** Need leftmost or rightmost position in sorted array with duplicates

**Key Problems:** #042 Find First and Last Position

**The Key Difference:** After finding target, DON'T return - keep searching!

**Template for LEFT bound:**
```python
def find_left_bound(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # KEY: Keep searching LEFT!
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

**Template for RIGHT bound:**
```python
def find_right_bound(arr, target):
    left, right = 0, len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # KEY: Keep searching RIGHT!
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result
```

**Common Bugs:**
- ❌ Returning immediately when finding target (not continuing search)
- ❌ Moving wrong pointer after match (mixing up left vs right)
- ❌ Not saving `result` before continuing
- ❌ Using `bisect_left/bisect_right` without understanding edge cases

**Test Cases:**
```python
[1,2,2,2,3] target=2  # multiple occurrences
[2,2,2,2] target=2    # all same
[1,2,3] target=2      # single occurrence
[1,3,5] target=2      # not found
```

---

### Pattern 3: Binary Search on Unsorted Array (Implicit Monotonicity)

**When to Use:** Array has peaks, valleys, or rotation - not explicitly sorted but has monotonic property

**Key Problems:** #010 Find Peak Element

**Mental Shift:** Not searching for a value - searching for a CONDITION (peak, valley, rotation point)

**Template:**
```python
def find_peak(arr):
    left, right = 0, len(arr) - 1

    while left < right:  # NOTE: < not <=!
        mid = left + (right - left) // 2

        if arr[mid] > arr[mid + 1]:
            # Descending, peak is at mid or left
            right = mid  # Keep mid as candidate
        else:
            # Ascending, peak is on right
            left = mid + 1

    return left  # left == right at convergence
```

**Why Different Template?**
- Use `while left < right` (not `<=`)
- Use `right = mid` (not `mid - 1`) - keep mid as candidate
- These two MUST go together or infinite loop!

**Common Bugs:**
- ❌ Using `left <= right` with `right = mid` → infinite loop
- ❌ Checking `arr[mid] > arr[mid-1]` and `arr[mid] > arr[mid+1]` → over-constraining
- ❌ Not handling boundary checks for `mid+1`

---

### Pattern 4: Binary Search on Answer Space ⭐ MOST IMPORTANT

**When to Use:** Problem asks "minimum capacity to...", "minimum speed to...", "maximum weight where..."

**Key Signal:** NOT searching IN array, searching FOR a value that satisfies constraints

**Key Problems:** #079 Ship Packages, #094 Koko Bananas, #074 Cutting Ribbons

**MENTAL MODEL SHIFT:**
```
You're NOT searching for an INDEX in the array!
You're binary searching over POSSIBLE ANSWER VALUES.

The array defines CONSTRAINTS.
You're searching a conceptual number line: [min_possible, max_possible]
```

**Template (Minimize):**
```python
def binary_search_on_answer_minimize(constraints):
    def is_valid(candidate_value):
        # Check if candidate_value satisfies constraints.
        # O(n) typically - must verify against all elements.
        # MUST be monotonic: if X valid, all X+1 valid too!
        # Problem-specific validation
        pass

    # Define search space
    left = minimum_possible_value  # e.g., max(array) for capacity
    right = maximum_possible_value  # e.g., sum(array) for capacity

    while left < right:
        mid = left + (right - left) // 2

        if is_valid(mid):
            # mid works, try smaller
            right = mid
        else:
            # mid doesn't work, need larger
            left = mid + 1

    return left
```

**Template (Maximize):**
```python
def binary_search_on_answer_maximize(constraints):
    def is_valid(candidate_value):
        pass

    left = min_possible
    right = max_possible

    while left < right:
        mid = left + (right - left + 1) // 2  # NOTE: +1 for maximize!

        if is_valid(mid):
            # mid works, try larger
            left = mid
        else:
            # mid doesn't work, need smaller
            right = mid - 1

    return left
```

**Common Bugs:**
- ❌ Wrong search space: must be [min_theoretically_possible, max_theoretically_possible]
- ❌ is_valid() not monotonic (violates binary search requirement!)
- ❌ Confusing minimize vs maximize (wrong pointer updates)
- ❌ Not using `+1` in mid for maximize → infinite loop
- ❌ is_valid() inefficient (not short-circuiting when answer known)

**How to Identify This Pattern:**
1. Problem has "minimum X such that..." or "maximum X such that..."
2. Array is given but you're not searching for index
3. Brute force would be "try every value from 1 to max"
4. There exists a check function where if X works, you know about X±1

**Example Breakdown - Koko Bananas:**
```python
# Problem: Minimum eating speed to finish in h hours
# What we're searching: speed (integer)
# Search space: [1, max(piles)]
# Why? Speed 1 = slowest, max(piles) = can eat biggest pile in 1 hour

def is_valid(speed):
    hours_needed = sum((pile + speed - 1) // speed for pile in piles)
    return hours_needed <= h

# Monotonic? If speed K works, speed K+1 definitely works (faster)
# So binary search for MINIMUM speed where is_valid returns True
```

---

## 🎓 Learning Path: Level 1 → Level 7

### Level 1: Classic Search (Foundation)
**Problem:** #042 Find First and Last Position
**Goal:** Master basic template with `<=` comparison
**Practice:** Write from scratch 5 times. Test all edge cases.
**Time:** 1-2 days

### Level 2: Boundary Search (Variation)
**Problem:** #042 (leftmost/rightmost variation)
**Goal:** Understand continuing search after finding match
**Practice:** Compare left vs right boundary templates
**Time:** 1 day

### Level 3: Implicit Monotonicity
**Problem:** #010 Find Peak Element
**Goal:** Recognize monotonic property without explicit sort
**Practice:** Draw arrays, explain why one half eliminates
**Time:** 1-2 days

### Level 4: Answer Space - Easy
**Problem:** #094 Koko Eating Bananas
**Goal:** Mental shift from "search in array" to "search for value"
**Practice:** Before coding, identify: search space, is_valid(), monotonicity
**Time:** 2-3 days

### Level 5: Answer Space - Capacity
**Problems:** #079 Ship Packages, #074 Cutting Ribbons
**Goal:** Apply pattern to capacity/allocation problems
**Practice:** Write is_valid() first, then binary search
**Time:** 2-3 days

### Level 6: Advanced 2D
**Problem:** #084 Kth Smallest in Sorted Matrix
**Goal:** Binary search with 2D constraints
**Practice:** Understand what makes 2D search monotonic
**Time:** 3-4 days

### Level 7: Master Challenge
**Problem:** #100 Median of Two Sorted Arrays
**Goal:** Binary search with partition logic
**Practice:** This is HARD - study, understand, implement 3 times
**Time:** 5-7 days

**Total Time to Mastery: 2-3 weeks with daily practice**

---

## ⚠️ Universal Common Errors

### Error 1: Integer Overflow
**Wrong:** `mid = (left + right) // 2`
**Correct:** `mid = left + (right - left) // 2`
**Why:** In Java/C++, left + right can overflow. Python OK but use correct form.

### Error 2: Template Confusion
**Wrong:** Using `while left < right` with `right = mid - 1`
**Correct:** Match loop condition with boundary update
**Rule:**
- `left <= right` requires `right = mid - 1`, `left = mid + 1`
- `left < right` allows `right = mid`, `left = mid + 1`

### Error 3: Off-by-One with Boundaries
**Test:** Always test arrays of size 1 and 2
**Common Issue:** `right = len(arr)` vs `len(arr) - 1`

### Error 4: Array Boundary Checks
**Wrong:** `if arr[mid] > arr[mid + 1]` without checking mid < len - 1
**Correct:** Always validate array access

---

## ✅ Testing Strategy

### Property-Based Testing
```python
import random

def test_binary_search_property():
    \"\"\"Run 1000 random tests\"\"\"
    for _ in range(1000):
        size = random.randint(0, 100)
        arr = sorted([random.randint(-100, 100) for _ in range(size)])
        target = random.randint(-100, 100)

        result = binary_search(arr, target)
        expected = arr.index(target) if target in arr else -1

        assert result == expected, f"Failed: arr={arr}, target={target}"
```

### Invariant Checking
```python
def binary_search_with_invariants(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        # Invariant: if target exists, it's in [left, right]
        assert 0 <= left <= len(arr)
        assert -1 <= right < len(arr)
        assert left <= right + 1

        mid = left + (right - left) // 2
        # ...
```

---

## 💎 Mastery Insights

### Insight 1: Two Different Mental Models

Binary search has TWO completely different use cases:

**USE CASE 1: Search IN Array**
- Input: Sorted/monotonic array
- Output: Index or -1
- Template: Classic binary search
- Example: #042

**USE CASE 2: Search FOR Answer**
- Input: Problem constraints (array defines limits, not search space!)
- Output: Optimal value (NOT an index!)
- Template: Binary search on answer space
- Example: #079, #094

Many students confuse these! Recognize which type before coding.

### Insight 2: Monotonicity is Everything

Binary search ONLY works when checking mid tells us which half to eliminate.

**For array search:** If arr[mid] < target → target must be in right half

**For answer search:** If is_valid(mid) = True → all values > mid also valid

**If this property doesn't hold, binary search FAILS!**

Example where it fails:
```python
arr = [3, 1, 4, 1, 5, 9, 2, 6]  # Not monotonic!
# Cannot eliminate half based on arr[mid] alone
```

### Insight 3: How to Recognize "Answer Space" Problems

🚨 **SIGNALS:**
- Keywords: "minimum capacity", "minimum speed", "maximum pages", "kth element"
- Question format: "What is the minimum X such that..."
- Array given but NOT searching for index/position
- Brute force: "try every value from min to max"

🔍 **VERIFICATION CHECKLIST:**
1. What am I minimizing/maximizing? (This is the "answer")
2. What are theoretical min/max bounds? (This is search space)
3. Can I write is_valid(candidate)? (This is the check function)
4. Is it monotonic? (If X works, does X+1 work? Or vice versa?)
5. If yes to all → Binary search on answer space!

### Insight 4: Template Choice Matters

**When to use `while left <= right`:**
- Searching for exact value
- Need to check every element
- Boundaries update with `mid ± 1`

**When to use `while left < right`:**
- Searching for first/last position
- Finding minimum/maximum satisfying condition
- Can use `right = mid` (keep mid as candidate)

**Rule:** If using `right = mid`, MUST use `left < right` (or infinite loop!)

---

## 📋 Complete Problem Reference

""".format(total=len(problems))

    # Add problem table
    content += "| # | Problem | Difficulty | Frequency |\n"
    content += "|---|---------|------------|----------|\n"
    for p in problems:
        content += f"| {p['num']} | [{p['title']}](./{p['filename']}) | {p['difficulty']} | {p['frequency']} |\n"

    content += "\n---\n\n[← Back to All Categories](../README.md)\n"

    with open(output_path, 'w') as f:
        f.write(content)


# Add similar functions for other categories... (abbreviated for space)
# I'll create a template generator that adapts to each category

def generate_summary(category_key, category_name, problems, output_path):
    """Generate comprehensive summary for any category."""

    # Count difficulties
    easy = sum(1 for p in problems if 'EASY' in p['difficulty'].upper())
    medium = sum(1 for p in problems if 'MEDIUM' in p['difficulty'].upper())
    hard = sum(1 for p in problems if 'HARD' in p['difficulty'].upper())

    # Sort by frequency (descending)
    try:
        problems_sorted = sorted(problems, key=lambda x: float(x['frequency'].rstrip('%')) if x['frequency'] != 'N/A' else 0, reverse=True)
    except:
        problems_sorted = problems

    # Skip Binary-Search - already have comprehensive version
    if category_key == 'Binary-Search':
        return

    # For other categories, use adaptive template
    generate_adaptive_summary(category_key, category_name, problems, problems_sorted, easy, medium, hard, output_path)


def generate_adaptive_summary(category_key, category_name, problems, problems_sorted, easy, medium, hard, output_path):
    """Generate comprehensive summary with adaptive content based on category."""

    # Category-specific insights (abbreviated - you can expand these)
    category_info = get_category_info(category_key)

    content = f"""# {category_name} - Comprehensive Guide

{category_info['subtitle']}

---

## 🎯 Overview

**Total Problems:** {len(problems)}
**Difficulty:** Easy ({easy}) • Medium ({medium}) • Hard ({hard})

**Core Concept:**
{category_info['core_concept']}

**Key Insight:**
{category_info['key_insight']}

---

## 📚 Sub-Patterns & Techniques

{category_info['sub_patterns']}

---

## 🎓 Learning Path

{category_info['learning_path']}

---

## ⚠️ Common Pitfalls

{category_info['common_pitfalls']}

---

## ✅ Testing Strategy

{category_info['testing_strategy']}

---

## 💡 Templates & Code Patterns

{category_info['templates']}

---

## 💎 Mastery Tips

{category_info['mastery_tips']}

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
"""

    for p in problems_sorted:
        content += f"| {p['num']} | [{p['title']}](./{p['filename']}) | {p['difficulty']} | {p['frequency']} |\n"

    content += "\n---\n\n[← Back to Main](../README.md)\n"

    with open(output_path, 'w') as f:
        f.write(content)


def get_category_info(category_key):
    """Get category-specific information."""

    info_map = {
        'Two-Pointers': {
            'subtitle': '## Opposite Direction vs Same Direction Techniques',
            'core_concept': 'Use two pointers to traverse array/list in O(n) time instead of O(n²) nested loops',
            'key_insight': 'Two pointers can move in OPPOSITE directions (start/end) or SAME direction (fast/slow). Choose based on problem requirements.',
            'sub_patterns': '''
### Pattern 1: Opposite Direction (Converging)
**Use when:** Need to find pairs, check palindrome, or compare elements from both ends
**Template:**
```python
def two_pointer_opposite(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        # Process arr[left] and arr[right]
        if condition:
            left += 1
        else:
            right -= 1
```
**Examples:** Two Sum in sorted array, Valid Palindrome, Container With Most Water

### Pattern 2: Same Direction (Fast-Slow)
**Use when:** Finding cycles, removing duplicates, or partitioning
**Template:**
```python
def two_pointer_same(arr):
    slow = 0
    for fast in range(len(arr)):
        if condition:
            arr[slow] = arr[fast]
            slow += 1
    return slow
```
**Examples:** Remove Duplicates, Move Zeros, Partition Array

### Pattern 3: Sliding Window (Special Case)
**Use when:** Finding subarrays with specific properties
**Template:**
```python
def sliding_window(arr):
    left = 0
    for right in range(len(arr)):
        # Expand window
        # ...
        while invalid_condition:
            # Shrink window
            left += 1
```
**Examples:** Longest Substring, Minimum Window
''',
            'learning_path': '''
1. **Start:** Valid Palindrome - simple opposite direction
2. **Next:** Remove Duplicates - same direction with slow/fast
3. **Then:** Container With Most Water - optimize with greedy pointer movement
4. **Advanced:** 3Sum - nested pointers
5. **Master:** Trapping Rain Water - complex pointer logic
''',
            'common_pitfalls': '''
1. ❌ Moving both pointers simultaneously when should move one
2. ❌ Off-by-one errors with `left < right` vs `left <= right`
3. ❌ Not handling edge cases: empty array, single element
4. ❌ Using nested loops instead of two pointers (missing O(n) optimization)
''',
            'testing_strategy': '''
**Test Cases:**
- Empty: []
- Single: [1]
- Two elements: [1, 2]
- All same: [5, 5, 5]
- Already sorted/valid
- Reverse sorted
- With duplicates
''',
            'templates': '''
```python
# Template 1: Opposite Direction
left, right = 0, len(arr) - 1
while left < right:
    if arr[left] + arr[right] == target:
        return [left, right]
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        right -= 1

# Template 2: Same Direction
slow = 0
for fast in range(len(arr)):
    if arr[fast] != val:
        arr[slow] = arr[fast]
        slow += 1
return slow
```
''',
            'mastery_tips': '''
1. **Recognize the pattern:** If problem mentions pairs, subarrays, or can be solved in O(n), consider two pointers
2. **Choose direction:** Opposite for pairs/symmetry, same for partitioning/duplicates
3. **Pointer movement rules:** Define clear conditions for when to move which pointer
4. **Invariant:** Always maintain what [left, right] represents
'''
        },

        'Sliding-Window': {
            'subtitle': '## Fixed Size vs Variable Size Windows',
            'core_concept': 'Maintain a window of elements and slide it across array/string to find optimal subarray',
            'key_insight': 'Window can be FIXED size (simpler) or VARIABLE size (more common). Variable uses while loop to shrink window.',
            'sub_patterns': '''
### Pattern 1: Fixed Size Window
**Use when:** Problem specifies exact window size k
**Template:**
```python
def fixed_window(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
```

### Pattern 2: Variable Size Window (Most Common!)
**Use when:** Find "longest/shortest substring/subarray that satisfies..."
**Template:**
```python
def variable_window(arr):
    left = 0
    result = 0
    window = {}  # Track window state

    for right in range(len(arr)):
        # Expand: add arr[right] to window
        window[arr[right]] = window.get(arr[right], 0) + 1

        # Shrink: while window invalid
        while window_invalid():
            window[arr[left]] -= 1
            left += 1

        # Update result with valid window
        result = max(result, right - left + 1)

    return result
```
''',
            'learning_path': '''
1. Maximum Sum Subarray of Size K (fixed window)
2. Longest Substring Without Repeating Characters (variable)
3. Minimum Window Substring (variable with complex validation)
4. Longest Substring with At Most K Distinct Characters
''',
            'common_pitfalls': '''
1. ❌ Not properly maintaining window state when shrinking
2. ❌ Updating result outside valid window
3. ❌ Forgetting to handle empty input
4. ❌ Using nested loops (O(n²)) instead of sliding window (O(n))
''',
            'testing_strategy': '''Test with: empty string, single char, all same, all unique, exactly k size, smaller than k''',
            'templates': '''See sub-patterns above for complete templates''',
            'mastery_tips': '''
1. Always expand right pointer in loop
2. Shrink left pointer in while loop when window becomes invalid
3. Use hash map to track window contents
4. Update result only when window is valid
'''
        },

        # Add more categories...
        'Array-Hashing': {
            'subtitle': '## Hash Tables for O(1) Lookup & Prefix Sums for Range Queries',
            'core_concept': 'Use hash maps for constant-time lookups and prefix sums for efficient range calculations',
            'key_insight': 'Trade space for time: hash maps give O(1) access but use O(n) space. Prefix sums enable O(1) range queries after O(n) preprocessing.',
            'sub_patterns': '''
### Pattern 1: Hash Map for Complement/Pair Finding
**Examples:** Two Sum, Group Anagrams
```python
seen = {}
for i, num in enumerate(arr):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### Pattern 2: Prefix Sum for Range Queries
**Examples:** Subarray Sum Equals K, Range Sum Query
```python
prefix = [0]
for num in arr:
    prefix.append(prefix[-1] + num)
# Sum of arr[i:j] = prefix[j] - prefix[i]
```

### Pattern 3: Counting with Hash Map
**Examples:** Top K Frequent Elements, Custom Sort
```python
from collections import Counter
count = Counter(arr)
```
''',
            'learning_path': '''Two Sum → Subarray Sum K → Top K Frequent → Group Anagrams''',
            'common_pitfalls': '''1. Not handling duplicates 2. Off-by-one in prefix sum 3. Modifying array while iterating''',
            'testing_strategy': '''Test: empty, single element, all same, all unique, with negatives''',
            'templates': '''See patterns above''',
            'mastery_tips': '''Know when to use hash map vs prefix sum. Hash for lookups, prefix for ranges.'''
        },

        'Stack': {
            'subtitle': '## LIFO for Nested Structures & Backtracking',
            'core_concept': 'Stack (Last-In-First-Out) perfect for nested structures, parsing, and operations needing reversal',
            'key_insight': 'Use stack when you need to process inner elements before outer (nested), or when you need to backtrack.',
            'sub_patterns': '''
### Pattern 1: Matching Pairs (Parentheses, Brackets)
### Pattern 2: Expression Evaluation (Calculator, Postfix)
### Pattern 3: Monotonic Stack (Next Greater Element)
### Pattern 4: DFS Simulation with Explicit Stack
''',
            'learning_path': '''Valid Parentheses → Basic Calculator II → Exclusive Time → Simplify Path''',
            'common_pitfalls': '''1. Not checking empty before pop 2. Not clearing stack between operations 3. Wrong order of operations''',
            'testing_strategy': '''Test: empty, single element, nested, flat, invalid input''',
            'templates': '''
```python
stack = []
for char in s:
    if opening:
        stack.append(char)
    else:
        if not stack or not matches(stack[-1], char):
            return False
        stack.pop()
return len(stack) == 0
```
''',
            'mastery_tips': '''Stack is LIFO - most recent first. Use for nesting, reversal, backtracking.'''
        },

        'Linked-List': {
            'subtitle': '## Pointer Manipulation & Fast-Slow Techniques',
            'core_concept': 'Master pointer manipulation, dummy nodes, and fast-slow pointer for cycles',
            'key_insight': 'Dummy node simplifies edge cases. Fast-slow pointers detect cycles and find middle.',
            'sub_patterns': '''
### Pattern 1: Dummy Node for Edge Cases
### Pattern 2: Fast-Slow Pointers (Cycle Detection, Middle Finding)
### Pattern 3: Reverse Linked List (Iterative & Recursive)
### Pattern 4: Merge Sorted Lists
''',
            'learning_path': '''Reverse List → Merge Two Lists → Remove Nth from End → Detect Cycle''',
            'common_pitfalls': '''1. Losing reference to head 2. Not handling None 3. Off-by-one in pointer movement 4. Cycle in reversal''',
            'testing_strategy': '''Test: null, single node, two nodes, cycle, no cycle''',
            'templates': '''
```python
# Dummy node pattern
dummy = ListNode(0)
dummy.next = head
current = dummy
# ...
return dummy.next

# Fast-slow pattern
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True  # Cycle detected
```
''',
            'mastery_tips': '''Always use dummy node. Draw diagrams. Check None cases.'''
        },

        'Tree': {
            'subtitle': '## DFS for Paths vs BFS for Levels',
            'core_concept': 'Choose DFS (recursion/stack) for path problems, BFS (queue) for level/distance problems',
            'key_insight': 'DFS: paths & subtree properties. BFS: levels & shortest distance.',
            'sub_patterns': '''
### Pattern 1: DFS Recursive (Height, Diameter, Path Sum)
### Pattern 2: BFS Level Order (Right Side View, Zigzag)
### Pattern 3: DFS Iterative with Stack
### Pattern 4: Parent Pointers for Upward Traversal
''',
            'learning_path': '''Max Depth → Diameter → Right Side View → LCA → Max Path Sum''',
            'common_pitfalls': '''1. Not checking None 2. Confusing pre/in/post order 3. Not tracking global state 4. DFS when need BFS''',
            'testing_strategy': '''Test: null, single node, left skewed, right skewed, balanced''',
            'templates': '''
```python
# DFS Template
def dfs(node):
    if not node:
        return base_case
    left = dfs(node.left)
    right = dfs(node.right)
    return combine(node.val, left, right)

# BFS Template
from collections import deque
queue = deque([root])
while queue:
    size = len(queue)
    for _ in range(size):
        node = queue.popleft()
        # process
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
```
''',
            'mastery_tips': '''BFS for levels, DFS for paths. Always check None first.'''
        },

        'Graph-DFS-BFS': {
            'subtitle': '## DFS for Paths & Cycles, BFS for Shortest Distance',
            'core_concept': 'DFS (stack/recursion) for connectivity & cycles, BFS (queue) for shortest paths',
            'key_insight': 'Always need visited set. DFS for deep exploration, BFS for level-by-level.',
            'sub_patterns': '''
### Pattern 1: DFS with Visited Set (Connected Components, Cycle Detection)
### Pattern 2: BFS for Shortest Path (Unweighted)
### Pattern 3: Union-Find for Connected Components
### Pattern 4: Topological Sort (DFS or BFS)
''',
            'learning_path': '''Clone Graph → Course Schedule → Word Ladder → Accounts Merge''',
            'common_pitfalls': '''1. Forgetting visited set 2. Not building adjacency list 3. Modifying during iteration 4. Infinite loops''',
            'testing_strategy': '''Test: single node, disconnected, cycle, DAG, empty''',
            'templates': '''
```python
# DFS
def dfs(node, visited):
    if node in visited:
        return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)

# BFS
from collections import deque
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)
```
''',
            'mastery_tips': '''Build adjacency list first. Always use visited. DFS=deep, BFS=level.'''
        },

        'Heap-Priority-Queue': {
            'subtitle': '## Top-K Problems & Running Median',
            'core_concept': 'Heap maintains min/max in O(log n), perfect for top-k and streaming data',
            'key_insight': 'Min heap for top K largest (invert), max heap for top K smallest',
            'sub_patterns': '''
### Pattern 1: Top K Elements (K Closest, K Frequent)
### Pattern 2: Merge K Sorted Lists
### Pattern 3: Running Median with Two Heaps
### Pattern 4: K-way Merge
''',
            'learning_path': '''Kth Largest → K Closest Points → Merge K Lists → Find Median''',
            'common_pitfalls': '''1. Wrong heap type 2. Not using negative for max heap 3. Not maintaining heap size 4. Forgetting heappush/heappop''',
            'testing_strategy': '''Test: empty, k=1, k=n, duplicates, single element''',
            'templates': '''
```python
import heapq

# Min heap (default)
heap = []
heapq.heappush(heap, val)
min_val = heapq.heappop(heap)

# Max heap (use negative)
max_heap = []
heapq.heappush(max_heap, -val)
max_val = -heapq.heappop(max_heap)

# Top K pattern
heap = []
for num in nums:
    heapq.heappush(heap, num)
    if len(heap) > k:
        heapq.heappop(heap)
return heap[0]  # kth largest
```
''',
            'mastery_tips': '''Python only has min heap. Use negative for max heap. Maintain size k for top-k.'''
        },

        'Dynamic-Programming': {
            'subtitle': '## From Recursion to Memoization to Tabulation',
            'core_concept': 'Break problem into overlapping subproblems, solve each once, reuse results',
            'key_insight': 'Start with recursion, add memoization, then convert to bottom-up DP',
            'sub_patterns': '''
### Pattern 1: 1D DP (Fibonacci, House Robber, Jump Game)
### Pattern 2: 2D DP (Grid Paths, Edit Distance, LCS)
### Pattern 3: DP on Strings (Palindrome, Word Break)
### Pattern 4: DP on Stocks (Buy/Sell with Constraints)
''',
            'learning_path': '''Climbing Stairs → House Robber → Coin Change → Edit Distance → Stock Trading''',
            'common_pitfalls': '''1. Wrong base case 2. Wrong state transition 3. Not considering all previous states 4. Space not optimized''',
            'testing_strategy': '''Test: base cases, small inputs, edge values, impossible cases''',
            'templates': '''
```python
# Top-down (Memoization)
def dp(i, memo={}):
    if i in memo:
        return memo[i]
    if base_case:
        return base_value
    memo[i] = recurrence_relation
    return memo[i]

# Bottom-up (Tabulation)
dp = [0] * (n + 1)
dp[0] = base_value
for i in range(1, n + 1):
    dp[i] = recurrence_relation
return dp[n]
```
''',
            'mastery_tips': '''1. Define state 2. Find recurrence 3. Identify base cases 4. Add memoization 5. Optimize space'''
        },

        'BST-Binary-Search-Tree': {
            'subtitle': '## Leverage In-Order Traversal = Sorted Sequence',
            'core_concept': 'BST property: left < root < right. In-order traversal gives sorted order.',
            'key_insight': 'Use BST property to prune search space. In-order gives sorted sequence.',
            'sub_patterns': '''
### Pattern 1: BST Search (O(log n) average, O(n) worst)
### Pattern 2: In-Order Traversal (Iterative & Recursive)
### Pattern 3: BST Validation
### Pattern 4: Range Queries
''',
            'learning_path': '''Validate BST → Kth Smallest → BST Iterator → Range Sum''',
            'common_pitfalls': '''1. Not handling duplicates 2. Wrong in-order logic 3. Not using BST property 4. Treating as regular tree''',
            'testing_strategy': '''Test: null, single, left-skewed, right-skewed, balanced, with duplicates''',
            'templates': '''
```python
# In-order iterative
def inorder_iterative(root):
    stack, result = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        result.append(curr.val)
        curr = curr.right
    return result
```
''',
            'mastery_tips': '''Remember: in-order = sorted. Use BST property to skip branches.'''
        },

        'Palindrome': {
            'subtitle': '## Expand from Center vs Two Pointers',
            'core_concept': 'Check symmetry using expand-from-center or two-pointer techniques',
            'key_insight': 'Two pointers from edges or expand from each possible center',
            'sub_patterns': '''
### Pattern 1: Two Pointers from Edges (Verification)
### Pattern 2: Expand from Center (Finding All)
### Pattern 3: DP for Palindrome Substrings
### Pattern 4: Manacher's Algorithm (Advanced)
''',
            'learning_path': '''Valid Palindrome → Longest Palindromic Substring → Palindrome Partitioning''',
            'common_pitfalls': '''1. Not handling even/odd length 2. Case sensitivity 3. Special characters 4. Empty string''',
            'testing_strategy': '''Test: empty, single, even length, odd length, no palindrome, all same''',
            'templates': '''
```python
# Expand from center
def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

# Two pointers
def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```
''',
            'mastery_tips': '''Expand from every index (both odd and even centers). Two pointers for validation.'''
        },

        'Parentheses': {
            'subtitle': '## Stack for Matching & Counting for Validation',
            'core_concept': 'Use stack for matching pairs, counter for simple validation',
            'key_insight': 'Stack tracks opening brackets, counter tracks balance',
            'sub_patterns': '''
### Pattern 1: Valid Parentheses (Stack)
### Pattern 2: Remove Invalid Parentheses (BFS or Backtracking)
### Pattern 3: Minimum Add/Remove (Counter + Stack)
### Pattern 4: Generate Parentheses (Backtracking)
''',
            'learning_path': '''Valid Parentheses → Minimum Remove → Minimum Add → Generate Parentheses''',
            'common_pitfalls': '''1. Not checking stack empty 2. Wrong matching logic 3. Not handling edge cases 4. Counter overflow''',
            'testing_strategy': '''Test: empty, single, balanced, unbalanced, nested, interleaved''',
            'templates': '''
```python
# Stack matching
def is_valid(s):
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}
    for char in s:
        if char in pairs:
            stack.append(char)
        else:
            if not stack or pairs[stack.pop()] != char:
                return False
    return len(stack) == 0
```
''',
            'mastery_tips': '''Stack for matching pairs. Counter for balance. Always check empty before pop.'''
        },

        'String': {
            'subtitle': '## StringBuilder, Two Pointers, & Pattern Matching',
            'core_concept': 'String manipulation using efficient techniques and pattern recognition',
            'key_insight': 'Use StringBuilder for concatenation, two pointers for reversal, KMP for pattern matching',
            'sub_patterns': '''
### Pattern 1: String Parsing & Transformation
### Pattern 2: Pattern Matching (KMP, Rabin-Karp)
### Pattern 3: String Compression & Encoding
### Pattern 4: Anagrams & Permutations
''',
            'learning_path': '''Reverse String → Add Strings → String to Integer → Group Anagrams''',
            'common_pitfalls': '''1. String immutability 2. Not handling empty 3. Unicode issues 4. Case sensitivity''',
            'testing_strategy': '''Test: empty, single char, spaces, special chars, unicode, very long''',
            'templates': '''
```python
# Use list for mutable string
chars = list(s)
# ... modify
result = ''.join(chars)

# Two pointers for reversal
def reverse(s):
    left, right = 0, len(s) - 1
    s = list(s)
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)
```
''',
            'mastery_tips': '''Strings are immutable in Python. Use list for modifications. Join at end.'''
        },

        'Math-Compute': {
            'subtitle': '## Mathematical Properties & Number Theory',
            'core_concept': 'Leverage mathematical properties for optimal solutions',
            'key_insight': 'Look for formulas, patterns, and mathematical properties before brute force',
            'sub_patterns': '''
### Pattern 1: Number Operations (Pow, GCD, Prime)
### Pattern 2: Digit Manipulation
### Pattern 3: Mathematical Formulas
### Pattern 4: Bit Manipulation
''',
            'learning_path': '''Power(x, n) → Add Strings → Maximum Swap → Strobogrammatic Number''',
            'common_pitfalls': '''1. Integer overflow 2. Negative numbers 3. Division by zero 4. Floating point precision''',
            'testing_strategy': '''Test: 0, 1, negative, max int, min int, edge values''',
            'templates': '''
```python
# Fast power
def pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    half = pow(x, n // 2)
    if n % 2 == 0:
        return half * half
    else:
        return half * half * x
```
''',
            'mastery_tips': '''Look for O(log n) solutions. Use bit manipulation when possible.'''
        },

        'Design': {
            'subtitle': '## Data Structure Design & API Implementation',
            'core_concept': 'Design custom data structures with optimal time/space complexity',
            'key_insight': 'Balance time complexity of operations with space requirements',
            'sub_patterns': '''
### Pattern 1: Cache Design (LRU, LFU)
### Pattern 2: Stream Processing (Moving Average, Median)
### Pattern 3: Iterator Design (BST Iterator, Flatten)
### Pattern 4: Specialized Data Structures
''',
            'learning_path': '''Moving Average → LRU Cache → BST Iterator → Design Twitter''',
            'common_pitfalls': '''1. Not considering all operations 2. Wrong complexity 3. Not thread-safe 4. Memory leaks''',
            'testing_strategy': '''Test: edge operations, capacity limits, empty, sequential operations''',
            'templates': '''
```python
# LRU Cache pattern
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
```
''',
            'mastery_tips': '''Define all operations first. Analyze complexity. Consider tradeoffs.'''
        }
    }

    # Return default if category not in map
    return info_map.get(category_key, {
        'subtitle': '## Problem Solving Techniques',
        'core_concept': 'Collection of related algorithmic problems',
        'key_insight': 'Master patterns through practice',
        'sub_patterns': 'Various sub-patterns exist in this category.',
        'learning_path': 'Progress from easier to harder problems.',
        'common_pitfalls': '1. Not testing edge cases\n2. Missing optimizations\n3. Incorrect complexity analysis',
        'testing_strategy': 'Test with empty input, single element, duplicates, and large inputs',
        'templates': 'See individual problem solutions for templates',
        'mastery_tips': 'Practice consistently, understand why solutions work, and recognize patterns'
    })


def main():
    """Generate comprehensive summaries for all categories."""
    print("Generating comprehensive mastery summaries for all 16 categories...\n")

    categories = [
        'Array-Hashing',
        'BST-Binary-Search-Tree',
        'Binary-Search',
        'Design',
        'Dynamic-Programming',
        'Graph-DFS-BFS',
        'Heap-Priority-Queue',
        'Linked-List',
        'Math-Compute',
        'Palindrome',
        'Parentheses',
        'Sliding-Window',
        'Stack',
        'String',
        'Tree',
        'Two-Pointers'
    ]

    for category in categories:
        category_path = os.path.join(BASE_DIR, category)
        if not os.path.exists(category_path):
            print(f"⚠ Skipping {category} - directory not found")
            continue

        problems = read_problems(category_path)
        if not problems:
            print(f"⚠ Skipping {category} - no problems found")
            continue

        # Generate summary filename
        summary_name = category.lower().replace('-', '_') + '_summary.md'
        output_path = os.path.join(category_path, summary_name)

        # Use category name for display
        display_name = category.replace('-', ' ')

        generate_summary(category, display_name, problems, output_path)
        print(f"✓ Generated {category}/{summary_name} ({len(problems)} problems)")

    print(f"\n✅ Complete! Generated comprehensive summaries for all {len(categories)} categories!")


if __name__ == '__main__':
    main()
