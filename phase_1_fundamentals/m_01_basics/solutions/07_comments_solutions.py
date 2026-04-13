# ============================================================
# MODULE 01 | EXERCISES 07 - Comments
# ============================================================
# 15 exercises - comments and docstrings
# Allowed from previous lectures:
#   - variables, type()                 (lecture 01)
#   - numbers, math operators           (lecture 02)
#   - string methods, slicing           (lecture 03)
#   - bool, comparison operators        (lecture 04)
#   - print(), sep, end, f-strings      (lecture 05)
#   - input() patterns                  (lecture 06)
#
# NOTE: These exercises are different from previous ones.
# The goal is not just to write working code,
# but to write WELL-COMMENTED code.
# You will also READ and FIX bad comments.
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
"""
============================================================
filename    : 07_comments_solutions.py
description : Exercises on Python comments and docstrings
author      : PhyN3X
created     : 2026-04-13
module      : m_01_basics
lecture     : 07_comments.py
============================================================
"""



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
sequence = "ATCGGCTATCGAATCG"
a_count = sequence.count("A")
t_count = sequence.count("T")
g_count = sequence.count("G")
c_count = sequence.count("C")
total = len(sequence)
gc = (g_count + c_count) / total * 100    # Calculates GC content
at = (a_count + t_count) / total * 100    # Calculates AT content
print(f"GC content: {gc:.1f}%")
print(f"AT content: {at:.1f}%")
print(f"GC + AT = {gc + at:.1f}%")        # Prints sum of GC and AT contents in %



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
# Set product price
x = 100

# Calculates discount on product
discount = x * 0.2

# Calculates final price after discount
final_price = x - discount

# Check if price after discount is less than 90
is_good_deal = final_price < 90

# Print price after discount
print(f"Final price: {final_price}")



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Write a function with a PROPER docstring.
# The function converts Celsius to Fahrenheit.
# Formula: F = (C * 9/5) + 32
#
# Your docstring must include:
#   - One-line summary
#   - Args section
#   - Returns section
#   - Examples section (at least 2 examples)
#
# After writing the function:
#   - Print its __doc__ attribute
#   - Call help() on it
#   - Call the function with 0, 100, and -40



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Use comments to PLAN your code before writing it.
# This technique is called "comment-driven development".
#
# Task: write a BMI calculator
# Formula: BMI = weight(kg) / height(m)²
# Categories:
#   < 18.5  → Underweight
#   18.5-25 → Normal
#   25-30   → Overweight
#   >= 30   → Obese
#
# Steps:
# 1. First write ALL steps as comments (no code yet)
# 2. Then fill in the actual code under each comment
# 3. Use simulated inputs



# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# Add a and b
a = 15
b = 4
result = a + b

is_large = result > 100           # Check if result is greater than 100

name = "anna"
formatted = name.title()          # Convert name to Title Case

# Split the string by commas
data = "10 20 30 40"
numbers = data.split()            # split into list of int numbers

# Calculate square root
import math
root = math.pow(2, 8)        # Calculate square root of 8



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# Future: Should support RNA sequences (U instead of T)

# FIXME: function crashes on empty string input
# FIXME: doesn't handle lowercase letters
def count_nucleotides(sequence): # NOTE: assumes sequence contains only valid nucleotides
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")
    return a, t, g, c

result = count_nucleotides("ATCGGCTA")

# WARNING: result is a percentage, not a decimal
print(result)



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# Write a well-commented solution for this problem:
#
# Task: analyze a DNA sequence and produce a full report.
# Use SECTION SEPARATOR comments to organize the code into:
#   --- Input ---
#   --- Validation ---
#   --- Analysis ---
#   --- Output ---
#
# Requirements for each section:
#   Input:      define the sequence and organism name
#   Validation: check sequence is not empty, is uppercase
#   Analysis:   count nucleotides, calculate GC%, AT%
#   Output:     print a formatted report
#
# Every non-obvious line must have a comment.
# Use the style from Part 9 of the lecture.



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Write docstrings for ALL three functions below.
# Each docstring must have:
#   - summary line
#   - Args
#   - Returns
#   - Examples
# Do NOT change the function code itself.

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def count_words(sentence):
    return len(sentence.strip().split())


# After adding docstrings, print __doc__ for each function
# and call help() on one of them.



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Comment-driven development for a more complex task.
#
# Task: build a simple grade calculator
# Input:  five exam scores (simulated)
# Output: average, letter grade, pass/fail, and feedback
#
# Grading scale:
#   90-100 → A → "Excellent"
#   80-89  → B → "Good"
#   70-79  → C → "Satisfactory"
#   60-69  → D → "Needs improvement"
#   0-59   → F → "Failing"
#
# Instructions:
# 1. Write the ENTIRE solution as comments first
#    (every step, every calculation, every output)
# 2. Then implement the code under each comment
# 3. Add inline comments explaining non-obvious parts



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Identify and list EVERY bad practice in this code.
# Then rewrite the ENTIRE block with proper comments.
#
# Bad code to analyze:

# x
x = [98, 87, 92, 78, 95]

# do the thing
r = sum(x) / len(x)

# idk why this works but it does
s = sorted(x)
m = s[len(s)//2]

# check
f = r >= 80

# OLD CODE - DO NOT USE
# r2 = (sum(x) - min(x)) / (len(x) - 1)

# lol
print(f"avg={r:.1f} med={m} pass={f}")

# First: list all bad practices as comments
# Then: rewrite with proper comments and better variable names


# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Write a fully documented module-level file.
#
# Create a "mini-module" for DNA utilities with:
#   1. File header (triple-quoted docstring at top)
#   2. Section separators between each function
#   3. Full docstring for EACH function
#   4. Inline comments for non-obvious lines
#   5. TODO tag for at least one missing feature
#
# Functions to write and document:
#
#   gc_content(sequence)
#     → returns GC% as float
#
#   is_valid_dna(sequence)
#     → returns True if only contains A,T,G,C
#
#   reverse_complement(sequence)
#     → returns reverse complement string
#       A↔T, G↔C, then reverse
#
# At the bottom, test each function with examples
# and print results with clear labels.



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Debugging with comments.
#
# This code has THREE bugs. Use comments to:
#   1. Mark each bug with # FIXME: explanation
#   2. Write your fix attempt below the bug
#   3. Add # FIXED: explanation after your fix
#   4. Add a # NOTE: comment explaining what the correct
#      behavior should be
#
# Buggy code:

def calculate_bmi(weight, height):
    bmi = weight / height               # bug 1
    return bmi

def is_leap_year(year):
    return year % 4 == 0               # bug 2 (incomplete)

def first_and_last(text):
    return text[0], text[-1]           # bug 3 (no guard for empty)

# Test cases that reveal the bugs:
print(calculate_bmi(70, 175))          # should be ~22.86 (height in cm!)
print(is_leap_year(1900))             # should be False (1900 is NOT leap)
print(first_and_last(""))             # should not crash



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Write a TEACHING comment for a complex algorithm.
#
# Task: explain the bubble sort algorithm using comments.
# Your comments should be SO clear that someone who has
# never seen sorting could understand it step by step.
#
# Requirements:
#   1. Start with a multi-line comment explaining
#      what bubble sort is in plain English
#   2. Add a visual diagram as a comment showing
#      how [5, 3, 1, 4, 2] gets sorted step by step
#   3. Write the code with a comment on EVERY line
#   4. End with a comment about time complexity
#
# The algorithm:
#   numbers = [5, 3, 1, 4, 2]
#   for i in range(len(numbers)):
#       for j in range(len(numbers) - i - 1):
#           if numbers[j] > numbers[j + 1]:
#               numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#   print(numbers)



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Write a COMPLETE, production-quality commented program.
#
# Task: student grade book with full documentation
#
# Requirements:
#   1. File header docstring
#   2. Constants section with comments
#   3. At least 3 functions, each with full docstrings
#   4. Section separators throughout
#   5. Inline comments on non-obvious lines
#   6. At least one TODO tag
#   7. At least one WARNING tag
#   8. Variable names that are self-documenting
#
# Program logic:
#   - Store 5 students with names and 3 exam scores each
#   - Calculate average score for each student
#   - Assign letter grade (A/B/C/D/F)
#   - Find class average
#   - Find highest and lowest scoring student
#   - Print a full formatted grade report
#
# The code quality and comment quality will be judged,
# not just whether it runs correctly.
