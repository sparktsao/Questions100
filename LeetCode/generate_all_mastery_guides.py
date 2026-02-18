#!/usr/bin/env python3
"""
Generate comprehensive mastery guides for ALL 16 categories.
Each guide includes: sub-patterns, learning paths, testing strategies, and mastery insights.
"""

import os
import glob
import re

BASE_DIR = '/Users/sparkt/2026C/Questions100/LeetCode'

def read_problems(category_path):
    """Read all problem files and extract metadata."""
    files = sorted(glob.glob(os.path.join(category_path, '[0-9]*.md')))
    problems = []
    
    for filepath in files:
        try:
            with open(filepath, 'r') as f:
                content = f.read()
                lines = content.split('\n')
            
            num = os.path.basename(filepath)[:3]
            title = lines[0].replace('#', '').strip() if lines else 'Unknown'
            if title.startswith(num):
                title = title[len(num):].lstrip('.').strip()
            
            difficulty = 'MEDIUM'
            frequency = 'N/A'
            
            for line in lines[:20]:
                if '**Difficulty:**' in line:
                    difficulty = line.split('**Difficulty:**')[1].strip()
                elif '**Frequency:**' in line:
                    frequency = line.split('**Frequency:**')[1].strip()
            
            problems.append({
                'num': num,
                'title': title,
                'difficulty': difficulty,
                'frequency': frequency,
                'filename': os.path.basename(filepath)
            })
        except:
            pass
    
    return problems


# Import the existing Binary Search analysis
from create_deep_summary import CATEGORY_ANALYSIS as BINARY_SEARCH_ANALYSIS

# Complete category analysis for all 16 categories
CATEGORY_GUIDES = {}

# 1. Binary Search (already done)
CATEGORY_GUIDES['Binary-Search'] = BINARY_SEARCH_ANALYSIS['Binary-Search']

# Continue with other categories...
print("Generated partial script - continuing with full implementation...")
