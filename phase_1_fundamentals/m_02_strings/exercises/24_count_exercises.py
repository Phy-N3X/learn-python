# ============================================================
# MODULE 02 | EXERCISES 24 - .count()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Use .count() to count occurrences of various substrings.
# Print each result with a descriptive label.
# BEFORE running, predict each result as a comment.

text = "python programming is fun and python is powerful"

# Prediction: ?
print(text.count("python"))
# Prediction: ?
print(text.count("is"))
# Prediction: ?
print(text.count("and"))
# Prediction: ?
print(text.count("java"))
# Prediction: ?
print(text.count("p"))
# Prediction: ?
print(text.count(" "))



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate that .count() NEVER returns -1.
# Compare the behavior of .count() and .find()
# when the substring is NOT found.
# Print the results of both and write a comment
# explaining the difference.

text = "Hello World Python"
search = "Java"

# Use .count() - what does it return?
# Use .find() - what does it return?
# Write comments: which is safer? which is more informative?



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate case sensitivity.
# For the text below, count each variant separately.
# Then count all variants together using .lower().
# Print all results with labels.

text = "Python python PYTHON PyThOn programming"
# Count: "Python", "python", "PYTHON", "PyThOn"
# Then count all using .lower().count("python")



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Count characters in the word "mississippi".
# Count each unique letter and verify they sum to len(word).
# Print each letter count with a label.
# Print the verification result.

word = "mississippi"
# Count: 'm', 'i', 's', 'p'
# Verify: sum of all counts == len(word)



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Use .count() to count separators and infer structure.
# For each string:
#   a) Count the separator
#   b) Calculate the number of fields (count + 1)
#   c) Print: "X separators → Y fields"

csv   = "Anna,Kowalska,25,Warsaw,Poland,anna@email.com"
path  = "/home/user/documents/reports/file.txt"
date  = "2024-03-15"
email = "anna.kowalska@university.edu"



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Calculate GC content of DNA sequences.
# GC content = (G + C) / total * 100
# Print: "Sequence: X | GC content: Y%"
# Round to 1 decimal place.
# Also print individual counts of A, T, G, C.

dna1 = "ATGCCCGCATTAGTCGA"
dna2 = "AAAAAATTTTTT"
dna3 = "GCGCGCGCGCGC"
dna4 = "ATGATGATGATG"



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Understand NON-OVERLAPPING counting.
#
# Part A:
# Predict the output of each before running.
# Write detailed predictions as comments.

text1 = "aaaa"
# Prediction: ?
print(text1.count("aa"))

text2 = "aaaaa"
# Prediction: ?
print(text2.count("aa"))

text3 = "aaaaaa"
# Prediction: ?
print(text3.count("aa"))

text4 = "abababab"
# Prediction: ?
print(text4.count("aba"))

# Part B:
# Write a comment explaining the NON-OVERLAPPING rule
# step by step for text1 = "aaaa" and substring "aa".
# Show exactly which indices are matched.



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use .count() with start and end parameters.
# For the text below, count "the" in:
#   a) the full string
#   b) the first 20 characters only
#   c) from position 15 onward
#   d) between positions 10 and 30
# Print each result with a label.

text = "the cat sat on the mat and the cat near the tree"



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Email format validator using .count().
# A basic valid email has:
#   - Exactly 1 "@" symbol
#   - At least 1 "." after the "@"
#   - No spaces
# Check each email and print: "valid" or "invalid" with reason.

emails = [
    "anna@university.edu",
    "anna.kowalska@university.edu",
    "annaemailcom",
    "anna@@university.edu",
    "anna @university.edu",
    "anna@universityedu",
    "@university.edu",
    "anna@.edu",
]



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Word frequency analysis.
# Given the text below, count the frequency of each
# word in the list. Use .count() on the full text
# (or .lower() version for case-insensitive).
# Print a formatted frequency table.
# Sort is not needed - print in the order given.
# Format: "word          : X occurrence(s)"

text = """To be or not to be that is the question
Whether tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles"""

words_to_count = ["to", "be", "the", "is", "or", "of", "and", "not"]



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Validate a DNA sequence using .count().
# A valid DNA sequence should:
#   a) Contain ONLY A, T, G, C characters (uppercase)
#   b) Have length divisible by 3 (complete codons)
#   c) Start with ATG (start codon)
#   d) Contain at least one stop codon: TAA, TAG, or TGA
#
# For each sequence, check all four conditions.
# Print the result of each check (True/False) with a label.
# Print "VALID" if all pass, "INVALID" if any fail.

seq1 = "ATGCCCGCATAA"           # should be valid
seq2 = "ATGCCCGCATAG"           # also valid
seq3 = "atgcccgcataa"           # lowercase - invalid
seq4 = "ATGCCCGCATA"            # length not div by 3
seq5 = "CCCGCATAA"              # no ATG start
seq6 = "ATGCCCGCACCC"           # no stop codon



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL errors and unexpected behaviors in the code below.
# For each line write a comment explaining what's wrong
# or surprising. Then fix all actual errors.

text = "Hello World Python"

result = text.count()                   # Error: ?
print(result)

result2 = text.count("world")
print(result2)                          # Surprising? Explain.

if text.count("Java") == -1:            # Logic error: ?
    print("Not found")

result3 = text.count("o", 20)
print(result3)                          # Error or valid? What prints?

print(text.count("Hello") + "found")   # Error: ?



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Text composition analysis.
# Given the text below, analyze its composition using .count().
#
# Part A: Count each vowel (a, e, i, o, u) - case insensitive.
#         Print count and percentage of total characters.
# Part B: Count each sentence-ending punctuation (. ! ?)
#         Print total sentences.
# Part C: Count spaces and infer approximate word count.
#         Compare with len(text.split()).
# Part D: Count digits (0-9) - how many numbers are in the text?
# Part E: Print a summary: "X letters, Y digits, Z spaces, W other"

text = ("Python 3 was released in 2008! It improved on Python 2. "
        "Are you using Python 3? You should be! "
        "There are 2 major versions: Python 2 and Python 3.")



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Restriction enzyme analysis using .count().
#
# Part A:
# Count occurrences of each restriction site in the DNA.
# Print: "Enzyme: site | Count: X | Cuts DNA into Y fragments"
# (Fragments = count + 1 if count > 0, else 1)

dna = ("ATGCCCGAATTCGCATTAGAATTCGTCGAAAGCTTCGAATTCATG"
       "CCCAAGCTTGAATTCGCAAGCTTAATAG")

enzymes = {
    "EcoRI":  "GAATTC",
    "HindIII": "AAGCTT",
    "BamHI":  "GGATCC",
    "NotI":   "GCGGCCGC",
}
# Since we haven't covered dict iteration yet,
# access each enzyme manually:
# enzymes["EcoRI"], enzymes["HindIII"], etc.

# Part B:
# What is the total number of restriction sites across all enzymes?

# Part C:
# Which enzyme cuts the most? Which cuts the least?
# (Compare counts manually)

# Part D:
# Count how many complete codons (triplets) are in the DNA.
# A complete codon = 3 nucleotides.
# Print: total length, number of complete codons, leftover nucleotides.



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Multi-part challenge: comprehensive .count() analysis.
#
# Part A: Pangram checker
# A pangram contains every letter of the alphabet at least once.
# "The quick brown fox jumps over the lazy dog" is a pangram.
# Using .count() and .lower(), check if each sentence is a pangram.
# Print: "Pangram: True/False" and which letters are missing (if any).

sentence1 = "The quick brown fox jumps over the lazy dog"
sentence2 = "Python programming is fun and powerful"
sentence3 = "Pack my box with five dozen liquor jugs"

# Part B: String similarity (simple version)
# Count how many characters two strings have in common.
# For each unique character in string1, count its occurrences
# in both strings. The "overlap" for that char is min(count1, count2).
# Sum all overlaps = similarity score.

str1 = "programming"
str2 = "bioinformatics"
# Count overlap for each letter manually:
# (Hint: for each unique letter in str1, use .count() on both strings)
# Print the total overlap score.

# Part C: Advanced GC analysis
# Given a DNA sequence, use .count() with start/end to analyze
# GC content in different regions:
#   - First third of the sequence
#   - Middle third
#   - Last third
# Compare GC content across regions.
# Print: "Region 1: X% | Region 2: Y% | Region 3: Z%"

dna = "ATGCCCGCATTAGTCGAAATGCCCGGCATTATGAAACCC"

# Part D: Count-based string reconstruction
# Given only the counts (no loops yet - use what you know):
# Verify this claim:
# For any string s: s.count(c) for all unique chars c
# should sum to len(s).
# Test with "mississippi" - count m, i, s, p and verify sum = len.
# Then test with "Hello World" - count all unique chars manually
# (H, e, l, o, space, W, r, d) and verify.