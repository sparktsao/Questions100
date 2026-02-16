#!/usr/bin/env python3
"""
Analyze incomplete LeetCode problem files and report what needs to be fixed.
"""

import os
import re
from pathlib import Path

def analyze_file(filepath):
    """Analyze a single markdown file for completeness."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []
    filename = os.path.basename(filepath)
    problem_num = filename.split('_')[0].lstrip('0')
    problem_name = ' '.join(filename.replace('.md', '').split('_')[1:]).title()

    # Check for generic problem descriptions
    # Look for truly generic phrases that indicate placeholder content
    generic_descriptions = [
        "Solve a.*algorithmic challenge",
        "Given an array or list of elements, solve a problem",  # More specific generic pattern
        "Optimize profit from buying and selling with given constraints",  # Generic stock problem
    ]

    for pattern in generic_descriptions:
        if re.search(pattern, content, re.IGNORECASE):
            issues.append("Generic problem description")
            break

    # Also check if problem description section is suspiciously short (< 50 chars after "## Problem Description")
    prob_desc_match = re.search(r'## Problem Description\s*\n\s*\n(.{0,100})', content, re.DOTALL)
    if prob_desc_match:
        desc_text = prob_desc_match.group(1).strip()
        # If description is very short and contains generic phrases, flag it
        if len(desc_text) < 50 and any(phrase in desc_text.lower() for phrase in ['solve', 'algorithmic', 'given an array or list']):
            if "Generic problem description" not in issues:
                issues.append("Generic problem description")

    # Check for generic/fake solutions
    generic_solutions = [
        r"def solve\(",
        r"def solve_dp\(",
        r"def binary_search_solution\(",
        r"def process\(item\)",
    ]

    for pattern in generic_solutions:
        if re.search(pattern, content):
            issues.append("Generic/fake solution code")
            break

    # Check for generic examples
    if re.search(r'nums = \[3,1,4,1,5,9,2,6\]', content):
        issues.append("Generic example data (not problem-specific)")

    # Check for vague output descriptions
    if re.search(r'\*\*Output:\*\* `Result (after processing|depends on)', content):
        issues.append("Vague/generic output descriptions")

    # Check for problem-specific content
    has_actual_problem = False
    if not any(issue in ['Generic problem description'] for issue in issues):
        has_actual_problem = True

    return {
        'number': problem_num,
        'name': problem_name,
        'file': filename,
        'issues': issues,
        'is_complete': len(issues) == 0
    }

def main():
    questions_dir = Path(__file__).parent
    markdown_files = sorted(questions_dir.glob('[0-1]*.md'))

    incomplete_files = []
    complete_count = 0

    print("=" * 80)
    print("LEETCODE QUESTIONS COMPLETION ANALYSIS")
    print("=" * 80)
    print()

    for filepath in markdown_files:
        result = analyze_file(filepath)

        if not result['is_complete']:
            incomplete_files.append(result)
        else:
            complete_count += 1

    # Print summary
    total = len(markdown_files)
    incomplete_count = len(incomplete_files)

    print(f"📊 SUMMARY:")
    print(f"   Total files: {total}")
    print(f"   ✅ Complete: {complete_count} ({complete_count/total*100:.1f}%)")
    print(f"   ❌ Incomplete: {incomplete_count} ({incomplete_count/total*100:.1f}%)")
    print()
    print("=" * 80)
    print()

    # Print incomplete files with details
    if incomplete_files:
        print(f"INCOMPLETE FILES ({incomplete_count} files need work):")
        print("=" * 80)
        print()

        for result in incomplete_files:
            print(f"#{result['number']:>3} - {result['name']}")
            print(f"      File: {result['file']}")
            print(f"      Issues:")
            for issue in result['issues']:
                print(f"        • {issue}")
            print()

    # Generate TODO list
    print("=" * 80)
    print("TODO: Fix these files")
    print("=" * 80)
    for result in incomplete_files:
        print(f"[ ] #{result['number']:>3} - {result['name']}")

    print()
    print("=" * 80)
    print(f"Run this script anytime to check progress: python3 {os.path.basename(__file__)}")
    print("=" * 80)

if __name__ == '__main__':
    main()
