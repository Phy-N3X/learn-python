# ============================================================
# MODULE 02 | EXERCISES 03 - Slicing
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Create a variable 'language' = "Programming"
# Using slicing, print:
#   - first 4 characters
#   - last 4 characters
#   - characters from index 2 to index 6
# Expected output:
#   Prog
#   ming
#   ogra



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Using the string below, demonstrate the difference
# between omitting start and omitting stop.
# Print:
#   - word[:5]   and explain in a comment what it does
#   - word[5:]   and explain in a comment what it does
#   - word[:]    and explain in a comment what it does

word = "Bioinformatics"



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output of each slice BEFORE running.
# Write your prediction as a comment, then verify.

text = "Hello World"
# Prediction: ?
print(text[0:5])
# Prediction: ?
print(text[6:11])
# Prediction: ?
print(text[:5])
# Prediction: ?
print(text[6:])
# Prediction: ?
print(text[:])



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use NEGATIVE indexes in slices.
# Given: word = "Python"
# Print:
#   - last 3 characters using negative start
#   - everything except last character using negative stop
#   - everything except first and last character
# Add comments explaining each slice.



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Given the date string below, extract:
#   - year  (first 4 characters)
#   - month (characters 5 and 6)
#   - day   (last 2 characters)
# Print each with a label.
# Expected output:
#   Year: 2024
#   Month: 07
#   Day: 19

date = "2024-07-19"



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Given the filename below:
#   - Extract the name without extension (before the dot)
#   - Extract only the extension (after the dot, without dot)
#   - Extract the extension including the dot
# Use slicing. You may hardcode the index of the dot.
# Print each with a label.

filename = "genome_data.fasta"



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Demonstrate that slicing does NOT raise IndexError
# even when indexes are out of range.
# Given: word = "Python"
# Print the result of these slices and write a comment
# explaining what Python does in each case:
#   word[0:100]
#   word[-100:3]
#   word[10:20]
#   word[3:3]
#   word[5:2]



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use slicing to "fix" the strings below.
# Each string has a problem - use slicing (and concatenation
# if needed) to produce the correct result.
# Print the fixed version.
#
# a) word = "PPython"     → should be "Python"   (extra P at start)
# b) word = "Pythonn"     → should be "Python"   (extra n at end)
# c) word = "xPythonx"    → should be "Python"   (extra chars both sides)

a = "PPython"
b = "Pythonn"
c = "xPythonx"



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Given the DNA sequence below:
# A codon is a group of 3 nucleotides.
# Extract and print the first 4 codons using slicing.
# Label each codon (Codon 1, Codon 2, etc.)
# Expected output:
#   Codon 1: ATG
#   Codon 2: CCC
#   Codon 3: GCA
#   Codon 4: TTA

dna = "ATGCCCGCATTAGTCGA"



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Rearrange the date format using slicing.
# Input format:  "2024-03-15"  (YYYY-MM-DD)
# Output format: "15/03/2024"  (DD/MM/YYYY)
# Use slicing to extract parts and concatenation to rebuild.
# Print the result.

date = "2024-03-15"



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Use slicing to extract the username and domain
# from the email address below.
# Then print them with labels.
# Expected output:
#   Username: anna.kowalska
#   Domain: university.edu
#
# Hint: the @ symbol is at a specific index - find it first
# by counting manually, then use that index in your slice.

email = "anna.kowalska@university.edu"



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# This exercise combines slicing with string concatenation
# to rearrange text.
#
# Given: full_name = "Kowalska Anna"
# (surname first, then first name - separated by space)
#
# Rearrange it to: "Anna Kowalska"
# (first name first, then surname)
#
# Steps to think about:
#   1. Find where the space is (count manually)
#   2. Extract the surname using a slice
#   3. Extract the first name using a slice
#   4. Combine them in the new order
# Print the result.

full_name = "Kowalska Anna"



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Predict ALL outputs before running.
# This tests your understanding of the stop-is-excluded rule
# and negative indexes in slices.

word = "abcdefghij"
# word has 10 characters, indexes 0-9 (positive) / -10 to -1 (negative)

# Prediction: ?
print(word[2:5])
# Prediction: ?
print(word[-5:-2])
# Prediction: ?
print(word[1:-1])
# Prediction: ?
print(word[-3:])
# Prediction: ?
print(word[:-3])
# Prediction: ?
print(word[-5:5])
# Prediction: ?
print(word[5:-5])



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# You are given a product code in this format:
#   "CAT-PRODUCTNAME-2024-XL"
#    CAT       = category (3 chars)
#    -         = separator
#    PRODUCTNAME = variable length product name
#    -         = separator
#    2024      = year (4 chars)
#    -         = separator
#    XL        = size (2 chars)
#
# For the specific code below:
#   - Extract category      using a slice
#   - Extract product name  using a slice
#     (Hint: it starts at index 4 and ends before the second dash.
#      Count the index of the second dash manually.)
#   - Extract year          using a slice from the end (negative)
#   - Extract size          using a slice from the end (negative)
# Print all four with labels.

product_code = "ELE-UltraMonitor-2024-XL"



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# This is a multi-part challenge.
#
# Part A:
# Given: sentence = "The quick brown fox jumps over the lazy dog"
# Using ONLY slicing and concatenation (no other methods yet):
#   - Extract "quick" and store in variable
#   - Extract "fox" and store in variable
#   - Extract "lazy dog" and store in variable
#   - Build a new sentence: "The lazy dog jumps over the quick fox"
#     (you can use the original slices + string literals for the rest)
# Print the new sentence.
#
# Part B:
# Given: text = "abcdefghij"
# Using slicing, split it into THREE equal parts.
# Print each part on a separate line.
# Expected output:
#   abcd
#   efgh  ← wait, that's only 8... think carefully!
#   ij    ← what should the three parts actually be?
# Hint: 10 characters ÷ 3 is not even. How do you handle this?
# Try splitting as: first 3, next 3, remaining.
# Print and explain your approach in a comment.
#
# Part C:
# Using slicing, verify that these two operations give the same result:
#   1. word[:-1][:-1]   (slice twice)
#   2. word[:-2]        (slice once)
# Test with word = "Python"
# Print both results and compare with ==