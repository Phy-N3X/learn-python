# ============================================================
# MODULE 01 | EXERCISES 06 - input()
# ============================================================
# 15 exercises - input() only
# Allowed from previous lectures:
#   - variables, type()                 (lecture 01)
#   - numbers, math operators           (lecture 02)
#   - string methods, slicing           (lecture 03)
#   - bool, comparison operators        (lecture 04)
#   - print(), sep, end, f-strings      (lecture 05)
#
# HOW TO WORK WITH THESE EXERCISES:
# Each exercise has TWO versions to write:
#   A) SIMULATED - use hardcoded values (runs without input)
#   B) REAL      - use actual input() calls
# Write BOTH versions. Comment out version B while testing A.
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Ask user for their name and print a greeting.
#
# Expected interaction:
#   Enter your name: Anna
#   Hello, Anna! Welcome to Python!
#
# Requirements:
#   - Use .strip() on the input
#   - Use f-string for the greeting
#
# Write version A (simulated) and version B (real input).

# Version A - simulated:

# Version B - real input (comment out when not testing):


# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Ask user for two integers and print their:
#   sum, difference, product, quotient
#
# Expected interaction:
#   Enter first number: 10
#   Enter second number: 3
#   Sum:        13
#   Difference: 7
#   Product:    30
#   Quotient:   3.33
#
# Requirements:
#   - Convert input to int
#   - Quotient rounded to 2 decimal places
#
# Write version A and version B.

# Version A - simulated:

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Ask user for their birth year and calculate their age.
# Also tell them what year they will turn 100.
#
# Expected interaction:
#   Enter your birth year: 2000
#   You are 25 years old.
#   You will turn 100 in the year 2100.
#
# Requirements:
#   - current_year = 2025
#   - Handle the input as int
#
# Write version A and version B.

# Version A - simulated:

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Temperature converter - Celsius to Fahrenheit AND Kelvin.
#
# Expected interaction:
#   Enter temperature in Celsius: 100
#   100.0°C = 212.0°F
#   100.0°C = 373.15K
#
# Formulas:
#   Fahrenheit = (Celsius * 9/5) + 32
#   Kelvin     = Celsius + 273.15
#
# Write version A and version B.

# Version A - simulated:

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# String analyzer - ask for a sentence and analyze it.
#
# Expected interaction:
#   Enter a sentence: Hello World Python
#   Original:   Hello World Python
#   Uppercase:  HELLO WORLD PYTHON
#   Lowercase:  hello world python
#   Length:     18 characters
#   Words:      3 words
#   Reversed:   nohtyP dlroW olleH
#
# Write version A and version B.

# Version A - simulated:

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Ask user for their name - handle spaces and case.
# Demonstrate why strip() and title() matter.
#
# Expected interaction:
#   Enter your full name:   anna kowalski
#   Raw input repr:    '  anna kowalski  '
#   After strip():     'anna kowalski'
#   After title():     'Anna Kowalski'
#   First name:        Anna
#   Last name:         Kowalski
#   Initials:          A.K.
#
# Simulate the raw input WITH spaces and lowercase.
# Write version A and version B.

# Version A - simulated:

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# yes/no input handler - case insensitive.
#
# Ask user: "Do you want to continue? (yes/no): "
# Accept as YES: "yes", "y", "YES", "Yes", "Y", "yeah"
# Accept as NO:  "no",  "n", "NO",  "No",  "N", "nope"
#
# Print:
#   User typed: Yes
#   Normalized: yes
#   Decision:   Continuing...
#   OR
#   Decision:   Stopping.
#
# Test with FOUR simulated inputs:
#   "YES", "n", "Yeah", "NOPE"
# Write version A and version B.

# Version A - simulated (test all four):

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# Default value pattern.
#
# Ask for username and age.
# If user leaves username empty → use "Anonymous"
# If user leaves age empty     → use 0
#
# Expected interaction A (values provided):
#   Enter username (or ENTER for Anonymous): Anna
#   Enter age (or ENTER for 0): 25
#   Username: Anna
#   Age: 25
#
# Expected interaction B (defaults used):
#   Enter username (or ENTER for Anonymous):
#   Enter age (or ENTER for 0):
#   Username: Anonymous
#   Age: 0
#
# Simulate both scenarios in version A.
# Write version A (both scenarios) and version B.

# Version A - simulated (scenario with values):

# Version A - simulated (scenario with defaults):

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Multiple values on one line.
#
# Ask user to enter 5 numbers separated by spaces.
# Calculate and print: sum, average, min, max.
#
# Expected interaction:
#   Enter 5 numbers separated by spaces: 10 20 30 40 50
#   Numbers: [10, 20, 30, 40, 50]
#   Sum:     150
#   Average: 30.0
#   Minimum: 10
#   Maximum: 50
#
# Use map(int, raw.split()) to convert all at once.
# Write version A and version B.

# Version A - simulated:

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# bool() pitfall and correct boolean input.
#
# Ask user: "Is the sequence coding? (true/false): "
# Handle these inputs correctly:
#   "true", "True", "TRUE", "yes", "1", "y"  → True
#   "false", "False", "FALSE", "no", "0", "n" → False
#   anything else → print "Invalid input" and treat as False
#
# Show the pitfall first:
#   raw = "False"
#   print(f"Wrong way - bool(raw): {bool(raw)}")  ← True!
#   print(f"Right way:             {correct result}")
#
# Test with simulated inputs: "True", "false", "YES", "0", "maybe"
# Write version A and version B.

# Version A - simulated:

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Safe integer input with error handling.
#
# Write a function safe_int(prompt, simulated, default=0)
# that:
#   1. Tries to convert simulated to int
#   2. If successful - returns the int
#   3. If ValueError - prints error message and returns default
#   4. Always strips the input first
#
# Test with these simulated inputs:
#   "42"          → should return 42
#   "3.14"        → should fail, return 0
#   "abc"         → should fail, return 0
#   ""            → should fail, return 0
#   "  25  "      → should return 25 (after strip)
#   "100" (default=999) → should return 100
#   "abc" (default=999) → should fail, return 999
#
# Print result and type for each test.

# Version A - simulated:

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Build a simple personal info form.
#
# Ask for and collect:
#   - First name     (str, stripped, title case)
#   - Last name      (str, stripped, title case)
#   - Age            (int, must be between 1-120, default 0)
#   - Height in cm   (float, default 0.0)
#   - City           (str, stripped, title case, default "Unknown")
#
# After collecting all data, print a formatted card:
#
#   ================================
#   PERSONAL INFORMATION
#   ================================
#   Full name : Anna Kowalski
#   Age       : 25 years
#   Height    : 165.5 cm
#   City      : Warsaw
#   ================================
#
# Simulate ALL inputs in version A.
# Write version A and version B.

# Version A - simulated:

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# CSV input parser.
#
# Ask user to enter student data in this format:
#   Name,Age,Score,City
# Example:
#   Anna Kowalski,22,95.5,Warsaw
#
# Parse it and print:
#
#   Parsed data:
#   Name:  Anna Kowalski
#   Age:   22
#   Score: 95.5
#   City:  Warsaw
#
#   Analysis:
#   First name:  Anna
#   Last name:   Kowalski
#   Pass/Fail:   Pass (score >= 60)
#   Grade:       A (score >= 90)
#   Adult:       True (age >= 18)
#
# Simulate input with two different entries in version A.
# Write version A and version B.

# Version A - simulated:

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Multi-input calculator with operation selection.
#
# Expected interaction:
#   ================================
#   SIMPLE CALCULATOR
#   ================================
#   Enter first number  : 15.5
#   Enter operation (+,-,*,/,//,%,**): **
#   Enter second number : 2
#   ================================
#   15.5 ** 2.0 = 240.25
#   ================================
#
# Requirements:
#   - Convert both numbers to float
#   - Support all 7 operations: + - * / // % **
#   - If operation is invalid: print "Unknown operation"
#   - If division by zero: print "Cannot divide by zero"
#   - Round result to 4 decimal places
#   - Show full expression in output: "15.5 ** 2.0 = 240.25"
#
# Simulate 5 different test cases in version A:
#   ("10", "+", "5"), ("20", "/", "4"),
#   ("3", "**", "3"), ("10", "/", "0"),
#   ("10", "?", "5")
# Write version A and version B.

# Version A - simulated:

# Version B - real input:


# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Interactive profile builder with full validation.
#
# Simulate a complete registration form.
# Collect and validate ALL fields:
#
#   username:
#     - 3 to 20 characters
#     - no spaces
#     - converted to lowercase
#
#   age:
#     - valid integer
#     - between 13 and 120
#
#   email:
#     - contains exactly one "@"
#     - contains "." after the "@"
#     - does not start with "@"
#
#   score:
#     - valid float
#     - between 0.0 and 100.0
#
# For each field, print whether it is valid or not.
# At the end print:
#
#   ================================
#   REGISTRATION SUMMARY
#   ================================
#   Username : anna_99       ✓
#   Age      : 25            ✓
#   Email    : anna@mail.com ✓
#   Score    : 98.5          ✓
#   --------------------------------
#   Status   : ACCEPTED
#   ================================
#   OR
#   Status   : REJECTED (list failed fields)
#
# Simulate TWO complete registrations in version A:
#   One valid, one with multiple invalid fields.
# Write version A and version B.

# Version A - simulated:

# Version B - real input:
