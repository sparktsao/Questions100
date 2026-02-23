# String - Comprehensive Mastery Guide

## 📋 Problems in This Category

- [043. Longest Common Prefix](https://github.com/sparktsao/Questions100/blob/main/LeetCode/String/043_longest_common_prefix.md) - `Vertical Scan`
- [046. Diagonal Traverse](https://github.com/sparktsao/Questions100/blob/main/LeetCode/String/046_diagonal_traverse.md) - `Diagonal Sim`
- [047. Missing Ranges](https://github.com/sparktsao/Questions100/blob/main/LeetCode/String/047_missing_ranges.md) - `Gap Check`
- [058. Valid Number](https://github.com/sparktsao/Questions100/blob/main/LeetCode/String/058_valid_number.md) - `DFA Validation`
- [067. String to Integer](https://github.com/sparktsao/Questions100/blob/main/LeetCode/String/067_string_to_integer_atoi.md) - `Parse+Validate`
- [095. Goat Latin](https://github.com/sparktsao/Questions100/blob/main/LeetCode/String/095_goat_latin.md) - `Transform`
- [097. Text Justification](https://github.com/sparktsao/Questions100/blob/main/LeetCode/String/097_text_justification.md) - `Greedy Pack`

---

## 🎯 Overview

**Total Problems:** 7
**Difficulty:** Easy (3) • Medium (2) • Hard (2)

**Core Concept:**
String manipulation involves **parsing, validation, transformation, and pattern recognition**. The key challenge is handling **immutability** in Python while maintaining optimal time/space complexity.

**Key Insights:**
1. **Strings are immutable** → Use list for O(1) modifications, join at end
2. **Character access is O(1)** → Random access and indexing are fast
3. **Concatenation is O(n)** → Each `s += char` creates new string (use list instead)
4. **Slicing creates copies** → `s[i:j]` is O(j-i) time and space
5. **Pattern matching varies** → Naive O(mn), KMP O(m+n), Rabin-Karp O(m+n) average

---

## 🔄 String Operations vs Other Approaches

### String Building: Concatenation vs List vs StringBuilder

**String Concatenation (Naive - SLOW):**
```python
# ❌ O(n²) - Each += creates new string and copies everything
result = ""
for char in s:
    result += char  # Creates new string every iteration
# "hello" → "" + "h" + "e" + "l" + "l" + "o"
# Time: 1 + 2 + 3 + 4 + 5 = O(n²)
```

**List Accumulation (FAST):**
```python
# ✅ O(n) - List append is O(1), join is O(n)
result = []
for char in s:
    result.append(char)  # O(1) append
return ''.join(result)   # O(n) single concatenation
# Time: n × O(1) + O(n) = O(n)
```

**When to use which:**
- **List + join:** Building string incrementally (most common)
- **Direct concat:** Only for 2-3 fixed strings (`first + " " + last`)
- **f-strings/format:** Embedding variables (`f"{name} is {age}"`)

**Performance comparison:**
```python
# Build string with 10,000 characters
# Concatenation: ~5 seconds (O(n²))
# List + join: ~0.005 seconds (O(n))
# 1000x faster!
```

---

### String Search: Naive vs Two Pointers vs Sliding Window vs KMP

**Naive Search (Check Every Position):**
```python
# O(mn) - Check pattern at each position
def naive_search(text: str, pattern: str) -> int:
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i+len(pattern)] == pattern:
            return i
    return -1
# text="ababcabcab", pattern="abcab"
# Check: ababc(✗), babca(✗), abcab(✗), bcabc(✗), cabca(✗), abcab(✓)
```

**Two Pointers (When Conditions Exist):**
```python
# O(n) - Process each character once
def is_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
# "racecar" → compare r-r, a-a, c-c, e-e (center)
```

**Sliding Window (Substring with Constraints):**
```python
# O(n) - Expand/shrink window
def longest_substring_k_distinct(s: str, k: int) -> int:
    char_count = {}
    left = max_len = 0

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1

        while len(char_count) > k:
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        max_len = max(max_len, right - left + 1)
    return max_len
# "eceba", k=2 → "ece" (length 3)
```

**KMP (Optimal Pattern Matching):**
```python
# O(m + n) - Preprocesses pattern to skip redundant comparisons
def kmp_search(text: str, pattern: str) -> int:
    lps = build_lps(pattern)  # Longest Prefix Suffix array

    i = j = 0
    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                return i - j
        elif j > 0:
            j = lps[j - 1]  # Skip to matching prefix
        else:
            i += 1
    return -1
# Avoids re-checking characters in text
```

**When to use which:**
- **Naive:** Pattern length ≤ 3, or text length < 100
- **Two Pointers:** Palindrome, reversal, comparing from both ends
- **Sliding Window:** Substring with constraints (max length, distinct chars)
- **KMP:** Long patterns, repeated pattern searches, guaranteed O(n)

---

### String Comparison: Character-by-Character vs Hash vs Sort

**Character-by-Character (Direct Comparison):**
```python
# O(n) - Best for checking equality or prefix
def is_prefix(text: str, prefix: str) -> bool:
    if len(prefix) > len(text):
        return False
    for i in range(len(prefix)):
        if text[i] != prefix[i]:
            return False
    return True
# Or just: text.startswith(prefix)
```

**Hash-Based (Anagram Detection):**
```python
# O(n) - Count frequency of characters
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
# "anagram" vs "nagaram"
# Counter: {'a':3, 'n':1, 'g':1, 'r':1, 'm':1} (equal)
```

**Sort-Based (Anagram Grouping):**
```python
# O(n log n) - Sort to canonical form
def group_anagrams(strs: List[str]) -> List[List[str]]:
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))  # O(n log n)
        groups.setdefault(key, []).append(s)
    return list(groups.values())
# ["eat","tea","tan","ate","nat","bat"]
# "aet": ["eat","tea","ate"], "ant": ["tan","nat"], "abt": ["bat"]
```

**When to use which:**
- **Character-by-character:** Exact match, prefix/suffix check
- **Hash (Counter):** Anagram detection, frequency comparison
- **Sort:** Grouping anagrams, canonical form needed

---

### String Parsing: State Machine vs Regex vs Manual

**State Machine (DFA - Deterministic Finite Automaton):**
```python
# O(n) - Explicit state transitions for complex validation
def is_valid_number(s: str) -> bool:
    state = 0
    transitions = {
        0: {'digit': 1, 'sign': 2, 'dot': 3},
        1: {'digit': 1, 'dot': 4, 'exp': 5},
        2: {'digit': 1, 'dot': 3},
        3: {'digit': 4},
        4: {'digit': 4, 'exp': 5},
        5: {'sign': 6, 'digit': 7},
        6: {'digit': 7},
        7: {'digit': 7}
    }
    final_states = {1, 4, 7}

    for char in s.strip():
        char_type = get_type(char)
        if char_type not in transitions[state]:
            return False
        state = transitions[state][char_type]

    return state in final_states
# Validates: "123", "-0.5", "2e10", ".5", "53.5e93"
# Rejects: "abc", "1a", "e3", "99e2.5"
```

**Regex (Declarative Pattern):**
```python
# O(n) - Pattern matching with regex engine
import re

def is_valid_number(s: str) -> bool:
    pattern = r'^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$'
    return bool(re.match(pattern, s.strip()))
# Same validation as state machine, more concise
```

**Manual Parsing (Custom Logic):**
```python
# O(n) - Direct character-by-character logic
def string_to_integer(s: str) -> int:
    s = s.strip()
    if not s:
        return 0

    sign = -1 if s[0] == '-' else 1
    if s[0] in '+-':
        s = s[1:]

    result = 0
    for char in s:
        if not char.isdigit():
            break
        result = result * 10 + int(char)
        if result * sign > 2**31 - 1:
            return 2**31 - 1
        if result * sign < -2**31:
            return -2**31

    return result * sign
# "  -42" → -42, "4193 with words" → 4193
```

**When to use which:**
- **State Machine:** Complex validation rules, clear state transitions (Valid Number)
- **Regex:** Simple patterns, need conciseness, not performance-critical
- **Manual:** Custom logic, need fine-grained control, performance-critical

---

### String Transformation: In-Place vs New String vs Two-Pass

**In-Place (Modify List):**
```python
# O(n) time, O(1) extra space (excluding output)
def reverse_words(s: List[str]) -> None:
    # Reverse entire string
    s.reverse()

    # Reverse each word
    start = 0
    for i in range(len(s) + 1):
        if i == len(s) or s[i] == ' ':
            s[start:i] = reversed(s[start:i])
            start = i + 1
# ["t","h","e"," ","s","k","y"]
# → ["y","k","s"," ","e","h","t"] (reverse all)
# → ["s","k","y"," ","t","h","e"] (reverse each word)
```

**New String (Build from Scratch):**
```python
# O(n) time, O(n) space
def reverse_words(s: str) -> str:
    words = s.split()
    return ' '.join(reversed(words))
# "the sky is blue" → "blue is sky the"
```

**Two-Pass (Collect then Process):**
```python
# O(n) time, O(n) space
def goat_latin(sentence: str) -> str:
    vowels = set('aeiouAEIOU')
    words = sentence.split()

    result = []
    for i, word in enumerate(words):
        if word[0] in vowels:
            new_word = word + 'ma'
        else:
            new_word = word[1:] + word[0] + 'ma'
        new_word += 'a' * (i + 1)
        result.append(new_word)

    return ' '.join(result)
# "I speak Goat Latin"
# → "Imaa peaksma oatGmaa atinLmaaaa"
```

**When to use which:**
- **In-place:** Space constraint, list input allowed
- **New string:** Simplest to implement, no space constraint
- **Two-pass:** Need preprocessing (split, analyze, then transform)

---

## 🧠 Deep Dive: String Operations & Complexity

### Immutability Impact

**Why Python Strings are Immutable:**
```python
s = "hello"
s[0] = 'H'  # TypeError: 'str' object does not support item assignment

# Each "modification" creates new string
s = "hello"
s = s + " world"  # Creates new string "hello world"
# Old "hello" is discarded (garbage collected)
```

**Performance Implications:**
```python
# ❌ SLOW: O(n²) - Creates n new strings
result = ""
for i in range(n):
    result += str(i)  # result = result + str(i)
# Iteration 1: "" + "0" = "0" (copy 1 char)
# Iteration 2: "0" + "1" = "01" (copy 2 chars)
# Iteration 3: "01" + "2" = "012" (copy 3 chars)
# Total copies: 1 + 2 + 3 + ... + n = O(n²)

# ✅ FAST: O(n) - Append to list, join once
result = []
for i in range(n):
    result.append(str(i))  # O(1) append
return ''.join(result)     # O(n) single join
```

### String Slicing Mechanics

```python
s = "hello world"

# Slicing creates NEW string (copy)
sub = s[0:5]  # "hello" - O(5) time, O(5) space

# Slicing doesn't modify original
s[0:5] = "HELLO"  # TypeError: immutable

# Multiple slices = multiple copies
parts = [s[0:5], s[6:11]]  # Two separate strings created

# Efficient checking without copying
if s[0:5] == "hello":  # Still creates "hello" copy for comparison
    pass

# More efficient: check character by character
if len(s) >= 5 and all(s[i] == "hello"[i] for i in range(5)):
    pass

# Or use startswith
if s.startswith("hello"):  # Optimized in C, no copy
    pass
```

### String Search Complexity

**Built-in `in` operator:**
```python
"pattern" in "text"  # Uses optimized C implementation
# Average: O(n) with Boyer-Moore-Horspool-like algorithm
# Worst: O(mn) but rare in practice
```

**find() vs index():**
```python
s.find("pattern")     # Returns -1 if not found
s.index("pattern")    # Raises ValueError if not found

# Both O(n) but find() is safer (no exception)
```

**count() complexity:**
```python
s.count("pattern")  # O(n) - scans entire string once
# Efficient even for multiple occurrences
```

---

## 📚 Sub-Patterns & Techniques

### Pattern 1: String Parsing & Validation

**Concept:** Read string sequentially, apply rules, validate format

```python
def string_to_integer(s: str) -> int:
    """
    Convert string to integer with bounds checking (atoi).
    Handle: whitespace, sign, digits, overflow
    """
    s = s.strip()
    if not s:
        return 0

    # Determine sign
    sign = -1 if s[0] == '-' else 1
    if s[0] in '+-':
        s = s[1:]

    # Parse digits
    result = 0
    for char in s:
        if not char.isdigit():
            break
        result = result * 10 + int(char)

        # Clamp to 32-bit integer range
        if result * sign > 2**31 - 1:
            return 2**31 - 1
        if result * sign < -2**31:
            return -2**31

    return result * sign
```

**Examples:**
- [067. String to Integer (atoi)](./067_string_to_integer_atoi.md)
- [058. Valid Number](./058_valid_number.md)

**Key Techniques:**
- Strip whitespace first: `s.strip()`
- Track state (sign seen, digits seen, etc.)
- Early termination on invalid character
- Bounds checking for overflow

**Time:** O(n), **Space:** O(1)

---

### Pattern 2: String Transformation & Formatting

**Concept:** Apply rules to modify string format or content

```python
def text_justification(words: List[str], max_width: int) -> List[str]:
    """
    Fully justify text by distributing spaces evenly.
    Greedy packing of words per line.
    """
    result = []
    current_line = []
    current_length = 0

    for word in words:
        # Check if word fits in current line (with spaces)
        if current_length + len(word) + len(current_line) > max_width:
            # Justify current line
            result.append(justify_line(current_line, max_width, False))
            current_line = []
            current_length = 0

        current_line.append(word)
        current_length += len(word)

    # Last line is left-justified
    result.append(justify_line(current_line, max_width, True))
    return result

def justify_line(words: List[str], max_width: int, is_last: bool) -> str:
    if is_last or len(words) == 1:
        # Left-justify
        return ' '.join(words).ljust(max_width)

    # Distribute spaces evenly
    total_chars = sum(len(w) for w in words)
    total_spaces = max_width - total_chars
    gaps = len(words) - 1
    spaces_per_gap = total_spaces // gaps
    extra_spaces = total_spaces % gaps

    result = []
    for i, word in enumerate(words):
        result.append(word)
        if i < gaps:
            result.append(' ' * spaces_per_gap)
            if i < extra_spaces:
                result.append(' ')

    return ''.join(result)
```

**Examples:**
- [097. Text Justification](./097_text_justification.md)
- [095. Goat Latin](./095_goat_latin.md)

**Key Techniques:**
- Greedy packing (fit as many words as possible)
- Space distribution (quotient + remainder)
- Edge case handling (last line, single word)

**Time:** O(n), **Space:** O(n)

---

### Pattern 3: String Comparison & Matching

**Concept:** Find common patterns, prefixes, or validate relationships

```python
def longest_common_prefix(strs: List[str]) -> str:
    """
    Find longest common prefix among strings.
    Vertical scan: check character at each position across all strings.
    """
    if not strs:
        return ""

    # Check each character position
    for i in range(len(strs[0])):
        char = strs[0][i]

        # Verify all strings have same character at position i
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]
```

**Alternative: Horizontal Scan**
```python
def longest_common_prefix(strs: List[str]) -> str:
    """Compare pairs of strings iteratively"""
    if not strs:
        return ""

    prefix = strs[0]
    for s in strs[1:]:
        # Shrink prefix until it matches
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix
```

**Examples:**
- [043. Longest Common Prefix](./043_longest_common_prefix.md)

**Key Techniques:**
- Vertical scan: Compare column-by-column
- Horizontal scan: Compare string-by-string
- Early termination when mismatch found

**Time:** O(S) where S = sum of all characters, **Space:** O(1)

---

### Pattern 4: Range & Gap Processing

**Concept:** Identify missing elements or gaps in sequences

```python
def find_missing_ranges(nums: List[int], lower: int, upper: int) -> List[str]:
    """
    Find missing ranges in sorted array.
    Handle: empty array, single element, no gaps, full gaps
    """
    result = []
    prev = lower - 1

    for num in nums + [upper + 1]:
        # Gap exists between prev and current
        if num - prev >= 2:
            result.append(format_range(prev + 1, num - 1))
        prev = num

    return result

def format_range(start: int, end: int) -> str:
    """Format range as 'start->end' or 'start' if equal"""
    if start == end:
        return str(start)
    return f"{start}->{end}"
```

**Examples:**
- [047. Missing Ranges](./047_missing_ranges.md)

**Key Techniques:**
- Sentinel values (lower-1, upper+1) simplify edge cases
- Gap detection: `current - prev >= 2`
- Range formatting based on size

**Time:** O(n), **Space:** O(1)

---

### Pattern 5: Two-Dimensional String Processing

**Concept:** Traverse matrix with string-like patterns

```python
def find_diagonal_order(matrix: List[List[int]]) -> List[int]:
    """
    Traverse matrix diagonally, alternating direction.
    Diagonal d: all cells where row + col = d
    """
    if not matrix or not matrix[0]:
        return []

    m, n = len(matrix), len(matrix[0])
    result = []

    # Process each diagonal
    for d in range(m + n - 1):
        diagonal = []

        # Collect cells in diagonal d
        if d % 2 == 0:  # Go up
            row = min(d, m - 1)
            col = d - row
            while row >= 0 and col < n:
                diagonal.append(matrix[row][col])
                row -= 1
                col += 1
        else:  # Go down
            col = min(d, n - 1)
            row = d - col
            while col >= 0 and row < m:
                diagonal.append(matrix[row][col])
                row += 1
                col -= 1

        result.extend(diagonal)

    return result
```

**Examples:**
- [046. Diagonal Traverse](./046_diagonal_traverse.md)

**Key Techniques:**
- Diagonal identification: `row + col = constant`
- Direction alternation: Even vs odd diagonals
- Boundary handling: Start positions differ by parity

**Time:** O(mn), **Space:** O(1)


---

## 🎓 Progressive Learning Path

### Level 1: Basic String Operations
**Start:** Simple manipulation and comparison
- Reverse String (warmup)
- Valid Palindrome (two pointers)
- [043. Longest Common Prefix](./043_longest_common_prefix.md)

**Learn:** Character access, two pointers, immutability basics

---

### Level 2: Parsing & Validation
**Next:** Rule-based string processing
- [067. String to Integer (atoi)](./067_string_to_integer_atoi.md)
- [058. Valid Number](./058_valid_number.md)

**Learn:** State machines, character classification, edge case handling

---

### Level 3: String Transformation
**Then:** Format and restructure strings
- [095. Goat Latin](./095_goat_latin.md)
- String to Title Case

**Learn:** Split, join, word-level processing

---

### Level 4: Range & Gap Analysis
**After:** Sequence processing
- [047. Missing Ranges](./047_missing_ranges.md)

**Learn:** Gap detection, range formatting, sentinel values

---

### Level 5: Complex Formatting
**Then:** Advanced layout and justification
- [097. Text Justification](./097_text_justification.md)

**Learn:** Greedy packing, space distribution, special case handling

---

### Level 6: 2D String Processing
**Finally:** Matrix traversal patterns
- [046. Diagonal Traverse](./046_diagonal_traverse.md)

**Learn:** Coordinate transformations, direction handling

---

## ⚠️ Common Pitfalls & How to Avoid Them

### 1. **String Concatenation in Loops (Performance Killer)**

```python
# ❌ WRONG: O(n²) - Creates new string every iteration
result = ""
for i in range(n):
    result += str(i)  # Copies entire result each time

# Example: Building "0123456789"
# Iter 0: "" + "0" = "0" (1 char copied)
# Iter 1: "0" + "1" = "01" (2 chars copied)
# Iter 2: "01" + "2" = "012" (3 chars copied)
# Total: 1+2+3+...+10 = 55 chars copied (O(n²))

# ✅ CORRECT: O(n) - Append to list, join once
result = []
for i in range(n):
    result.append(str(i))  # O(1) append
return ''.join(result)     # O(n) join

# Copies: 10 appends + 1 join = 10 chars total
```

**Why it happens:** Not understanding string immutability cost

---

### 2. **Not Handling Empty Strings**

```python
# ❌ WRONG: Crashes on empty string
def first_char(s: str) -> str:
    return s[0]  # IndexError if s = ""

# ❌ WRONG: Doesn't handle empty
def longest_prefix(strs: List[str]) -> str:
    prefix = strs[0]  # IndexError if strs = []
    for s in strs[1:]:
        # ...

# ✅ CORRECT: Guard against empty
def first_char(s: str) -> str:
    return s[0] if s else ""

def longest_prefix(strs: List[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    # ...
```

**Why it happens:** Assuming input is always non-empty

---

### 3. **Off-By-One in Slicing**

```python
# ❌ WRONG: Incorrect slice boundaries
s = "hello"
print(s[1:4])   # "ell" (not "ello"!)
print(s[0:6])   # "hello" (doesn't crash, but 6 > len)

# Common mistake: thinking s[i:j] includes j
s = "world"
first_three = s[0:3]  # "wor" (not "worl")

# ✅ CORRECT: Remember [start:end) is half-open
s = "hello"
print(s[1:5])   # "ello" (indices 1,2,3,4)
print(s[:3])    # "hel" (first 3 characters)
print(s[-3:])   # "llo" (last 3 characters)
```

**Why it happens:** Confusing inclusive vs exclusive bounds

---

### 4. **Case Sensitivity Assumptions**

```python
# ❌ WRONG: Doesn't handle case variations
def is_palindrome(s: str) -> bool:
    return s == s[::-1]
# "Aba" != "abA" (False, but should be True)

# ❌ WRONG: Partial case handling
def compare(s1: str, s2: str) -> bool:
    return s1.lower() == s2
# Compares lowercase s1 with original s2

# ✅ CORRECT: Normalize both sides
def is_palindrome(s: str) -> bool:
    s = s.lower()
    return s == s[::-1]

def compare(s1: str, s2: str) -> bool:
    return s1.lower() == s2.lower()
```

**Why it happens:** Forgetting case matters in comparison

---

### 5. **Modifying String Directly**

```python
# ❌ WRONG: Strings are immutable!
s = "hello"
s[0] = 'H'  # TypeError: 'str' object does not support item assignment

# ❌ WRONG: Trying to modify in-place
def reverse_string(s: str) -> str:
    for i in range(len(s) // 2):
        s[i], s[-i-1] = s[-i-1], s[i]  # TypeError!

# ✅ CORRECT: Convert to list, modify, convert back
def reverse_string(s: str) -> str:
    chars = list(s)
    left, right = 0, len(chars) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)

# Or use slicing
def reverse_string(s: str) -> str:
    return s[::-1]
```

**Why it happens:** Treating strings like mutable lists

---

### 6. **Not Stripping Whitespace**

```python
# ❌ WRONG: Doesn't handle leading/trailing spaces
def string_to_int(s: str) -> int:
    return int(s)  # ValueError: invalid literal for int() with base 10: ' 42 '

# ❌ WRONG: Manually removing only leading space
def parse(s: str) -> int:
    if s[0] == ' ':
        s = s[1:]
    return int(s)  # Still fails on trailing spaces

# ✅ CORRECT: Strip all whitespace
def string_to_int(s: str) -> int:
    s = s.strip()
    if not s:
        return 0
    return int(s)
```

**Why it happens:** Forgetting real-world input has whitespace

---

### 7. **Unicode and Special Characters**

```python
# ❌ WRONG: Assumes ASCII
def is_alpha(char: str) -> bool:
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'
# Fails on: 'ñ', 'ü', '中', '😀'

# ✅ CORRECT: Use built-in methods
def is_alpha(char: str) -> bool:
    return char.isalpha()

# ❌ WRONG: Length assumption
s = "hello😀"
print(len(s))  # 6 (emoji is 1 character)
# But in bytes: len(s.encode('utf-8')) = 10

# ✅ CORRECT: Be aware of unicode
# Use .isalpha(), .isdigit(), .isalnum() for unicode safety
```

**Why it happens:** Not considering international characters

---

## ✅ Comprehensive Testing Strategy

### Test Case Categories

#### 1. **Empty and Minimal**
```python
# Empty string
assert process("") == expected_empty

# Single character
assert process("a") == "a"

# Single word
assert longest_prefix(["a"]) == "a"
```

#### 2. **Whitespace Handling**
```python
# Leading/trailing spaces
assert string_to_int("  42  ") == 42

# Only spaces
assert string_to_int("   ") == 0

# Spaces between
assert reverse_words("a   b") == "b   a"
```

#### 3. **Case Variations**
```python
# Mixed case
assert is_palindrome("Aba") == True

# All uppercase
assert is_palindrome("RACECAR") == True

# All lowercase
assert is_palindrome("racecar") == True
```

#### 4. **Special Characters**
```python
# Punctuation
assert clean_string("hello, world!") == "hello world"

# Numbers
assert is_palindrome("A man, a plan, a canal: Panama") == True

# Unicode
assert length("café") == 4
assert length("你好") == 2
```

#### 5. **Boundary Conditions**
```python
# Maximum length
assert process("a" * 10000) == expected

# Numeric boundaries
assert string_to_int("2147483647") == 2**31 - 1   # INT_MAX
assert string_to_int("2147483648") == 2**31 - 1   # Overflow
assert string_to_int("-2147483648") == -2**31     # INT_MIN

# Empty array
assert longest_prefix([]) == ""
```

#### 6. **Edge Cases**
```python
# All same character
assert compress("aaaa") == "a4"

# No common prefix
assert longest_prefix(["abc", "def"]) == ""

# Complete match
assert longest_prefix(["abc", "abc"]) == "abc"

# Prefix of another
assert longest_prefix(["flower", "flow"]) == "flow"
```

#### 7. **Invalid Input**
```python
# Non-numeric in atoi
assert string_to_int("4193 with words") == 4193

# Invalid format
assert is_valid_number("abc") == False

# Mixed content
assert extract_digits("abc123def456") == [123, 456]
```

#### 8. **Performance Tests**
```python
# Large input
assert process("a" * 100000) completes in < 1 second

# Many small strings
assert longest_prefix(["a"] * 10000) completes quickly

# Deep nesting (if applicable)
assert process("(((" * 1000 + ")))" * 1000) handles deep recursion
```

---

## 💡 Templates & Code Patterns

### Template 1: String Building (Efficient)

```python
def build_string_efficiently(items: List[str]) -> str:
    """
    Build string from parts using list accumulation.
    Avoid repeated concatenation.
    """
    result = []

    for item in items:
        # Process and append
        processed = process(item)
        result.append(processed)

    return ''.join(result)  # Single join at end
```

---

### Template 2: Two Pointers (Reversal/Palindrome)

```python
def two_pointer_string(s: str) -> bool:
    """
    Process string from both ends toward center.
    Common for palindrome, reversal, matching.
    """
    left, right = 0, len(s) - 1

    while left < right:
        # Skip non-alphanumeric (optional)
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare or process
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True
```

---

### Template 3: String Parsing with State

```python
def parse_with_state(s: str) -> int:
    """
    Parse string sequentially, tracking state.
    Common for atoi, valid number, expression parsing.
    """
    s = s.strip()
    if not s:
        return default_value

    # Initialize state
    sign = 1
    result = 0
    i = 0

    # Handle sign
    if s[i] in '+-':
        sign = -1 if s[i] == '-' else 1
        i += 1

    # Process characters
    while i < len(s):
        char = s[i]

        if not char.isdigit():
            break

        # Update result
        result = result * 10 + int(char)

        # Overflow check (if needed)
        if result * sign > MAX_INT:
            return MAX_INT
        if result * sign < MIN_INT:
            return MIN_INT

        i += 1

    return result * sign
```

---

### Template 4: Sliding Window on String

```python
def sliding_window_string(s: str, k: int) -> int:
    """
    Find optimal substring with constraints.
    Common for longest/shortest substring problems.
    """
    char_count = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        # Expand window
        char_count[char] = char_count.get(char, 0) + 1

        # Shrink window if constraint violated
        while violates_constraint(char_count, k):
            char_count[s[left]] -= 1
            if char_count[s[left]] == 0:
                del char_count[s[left]]
            left += 1

        # Update result
        max_length = max(max_length, right - left + 1)

    return max_length
```

---

### Template 5: Vertical Scan (String Array)

```python
def vertical_scan(strs: List[str]) -> str:
    """
    Compare strings column-by-column.
    Common for longest common prefix.
    """
    if not strs:
        return ""

    for i in range(len(strs[0])):
        char = strs[0][i]

        # Check all strings at position i
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]

    return strs[0]
```

---

### Template 6: String Transformation with Split/Join

```python
def transform_words(s: str) -> str:
    """
    Transform at word level.
    Common for word reversal, case conversion, formatting.
    """
    words = s.split()  # Split on whitespace

    transformed = []
    for i, word in enumerate(words):
        # Apply transformation
        new_word = transform(word, i)
        transformed.append(new_word)

    return ' '.join(transformed)  # Join with space
```

---

## 💎 Mastery Tips & Mental Models

### Mental Model 1: String as Immutable Array
Think of strings as **read-only character arrays**.
- ✅ Can read any position: `s[i]`
- ✅ Can iterate: `for char in s`
- ✅ Can slice (creates copy): `s[i:j]`
- ❌ Cannot modify: `s[i] = 'X'`

**When to convert to list:**
- Need to modify characters in place
- Building string character by character
- Swapping characters (reversal)

---

### Mental Model 2: String Building = Parts Assembly
Think of building strings like **assembling parts** in a factory.
- ❌ Bad: Glue each part immediately (O(n²) concatenation)
- ✅ Good: Collect all parts, assemble once (O(n) list + join)

```python
# Bad: Glue immediately
result = ""
for part in parts:
    result += part  # Re-glue entire result each time

# Good: Collect then assemble
result = []
for part in parts:
    result.append(part)  # Just add to collection
final = ''.join(result)  # Assemble once
```

---

### Mental Model 3: Parsing = State Machine
Think of parsing as a **finite state machine** moving between states.

```
State: START → SAW_SIGN → SAW_DIGIT → END
         |         |           |
      +-sign    0-9        0-9
```

**Key principles:**
- Each character determines next state
- Invalid character = error or stop
- Final state determines validity

---

### Mental Model 4: String Search = Pattern Sliding
Visualize pattern **sliding along text** like a window.

```
Text:    "ababcabcab"
Pattern: "abcab"

Position 0: ababc ≠ abcab
Position 1:  babc ≠ abcab
Position 2:   abc_ ≠ abcab
...
Position 5:     abcab = abcab ✓
```

---

### Recognition Patterns (When to Use What)

✅ **Use List + Join When:**
- Building string incrementally
- Modifying characters
- Reversing string
- Concatenating many parts

✅ **Use Two Pointers When:**
- Palindrome checking
- Reversing in-place (list)
- Comparing from both ends
- Removing duplicates

✅ **Use Sliding Window When:**
- Longest/shortest substring with constraint
- Fixed-size window moving across string
- Character frequency in range

✅ **Use HashMap When:**
- Character frequency counting
- Anagram detection
- Character position lookup
- Seen/unseen tracking

✅ **Use State Machine When:**
- Complex validation rules
- Multiple parse paths
- Sequential state transitions

❌ **Avoid String When:**
- Need frequent modifications → Use list
- Need O(1) membership → Use set
- Need key-value lookup → Use dict

---

### Complexity Patterns

**Common Time Complexities:**
- Character iteration: O(n)
- Slicing: O(k) where k = slice length
- Concatenation: O(n + m) per concat
- Join n strings: O(total characters)
- Built-in find/index: O(n) average, O(nm) worst
- Sorting: O(n log n)

**Space Optimization:**
- Use slicing views when possible (but they copy in Python)
- Process string in-place if input is list
- Avoid storing unnecessary intermediate strings

**When O(n²) is Acceptable:**
- n < 100 and code is simpler
- Readability matters more than performance
- Not in hot path or tight loop

---

### Interview Strategy

1. **Clarify Requirements:**
   - Case sensitive?
   - Handle whitespace?
   - Unicode or ASCII only?
   - Empty string valid input?

2. **Choose Approach:**
   - Identify pattern (parsing, transformation, search)
   - Select technique (two pointers, sliding window, state machine)
   - Plan data structure (list, set, dict)

3. **Handle Edge Cases:**
   - Empty string: `if not s: return default`
   - Single character: Base case
   - All same: Test uniformity
   - Very long: Test performance

4. **Optimize:**
   - Replace concatenation with list + join
   - Use built-ins: `str.startswith()`, `str.find()`
   - Consider early termination

5. **Test Mentally:**
   - Empty: ""
   - Single: "a"
   - Two: "ab"
   - Repeated: "aaaa"
   - Mixed: "a1B2c3"

---

## 📋 Problem List (by Frequency)

| # | Problem | Difficulty | Frequency |
|---|---------|------------|----------|
| 043 | [Longest Common Prefix](./043_longest_common_prefix.md) | EASY | 59.4% |
| 046 | [Diagonal Traverse](./046_diagonal_traverse.md) | MEDIUM | 56.0% |
| 047 | [Missing Ranges](./047_missing_ranges.md) | EASY | 56.0% |
| 058 | [Valid Number](./058_valid_number.md) | HARD | 47.0% |
| 067 | [String to Integer (atoi)](./067_string_to_integer_atoi.md) | MEDIUM | 40.7% |
| 095 | [Goat Latin](./095_goat_latin.md) | EASY | 32.0% |
| 097 | [Text Justification](./097_text_justification.md) | HARD | 32.0% |

---

[← Back to Main](../README.md)
