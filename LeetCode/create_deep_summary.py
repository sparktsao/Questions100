#!/usr/bin/env python3
"""
Create comprehensive, deep-dive category summaries with:
- Sub-pattern identification
- Learning progression
- Common pitfalls and testing strategies
- Code templates
- Mastery insights
"""

import os
import glob
import re
from collections import defaultdict

BASE_DIR = '/Users/sparkt/2026C/Questions100/LeetCode'

# Deep pattern analysis for each category
CATEGORY_ANALYSIS = {
    'Binary-Search': {
        'name': 'Binary Search Mastery',
        'subtitle': 'From Array Search to Answer Space Optimization',
        'core_insight': '''The fundamental insight of binary search is MONOTONICITY - if we can check a condition
and know which half of the search space to eliminate, we can solve in O(log n) time. This applies to:
1. Sorted arrays (traditional)
2. Unsorted arrays with monotonic properties
3. Answer spaces where "if X works, all values > X work"''',

        'sub_patterns': {
            'Classic Binary Search': {
                'description': 'Search for target in explicitly sorted array',
                'when_to_use': 'Array is sorted, looking for specific value or boundaries',
                'examples': ['#042 Find First and Last Position'],
                'template': '''def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:  # NOTE: <=  for exact search
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1''',
                'common_bugs': [
                    'Using < instead of <= (infinite loop or miss last element)',
                    'Not using left + (right - left) // 2 (integer overflow in other languages)',
                    'Forgetting to return after finding target (unnecessary iterations)',
                    'Wrong boundary: right = mid instead of mid - 1'
                ],
                'testing_strategy': '''Test cases:
- Empty array []
- Single element [1]
- Target at start [1,2,3] target=1
- Target at end [1,2,3] target=3
- Target in middle [1,2,3,4,5] target=3
- Target not found [1,3,5] target=2
- Duplicates [1,2,2,2,3] target=2'''
            },

            'Binary Search for Boundaries': {
                'description': 'Find leftmost/rightmost occurrence in sorted array with duplicates',
                'when_to_use': 'Need first or last position of value in sorted array',
                'examples': ['#042 Find First and Last Position'],
                'template': '''def find_left_bound(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # KEY: Keep searching LEFT
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

def find_right_bound(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # KEY: Keep searching RIGHT
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result''',
                'common_bugs': [
                    'Stopping at first match (not continuing search)',
                    'Moving wrong pointer (left vs right after match)',
                    'Not saving result before continuing search',
                    'Using < instead of <= for comparison'
                ],
                'key_insight': '''The critical difference from classic binary search:
AFTER finding target, don't return immediately! Save it and keep searching in
the direction needed (left for first, right for last).'''
            },

            'Binary Search on Implicit Array': {
                'description': 'Search in array with monotonic property but not explicitly sorted',
                'when_to_use': 'Array has peaks/valleys, rotated sorted, or bitonic properties',
                'examples': ['#010 Find Peak Element'],
                'template': '''def find_peak(arr):
    left, right = 0, len(arr) - 1
    while left < right:  # NOTE: < not <= !
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid + 1]:
            # Peak is at mid or to the left
            right = mid  # Keep mid as candidate
        else:
            # Peak is to the right
            left = mid + 1
    return left  # left == right at end''',
                'common_bugs': [
                    'Using left <= right (infinite loop with right = mid)',
                    'Using right = mid - 1 (might skip the peak)',
                    'Not checking mid+1 boundary (index out of bounds)',
                    'Returning mid instead of left/right'
                ],
                'key_insight': '''Template difference: while left < right (not <=)
Because we use right = mid (not mid-1), need < to avoid infinite loop.
This template finds "first occurrence of condition" pattern.'''
            },

            'Binary Search on Answer Space': {
                'description': 'Search for optimal value, not array index. "Minimize maximum" or "Maximize minimum" problems.',
                'when_to_use': '''Problem asks "minimum capacity to...", "minimum speed to...", "maximum weight where...".
Key signal: Not searching IN array, but for a VALUE that satisfies conditions.''',
                'examples': ['#079 Capacity To Ship Packages', '#094 Koko Eating Bananas', '#074 Cutting Ribbons'],
                'template': '''def binary_search_on_answer(problem_constraints):
    """
    Core pattern: Find minimum value that satisfies condition
    OR: Find maximum value that satisfies condition
    """
    def is_valid(candidate_value):
        """
        Check if candidate_value satisfies problem constraints.
        This is O(n) typically - must check all elements.
        """
        # Problem-specific validation logic
        pass

    # Define search space based on problem
    left = minimum_possible_answer
    right = maximum_possible_answer

    while left < right:  # Use < for "minimize" problems
        mid = left + (right - left) // 2

        if is_valid(mid):
            # mid works, try smaller (for minimize problems)
            right = mid
        else:
            # mid doesn't work, need larger value
            left = mid + 1

    return left  # Final answer

# For "maximize" problems, flip the logic:
def binary_search_maximize(problem_constraints):
    def is_valid(candidate_value):
        pass

    left, right = min_val, max_val

    while left < right:
        mid = left + (right - left + 1) // 2  # NOTE: +1 for maximize!

        if is_valid(mid):
            # mid works, try larger
            left = mid  # Use left = mid for maximize
        else:
            # mid doesn't work, need smaller
            right = mid - 1

    return left''',
                'common_bugs': [
                    'Wrong search space bounds (must be [min_possible, max_possible])',
                    'Inefficient is_valid() function (should short-circuit)',
                    'Not using +1 in mid calculation for maximize (infinite loop)',
                    'Confusing minimize vs maximize templates',
                    'Forgetting that is_valid() must be MONOTONIC'
                ],
                'key_insight': '''MENTAL MODEL SHIFT: You're not searching for an index!
You're binary searching over POSSIBLE ANSWERS.

The array defines constraints, but you're searching a conceptual number line:
[1, 2, 3, ..., max_capacity]
     ↑
  Looking for minimum value where is_valid(value) = True

Monotonicity requirement: If value X doesn't work, no value < X works.
                         If value X works, all values > X work.

This is why we can binary search - the condition splits space in half!'''
            }
        },

        'learning_path': [
            {
                'level': 1,
                'title': 'Start: Classic Binary Search',
                'problems': ['#042 Find First and Last Position'],
                'goal': 'Master the basic template with <= comparison',
                'practice': 'Write from scratch 5 times without looking. Test all edge cases.'
            },
            {
                'level': 2,
                'title': 'Boundaries: Left/Right Bound Search',
                'problems': ['#042 (boundary variation)'],
                'goal': 'Understand when to continue searching after finding match',
                'practice': 'Modify classic template to find first/last occurrence. Compare both.'
            },
            {
                'level': 3,
                'title': 'Implicit Monotonicity: Peak Finding',
                'problems': ['#010 Find Peak Element'],
                'goal': 'Recognize monotonic property without explicit sorting',
                'practice': 'Draw array, mark mid, explain why one half can be eliminated'
            },
            {
                'level': 4,
                'title': 'Answer Space: Minimize Problems',
                'problems': ['#094 Koko Eating Bananas'],
                'goal': 'Mental shift from "search in array" to "search for value"',
                'practice': 'Identify: What are we searching for? What is search space? What is is_valid()?'
            },
            {
                'level': 5,
                'title': 'Answer Space: Capacity Problems',
                'problems': ['#079 Capacity To Ship Packages', '#074 Cutting Ribbons'],
                'goal': 'Apply pattern to capacity/resource allocation problems',
                'practice': 'Before coding, write down: [min, max] bounds and is_valid() logic'
            },
            {
                'level': 6,
                'title': 'Advanced: 2D Binary Search',
                'problems': ['#084 Kth Smallest in Sorted Matrix'],
                'goal': 'Combine binary search with 2D array properties',
                'practice': 'Identify what makes the search space monotonic in 2D'
            },
            {
                'level': 7,
                'title': 'Master: Median of Two Sorted Arrays',
                'problems': ['#100 Median of Two Sorted Arrays'],
                'goal': 'Binary search with partition logic and edge cases',
                'practice': 'This is HARD. Study solution, then implement without looking.'
            }
        ],

        'common_errors_across_all': [
            {
                'error': 'Integer overflow in mid calculation',
                'wrong': 'mid = (left + right) // 2',
                'correct': 'mid = left + (right - left) // 2',
                'why': 'In Python not a problem, but in Java/C++ left+right can overflow',
                'test': 'left=2^30, right=2^30 → overflow in some languages'
            },
            {
                'error': 'Off-by-one errors with boundaries',
                'wrong': 'if found: right = mid - 1',
                'correct': 'if found: right = mid (when using while left < right)',
                'why': 'Template choice determines boundary update. Mixing templates causes bugs.',
                'test': 'Array of size 2, target is first element'
            },
            {
                'error': 'Infinite loop with wrong template',
                'wrong': 'while left < right: ... right = mid',
                'correct': 'Match loop condition with boundary update',
                'why': 'left < right requires right = mid (include mid). left <= right requires right = mid - 1',
                'test': 'Run with array [1,2], target=1. Does it terminate?'
            },
            {
                'error': 'Not checking array boundaries',
                'wrong': 'if arr[mid] > arr[mid+1]',
                'correct': 'if mid < len(arr) - 1 and arr[mid] > arr[mid+1]',
                'why': 'mid+1 can go out of bounds when mid = len-1',
                'test': 'Array of size 1'
            }
        ],

        'testing_checklist': '''
## Unit Testing Strategy for Binary Search

### 1. Edge Cases (ALWAYS test these first)
- Empty array: []
- Single element: [1]
- Two elements: [1, 2]
- All same: [5, 5, 5, 5]

### 2. Position Cases
- Target at index 0
- Target at last index
- Target in middle
- Target not present (between elements)
- Target not present (before all)
- Target not present (after all)

### 3. Duplicate Cases (for boundary search)
- All duplicates of target: [2, 2, 2, 2]
- Target at boundaries: [2, 2, 3, 4] or [1, 2, 3, 3]
- Single occurrence: [1, 2, 3]

### 4. For Answer Space Problems
- Minimum possible answer
- Maximum possible answer
- Answer in middle of range
- Impossible case (if applicable)

### 5. Property Testing
Write a test that:
1. Generates random sorted array
2. Picks random target
3. Runs your binary search
4. Verifies result with linear search
5. Repeat 1000 times

```python
import random

def test_binary_search_random():
    for _ in range(1000):
        size = random.randint(0, 100)
        arr = sorted([random.randint(-100, 100) for _ in range(size)])
        target = random.randint(-100, 100)

        result = binary_search(arr, target)
        expected = linear_search(arr, target)

        assert result == expected, f"Failed on arr={arr}, target={target}"
```

### 6. Invariant Checking
Add assertions in your binary search:
```python
def binary_search_with_invariants(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        # Invariant: if target exists, it's in [left, right]
        assert 0 <= left <= len(arr)
        assert -1 <= right < len(arr)
        assert left <= right + 1  # Allow left = right + 1 for termination

        mid = left + (right - left) // 2
        # ... rest of logic
```
''',

        'mastery_insights': [
            {
                'insight': 'Two Completely Different Mental Models',
                'explanation': '''Binary search has TWO distinct use cases that require different thinking:

1. SEARCH IN ARRAY: Find index/position
   - Input: Sorted (or monotonic) array
   - Output: Index or -1
   - Template: Classic binary search

2. SEARCH ON ANSWER: Find optimal value
   - Input: Problem constraints (array defines constraints, not search space)
   - Output: Optimal value (not an index!)
   - Template: Binary search on answer

Many students confuse these. #042 is type 1. #079 and #094 are type 2.
'''
            },
            {
                'insight': 'Why Binary Search Works: The Monotonicity Guarantee',
                'explanation': '''Binary search ONLY works when checking mid tells us which half to eliminate.

For array search: If arr[mid] < target, we know target is in right half.
For answer search: If is_valid(mid) = True, we know all values > mid are also valid.

If this property doesn't hold, binary search fails!

Example where it FAILS:
Array: [3, 1, 4, 1, 5, 9, 2, 6]  ← Not monotonic!
Cannot eliminate half based on arr[mid] comparison.
'''
            },
            {
                'insight': 'Template Choice: < vs <= and When It Matters',
                'explanation': '''Two templates exist for good reasons:

TEMPLATE A (for exact match):
```python
while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
```
Use when: Looking for exact value, need to check all elements.
Boundary update: MUST be mid ± 1 (exclusive)

TEMPLATE B (for condition finding):
```python
while left < right:
    mid = (left + right) // 2
    if condition(mid):
        right = mid  # Keep mid as candidate
    else:
        left = mid + 1
```
Use when: Finding first/last position satisfying condition.
Boundary update: Can include mid (right = mid)

Mixing these causes infinite loops! If using right = mid, MUST use left < right.
'''
            },
            {
                'insight': 'Answer Space Problems: Identifying the Pattern',
                'explanation': '''How to recognize "binary search on answer" problems:

🚨 SIGNALS 🚨
- Problem asks for "minimum value that...", "maximum value where..."
- Keywords: "minimum capacity", "minimum speed", "maximum pages", "kth element"
- Array defines CONSTRAINTS, not the search space
- Brute force would be "try every possible value from min to max"

STEPS TO SOLVE:
1. Identify what you're minimizing/maximizing (this is your "answer")
2. Find bounds: [minimum_possible, maximum_possible]
3. Write is_valid(candidate): checks if candidate satisfies constraints
4. Verify monotonicity: if X works, does X+1 work? (or vice versa)
5. Apply binary search template on [min, max]

Example: "Minimum speed to eat all bananas in H hours"
- Answer: speed (integer from 1 to max(piles))
- is_valid(speed): returns true if can finish with this speed
- Monotonic: if speed K works, speed K+1 also works
- Binary search for smallest K where is_valid(K) = true
'''
            }
        ]
    },

    # Add more categories...
    'Two-Pointers': {
        'name': 'Two Pointers Mastery',
        'subtitle': 'From Simple Traversal to Complex Sliding Windows',
        # Similar deep structure...
    }
}


def read_all_problems(category_path):
    """Read all problem files and extract metadata."""
    files = sorted(glob.glob(os.path.join(category_path, '[0-9]*.md')))
    problems = []

    for filepath in files:
        with open(filepath, 'r') as f:
            content = f.read()
            lines = content.split('\n')

        # Extract metadata
        num = os.path.basename(filepath)[:3]
        title = lines[0].replace('#', '').strip() if lines else 'Unknown'
        if title.startswith(num):
            title = title[len(num):].lstrip('.').strip()

        difficulty = 'MEDIUM'
        frequency = 'N/A'

        for line in lines[:15]:
            if '**Difficulty:**' in line:
                difficulty = line.split('**Difficulty:**')[1].strip()
            elif '**Frequency:**' in line:
                frequency = line.split('**Frequency:**')[1].strip()

        problems.append({
            'num': num,
            'title': title,
            'difficulty': difficulty,
            'frequency': frequency,
            'content': content,
            'filename': os.path.basename(filepath)
        })

    return problems


def generate_comprehensive_summary(category_key, category_path):
    """Generate deep-dive summary with patterns and insights."""

    if category_key not in CATEGORY_ANALYSIS:
        print(f"⚠ Skipping {category_key} - no deep analysis defined yet")
        return

    analysis = CATEGORY_ANALYSIS[category_key]
    problems = read_all_problems(category_path)

    if not problems:
        return

    # Build comprehensive summary
    content = f"# {analysis['name']}\n\n"
    content += f"## {analysis['subtitle']}\n\n"
    content += "---\n\n"

    # Overview
    content += "## 🎯 Category Overview\n\n"
    content += f"**Total Problems:** {len(problems)}\n\n"
    content += f"**Core Insight:**\n{analysis['core_insight']}\n\n"
    content += "---\n\n"

    # Sub-patterns deep dive
    content += "## 📚 Sub-Pattern Deep Dive\n\n"
    content += f"This category has **{len(analysis['sub_patterns'])} distinct sub-patterns**. Master each progressively:\n\n"

    for i, (pattern_name, pattern) in enumerate(analysis['sub_patterns'].items(), 1):
        content += f"### Pattern {i}: {pattern_name}\n\n"
        content += f"**Description:** {pattern['description']}\n\n"
        content += f"**When to Use:** {pattern['when_to_use']}\n\n"
        content += f"**Examples in This Set:** {', '.join(pattern['examples'])}\n\n"

        content += "**Code Template:**\n\n"
        content += f"```python\n{pattern['template']}\n```\n\n"

        content += "**Common Bugs:**\n\n"
        for bug in pattern['common_bugs']:
            content += f"- ❌ {bug}\n"
        content += "\n"

        if 'key_insight' in pattern:
            content += f"**💡 Key Insight:**\n\n{pattern['key_insight']}\n\n"

        if 'testing_strategy' in pattern:
            content += f"**Testing Strategy:**\n\n```\n{pattern['testing_strategy']}\n```\n\n"

        content += "---\n\n"

    # Learning path
    content += "## 🎓 Learning Path: Easiest to Hardest\n\n"
    for step in analysis['learning_path']:
        content += f"### Level {step['level']}: {step['title']}\n\n"
        content += f"**Problems:** {', '.join(step['problems'])}\n\n"
        content += f"**Goal:** {step['goal']}\n\n"
        content += f"**Practice:** {step['practice']}\n\n"
        content += "---\n\n"

    # Common errors
    content += "## ⚠️ Common Errors Across All Patterns\n\n"
    for error_info in analysis['common_errors_across_all']:
        content += f"### {error_info['error']}\n\n"
        content += f"**❌ Wrong:**\n```python\n{error_info['wrong']}\n```\n\n"
        content += f"**✅ Correct:**\n```python\n{error_info['correct']}\n```\n\n"
        content += f"**Why:** {error_info['why']}\n\n"
        content += f"**Test:** {error_info['test']}\n\n"
        content += "---\n\n"

    # Testing checklist
    content += "## ✅ Testing & Verification\n\n"
    content += analysis['testing_checklist']
    content += "\n\n---\n\n"

    # Mastery insights
    content += "## 💎 Mastery Insights\n\n"
    for insight_info in analysis['mastery_insights']:
        content += f"### {insight_info['insight']}\n\n"
        content += f"{insight_info['explanation']}\n\n"
        content += "---\n\n"

    # Problem reference table
    content += "## 📋 Complete Problem Reference\n\n"
    content += "| # | Problem | Difficulty | Frequency | File |\n"
    content += "|---|---------|------------|-----------|------|\n"
    for p in problems:
        content += f"| {p['num']} | {p['title']} | {p['difficulty']} | {p['frequency']} | [{p['filename']}](./{p['filename']}) |\n"
    content += "\n\n"

    content += "---\n\n"
    content += "[← Back to All Categories](../README.md)\n"

    # Write file
    summary_filename = f"{category_key.lower().replace('-', '_')}_MASTERY.md"
    summary_path = os.path.join(category_path, summary_filename)

    with open(summary_path, 'w') as f:
        f.write(content)

    print(f"✓ Generated {category_key}/{summary_filename}")


def main():
    """Generate comprehensive summaries for all defined categories."""
    print("Generating comprehensive mastery guides...\n")

    for category_key in CATEGORY_ANALYSIS.keys():
        category_path = os.path.join(BASE_DIR, category_key)
        if os.path.exists(category_path):
            generate_comprehensive_summary(category_key, category_path)

    print("\n✓ Generated comprehensive mastery guides!")
    print("\nNote: Only categories with deep analysis defined are generated.")
    print("To add more categories, extend CATEGORY_ANALYSIS dictionary.")


if __name__ == '__main__':
    main()
