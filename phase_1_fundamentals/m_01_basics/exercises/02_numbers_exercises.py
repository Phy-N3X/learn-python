# ============================================================
# MODULE 01 | EXERCISES 02 - Numbers
# ============================================================
# 15 exercises - numbers only
# Allowed from previous lectures: variables, print(), type()
# Nothing else from lecture 01 is required
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Create one variable of each numeric type:
#   - an integer
#   - a float
#   - a complex number
# Print each variable and its type.
# Expected output format:
#   10 <class 'int'>
#   3.14 <class 'float'>
#   (2+3j) <class 'complex'>



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Create two variables:
#   a = 17
#   b = 5
# Print the result of ALL seven arithmetic operations:
#   addition, subtraction, multiplication,
#   division, floor division, modulo, exponentiation
# Label each result clearly.
# Expected output format:
#   17 + 5 = 22
#   17 - 5 = 12
#   ... etc.



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Use a single variable x = 100
# Apply ALL assignment operators step by step:
#   += 50
#   -= 30
#   *= 2
#   /= 4
#   //= 3
#   %= 7
#   **= 2
# Print x after EACH operation.



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use ONLY built-in functions (no import needed):
# abs(), round(), min(), max(), pow(), divmod()
#
# Given: numbers = -7.8, 3.2, -1, 5.5, 2
#
# Find and print:
#   1. Absolute value of -7.8
#   2. Round 3.14159 to 3 decimal places
#   3. Minimum of all five numbers
#   4. Maximum of all five numbers
#   5. 2 to the power of 8 using pow()
#   6. Floor division and remainder of 23 divided by 4
#      using divmod() - print both values separately



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Import math and use it to print:
#   1. The value of pi (to full precision)
#   2. The value of e (to full precision)
#   3. Square root of 256
#   4. 5 factorial
#   5. Ceiling of 4.1
#   6. Floor of 4.9
# Label each result.



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Predict the output of each line WITHOUT running it first.
# Write your prediction as a comment, then run and verify.
#
# print(10 / 2)
# print(10 // 3)
# print(10 % 3)
# print(2 ** 8)
# print(-7 // 2)
# print(type(10 / 2))
# print(type(10 // 2))



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Operator precedence - predict the result WITHOUT running.
# Write prediction as comment, then verify.
#
# a = 2 + 3 * 4
# b = (2 + 3) * 4
# c = 2 ** 3 ** 2
# d = (2 ** 3) ** 2
# e = 10 - 3 - 2
# f = 100 / 10 * 2
# g = 100 / (10 * 2)



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# Investigate the floating point pitfall.
#
# 1. Print the result of 0.1 + 0.2
# 2. Print whether 0.1 + 0.2 == 0.3
# 3. Import math and use math.isclose() to compare them
# 4. Print whether math.isclose(0.1 + 0.2, 0.3)
# 5. Write a comment explaining WHY 0.1 + 0.2 != 0.3



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Banker's rounding investigation.
# Print round() for these values:
#   0.5, 1.5, 2.5, 3.5, 4.5, 5.5
# Write a comment describing the pattern you notice.
# Then explain: when does Python round UP vs DOWN?



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Use the math module ONLY (no manual formulas).
# Calculate and print:
#   1. log base 10 of 10000
#   2. log base 2 of 512
#   3. natural log of e²  (hint: math.e ** 2)
#   4. sin of 90 degrees  (hint: convert to radians first!)
#   5. cos of 180 degrees (hint: convert to radians first!)
#   6. GCD of 252 and 105



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# int and float interaction.
# For each operation below, predict BOTH the result
# and the TYPE before running. Write as comments.
#
# 3 + 4
# 3.0 + 4
# 3 + 4.0
# 3.0 + 4.0
# 10 / 2
# 10 // 2
# 10 // 2.0
# 10.0 // 2



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Without using any formula written by hand,
# use ONLY Python math operations to calculate:
#
#   1. Area of a circle with radius 7
#      formula: π × r²
#
#   2. Hypotenuse of a right triangle
#      with sides a=3, b=4
#      formula: √(a² + b²)
#
#   3. Compound interest
#      principal=1000, rate=0.05, years=10
#      formula: principal × (1 + rate) ** years
#
# Print each result rounded to 2 decimal places.



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Floor division and modulo - real use case.
# You have 1000 seconds total.
#
# Using ONLY // and % operators, calculate:
#   1. How many full hours in 1000 seconds?
#   2. How many full minutes remain after removing full hours?
#   3. How many seconds remain after removing full minutes?
#
# Print result in format:
#   1000 seconds = X hours, Y minutes, Z seconds
#
# Verify: X*3600 + Y*60 + Z should equal 1000



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Floating point precision deep dive.
#
# 1. Print 0.1 + 0.2 + 0.3
# 2. Print 0.1 + 0.2 + 0.3 == 0.6
# 3. Print (0.1 + 0.2) + 0.3 == 0.1 + (0.2 + 0.3)
#    Are they equal? Why or why not? (write as comment)
# 4. Use math.isclose() with custom tolerance rel_tol=1e-9
#    to compare 0.1 + 0.2 + 0.3 with 0.6
# 5. Print the result of:
#    round(0.1 + 0.2 + 0.3, 10) == round(0.6, 10)
# 6. Write a comment: which method is safest for
#    comparing floats and why?



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Number system investigation using only Python math.
#
# Given a = 2, b = 3, c = 4:
#
# 1. Prove that (a+b)² = a² + 2ab + b²
#    Calculate both sides separately and compare with ==
#    Use math.isclose() in case of float issues
#
# 2. Find x where: 2x² + 3x - 5 = 0
#    One solution is x = 1. Verify it by substituting
#    into the formula and checking if result == 0
#    Use math.isclose() for comparison
#
# 3. Calculate how many digits 2**1000 has
#    Hint: number of digits = floor(log10(n)) + 1
#    Use math.log10() and math.floor()
#    Print: "2**1000 has X digits"
#
# 4. Verify Euler's formula for x = math.pi:
#    e^(i*π) + 1 should equal 0
#    In Python: use cmath module (complex math)
#    import cmath
#    result = cmath.exp(cmath.pi * 1j) + 1
#    Print result and use math.isclose(abs(result), 0)

