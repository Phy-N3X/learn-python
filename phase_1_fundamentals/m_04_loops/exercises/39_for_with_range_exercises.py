# ============================================================
# MODULE 04 | EXERCISES 39 - for with range()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Use for with range() to print the following.
# Each task must use range() - not hardcoded values.
#
# Task A: Print numbers 1 to 15, one per line
#
# Task B: Print even numbers from 2 to 20 on ONE line
# Expected: 2 4 6 8 10 12 14 16 18 20
#
# Task C: Print a countdown from 10 to 1, then "Go! 🚀"
# Expected:
# 10 9 8 7 6 5 4 3 2 1
# Go! 🚀
#
# Task D: Print every 3rd number from 3 to 30 on one line
# Expected: 3 6 9 12 15 18 21 24 27 30
#
# Task E: Use range() to access and print each character
# of the string "bioinformatics" WITH its index.
# Expected:
# 0: b
# 1: i
# 2: o
# ... etc

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what this code will print BEFORE running.
# Write your prediction as a comment before each print/block.
# Then run and verify.
#
# # Block A:
# word = "Python"
# for i in range(len(word)):
#     if i % 2 == 0:
#         print(word[i].upper(), end="")
#     else:
#         print(word[i].lower(), end="")
# print()
# # prediction: ?
#
# # Block B:
# total = 0
# for i in range(1, 6):
#     total += i * i
# # prediction: total = ?
# print(total)
#
# # Block C:
# result = []
# for i in range(10, 0, -2):
#     result.append(i)
# # prediction: result = ?
# print(result)
#
# # Block D:
# s = "ATCG"
# output = ""
# for i in range(len(s) - 1, -1, -1):
#     output += s[i]
# # prediction: output = ?
# print(output)
#
# Final question (answer as comment):
# In block A, why does index 0 print uppercase?
# In block D, what does range(len(s)-1, -1, -1) produce?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL errors in the code below.
# Write what each error is as a comment next to the line.
# Then fix all errors so the code runs correctly.
#
# items = ["a", "b", "c", "d"]
#
# for i in range(len(items) + 1):
#     print(items[i])
#
# for i in range(len(items)):
#     print(items[i + 1])
#
# for i in range(len(items) - 1):
#     same_i = i
#     for i in range(3):
#         print(items[same_i], i)
#
# for i in range(len(items)):
#     items.append("x")
#     print(items[i])

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use for with range() to build these outputs.
# Each line uses the loop index in some calculation.
#
# Table A - Powers:
# i=1: 2^1=2,  3^1=3,  5^1=5
# i=2: 2^2=4,  3^2=9,  5^2=25
# i=3: 2^3=8,  3^3=27, 5^3=125
# i=4: 2^4=16, 3^4=81, 5^4=625
# i=5: 2^5=32, 3^5=243,5^5=3125
#
# Table B - Sums:
# 1
# 1+2=3
# 1+2+3=6
# 1+2+3+4=10
# 1+2+3+4+5=15
#
# (hint: maintain a running total)

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Use for with range() to find information about a string.
# Ask the user to enter any word or sentence.
#
# Using ONLY for with range() and index access (no built-in
# methods like .count(), .find(), .index()):
#
# 1. Count how many uppercase letters it contains
# 2. Count how many lowercase letters it contains
# 3. Count spaces
# 4. Find the position of the FIRST vowel (a,e,i,o,u - any case)
# 5. Find the position of the LAST vowel
# 6. Reverse the string character by character
# 7. Count how many times the letter 'a' (any case) appears
#
# Print all results in a formatted report.

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a full ASCII art pattern generator.
# Ask the user for a size (integer, 3-10).
# Generate ALL of these patterns using for+range():
#
# (for size = 5)
#
# Pattern 1 - Hollow square:
# #####
# #   #
# #   #
# #   #
# #####
#
# Pattern 2 - Number grid:
# 11111
# 22222
# 33333
# 44444
# 55555
#
# Pattern 3 - Diagonal:
# #....
# .#...
# ..#..
# ...#.
# ....#
#
# Pattern 4 - Checkerboard:
# # # #
#  # #
# # # #
#  # #
# # # #
#
# Pattern 5 - X pattern:
# #...#
# .#.#.
# ..#..
# .#.#.
# #...#
#
# Use only for+range() for all patterns.

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a codon analyzer that processes a DNA sequence
# using for with range(start, stop, step=3).
#
# dna = "ATGAAATTTGGGCCCTTTAGATAA"
#
# For each codon (group of 3 bases), using range(0, len, 3):
# 1. Print the codon number, position, and codon
# 2. Calculate GC content of the codon (0, 33, 67, or 100%)
# 3. Classify: START (ATG), STOP (TAA/TAG/TGA), or coding
# 4. Mark if it's purine-rich (A or G > 50%)
# 5. Mark if it's pyrimidine-rich (T or C > 50%)
#
# At the end print:
# - Total codons
# - % of GC-rich codons (GC > 50%)
# - Number of START codons
# - Number of STOP codons
# - Average GC content across all codons

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Implement a bubble sort visualizer using for+range().
#
# Start with this list:
# numbers = [64, 34, 25, 12, 22, 11, 90]
#
# Bubble sort algorithm:
# Outer loop: for i in range(n-1)
# Inner loop: for j in range(n-1-i)
# If numbers[j] > numbers[j+1]: swap them
#
# After EACH complete pass (outer iteration):
# - Print the current state of the list
# - Print which elements were swapped
# - Print how "sorted" it is (count elements in correct position)
#
# Expected output format:
# Initial: [64, 34, 25, 12, 22, 11, 90]
# Pass 1: [34, 25, 12, 22, 11, 64, 90] (2 swapped)
# Pass 2: [25, 12, 22, 11, 34, 64, 90] (2 swapped)
# ...
# Final: [11, 12, 22, 25, 34, 64, 90] ✅ Sorted!
# Total passes: X
# Total swaps: Y

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this nested range() code step by step.
# Before each print, write your prediction as a comment.
# Then run and verify.
#
# # Block A - what does this print?
# for i in range(1, 4):
#     for j in range(i, 4):
#         print(f"({i},{j})", end=" ")
#     print()
# # prediction: ?
#
# # Block B - count total iterations:
# count = 0
# for i in range(5):
#     for j in range(i + 1):
#         count += 1
# # prediction: count = ?
# print(count)
#
# # Block C - what pattern is built?
# result = []
# for i in range(1, 5):
#     for j in range(1, i + 1):
#         result.append(i * j)
# # prediction: result = ?
# print(result)
#
# # Block D - matrix diagonal sum:
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# diag_sum = 0
# for i in range(len(matrix)):
#     diag_sum += matrix[i][i]
# # prediction: diag_sum = ?
# print(diag_sum)
#
# Answer as comments:
# In Block B, why is count = 15 (or whatever it is)?
# In Block D, which elements are on the diagonal?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a sequence alignment tool using for+range().
#
# Implement a simplified Needleman-Wunsch inspired comparison:
#
# Given two sequences of the same length:
# seq1 = "ATCGATCGAT"
# seq2 = "ATCGTTCGTT"
#
# Using for+range():
# 1. Compare them position by position
# 2. Build an alignment string (| for match, X for mismatch)
# 3. Calculate % identity
# 4. Find all mismatch positions and what changed (e.g. A→T)
# 5. Calculate longest run of matches (consecutive |)
# 6. Calculate longest run of mismatches (consecutive X)
# 7. Create a dotplot matrix: 1 if match, 0 if mismatch
#    (use nested range() to create and print the matrix)
#
# Print a complete alignment report:
# Seq1: ATCGATCGAT
#       ||||XX||||   ← alignment string
# Seq2: ATCGTTCGTT
#
# Identity: 80.0% (8/10)
# Mismatches: position 5 (G→T), position 6 (A→T)
# Longest match run: 4
# Longest mismatch run: 2

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a polynomial calculator using for+range().
#
# A polynomial: a_n * x^n + a_(n-1) * x^(n-1) + ... + a_1*x + a_0
#
# Ask user for:
# - Coefficients as space-separated numbers (highest degree first)
#   Example: "3 0 -2 5" means 3x³ + 0x² - 2x + 5
# - Value of x to evaluate at
# - Number of x values to evaluate (for a range)
# - Start and end x for the range
#
# Using for+range():
# 1. Parse coefficients into a list
# 2. Evaluate the polynomial at a single x value:
#    Horner's method: start with coefficients[0]
#    for i in range(1, len(coefficients)):
#        result = result * x + coefficients[i]
# 3. Evaluate at a range of x values and print a table
# 4. Find roots approximately (where sign changes between evaluations)
# 5. Find the minimum/maximum in the evaluated range
#
# Print:
# - Polynomial in human-readable form: 3x³ - 2x + 5
# - Table of (x, f(x)) values
# - Approximate roots (where f(x) ≈ 0 or sign changes)
# - Maximum and minimum values found
#
# Example interaction:
# Coefficients: 1 -3 2
# This represents: x² - 3x + 2
# Evaluate from x=-1 to x=4:
# x=-1.0: f(x)=  6.00
# x= 0.0: f(x)=  2.00
# x= 1.0: f(x)=  0.00  ← root!
# x= 2.0: f(x)=  0.00  ← root!
# x= 3.0: f(x)=  2.00
# x= 4.0: f(x)=  6.00

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a protein charge calculator using for+range().
#
# Proteins have an isoelectric point (pI) - the pH at which
# the net charge is zero. At different pH values, the
# amino acid residues have different charges.
#
# Use this protein: "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAPSVT"
#
# Charged residues and their pKa values:
# N-terminus (any start): pKa = 8.0
# C-terminus (any end):   pKa = 3.1
# Asp (D): pKa = 3.9  (negative above pKa)
# Glu (E): pKa = 4.1  (negative above pKa)
# His (H): pKa = 6.5  (positive below pKa)
# Cys (C): pKa = 8.3  (negative above pKa)
# Tyr (Y): pKa = 10.5 (negative above pKa)
# Lys (K): pKa = 10.8 (positive below pKa)
# Arg (R): pKa = 12.5 (positive below pKa)
#
# Charge formula at given pH:
# For positive groups: charge = 1 / (1 + 10^(pH - pKa))
# For negative groups: charge = -1 / (1 + 10^(pKa - pH))
#
# Using for+range():
# 1. Count each charged residue type
# 2. Calculate net charge at pH 7.0
# 3. Calculate net charge for pH 0.0 to 14.0 in steps of 0.5
# 4. Find the pI (pH where net charge ≈ 0) by finding
#    where sign changes in your charge calculations
# 5. Print a charge vs pH table with a visual bar chart
#
# Example output:
# Protein: MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAPSVT
# Length: 38 aa
# Charged residues: K=4, R=4, H=1, D=0, E=2, C=0, Y=1
# Net charge at pH 7: +X.XX
# Estimated pI: ~X.X
# (table of pH vs charge)

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a matrix operations library using for+range().
# Implement all operations using nested for+range() loops.
# Do NOT use any external libraries (no numpy).
#
# Implement these functions (write them as proper code blocks):
#
# 1. print_matrix(M): print matrix in readable format
#
# 2. matrix_add(A, B): add two matrices element by element
#    Result[i][j] = A[i][j] + B[i][j]
#
# 3. matrix_multiply(A, B): multiply two matrices
#    Result[i][j] = sum(A[i][k] * B[k][j] for k in range)
#
# 4. matrix_transpose(M): flip rows and columns
#    Result[j][i] = M[i][j]
#
# 5. matrix_trace(M): sum of diagonal elements
#    sum(M[i][i] for i in range)
#
# 6. is_symmetric(M): check if M == M_transposed
#
# 7. row_sums(M): list of sums of each row
#
# 8. column_sums(M): list of sums of each column
#
# Test with:
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
# C = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]  ← is symmetric?
#
# Print results of all operations with clear labels.

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a full DNA sequence processor using for+range().
#
# Process this sequence:
# dna = ("ATGAAATTTGGGCCCTTTAGATAAGCTGATCGATCG"
#        "ATGGCTATCGATCGATCGAAATTTGGGCCCATGTAA"
#        "ATGCGATACGCTTAAGGCCCCTAAATCGATCGATCG")
#
# Using for+range() for ALL operations:
#
# Step 1 - Find all ORFs (Open Reading Frames):
# An ORF starts at ATG and ends at the next in-frame stop codon
# Use range(0, len, 3) to check each reading frame
# Also check all 3 forward reading frames (+1, +2, +3)
# and 3 reverse complement reading frames
#
# Step 2 - For each ORF found:
# - Record start position, end position, length
# - Extract the sequence
# - Translate to protein using the codon table
# - Calculate GC content of the ORF
# - Classify as short (<30aa), medium (30-100aa), long (>100aa)
#
# Step 3 - Repeat analysis:
# - Find all repeated sequences of length 6 (hexamers)
# - For each unique hexamer, count how many times it appears
# - Find the most repeated hexamer
# - Calculate repeat density: total repeated bases / total length
#
# Step 4 - Composition bias:
# - Using range() with step=10, analyze GC content in windows of 10
# - Find regions with extreme GC (>70% or <30%)
# - Plot a text-based GC content graph
#
# Print a complete genome analysis report.

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a numerical methods solver using for+range().
# Implement three root-finding algorithms.
#
# The goal: find the root(s) of f(x) = x³ - 6x² + 11x - 6
# (roots are at x=1, x=2, x=3 - use these to verify)
#
# Algorithm 1 - Bisection Method:
# Given interval [a, b] where f(a) and f(b) have opposite signs:
# for i in range(max_iterations):
#     mid = (a + b) / 2
#     if f(mid) ≈ 0: found root
#     elif f(a) * f(mid) < 0: b = mid  (root in left half)
#     else: a = mid  (root in right half)
# Print each iteration: i, a, b, mid, f(mid), |b-a|
#
# Algorithm 2 - Newton-Raphson Method:
# f'(x) = 3x² - 12x + 11 (derivative)
# x_new = x_old - f(x_old) / f'(x_old)
# for i in range(max_iterations):
#     x_new = x - f(x) / f_prime(x)
#     if |x_new - x| < tolerance: converged
#     x = x_new
# Print each iteration: i, x, f(x), |x_new - x|
#
# Algorithm 3 - Secant Method:
# Uses two starting points, no derivative needed
# for i in range(max_iterations):
#     x_new = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
#     x0, x1 = x1, x_new
#
# For each algorithm:
# - Start with different intervals/starting points
# - Track convergence (how many iterations to find root)
# - Print iteration table
# - Compare speed of convergence between methods
# - Verify result by plugging back into f(x)
#
# Also:
# - Evaluate f(x) for x in range(-1, 5, step=0.1) using range
# - Print a text graph of the function
# - Mark where roots are found (★)
# ============================================================