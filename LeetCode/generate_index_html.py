#!/usr/bin/env python3
"""
Generate comprehensive index.html with 16 categories and detailed tables.
"""

import os
import glob
import json
import re

BASE_DIR = '/Users/sparkt/2026C/Questions100/LeetCode'

CATEGORY_INFO = {
    'Parentheses': {
        'desc': 'Parentheses validation, balancing, and removal',
        'icon': '📚',
        'key_diff': 'Stack-based tracking, different removal strategies'
    },
    'Palindrome': {
        'desc': 'Palindrome detection and manipulation',
        'icon': '🔄',
        'key_diff': 'Two-pointers vs DP, string modification allowed'
    },
    'BST-Binary-Search-Tree': {
        'desc': 'Binary Search Tree leveraging BST properties',
        'icon': '🌲',
        'key_diff': 'In-order traversal, BST property pruning'
    },
    'Binary-Search': {
        'desc': 'Binary search on arrays and search spaces',
        'icon': '🔍',
        'key_diff': 'Search target vs search answer space'
    },
    'Two-Pointers': {
        'desc': 'Two-pointer technique for optimal solutions',
        'icon': '👉',
        'key_diff': 'Same direction vs opposite direction pointers'
    },
    'Math-Compute': {
        'desc': 'Mathematical computations and operations',
        'icon': '🔢',
        'key_diff': 'Iterative vs recursive, carry handling'
    },
    'Heap-Priority-Queue': {
        'desc': 'Heap-based problems for efficient access',
        'icon': '⛰️',
        'key_diff': 'Min heap vs max heap vs dual heap'
    },
    'Tree': {
        'desc': 'General binary tree problems and traversals',
        'icon': '🌳',
        'key_diff': 'DFS vs BFS, pre/in/post-order, level-order'
    },
    'Graph-DFS-BFS': {
        'desc': 'Graph traversal and path finding',
        'icon': '🕸️',
        'key_diff': 'DFS for cycles, BFS for shortest path'
    },
    'Linked-List': {
        'desc': 'Linked list manipulation and operations',
        'icon': '🔗',
        'key_diff': 'Dummy node, two-pointer, in-place modification'
    },
    'Stack': {
        'desc': 'Stack-based sequential processing',
        'icon': '📚',
        'key_diff': 'Monotonic stack vs regular stack, what to store'
    },
    'Sliding-Window': {
        'desc': 'Sliding window for subarray/substring problems',
        'icon': '🪟',
        'key_diff': 'Fixed size vs variable size window'
    },
    'Array-Hashing': {
        'desc': 'Array operations and hash table lookups',
        'icon': '🗂️',
        'key_diff': 'Prefix sum, hash for O(1) lookup, sorting'
    },
    'Dynamic-Programming': {
        'desc': 'DP with optimal substructure',
        'icon': '📊',
        'key_diff': '1D vs 2D DP, top-down vs bottom-up'
    },
    'Design': {
        'desc': 'Data structure design problems',
        'icon': '🛠️',
        'key_diff': 'Trade-offs between time/space complexity'
    },
    'String': {
        'desc': 'String manipulation and parsing',
        'icon': '📝',
        'key_diff': 'In-place vs new string, validation vs parsing'
    }
}

def extract_metadata(filepath):
    """Extract comprehensive metadata from markdown file."""
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()

        # Extract from first 20 lines
        title = lines[0].replace('#', '').strip() if lines else 'Unknown'
        difficulty = 'MEDIUM'
        frequency = 'N/A'
        categories = ''
        time_complex = ''
        space_complex = ''

        for line in lines[:30]:
            if '**Difficulty:**' in line:
                difficulty = line.split('**Difficulty:**')[1].strip()
            elif '**Frequency:**' in line:
                frequency = line.split('**Frequency:**')[1].strip()
            elif '**Primary Topics:**' in line or '**Categories:**' in line:
                categories = line.split('**')[2].split(':')[1].strip() if ':**' in line else ''
            elif '**Time:' in line or 'Time:' in line:
                time_complex = re.search(r'O\([^\)]+\)', line)
                time_complex = time_complex.group(0) if time_complex else ''
            elif '**Space:' in line or 'Space:' in line:
                space_complex = re.search(r'O\([^\)]+\)', line)
                space_complex = space_complex.group(0) if space_complex else ''

        # Extract number
        filename = os.path.basename(filepath)
        num = filename[:3]

        # Clean title
        if title.startswith(num):
            title = title[len(num):].lstrip('.').strip()

        return {
            'num': num,
            'title': title,
            'difficulty': difficulty,
            'frequency': frequency,
            'categories': categories,
            'time': time_complex,
            'space': space_complex,
            'filename': filename
        }
    except Exception as e:
        print(f"Error extracting metadata from {filepath}: {e}")
        return None

def generate_html():
    """Generate comprehensive index.html."""

    # Collect all problems by category
    categories_data = {}

    for category in sorted(CATEGORY_INFO.keys()):
        category_path = os.path.join(BASE_DIR, category)
        if not os.path.exists(category_path):
            continue

        files = sorted(glob.glob(os.path.join(category_path, '[0-9]*.md')))
        problems = []

        for filepath in files:
            metadata = extract_metadata(filepath)
            if metadata:
                problems.append(metadata)

        if problems:
            categories_data[category] = problems

    # Generate HTML
    html = generate_html_content(categories_data)

    # Write to file
    output_path = os.path.join(BASE_DIR, 'index.html')
    with open(output_path, 'w') as f:
        f.write(html)

    print(f"✓ Generated {output_path}")
    print(f"  Total categories: {len(categories_data)}")
    print(f"  Total problems: {sum(len(p) for p in categories_data.values())}")

def generate_html_content(categories_data):
    """Generate HTML content."""

    # Build category sections
    category_sections = ''
    category_nav = ''

    for i, (category, problems) in enumerate(sorted(categories_data.items())):
        info = CATEGORY_INFO.get(category, {})
        icon = info.get('icon', '📁')
        desc = info.get('desc', '')
        key_diff = info.get('key_diff', '')

        # Category navigation
        category_nav += f'''
            <div class="category-card" onclick="scrollToCategory('{category}')">
                <div class="category-icon">{icon}</div>
                <div class="category-name">{category.replace('-', ' ')}</div>
                <div class="category-count">{len(problems)} problems</div>
            </div>
        '''

        # Problem rows
        problem_rows = ''
        for prob in problems:
            difficulty_class = prob['difficulty'].lower()
            problem_rows += f'''
                <tr>
                    <td class="num-col">{prob['num']}</td>
                    <td class="title-col">
                        <a href="{category}/{prob['filename']}" class="problem-link" target="_blank">
                            {prob['title']}
                        </a>
                    </td>
                    <td class="diff-col">
                        <span class="badge badge-{difficulty_class}">{prob['difficulty']}</span>
                    </td>
                    <td class="freq-col">{prob['frequency']}</td>
                    <td class="tags-col">{prob['categories']}</td>
                    <td class="complex-col">{prob['time']}</td>
                    <td class="complex-col">{prob['space']}</td>
                </tr>
            '''

        # Category section
        category_sections += f'''
            <section id="{category}" class="category-section">
                <div class="category-header">
                    <div class="category-title">
                        <span class="category-icon-large">{icon}</span>
                        <h2>{category.replace('-', ' ')}</h2>
                        <span class="problem-count">{len(problems)} problems</span>
                    </div>
                    <div class="category-description">
                        <strong>Focus:</strong> {desc}
                    </div>
                    <div class="key-differences">
                        <strong>🔑 Key Differences:</strong> {key_diff}
                    </div>
                </div>

                <div class="table-container">
                    <table class="problem-table">
                        <thead>
                            <tr>
                                <th class="num-col">#</th>
                                <th class="title-col">Problem</th>
                                <th class="diff-col">Difficulty</th>
                                <th class="freq-col">Frequency</th>
                                <th class="tags-col">Tags</th>
                                <th class="complex-col">Time</th>
                                <th class="complex-col">Space</th>
                            </tr>
                        </thead>
                        <tbody>
                            {problem_rows}
                        </tbody>
                    </table>
                </div>
            </section>
        '''

    # Complete HTML template
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeetCode 100 Problems - Category View</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }}

        .header {{
            text-align: center;
            color: white;
            padding: 40px 20px;
            margin-bottom: 30px;
        }}

        .header h1 {{
            font-size: 3em;
            margin-bottom: 10px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        }}

        .header .subtitle {{
            font-size: 1.2em;
            opacity: 0.95;
        }}

        .stats-bar {{
            background: white;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
            text-align: center;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
        }}

        .stats-bar .stat {{
            display: inline-block;
            margin: 0 30px;
            font-size: 1.1em;
        }}

        .stats-bar .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #667eea;
            display: block;
        }}

        .category-nav {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin-bottom: 30px;
        }}

        .category-card {{
            background: white;
            padding: 20px;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }}

        .category-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 8px 25px rgba(0,0,0,0.15);
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}

        .category-icon {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}

        .category-name {{
            font-weight: 600;
            font-size: 1em;
            margin-bottom: 5px;
        }}

        .category-count {{
            font-size: 0.9em;
            opacity: 0.7;
        }}

        .category-section {{
            background: white;
            border-radius: 12px;
            margin-bottom: 30px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.15);
            overflow: hidden;
        }}

        .category-header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
        }}

        .category-title {{
            display: flex;
            align-items: center;
            gap: 15px;
            margin-bottom: 15px;
        }}

        .category-icon-large {{
            font-size: 2.5em;
        }}

        .category-title h2 {{
            font-size: 2em;
            margin: 0;
        }}

        .problem-count {{
            background: rgba(255,255,255,0.2);
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.9em;
        }}

        .category-description {{
            font-size: 1.1em;
            margin-bottom: 10px;
            opacity: 0.95;
        }}

        .key-differences {{
            background: rgba(255,255,255,0.15);
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 1em;
            margin-top: 15px;
        }}

        .table-container {{
            padding: 20px;
            overflow-x: auto;
        }}

        .problem-table {{
            width: 100%;
            border-collapse: collapse;
        }}

        .problem-table th {{
            background: #f5f5f5;
            padding: 15px 10px;
            text-align: left;
            font-weight: 600;
            color: #333;
            border-bottom: 2px solid #667eea;
            position: sticky;
            top: 0;
            z-index: 10;
        }}

        .problem-table td {{
            padding: 15px 10px;
            border-bottom: 1px solid #e0e0e0;
        }}

        .problem-table tr:hover {{
            background: #f9f9f9;
        }}

        .num-col {{
            width: 60px;
            text-align: center;
            font-weight: 600;
            color: #667eea;
        }}

        .title-col {{
            min-width: 300px;
        }}

        .problem-link {{
            color: #333;
            text-decoration: none;
            font-weight: 500;
            border-bottom: 2px solid transparent;
            transition: all 0.3s;
        }}

        .problem-link:hover {{
            color: #667eea;
            border-bottom-color: #667eea;
        }}

        .diff-col {{
            width: 100px;
            text-align: center;
        }}

        .badge {{
            display: inline-block;
            padding: 5px 12px;
            border-radius: 12px;
            font-size: 11px;
            font-weight: 700;
            text-transform: uppercase;
        }}

        .badge-easy {{
            background: #d4edda;
            color: #155724;
        }}

        .badge-medium {{
            background: #fff3cd;
            color: #856404;
        }}

        .badge-hard {{
            background: #f8d7da;
            color: #721c24;
        }}

        .freq-col {{
            width: 100px;
            text-align: center;
            font-weight: 600;
            color: #764ba2;
        }}

        .tags-col {{
            min-width: 200px;
            font-size: 0.9em;
            color: #666;
        }}

        .complex-col {{
            width: 120px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: #2196F3;
            text-align: center;
        }}

        .back-to-top {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #667eea;
            color: white;
            width: 50px;
            height: 50px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            transition: all 0.3s;
            font-size: 1.5em;
        }}

        .back-to-top:hover {{
            background: #5568d3;
            transform: translateY(-5px);
        }}

        @media (max-width: 768px) {{
            .header h1 {{
                font-size: 2em;
            }}

            .category-nav {{
                grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                gap: 10px;
            }}

            .stats-bar .stat {{
                display: block;
                margin: 10px 0;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🎯 LeetCode 100 Problems</h1>
        <p class="subtitle">Organized by Category | Click to Navigate</p>
    </div>

    <div class="stats-bar">
        <div class="stat">
            <span class="stat-number">{len(categories_data)}</span>
            <span>Categories</span>
        </div>
        <div class="stat">
            <span class="stat-number">{sum(len(p) for p in categories_data.values())}</span>
            <span>Problems</span>
        </div>
        <div class="stat">
            <span class="stat-number">100%</span>
            <span>Coverage</span>
        </div>
    </div>

    <div class="category-nav">
        {category_nav}
    </div>

    {category_sections}

    <div class="back-to-top" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">
        ↑
    </div>

    <script>
        function scrollToCategory(categoryId) {{
            const element = document.getElementById(categoryId);
            if (element) {{
                element.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
            }}
        }}
    </script>
</body>
</html>
'''

    return html

if __name__ == '__main__':
    generate_html()
