# ============================================================
# MODULE 02 | LECTURE 26 - .format()
# ============================================================
# What you will learn:
#   - What .format() does and why it exists
#   - Basic positional placeholders {}
#   - Positional indexes {0}, {1}, {2}
#   - Named placeholders {name}, {age}
#   - Reusing placeholders
#   - Format specifications: width, alignment, precision
#   - Formatting numbers: integers, floats, percentages
#   - Formatting strings: alignment and padding
#   - .format() vs f-strings vs % formatting
#   - Real world use cases
#   - Common mistakes
# ============================================================


# ------------------------------------------------------------
# PART 1: What is .format() and why does it exist?
# ------------------------------------------------------------

# .format() is a string method for building strings
# that contain VARIABLE content.
#
# Instead of concatenating strings with +:
#   "Hello, " + name + "! You are " + str(age) + " years old."
#
# You write a TEMPLATE with PLACEHOLDERS:
#   "Hello, {}! You are {} years old.".format(name, age)
#
# The {} are called FORMAT FIELDS or PLACEHOLDERS.
# .format() fills them in with the provided values.

name = "Anna"
age = 25

# ❌ Old way - concatenation (ugly and error-prone):
result = "Hello, " + name + "! You are " + str(age) + " years old."
print(result)   # Hello, Anna! You are 25 years old.

# ✅ With .format() - clean template:
result = "Hello, {}! You are {} years old.".format(name, age)
print(result)   # Hello, Anna! You are 25 years old.

# ✅ Modern way - f-strings (Python 3.6+):
result = f"Hello, {name}! You are {age} years old."
print(result)   # Hello, Anna! You are 25 years old.

# Why learn .format() if f-strings exist?
#   1. .format() works in ALL Python versions (2.7+)
#   2. You will see it constantly in existing code
#   3. Templates can be stored separately from values
#   4. .format() has some features f-strings don't
#   5. Understanding .format() deepens your Python knowledge


# ------------------------------------------------------------
# PART 2: Basic positional placeholders {}
# ------------------------------------------------------------

# The simplest form: empty curly braces {}.
# Values are inserted in order, left to right.
#
# .format(value1, value2, value3, ...)
# {}         {}         {}
# ↑          ↑          ↑
# value1     value2     value3

# ── One placeholder ──
print("Hello, {}!".format("World"))         # Hello, World!
print("The answer is {}.".format(42))       # The answer is 42.
print("Pi is approximately {}.".format(3.14159))  # Pi is approximately 3.14159.

# ── Two placeholders ──
print("My name is {} and I am {} years old.".format("Anna", 25))
# My name is Anna and I am 25 years old.

print("{} + {} = {}".format(3, 4, 7))
# 3 + 4 = 7

# ── Multiple placeholders ──
print("{} {} {} {}".format("one", "two", "three", "four"))
# one two three four

# ── Values can be any type ──
print("String: {}, Int: {}, Float: {}, Bool: {}".format(
    "hello", 42, 3.14, True))
# String: hello, Int: 42, Float: 3.14, Bool: True

# ── .format() converts values to strings automatically ──
# No need for str()!
age = 25
gpa = 4.75
print("Age: {}, GPA: {}".format(age, gpa))   # Age: 25, GPA: 4.75
# Compare: "Age: " + str(age) + ", GPA: " + str(gpa)  ← much worse!


# ------------------------------------------------------------
# PART 3: Positional indexes {0}, {1}, {2}
# ------------------------------------------------------------

# You can specify the INDEX of the argument inside {}.
# This gives you control over ORDER and REUSE.
#
# {0} → first argument
# {1} → second argument
# {2} → third argument
# etc.

# ── Basic indexed placeholders ──
print("Hello, {0}! You are {1} years old.".format("Anna", 25))
# Hello, Anna! You are 25 years old.

# ── Change the order ~~
print("{1} is {0} years old.".format(25, "Anna"))
# Anna is 25 years old.
# ↑ {0}=25, {1}="Anna" but {1} comes FIRST in the template!

# ── Reuse the same argument ~~
print("{0} loves {0} and {0} is great!".format("Python"))
# Python loves Python and Python is great!
# ↑ {0} used THREE times, only ONE argument!

print("({0}, {1}) and ({1}, {0})".format("x", "y"))
# (x, y) and (y, x)

# ── Mix indexed and non-indexed? ~~
# You CANNOT mix {} and {0} in the same string!
# print("{} and {0}".format("a", "b"))  # ❌ ValueError!
# Use either ALL empty {} or ALL indexed {0}, {1}...

# ── Practical example: repeated value ~~
animal = "cat"
print("The {0} chased the {0}, but the {0} ran away.".format(animal))
# The cat chased the cat, but the cat ran away.

city = "Warsaw"
print("{0} is a city. I live in {0}. {0} is beautiful.".format(city))
# Warsaw is a city. I live in Warsaw. Warsaw is beautiful.


# ------------------------------------------------------------
# PART 4: Named placeholders {name}, {age}
# ------------------------------------------------------------

# Instead of position numbers, you can use NAMES.
# This makes templates much more readable!
#
# Syntax: {keyword} in the string
#         .format(keyword=value) in the call

# ── Basic named placeholders ~~
print("Hello, {name}! You are {age} years old.".format(
    name="Anna", age=25))
# Hello, Anna! You are 25 years old.

# ── Order doesn't matter with named placeholders ~~
print("{city} is in {country}.".format(country="Poland", city="Warsaw"))
# Warsaw is in Poland.
# ↑ country comes BEFORE city in .format() but AFTER in template - no problem!

# ── Reuse named placeholders ~~
print("{word} is a {word}!".format(word="palindrome"))
# palindrome is a palindrome!

# ── Mix named and positional (indexed) ~~
print("{0} and {name}".format("Anna", name="Jan"))
# Anna and Jan
# ↑ {0} = first positional arg, {name} = keyword arg

# ── Stored templates ~~
# This is where named placeholders really shine!
# You can store the TEMPLATE separately and fill it in later.

template = "Dear {first_name} {last_name},\nYour order {order_id} is ready."
result = template.format(
    first_name="Anna",
    last_name="Kowalska",
    order_id="ORD-2024-789"
)
print(result)
# Dear Anna Kowalska,
# Your order ORD-2024-789 is ready.

# ── Template reuse ~~
report_template = "Name: {name} | Score: {score} | Grade: {grade}"
print(report_template.format(name="Anna",  score=95, grade="A"))
print(report_template.format(name="Jan",   score=82, grade="B"))
print(report_template.format(name="Maria", score=78, grade="C"))


# ------------------------------------------------------------
# PART 5: Format specifications - the colon syntax
# ------------------------------------------------------------

# Inside the placeholder, after a COLON, you can specify
# HOW the value should be formatted.
#
# Syntax:
#   {[index_or_name]:[format_spec]}
#
# Format spec can control:
#   - Width (minimum number of characters)
#   - Alignment (< left, > right, ^ center)
#   - Fill character
#   - Sign (+ - space)
#   - Number format (d, f, e, %, x, o, b)
#   - Precision (decimal places)

# We will explore each of these in detail.


# ------------------------------------------------------------
# PART 6: Width - minimum number of characters
# ------------------------------------------------------------

# {:n} where n is an integer = minimum width.
# If the value is shorter, it's PADDED with spaces.
# If longer, no truncation - the value is printed as-is.

# ── Integer width ~~
print("{:10}".format("hello"))      # "hello     "  ← 5 chars + 5 spaces = 10
print("{:10}".format("hi"))         # "hi        "  ← 2 chars + 8 spaces = 10
print("{:10}".format("toolongstr")) # "toolongstr"  ← 10 chars, no padding
print("{:10}".format("waytoolong")) # "waytoolong"  ← still 10, no truncation
print("{:15}".format("waytoolong")) # "waytoolong     " ← 10 + 5 spaces = 15

# ── Width for numbers ~~
print("{:10}".format(42))           # "        42"  ← right-aligned by default!
print("{:10}".format(3.14))         # "      3.14"  ← right-aligned

# Note: strings default to LEFT alignment
#       numbers default to RIGHT alignment
# We can change this with alignment specifiers (Part 7).

# ── Practical: building a table ~~
print("{:15} {:5} {:10}".format("Name", "Age", "City"))
print("{:15} {:5} {:10}".format("Anna Kowalska", 25, "Warsaw"))
print("{:15} {:5} {:10}".format("Jan Nowak", 32, "Krakow"))
print("{:15} {:5} {:10}".format("Maria Schmidt", 28, "Berlin"))
# Name            Age   City
# Anna Kowalska    25   Warsaw
# Jan Nowak        32   Krakow
# Maria Schmidt    28   Berlin


# ------------------------------------------------------------
# PART 7: Alignment - < > ^ =
# ------------------------------------------------------------

# Alignment specifiers:
#   <  → LEFT alignment  (default for strings)
#   >  → RIGHT alignment (default for numbers)
#   ^  → CENTER alignment
#   =  → pad BETWEEN sign and digits (for numbers only)

# Syntax: {:alignment width}
# Example: {:<10} = left-align in 10 characters

# ── Left alignment ~~
print("{:<10}".format("hi"))        # "hi        "  ← left, padded right
print("{:<10}".format(42))          # "42        "  ← left (override number default!)

# ── Right alignment ~~
print("{:>10}".format("hi"))        # "        hi"  ← right, padded left
print("{:>10}".format(42))          # "        42"  ← right (already default for int)

# ── Center alignment ~~
print("{:^10}".format("hi"))        # "    hi    "  ← centered, 4 spaces each side
print("{:^10}".format("hello"))     # "  hello   "  ← centered, 2 left + 3 right
print("{:^10}".format(42))          # "    42    "  ← centered

# ── Comparing all three ~~
print("|{:<10}|".format("text"))    # |text      |  left
print("|{:>10}|".format("text"))    # |      text|  right
print("|{:^10}|".format("text"))    # |   text   |  center

# ── Practical: formatted table ~~
print("-" * 35)
print("|{:^10}|{:^10}|{:^10}|".format("Name", "Age", "City"))
print("-" * 35)
print("|{:<10}|{:^10}|{:<10}|".format("Anna", 25, "Warsaw"))
print("|{:<10}|{:^10}|{:<10}|".format("Jan", 32, "Krakow"))
print("-" * 35)


# ------------------------------------------------------------
# PART 8: Fill character
# ------------------------------------------------------------

# You can replace the default space padding with ANY character.
# Syntax: {:fill_char alignment width}
# The fill character comes BEFORE the alignment specifier.

# ── Fill with specific character ~~
print("{:*<10}".format("hi"))       # "hi********"  ← filled with *
print("{:*>10}".format("hi"))       # "********hi"  ← filled with *
print("{:*^10}".format("hi"))       # "****hi****"  ← filled with *

print("{:-<10}".format("hi"))       # "hi--------"
print("{:->10}".format("hi"))       # "--------hi"
print("{:-^10}".format("hi"))       # "----hi----"

print("{:0>5}".format(42))          # "00042"  ← zero-padded number!
print("{:0>8}".format(42))          # "00000042"

# ── Practical: decorative headers ~~
title = "Python Tutorial"
print("{:*^40}".format(" " + title + " "))
# *********** Python Tutorial ************

print("{:-^40}".format(" CHAPTER 1 "))
# --------------- CHAPTER 1 ---------------

# ── Progress bar style ~~
progress = 7
total = 10
filled = int(progress / total * 20)
empty = 20 - filled
bar = "[" + "█" * filled + "░" * empty + "]"
print("{} {:>3}%".format(bar, int(progress/total*100)))
# [██████████████░░░░░░]  70%


# ------------------------------------------------------------
# PART 9: Formatting integers
# ------------------------------------------------------------

# Format type specifiers for integers:
#   d  → decimal (normal integer) - this is the default
#   b  → binary
#   o  → octal
#   x  → hexadecimal (lowercase)
#   X  → hexadecimal (uppercase)
#   n  → locale-aware number formatting
#   ,  → thousands separator

# ── Basic integer formatting ~~
n = 255
print("{:d}".format(n))     # 255     ← decimal (default)
print("{:b}".format(n))     # 11111111 ← binary
print("{:o}".format(n))     # 377     ← octal
print("{:x}".format(n))     # ff      ← hex lowercase
print("{:X}".format(n))     # FF      ← hex uppercase

# ── With width ~~
print("{:10d}".format(42))  # "        42"  ← right-aligned integer
print("{:010d}".format(42)) # "0000000042"  ← zero-padded!

# ── Thousands separator ~~
n = 1000000
print("{:,}".format(n))         # 1,000,000   ← with commas
print("{:,}".format(9876543))   # 9,876,543

# ── Width with thousands separator ~~
print("{:15,}".format(1000000)) # "      1,000,000"

# ── Sign specifier ~~
print("{:+d}".format(42))   # +42  ← always show sign
print("{:+d}".format(-42))  # -42
print("{: d}".format(42))   # " 42" ← space for positive
print("{: d}".format(-42))  # "-42" ← minus for negative


# ------------------------------------------------------------
# PART 10: Formatting floats
# ------------------------------------------------------------

# Format type specifiers for floats:
#   f  → fixed-point notation
#   e  → scientific notation (lowercase e)
#   E  → scientific notation (uppercase E)
#   g  → general (chooses f or e based on magnitude)
#   %  → percentage (multiplies by 100, adds %)
#
# Precision: .n specifies decimal places

pi = 3.141592653589793

# ── Fixed-point notation ~~
print("{:f}".format(pi))        # 3.141593  ← default 6 decimal places
print("{:.2f}".format(pi))      # 3.14      ← 2 decimal places
print("{:.4f}".format(pi))      # 3.1416    ← 4 decimal places
print("{:.0f}".format(pi))      # 3         ← 0 decimal places (rounds!)
print("{:.10f}".format(pi))     # 3.1415926536  ← 10 decimal places

# ── Width + precision ~~
print("{:10.2f}".format(pi))    # "      3.14"  ← width 10, 2 decimals
print("{:10.4f}".format(pi))    # "    3.1416"  ← width 10, 4 decimals

# ── Practical: prices ~~
prices = [9.99, 149.5, 1299.0, 0.5]
for price in prices:
    print("{:>10.2f} USD".format(price))
# "      9.99 USD"
# "    149.50 USD"
# "   1299.00 USD"
# "      0.50 USD"

# ── Scientific notation ~~
big   = 12345678.9
small = 0.000001234

print("{:e}".format(big))       # 1.234568e+07
print("{:E}".format(big))       # 1.234568E+07
print("{:.2e}".format(big))     # 1.23e+07
print("{:e}".format(small))     # 1.234000e-06
print("{:.3e}".format(small))   # 1.234e-06

# ── Percentage ~~
ratio = 0.7543
print("{:%}".format(ratio))     # 75.430000%  ← multiplies by 100, adds %
print("{:.1%}".format(ratio))   # 75.4%       ← 1 decimal place
print("{:.0%}".format(ratio))   # 75%         ← no decimal places

# ── Thousands separator with floats ~~
big_float = 9876543.21
print("{:,.2f}".format(big_float))  # 9,876,543.21


# ------------------------------------------------------------
# PART 11: Formatting strings - alignment and truncation
# ------------------------------------------------------------

# For strings, you can:
#   - Set minimum width
#   - Set alignment (< > ^)
#   - Set maximum width (precision for strings - truncation!)
#   - Set fill character

# ── String truncation with precision ~~
# For strings, .n TRUNCATES to n characters (opposite of floats!)
text = "Hello World Python"

print("{:.5}".format(text))     # "Hello"       ← first 5 chars only!
print("{:.10}".format(text))    # "Hello Worl"  ← first 10 chars

# ── Width + truncation ~~
print("{:10.5}".format(text))   # "Hello     "  ← truncate to 5, pad to 10
print("{:>10.5}".format(text))  # "     Hello"  ← truncate to 5, right-align in 10
print("{:^10.5}".format(text))  # "  Hello   "  ← truncate to 5, center in 10

# ── Practical: fixed-width column with long text ~~
names = ["Anna Kowalska", "Jan Nowak", "Maria Schmidt-Kowalski"]
for name in names:
    print("|{:<20.15}|".format(name))  # max 15 chars, left in 20
# |Anna Kowalska      |
# |Jan Nowak          |
# |Maria Schmidt-Kow  |  ← truncated!


# ------------------------------------------------------------
# PART 12: Combining format specifications
# ------------------------------------------------------------

# Format spec order (must follow this order!):
# {:fill align width , .precision type}
#   fill   = any character (only with align)
#   align  = < > ^ =
#   width  = integer
#   ,      = thousands separator
#   .prec  = precision (decimal places or string truncation)
#   type   = d f e g % b o x X s

# Examples combining multiple specs:

# Width + alignment + fill:
print("{:*^20}".format("hello"))        # *******hello********

# Width + sign + precision + type (float):
print("{:+10.2f}".format(3.14))         # "     +3.14"
print("{:+10.2f}".format(-3.14))        # "     -3.14"

# Width + comma + precision:
print("{:15,.2f}".format(9876543.21))   # "  9,876,543.21"

# Zero-fill + width + precision:
print("{:015.2f}".format(3.14))         # "000000000003.14"

# Fill + align + width + precision + type:
print("{:0>10.2f}".format(3.14))        # "0000003.14"
print("{:*>10d}".format(42))            # "********42"
print("{:->10}".format("hi"))           # "--------hi"


# ------------------------------------------------------------
# PART 13: .format() vs f-strings vs % formatting
# ------------------------------------------------------------

# Python has three string formatting methods.
# Understanding all three helps you read any Python code.

name = "Anna"
age = 25
gpa = 4.75

# ── % formatting (old, Python 2 style) ~~
# Still works but considered outdated.
result = "Name: %s, Age: %d, GPA: %.2f" % (name, age, gpa)
print(result)   # Name: Anna, Age: 25, GPA: 4.75

# ── .format() (Python 2.7+ and 3.x) ~~
# Modern, powerful, works everywhere.
result = "Name: {}, Age: {}, GPA: {:.2f}".format(name, age, gpa)
print(result)   # Name: Anna, Age: 25, GPA: 4.75

# ── f-strings (Python 3.6+) ~~
# Most modern, most readable.
result = f"Name: {name}, Age: {age}, GPA: {gpa:.2f}"
print(result)   # Name: Anna, Age: 25, GPA: 4.75

# ── When to use each ~~
#
# f-strings  → use this in NEW code! Best for readability.
# .format()  → use when template is stored separately from values,
#              or when targeting older Python versions.
# %          → use only when maintaining OLD code.

# ── Key advantage of .format() over f-strings ~~
# Templates can be stored and reused:

# ✅ Template stored as variable (can't do this with f-strings easily):
template = "Dear {name},\nYour score is {score:.1f}%.\nGrade: {grade}"
# Use the template multiple times with different data:
print(template.format(name="Anna",  score=94.3, grade="A"))
print(template.format(name="Jan",   score=78.6, grade="C+"))
print(template.format(name="Maria", score=88.0, grade="B+"))

# ❌ With f-strings this doesn't work the same way:
# f"Dear {name}..." requires name to exist AT THAT MOMENT.


# ------------------------------------------------------------
# PART 14: Real world applications
# ------------------------------------------------------------

# ── Application 1: Generate formatted report ~~
print("=" * 50)
print("{:^50}".format("STUDENT REPORT"))
print("=" * 50)
print("{:<20} {:>10} {:>10} {:>8}".format("Name", "Score", "Max", "Grade"))
print("-" * 50)

students = [
    ("Anna Kowalska",  94, 100, "A"),
    ("Jan Nowak",      78, 100, "C+"),
    ("Maria Schmidt",  88, 100, "B+"),
    ("Piotr Wiśniewski", 62, 100, "D"),
]
for name, score, max_s, grade in students:
    print("{:<20} {:>10} {:>10} {:>8}".format(name, score, max_s, grade))
print("=" * 50)

# ── Application 2: Format scientific data ~~
molecules = [
    ("Glucose",   180.16, 6.0221e23, 0.3),
    ("Water",      18.02, 6.0221e23, 1.0),
    ("Ethanol",    46.07, 6.0221e23, 0.789),
]

print("{:<12} {:>10} {:>15} {:>10}".format(
    "Molecule", "Mol. Mass", "Avogadro", "Density"))
print("-" * 50)
for mol, mass, avo, dens in molecules:
    print("{:<12} {:>10.2f} {:>15.4e} {:>10.3f}".format(
        mol, mass, avo, dens))

# ── Application 3: Progress display ~~
def show_progress(current, total, width=30):
    pct = current / total
    filled = int(pct * width)
    bar = "█" * filled + "░" * (width - filled)
    print("\r[{}] {:>6.1%} ({}/{})".format(bar, pct, current, total), end="")

for i in range(11):
    show_progress(i, 10)
    import time
    time.sleep(0.1)
print()  # new line after progress bar

# ── Application 4: DNA sequence statistics ~~
dna = "ATGCCCGCATTAGTCGAAATGCCC"
a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")
total = len(dna)

print("{:^40}".format("DNA SEQUENCE ANALYSIS"))
print("-" * 40)
print("{:<5} {:>5} {:>10}".format("Base", "Count", "Frequency"))
print("-" * 40)
for base, count in [("A", a), ("T", t), ("G", g), ("C", c)]:
    print("{:<5} {:>5} {:>10.1%}".format(base, count, count/total))
print("-" * 40)
print("{:<5} {:>5} {:>10}".format("Total", total, "100.0%"))
print("GC Content: {:.1%}".format((g + c) / total))

# ── Application 5: Price formatting ~~
items = [
    ("Python Book",      29.99),
    ("DNA Kit",         149.99),
    ("Microscope",     2999.00),
    ("Lab notebook",     12.50),
]
total_price = sum(price for _, price in items)

print("{:^40}".format("SHOPPING CART"))
print("-" * 40)
for item, price in items:
    print("{:<25} {:>10,.2f} USD".format(item, price))
print("-" * 40)
print("{:<25} {:>10,.2f} USD".format("TOTAL", total_price))

# ── Application 6: Log message formatter ~~
log_template = "[{level:^8}] {timestamp} | {message}"

print(log_template.format(
    level="INFO",
    timestamp="2024-03-15 14:30:22",
    message="Server started successfully"
))
print(log_template.format(
    level="ERROR",
    timestamp="2024-03-15 14:31:05",
    message="Database connection failed"
))
print(log_template.format(
    level="WARNING",
    timestamp="2024-03-15 14:31:10",
    message="Memory usage above 80%"
))


# ------------------------------------------------------------
# PART 15: Common mistakes with .format()
# ------------------------------------------------------------

# ── Mistake 1: Wrong number of arguments ~~
# print("{} and {}".format("only_one"))
# ❌ IndexError: Replacement index 1 out of range

# ── Mistake 2: Mixing {} and {0} ~~
# print("{} and {0}".format("a", "b"))
# ❌ ValueError: cannot switch from automatic field numbering
#               to manual field specification

# ── Mistake 3: Wrong keyword name ~~
# print("{namo}".format(name="Anna"))
# ❌ KeyError: 'namo'  ← typo in placeholder name!

# ── Mistake 4: Not using the return value ~~
text = "Hello, {}!"
text.format("World")        # ← result thrown away!
print(text)                 # "Hello, {}!"  ← not formatted!

# ✅ Fix:
result = text.format("World")
print(result)               # "Hello, World!"

# ── Mistake 5: Forgetting the colon in format spec ~~
# print("{10}".format("hi"))    # ← {10} means "argument at index 10"!
# print("{:10}".format("hi"))   # ← {:10} means "width 10" ✅

# ── Mistake 6: Wrong order of format spec components ~~
# print("{:.2,f}".format(9876.5))   # ❌ wrong order!
print("{:,.2f}".format(9876.5))     # ✅ comma before precision: 9,876.50

# ── Mistake 7: Trying to truncate numbers with precision ~~
# For strings: {:.5} truncates to 5 characters
# For numbers: {:.5} means 5 DECIMAL PLACES
print("{:.5}".format("Hello World"))    # "Hello"    ← truncate string
print("{:.5f}".format(3.14))            # "3.14000"  ← 5 decimal places!

# ── Mistake 8: Forgetting that {} in .format() is special ~~
# If you want a literal { or } in the output, double them:
print("{}% done".format(75))           # 75% done  ← OK
print("{:.1f}% done".format(75.0))     # 75.0% done ← OK
print("{{literal braces}}".format())   # {literal braces}  ← escaped!
print("{{{0}}}".format("value"))        # {value}  ← escaped outer + {value}


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ .format() fills {} placeholders with values
# ✅ {} → positional (in order)
# ✅ {0}, {1} → indexed (specific position, reusable)
# ✅ {name} → named (keyword argument)
# ✅ Cannot mix {} and {0} in the same string
# ✅ Returns NEW string, original template unchanged
# ✅ Format spec after colon: {:spec}
#
# FORMAT SPEC COMPONENTS (in order):
# ✅ fill    → any character (only with alignment)
# ✅ align   → < left, > right, ^ center
# ✅ width   → minimum character width
# ✅ ,       → thousands separator
# ✅ .prec   → decimal places (float) or max chars (string)
# ✅ type    → d (int), f (float), e (sci), % (percent),
#              b (binary), x (hex), s (string)
#
# COMMON PATTERNS:
# ✅ {:10}    → width 10 (default alignment)
# ✅ {:<10}   → left-align in width 10
# ✅ {:>10}   → right-align in width 10
# ✅ {:^10}   → center in width 10
# ✅ {:*^10}  → center with * fill in width 10
# ✅ {:.2f}   → float with 2 decimal places
# ✅ {:,.2f}  → float with comma separator and 2 decimals
# ✅ {:.1%}   → percentage with 1 decimal place
# ✅ {:05d}   → zero-padded integer
# ✅ {{ }}    → literal curly braces in output