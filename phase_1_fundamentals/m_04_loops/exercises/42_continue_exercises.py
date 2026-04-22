# ============================================================
# MODULE 04 | EXERCISES 42 - continue
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Use continue to print only specific numbers.
#
# Task A: Print numbers from 1 to 20, but skip multiples of 3.
# Expected: 1 2 4 5 7 8 10 11 13 14 16 17 19 20
#
# Task B: Print numbers from 1 to 30, but skip numbers
# that contain the digit '5' (5, 15, 25).
# Expected: 1 2 3 4 6 7 8 9 10 11 12 13 14 16 17 18 19 20 21 22 23 24 26 27 28 29 30
#
# Task C: Print numbers from 1 to 20, but skip numbers
# that are both even AND greater than 10 (12, 14, 16, 18, 20).
# Expected: 1 2 3 4 5 6 7 8 9 10 11 13 15 17 19
#
# Use a single for loop with continue for each task.

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what this code will print BEFORE running.
# Write your prediction as a comment before each section.
# Then run and verify.
#
# # Section A:
# for i in range(8):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")
# print()
# # prediction: ?
#
# # Section B:
# words = ["hello", "", "world", "  ", "python", ""]
# result = []
# for word in words:
#     if not word.strip():
#         continue
#     result.append(word.upper())
# # prediction: result = ?
# print(result)
#
# # Section C:
# total = 0
# i = 0
# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     total += i
# # prediction: total = ?
# print(total)
#
# # Section D:
# for i in range(4):
#     for j in range(4):
#         if i == j:
#             continue
#         print(f"{i}{j}", end=" ")
#     print()
# # prediction: ?
#
# Final question (answer as comment):
# In Section D, which cells are skipped and why?
# In Section C, why does total = 25 (or whatever)?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL errors in the code below.
# Write what each error is as a comment.
# Then fix all errors so the code runs correctly.
#
# # Error set 1:
# continue
#
# # Error set 2:
# for i in range(10):
#     print(i)
# continue
#
# # Error set 3:
# i = 0
# while i < 5:
#     if i % 2 == 0:
#         continue      # will this cause an infinite loop? why?
#     print(i)
#     i += 1
#
# # Error set 4:
# for i in range(5):
#     if i == 3:
#         continue
#         print(f"Skipping {i}")    # what's wrong here?
#     print(i)

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use continue to clean a DNA sequence.
# The sequence may contain spaces, numbers, lowercase letters,
# and invalid characters.
#
# raw = "ATcg 123 ATCG\nXYZ ATCG atcg TTTT"
#
# Using a for loop with continue:
# 1. Skip spaces
# 2. Skip newline characters (\n)
# 3. Skip digits (0-9)
# 4. Skip lowercase letters (convert to uppercase first, then check)
# 5. Skip any character not in ATCG
#
# Build the clean DNA sequence from valid bases only.
# Print the original and cleaned version.
# Print how many characters were skipped in each category.
#
# Expected output:
# Original: ATcg 123 ATCG\nXYZ ATCG atcg TTTT
# Cleaned: ATCGATCGATCGTTTT
# Skipped: X spaces, X newlines, X digits, X lowercase, X invalid

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Use continue to implement a simple number filter.
# Ask user for a list of numbers (comma-separated).
# Parse them into individual values.
# Using a for loop with continue, collect only:
# - Numbers that are positive
# - Numbers that are less than 1000
# - Numbers that are not equal to 42 (the "forbidden" number)
# - Numbers that are integers (whole numbers, no decimal part)
#
# For each skipped number, print WHY it was skipped.
# At the end, print the collected numbers and their sum.
#
# Example interaction:
# Enter numbers: 5, -3, 42, 1500, 7.5, 100, 8, -1
# -3: skipped (negative)
# 42: skipped (forbidden number)
# 1500: skipped (too large)
# 7.5: skipped (not an integer)
# -1: skipped (negative)
# Collected: [5, 100, 8]
# Sum: 113

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a data validation pipeline using continue.
# Process a list of "student records" (tuples).
# Skip records that fail any validation check.
#
# students = [
#     ("Anna Kowalski", 22, 3.8, "Biology"),
#     ("", 20, 3.5, "Chemistry"),          # empty name
#     ("Bob Smith", -1, 3.2, "Physics"),   # invalid age
#     ("Carol Jones", 25, 5.0, "Biology"), # GPA > 4.0
#     ("David Brown", 21, 3.1, ""),        # empty major
#     ("Eve Wilson", 19, 2.8, "Math"),
#     ("Frank Lee", 200, 3.5, "Biology"),  # age too large
#     ("Grace Kim", 23, 3.9, "Chemistry"),
# ]
#
# Validation rules (use continue for each failed rule):
# 1. Name must not be empty and must have at least 2 words
# 2. Age must be between 18 and 100
# 3. GPA must be between 0.0 and 4.0
# 4. Major must not be empty
#
# For each skipped record, print which rule it failed.
# For each valid record, print a formatted summary line.
# At the end, print statistics: total, valid, rejected, avg GPA.

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a word statistics analyzer using continue.
# Ask user for a paragraph of text.
# Process each word using a for loop with continue.
#
# Skip words that:
# - Are shorter than 3 characters
# - Are already in your "processed" list (duplicates)
# - Are pure punctuation (all chars are punctuation)
# - Start with a capital letter (proper nouns)
#
# For each valid word, calculate and print:
# - The word (lowercase)
# - Its length
# - Whether it's a palindrome
# - Number of vowels it contains
#
# After processing, print:
# - Total words in text
# - Words skipped (with reason counts)
# - Words processed
# - Longest processed word
# - Average length of processed words

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use continue in a while loop to simulate
# a quality control process.
#
# Simulate reading sensor data:
# Use random.randint(1, 100) to generate "sensor readings"
# Keep reading until you have collected 10 VALID readings.
#
# Skip readings that are:
# - Less than 20 (too low - sensor error)
# - Greater than 80 (too high - sensor error)
# - Equal to the previous valid reading (duplicate)
# - A multiple of 7 (calibration artifact)
#
# Track:
# - Total readings generated
# - Readings skipped (with counts per reason)
# - Valid readings collected
#
# After collecting 10 valid readings:
# - Print all valid readings
# - Print statistics (min, max, mean)
# - Print skip efficiency: how many total were needed
#
# Use while True with continue for skips and
# break when 10 valid readings are collected.

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this continue code step by step.
# Before each print or accumulation, write your prediction.
# Then run and verify.
#
# # Block A:
# data = [5, 0, 3, 0, 8, 1, 0, 4]
# result = []
# for i in range(len(data)):
#     if data[i] == 0:
#         continue
#     if i > 0 and data[i-1] == 0:
#         result.append(data[i] * 10)
#         continue
#     result.append(data[i])
# # prediction: result = ?
# print(result)
#
# # Block B:
# text = "Hello World Python"
# vowels = "aeiouAEIOU"
# consonant_count = 0
# for char in text:
#     if not char.isalpha():
#         continue
#     if char in vowels:
#         continue
#     consonant_count += 1
# # prediction: consonant_count = ?
# print(consonant_count)
#
# # Block C: What does this print?
# for i in range(1, 6):
#     for j in range(1, 6):
#         if i + j > 6:
#             continue
#         if i == j:
#             continue
#         print(f"{i}+{j}={i+j}", end=" ")
#     print()
# # prediction: ?
#
# Answer as comments:
# In Block A, why do some zeros cause the next value to be *10?
# In Block C, list all the (i,j) combinations that get printed.

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a protein sequence quality filter using continue.
# The filter processes sequences and skips problematic ones.
#
# sequences = [
#     ("P001", "MKTAYIAKQRQISFVK"),
#     ("P002", "MKTAYIAK"),           # too short (< 10 aa)
#     ("P003", ""),                   # empty
#     ("P004", "BKTAYIAKQRQISFVK"),   # invalid aa 'B'
#     ("P005", "MKTAYIAKQRQISFVKMKTAYIAKQRQISFVKMKTAYIAK"),  # too long > 30
#     ("P006", "MKTAYIAKQRQISFVKSHFS"),
#     ("P007", "AAAAAAAAAAAAAAAA"),   # low complexity (all same)
#     ("P008", "MKTAYIAKQRQISFVK"),   # duplicate of P001
# ]
#
# Using continue, skip sequences that:
# 1. Are empty
# 2. Are shorter than 10 amino acids
# 3. Are longer than 30 amino acids
# 4. Contain invalid amino acid codes (valid: ACDEFGHIKLMNPQRSTVWY)
# 5. Have low complexity: any single amino acid appears > 50% of length
# 6. Are duplicates of already processed sequences
#
# For each skipped sequence, print the ID and reason.
# For valid sequences, calculate and print:
# - Length
# - Composition: % hydrophobic (AVILMFWP), % charged (KRHDEC), % other
# - Has start Met (M at position 0)?
# - Estimated molecular weight (length × 110 Da)
#
# Print summary statistics at the end.

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a financial data processor using continue.
# Process a series of financial transactions.
#
# transactions = [
#     ("2024-01-01", "deposit",    1000.00, "salary"),
#     ("2024-01-02", "withdrawal",  150.00, "groceries"),
#     ("2024-01-03", "withdrawal", 2000.00, "rent"),
#     ("2024-01-04", "transfer",    500.00, ""),        # empty description
#     ("2024-01-05", "deposit",      -50.00, "refund"), # negative deposit
#     ("2024-01-06", "withdrawal",   75.50, "utilities"),
#     ("2024-01-07", "invalid",     100.00, "misc"),    # invalid type
#     ("2024-01-08", "deposit",    2500.00, "bonus"),
#     ("2024-01-09", "withdrawal",    0.00, "nothing"), # zero amount
#     ("2024-01-10", "withdrawal",  200.00, "shopping"),
# ]
#
# Using continue, skip transactions that:
# 1. Have empty or missing description
# 2. Have negative amount (unless it's a correction)
# 3. Have zero amount
# 4. Have invalid transaction type (only: deposit, withdrawal, transfer)
# 5. Would make balance go below -500 (overdraft limit)
#
# Starting balance: 0.00 PLN
# For valid transactions:
# - Update running balance
# - Print transaction details with running balance
# - Mark large transactions (> 1000 PLN) with ⚠
#
# After all transactions:
# - Print final balance
# - Total deposited vs total withdrawn
# - Number of skipped transactions (with reason counts)
# - Largest single transaction

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a codon frequency analyzer that skips
# ambiguous and incomplete codons.
#
# Read a DNA sequence with the following issues:
# dna = ("ATG AAA TTT GGG CCC TTT AGA TAA GCT GAT"
#        "CGA TCG NNN ATG GCT ATC GAT CGA TCG AAA"
#        "TTT GGG CCC ATG TAA ATG CGA TAC GCT TAA"
#        "GGC CCN TAA ATC GAT CGA TCG XX ATG")
#
# Clean and process:
# 1. Remove spaces (join all without spaces)
# 2. Process in codons of 3 using range(0, len, 3)
#
# Skip codons using continue if:
# - Length is not exactly 3 (partial codon at end)
# - Contains any character not in ATCG
# - Is before the first ATG (find ATG first, then start counting)
# - Is after a STOP codon (TAA, TAG, TGA)
#
# For valid codons:
# - Count frequency of each codon
# - Classify: START, STOP, or coding
# - Track GC content per codon position (1st, 2nd, 3rd base)
#
# Print:
# - Total bases, total codons attempted, valid codons
# - Codon frequency table (sorted by frequency)
# - GC content at each codon position
# - ORF boundaries (start to stop)

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a multi-pass text processor using continue
# to implement a mini markup language parser.
#
# The "markup" uses these tags:
# ## text  → header (print in UPPERCASE with === border)
# -- text  → comment (skip/don't print)
# >> text  → quote (print indented with |)
# !! text  → warning (print with ⚠ prefix)
# ** text  → emphasis (print surrounded by ***)
# Normal lines → print as-is
# Empty lines → skip (continue)
# Lines starting with # (single) → skip (comment)
#
# document = """
# ## Introduction to Python
# This is a normal paragraph about Python.
# -- This is a hidden comment
# >> Guido van Rossum created Python in 1991.
# !! Python 2 is no longer supported.
# # This is also a comment
# ** Python is great for bioinformatics! **
#
# ## Data Types
# Python has several built-in data types.
# -- Author note: add more detail here
# >> Integers, floats, strings, lists, tuples, dicts.
# !! Always use type hints in production code.
# """
#
# Process each line using continue for lines to skip.
# For lines to process, determine the tag type.
# Render each line according to its tag.
#
# Also count: headers, quotes, warnings, emphases, normals, skipped.
# Print the rendered document followed by statistics.

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a genome annotation filter using continue.
# Process a simulated genome feature table.
#
# features = [
#     {"type": "gene", "start": 100, "end": 500, "strand": "+",
#      "name": "geneA", "product": "hypothetical protein"},
#     {"type": "CDS", "start": 100, "end": 500, "strand": "+",
#      "name": "geneA_CDS", "product": "DNA polymerase"},
#     {"type": "gene", "start": 200, "end": 300, "strand": "-",
#      "name": "geneB", "product": ""},              # no product
#     {"type": "repeat", "start": 600, "end": 700, "strand": "+",
#      "name": "rep1", "product": "transposase"},
#     {"type": "CDS", "start": 800, "end": 700, "strand": "+",
#      "name": "bad_CDS", "product": "kinase"},      # start > end!
#     {"type": "gene", "start": 1000, "end": 2000, "strand": "?",
#      "name": "geneC", "product": "helicase"},      # invalid strand
#     {"type": "CDS", "start": 1000, "end": 2001, "strand": "+",
#      "name": "geneC_CDS", "product": "helicase"},  # length not %3
#     {"type": "gene", "start": 3000, "end": 4500, "strand": "-",
#      "name": "geneD", "product": "RNA polymerase"},
#     {"type": "CDS", "start": 3000, "end": 4500, "strand": "-",
#      "name": "geneD_CDS", "product": "RNA polymerase"},
#     {"type": "misc", "start": 100, "end": 200, "strand": "+",
#      "name": "misc1", "product": "unknown"},
# ]
#
# Using continue, skip features that:
# 1. Type is not "gene" or "CDS" (skip misc, repeat, etc.)
# 2. Have empty product description
# 3. Have start > end (invalid coordinates)
# 4. Have invalid strand (not "+" or "-")
# 5. Are CDS with length not divisible by 3
#    (end - start + 1 must be divisible by 3)
# 6. Overlap with a previously processed feature of same type
#    (check if start/end range overlaps with any in processed list)
#
# For valid features:
# - Calculate length
# - Determine feature class: short (<300bp), medium (300-1000bp), long (>1000bp)
# - For CDS: estimate protein length (DNA length / 3)
# - Assign a quality score: 10 - (number of warnings)
#   Warnings: product contains "hypothetical", length < 100bp
#
# Print a formatted genome annotation report:
# - Feature table with all valid features
# - Skip log with reasons
# - Summary statistics by feature type
# - Features sorted by quality score

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a comprehensive RNA-seq data processor using continue.
# This simulates processing gene expression data.
#
# gene_expression = {
#     "GENE001": [120, 135, 128, 0, 142],     # one zero (missing)
#     "GENE002": [0, 0, 0, 0, 0],             # all zeros (not expressed)
#     "GENE003": [5000, 4800, 5200, 4900, 5100],  # highly expressed
#     "GENE004": [10, 12, 11, 10000, 13],     # outlier in sample 4
#     "GENE005": [45, 52, 48, 50, 47],
#     "GENE006": [1, 2, 1, 2, 1],             # too low expression
#     "GENE007": [200, 195, 205, 198, 202],
#     "GENE008": [None, 150, 160, 145, 155],  # missing value
#     "GENE009": [80, 75, 85, 78, 82],
#     "GENE010": [300, 310, 290, 305, 295],
# }
#
# sample_names = ["Control1", "Control2", "Treat1", "Treat2", "Treat3"]
#
# Processing pipeline (use continue for skips at each step):
#
# Step 1 - Data quality filter:
# Skip genes where:
# - Any value is None (missing data)
# - More than 1 value is 0 (not reliably expressed)
# - Mean expression < 20 (below detection threshold)
#
# Step 2 - Outlier detection (for remaining genes):
# Skip genes with outliers where:
# - Any value is > 3 standard deviations from the mean
# (Use: mean = sum/n, std = sqrt(sum((x-mean)^2)/n))
#
# Step 3 - Statistical analysis (for clean genes):
# Calculate:
# - Mean expression for control samples (samples 0,1)
# - Mean expression for treatment samples (samples 2,3,4)
# - Fold change = treatment_mean / control_mean
# - Skip genes where fold change is between 0.5 and 2.0
#   (not differentially expressed)
#
# Step 4 - Classification of remaining (DE) genes:
# - Up-regulated: fold_change > 2.0
# - Down-regulated: fold_change < 0.5
# - Calculate p-value approximation: 1 / (abs(log2(fold_change)) + 1)
#   (simplified - not real statistics)
#
# Print:
# - Complete processing log with skip reasons at each step
# - Final list of differentially expressed genes
# - Volcano plot (text-based): x=log2(FC), y=-log10(p-value)
# - Summary statistics
# ============================================================