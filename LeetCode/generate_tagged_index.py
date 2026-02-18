#!/usr/bin/env python3
"""
Generate comprehensive index.html with problem-specific tags based on key differences.
"""

import os
import glob
import json
import re

BASE_DIR = '/Users/sparkt/2026C/Questions100/LeetCode'
# GitHub repository URL for blob links
GITHUB_REPO = 'https://github.com/sparktsao/Questions100/blob/main/LeetCode'


# Problem-specific tags highlighting their unique approach
PROBLEM_TAGS = {
    # Parentheses - Stack-based tracking, different removal strategies
    '001': 'Stack+Indices',
    '020': 'Stack+Matching',
    '052': 'Greedy Count',
    '056': 'BFS+Removal',

    # Palindrome - Two-pointers vs DP, string modification allowed
    '004': '2-Ptr, 1 Skip',
    '029': '2-Ptr, Validation',
    '057': 'Expand Center',
    '083': 'DP, K Deletions',
    '096': 'Expand+DP',

    # BST - In-order traversal, BST property pruning
    '027': 'DFS+Pruning',
    '051': 'Iterator+Stack',
    '060': 'Binary Search',
    '092': 'Inorder+Counter',

    # Binary Search - Search target vs search answer space
    '010': 'Search Peak',
    '041': 'Search Answer',
    '042': 'Dual Binary Search',
    '074': 'Search Answer',
    '079': 'Search Capacity',
    '084': 'Search Value Range',
    '094': 'Search Speed',
    '100': 'Search Partition',

    # Two-Pointers - Same direction vs opposite direction
    '002': 'Same Dir',
    '028': 'Same Dir',
    '029': 'Opposite Dir',
    '030': 'Same Dir+Greedy',
    '033': 'Opposite Dir',
    '044': 'Opposite Dir',
    '065': 'Opposite Dir',
    '073': 'Opposite Dir+Greedy',
    '078': 'Opposite Dir',
    '088': 'Same Dir',

    # Math-Compute - Iterative vs recursive, carry handling
    '021': 'Recursive',
    '050': 'Iterative+Carry',
    '072': 'Greedy+Digit',
    '085': 'Direct',

    # Heap - Min heap vs max heap vs dual heap
    '006': 'Min Heap',
    '012': 'Binary Search+Prefix',
    '015': 'Bucket Sort',
    '019': 'Min Heap',
    '034': 'Dual Heap+Lazy',
    '082': 'Dual Heap',
    '091': 'Reservoir Sampling',

    # Tree - DFS vs BFS, pre/in/post-order, level-order
    '003': 'BFS+Column Track',
    '005': 'DFS+Parent Ptr',
    '007': 'BFS Level-Order',
    '009': 'DFS Recursive',
    '011': 'DFS+Depth',
    '013': 'DFS Path Track',
    '014': 'DFS Bottom-Up',
    '061': 'DFS+Sort',
    '066': 'BFS+Parent Map',
    '076': 'DFS+Max Path',

    # Graph - DFS for cycles, BFS for shortest path
    '025': 'DFS+Clone',
    '031': 'BFS Shortest',
    '036': 'DFS+Union-Find',
    '038': 'Union-Find',
    '053': 'DFS+Backtrack',
    '063': 'DFS Cycle Detect',
    '070': 'Dijkstra',
    '081': 'BFS Transform',
    '086': 'DFS+BFS Hybrid',

    # Linked-List - Dummy node, two-pointer, in-place modification
    '019': 'Min Heap+Merge',
    '032': 'HashMap',
    '045': '2-Ptr Gap',
    '054': 'Dummy+Carry',
    '064': 'Edge Cases',

    # Stack - Monotonic stack vs regular stack, what to store
    '008': 'Stack+Operator',
    '035': 'Stack+Path',
    '049': 'Stack+Time',
    '093': 'Stack+Nested',
    '098': 'Stack+Count',

    # Sliding-Window - Fixed size vs variable size window
    '037': 'Variable Size',
    '040': 'Variable Size',
    '059': 'HashMap+Mod',
    '068': 'Fixed Size',
    '080': 'Variable Size',
    '090': 'Variable Size+Sort',

    # Array-Hashing - Prefix sum, hash for O(1) lookup, sorting
    '016': 'Sort+Merge',
    '017': 'HashMap O(1)',
    '022': 'Right-to-Left',
    '023': 'Count+Build',
    '024': 'Max Heap',
    '026': 'Prefix Sum+Hash',
    '062': 'Hash Pattern',
    '069': 'Heap+Greedy',
    '071': 'SQL Aggregate',
    '077': 'Difference Array',
    '087': 'Kadane DP',
    '089': 'Prefix Sum',

    # Dynamic-Programming - 1D vs 2D DP, top-down vs bottom-up
    '018': '1D DP',
    '055': 'Backtrack',
    '075': '1D DP',
    '083': '2D DP',
    '099': 'State Machine DP',

    # Design - Trade-offs between time/space complexity
    '039': 'HashMap+DLL',
    '048': 'Queue+Sum',
    '091': 'HashMap+Random',

    # String - In-place vs new string, validation vs parsing
    '043': 'Vertical Scan',
    '046': 'Diagonal Sim',
    '047': 'Gap Check',
    '058': 'DFA Validation',
    '067': 'Parse+Validate',
    '095': 'Transform',
    '097': 'Greedy Pack',
}

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

        filename = os.path.basename(filepath)
        num = filename[:3]

        if title.startswith(num):
            title = title[len(num):].lstrip('.').strip()

        # Get problem-specific tag
        tag = PROBLEM_TAGS.get(num, 'Standard')

        return {
            'num': num,
            'title': title,
            'difficulty': difficulty,
            'frequency': frequency,
            'categories': categories,
            'time': time_complex,
            'space': space_complex,
            'tag': tag,
            'filename': filename
        }
    except Exception as e:
        print(f"Error extracting metadata from {filepath}: {e}")
        return None

def generate_html():
    """Generate comprehensive index.html."""
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

    html = generate_html_content(categories_data)

    output_path = os.path.join(BASE_DIR, 'index.html')
    with open(output_path, 'w') as f:
        f.write(html)

    print(f"✓ Generated {output_path}")
    print(f"  Total categories: {len(categories_data)}")
    print(f"  Total problems: {sum(len(p) for p in categories_data.values())}")

def generate_html_content(categories_data):
    """Generate HTML content."""
    category_sections = ''
    category_nav = ''

    for i, (category, problems) in enumerate(sorted(categories_data.items())):
        info = CATEGORY_INFO.get(category, {})
        icon = info.get('icon', '📁')
        desc = info.get('desc', '')
        key_diff = info.get('key_diff', '')

        category_nav += f'''
            <div class="category-card" onclick="scrollToCategory('{category}')">
                <div class="category-icon">{icon}</div>
                <div class="category-name">{category.replace('-', ' ')}</div>
                <div class="category-count">{len(problems)} problems</div>
            </div>
        '''

        problem_rows = ''
        for prob in problems:
            difficulty_class = prob['difficulty'].lower()
            problem_rows += f'''
                <tr>
                    <td class="num-col">{prob['num']}</td>
                    <td class="title-col">
                        <a href="{GITHUB_REPO}/{category}/{prob['filename']}" class="problem-link" target="_blank">
                            {prob['title']}
                        </a>
                    </td>
                    <td class="tag-col">
                        <span class="tag-badge">{prob['tag']}</span>
                    </td>
                    <td class="diff-col">
                        <span class="badge badge-{difficulty_class}">{prob['difficulty']}</span>
                    </td>
                    <td class="freq-col">{prob['frequency']}</td>
                    <td class="complex-col">{prob['time']}</td>
                    <td class="complex-col">{prob['space']}</td>
                </tr>
            '''

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
                                <th class="tag-col">🏷️ Approach Tag</th>
                                <th class="diff-col">Difficulty</th>
                                <th class="freq-col">Frequency</th>
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

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LeetCode 100 Problems - Tagged Category View</title>
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
            min-width: 280px;
        }}

        .tag-col {{
            min-width: 140px;
            text-align: center;
        }}

        .tag-badge {{
            display: inline-block;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 700;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            box-shadow: 0 2px 6px rgba(102, 126, 234, 0.3);
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

            .tag-col {{
                min-width: 100px;
            }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🎯 LeetCode 100 Problems</h1>
        <p class="subtitle">Tagged by Approach | Organized by Category</p>
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
            <span class="stat-number">🏷️</span>
            <span>Approach Tags</span>
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
