# Levenshtein Distance Calculator

A small interactive Python script that computes the **Levenshtein distance** between two words and shows the steps needed to turn the first one into the second.

## What is the Levenshtein distance?

The Levenshtein distance is the **minimum number of single-character edits** (insertion, deletion, substitution) needed to turn one string into another, with cost 1 per edit. It is named after the Soviet mathematician Vladimir Levenshtein, who introduced it in 1965. It is used in spellchecking, approximate search, OCR, speech recognition and biological sequence comparison.

Example: `kitten → sitting` requires **3 edits**.

## Usage

Follow the prompts:

1. Type the **first word**.
2. Type the **second word**.
3. The script prints the distance and each edit step, numbered.
4. Choose:
   - **1** → continue from the last word (type only one new word).
   - **2** → compare two completely new words.
5. Answer `y`/`n` when asked whether you want to keep going.

## Example

```
First word:  kitten
Second word: sitting

Distance: 3

1. sitten
2. sittin
3. sitting

Do you want to enter another word? (y/n): n

Do you want to enter a new word? (y/n): n
```

## How it works

The script uses **dynamic programming**: it builds a matrix `dp` where `dp[i][j]` is the distance between the first `i` characters of the first word and the first `j` characters of the second. Each cell is the minimum of:

- `dp[i-1][j] + 1` → deletion
- `dp[i][j-1] + 1` → insertion
- `dp[i-1][j-1] + (a[i-1] != b[j-1])` → substitution (0 if equal)

The final answer is `dp[m][n]`. The step-by-step output is obtained by walking the matrix backwards and applying each operation to a copy of the first word.

## Complexity

- **Time:** `O(m · n)`
- **Space:** `O(m · n)` (full matrix needed for the step-by-step output)

## Author

[Andrea De Vita](https://github.com/andreadevita99)

## License

All rights reserved. This project is provided for demonstration purposes only. No permission is granted to use, copy, modify, merge, publish, distribute, sublicense, or otherwise reproduce any part of this software without explicit written consent from the author. Unauthorized use, modification, or redistribution is strictly prohibited.
