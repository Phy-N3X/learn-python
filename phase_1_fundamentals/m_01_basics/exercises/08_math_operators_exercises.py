# ============================================================
# MODULE 01 | EXERCISES 08 - Math Operators
# ============================================================
# 15 exercises - math operators only
# Allowed from previous lectures:
#   - variables, type()                 (lecture 01)
#   - int, float, complex               (lecture 02)
#   - string methods, f-strings         (lecture 03)
#   - bool, comparison operators        (lecture 04)
#   - print(), sep, end                 (lecture 05)
#   - input() patterns                  (lecture 06)
#   - comments and docstrings           (lecture 07)
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Basic operators - predict then verify.
# For each expression, write your prediction as a comment
# BEFORE running. Then run and verify.
#
# a = 20
# b = 6
#
# a + b
# a - b
# a * b
# a / b
# a // b
# a % b
# a ** b
# type(a / b)
# type(a // b)
#
# For each: write "# Prediction: X" then verify.
# If wrong, write "# Actual: X and WHY I was wrong: ..."



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Augmented assignment operators.
# Start with x = 100.
# Apply EACH augmented operator step by step.
# Print x AND its type after EVERY operation.
#
# Operations in order:
#   += 50
#   -= 30
#   *= 3
#   /= 6           ← notice type change!
#   //= 4
#   %= 7
#   **= 2
#
# Expected output format:
#   After +=  50: x = 150   type = <class 'int'>
#   After -=  30: x = 120   type = <class 'int'>
#   ...



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Operator precedence - predict each result.
# Write prediction as comment BEFORE running.
# If wrong, explain why in a comment.
#
#   2 + 3 * 4
#   (2 + 3) * 4
#   2 ** 3 ** 2
#   (2 ** 3) ** 2
#   -2 ** 2
#   (-2) ** 2
#   10 - 4 - 2
#   10 / 2 * 5
#   10 / (2 * 5)
#   2 + 3 * 4 - 1
#   100 % 30 // 4
#   2 ** 2 ** 2 ** 2



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Floor division and modulo - convert seconds.
# Given total_seconds = 9999
#
# Using ONLY // and %:
#   1. How many full hours?
#   2. How many full minutes remain?
#   3. How many seconds remain?
#
# Print: "9999 seconds = Xh Ym Zs"
# Verify: X*3600 + Y*60 + Z == 9999
# Print verification result (True/False)



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Modulo patterns.
# Using ONLY the % operator:
#
# For numbers 1 to 15, print:
#   - "even" if divisible by 2
#   - "odd" if not divisible by 2
#   - Also mark multiples of 3 with "(x3)"
#   - Also mark multiples of 5 with "(x5)"
#
# Expected output (partial):
#   1: odd
#   2: even
#   3: odd (x3)
#   4: even
#   5: odd (x5)
#   6: even (x3)
#   ...
#   15: odd (x3) (x5)
#
# Use a for loop: for n in range(1, 16):



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Exponentiation patterns.
# Using ONLY the ** operator (no math module):
#
#   1. Calculate square root of 625
#      Hint: x ** 0.5
#
#   2. Calculate cube root of 1000
#      Hint: x ** (1/3)
#
#   3. Calculate 2 to the power of 0, 1, 2, ... 10
#      Print each result on one line separated by spaces
#
#   4. Verify: does (-2)**2 equal -(2**2)?
#      Print both and explain the difference
#
#   5. Calculate compound interest:
#      principal = 5000, rate = 7%, years = 20
#      Formula: principal * (1 + rate/100) ** years
#      Print: "After 20 years: $X"



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# math module - use ONLY math functions for all calculations.
# No ** operator or manual formulas allowed.
#
#   1. Square root of 1764
#   2. Cube root of 3375
#      Hint: math.pow(x, 1/3)
#   3. log base 10 of 1000000
#   4. log base 2 of 65536
#   5. factorial of 12
#   6. GCD of 144 and 60
#   7. LCM of 12, 15 and 20
#      Hint: math.lcm(a, b, c) works in Python 3.9+
#   8. sin(30°), cos(60°), tan(45°)
#      Convert degrees to radians first!
#   9. Ceiling and floor of 7.3 and -7.3
#      (4 values total - notice the pattern)
#   10. isclose(0.1 + 0.2, 0.3) - why is this needed?



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# Investigate floor() vs trunc() vs round() for negatives.
#
# For each of these values: 2.9, 2.5, 2.1, -2.1, -2.5, -2.9
# Print a table showing:
#
# Value  | floor | ceil | trunc | round
# -------|-------|------|-------|------
#   2.9  |   2   |   3  |   2   |   3
#   2.5  |   2   |   3  |   2   |   2  ← banker's rounding!
#   ...
#
# After the table, write comments explaining:
#   - When floor() and trunc() give DIFFERENT results
#   - What "banker's rounding" means for round()
#   - Which function rounds toward zero always



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a complete calculator using augmented assignment.
#
# Start with result = 0
# Perform these operations IN ORDER using augmented assignment:
#   1. Add 100
#   2. Multiply by 3
#   3. Subtract 50
#   4. Floor divide by 4
#   5. Raise to power 2
#   6. Take modulo of 100
#   7. Add square root of result (use math.sqrt, add as float)
#
# Print result after EACH step with the operation label.
# Write a docstring-style comment at the top explaining
# what this sequence calculates.



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Implement these utility functions WITH full docstrings.
# Use ONLY math operators (no if statements needed).
#
#   1. circle_area(radius)
#      Formula: π × r²
#
#   2. distance(x1, y1, x2, y2)
#      Formula: √((x2-x1)² + (y2-y1)²)
#
#   3. percent_change(old, new)
#      Formula: ((new - old) / old) * 100
#
#   4. celsius_to_all(celsius)
#      Returns: fahrenheit AND kelvin (two values!)
#      F = (C × 9/5) + 32
#      K = C + 273.15
#
# Test each with at least 2 examples.
# Print results with labels and 2 decimal places.



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Digit extraction using // and %.
# Given number = 78956
#
# Using ONLY // and % operators:
#   1. Extract the ones digit       (6)
#   2. Extract the tens digit       (5)
#   3. Extract the hundreds digit   (9)
#   4. Extract the thousands digit  (8)
#   5. Extract the ten-thousands digit (7)
#   6. Sum all digits               (7+8+9+5+6 = 35)
#   7. Reverse the digits           (65987)
#      Hint: build digit by digit using % and //
#
# Print each step with a label.
# Write a comment explaining the pattern for extracting
# the nth digit: number // 10**n % 10



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Wrap-around index using modulo.
#
# Given a playlist with 7 songs (index 0-6):
# songs = ["Song A", "Song B", "Song C", "Song D",
#          "Song E", "Song F", "Song G"]
#
# Using ONLY the % operator for index calculation:
#
#   1. Print songs at positions 0, 7, 14, 21
#      (all should show "Song A" - wrap around!)
#
#   2. Print songs at positions 5, 6, 7, 8, 9
#      (should wrap: E, F, G, A, B)
#
#   3. Simulate playing songs 0 through 20 (inclusive)
#      Print: "Track X: Song Y"
#
#   4. Given current_position = 4, steps_forward = 10
#      Where do you end up? (use %)
#      Print: "Starting at 4, moving 10 steps: Song X"
#
# Write a comment explaining WHY modulo is perfect
# for circular/wrap-around indexing.



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Float precision investigation.
#
#   1. Print 0.1 + 0.2
#      Is it 0.3? Why or why not? (comment)
#
#   2. Print (0.1 + 0.2) == 0.3
#      Print math.isclose(0.1 + 0.2, 0.3)
#
#   3. For each of these, print actual result and
#      whether it equals the expected value:
#      0.1 * 3   expected 0.3
#      1.1 + 2.2 expected 3.3
#      0.7 + 0.1 expected 0.8
#
#   4. Demonstrate the issue with % and floats:
#      Print (0.1 + 0.2) % 0.1
#      Why is this not 0.0? (comment)
#
#   5. Show the SAFE way to compare floats:
#      Print math.isclose(a, b, rel_tol=1e-9) for each case above
#
#   6. Write a comment: when does float precision matter most
#      and what should you do about it?



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a unit converter using math operators only.
# Write full docstrings for all functions.
#
# Functions to implement:
#
#   km_to_miles(km)         1 km = 0.621371 miles
#   kg_to_pounds(kg)        1 kg = 2.20462 pounds
#   liters_to_gallons(l)    1 liter = 0.264172 gallons
#   degrees_to_radians(d)   use math.pi
#   radians_to_degrees(r)   use math.pi
#   hectares_to_acres(h)    1 hectare = 2.47105 acres
#
# Then build a conversion TABLE:
#
# KM → Miles conversion table:
# ┌──────┬──────────┐
# │  km  │  miles   │
# ├──────┼──────────┤
# │    1 │    0.621 │
# │    5 │    3.107 │
# │   10 │    6.214 │
# │   50 │   31.069 │
# │  100 │   62.137 │
# └──────┴──────────┘
#
# Repeat the same table format for kg → pounds.
# Use f-string formatting for alignment.



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Mathematical sequence calculator.
# Implement and document the following sequences
# using ONLY Python math operators and a for loop.
#
#   1. Fibonacci sequence - first 15 numbers
#      0, 1, 1, 2, 3, 5, 8, 13, ...
#      Hint: use two variables and swap
#
#   2. Powers of 2 - first 16 values (2**0 to 2**15)
#      Print in format: "2^0 = 1"
#
#   3. Factorial sequence - 0! to 10!
#      Print in format: "10! = 3628800"
#      Hint: accumulate using *=
#
#   4. Running average
#      Given: values = [10, 25, 8, 42, 17, 33, 5, 61, 29, 14]
#      After each new value, print the running average
#      Format: "After 3 values: avg = 14.33"
#
#   5. Geometric series sum
#      Sum = a + a*r + a*r² + a*r³ + ... (10 terms)
#      Given: a = 1 (first term), r = 0.5 (ratio)
#      Print sum after each term, final answer rounded to 6 decimals
#
# Write a one-line comment above EACH sequence explaining
# what it is and where it appears in real life.
