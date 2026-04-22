# ============================================================
# MODULE 04 | EXERCISES 40 - while loop
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Write a while loop that prints numbers from 1 to 10.
# Then write a while loop that prints from 10 down to 1.
# Both on separate lines, space-separated.
#
# Expected output:
# 1 2 3 4 5 6 7 8 9 10
# 10 9 8 7 6 5 4 3 2 1

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what this code will print BEFORE running.
# Write your prediction as a comment before each section.
# Then run and verify.
#
# # Section A:
# x = 1
# while x < 100:
#     x *= 3
# # prediction: x = ?
# print(x)
#
# # Section B:
# n = 10
# total = 0
# while n > 0:
#     total += n
#     n -= 2
# # prediction: total = ?
# # prediction: n = ?
# print(total, n)
#
# # Section C:
# s = "Python"
# i = 0
# result = ""
# while i < len(s):
#     result += s[i]
#     i += 2
# # prediction: result = ?
# print(result)
#
# # Section D:
# count = 0
# n = 1
# while n <= 50:
#     if n % 7 == 0:
#         count += 1
#     n += 1
# # prediction: count = ?
# print(count)
#
# Final question (answer as comment):
# In section A, why does x end at 243 (or whatever it is)?
# In section C, why does result skip letters?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL errors in the while loop code below.
# Write what each error is as a comment.
# Then fix all errors so the code runs correctly.
#
# # Error set 1:
# count = 0
# while count < 5
#     print(count)
#     count += 1
#
# # Error set 2:
# n = 10
# While n > 0:
#     print(n)
#     n -= 1
#
# # Error set 3:
# x = 0
# while x < 3:
#     print(x)
#
# # Error set 4:
# total = 0
# i = 1
# while i <= 10:
# total += i
# i += 1
# print(total)

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use a while loop to calculate the sum of all integers
# from 1 to N, where N is entered by the user.
# Validate that N is a positive integer (greater than 0).
#
# Also find and print:
# - Sum of even numbers in the range
# - Sum of odd numbers in the range
# - Verify: sum_even + sum_odd should equal total sum
#
# Example interaction:
# Enter N: 10
# Sum from 1 to 10: 55
# Sum of even numbers (2,4,6,8,10): 30
# Sum of odd numbers (1,3,5,7,9): 25
# Verification: 30 + 25 = 55 ✅

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Create a while loop that keeps asking the user to enter
# DNA bases one at a time.
# Valid bases: A, T, C, G (case insensitive)
# Stop when the user presses Enter with no input.
#
# For each base entered:
# - If valid → add to sequence, print current sequence
# - If invalid → print warning, don't add to sequence
#
# At the end, print:
# - Full sequence
# - Length
# - Base counts (A, T, C, G)
# - GC content %
#
# Example interaction:
# Enter base (or Enter to stop): A
# Sequence so far: A
# Enter base (or Enter to stop): t
# Sequence so far: AT
# Enter base (or Enter to stop): X
# ❌ Invalid base: X
# Enter base (or Enter to stop):
# Final sequence: AT
# Length: 2
# A: 1, T: 1, C: 0, G: 0
# GC content: 0.0%

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a number guessing game using while.
# The program thinks of a number between 1 and 100.
# The user has unlimited guesses.
# After each guess, tell the user: too high / too low / correct!
# Also track:
# - Number of attempts
# - Best guess so far (closest to secret)
# - All guesses made
# When correct, display:
# - "Congratulations!"
# - How many guesses were needed
# - Classification: 1=Genius, <=5=Excellent, <=10=Good, >10=Keep practicing
#
# Tip: import random; secret = random.randint(1, 100)

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a compound interest calculator using while.
# Ask user for:
# - Initial deposit (principal)
# - Annual interest rate (%)
# - Target amount (goal)
#
# Calculate how many years it takes to reach the goal.
# Print a year-by-year table showing the growth.
# Mark the year when the balance doubles for the first time.
# Mark the year when the goal is reached.
#
# Example interaction:
# Principal: 1000
# Annual rate (%): 8
# Goal: 5000
#
# Year  1:   1080.00 PLN
# Year  2:   1166.40 PLN
# ...
# Year  9:   1999.00 PLN ← (near double)
# Year 10:   2158.92 PLN ✓ DOUBLED!
# ...
# Year 21:   5033.83 PLN 🎯 GOAL REACHED!
# Total years: 21

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Implement a while-based menu system for a student database.
# The menu should keep running until the user chooses "quit".
#
# Menu options:
# 1. Add student (name + GPA)
# 2. List all students
# 3. Find student by name
# 4. Show highest GPA
# 5. Show average GPA
# 6. Remove student by name
# 7. Quit
#
# Use a list to store students as dictionaries:
# {"name": "Anna", "gpa": 3.8}
#
# Validate input for each option:
# - GPA must be 0.0-4.0
# - Name must not be empty
# - Warn if student not found
#
# Print appropriate messages for all operations.

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this while loop code step by step.
# Before each print, write your prediction as a comment.
# Then run and verify.
#
# # Block A: Collatz sequence
# n = 12
# steps = 0
# sequence = [n]
# while n != 1:
#     if n % 2 == 0:
#         n = n // 2
#     else:
#         n = 3 * n + 1
#     steps += 1
#     sequence.append(n)
# # prediction: steps = ?
# # prediction: sequence = ?
# print(steps)
# print(sequence)
#
# # Block B: Digit sum
# n = 9875
# while n >= 10:
#     digit_sum = 0
#     temp = n
#     while temp > 0:
#         digit_sum += temp % 10
#         temp //= 10
#     n = digit_sum
# # prediction: n = ?
# print(n)
#
# # Block C: GCD (Euclidean algorithm)
# a = 48
# b = 18
# while b != 0:
#     a, b = b, a % b
# # prediction: a = ?
# print(a)
#
# Answer as comments:
# What mathematical concept does Block C implement?
# What is the Collatz conjecture about Block A?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a while-based input validator and data processor.
# Create a program that collects temperature measurements
# from a scientific experiment.
#
# Rules:
# - Keep asking for temperatures until user enters "done"
# - Valid temperature range: -273.15°C to 1000°C
# - Must be a valid number (handle non-numeric input)
# - Need at least 3 measurements before "done" is accepted
# - Maximum 20 measurements
#
# After collection, calculate and print:
# - All measurements in order
# - Minimum and maximum temperature
# - Mean temperature
# - Median temperature
# - Standard deviation
# - Measurements above and below mean
# - Temperature trend: is it generally increasing, decreasing,
#   or mixed? (compare first half average to second half average)
# - A simple ASCII chart of the values
#
# Use only while loops (no for loops) for all calculations.

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a while-based prime number generator.
#
# Part 1: Find all primes up to N (user input)
# Use a while loop to test each number.
# For each number, use another while loop to check divisibility.
# Count how many were found.
#
# Part 2: Find the Nth prime
# Keep generating primes until you've found N of them.
# (user specifies which prime they want: 1st, 2nd, 100th...)
#
# Part 3: Prime factorization using while
# For a number M, find its prime factorization.
# Algorithm: while M > 1, try to divide by smallest factor
#
# Part 4: Twin prime finder
# Keep checking pairs until you find N twin prime pairs.
# (Twin primes: pairs that differ by 2, like 3&5, 11&13)
#
# For each part, print results and statistics.
# Use ONLY while loops.
#
# Example output (Part 3, M=360):
# 360 = 2³ × 3² × 5¹

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a while-based PCR simulation.
# PCR (Polymerase Chain Reaction) amplifies DNA.
# Each cycle doubles the number of DNA copies.
# But in reality, efficiency < 100%.
#
# Ask user for:
# - Initial number of DNA copies (e.g. 10)
# - PCR efficiency (0.8-1.0, e.g. 0.95 = 95%)
# - Target number of copies (e.g. 1,000,000)
# - Maximum cycles allowed (e.g. 40)
#
# Simulation:
# Each cycle: new_copies = current_copies * (1 + efficiency)
# Also simulate: 5% degradation every 5 cycles
# (multiply by 0.95 every 5th cycle)
#
# Use while loop until target reached OR max cycles exceeded.
# After each cycle print:
# - Cycle number
# - Current copies (formatted with commas)
# - Copies added this cycle
# - Efficiency indicator (█ bars based on % of target)
#
# At the end, print:
# - Whether target was reached
# - Total cycles used
# - Final copy number
# - Fold amplification (final / initial)
# - Theoretical vs actual comparison

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a while-based text adventure game.
# Keep it simple but use while loops extensively.
#
# Game concept: "Lab Escape"
# The player is trapped in a lab and must solve puzzles to escape.
#
# Game structure (use while loops for):
# - Main game loop (while not game_over)
# - Each room/puzzle (while not puzzle_solved)
# - Input validation (while not valid_input)
#
# Rooms to implement:
#
# Room 1 - Storage Room:
# Puzzle: Guess the correct chemical formula from hints
# Hints given one at a time (while not solved, give next hint)
# Answer: "H2O" (water)
# Max 5 attempts
#
# Room 2 - Lab:
# Puzzle: Binary to decimal conversion
# Computer shows binary number, player types decimal
# 3 rounds, must get at least 2 right
# Random binary numbers: use random.randint(0, 255)
#
# Room 3 - Server Room:
# Puzzle: Password is the sum of digits of a given number
# "The access code is the digital root of 9875"
# Digital root: keep summing digits until single digit
#
# Features:
# - Health/attempts tracking
# - Hints cost "time" (counter)
# - Final score based on time used and hints taken
# - Game over if too many failures
#
# Print narrative text for atmosphere.
# Use while loops for all loops.

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a comprehensive while-based sorting algorithm visualizer.
# Implement and visualize THREE sorting algorithms.
# Each must use while loops (convert any for loops to while).
#
# Algorithm 1 - Bubble Sort:
# Compare adjacent elements, swap if out of order.
# Repeat until no swaps occur in a full pass.
# Track: passes, comparisons, swaps
#
# Algorithm 2 - Selection Sort:
# Find minimum in unsorted portion, place at start.
# Use while to scan for minimum.
# Track: passes, comparisons, swaps
#
# Algorithm 3 - Insertion Sort:
# Take each element, insert into correct position in sorted portion.
# Use while to shift larger elements right.
# Track: passes, comparisons, shifts
#
# For EACH algorithm:
# - Start with the SAME unsorted list: [64, 34, 25, 12, 22, 11, 90]
# - Show the state of the list after EACH major step
# - Print a visual bar chart (use █ characters, length = value//5)
# - Count all operations
# - Measure performance (compare operation counts)
#
# Final comparison table:
# Algorithm       │ Comparisons │ Swaps │ Passes
# Bubble Sort     │     X       │   X   │   X
# Selection Sort  │     X       │   X   │   X
# Insertion Sort  │     X       │   X   │   X

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a while-based biological sequence assembler.
# This simulates (very simply) DNA sequence assembly.
#
# The concept:
# You have short DNA "reads" (fragments).
# You need to assemble them into one longer sequence.
# Find overlapping regions and merge them.
#
# reads = [
#     "ATCGATCGTA",
#     "CGATCGTACG",
#     "TCGTACGCTA",
#     "ACGCTAATCG",
#     "TAATCGATCG",
# ]
#
# Assembly algorithm (greedy, using while):
#
# Step 1 - Find overlaps:
# For each pair of reads, find the longest overlap
# where end of read_A matches start of read_B.
# Use a while loop to check all possible overlap lengths
# (from longest to shortest, minimum overlap = 4 bases).
#
# Step 2 - Greedy assembly:
# Start with the first read as current assembly.
# While there are unassembled reads:
#   - Find which remaining read has the best overlap
#     with the END of the current assembly
#   - Merge them (append the non-overlapping part)
#   - Remove that read from unassembled list
#   - Repeat
#
# Step 3 - Verify assembly:
# Check that each original read appears in the final assembly.
# Calculate assembly statistics:
# - Total length of all reads
# - Length of assembled sequence
# - Compression ratio
# - Coverage: average number of reads covering each position
#
# Step 4 - Quality check:
# For each position in the assembly, check which reads
# cover it and if they all agree on the base.
# Report any positions with conflicts.
#
# Print:
# - All reads with their lengths
# - Overlap matrix (which reads overlap which)
# - Assembly process step by step
# - Final assembled sequence
# - Quality statistics
# ============================================================