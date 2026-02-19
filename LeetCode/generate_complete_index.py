#!/usr/bin/env python3
"""
Generate complete index.html with all 100 LeetCode problems organized by category.
Extracts data from TAG_REFERENCE.md and individual problem markdown files.
"""

import re
import os
from pathlib import Path

# Category metadata
CATEGORY_INFO = {
    'Parentheses': {'icon': '📚', 'description': 'Stack-based tracking, different removal strategies'},
    'Palindrome': {'icon': '🔄', 'description': 'Two-pointers vs DP, string modification allowed'},
    'BST-Binary-Search-Tree': {'icon': '🌲', 'description': 'In-order traversal, BST property pruning'},
    'Binary-Search': {'icon': '🔍', 'description': 'Search target vs search answer space'},
    'Two-Pointers': {'icon': '👉', 'description': 'Same direction vs opposite direction'},
    'Math-Compute': {'icon': '🔢', 'description': 'Iterative vs recursive, carry handling'},
    'Heap-Priority-Queue': {'icon': '⛰️', 'description': 'Min heap vs max heap vs dual heap'},
    'Tree': {'icon': '🌳', 'description': 'DFS vs BFS, pre/in/post-order, level-order'},
    'Graph-DFS-BFS': {'icon': '🕸️', 'description': 'DFS for cycles, BFS for shortest path'},
    'Linked-List': {'icon': '🔗', 'description': 'Dummy node, two-pointer, in-place modification'},
    'Stack': {'icon': '📚', 'description': 'Monotonic stack vs regular stack, what to store'},
    'Sliding-Window': {'icon': '🪟', 'description': 'Fixed size vs variable size'},
    'Array-Hashing': {'icon': '🗂️', 'description': 'Prefix sum, hash for O(1) lookup, sorting'},
    'Dynamic-Programming': {'icon': '📊', 'description': 'DP patterns and state machines'},
    'Design': {'icon': '🛠️', 'description': 'Trade-offs between time/space complexity'},
    'String': {'icon': '📝', 'description': 'In-place vs new string, validation vs parsing'},
}

def parse_tag_reference():
    """Parse TAG_REFERENCE.md to extract problem data."""
    tag_ref_path = Path('/Users/sparkt/2026C/Questions100/LeetCode/TAG_REFERENCE.md')

    with open(tag_ref_path, 'r') as f:
        content = f.read()

    problems = {}
    current_category = None

    # Pattern to match category headers
    category_pattern = r'###\s+([A-Za-z-]+)\s+-\s+(.+)'
    # Pattern to match problem rows: | 001 | Problem Name | Tag | Meaning |
    problem_pattern = r'\|\s*(\d{3})\s*\|\s*([^|]+)\|\s*([^|]+)\|\s*([^|]+)\|'

    lines = content.split('\n')
    for line in lines:
        category_match = re.match(category_pattern, line)
        if category_match:
            current_category = category_match.group(1)
            continue

        problem_match = re.match(problem_pattern, line)
        if problem_match and current_category:
            num = problem_match.group(1)
            title = problem_match.group(2).strip()
            tag = problem_match.group(3).strip()

            problems[num] = {
                'number': num,
                'title': title,
                'tag': tag,
                'category': current_category
            }

    return problems

def extract_problem_metadata(problem_file):
    """Extract difficulty and frequency from problem markdown file."""
    try:
        with open(problem_file, 'r') as f:
            content = f.read(500)  # Read first 500 chars

        difficulty_match = re.search(r'\*\*Difficulty:\*\*\s+(\w+)', content)
        frequency_match = re.search(r'\*\*Frequency:\*\*\s+([\d.]+)%', content)

        difficulty = difficulty_match.group(1) if difficulty_match else 'MEDIUM'
        frequency = frequency_match.group(1) if frequency_match else '0.0'

        return difficulty, frequency
    except Exception as e:
        print(f"Error reading {problem_file}: {e}")
        return 'MEDIUM', '0.0'

def find_problem_file(category, problem_num):
    """Find the markdown file for a given problem."""
    category_dir = Path(f'/Users/sparkt/2026C/Questions100/LeetCode/{category}')

    if not category_dir.exists():
        return None

    # Find file starting with problem number
    for file in category_dir.glob(f'{problem_num}_*.md'):
        return file

    return None

def generate_problem_row(problem_data, difficulty, frequency):
    """Generate HTML table row for a problem."""
    num = problem_data['number']
    title = problem_data['title']
    tag = problem_data['tag']
    category = problem_data['category']

    # Convert difficulty to badge class
    badge_class = f"badge-{difficulty.lower()}"

    # Generate file path
    filename = title.lower()
    filename = re.sub(r'[^\w\s-]', '', filename)
    filename = re.sub(r'[-\s]+', '_', filename)
    file_path = f"LeetCode/{category}/{num}_{filename}.md"

    return f'''                        <tr data-title="{title}" data-tag="{tag}" data-diff="{difficulty}" data-category="{category}">
                            <td class="num-col">{num}</td>
                            <td class="title-col">
                                <a href="{file_path}" class="problem-link">
                                    {title}
                                </a>
                            </td>
                            <td class="tag-col">
                                <span class="tag-badge">{tag}</span>
                            </td>
                            <td class="diff-col">
                                <span class="badge {badge_class}">{difficulty}</span>
                            </td>
                            <td class="freq-col">{frequency}%</td>
                        </tr>'''

def generate_category_section(category, problems_in_category):
    """Generate HTML section for a category."""
    info = CATEGORY_INFO.get(category, {'icon': '📁', 'description': 'Problem category'})
    icon = info['icon']
    description = info['description']
    count = len(problems_in_category)

    # Generate problem rows
    problem_rows = '\n'.join(problems_in_category)

    return f'''
        <section id="{category}" class="category-section" data-category="{category}">
            <div class="category-header">
                <div class="category-title">
                    <span class="category-icon-large">{icon}</span>
                    <h2>{category.replace('-', ' ').title()}</h2>
                    <span class="problem-count">{count} problems</span>
                </div>
                <div class="category-description">
                    <strong>Focus:</strong> {description}
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
                        </tr>
                    </thead>
                    <tbody>
{problem_rows}
                    </tbody>
                </table>
            </div>
        </section>'''

def main():
    """Main function to generate complete index.html."""
    print("Parsing TAG_REFERENCE.md...")
    problems = parse_tag_reference()
    print(f"Found {len(problems)} problems")

    # Organize problems by category
    categories = {}
    for num, problem in sorted(problems.items()):
        category = problem['category']

        # Find problem file and extract metadata
        problem_file = find_problem_file(category, num)
        if problem_file:
            difficulty, frequency = extract_problem_metadata(problem_file)
        else:
            print(f"Warning: File not found for {num} - {problem['title']}")
            difficulty, frequency = 'MEDIUM', '0.0'

        # Generate row HTML
        row_html = generate_problem_row(problem, difficulty, frequency)

        if category not in categories:
            categories[category] = []
        categories[category].append(row_html)

        print(f"  {num}: {problem['title']} ({category})")

    print(f"\nGenerating HTML for {len(categories)} categories...")

    # Generate category sections
    category_sections = []
    for category in categories.keys():
        section_html = generate_category_section(category, categories[category])
        category_sections.append(section_html)

    all_sections = '\n'.join(category_sections)

    # Read current index.html to get header and styles
    index_path = Path('/Users/sparkt/2026C/Questions100/index.html')
    with open(index_path, 'r') as f:
        current_html = f.read()

    # Find the section where we need to replace content
    # Replace from <div id="categorySections"> to </div> before <div id="noResults">
    pattern = r'(<div id="categorySections">).*?(</div>\s*<div id="noResults")'

    new_html = re.sub(
        pattern,
        r'\1' + all_sections + r'\n    \2',
        current_html,
        flags=re.DOTALL
    )

    # Write updated HTML
    with open(index_path, 'w') as f:
        f.write(new_html)

    print(f"\n✅ Successfully generated complete index.html with {len(problems)} problems across {len(categories)} categories!")

if __name__ == '__main__':
    main()
