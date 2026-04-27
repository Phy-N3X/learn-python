# ============================================================
# MODULE 01 | EXERCISES 02 - Numbers
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create one variable of each numeric type:
#   - an integer
#   - a float
#   - a complex number

# Print each variable and its type.

# Expected output:
#   10 <class 'int'>
#   3.14 <class 'float'>
#   (2+3j) <class 'complex'>
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("Exercise 1:")

random_int = 100
random_float = 4.522
random_complex = 4 + 2j

print(random_int,type(random_int))
print(random_float, type(random_float))
print(random_complex, type(random_complex))



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create two variables:
#   a = 17
#   b = 5

# Print the result of all seven arithmetic operations:
#   - addition
#   - subtraction
#   - multiplication
#   - division
#   - floor division
#   - modulo
#   - exponentiation

# Label each result clearly.

# Expected output format:
#   17 + 5 = 22
#   17 - 5 = 12
#   etc.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 2:")

a = 17
b = 5

print("a:", a, "b:", b)
print("a + b: ", a + b)
print("a - b: ", a - b)
print("a * b: ", a * b)
print("a / b: ", a / b)
print("a // b: ", a // b)
print("a % b: ", a % b)
print("a ** b: ", a ** b)



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Use a single variable: x = 100

# Apply all assignment operators step by step:
#   += 50
#   -= 30
#   *= 2
#   /= 4
#   //= 3
#   %= 7
#   **= 2

# Print x after each operation.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
x = 100

x += 50
print(x)

x -= 30
print(x)

x *= 2
print(x)

x /= 4
print(x)

x //= 3
print(x)

x %= 7
print(x)

x **= 2
print(x)



# ------------------------------------------------------------
# EXERCISE 4 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Use: abs(), round(), min(), max(), pow(), divmod()

# Given: numbers = -7.8, 3.2, -1, 5.5, 2

# Find and print:
#   1. Absolute value of -7.8
#   2. Round 3.14159 to 3 decimal places
#   3. Minimum of all five numbers
#   4. Maximum of all five numbers
#   5. 2 to the power of 8 using pow()
#   6. Floor division and remainder of 23 divided by 4
#      using divmod() - print both values separately
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 4:")

print("1. ", abs(-7.8))
print("2. ", round(3.14159, 3))
print("3. ", min(-7.8, 3.2, -1, 5.5, 2))
print("4. ", max(-7.8, 3.2, -1, 5.5, 2))
print("5. ", pow(2, 8))

quotient, remainder = divmod(23, 4)
print(quotient)
print(remainder)



# ------------------------------------------------------------
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
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
# CODE:
# ------------------------------------------------------------
print("\nExercise 5:")

import math

print("PI: ", math.pi)
print("Euler number: ", math.e)
print("Square root of 256: ", math.sqrt(256))
print("5 factorial: ", math.factorial(5))
print("Ceiling of 4.1: ", math.ceil(4.1))
print("Floor of 4.9: ", math.floor(4.9))



# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Predict the output of each line without running it first.
# Write your prediction as a comment, then run and verify.
#   print(10 / 2)
#   print(10 // 3)
#   print(10 % 3)
#   print(2 ** 8)
#   print(-7 // 2)
#   print(type(10 / 2))
#   print(type(10 // 2))
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 6:")

print(10 / 2)          # 5.0
print(10 // 3)         # 3
print(10 % 3)          # 1
print(2 ** 8)          # 256
print(-7 // 2)         # -4
print(type(10 / 2))    # float
print(type(10 // 2))   # int



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Operator precedence - predict the result without running.
# Write prediction as comment, then verify.
#   a = 2 + 3 * 4
#   b = (2 + 3) * 4
#   c = 2 ** 3 ** 2
#   d = (2 ** 3) ** 2
#   e = 10 - 3 - 2
#   f = 100 / 10 * 2
#   g = 100 / (10 * 2)
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 7:")

a = 2 + 3 * 4          # 14
b = (2 + 3) * 4        # 20
c = 2 ** 3 ** 2        # 512
d = (2 ** 3) ** 2      # 64
e = 10 - 3 - 2         # 5
f = 100 / 10 * 2       # 20.0
g = 100 / (10 * 2)     # 5.0



# ------------------------------------------------------------
# EXERCISE 8 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Investigate the floating point pitfall.

# 1. Print the result of 0.1 + 0.2
# 2. Print whether 0.1 + 0.2 == 0.3
# 3. Import math and use math.isclose() to compare them
# 4. Print whether math.isclose(0.1 + 0.2, 0.3)
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 8:")

import math

num_a = 0.1
num_b = 0.2

print("a + b: ", num_a + num_b)
print("a + b == 0.3? ", num_a + num_b == 0.3)
print("a + b == 0.3 with 'math.isclose': ", math.isclose(num_a + num_b, 0.3))



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Print round() for these values:
#   0.5, 1.5, 2.5, 3.5, 4.5, 5.5

# Write a comment describing the pattern you notice.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 9:")

print(round(0.5))
print(round(1.5))
print(round(2.5))
print(round(3.5))
print(round(4.5))
print(round(5.5))

# round() function always rounds to the NEAREST even number



# ------------------------------------------------------------
# EXERCISE 10 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Use the math module only (no manual formulas).
# Calculate and print:
#   1. log base 10 of 10000
#   2. log base 2 of 512
#   3. natural log of e²  (hint: math.e ** 2)
#   4. sin of 90 degrees  (hint: convert to radians first!)
#   5. cos of 180 degrees (hint: convert to radians first!)
#   6. GCD of 252 and 105
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 10:")

import math

print("1. ", math.log(100, 10))
print("2. ", math.log2(512))
print("3. ", math.log(math.e ** 2))
print("4. ", math.sin(math.radians(90)))
print("5. ", math.cos(math.radians(180)))
print("6. ", math.gcd(252, 105))



# ------------------------------------------------------------
# EXERCISE 11 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# For each operation below, predict both the result
# and the type running (write as comments).
#   3 + 4
#   3.0 + 4
#   3 + 4.0
#   3.0 + 4.0
#   10 / 2
#   10 // 2
#   10 // 2.0
#   10.0 // 2
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 11:")

print(3 + 4)         # 7 (int)
print(3.0 + 4)       # 7.0 (float + int = float)
print(3 + 4.0)       # 7.0 (int + float = float)
print(3.0 + 4.0)     # 7.0 (float + float = float)
print(10 / 2)        # 5.0 (float)
print(10 // 2)       # 5 (int)
print(10 // 2.0)     # 5.0 (int // float = float)
print(10.0 // 2)     # 5.0 (float // int = float)



# ------------------------------------------------------------
# EXERCISE 12 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Without using any formula written by hand, use only Python
# math operations to calculate:
#   1. Area of a circle with radius 7
#      formula: π × r²

#   2. Hypotenuse of a right triangle
#      with sides a=3, b=4
#      formula: √(a² + b²)

#   3. Compound interest
#      principal=1000, rate=0.05, years=10
#      formula: principal × (1 + rate) ** years

# Print each result rounded to 2 decimal places.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 12:")

print("Area of a circle: ", round(3.14159265 * 7 ** 2, 2))
print("Hypotenuse: ", round(((3 ** 2 + 4 ** 2) ** 0.5), 2))
print("Compound interest: ", round(1000 * (1 + 0.05) ** 10, 2))



# ------------------------------------------------------------
# EXERCISE 13 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# You have 1000 seconds total.

# Using only // and % operators, calculate:
#   1. How many full hours in 1000 seconds?
#   2. How many full minutes remain after removing full hours?
#   3. How many seconds remain after removing full minutes?

# Print result in format:
#   1000 seconds = X hours, Y minutes, Z seconds

# Verify: X*3600 + Y*60 + Z should equal 1000
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 13:")

total_seconds = 1000

hours = total_seconds // 3600
remaining = total_seconds % 3600

minutes = remaining // 60
seconds = remaining % 60

print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")

check = hours * 3600 + minutes * 60 + seconds
print(f"Verify: {hours} * 3600 + {minutes} * 60 + {seconds} = {check}")



# ------------------------------------------------------------
# EXERCISE 14 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# 1. Print 0.1 + 0.2 + 0.3
# 2. Print 0.1 + 0.2 + 0.3 == 0.6
# 3. Print (0.1 + 0.2) + 0.3 == 0.1 + (0.2 + 0.3)
#    Are they equal? Why or why not?
# 4. Use math.isclose() with custom tolerance rel_tol=1e-9
#    to compare 0.1 + 0.2 + 0.3 with 0.6
# 5. Print the result of:
#    round(0.1 + 0.2 + 0.3, 10) == round(0.6, 10)
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 14:")

import math

print("0.1 + 0.2 + 0.3 = ", 0.1 + 0.2 + 0.3)
print("0.1 + 0.2 + 0.3 == 0.6? ", 0.1 + 0.2 + 0.3 == 0.6)
print("(0.1 + 0.2) + 0.3 == 0.1 + (0.2 + 0.3) ", (0.1 + 0.2) + 0.3 == 0.1 + (0.2 + 0.3))

print(math.isclose(0.1 + 0.2 + 0.3, 0.6, rel_tol=1e-9))
print(round(0.1 + 0.2 + 0.3, 10) == round(0.6, 10))



# ------------------------------------------------------------
# EXERCISE 15 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given a = 2, b = 3, c = 4:

# 1. Prove that (a+b)² = a² + 2ab + b²
#    Calculate both sides separately and compare with ==
#    Use math.isclose() in case of float issues

# 2. Find x where: 2x² + 3x - 5 = 0
#    One solution is x = 1. Verify it by substituting
#    into the formula and checking if result == 0
#    Use math.isclose() for comparison

# 3. Calculate how many digits 2**1000 has
#    Hint: number of digits = floor(log10(n)) + 1
#    Use math.log10() and math.floor()
#    Print: "2**1000 has X digits"

# 4. Verify Euler's formula for x = math.pi:
#    e^(i*π) + 1 should equal 0
#    In Python: use cmath module (complex math)
#    import cmath
#    result = cmath.exp(cmath.pi * 1j) + 1
#    Print result and use math.isclose(abs(result), 0)
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 15:")

import math
import cmath

a, b, c = 2, 3, 4

print("=" * 45)

left_side  = (a + b) ** 2
right_side = a ** 2 + 2 * a * b + b ** 2

print("1. SQUARE OF A SUM")
print(f"(a + b)² = ({a} + {b})² = {left_side}")
print(f"a²+ 2ab + b²  = {a}² + 2 · {a} · {b} + {b}² = {right_side}")
print(f"Equal? = {math.isclose(left_side, right_side)}")

print("=" * 45)

x = 1
result = 2 * x ** 2 + 3 * x - 5

print("2. QUADRATIC EQUATION  2x² + 3x - 5 = 0")
print(f"x = {x}")
print(f"2({x})² + 3({x}) - 5 = {result}")
print(f"Result is 0? = {math.isclose(result, 0)}")

print("=" * 45)

digits = math.floor(1000 * math.log10(2)) + 1

print("3. HOW MANY DIGITS HAS 2^1000?")
print(f"floor(log10(2^1000)) + 1 = {digits}")
print(f"2^1000 has {digits} digits")

print("=" * 45)

result_euler = cmath.exp(cmath.pi * 1j) + 1

print("4. EULER'S FORMULA: e^(iπ) + 1 = 0")
print(f"e^(iπ) + 1 = {result_euler}")
print(f"abs(result) = {abs(result_euler)}")
print(f"Close to 0? = {math.isclose(abs(result_euler), 0)}")

print("=" * 45)