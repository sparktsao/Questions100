#!/usr/bin/env python3
"""
Reorganize LeetCode questions into category folders based on problem characteristics.
"""

import os
import shutil
import re

BASE_DIR = '/Users/sparkt/2026C/Questions100/LeetCode'

# Define categorization rules with priority
CATEGORIZATION = {
    'Parentheses': {
        'patterns': ['parenthes', 'bracket'],
        'questions': ['001', '020', '052', '056']
    },
    'Palindrome': {
        'patterns': ['palindrom'],
        'questions': ['004', '029', '057', '083', '096']
    },
    'BST-Binary-Search-Tree': {
        'patterns': ['binary search tree', 'bst'],
        'questions': ['027', '051', '060', '092']
    },
    'Binary-Search': {
        'patterns': ['binary search'],
        'exclude': ['tree', 'bst'],
        'questions': ['010', '041', '042', '074', '079', '084', '094', '100']
    },
    'Two-Pointers': {
        'patterns': ['two pointer'],
        'questions': ['002', '004', '029', '030', '033', '044', '065', '073', '078', '088']
    },
    'Math-Compute': {
        'patterns': ['pow', 'add string', 'add two integer', 'maximum swap', '^math'],
        'questions': ['021', '050', '072', '085']
    },
    'Heap-Priority-Queue': {
        'patterns': ['heap', 'priority queue', 'kth largest', 'kth smallest', 'median'],
        'questions': ['006', '012', '015', '019', '034', '082', '091']
    },
    'Linked-List': {
        'patterns': ['linked list'],
        'questions': ['019', '032', '045', '054', '064']
    },
    'Stack': {
        'patterns': ['stack'],
        'questions': ['008', '020', '035', '049', '051', '093', '098']
    },
    'Sliding-Window': {
        'patterns': ['sliding window'],
        'questions': ['037', '040', '059', '068', '080', '090']
    },
    'Tree': {
        'patterns': [r'\btree\b', 'binary tree'],
        'exclude': ['bst', 'binary search tree'],
        'questions': ['003', '005', '007', '009', '011', '013', '014', '061', '066', '076']
    },
    'Graph-DFS-BFS': {
        'patterns': ['graph', 'dfs', 'bfs', 'depth-first', 'breadth-first', 'topological'],
        'questions': ['025', '031', '036', '038', '053', '063', '070', '081', '086']
    },
    'Array-Hashing': {
        'patterns': ['hash table', 'prefix sum', 'subarray sum', 'interval'],
        'questions': ['016', '017', '022', '023', '024', '026', '062', '069', '071', '077', '087', '089']
    },
    'Dynamic-Programming': {
        'patterns': ['dynamic programming', r'\bdp\b'],
        'questions': ['018', '055', '075', '083', '099']
    },
    'Design': {
        'patterns': ['design', 'lru', 'iterator', 'data stream', 'random pick'],
        'questions': ['039', '048', '091']
    },
    'String': {
        'patterns': ['atoi', 'text justification', 'goat latin', 'diagonal traverse', 'missing ranges'],
        'questions': ['043', '046', '047', '058', '067', '095', '097']
    }
}

def read_question_metadata(filepath):
    """Read first 100 lines of a question file to extract metadata."""
    try:
        with open(filepath, 'r') as f:
            content = f.read(3000).lower()
        return content
    except:
        return ""

def categorize_question(num, filename, content):
    """Determine category for a question."""
    for category, rules in CATEGORIZATION.items():
        if num in rules.get('questions', []):
            return category

    for category, rules in CATEGORIZATION.items():
        patterns = rules.get('patterns', [])
        excludes = rules.get('exclude', [])

        for pattern in patterns:
            if re.search(pattern, content):
                if any(re.search(excl, content) for excl in excludes):
                    continue
                return category

    return None

def get_all_question_files():
    """Get all question markdown files."""
    files = []
    for f in os.listdir(BASE_DIR):
        if f.endswith('.md') and f[0].isdigit() and f != 'README.md':
            files.append(f)
    return sorted(files)

def move_questions():
    """Analyze and move all question files to categories."""
    files = get_all_question_files()

    moved_count = {}
    unmapped = []

    print(f"Processing {len(files)} question files...\n")

    for filename in files:
        num = filename[:3]
        filepath = os.path.join(BASE_DIR, filename)
        content = read_question_metadata(filepath)
        category = categorize_question(num, filename, content)

        if category:
            dest_dir = os.path.join(BASE_DIR, category)
            dest_path = os.path.join(dest_dir, filename)
            shutil.move(filepath, dest_path)
            moved_count[category] = moved_count.get(category, 0) + 1
            print(f"✓ {filename} → {category}/")
        else:
            unmapped.append(filename)
            print(f"? {filename} → (unmapped)")

    print("\n" + "="*60)
    print("REORGANIZATION SUMMARY")
    print("="*60)
    for category in sorted(moved_count.keys()):
        print(f"  {category:<30} {moved_count[category]:>3} files")

    if unmapped:
        print(f"\n⚠ Unmapped files: {len(unmapped)}")
        for f in unmapped:
            print(f"  - {f}")

    total = sum(moved_count.values())
    print(f"\n✓ Successfully moved {total} files into {len(moved_count)} categories")

    return moved_count

if __name__ == '__main__':
    result = move_questions()
