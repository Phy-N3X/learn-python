# ============================================================
# MODULE 01 | LECTURE 02 - Numbers
# ============================================================
# What you will learn:
#   - Integer (int)
#   - Float (float)
#   - Complex (complex)
#   - Arithmetic operators
#   - Operator precedence
#   - Built-in math functions
#   - Common pitfalls with numbers
# ============================================================


# ------------------------------------------------------------
# PART 1: Integer (int)
# ------------------------------------------------------------

# Integers are whole numbers - no decimal point
# Positive, negative or zero - no limit on size in Python!

x = 10
y = -5
z = 0
big = 1_000_000_000   # underscores for readability - Python ignores them

print(x)              # 10
print(big)            # 1000000000
print(type(x))        # <class 'int'>

# Python integers have no size limit (unlike C, Java)
huge = 99999999999999999999999999999999999999
print(huge)           # works perfectly fine!


# ------------------------------------------------------------
# PART 2: Float (float)
# ------------------------------------------------------------

# Floats are numbers WITH a decimal point
pi = 3.14159
temperature = -12.5
price = 9.99
simple = 1.0          # this is float, NOT int!

print(type(pi))       # <class 'float'>
print(type(simple))   # <class 'float'>

# Scientific notation - useful for very small or large numbers
avogadro = 6.022e23       # 6.022 × 10²³
electron_mass = 9.11e-31  # 9.11 × 10⁻³¹

print(avogadro)           # 6.022e+23
print(electron_mass)      # 9.11e-31


# ------------------------------------------------------------
# PART 3: Complex (complex)
# ------------------------------------------------------------

# Complex numbers have a real and imaginary part
# Used in signal processing, quantum computing
# Less common in everyday programming

c1 = 3 + 4j           # j is the imaginary unit in Python
c2 = complex(2, -1)   # complex(real, imaginary)

print(c1)             # (3+4j)
print(c2)             # (2-1j)
print(type(c1))       # <class 'complex'>

print(c1.real)        # 3.0  - real part
print(c1.imag)        # 4.0  - imaginary part


# ------------------------------------------------------------
# PART 4: Arithmetic Operators
# ------------------------------------------------------------

a = 17
b = 5

# Addition
print(a + b)          # 22

# Subtraction
print(a - b)          # 12

# Multiplication
print(a * b)          # 85

# Division - ALWAYS returns float!
print(a / b)          # 3.4
print(type(a / b))    # <class 'float'>

# Floor division - rounds DOWN to nearest integer
print(a // b)         # 3   (not 3.4, not 4 - always floors!)
print(-17 // 5)       # -4  (floors towards negative infinity!)

# Modulo - remainder after division
print(a % b)          # 2   (17 = 5*3 + 2)
print(10 % 3)         # 1
print(10 % 2)         # 0   (even number - no remainder)

# Exponentiation - power
print(2 ** 10)        # 1024
print(9 ** 0.5)       # 3.0 (square root!)
print(27 ** (1/3))    # 3.0 (cube root!)


# ------------------------------------------------------------
# PART 5: Operator Precedence (PEMDAS / BODMAS)
# ------------------------------------------------------------

# Python follows standard math rules:
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Multiplication *, Division /, //, %
# 4. Addition +, Subtraction -
# Left to right for same priority

print(2 + 3 * 4)        # 14  NOT 20 (multiplication first!)
print((2 + 3) * 4)      # 20  parentheses first
print(2 ** 3 ** 2)      # 512 NOT 64 (** is right-to-left: 2**9)
print((2 ** 3) ** 2)    # 64
print(10 - 3 - 2)       # 5   (left to right: (10-3)-2)
print(10 / 2 * 5)       # 25.0 (left to right: (10/2)*5)

# When in doubt - use parentheses!
result = (2 + 3) * (4 - 1) ** 2 / 3
print(result)           # 25.0


# ------------------------------------------------------------
# PART 6: Assignment Operators (shortcuts)
# ------------------------------------------------------------

x = 10

x += 5      # same as: x = x + 5
print(x)    # 15

x -= 3      # same as: x = x - 3
print(x)    # 12

x *= 2      # same as: x = x * 2
print(x)    # 24

x //= 5     # same as: x = x // 5
print(x)    # 4

x **= 3     # same as: x = x ** 3
print(x)    # 64

x %= 10     # same as: x = x % 10
print(x)    # 4


# ------------------------------------------------------------
# PART 7: Built-in Math Functions (no import needed!)
# ------------------------------------------------------------

# abs() - absolute value
print(abs(-42))         # 42
print(abs(3.14))        # 3.14

# round() - rounding
print(round(3.14159))       # 3
print(round(3.14159, 2))    # 3.14
print(round(3.14159, 4))    # 3.1416
print(round(2.5))           # 2  ← banker's rounding! (not 3)
print(round(3.5))           # 4  ← banker's rounding!

# min() and max()
print(min(3, 1, 4, 1, 5))  # 1
print(max(3, 1, 4, 1, 5))  # 5

# sum()
print(sum([1, 2, 3, 4, 5])) # 15

# pow() - same as **
print(pow(2, 10))           # 1024
print(pow(2, 10, 100))      # 24  ← pow(base, exp, mod) - very efficient!

# divmod() - floor division AND modulo at once
quotient, remainder = divmod(17, 5)
print(quotient)             # 3
print(remainder)            # 2


# ------------------------------------------------------------
# PART 8: The math module (import needed)
# ------------------------------------------------------------

import math

# Constants
print(math.pi)          # 3.141592653589793
print(math.e)           # 2.718281828459045
print(math.inf)         # inf (infinity)
print(math.tau)         # 6.283... (2 * pi)

# Rounding functions
print(math.floor(3.9))  # 3  ← always rounds DOWN
print(math.ceil(3.1))   # 4  ← always rounds UP
print(math.trunc(3.9))  # 3  ← cuts decimal part (towards zero)
print(math.trunc(-3.9)) # -3 ← towards zero, NOT floor!

# Square root and power
print(math.sqrt(144))   # 12.0
print(math.pow(2, 10))  # 1024.0 ← always returns float!

# Logarithms
print(math.log(math.e)) # 1.0       natural log (base e)
print(math.log(100, 10))# 2.0       log base 10
print(math.log10(1000)) # 3.0       log base 10 shortcut
print(math.log2(1024))  # 10.0      log base 2

# Trigonometry (radians!)
print(math.sin(math.pi / 2))   # 1.0
print(math.cos(0))             # 1.0
print(math.degrees(math.pi))   # 180.0  radians → degrees
print(math.radians(180))       # 3.14...  degrees → radians

# factorial
print(math.factorial(5))       # 120  (5! = 5×4×3×2×1)
print(math.factorial(10))      # 3628800

# Greatest common divisor
print(math.gcd(48, 18))        # 6

# Is it infinity or NaN?
print(math.isinf(math.inf))    # True
print(math.isnan(float('nan')))# True


# ------------------------------------------------------------
# PART 9: Integer and Float interaction
# ------------------------------------------------------------

# int + int = int
print(type(3 + 4))          # <class 'int'>

# float + float = float
print(type(3.0 + 4.0))      # <class 'float'>

# int + float = float (Python promotes to float)
print(type(3 + 4.0))        # <class 'float'>
print(3 + 4.0)              # 7.0

# Division ALWAYS gives float
print(type(10 / 2))         # <class 'float'>
print(10 / 2)               # 5.0  NOT 5!

# Floor division gives int (if both are int)
print(type(10 // 3))        # <class 'int'>
print(type(10.0 // 3))      # <class 'float'>


# ------------------------------------------------------------
# PART 10: Common Pitfalls ⚠️
# ------------------------------------------------------------

# PITFALL 1: Floating point precision
print(0.1 + 0.2)            # 0.30000000000000004  ← NOT 0.3!
print(0.1 + 0.2 == 0.3)     # False ← dangerous in comparisons!

# Solution: use round() or math.isclose()
print(round(0.1 + 0.2, 10) == 0.3)         # True
print(math.isclose(0.1 + 0.2, 0.3))        # True ← correct way!

# PITFALL 2: Integer division surprises
print(7 / 2)                # 3.5   (float division)
print(7 // 2)               # 3     (floor division)
print(-7 // 2)              # -4    (floors towards -infinity!)

# PITFALL 3: Banker's rounding
print(round(0.5))           # 0  ← rounds to EVEN number
print(round(1.5))           # 2  ← rounds to EVEN number
print(round(2.5))           # 2  ← rounds to EVEN number
print(round(3.5))           # 4  ← rounds to EVEN number

# PITFALL 4: Very large floats lose precision
big_float = 1e308
print(big_float)            # 1e+308
bigger = 1e309
print(bigger)               # inf  ← overflow!

# PITFALL 5: Division by zero
# print(10 / 0)             # ZeroDivisionError! (we'll handle this in Module 11)


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ int   = whole numbers, unlimited size
# ✅ float = decimal numbers, scientific notation (e)
# ✅ complex = real + imaginary (j)
# ✅ Operators: + - * / // % **
# ✅ Precedence: () > ** > * / // % > + -
# ✅ Shortcuts: += -= *= /= //= %= **=
# ✅ Built-in: abs() round() min() max() pow() divmod()
# ✅ math module: sqrt log sin cos floor ceil factorial gcd
# ✅ int + float = float, / always float
# ⚠️  0.1 + 0.2 ≠ 0.3  use math.isclose()
# ⚠️  round() uses banker's rounding
# ⚠️  -7 // 2 = -4  not -3!