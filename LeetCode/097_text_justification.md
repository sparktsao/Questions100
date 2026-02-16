# 097. Text Justification

**Difficulty:** HARD
**Frequency:** 32.0%
**Acceptance Rate:** 48.1%
**LeetCode Link:** [Text Justification](https://leetcode.com/problems/text-justification)

---

## Problem Description

Given an array of strings `words` and a width `maxWidth`, format the text such that each line has exactly `maxWidth` characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces `' '` when necessary so that each line has exactly `maxWidth` characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

**Note:**
- A word is defined as a character sequence consisting of non-space characters only.
- Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
- The input array words contains at least one word.

**Constraints:**
- 1 <= words.length <= 300
- 1 <= words[i].length <= 20
- words[i] consists of only English letters and symbols
- 1 <= maxWidth <= 100
- words[i].length <= maxWidth

---

## Examples

### Example 1
**Input:** `words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16`
**Output:**
```
[
  "This    is    an",
  "example  of text",
  "justification.  "
]
```
**Explanation:** The first line contains "This", "is", and "an" with 2 extra spaces distributed evenly. The second line has one word with only 1 space, so extra space goes to the left slot. The last line is left-justified.

### Example 2
**Input:** `words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16`
**Output:**
```
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
```
**Explanation:** Note that the last line is "shall be    " instead of "shall be", because the last line must be left-justified instead of fully-justified. Also note that the second line is also left-justified because it contains only one word.

### Example 3
**Input:** `words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20`
**Output:**
```
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
```
**Explanation:** Multiple lines with different space distributions, last line is left-justified

### Example 4
**Input:** `words = ["a"], maxWidth = 1`
**Output:** `["a"]`
**Explanation:** Single word that fits exactly in maxWidth

---

## Optimal Solution

### Implementation

```python
def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    """
    Text justification using greedy packing and space distribution.

    Time: O(n), Space: O(n) where n is total characters in all words
    """
    result = []
    i = 0

    while i < len(words):
        # Determine how many words fit in current line
        line_length = len(words[i])
        j = i + 1

        # Greedily pack words (each word needs at least 1 space after it)
        while j < len(words) and line_length + 1 + len(words[j]) <= maxWidth:
            line_length += 1 + len(words[j])
            j += 1

        # Build the justified line
        num_words = j - i
        num_spaces = maxWidth - line_length + (num_words - 1)

        # Check if this is the last line or line has only one word
        if j == len(words) or num_words == 1:
            # Left-justify
            line = ' '.join(words[i:j])
            line += ' ' * (maxWidth - len(line))
        else:
            # Fully justify - distribute spaces evenly
            gaps = num_words - 1
            spaces_per_gap = num_spaces // gaps
            extra_spaces = num_spaces % gaps

            line = ''
            for k in range(num_words - 1):
                line += words[i + k]
                line += ' ' * (spaces_per_gap + (1 if k < extra_spaces else 0))
            line += words[j - 1]

        result.append(line)
        i = j

    return result
```

### Complexity Analysis

**Time: O(n) - single pass through all words. Space: O(n) - output storage**

**Why This is Optimal:**
- Achieves best possible asymptotic complexity - must process each word at least once
- Greedy packing ensures optimal line utilization
- Space distribution algorithm runs in constant time per line
- Handles all edge cases: single word lines, last line, even/uneven space distribution
- No redundant computations or backtracking needed

---

## Categories & Tags

**Primary Topics:** Array, String, Simulation

**Difficulty Level:** HARD

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/text-justification)*
