# ============================================================
# MODULE 04 | EXERCISES 38 - range()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Without running the code, predict what list each range()
# will produce. Write your prediction as a comment.
# Then verify by running list(range(...)).
#
# list(range(6))            # prediction: ?
# list(range(1, 6))         # prediction: ?
# list(range(2, 10))        # prediction: ?
# list(range(0, 20, 4))     # prediction: ?
# list(range(10, 0, -1))    # prediction: ?
# list(range(5, -1, -1))    # prediction: ?
# list(range(1, 10, 2))     # prediction: ?
# list(range(0, 10, 3))     # prediction: ?
# list(range(10, 1, -3))    # prediction: ?
# list(range(5, 5))         # prediction: ?
# list(range(5, 0))         # prediction: ?
# list(range(0, -10, -2))   # prediction: ?
#
# Final questions (answer as comments):
# Why is range(5, 0) empty?
# What's the difference between range(5) and range(1, 6)?
# How many elements does range(0, 100, 10) have?

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL errors in the range() calls below.
# Write what each error is as a comment.
# Then fix all errors so the code runs correctly.
#
# for i in range(1, 10, 0):
#     print(i)
#
# for i in range(1.0, 10.0):
#     print(i)
#
# for i in range("a", "z"):
#     print(i)
#
# r = range(5)
# print(r)
#
# for i in range(10, 0):
#     print(i)

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Use range() to print the following sequences.
# Each sequence on one line, numbers separated by spaces.
# Use ONLY range() - do not type out the numbers manually.
#
# 1. Numbers from 1 to 10
# 2. Numbers from 0 to 100 in steps of 10
# 3. Even numbers from 2 to 20
# 4. Odd numbers from 1 to 19
# 5. Countdown from 10 to 1
# 6. Numbers from 5 to 50 in steps of 5
# 7. Powers of 2: 1, 2, 4, 8, 16, 32, 64, 128
#    (hint: use i as exponent: 2**i)
# 8. Numbers from -5 to 5
#
# Expected output:
# 1 2 3 4 5 6 7 8 9 10
# 0 10 20 30 40 50 60 70 80 90 100
# 2 4 6 8 10 12 14 16 18 20
# ... etc.

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use range() to print the multiplication table
# for numbers 1 through 5.
# Each row is one number's table (1× to 10×).
#
# Expected output:
# 1 × 1 =  1   1 × 2 =  2  ...  1 × 10 = 10
# 2 × 1 =  2   2 × 2 =  4  ...  2 × 10 = 20
# ...
# 5 × 1 =  5   5 × 2 = 10  ...  5 × 10 = 50
#
# Print each table on its own line.
# Format the result with alignment:
# f"{n} × {i:2d} = {n*i:3d}"

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Create a Celsius to Fahrenheit conversion table
# using range().
#
# Requirements:
# - Start at -20°C, end at 100°C, step of 5°C
# - Formula: F = C × 9/5 + 32
# - Print a header and separator line
# - Mark "Freezing point" at 0°C
# - Mark "Body temperature" at 37°C (nearest in range)
# - Mark "Boiling point" at 100°C
#
# Expected output format:
# ================================
#  Celsius │ Fahrenheit │ Note
# ================================
#      -20 │      -4.0  │
#      -15 │       5.0  │
#        0 │      32.0  │ ← Freezing point
#       35 │      95.0  │
#       40 │     104.0  │ ← Near body temp
#      100 │     212.0  │ ← Boiling point
# ================================

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use range() to calculate the following mathematical values.
# Show your work (print each step):
#
# 1. Sum of all integers from 1 to 1000
#    (verify: should be 500500)
#
# 2. Sum of all even integers from 2 to 1000
#    (verify: should be 250500)
#
# 3. Sum of all odd integers from 1 to 999
#    (verify: should be 250000)
#
# 4. Product of integers from 1 to 12 (12!)
#    (verify: should be 479001600)
#
# 5. Sum of squares from 1 to 10: 1² + 2² + ... + 10²
#    (verify: should be 385)
#
# 6. Sum of cubes from 1 to 10: 1³ + 2³ + ... + 10³
#    (verify: should be 3025)
#
# Print each result with a clear label and verification.

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Generate DNA codons systematically using range().
# A DNA sequence is 60 bases long (20 codons).
#
# dna = "ATGCGATACGCTTAAGGCCCCTAAATCGATCGATCGTTTATGCCCGGGAAA"
# (use only first 60 chars if needed, or this 51-char version)
#
# Use range() with step=3 to:
# 1. Print each codon with its position number (1-indexed)
# 2. Count how many codons are START codons (ATG)
# 3. Count how many codons are STOP codons (TAA, TAG, TGA)
# 4. Find the position of the FIRST stop codon
# 5. Count how many codons have GC content >= 67% (2 or more G/C)
#
# Print a full codon report.

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a visual pattern generator using range().
# Print ALL of the following patterns using loops:
#
# Pattern 1 - Right triangle (size 6):
# *
# **
# ***
# ****
# *****
# ******
#
# Pattern 2 - Inverted triangle (size 6):
# ******
# *****
# ****
# ***
# **
# *
#
# Pattern 3 - Number triangle:
# 1
# 12
# 123
# 1234
# 12345
#
# Pattern 4 - Pyramid (size 5):
#     *
#    ***
#   *****
#  *******
# *********
#
# Pattern 5 - Diamond (size 5):
#     *
#    ***
#   *****
#    ***
#     *
#
# Use range() for all loops. No hardcoded strings.

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this code and predict ALL outputs.
# Write predictions as comments before each print.
# Then run and verify.
#
# # Block 1:
# result = 0
# for i in range(1, 6):
#     result += i * i
# # prediction: result = ?
# print(result)
#
# # Block 2:
# items = []
# for i in range(0, 20, 3):
#     if i % 2 == 0:
#         items.append(i)
# # prediction: items = ?
# print(items)
#
# # Block 3:
# text = ""
# for i in range(5, 0, -1):
#     text += str(i)
# # prediction: text = ?
# print(text)
#
# # Block 4:
# count = 0
# for i in range(2, 50):
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#     if is_prime:
#         count += 1
# # prediction: count = ?
# print(count)
#
# Answer as comments:
# In block 2, why doesn't 3, 9, 15 appear in items?
# In block 4, what is being counted?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a number analysis tool using range().
# Ask user for a number N (between 2 and 1000).
#
# Using range(), find and display:
# 1. All divisors of N
# 2. Whether N is prime (no divisors except 1 and itself)
# 3. Whether N is perfect (sum of divisors = N)
#    Perfect numbers: 6 (1+2+3=6), 28 (1+2+4+7+14=28)
# 4. Whether N is a perfect square
# 5. The prime factorization of N
#    Example: 12 = 2² × 3¹
# 6. Sum of all divisors
# 7. Count of divisors
#
# Example interaction:
# Enter a number: 28
# Divisors of 28: 1, 2, 4, 7, 14, 28
# Count: 6
# Sum: 56
# Prime? No
# Perfect? Yes! (1 + 2 + 4 + 7 + 14 = 28)
# Perfect square? No
# Prime factorization: 2² × 7¹

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create an ASCII art generator using range().
#
# Ask the user for:
# - A character to draw with (e.g. *, #, @, ♦)
# - Size (integer, e.g. 7)
# - Shape: square / rectangle / triangle / diamond / hourglass
#
# Generate the shape using only range() loops.
#
# Requirements for each shape:
# square: size × size grid of characters
# rectangle: size wide, size//2 tall
# triangle: growing from 1 to size (right-aligned)
# diamond: grows from 1 to size, then shrinks (centered)
# hourglass: starts wide, narrows to 1, then grows back
#
# Example interaction (char=*, size=5, shape=diamond):
#   *
#  ***
# *****
#  ***
#   *
#
# Example (char=#, size=5, shape=hourglass):
# #####
#  ###
#   #
#  ###
# #####

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a codon frequency analyzer using range() and a sequence.
#
# Use this long DNA sequence:
# dna = ("ATGAAATTTGGGCCCTTTAGATAAGCTGATCGATCG"
#        "ATGGCTATCGATCGATCGAAATTTGGGCCCATGTAA"
#        "ATGCGATACGCTTAAGGCCCCTAAATCGATCGATCG")
#
# Using range() with step=3:
# 1. Extract ALL codons from the sequence
# 2. Build a frequency dictionary (count each codon)
#    Use a for loop to count - do NOT use .count()
# 3. Find the most frequent codon
# 4. Find the least frequent codon (that appears at least once)
# 5. Count how many UNIQUE codons appear
# 6. Calculate what % of codons are:
#    - START codons (ATG)
#    - STOP codons (TAA, TAG, TGA)
#    - GC-rich (contain 2 or 3 G/C bases)
# 7. Print a sorted frequency table (most frequent first)
#    Show: rank, codon, count, percentage bar
#
# Expected output format:
# Total codons: X
# Unique codons: X
# ┌────────┬───────┬───────┬──────────────────┐
# │ Rank   │ Codon │ Count │ Frequency        │
# ├────────┼───────┼───────┼──────────────────┤
# │  1     │ ATG   │   3   │ ████             │
# ...

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a mathematical sequence explorer using range().
#
# Ask the user to choose a sequence type:
# 1. Arithmetic sequence: a, a+d, a+2d, ...
# 2. Geometric sequence: a, a*r, a*r², ...
# 3. Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, ...
# 4. Square numbers: 1, 4, 9, 16, 25, ...
# 5. Triangular numbers: 1, 3, 6, 10, 15, ...
# 6. Prime numbers
#
# Ask user for:
# - Sequence type (1-6)
# - How many terms to generate (N)
# - For arithmetic: starting value (a) and common difference (d)
# - For geometric: starting value (a) and common ratio (r)
#
# For each sequence, calculate and print:
# - The first N terms
# - Sum of the sequence
# - Mean of the sequence
# - Largest term
# - Smallest term
# - Whether the sequence is increasing, decreasing, or mixed
#
# Use range() for all iteration.
# Format output as a numbered list with a running sum column.
#
# Example interaction (Fibonacci, N=10):
# Term  1:   0  │ Running sum:    0
# Term  2:   1  │ Running sum:    1
# Term  3:   1  │ Running sum:    2
# Term  4:   2  │ Running sum:    4
# ...
# Term 10:  34  │ Running sum:   88
# Statistics: sum=88, mean=8.8, min=0, max=34

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a scientific measurement range generator.
# In science, you often need to test values across a range
# with different scales (linear, logarithmic, etc.)
#
# Create a system that generates measurement series:
#
# Ask user for:
# - Scale type: linear / exponential / logarithmic / custom
# - Start value (float)
# - End value (float)
# - Number of points (integer)
#
# For LINEAR scale:
# Use equal steps: step = (end - start) / (points - 1)
# Use range(points) and calculate: value = start + i * step
#
# For EXPONENTIAL scale:
# Values: start * (end/start)^(i/(points-1)) for i in range(points)
# (geometric progression)
#
# For LOGARITHMIC scale:
# Similar to exponential but inverted density
# More points near start, fewer near end
#
# For CUSTOM scale:
# Ask user for step size and direction (ascending/descending)
# Use range() appropriately
#
# For each generated value, also calculate and display:
# - The value in scientific notation
# - Whether it falls in a "critical zone" (ask user to define)
# - Running average
# - Cumulative sum
#
# Print a formatted table with all columns.
# At the end, print statistics: min, max, mean, std deviation.
#
# Example interaction:
# Scale type: linear
# Start: 0
# End: 100
# Points: 11
# Critical zone: 40-60
#
# Point  1:    0.00 │    0.00e+00 │        │ Avg:   0.00 │ Sum:     0.0
# Point  2:   10.00 │    1.00e+01 │        │ Avg:   5.00 │ Sum:    10.0
# ...
# Point  6:   50.00 │    5.00e+01 │ ⚠ CRIT │ Avg:  25.00 │ Sum:   150.0

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a comprehensive prime number analyzer using range().
#
# This exercise builds a mini prime number research tool.
#
# Part 1 - Basic prime finding:
# Ask user for upper limit N.
# Find all primes up to N using the Sieve of Eratosthenes:
# Algorithm:
# 1. Create a list of True values, size N+1 (index = number)
# 2. Start from 2
# 3. For each prime p: mark all multiples as False
#    range(p*p, N+1, p)  ← start from p², step by p
# 4. All remaining True indices are prime
#
# Part 2 - Prime statistics:
# Using range() and the found primes, calculate:
# 1. Total count of primes up to N
# 2. Largest prime found
# 3. Prime density: count / N × 100%
# 4. List of twin primes (pairs that differ by 2): (3,5), (5,7)...
# 5. List of prime gaps (differences between consecutive primes)
# 6. Average prime gap
# 7. Largest prime gap found
# 8. Goldbach verification for even numbers 4 to 50:
#    Every even number > 2 = sum of two primes
#    Example: 4=2+2, 6=3+3, 8=3+5, 10=3+7 or 5+5
#
# Part 3 - Prime visualization:
# Print a grid of numbers 1-100 where:
# - Prime numbers are shown as their value
# - Non-prime numbers are shown as dots (.)
# - Twin primes are shown with asterisk: *p*
# - Format: 10 numbers per row
#
# Example output (partial):
# Primes up to 100: [2, 3, 5, 7, 11, ...]
# Count: 25
# Density: 25.0%
# Twin primes: (3,5), (5,7), (11,13), ...
#
# Grid (1-100):
#  .  2 *3*  . *5*  . *7*  .  .  .
# 11 *11*13*  .  .  .  . *17*  . *19*
# ...
# ============================================================