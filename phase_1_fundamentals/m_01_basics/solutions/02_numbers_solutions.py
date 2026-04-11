# ============================================================
# MODULE 01 | EXERCISES 02 - Numbers
# ============================================================
# 15 exercises - numbers only
# Allowed from previous lectures: variables, print(), type()
# Nothing else from lecture 01 is required
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
random_int = 100
random_float = 4.522
random_complex = 4 + 2j

print(random_int,type(random_int))
print(random_float, type(random_float))
print(random_complex, type(random_complex))



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
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
import math

num_a = 0.1
num_b = 0.2

print("a + b: ", num_a + num_b)
print("a + b == 0.3? ", num_a + num_b == 0.3)
print("a + b == 0.3 with 'math.isclose': ", math.isclose(num_a + num_b, 0.3))



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
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
# int and float interaction.
# For each operation below, predict BOTH the result
# and the TYPE before running. Write as comments.
#
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
print("Area of a circle: ", round(3.14159265 * 7 ** 2, 2))
print("Hypotenuse: ", round(((3 ** 2 + 4 ** 2) ** 0.5), 2))
print("Compound interest: ", round(1000 * (1 + 0.05) ** 10, 2))



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
# EXERCISE 14 ✅ | HARD
# ------------------------------------------------------------
import math

print("0.1 + 0.2 + 0.3 = ", 0.1 + 0.2 + 0.3)
print("0.1 + 0.2 + 0.3 == 0.6? ", 0.1 + 0.2 + 0.3 == 0.6)
print("(0.1 + 0.2) + 0.3 == 0.1 + (0.2 + 0.3) ", (0.1 + 0.2) + 0.3 == 0.1 + (0.2 + 0.3))

print(math.isclose(0.1 + 0.2 + 0.3, 0.6, rel_tol=1e-9))
print(round(0.1 + 0.2 + 0.3, 10) == round(0.6, 10))


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