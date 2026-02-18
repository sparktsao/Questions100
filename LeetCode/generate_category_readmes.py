#!/usr/bin/env python3
"""
Generate README.md files for each category folder.
"""

import os
import glob
import re

BASE_DIR = '/Users/sparkt/2026C/Questions100/LeetCode'

CATEGORY_DESCRIPTIONS = {
    'Parentheses': 'Problems involving parentheses validation, balancing, and removal.',
    'Palindrome': 'Problems involving palindrome detection, validation, and string manipulation.',
    'BST-Binary-Search-Tree': 'Binary Search Tree specific problems leveraging BST properties.',
    'Binary-Search': 'Binary search algorithm applications on arrays and search spaces.',
    'Two-Pointers': 'Problems solved using two-pointer technique for optimal time complexity.',
    'Math-Compute': 'Mathematical computations, number operations, and arithmetic problems.',
    'Heap-Priority-Queue': 'Problems using heaps and priority queues for efficient element access.',
    'Tree': 'General binary tree problems including traversal, construction, and queries.',
    'Graph-DFS-BFS': 'Graph problems solved using depth-first search and breadth-first search.',
    'Linked-List': 'Linked list manipulation, traversal, and structural modifications.',
    'Stack': 'Stack-based problems for parsing, evaluation, and sequential processing.',
    'Sliding-Window': 'Sliding window technique for substring/subarray problems.',
    'Array-Hashing': 'Array manipulation and hash table problems for efficient lookups.',
    'Dynamic-Programming': 'Dynamic programming problems with optimal substructure.',
    'Design': 'Data structure and system design problems.',
    'String': 'String manipulation, parsing, and transformation problems.'
}

def extract_metadata(filepath):
    """Extract title, difficulty, and frequency from markdown file."""
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()

        title = lines[0].replace('#', '').strip() if lines else 'Unknown'
        difficulty = 'MEDIUM'
        frequency = 'N/A'

        for line in lines[:15]:
            if '**Difficulty:**' in line:
                difficulty = line.split('**Difficulty:**')[1].strip()
            elif '**Frequency:**' in line:
                frequency = line.split('**Frequency:**')[1].strip()

        return title, difficulty, frequency
    except:
        return 'Unknown', 'MEDIUM', 'N/A'

def generate_category_readme(category_path, category_name):
    """Generate README for a category folder."""
    files = sorted(glob.glob(os.path.join(category_path, '[0-9]*.md')))

    if not files:
        return

    description = CATEGORY_DESCRIPTIONS.get(category_name, 'Collection of related problems.')

    content = f"# {category_name.replace('-', ' ')}\n\n"
    content += f"**Description:** {description}\n\n"
    content += f"**Total Problems:** {len(files)}\n\n"
    content += "---\n\n"
    content += "## Problems\n\n"
    content += "| # | Problem | Difficulty | Frequency |\n"
    content += "|---|---------|------------|----------|\n"

    for filepath in files:
        filename = os.path.basename(filepath)
        num = filename[:3]
        title, difficulty, frequency = extract_metadata(filepath)

        if title.startswith(num):
            title = title[len(num):].lstrip('.').strip()

        content += f"| {num} | [{title}](./{filename}) | {difficulty} | {frequency} |\n"

    content += "\n---\n\n"
    content += "[← Back to All Categories](../README.md)\n"

    readme_path = os.path.join(category_path, 'README.md')
    with open(readme_path, 'w') as f:
        f.write(content)

    print(f"✓ Generated {category_name}/README.md ({len(files)} problems)")

def main():
    """Generate all category READMEs."""
    categories = sorted([d for d in os.listdir(BASE_DIR)
                        if os.path.isdir(os.path.join(BASE_DIR, d))
                        and d[0].isupper()])

    print(f"Generating README files for {len(categories)} categories...\n")

    for category in categories:
        category_path = os.path.join(BASE_DIR, category)
        generate_category_readme(category_path, category)

    print(f"\n✓ Generated {len(categories)} README files")

if __name__ == '__main__':
    main()
