# ============================================================
# MODULE 01 | LECTURE 08 - Math Operators
# ============================================================
# What you will learn:
#   - All arithmetic operators in depth
#   - Operator precedence (full rules)
#   - Assignment operators
#   - Augmented assignment
#   - Integer vs float results
#   - math module in depth
#   - Practical math patterns
#   - Common pitfalls
# ============================================================
# NOTE: This lecture expands on numbers (lecture 02)
#       Focus here is operators, precedence and patterns
#       not the number types themselves
# ============================================================


# ------------------------------------------------------------
# PART 1: All Arithmetic Operators
# ------------------------------------------------------------

# Python has 7 arithmetic operators:
# +   addition
# -   subtraction
# *   multiplication
# /   division         (always returns float)
# //  floor division   (rounds toward negative infinity)
# %   modulo           (remainder)
# **  exponentiation   (power)

a = 17
b = 5

print(f"a = {a}, b = {b}")
print(f"a + b  = {a + b}")          # 22  addition
print(f"a - b  = {a - b}")          # 12  subtraction
print(f"a * b  = {a * b}")          # 85  multiplication
print(f"a / b  = {a / b}")          # 3.4 division - ALWAYS float
print(f"a // b = {a // b}")         # 3   floor division
print(f"a % b  = {a % b}")          # 2   modulo (17 = 5*3 + 2)
print(f"a ** b = {a ** b}")         # 1419857  exponentiation


# ------------------------------------------------------------
# PART 2: Addition and Subtraction in Depth
# ------------------------------------------------------------

# Integer addition - stays integer
print(3 + 4)            # 7       int
print(3 + 4.0)          # 7.0     float (int + float = float)
print(-3 + -4)          # -7      negative numbers
print(-3 + 4)           # 1       mixed signs

# Unary operators - sign of a single number
x = 5
print(+x)               # 5       unary plus (rarely used)
print(-x)               # -5      unary minus (negation)
print(-(-x))            # 5       double negation

# Useful patterns with addition:
total = 0
total = total + 10      # accumulate values
total = total + 20
total = total + 30
print(total)            # 60

# Subtraction with negative results:
print(3 - 10)           # -7
print(-5 - 3)           # -8
print(-5 - -3)          # -2  (subtracting a negative = adding)


# ------------------------------------------------------------
# PART 3: Multiplication in Depth
# ------------------------------------------------------------

# Integer multiplication
print(6 * 7)            # 42
print(-3 * 4)           # -12
print(-3 * -4)          # 12   (negative × negative = positive)

# Float multiplication
print(2.5 * 4)          # 10.0
print(1.5 * 1.5)        # 2.25

# String multiplication (repetition) - not just numbers!
print("ha" * 3)         # hahaha
print("-" * 20)         # --------------------
print("=" * 20)         # ====================

# List multiplication (preview):
print([0] * 5)          # [0, 0, 0, 0, 0]
print([1, 2] * 3)       # [1, 2, 1, 2, 1, 2]

# Multiplication patterns:
# Scaling
original_price = 100
tax_rate       = 0.23       # 23% VAT
tax_amount     = original_price * tax_rate
print(f"Tax: {tax_amount}")     # 23.0

# Percentage
score      = 47
max_score  = 60
percentage = (score / max_score) * 100
print(f"Score: {percentage:.1f}%")  # 78.3%


# ------------------------------------------------------------
# PART 4: Division in Depth
# ------------------------------------------------------------

# Regular division / - ALWAYS returns float
print(10 / 2)           # 5.0    NOT 5!
print(7  / 2)           # 3.5
print(1  / 3)           # 0.3333333333333333
print(type(10 / 2))     # <class 'float'>

# Floor division // - rounds toward NEGATIVE infinity
print(17  // 5)         # 3    (17/5 = 3.4 → floor = 3)
print(-17 // 5)         # -4   (−17/5 = −3.4 → floor = −4 !)
print(17  // -5)        # -4   (-17/5 = -3.4 → floor = -4 !)
print(-17 // -5)        # 3    (17/5 = 3.4 → floor = 3)

# KEY INSIGHT: floor division floors toward NEGATIVE INFINITY
# not toward zero!
print(7  // 2)          # 3    (3.5 → 3)
print(-7 // 2)          # -4   (-3.5 → -4, NOT -3!)

# Float floor division - result is float but still floored
print(17.0 // 5)        # 3.0  ← float but floored
print(17   // 5.0)      # 3.0  ← float but floored

# Practical uses of floor division:
# Convert seconds to hours and minutes
total_seconds = 3725
hours   = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60
print(f"{total_seconds}s = {hours}h {minutes}m {seconds}s")  # 1h 2m 5s

# Divide into equal groups
students = 27
group_size = 4
full_groups     = students // group_size    # 6
remaining       = students % group_size     # 3
print(f"{full_groups} full groups, {remaining} remaining")

# Page numbers
items_per_page = 10
total_items    = 47
total_pages    = (total_items + items_per_page - 1) // items_per_page
print(f"Pages needed: {total_pages}")       # 5


# ------------------------------------------------------------
# PART 5: Modulo in Depth
# ------------------------------------------------------------

# Modulo % returns the REMAINDER after floor division
# a % b = a - (a // b) * b

print(17 % 5)           # 2    (17 = 5*3 + 2)
print(10 % 3)           # 1    (10 = 3*3 + 1)
print(10 % 2)           # 0    (10 = 2*5 + 0) - even number!
print(10 % 10)          # 0
print(3  % 10)          # 3    (when a < b, result is a)

# Modulo with negatives - follows floor division rule
print(-17 % 5)          # 3    not -2! (sign follows divisor in Python)
print(17  % -5)         # -3   (sign follows divisor)
print(-17 % -5)         # -2

# KEY PATTERN: result has same sign as the DIVISOR (b)

# Essential use cases of modulo:

# 1. Check if even or odd
for n in range(8):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

# 2. Check divisibility
print(100 % 4 == 0)     # True  - 100 is divisible by 4
print(100 % 7 == 0)     # False - 100 is not divisible by 7

# 3. Wrap around (circular indexing)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for i in range(10):
    print(f"Day {i}: {days[i % 7]}")    # wraps back to Mon after Sun

# 4. Extract digits
number = 12345
ones      = number % 10          # 5
tens      = (number // 10) % 10  # 4
hundreds  = (number // 100) % 10 # 3
print(f"Ones: {ones}, Tens: {tens}, Hundreds: {hundreds}")

# 5. Time calculations
minutes_total = 150
hours   = minutes_total // 60    # 2
minutes = minutes_total % 60     # 30
print(f"{minutes_total} minutes = {hours}h {minutes}m")


# ------------------------------------------------------------
# PART 6: Exponentiation in Depth
# ------------------------------------------------------------

# ** operator - raise to power
print(2 ** 10)          # 1024
print(3 ** 3)           # 27
print(10 ** 6)          # 1000000

# Fractional exponents - roots!
print(9   ** 0.5)       # 3.0    square root
print(27  ** (1/3))     # 3.0    cube root
print(16  ** 0.25)      # 2.0    fourth root
print(100 ** 0.5)       # 10.0

# Negative exponents - fractions!
print(2 ** -1)          # 0.5    (1/2)
print(2 ** -2)          # 0.25   (1/4)
print(10 ** -3)         # 0.001  (1/1000)

# Zero exponent - always 1
print(5 ** 0)           # 1
print(0 ** 0)           # 1  (by convention)

# Associativity - ** is RIGHT to left!
print(2 ** 3 ** 2)      # 512  = 2 ** (3**2) = 2 ** 9 = 512
print((2 ** 3) ** 2)    # 64   = 8 ** 2 = 64

# Practical uses:
# Compound interest
principal = 1000
rate      = 0.05        # 5% per year
years     = 10
amount    = principal * (1 + rate) ** years
print(f"After {years} years: ${amount:.2f}")    # $1628.89

# Scientific calculations
speed_of_light = 3 * 10 ** 8    # 300,000,000 m/s
print(f"Speed of light: {speed_of_light:,} m/s")

# Binary powers
print(2 ** 8)           # 256   - 8-bit values (0-255)
print(2 ** 16)          # 65536 - 16-bit values
print(2 ** 32)          # 4294967296 - 32-bit values


# ------------------------------------------------------------
# PART 7: Operator Precedence - Complete Rules
# ------------------------------------------------------------

# Python evaluates operators in this order (highest to lowest):
#
# Priority  Operator          Description
# --------  --------          -----------
# 1         ()                Parentheses
# 2         **                Exponentiation (right to left!)
# 3         +x, -x            Unary plus, unary minus
# 4         * / // %          Multiplication, division, modulo
# 5         + -               Addition, subtraction
#
# Same priority → left to right (except ** which is right to left)

# Examples - predict before running!
print(2 + 3 * 4)            # 14   (* before +)
print((2 + 3) * 4)          # 20   (parentheses first)
print(2 ** 3 + 1)           # 9    (** before +)
print(2 ** (3 + 1))         # 16   (parentheses first)
print(10 - 3 - 2)           # 5    (left to right: (10-3)-2)
print(2 ** 3 ** 2)          # 512  (right to left: 2**(3**2))
print(10 / 2 * 5)           # 25.0 (left to right: (10/2)*5)
print(10 / (2 * 5))         # 1.0  (parentheses change result)
print(-2 ** 2)              # -4   (** before unary minus: -(2**2))
print((-2) ** 2)            # 4    (parentheses: (-2)**2)

# Complex examples:
print(2 + 3 * 4 - 1)        # 13   3*4=12, 2+12=14, 14-1=13
print(2 ** 2 + 3 ** 2)      # 13   4 + 9
print(100 / 10 / 2)         # 5.0  (100/10)=10.0, 10.0/2=5.0
print(100 / (10 / 2))       # 20.0 10/2=5.0, 100/5.0=20.0

# GOLDEN RULE: when in doubt, use parentheses!
# Clear:
result = (2 + 3) * (4 - 1) ** 2 / 3
# This is easier to read than without parentheses


# ------------------------------------------------------------
# PART 8: Assignment Operators (Augmented Assignment)
# ------------------------------------------------------------

# Regular assignment:
x = 10

# Augmented assignment operators - shorthand for updating a variable

# += addition
x += 5          # same as: x = x + 5
print(x)        # 15

# -= subtraction
x -= 3          # same as: x = x - 3
print(x)        # 12

# *= multiplication
x *= 2          # same as: x = x * 2
print(x)        # 24

# /= division
x /= 4          # same as: x = x / 4
print(x)        # 6.0  ← becomes float!

# //= floor division
x = 25          # reset
x //= 4         # same as: x = x // 4
print(x)        # 6    ← stays int if both were int

# %= modulo
x %= 4          # same as: x = x % 4
print(x)        # 2

# **= exponentiation
x **= 10        # same as: x = x ** 10
print(x)        # 1024

# These work with strings too!
text = "Hello"
text += " World"        # concatenation
print(text)             # Hello World

text *= 2               # repetition
print(text)             # Hello WorldHello World

# Practical use - accumulating values:
total   = 0
count   = 0
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    total += num        # accumulate sum
    count += 1          # count items

average = total / count
print(f"Total: {total}, Count: {count}, Average: {average}")


# ------------------------------------------------------------
# PART 9: Math Module - Complete Reference
# ------------------------------------------------------------

import math

# --- Constants ---
print(f"pi      = {math.pi}")           # 3.141592653589793
print(f"e       = {math.e}")            # 2.718281828459045
print(f"tau     = {math.tau}")          # 6.283185307179586 (2*pi)
print(f"inf     = {math.inf}")          # inf
print(f"nan     = {math.nan}")          # nan
print(f"sqrt(2) = {math.sqrt(2)}")      # 1.4142135623730951

# --- Rounding ---
print(math.floor(3.9))      # 3   always rounds DOWN
print(math.floor(-3.1))     # -4  floors toward -infinity!
print(math.ceil(3.1))       # 4   always rounds UP
print(math.ceil(-3.9))      # -3  ceil toward +infinity!
print(math.trunc(3.9))      # 3   toward zero
print(math.trunc(-3.9))     # -3  toward zero (not floor!)

# Difference: floor vs trunc for negatives
print(math.floor(-3.1))     # -4  ← floor goes further negative
print(math.trunc(-3.1))     # -3  ← trunc goes toward zero

# --- Powers and Roots ---
print(math.sqrt(144))       # 12.0
print(math.sqrt(2))         # 1.4142135623730951
print(math.pow(2, 10))      # 1024.0  ← always float!
print(math.pow(2, 0.5))     # 1.4142135623730951
print(math.isqrt(17))       # 4   integer square root (floor)
print(math.isqrt(16))       # 4   exact

# --- Logarithms ---
print(math.log(math.e))     # 1.0  natural log (base e)
print(math.log(100, 10))    # 2.0  log base 10
print(math.log10(1000))     # 3.0  log base 10 shortcut
print(math.log2(1024))      # 10.0 log base 2
print(math.log(8, 2))       # 3.0  log base 2

# --- Trigonometry (input in RADIANS) ---
print(math.sin(0))                  # 0.0
print(math.sin(math.pi / 2))        # 1.0
print(math.cos(0))                  # 1.0
print(math.cos(math.pi))            # -1.0
print(math.tan(math.pi / 4))        # 1.0

# Convert between degrees and radians
print(math.degrees(math.pi))        # 180.0
print(math.radians(90))             # 1.5707963267948966

# --- Combinatorics ---
print(math.factorial(5))            # 120     5! = 5×4×3×2×1
print(math.factorial(10))           # 3628800
print(math.comb(10, 3))             # 120     "10 choose 3"
print(math.perm(10, 3))             # 720     permutations

# --- GCD and LCM ---
print(math.gcd(48, 18))             # 6
print(math.gcd(100, 75))            # 25
print(math.lcm(4, 6))              # 12
print(math.lcm(12, 18))            # 36

# --- Checking special values ---
print(math.isinf(math.inf))         # True
print(math.isinf(1e309))            # True  (overflow)
print(math.isinf(1000))             # False
print(math.isnan(math.nan))         # True
print(math.isnan(float("nan")))     # True
print(math.isnan(0))                # False
print(math.isfinite(42))            # True
print(math.isfinite(math.inf))      # False
print(math.isclose(0.1+0.2, 0.3))  # True  (with tolerance)

# --- Absolute value and sign ---
print(math.fabs(-3.14))             # 3.14  always float (vs abs())
print(math.copysign(3, -1))         # -3.0  copy sign from second arg
print(math.copysign(-3, 1))         # 3.0


# ------------------------------------------------------------
# PART 10: Practical Math Patterns
# ------------------------------------------------------------

import math

# Pattern 1: Rounding to n decimal places
pi = math.pi
print(round(pi, 0))     # 3.0
print(round(pi, 2))     # 3.14
print(round(pi, 4))     # 3.1416
print(round(pi, 6))     # 3.141593

# Pattern 2: Rounding to nearest multiple
def round_to_nearest(n, multiple):
    """Round n to nearest multiple."""
    return round(n / multiple) * multiple

print(round_to_nearest(47, 5))      # 45
print(round_to_nearest(48, 5))      # 50
print(round_to_nearest(123, 10))    # 120

# Pattern 3: Clamping a value between min and max
def clamp(value, minimum, maximum):
    """Clamp value between minimum and maximum."""
    return max(minimum, min(value, maximum))

print(clamp(5,  0, 10))     # 5   (within range)
print(clamp(-3, 0, 10))     # 0   (below minimum)
print(clamp(15, 0, 10))     # 10  (above maximum)

# Pattern 4: Safe division (avoid ZeroDivisionError)
def safe_divide(a, b, default=0):
    """Divide a by b, return default if b is zero."""
    return a / b if b != 0 else default

print(safe_divide(10, 2))       # 5.0
print(safe_divide(10, 0))       # 0    (default)
print(safe_divide(10, 0, -1))   # -1   (custom default)

# Pattern 5: Check if number is integer (no decimal part)
print(3.0 == int(3.0))          # True  - 3.0 is a whole number
print(3.5 == int(3.5))          # False - 3.5 has decimal part
print(float(10).is_integer())   # True
print(float(10.5).is_integer()) # False

# Pattern 6: Working with very large/small numbers
avogadro    = 6.022e23          # scientific notation
print(f"{avogadro:.3e}")        # 6.022e+23
print(f"{avogadro:,.0f}")       # 602,200,000,000,000,000,000,000

# Pattern 7: Number formatting
price = 1234567.891
print(f"{price:,.2f}")          # 1,234,567.89  (thousands separator)
print(f"{price:.2e}")           # 1.23e+06      (scientific)
print(f"{0.004:.2%}")           # 0.40%         (percentage)
print(f"{42:08d}")              # 00000042      (zero padded)
print(f"{42:+d}")               # +42           (always show sign)
print(f"{-42:+d}")              # -42

# Pattern 8: Integer check and conversion
x = 7 / 1                      # 7.0
if x == int(x):
    x = int(x)                  # convert to int if whole number
print(x, type(x))              # 7 <class 'int'>


# ------------------------------------------------------------
# PART 11: Common Pitfalls ⚠️
# ------------------------------------------------------------

# PITFALL 1: Division always returns float
result = 10 / 5
print(result)                   # 5.0  NOT 5!
print(type(result))             # float

# PITFALL 2: Floor division with negatives
print( 7 // 2)                  # 3
print(-7 // 2)                  # -4  not -3! floors toward -inf

# PITFALL 3: ** is right-associative
print(2 ** 3 ** 2)              # 512 = 2**(3**2), NOT (2**3)**2=64

# PITFALL 4: Unary minus and **
print(-2 ** 2)                  # -4  = -(2**2), NOT (-2)**2=4!
print((-2) ** 2)                # 4   use parentheses!

# PITFALL 5: /= always produces float
x = 10
x /= 2
print(x)                        # 5.0  not 5!
print(type(x))                  # float  ← changed type!

# PITFALL 6: Float precision with modulo
print(0.1 + 0.2)                # 0.30000000000000004
print((0.1 + 0.2) % 0.1)       # 0.09999999999999995  unexpected!
# Use round() or math.isclose() when precision matters

# PITFALL 7: math.pow() vs ** operator
print(type(2 ** 10))            # int   ← ** preserves int
print(type(math.pow(2, 10)))    # float ← math.pow always returns float

# PITFALL 8: math.floor returns int, // may return float
print(type(math.floor(3.9)))    # int
print(type(7.0 // 2))           # float ← // with float = float!

# PITFALL 9: Integer overflow does NOT exist in Python
# (unlike C/Java where int has a maximum value)
huge = 2 ** 10000
print(type(huge))               # int  ← Python handles it!
print(len(str(huge)))           # 3011 digits!


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ +  -  *          - basic arithmetic
# ✅ /               - ALWAYS returns float
# ✅ //              - floor division (toward -infinity!)
# ✅ %               - modulo (remainder, sign follows divisor)
# ✅ **              - exponentiation (right-to-left!)
# ✅ Precedence      - () > ** > unary > * / // % > + -
# ✅ +=  -=  *=      - augmented assignment
# ✅ /=  //=  %=  **= - augmented assignment
# ✅ math.floor()    - always rounds down (toward -inf)
# ✅ math.ceil()     - always rounds up
# ✅ math.trunc()    - rounds toward zero
# ✅ math.sqrt()     - square root (returns float)
# ✅ math.pow()      - power (always returns float)
# ✅ math.log()      - logarithm (natural, or any base)
# ✅ math.isclose()  - safe float comparison
# ✅ math.gcd()      - greatest common divisor
# ✅ math.factorial()- n!
# ⚠️  10/2 = 5.0     - division always float
# ⚠️  -7//2 = -4     - floor toward NEGATIVE infinity
# ⚠️  -2**2 = -4     - unary minus AFTER **
# ⚠️  2**3**2 = 512  - ** is RIGHT-to-left
# ⚠️  /= changes type to float always
# ⚠️  math.pow() always float, ** preserves int