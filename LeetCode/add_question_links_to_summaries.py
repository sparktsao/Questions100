#!/usr/bin/env python3
"""
Update all category summary files to include links to individual questions.
"""

import re
from pathlib import Path

def parse_tag_reference():
    """Parse TAG_REFERENCE.md to extract problem data by category."""
    tag_ref_path = Path('/Users/sparkt/2026C/Questions100/LeetCode/TAG_REFERENCE.md')

    with open(tag_ref_path, 'r') as f:
        content = f.read()

    categories = {}
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
            categories[current_category] = []
            continue

        problem_match = re.match(problem_pattern, line)
        if problem_match and current_category:
            num = problem_match.group(1)
            title = problem_match.group(2).strip()
            tag = problem_match.group(3).strip()

            # Generate filename
            filename = title.lower()
            filename = re.sub(r'[^\w\s-]', '', filename)
            filename = re.sub(r'[-\s]+', '_', filename)
            file_path = f"{num}_{filename}.md"

            categories[current_category].append({
                'number': num,
                'title': title,
                'tag': tag,
                'filename': file_path
            })

    return categories

def generate_problem_links_section(problems):
    """Generate the problem links section for a summary."""
    links = []
    for problem in problems:
        num = problem['number']
        title = problem['title']
        tag = problem['tag']
        filename = problem['filename']
        links.append(f"- [{num}. {title}]({filename}) - `{tag}`")

    section = f"""## 📋 Problems in This Category

{chr(10).join(links)}

---

"""
    return section

def update_summary_file(category, problems):
    """Update a summary file to include problem links."""
    # Generate summary filename
    summary_filename = category.lower().replace('-', '_') + '_summary.md'
    summary_path = Path(f'/Users/sparkt/2026C/Questions100/LeetCode/{category}/{summary_filename}')

    # Special case: Graph-DFS-BFS uses graph_summary.md
    if not summary_path.exists() and category == 'Graph-DFS-BFS':
        summary_path = Path(f'/Users/sparkt/2026C/Questions100/LeetCode/{category}/graph_summary.md')

    if not summary_path.exists():
        print(f"⚠️  Summary file not found: {summary_path}")
        return False

    # Read current content
    with open(summary_path, 'r') as f:
        content = f.read()

    # Check if problem links section already exists
    if '## 📋 Problems in This Category' in content:
        print(f"✓ {category}: Problem links already exist, skipping")
        return False

    # Generate problem links section
    links_section = generate_problem_links_section(problems)

    # Find where to insert (after the first header and any intro text, before the first ## section)
    # We'll insert after the first line and before the first ## (except the title)
    lines = content.split('\n')

    # Find first non-title ## header
    insert_index = 0
    found_title = False
    for i, line in enumerate(lines):
        if line.startswith('# '):  # Title
            found_title = True
            insert_index = i + 1
            # Skip blank lines after title
            while insert_index < len(lines) and lines[insert_index].strip() == '':
                insert_index += 1
        elif found_title and line.startswith('## '):
            # Found first section header, insert before it
            break
        elif found_title:
            insert_index = i + 1

    # Insert the links section
    new_content = '\n'.join(lines[:insert_index]) + '\n\n' + links_section + '\n'.join(lines[insert_index:])

    # Write updated content
    with open(summary_path, 'w') as f:
        f.write(new_content)

    print(f"✓ {category}: Added {len(problems)} problem links")
    return True

def main():
    """Main function to update all summary files."""
    print("Parsing TAG_REFERENCE.md...")
    categories = parse_tag_reference()
    print(f"Found {len(categories)} categories\n")

    updated_count = 0
    for category, problems in categories.items():
        if update_summary_file(category, problems):
            updated_count += 1

    print(f"\n✅ Updated {updated_count} summary files with problem links!")

if __name__ == '__main__':
    main()
