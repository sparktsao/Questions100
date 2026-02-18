#!/usr/bin/env python3
"""
Generate comprehensive category summary files based on tree_summary.md template.
"""

import os
import glob
import re

BASE_DIR = '/Users/sparkt/2026C/Questions100/LeetCode'

CATEGORIES = {
    'Array-Hashing': {
        'name': 'Array Hashing',
        'overview': 'Array manipulation and hash table problems for efficient lookups.',
        'key_insight': 'Use hash maps for O(1) lookups and prefix sums for range queries.',
        'core_concept': 'Hash maps for constant-time lookups vs array iteration',
    },
    'BST-Binary-Search-Tree': {
        'name': 'BST Binary Search Tree',
        'overview': 'Binary Search Tree specific problems leveraging BST properties.',
        'key_insight': 'In-order traversal gives sorted sequence; leverage BST ordering.',
        'core_concept': 'BST properties (left < root < right) for efficient search/insertion',
    },
    'Binary-Search': {
        'name': 'Binary Search',
        'overview': 'Binary search algorithm applications on arrays and search spaces.',
        'key_insight': 'Reduce search space by half each iteration; requires sorted or monotonic property.',
        'core_concept': 'Divide and conquer on sorted/monotonic spaces',
    },
    'Design': {
        'name': 'Design',
        'overview': 'Data structure and system design problems.',
        'key_insight': 'Balance time/space complexity with clean API design.',
        'core_concept': 'Custom data structures optimized for specific operations',
    },
    'Dynamic-Programming': {
        'name': 'Dynamic Programming',
        'overview': 'Dynamic programming problems with optimal substructure.',
        'key_insight': 'Break into overlapping subproblems; memoize or build bottom-up.',
        'core_concept': 'Optimal substructure + overlapping subproblems = DP',
    },
    'Graph-DFS-BFS': {
        'name': 'Graph DFS BFS',
        'overview': 'Graph problems solved using depth-first search and breadth-first search.',
        'key_insight': 'DFS for paths/cycles, BFS for shortest distances.',
        'core_concept': 'Graph traversal using DFS (stack/recursion) vs BFS (queue)',
    },
    'Heap-Priority-Queue': {
        'name': 'Heap Priority Queue',
        'overview': 'Problems using heaps and priority queues for efficient element access.',
        'key_insight': 'Heaps maintain min/max in O(log n) time; perfect for top-k problems.',
        'core_concept': 'Priority queue for efficient min/max access and updates',
    },
    'Linked-List': {
        'name': 'Linked List',
        'overview': 'Linked list manipulation, traversal, and structural modifications.',
        'key_insight': 'Use slow/fast pointers for cycle detection; dummy nodes simplify edge cases.',
        'core_concept': 'Pointer manipulation for sequential data structures',
    },
    'Math-Compute': {
        'name': 'Math Compute',
        'overview': 'Mathematical computations, number operations, and arithmetic problems.',
        'key_insight': 'Look for mathematical properties and formulas to optimize.',
        'core_concept': 'Mathematical algorithms and number theory',
    },
    'Palindrome': {
        'name': 'Palindrome',
        'overview': 'Problems involving palindrome detection, validation, and string manipulation.',
        'key_insight': 'Expand from center or use two pointers from edges.',
        'core_concept': 'String symmetry and character matching',
    },
    'Parentheses': {
        'name': 'Parentheses',
        'overview': 'Problems involving parentheses validation, balancing, and removal.',
        'key_insight': 'Stack for matching pairs; counter for quick validation.',
        'core_concept': 'Stack-based matching for nested structures',
    },
    'Sliding-Window': {
        'name': 'Sliding Window',
        'overview': 'Sliding window technique for substring/subarray problems.',
        'key_insight': 'Maintain window invariant while expanding/contracting.',
        'core_concept': 'Two pointers maintaining window with specific property',
    },
    'Stack': {
        'name': 'Stack',
        'overview': 'Stack-based problems for parsing, evaluation, and sequential processing.',
        'key_insight': 'LIFO for nested structures, parsing, and backtracking.',
        'core_concept': 'Last-in-first-out for sequential processing',
    },
    'String': {
        'name': 'String',
        'overview': 'String manipulation, parsing, and transformation problems.',
        'key_insight': 'Use StringBuilder for efficiency; consider character arrays.',
        'core_concept': 'String algorithms for pattern matching and transformation',
    },
    'Tree': {
        'name': 'Tree',
        'overview': 'General binary tree problems including traversal, construction, and queries.',
        'key_insight': 'BFS for level information, DFS for paths and subtree properties.',
        'core_concept': 'Binary tree traversal using DFS (recursive/path tracking) vs BFS (level-order/shortest distance)',
    },
    'Two-Pointers': {
        'name': 'Two Pointers',
        'overview': 'Problems solved using two-pointer technique for optimal time complexity.',
        'key_insight': 'Move pointers based on conditions to achieve O(n) time.',
        'core_concept': 'Two pointers moving in same/opposite directions',
    },
}

def extract_metadata(filepath):
    """Extract title, difficulty, frequency, and tags from markdown file."""
    try:
        with open(filepath, 'r') as f:
            content = f.read()
            lines = content.split('\n')

        title = lines[0].replace('#', '').strip() if lines else 'Unknown'
        difficulty = 'MEDIUM'
        frequency = 'N/A'
        tags = []

        for line in lines[:20]:
            if '**Difficulty:**' in line:
                difficulty = line.split('**Difficulty:**')[1].strip()
            elif '**Frequency:**' in line:
                frequency = line.split('**Frequency:**')[1].strip()
            elif '**Tags:**' in line:
                tags_str = line.split('**Tags:**')[1].strip()
                tags = [t.strip() for t in tags_str.split(',')]

        return title, difficulty, frequency, tags, content
    except:
        return 'Unknown', 'MEDIUM', 'N/A', [], ''

def generate_summary(category_path, category_key):
    """Generate comprehensive summary for a category."""
    files = sorted(glob.glob(os.path.join(category_path, '[0-9]*.md')))

    if not files:
        return

    meta = CATEGORIES.get(category_key, {})
    category_name = meta.get('name', category_key.replace('-', ' '))

    # Collect all problem metadata
    problems = []
    for filepath in files:
        filename = os.path.basename(filepath)
        num = filename[:3]
        title, difficulty, frequency, tags, content = extract_metadata(filepath)

        # Clean title
        if title.startswith(num):
            title = title[len(num):].lstrip('.').strip()

        problems.append({
            'num': num,
            'title': title,
            'difficulty': difficulty,
            'frequency': frequency,
            'tags': tags,
            'filename': filename,
            'content': content
        })

    # Count by difficulty
    easy = sum(1 for p in problems if 'EASY' in p['difficulty'].upper())
    medium = sum(1 for p in problems if 'MEDIUM' in p['difficulty'].upper())
    hard = sum(1 for p in problems if 'HARD' in p['difficulty'].upper())

    # Generate content
    content = f"# {category_name} - Comprehensive Analysis\n\n"
    content += f"## 🎯 Category Overview\n\n"
    content += f"**Total Problems:** {len(problems)}\n"
    content += f"**Difficulty Distribution:** Easy ({easy}) • Medium ({medium}) • Hard ({hard})\n"
    content += f"**Core Concept:** {meta.get('core_concept', 'Collection of related algorithmic problems.')}\n\n"
    content += f"**🔑 Key Insight:** {meta.get('key_insight', 'Master the fundamental patterns.')}\n\n"
    content += "---\n\n"

    # Problem progression map
    content += "## 📊 Problem Progression Map\n\n"
    content += "```\n"
    for i, p in enumerate(problems, 1):
        content += f"Level {i}: {p['title']} (#{p['num']}) - {p['difficulty']}\n"
        if i < len(problems):
            content += "    ↓\n"
    content += "```\n\n"
    content += "---\n\n"

    # Problems list
    content += "## 📖 Problems\n\n"

    for i, p in enumerate(problems, 1):
        content += f"### {i}️⃣ **Problem #{p['num']}: {p['title']}** ({p['difficulty']})\n\n"
        content += f"**🎯 Frequency:** {p['frequency']}\n"
        if p['tags']:
            content += f"**🏷️ Tags:** {', '.join(p['tags'])}\n"
        content += f"**📄 [View Problem](./{p['filename']})**\n\n"

        # Try to extract approach/algorithm from content
        approach = extract_approach(p['content'])
        if approach:
            content += f"**Key Approach:**\n{approach}\n\n"

        content += "---\n\n"

    # Summary table
    content += "## 🎨 Summary Table\n\n"
    content += "| # | Problem | Difficulty | Frequency |\n"
    content += "|---|---------|------------|----------|\n"
    for p in problems:
        content += f"| {p['num']} | [{p['title']}](./{p['filename']}) | {p['difficulty']} | {p['frequency']} |\n"
    content += "\n---\n\n"

    # Key concepts
    content += "## 💡 Key Concepts\n\n"
    content += f"- {meta.get('overview', 'Collection of algorithmic problems')}\n"
    content += f"- {meta.get('key_insight', 'Focus on pattern recognition and optimization')}\n"
    content += "- Practice progressing from easier to harder problems\n"
    content += "- Master the core technique before moving to variations\n\n"
    content += "---\n\n"

    content += "[← Back to All Categories](../README.md)\n"

    # Write summary file
    summary_filename = f"{category_key.lower().replace('-', '_')}_summary.md"
    summary_path = os.path.join(category_path, summary_filename)
    with open(summary_path, 'w') as f:
        f.write(content)

    print(f"✓ Generated {category_key}/{summary_filename}")

def extract_approach(content):
    """Extract algorithm/approach section from problem content."""
    lines = content.split('\n')
    in_approach = False
    approach_lines = []

    for line in lines:
        if '## Algorithm' in line or '## Approach' in line or '## Solution' in line:
            in_approach = True
            continue
        if in_approach:
            if line.startswith('##'):
                break
            if line.strip():
                approach_lines.append(line)
            if len(approach_lines) >= 5:  # Limit to first few lines
                break

    return '\n'.join(approach_lines[:5]) if approach_lines else ''

def main():
    """Generate all comprehensive summaries."""
    print(f"Generating comprehensive summaries for {len(CATEGORIES)} categories...\n")

    for category_key in sorted(CATEGORIES.keys()):
        category_path = os.path.join(BASE_DIR, category_key)
        if os.path.exists(category_path):
            generate_summary(category_path, category_key)

    print(f"\n✓ Generated all comprehensive summaries!")

if __name__ == '__main__':
    main()
