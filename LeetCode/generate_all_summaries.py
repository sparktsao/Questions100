#!/usr/bin/env python3
"""
Generate comprehensive summary documents for all 16 categories.
This script will be executed to create detailed comparison summaries.
"""

import os
import glob

BASE_DIR = '/Users/sparkt/2026C/Questions100/LeetCode'

CATEGORIES = [
    'Parentheses',
    'Palindrome',
    'BST-Binary-Search-Tree',
    'Binary-Search',
    'Two-Pointers',
    'Math-Compute',
    'Heap-Priority-Queue',
    'Tree',
    'Graph-DFS-BFS',
    'Linked-List',
    'Stack',
    'Sliding-Window',
    'Array-Hashing',
    'Dynamic-Programming',
    'Design',
    'String'
]

def get_problems_in_category(category):
    """Get all problem files in a category."""
    pattern = os.path.join(BASE_DIR, category, '[0-9]*.md')
    files = sorted(glob.glob(pattern))
    return files

def extract_problem_info(filepath):
    """Extract basic info from problem file."""
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()

        title = lines[0].replace('#', '').strip() if lines else 'Unknown'
        num = os.path.basename(filepath)[:3]

        difficulty = 'MEDIUM'
        for line in lines[:15]:
            if '**Difficulty:**' in line:
                difficulty = line.split('**Difficulty:**')[1].strip()
                break

        return {
            'num': num,
            'title': title,
            'difficulty': difficulty,
            'filepath': filepath
        }
    except:
        return None

def main():
    """Main execution."""
    print("=" * 60)
    print("GENERATING CATEGORY SUMMARIES")
    print("=" * 60)
    print()

    for category in CATEGORIES:
        problems = get_problems_in_category(category)

        if not problems:
            print(f"⚠️  {category}: No problems found")
            continue

        print(f"📂 {category}: {len(problems)} problems")
        for prob_file in problems:
            info = extract_problem_info(prob_file)
            if info:
                print(f"   {info['num']}: {info['title']} ({info['difficulty']})")
        print()

    print("=" * 60)
    print(f"✓ Found {len(CATEGORIES)} categories")
    print("=" * 60)
    print()
    print("Note: Detailed summaries will be created manually")
    print("      focusing on problem progression and differences.")

if __name__ == '__main__':
    main()
