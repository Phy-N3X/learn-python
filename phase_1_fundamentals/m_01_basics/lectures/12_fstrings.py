# ============================================================
# MODULE 01 | LECTURE 12 - F-Strings
# ============================================================
# What you will learn:
#   - What f-strings are and why use them
#   - Basic syntax
#   - Expressions inside f-strings
#   - Format specifiers (width, alignment, precision)
#   - Number formatting
#   - String formatting
#   - Date formatting
#   - Debugging with f-strings (= specifier)
#   - Nested f-strings
#   - Multiline f-strings
#   - Common pitfalls
# ============================================================


# ------------------------------------------------------------
# PART 1: What are F-Strings?
# ------------------------------------------------------------

# F-strings (formatted string literals) were introduced in Python 3.6
# They are the MODERN and RECOMMENDED way to format strings
# Prefix the string with f or F, then use {} for expressions

name = "Anna"
age  = 25

# Old ways (still work but avoid in new code):
print("Hello, " + name + "!")                       # concatenation
print("Hello, %s! You are %d." % (name, age))       # % formatting
print("Hello, {}! You are {}.".format(name, age))   # .format()

# Modern way - f-string:
print(f"Hello, {name}! You are {age}.")             # ← use this!

# F-strings are:
# ✅ Faster than .format() and %
# ✅ More readable
# ✅ Support any Python expression inside {}
# ✅ Support powerful format specifiers


# ------------------------------------------------------------
# PART 2: Basic Syntax
# ------------------------------------------------------------

# Syntax: f"text {expression} text"
# Anything inside {} is evaluated as Python code

name   = "Anna"
age    = 25
height = 1.75
city   = "Warsaw"

# Single variable:
print(f"Name: {name}")              # Name: Anna
print(f"Age: {age}")                # Age: 25
print(f"Height: {height}")          # Height: 1.75

# Multiple variables:
print(f"{name} is {age} years old and lives in {city}.")

# Single quotes inside f-string:
print(f'Name: {name}')             # works with single quotes too

# Triple quotes for multiline:
info = f"""
Name:   {name}
Age:    {age}
City:   {city}
"""
print(info)

# Curly braces in output - use double {{ }}:
print(f"Set notation: {{{1, 2, 3}}}")   # Set notation: {1, 2, 3}
print(f"{{}} is an empty dict")         # {} is an empty dict


# ------------------------------------------------------------
# PART 3: Expressions Inside F-Strings
# ------------------------------------------------------------

# ANY valid Python expression works inside {}

x = 10
y = 3

# Math:
print(f"Sum:       {x + y}")        # 13
print(f"Product:   {x * y}")        # 30
print(f"Division:  {x / y:.2f}")    # 3.33
print(f"Power:     {x ** y}")       # 1000

# String methods:
name = "anna kowalski"
print(f"Title:     {name.title()}")     # Anna Kowalski
print(f"Upper:     {name.upper()}")     # ANNA KOWALSKI
print(f"Length:    {len(name)}")        # 14

# Boolean expressions:
age = 20
print(f"Adult:     {age >= 18}")        # True
print(f"Teen:      {13 <= age <= 19}")  # False

# Ternary expressions:
score = 85
print(f"Grade:     {'Pass' if score >= 60 else 'Fail'}")    # Pass

temperature = 22
print(f"Weather:   {'Hot' if temperature > 30 else 'Cool' if temperature > 20 else 'Cold'}")

# Function calls:
import math
print(f"Pi:        {math.pi:.4f}")      # 3.1416
print(f"Sqrt(2):   {math.sqrt(2):.4f}")# 1.4142
print(f"Factorial: {math.factorial(5)}")# 120

# List/dict access:
colors = ["red", "green", "blue"]
person = {"name": "Bob", "age": 30}
print(f"Color:     {colors[1]}")        # green
print(f"Person:    {person['name']}")   # Bob ← use different quotes!


# ------------------------------------------------------------
# PART 4: Format Specifiers - Overview
# ------------------------------------------------------------

# Format specifier syntax:
# {value:[[fill]align][sign][#][0][width][grouping][.precision][type]}

# Components:
# fill      - character to fill with (default: space)
# align     - < left, > right, ^ center, = sign-aware
# sign      - + always, - only negative, space for positive
# #         - alternate form (0b, 0x, 0o prefix)
# 0         - zero-padding
# width     - minimum field width
# grouping  - , or _ for thousands separator
# .precision- decimal places for float, max chars for string
# type      - d int, f float, s string, e scientific, % percent, b binary...

# Simple example:
pi = 3.14159265
print(f"{pi}")              # 3.14159265    no format
print(f"{pi:.2f}")          # 3.14          2 decimal places
print(f"{pi:10.2f}")        # "      3.14"  width 10, 2 decimals
print(f"{pi:>10.2f}")       # "      3.14"  right-aligned (default for numbers)
print(f"{pi:<10.2f}")       # "3.14      "  left-aligned
print(f"{pi:^10.2f}")       # "   3.14   "  centered
print(f"{pi:0>10.2f}")      # "000003.14"   zero-filled... wait
print(f"{pi:010.2f}")       # "0000003.14"  zero-padded properly


# ------------------------------------------------------------
# PART 5: Number Formatting - Integers
# ------------------------------------------------------------

n = 42

# Basic integer types:
print(f"{n:d}")             # 42        decimal (default)
print(f"{n:b}")             # 101010    binary
print(f"{n:o}")             # 52        octal
print(f"{n:x}")             # 2a        hex lowercase
print(f"{n:X}")             # 2A        hex uppercase

# With prefix (#):
print(f"{n:#b}")            # 0b101010  binary with prefix
print(f"{n:#o}")            # 0o52      octal with prefix
print(f"{n:#x}")            # 0x2a      hex with prefix
print(f"{n:#X}")            # 0X2A      hex with prefix

# Width and alignment:
print(f"{n:5d}")            # "   42"   width 5, right-aligned (default)
print(f"{n:<5d}")           # "42   "   left-aligned
print(f"{n:^5d}")           # " 42  "   centered
print(f"{n:05d}")           # "00042"   zero-padded

# Sign:
positive = 42
negative = -42
print(f"{positive:+d}")     # +42       always show sign
print(f"{negative:+d}")     # -42
print(f"{positive: d}")     # " 42"     space for positive
print(f"{negative: d}")     # "-42"

# Thousands separator:
big = 1234567890
print(f"{big:,}")           # 1,234,567,890
print(f"{big:_}")           # 1_234_567_890  (underscore separator)
print(f"{big:,.0f}")        # 1,234,567,890  (as float with comma)


# ------------------------------------------------------------
# PART 6: Number Formatting - Floats
# ------------------------------------------------------------

pi    = 3.14159265358979
price = 9.99
ratio = 0.0042

# Fixed point (f):
print(f"{pi:f}")            # 3.141593      default 6 decimal places
print(f"{pi:.0f}")          # 3             no decimals
print(f"{pi:.2f}")          # 3.14          2 decimal places
print(f"{pi:.10f}")         # 3.1415926536  10 decimal places

# Scientific notation (e/E):
print(f"{pi:e}")            # 3.141593e+00
print(f"{pi:.2e}")          # 3.14e+00
print(f"{pi:E}")            # 3.141593E+00  uppercase E
print(f"{ratio:.2e}")       # 4.20e-03

# General (g) - switches between f and e:
print(f"{pi:g}")            # 3.14159       removes trailing zeros
print(f"{ratio:g}")         # 0.0042
print(f"{1234567.0:g}")     # 1.23457e+06   switches to scientific

# Percentage (%):
print(f"{0.5:%}")           # 50.000000%
print(f"{0.5:.1%}")         # 50.0%
print(f"{0.5:.0%}")         # 50%
print(f"{ratio:.2%}")       # 0.42%
print(f"{1.0:.0%}")         # 100%

# Width + precision:
print(f"{pi:10.2f}")        # "      3.14"
print(f"{pi:<10.2f}")       # "3.14      "
print(f"{pi:^10.2f}")       # "   3.14   "
print(f"{pi:010.2f}")       # "0000003.14"

# Thousands separator with floats:
amount = 1234567.89
print(f"{amount:,.2f}")     # 1,234,567.89
print(f"{amount:_.2f}")     # 1_234_567.89


# ------------------------------------------------------------
# PART 7: String Formatting
# ------------------------------------------------------------

word  = "Python"
short = "Hi"
long  = "Bioinformatics"

# Width and alignment:
print(f"{word:10}")         # "Python    "  left-aligned (default for str)
print(f"{word:<10}")        # "Python    "  explicit left
print(f"{word:>10}")        # "    Python"  right
print(f"{word:^10}")        # "  Python  "  centered

# Fill character:
print(f"{word:*<10}")       # "Python****"  fill with *
print(f"{word:*>10}")       # "****Python"
print(f"{word:*^10}")       # "**Python**"
print(f"{word:-^20}")       # "-------Python-------"
print(f"{word:=^20}")       # "=======Python======="

# Precision for strings (max characters):
print(f"{long:.5}")         # "Bioin"  truncate to 5 chars
print(f"{long:10.5}")       # "Bioin     "  width 10, max 5 chars
print(f"{long:>10.5}")      # "     Bioin"

# Building tables:
headers = ["Name", "Age", "City", "Score"]
rows = [
    ("Alice",   22, "Warsaw",  98.5),
    ("Bob",     30, "Krakow",  87.2),
    ("Charlie", 22, "Gdansk",  95.0),
]

# Header:
print(f"{'Name':<10} {'Age':>5} {'City':<10} {'Score':>7}")
print("-" * 35)
for name, age, city, score in rows:
    print(f"{name:<10} {age:>5} {city:<10} {score:>7.1f}")


# ------------------------------------------------------------
# PART 8: The = Specifier (Debug Format)
# ------------------------------------------------------------

# Python 3.8+ introduced the = specifier for debugging
# {variable=} prints: variable=value

x     = 42
name  = "Anna"
pi    = 3.14159
score = 85

# Basic debug format:
print(f"{x=}")              # x=42
print(f"{name=}")           # name='Anna'
print(f"{pi=}")             # pi=3.14159
print(f"{score=}")          # score=85

# With expressions:
print(f"{x + 10=}")         # x + 10=52
print(f"{x * pi=}")         # x * pi=131.94678...
print(f"{name.upper()=}")   # name.upper()='ANNA'
print(f"{score >= 60=}")    # score >= 60=True
print(f"{len(name)=}")      # len(name)=4

# With format specifiers (after =):
print(f"{pi=:.2f}")         # pi=3.14
print(f"{x=:05d}")          # x=00042
print(f"{score=:+d}")       # score=+85

# Extremely useful for debugging!
# Instead of: print("x =", x, "y =", y, "sum =", x+y)
# Write:       print(f"{x=} {y=} {x+y=}")
y = 10
print(f"{x=} {y=} {x+y=}")     # x=42 y=10 x+y=52


# ------------------------------------------------------------
# PART 9: Nested F-Strings
# ------------------------------------------------------------

# F-strings can be nested - useful for dynamic format strings

# Dynamic width:
width = 10
name  = "Python"
print(f"{name:{width}}")            # "Python    "  width from variable!
print(f"{name:^{width}}")           # "  Python  "

# Dynamic precision:
precision = 3
pi = 3.14159265
print(f"{pi:.{precision}f}")        # 3.142

# Both dynamic:
print(f"{pi:{width}.{precision}f}") # "     3.142"

# Dynamic fill character:
fill = "*"
print(f"{name:{fill}^{width}}")     # "**Python**"

# Practical: format table with variable column widths
col_widths = [10, 5, 12]
data = ("Alice", 25, "Warsaw")
print(f"{data[0]:<{col_widths[0]}} {data[1]:>{col_widths[1]}} {data[2]:^{col_widths[2]}}")

# Conditional format:
value     = -42
is_red    = value < 0
color_fmt = "- " if is_red else "+ "
print(f"{color_fmt}{abs(value)}")   # "- 42"


# ------------------------------------------------------------
# PART 10: Multiline F-Strings
# ------------------------------------------------------------

name    = "Anna"
age     = 25
score   = 92.5
city    = "Warsaw"
active  = True

# Triple-quoted multiline:
report = f"""
{'='*40}
STUDENT REPORT
{'='*40}
Name    : {name}
Age     : {age}
Score   : {score:.1f}%
City    : {city}
Active  : {active}
{'='*40}
"""
print(report)

# F-string across multiple lines (use backslash or parentheses):
message = (
    f"Dear {name},\n"
    f"Your score of {score:.1f} "
    f"{'exceeds' if score >= 90 else 'meets'} "
    f"our requirements.\n"
    f"Welcome to {city}!"
)
print(message)

# Building complex output:
items  = [("Widget", 9.99, 3), ("Gadget", 24.99, 1), ("Doohickey", 4.99, 5)]
total  = sum(price * qty for _, price, qty in items)

receipt = f"""
{'RECEIPT':^30}
{'-'*30}
{'Item':<15} {'Price':>7} {'Qty':>3} {'Total':>7}
{'-'*30}"""

for item, price, qty in items:
    receipt += f"\n{item:<15} {price:>7.2f} {qty:>3} {price*qty:>7.2f}"

receipt += f"""
{'-'*30}
{'TOTAL':>26} {total:>7.2f}
{'='*30}
"""
print(receipt)


# ------------------------------------------------------------
# PART 11: Formatting Dates and Special Types
# ------------------------------------------------------------

import datetime

now  = datetime.datetime(2025, 1, 15, 14, 30, 45)
date = datetime.date(2025, 1, 15)

# Date formatting with strftime codes:
print(f"{now:%Y-%m-%d}")            # 2025-01-15
print(f"{now:%d/%m/%Y}")            # 15/01/2025
print(f"{now:%B %d, %Y}")          # January 15, 2025
print(f"{now:%I:%M %p}")           # 02:30 PM
print(f"{now:%Y-%m-%d %H:%M:%S}")  # 2025-01-15 14:30:45
print(f"{now:%A, %B %d}")          # Wednesday, January 15

# Formatting other special types:
# Bytes:
data = b"hello"
print(f"{data}")                    # b'hello'

# None:
value = None
print(f"{value}")                   # None
print(f"{value!r}")                 # None (repr)
print(f"{str(value) or 'N/A'}")    # None - careful!
print(f"{'N/A' if value is None else value}")   # N/A ← correct


# ------------------------------------------------------------
# PART 12: Conversion Flags !r !s !a
# ------------------------------------------------------------

# Three conversion flags available in f-strings:
# !r  applies repr() - shows developer representation
# !s  applies str()  - shows string representation (default)
# !a  applies ascii() - escapes non-ASCII characters

text     = "hello\nworld"
name     = "Ząbek"           # Polish characters
number   = 3.14

# !s (default - same as no flag):
print(f"{text!s}")           # hello
                             # world
print(f"{text}")             # same

# !r (repr - useful for debugging):
print(f"{text!r}")           # 'hello\nworld'  ← shows \n literally
print(f"{name!r}")           # 'Ząbek'

# !a (ascii - escapes non-ASCII):
print(f"{name!a}")           # 'Z\u0105bek'  ← escapes Polish chars

# Practical use of !r for debugging:
messy_string = "  hello   \t world  \n"
print(f"String repr: {messy_string!r}")  # shows hidden characters!


# ------------------------------------------------------------
# PART 13: F-String Performance and Best Practices
# ------------------------------------------------------------

# Performance: f-strings are the FASTEST string formatting method
# Benchmark: f-strings > .format() > % formatting > concatenation

# Best practices:

# 1. Use f-strings for any string with variables:
name = "Anna"
# ❌ Avoid:
print("Hello " + name + "!")
# ✅ Use:
print(f"Hello {name}!")

# 2. Format numbers directly in f-string:
pi = 3.14159
# ❌ Avoid:
print("Pi is " + str(round(pi, 2)))
# ✅ Use:
print(f"Pi is {pi:.2f}")

# 3. Use = specifier for debugging (not print statements):
x = 42
# ❌ Avoid:
print("x =", x)
# ✅ Use:
print(f"{x=}")

# 4. Keep expressions simple - extract complex logic to variables:
scores = [85, 92, 78, 96]
# ❌ Avoid (hard to read):
print(f"Average: {sum(scores)/len(scores):.1f}")
# ✅ Prefer (clearer):
average = sum(scores) / len(scores)
print(f"Average: {average:.1f}")

# 5. Use different quotes to avoid escaping:
name = "Anna"
# ❌ Avoid:
print(f"Hello {name}, it\'s a nice day")
# ✅ Use (outer single, inner not needed):
print(f"Hello {name}, it's a nice day")

# 6. Break long f-strings across lines:
# ❌ Avoid (one very long line):
# print(f"Name: {name} Age: {age} City: {city} Score: {score}")
# ✅ Use parentheses:
message = (
    f"Name: {name} "
    f"Age: {age} "
)
print(message)


# ------------------------------------------------------------
# PART 14: Common Pitfalls ⚠️
# ------------------------------------------------------------

# PITFALL 1: Same quote inside f-string (Python < 3.12)
name = "Anna"
# print(f"Hello {"Anna"}")    # SyntaxError in Python < 3.12!
# Fix: use different quotes
print(f"Hello {'Anna'}")      # ← works
print(f'Hello {"Anna"}')      # ← works

# In Python 3.12+, same quotes ARE allowed:
# print(f"Hello {"Anna"}")    # ← works in 3.12+

# PITFALL 2: Backslash in f-string expression (Python < 3.12)
items = ["a", "b", "c"]
# print(f"Joined: {'\n'.join(items)}")  # SyntaxError in < 3.12!
# Fix: use variable
joined = "\n".join(items)
print(f"Joined:\n{joined}")

# PITFALL 3: Missing f prefix
name = "Anna"
print("Hello {name}")         # Hello {name}  ← forgot f!
print(f"Hello {name}")        # Hello Anna    ← correct

# PITFALL 4: Forgetting quotes around dict key
person = {"name": "Anna"}
# print(f"{person[name]}")    # NameError! 'name' not defined as variable
print(f"{person['name']}")    # Anna  ← correct

# PITFALL 5: Formatting None
value = None
# print(f"{value:.2f}")       # TypeError! can't format None as float
print(f"{value if value is not None else 0:.2f}")   # 0.00  ← safe

# PITFALL 6: Large numbers without separator
n = 1000000
print(f"{n}")                 # 1000000  ← hard to read
print(f"{n:,}")               # 1,000,000  ← much better!

# PITFALL 7: Width doesn't truncate by default
name = "Bioinformatics"
print(f"{name:5}")            # "Bioinformatics"  ← wider than 5!
print(f"{name:.5}")           # "Bioin"  ← truncate with precision


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ f"text {expr}"        basic f-string
# ✅ {expr:.2f}            2 decimal places
# ✅ {expr:10}             minimum width 10
# ✅ {expr:<10}            left align
# ✅ {expr:>10}            right align
# ✅ {expr:^10}            center align
# ✅ {expr:*^10}           center with * fill
# ✅ {expr:010}            zero-pad width 10
# ✅ {expr:,}              thousands separator
# ✅ {expr:.0%}            percentage no decimals
# ✅ {expr:e}              scientific notation
# ✅ {expr:b}              binary
# ✅ {expr:x}              hexadecimal
# ✅ {expr=}               debug: shows name=value
# ✅ {expr=:.2f}           debug with format
# ✅ {expr!r}              repr() conversion
# ✅ {expr!s}              str() conversion (default)
# ✅ {expr!a}              ascii() conversion
# ✅ f"{name:{width}}"     nested f-string (dynamic width)
# ✅ {date:%Y-%m-%d}       date formatting
# ⚠️  Missing f prefix     → no substitution!
# ⚠️  Same quotes inside   → use different quotes (or Python 3.12+)
# ⚠️  Backslash in expr    → use variable (or Python 3.12+)
# ⚠️  Dict key in f-string → use different quotes for key
# ⚠️  None formatting      → check for None first
# ⚠️  Width != truncation  → use .precision for string truncation