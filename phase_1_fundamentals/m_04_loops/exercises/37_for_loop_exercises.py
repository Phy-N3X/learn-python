# ============================================================
# MODULE 04 | EXERCISES 37 - for loop
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Write a for loop that prints each character of your name
# on a separate line.
# Then print "Done!" after the loop.
#
# Example (name = "Anna"):
# A
# n
# n
# a
# Done!

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what this code will print BEFORE running.
# Write your prediction as a comment before each print.
# Then run and verify.
#
# word = "loop"
#
# for letter in word:
#     # prediction: ?
#     print(letter.upper())
#
# # prediction: ?
# print(f"Last letter was: {letter}")
#
# total = 0
# for num in [10, 20, 30, 40]:
#     total += num
#     # prediction after each iteration:
#     # after 10: total = ?
#     # after 20: total = ?
#     # after 30: total = ?
#     # after 40: total = ?
#     print(total)
#
# Final question (answer as comment):
# What is the value of 'letter' after the first loop ends?
# Why does 'total' print 4 times?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL errors in the code below.
# Write what each error is as a comment next to the line.
# Then fix all errors so the code runs correctly.
#
# for letter in "Python"
#     print(letter)
#
# for in "DNA":
#     print(item)
#
# for char in "hello":
# print(char)
#
# for digit in 12345:
#     print(digit)
#
# for x in "abc":
#     print(x)
#     print(x * 2)
#         print("---")

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use a for loop to count the number of vowels
# in a word entered by the user.
# Vowels: a, e, i, o, u (both upper and lower case)
#
# Example interaction 1:
# Enter a word: Python
# Vowels in 'Python': 1
#
# Example interaction 2:
# Enter a word: bioinformatics
# Vowels in 'bioinformatics': 7
#
# Example interaction 3:
# Enter a word: rhythm
# Vowels in 'rhythm': 0

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Use a for loop to calculate the sum and product
# of all numbers in this list:
# numbers = [3, 7, 2, 9, 4, 6, 1, 8, 5]
#
# Print:
# - Sum of all numbers
# - Product of all numbers
# - Average (sum / count)
# - Maximum value (find it manually with the loop, no max() function)
# - Minimum value (find it manually, no min() function)
#
# Expected output:
# Numbers: [3, 7, 2, 9, 4, 6, 1, 8, 5]
# Sum: 45
# Product: 362880
# Average: 5.0
# Maximum: 9
# Minimum: 1

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Write a for loop that prints a multiplication table
# for a number entered by the user.
# Show results from 1 to 10.
#
# Example interaction (user enters 7):
# Enter a number: 7
# 7 × 1  =  7
# 7 × 2  = 14
# 7 × 3  = 21
# 7 × 4  = 28
# 7 × 5  = 35
# 7 × 6  = 42
# 7 × 7  = 49
# 7 × 8  = 56
# 7 × 9  = 63
# 7 × 10 = 70
#
# Tip: use f-string with alignment:
# f"{n} × {i:2d} = {result:3d}"

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Analyze a DNA sequence using a for loop.
# Use this sequence:
# dna = "ATGCGATACGCTTAAGGCCCCTAA"
#
# Count each base (A, T, C, G) separately.
# Calculate GC content = (G + C) / total * 100
# Find if the sequence starts with ATG (start codon).
# Find if the sequence ends with TAA, TAG, or TGA (stop codon).
#
# Print a full analysis report:
# Sequence: ATGCGATACGCTTAAGGCCCCTAA
# Length: 24 bp
# A count: X (X.X%)
# T count: X (X.X%)
# C count: X (X.X%)
# G count: X (X.X%)
# GC content: XX.X%
# Has START codon (ATG): Yes/No
# Has STOP codon: Yes/No (which one)

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a word analyzer using a for loop.
# Ask the user to enter a sentence.
# Split it into words using .split()
# (sentence.split() returns a list of words)
#
# For each word, print:
# - The word itself
# - Its length
# - Whether it starts with a capital letter
# - Whether it's longer than 5 characters
#
# At the end, print:
# - Total word count
# - Longest word
# - Average word length
#
# Example interaction:
# Enter a sentence: The quick brown fox jumps
# Word: 'The'    | Length: 3 | Capital: Yes | Long: No
# Word: 'quick'  | Length: 5 | Capital: No  | Long: No
# Word: 'brown'  | Length: 5 | Capital: No  | Long: No
# Word: 'fox'    | Length: 3 | Capital: No  | Long: No
# Word: 'jumps'  | Length: 5 | Capital: No  | Long: No
# Total words: 5
# Longest word: quick/brown/jumps (5 chars)
# Average length: 4.2

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this code step by step.
# Before each print, write your prediction as a comment.
# Then run and verify.
#
# data = ["DNA", "RNA", "protein", "lipid", "carbohydrate"]
# result = ""
# count = 0
#
# for item in data:
#     if len(item) > 4:
#         result += item[0].upper()
#         count += 1
#
# # prediction: result = ?
# print(result)
#
# # prediction: count = ?
# print(count)
#
# total_chars = 0
# for item in data:
#     total_chars += len(item)
#
# # prediction: total_chars = ?
# print(total_chars)
#
# longest = ""
# for item in data:
#     if len(item) > len(longest):
#         longest = item
#
# # prediction: longest = ?
# print(longest)
#
# Answer as comments:
# In the first loop, why is "DNA" and "RNA" excluded?
# What does item[0].upper() do?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a Caesar cipher encoder using a for loop.
# A Caesar cipher shifts each letter by a fixed number of positions.
# Example: shift=3, "ABC" → "DEF", "XYZ" → "ABC"
#
# Ask user for:
# - Message to encode
# - Shift amount (integer)
#
# Rules:
# - Only shift letters (A-Z, a-z)
# - Preserve case (uppercase stays uppercase)
# - Keep non-letter characters unchanged (spaces, punctuation)
# - Wrap around: Z + 1 = A
#
# Hint for shifting:
# For uppercase: chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
# For lowercase: chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
# ord() gives ASCII number, chr() converts back to character
#
# Example interaction:
# Enter message: Hello, World!
# Enter shift: 3
# Encoded: Khoor, Zruog!
#
# Also decode back by shifting in reverse and verify.

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a protein sequence statistics calculator.
# Use this protein sequence:
# protein = "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAPSVT"
#
# Using ONLY for loops and if statements (no built-in count()):
#
# Calculate:
# 1. Total length
# 2. Count of each amino acid type:
#    - Hydrophobic: A, V, I, L, M, F, W, P
#    - Hydrophilic: S, T, C, Y, N, Q
#    - Positive:    K, R, H
#    - Negative:    D, E
# 3. Isoelectric point estimate:
#    - Count positive residues (K, R, H)
#    - Count negative residues (D, E)
#    - Net charge = positive - negative
#    - If net > 0 → "Basic protein (pI > 7)"
#    - If net < 0 → "Acidic protein (pI < 7)"
#    - If net = 0 → "Neutral protein (pI ≈ 7)"
# 4. Has signal peptide? (starts with M followed by 5+ hydrophobic)
# 5. Molecular weight estimate: length × 110 Da
#
# Print a full protein analysis report.

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a text statistics analyzer.
# Ask the user for a paragraph of text.
#
# Using for loops, calculate:
# 1. Total characters (with spaces)
# 2. Total characters (without spaces)
# 3. Total words (split by spaces)
# 4. Total sentences (count . ! ?)
# 5. Average word length
# 6. Most common vowel (check a, e, i, o, u)
# 7. Count of uppercase letters
# 8. Count of lowercase letters
# 9. Count of digits in the text
# 10. Count of punctuation marks (. , ! ? ; : ' ")
# 11. Unique characters used (build a string of unique chars)
# 12. Is it a pangram? (contains every letter a-z)
#
# Print a formatted report with all statistics.
# Use only for loops (no built-in count(), sum(), etc.)
#
# Example interaction:
# Enter text: The quick brown fox jumps over the lazy dog.
# [full report printed]

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a DNA to protein translator using for loops.
# Translate a DNA sequence into a protein sequence.
#
# Rules:
# - Read the DNA in groups of 3 (codons)
# - Start translation at the first ATG
# - Stop at any STOP codon (TAA, TAG, TGA)
# - If no ATG found → "No start codon found"
# - If sequence length not divisible by 3 after ATG → handle remainder
#
# Use this simplified codon table (add more if you want):
# codon_table = {
#     "ATG": "Met", "TAA": "STOP", "TAG": "STOP", "TGA": "STOP",
#     "GCT": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
#     "TGT": "Cys", "TGC": "Cys",
#     "GAT": "Asp", "GAC": "Asp",
#     "GAA": "Glu", "GAG": "Glu",
#     "TTT": "Phe", "TTC": "Phe",
#     "GGT": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly",
#     "CAT": "His", "CAC": "His",
#     "ATT": "Ile", "ATC": "Ile", "ATA": "Ile",
#     "AAA": "Lys", "AAG": "Lys",
#     "TTG": "Leu", "TTA": "Leu", "CTT": "Leu", "CTC": "Leu",
#     "AAT": "Asn", "AAC": "Asn",
# }
#
# Test with: "XXATGGCTGATTTTAAATAA"
#            (XX before ATG should be ignored)
#
# Expected output:
# DNA: XXATGGCTGATTTTAAATAA
# ORF found at position 2
# Codons: ATG | GCT | GAT | TTT | AAA | TAA
# Protein: Met-Ala-Asp-Phe-Lys-[STOP]
# Protein length: 5 amino acids

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a mini spreadsheet calculator.
# Ask user for data as comma-separated numbers.
# Example input: "10, 25, 8, 42, 15, 33, 7, 28"
#
# Parse the input into a list of floats using a for loop
# (don't use list comprehension yet).
# Validate each value: skip non-numeric values and warn user.
#
# Calculate ALL of the following using ONLY for loops:
# 1. Count of valid numbers
# 2. Sum
# 3. Mean (average)
# 4. Minimum and maximum
# 5. Range (max - min)
# 6. Median (sort manually using a loop, then find middle)
#    Hint: implement bubble sort:
#    for i in range(len): for j in range(len-1): swap if needed
# 7. Variance = sum of (x - mean)² / count
# 8. Standard deviation = √variance
# 9. Count of values above mean
# 10. Count of values below mean
# 11. Percentiles: what % of values are below each quartile
#     Q1 (25th percentile), Q2 (50th = median), Q3 (75th)
#
# Print a full statistical report.

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a multi-sequence DNA analysis pipeline.
# Process multiple DNA sequences and generate a comparison report.
#
# sequences = {
#     "Sample_01": "ATGCGATACGCTTAAGGCCCCTAA",
#     "Sample_02": "ATGAAATTTGGGCCCTTTAGATAA",
#     "Sample_03": "TTTATGCCCGGGAAATTTCGATGA",
#     "Sample_04": "ATGATGATGATGATGATGATGTAA",
#     "Sample_05": "GCGCGCGCATCGATCGATCGATCG",
# }
#
# For EACH sequence, using for loops, calculate:
# 1. Length
# 2. Base counts (A, T, C, G)
# 3. GC content (%)
# 4. AT content (%)
# 5. Has valid start codon (ATG): yes/no, at which position
# 6. Has valid stop codon: yes/no, which one, at which position
# 7. Reading frame check: (length - start_pos) % 3 == 0
# 8. Number of ATG occurrences (possible internal starts)
# 9. Longest homopolymer run (e.g. AAAA = run of 4)
#    (same base repeated consecutively)
# 10. Reverse complement
#     (A↔T, C↔G, then reverse the whole string)
#
# Then generate a COMPARISON SUMMARY:
# - Which sequence has highest GC content?
# - Which sequence has the longest ORF (start to stop)?
# - Which sequence has the longest homopolymer run?
# - Average GC content across all sequences
# - How many sequences have both start AND stop codon?
#
# Print a formatted comparison table and summary report.
# ============================================================