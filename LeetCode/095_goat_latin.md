# 095. Goat Latin

**Difficulty:** EASY
**Frequency:** 32.0%
**Acceptance Rate:** 69.4%
**LeetCode Link:** [Goat Latin](https://leetcode.com/problems/goat-latin)

---

## Problem Description

You are given a string `sentence` that consists of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:
- If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
  - For example, the word "apple" becomes "applema".
- If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
  - For example, the word "goat" becomes "oatgma".
- Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
  - For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.

Return the final sentence representing the conversion from sentence to Goat Latin.

**Constraints:**
- 1 <= sentence.length <= 150
- sentence consists of English letters and spaces
- sentence has no leading or trailing spaces
- All words in sentence are separated by a single space

---

## Examples

### Example 1
**Input:** `sentence = "I speak Goat Latin"`
**Output:** `"Imaa peaksmaaa oatGmaaaa atinLmaaaaa"`
**Explanation:**
- "I" starts with vowel → "Ima" + "a" = "Imaa"
- "speak" starts with consonant → "peaksma" + "aa" = "peaksmaaa"
- "Goat" starts with consonant → "oatGma" + "aaa" = "oatGmaaaa"
- "Latin" starts with consonant → "atinLma" + "aaaa" = "atinLmaaaaa"

### Example 2
**Input:** `sentence = "The quick brown fox jumped over the lazy dog"`
**Output:** `"heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"`
**Explanation:** Each word is transformed according to Goat Latin rules

### Example 3
**Input:** `sentence = "Each word consists of lowercase and uppercase letters only"`
**Output:** `"Eachmaa ordwmaaa onsistscmaaaa ofmaaaaa owercaselmaaaaaa andmaaaaaaa uppercasemaaaaaaaa etterslmaaaaaaaaa onlymaaaaaaaaaa"`
**Explanation:** Vowel words get "ma" appended, consonant words get first letter moved to end

### Example 4
**Input:** `sentence = "apple"`
**Output:** `"applema"`
**Explanation:** Single word starting with vowel, first word gets one 'a' added

---

## Optimal Solution

### Implementation

```python
def toGoatLatin(sentence: str) -> str:
    """
    Convert sentence to Goat Latin by applying transformation rules.

    Time: O(n), Space: O(n) where n is length of sentence
    """
    vowels = set('aeiouAEIOU')
    words = sentence.split()
    result = []

    for i, word in enumerate(words):
        # Apply Goat Latin rules
        if word[0] in vowels:
            # Vowel: append "ma"
            goat_word = word + "ma"
        else:
            # Consonant: move first letter to end, append "ma"
            goat_word = word[1:] + word[0] + "ma"

        # Add 'a' based on word index (1-indexed)
        goat_word += 'a' * (i + 1)
        result.append(goat_word)

    return ' '.join(result)
```

### Alternative Implementation (More Concise)

```python
def toGoatLatin(sentence: str) -> str:
    """
    One-liner approach using list comprehension.

    Time: O(n), Space: O(n)
    """
    vowels = set('aeiouAEIOU')
    words = sentence.split()

    return ' '.join(
        (word if word[0] in vowels else word[1:] + word[0]) + 'ma' + 'a' * (i + 1)
        for i, word in enumerate(words)
    )
```

### Complexity Analysis

**Time: O(n) - where n is the length of the sentence. Space: O(n) - for storing the result**

**Why This is Optimal:**
- Single pass through the sentence
- Efficient string operations using join() instead of repeated concatenation
- Set lookup for vowels is O(1)
- Each word is processed exactly once
- Space complexity is optimal since we need to store the output

---

## Categories & Tags

**Primary Topics:** String

**Difficulty Level:** EASY

---

---

*Problem source: [LeetCode](https://leetcode.com/problems/goat-latin)*
