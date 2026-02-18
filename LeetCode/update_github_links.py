#!/usr/bin/env python3
"""
Update generate_tagged_index.py to use GitHub blob URLs
"""

import re

# Read the file
with open('generate_tagged_index.py', 'r') as f:
    content = f.read()

# Add GitHub URL constant after BASE_DIR
github_section = '''
# GitHub repository URL for blob links
GITHUB_REPO = 'https://github.com/sparktsao/Questions100/blob/main/LeetCode'
'''

# Insert after BASE_DIR line
content = content.replace(
    "BASE_DIR = '/Users/sparkt/2026C/Questions100/LeetCode'",
    "BASE_DIR = '/Users/sparkt/2026C/Questions100/LeetCode'" + github_section
)

# Update the href line to use GitHub URL
old_href = '                        <a href="{category}/{prob[\'filename\']}" class="problem-link" target="_blank">'
new_href = '                        <a href="{GITHUB_REPO}/{category}/{prob[\'filename\']}" class="problem-link" target="_blank">'

content = content.replace(old_href, new_href)

# Write back
with open('generate_tagged_index.py', 'w') as f:
    f.write(content)

print("✓ Updated generate_tagged_index.py with GitHub blob URLs")
