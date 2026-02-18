#!/bin/bash

echo "============================================"
echo "Questions100 Reorganization Verification"
echo "============================================"
echo ""

cd /Users/sparkt/2026C/Questions100/LeetCode

echo "Categories and File Counts:"
echo "----------------------------"

for dir in */; do
    if [ -d "$dir" ]; then
        count=$(find "$dir" -maxdepth 1 -name "[0-9]*.md" -type f 2>/dev/null | wc -l)
        count=$(echo $count | tr -d ' ')
        if [ "$count" -gt 0 ]; then
            printf "%-35s %3d files\n" "$dir" "$count"
        fi
    fi
done

echo ""
total=$(find . -name "[0-9][0-9][0-9]_*.md" -type f | wc -l | tr -d ' ')
readmes=$(find . -name "README.md" -type f | wc -l | tr -d ' ')

echo "Summary:"
echo "--------"
echo "Total question files: $total"
echo "README files: $readmes"
echo "Index files: $(find /Users/sparkt/2026C/Questions100 -maxdepth 2 -name "index.html" -type f | wc -l | tr -d ' ')"
echo ""
echo "✓ Questions100 reorganization complete!"
echo ""
echo "To view: open /Users/sparkt/2026C/Questions100/index.html"
