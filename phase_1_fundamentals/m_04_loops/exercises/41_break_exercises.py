# ============================================================
# MODULE 04 | EXERCISES 41 - break
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Write a for loop that iterates over the numbers 1 to 20.
# Use break to stop the loop when you reach a number
# that is divisible by both 3 and 5 (i.e. divisible by 15).
# Print each number before stopping, and print a message
# explaining why the loop stopped.
#
# Expected output:
# 1
# 2
# 3
# ...
# 14
# 15
# Stopped at 15 - divisible by both 3 and 5!

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what this code will print BEFORE running.
# Write your prediction as a comment before each section.
# Then run and verify.
#
# # Section A:
# for i in range(10):
#     if i == 5:
#         break
#     print(i, end=" ")
# print()
# # prediction: ?
#
# # Section B:
# i = 0
# while True:
#     if i * i > 50:
#         break
#     i += 1
# # prediction: i = ?
# print(i)
#
# # Section C:
# words = ["hello", "world", "STOP", "python", "break"]
# result = []
# for word in words:
#     if word == "STOP":
#         break
#     result.append(word.upper())
# # prediction: result = ?
# print(result)
#
# # Section D:
# for i in range(3):
#     for j in range(3):
#         if j == 1:
#             break
#         print(f"{i}{j}", end=" ")
# print()
# # prediction: ?
#
# Final question (answer as comment):
# In Section D, why does the outer loop NOT stop when break is hit?
# What exactly does each break exit?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL errors in the code below.
# Write what each error is as a comment.
# Then fix all errors so the code runs correctly.
#
# # Error set 1:
# break
#
# # Error set 2:
# for i in range(5):
#     print(i)
# break
#
# # Error set 3:
# for i in range(10):
#     if i == 5:
#         break
#         print("Found 5!")
#     print(i)
#
# # Error set 4:
# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     if n < 0:
#         break    # intended to skip negatives, not stop!
#     print(n)

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use a while True loop with break to implement
# a simple input validator.
#
# Ask the user for their age repeatedly until they enter
# a valid age (integer between 0 and 120).
# Handle the case where they enter non-numeric text.
#
# After accepting valid input, print:
# - The age entered
# - Whether they are a child (<18), adult (18-64), or senior (65+)
# - How many attempts it took
#
# Example interaction:
# Enter age: abc
# ❌ Not a number! Try again.
# Enter age: -5
# ❌ Age must be between 0 and 120!
# Enter age: 25
# ✅ Age accepted: 25
# Category: Adult
# Attempts needed: 3

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Search for the first occurrence of a codon in a DNA sequence.
# Use break to stop as soon as you find it.
#
# dna = "GCTATCGATGCGATACGCTTAAGGCCCCTAA"
# target_codon = "ATG"
#
# Using a for loop with range() and step=3:
# - Check each codon (group of 3 bases)
# - When you find the target codon, print its position and break
# - Also count how many codons you checked before finding it
# - If not found, print an appropriate message
#
# Then repeat the search for "TAA" and "GGG".
#
# Expected output (for ATG):
# Searching for 'ATG'...
# Checked codon 1: GCT - no match
# Checked codon 2: ATC - no match
# Checked codon 3: GAT - no match
# Checked codon 4: GCG - no match
# Found 'ATG' at position 12 (codon #5)!
# Stopped after checking 5 codons.

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a while True menu system that uses break to exit.
# The menu is for a simple DNA analysis tool.
#
# Menu options:
# 1. Enter DNA sequence
# 2. Count bases (A, T, C, G)
# 3. Calculate GC content
# 4. Find a pattern (user inputs pattern to find)
# 5. Quit
#
# Rules:
# - Store the DNA sequence in a variable
# - Option 2, 3, 4 should warn if no sequence entered yet
# - Option 4 should search for ALL occurrences and list positions
# - Option 5 uses break to exit
# - Invalid choices print a warning and loop continues
#
# Use break ONLY for option 5 (quit).
# Keep the menu running until quit is chosen.

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Implement a number search with break to optimize performance.
#
# Task: Find ALL prime numbers up to N (user input).
# But use break to optimize the inner divisibility check.
#
# For each number being tested:
# - Use a while loop to check divisors
# - When you find ANY divisor → break (it's not prime)
# - Count how many break-exits occurred (composite numbers found)
# - Count how many numbers completed without break (primes)
#
# Print:
# - List of all primes found
# - Count of primes
# - Count of composites
# - Total numbers checked
# - "Break efficiency": how many unnecessary checks were avoided
#   (for each composite, the breaks saved = divisors_not_checked)
#
# Example interaction:
# Find primes up to: 20
# Primes: [2, 3, 5, 7, 11, 13, 17, 19]
# Count: 8 primes, 10 composites
# Total numbers tested: 19 (2 to 20)

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a while True guessing game with break.
# The player guesses a secret number (1-100).
#
# Features:
# - Use random.randint(1, 100) for the secret number
# - Give "higher"/"lower" hints after each guess
# - Allow max 7 guesses
# - Use break when:
#   a) Correct guess found
#   b) Max guesses exceeded
#   c) User types "quit" to give up
# - Handle non-numeric input gracefully
# - After the game ends, print statistics:
#   - Secret number (if not guessed)
#   - Number of guesses used
#   - Whether they won or lost
#   - "Optimal" number of guesses needed (log2(100) ≈ 7)
#
# Example interaction:
# Secret number chosen. You have 7 guesses.
# Guess 1/7: 50
# 📈 Higher!
# Guess 2/7: 75
# 📉 Lower!
# Guess 3/7: 62
# 🎉 Correct! Found in 3 guesses!

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this code with break in nested loops.
# Before each print, write your prediction as a comment.
# Then run and verify.
#
# # Block A - 2D search:
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# target = 5
# found_r, found_c = -1, -1
#
# for r in range(len(matrix)):
#     for c in range(len(matrix[r])):
#         if matrix[r][c] == target:
#             found_r, found_c = r, c
#             break
#     if found_r != -1:
#         break
#
# # prediction: found_r = ?, found_c = ?
# print(found_r, found_c)
#
# # prediction: which cells were visited before finding 5?
# # (list them as (r,c) pairs)
#
# # Block B - break with accumulator:
# words = ["bio", "STOP", "info", "STOP", "rmatics"]
# result = ""
# for word in words:
#     if word == "STOP":
#         break
#     result += word
# # prediction: result = ?
# print(result)
#
# # Block C - while with break condition:
# n = 1
# product = 1
# while True:
#     product *= n
#     if product > 100:
#         break
#     n += 1
# # prediction: n = ?, product = ?
# print(n, product)
#
# Answer as comments:
# In Block A, after the inner break, why is the outer break needed?
# Without the outer break, what would happen?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a DNA sequence quality checker using break.
#
# dna_sequences = [
#     "ATCGATCGATCG",         # valid
#     "ATCG ATCG",            # has space
#     "atcgatcg",             # lowercase
#     "ATCG1234",             # has digits
#     "ATCGXYZATCG",          # has invalid letters
#     "ATCGATCGATCGATCG",     # valid but long
# ]
#
# For each sequence:
# 1. Check character by character using a for loop
# 2. Use break when the FIRST error is found
# 3. Report what was found (valid or what error at what position)
# 4. Track statistics: how many were valid, how many had errors
#
# After all sequences processed:
# - Print a summary table
# - Show which error type was most common
# - Show the average position where errors were found
#   (for sequences with errors)
#
# Error types to detect (in order of checking):
# - Lowercase letter
# - Space character
# - Digit
# - Invalid nucleotide letter (not A,T,C,G)
# - Any other invalid character

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Implement a convergence-based iterative algorithm using break.
#
# The Newton-Raphson method for finding cube root of a number:
# x_new = (2 * x + n / x^2) / 3
# where x is current estimate, n is the target number
#
# Ask user for:
# - Number to find cube root of
# - Tolerance (e.g. 0.0001)
# - Maximum iterations (e.g. 1000)
#
# Algorithm:
# 1. Start with initial guess = n / 3
# 2. Repeat:
#    - Calculate x_new using formula
#    - If |x_new - x| < tolerance → break (converged!)
#    - If iterations >= max_iterations → break (failed!)
#    - Update x = x_new
# 3. Report result
#
# Print a table for EACH iteration:
# - Iteration number
# - Current estimate
# - New estimate
# - Error (|x_new - x|)
# - Convergence status
#
# After loop:
# - Whether it converged or hit max iterations
# - Final answer
# - Verification: answer^3 should ≈ original number
# - Comparison with Python's built-in: n ** (1/3)
#
# Test with: n=27 (answer=3), n=125 (answer=5), n=1000 (answer=10)

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a protein sequence scanner using break.
# Scan for functional motifs (short sequence patterns).
#
# protein = "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAPSVTMKTAA"
#
# Motifs to search for (in priority order - stop at first match):
# 1. "MKTAY" → Signal peptide start
# 2. "QRQI"  → Binding domain
# 3. "RLGL"  → Hydrophobic core
# 4. "APSVT" → Active site
# 5. "KTAA"  → C-terminal signal
#
# Search algorithm:
# - Outer while loop: iterate through motifs
# - Inner for loop: scan protein for each motif
# - Use break on the inner loop when motif is found
# - Use break on outer loop after finding the HIGHEST PRIORITY motif
#   (the one that appears earliest AND has highest priority)
#
# Wait - actually: find ALL motifs present, but report them
# in priority order. For each motif found:
# - Report its position in the protein
# - Report what it means
# - If found at multiple positions, list all
#
# Then: report the HIGHEST PRIORITY motif found
# (lowest priority number = most important)
#
# Use break strategically:
# - Break inner search loop when current motif is found
#   (to record position, then continue to next motif)
# - Break outer motif loop... only if you decide to stop early

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Build a multi-level password system using break.
#
# The system has 3 security levels, each requiring different checks.
# Use nested loops with break for each level.
#
# Level 1 - PIN check:
# Correct PIN: "1234"
# Max 3 attempts
# Use while loop + break
#
# Level 2 - Security question:
# Only reached if Level 1 passed
# Questions and answers (pick one randomly):
# {"What is 2+2?": "4",
#  "First letter of Python?": "P",
#  "How many bases in DNA?": "4"}
# Max 2 attempts
# Use while loop + break
#
# Level 3 - Password:
# Only reached if Level 1 AND Level 2 passed
# Password rules:
# - At least 8 characters
# - Contains at least one digit
# - Contains at least one uppercase letter
# - Contains no spaces
# Check each rule using a for loop with break on first violation
# Tell user WHICH rule they violated
# Max 3 attempts
#
# After all 3 levels passed → "✅ FULL ACCESS GRANTED"
# If any level fails completely → "❌ ACCESS DENIED - Security breach logged"
#
# Track and print:
# - Total attempts across all levels
# - Which level(s) needed retries
# - Time taken (use a counter - each attempt = 1 "second")

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Implement a complete genome ORF (Open Reading Frame) finder
# using break.
#
# An ORF is a sequence that:
# - Starts with ATG (start codon)
# - Ends with TAA, TAG, or TGA (stop codon)
# - Has codons in between
# - Length must be multiple of 3 (already guaranteed if we read in frame)
#
# dna = ("ATGAAATTTGGGCCCTTTAGATAAGCTGATCGATCG"
#        "ATGGCTATCGATCGATCGAAATTTGGGCCCATGTAA"
#        "ATGCGATACGCTTAAGGCCCCTAAATCGATCGATCG")
#
# Algorithm (use break strategically):
#
# Step 1: Check all 3 reading frames (+1, +2, +3)
# For each frame start (0, 1, 2):
#   - Use a for loop with range(frame, len(dna)-2, 3)
#   - When you find ATG:
#       - Record start position
#       - Continue scanning for stop codon
#       - Use break when stop codon found (one ORF complete)
#       - Add ORF to results
#       - Continue outer scan (don't stop just because one ORF found)
#
# Step 2: Also check reverse complement
# Reverse complement: A↔T, C↔G, then reverse the whole string
# Apply same ORF finding algorithm to reverse complement
#
# For each ORF found, report:
# - Frame (+1, +2, +3, -1, -2, -3)
# - Start position (in original sequence)
# - End position
# - Length in nucleotides and amino acids
# - The ORF sequence
# - GC content of the ORF
#
# Print a complete ORF report sorted by length (longest first).
# Mark the longest ORF as "Primary ORF".

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Build a complete text-based simulation using break
# for all exit conditions.
#
# Simulation: "Protein Folding Game"
# The player guides a chain of amino acids to fold correctly.
#
# Setup:
# - Protein sequence: "MHKGLYFE" (8 amino acids)
# - Each amino acid has a property:
#   M=neutral, H=positive, K=positive, G=flexible,
#   L=hydrophobic, Y=aromatic, F=hydrophobic, E=negative
# - The protein folds on a 5x5 grid
# - Start: all amino acids in a line (row 0, columns 0-7 ... but grid is 5x5!)
#   Actually: place them in a zigzag pattern initially
#
# Game loop (while True with break):
# - Show current state of the grid
# - Show current "folding score" (see scoring below)
# - Ask player to move an amino acid:
#   "Move amino acid N in direction (U/D/L/R)"
# - Validate move:
#   - Amino acid number must be 1-8
#   - Direction must be U/D/L/R
#   - New position must be within grid (0-4, 0-4)
#   - New position must not be occupied
#   - Must remain connected to neighbors
# - Apply move
# - Recalculate score
# - Check win condition (score >= target)
# - Check if player wants to quit ("quit" command)
# - Use break for: win condition, quit command, max moves exceeded
#
# Scoring (use nested loops with break for efficiency):
# +2 for each pair of hydrophobic amino acids (L, F) that are
#    adjacent (up/down/left/right) but not bonded in sequence
# +1 for each positive-negative pair that are adjacent
# -1 for each hydrophobic amino acid on the edge of the grid
#
# Win condition: score >= 4
# Max moves: 20
#
# Print after each move:
# - Updated grid
# - Score change and total score
# - Moves remaining
# - Hint: which amino acids would benefit from moving
# ============================================================