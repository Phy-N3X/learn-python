# ============================================================
# MODULE 03 | LECTURE 31 - if statement
# ============================================================
# What you will learn:
# - What a conditional statement is
# - How to write an if statement
# - What a boolean condition is
# - Comparison operators
# - Indentation rules
# - Multiple conditions with and / or / not
# - Nested conditions (preview)
# - Common mistakes and edge cases
# - Real-world use cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is a conditional statement?
# ------------------------------------------------------------

# So far, your programs ran line by line - always the same way.
# Every line executed, every time, in order.
# That's fine for simple scripts, but real programs need to DECIDE.
#
# A conditional statement lets your program ask a question:
# "Is this condition True?"
# If YES → do something
# If NO  → skip it (or do something else)
#
# This is the foundation of ALL programming logic.
# Without conditions, programs cannot make decisions.
#
# Real life analogy:
# ┌─────────────────────────────────────────────┐
# │ IF it is raining                            │
# │     take an umbrella                        │
# │                                             │
# │ IF your score is above 90                   │
# │     you get an A                            │
# │                                             │
# │ IF the user typed the correct password      │
# │     let them in                             │
# └─────────────────────────────────────────────┘
#
# Python uses the same logic - just with code syntax.

# ------------------------------------------------------------
# PART 2: Basic if syntax
# ------------------------------------------------------------

# Syntax:
#     if condition:
#         code to run if condition is True
#
# Rules:
# 1. Start with the keyword 'if'
# 2. Write a condition (something that evaluates to True/False)
# 3. End the line with a colon ':'
# 4. Indent the next line(s) with 4 spaces (or 1 tab)
# 5. Only indented lines belong to the if block

# Simplest possible example:

x = 10

if x > 5:
    print("x is greater than 5")

# Output: x is greater than 5

# What happens step by step:
# 1. Python evaluates: x > 5  →  10 > 5  →  True
# 2. Condition is True → execute the indented block
# 3. Prints: "x is greater than 5"

# Now with False condition:

y = 3

if y > 5:
    print("y is greater than 5")

print("This always runs")

# Output: This always runs
# (the if block is skipped because 3 > 5 is False)

# Visual flow diagram:
#
#   condition
#   (True/False)
#       │
#    ┌──▼──┐
#    │ True│──── YES ──→ run indented block
#    └──┬──┘                    │
#       │ NO                    │
#       ▼                       ▼
#   skip block ◄───────────────┘
#       │
#       ▼
#   continue program

# ------------------------------------------------------------
# PART 3: The condition - what can go inside if?
# ------------------------------------------------------------

# The condition is ANY expression that evaluates to True or False.
# Python is very flexible about what counts as True or False.

# OPTION 1: Comparison expression (most common)

age = 20
if age >= 18:
    print("Adult")               # Adult

temperature = -5
if temperature < 0:
    print("Below freezing")      # Below freezing

name = "Anna"
if name == "Anna":
    print("Hello Anna!")         # Hello Anna!

# OPTION 2: A boolean variable directly

is_logged_in = True
if is_logged_in:
    print("Welcome back!")       # Welcome back!

is_raining = False
if is_raining:
    print("Take umbrella")       # (nothing - False)

# OPTION 3: Result of a function call

text = "Hello"
if text.startswith("H"):
    print("Starts with H")       # Starts with H

numbers = [1, 2, 3]
if len(numbers) > 0:
    print("List is not empty")   # List is not empty

# OPTION 4: 'in' / 'not in' (from Module 02)

email = "user@gmail.com"
if "@" in email:
    print("Valid email format")  # Valid email format

# OPTION 5: Literal True / False (rarely useful, but valid)

if True:
    print("This always runs")    # This always runs

if False:
    print("This never runs")     # (never executes)

# ------------------------------------------------------------
# PART 4: Comparison operators
# ------------------------------------------------------------

# These are the operators you use to build conditions.
# Each one compares two values and returns True or False.

# ┌──────────┬─────────────────────┬─────────────────────────┐
# │ Operator │ Meaning             │ Example                 │
# ├──────────┼─────────────────────┼─────────────────────────┤
# │ ==       │ equal to            │ x == 5  → True if x=5   │
# │ !=       │ not equal to        │ x != 5  → True if x≠5   │
# │ >        │ greater than        │ x > 5   → True if x>5   │
# │ <        │ less than           │ x < 5   → True if x<5   │
# │ >=       │ greater or equal    │ x >= 5  → True if x≥5   │
# │ <=       │ less or equal       │ x <= 5  → True if x≤5   │
# └──────────┴─────────────────────┴─────────────────────────┘

x = 7

print(x == 7)    # True  - x equals 7
print(x == 5)    # False - x does not equal 5
print(x != 5)    # True  - x is not equal to 5
print(x > 5)     # True  - 7 is greater than 5
print(x > 10)    # False - 7 is not greater than 10
print(x < 10)    # True  - 7 is less than 10
print(x >= 7)    # True  - 7 is greater than or equal to 7
print(x <= 6)    # False - 7 is not less than or equal to 6

# ⚠ IMPORTANT: == vs =
# = is ASSIGNMENT    →  x = 5   (stores 5 in x)
# == is COMPARISON   →  x == 5  (asks: is x equal to 5?)

# This is one of the most common beginner mistakes!

score = 95
if score == 100:
    print("Perfect score!")      # (not printed - 95 ≠ 100)

if score >= 90:
    print("Excellent!")          # Excellent!

# Comparing strings:
language = "Python"
if language == "Python":
    print("Great choice!")       # Great choice!

if language == "python":         # case-sensitive!
    print("Lowercase")           # (not printed)

# Comparing with variables:
a = 10
b = 20
if a < b:
    print(f"{a} is less than {b}")    # 10 is less than 20

# ------------------------------------------------------------
# PART 5: Indentation - the most important rule in Python
# ------------------------------------------------------------

# Python uses INDENTATION to define code blocks.
# This is NOT optional - it is part of the language syntax.
# Other languages use {} curly braces. Python uses spaces.

# Standard: 4 spaces per level (or 1 tab, but spaces preferred)

# ✅ CORRECT indentation:

temperature = 35
if temperature > 30:
    print("It's hot outside")      # 4 spaces - inside if block
    print("Stay hydrated")         # 4 spaces - also inside if block
print("Weather check done")        # 0 spaces - outside if block

# Output:
# It's hot outside
# Stay hydrated
# Weather check done

# ✅ CORRECT - multiple lines in one if block:

score = 85
if score >= 80:
    print("Good job!")
    print("You passed the exam")
    print("Keep it up!")
print("End of report")

# Output:
# Good job!
# You passed the exam
# Keep it up!
# End of report

# ❌ WRONG - missing indentation:

# if temperature > 30:
# print("Hot")          ← IndentationError!

# ❌ WRONG - inconsistent indentation:

# if temperature > 30:
#     print("Hot")      ← 4 spaces
#   print("Drink")      ← 2 spaces - IndentationError!

# ❌ WRONG - indenting something that shouldn't be indented:

# score = 85
#     if score > 80:    ← unexpected indent!
#         print("Good")

# Visual structure - think of it as blocks:
#
# ──────────────────────────
# MAIN CODE (no indent)
# ──────────────────────────
# if condition:
#     ────────────────────
#     IF BLOCK (4 spaces)
#     ────────────────────
# ──────────────────────────
# MAIN CODE continues
# ──────────────────────────

# ------------------------------------------------------------
# PART 6: Truthy and Falsy values
# ------------------------------------------------------------

# In Python, not just True/False can be used as conditions.
# Every value has a "truthiness" - it behaves as True or False.

# FALSY values (treated as False in conditions):
# ┌──────────────┬──────────────────────────────┐
# │ Value        │ Why it's falsy               │
# ├──────────────┼──────────────────────────────┤
# │ False        │ explicitly False             │
# │ 0            │ zero integer                 │
# │ 0.0          │ zero float                   │
# │ ""           │ empty string                 │
# │ []           │ empty list                   │
# │ None         │ no value                     │
# └──────────────┴──────────────────────────────┘

# TRUTHY values (treated as True in conditions):
# - True
# - Any non-zero number (1, -1, 0.1, 100...)
# - Any non-empty string ("a", "hello", " "...)
# - Any non-empty list, dict, etc.

# Examples:

name = ""
if name:
    print("Name is set")
else:
    print("Name is empty")       # This runs - empty string is falsy

name = "Anna"
if name:
    print("Name is set")         # This runs - non-empty string is truthy

count = 0
if count:
    print("Has items")           # (skipped - 0 is falsy)

count = 5
if count:
    print("Has items")           # Has items

result = None
if result:
    print("Has result")          # (skipped - None is falsy)

result = 42
if result:
    print("Has result")          # Has result

# This is very useful for checking "is this empty/missing?"
# Instead of:  if name != "" and name is not None:
# You can write: if name:

# ------------------------------------------------------------
# PART 7: Combining conditions - and, or, not
# ------------------------------------------------------------

# You can combine multiple conditions in one if statement.

# AND - both conditions must be True
# OR  - at least one condition must be True
# NOT - reverses True to False and False to True

# AND operator:
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Entry allowed")       # Entry allowed

# Both must be True:
# age >= 18 → True
# has_ticket → True
# True AND True → True → block executes

age = 15
if age >= 18 and has_ticket:
    print("Entry allowed")       # (skipped - 15 >= 18 is False)

# OR operator:
is_member = False
has_coupon = True

if is_member or has_coupon:
    print("Discount applied")    # Discount applied

# At least one is True:
# is_member → False
# has_coupon → True
# False OR True → True → block executes

# NOT operator:
is_banned = False

if not is_banned:
    print("User can post")       # User can post

is_banned = True
if not is_banned:
    print("User can post")       # (skipped - not True = False)

# Combining all three:
age = 22
is_vip = False
has_id = True

if (age >= 18 and has_id) and (is_vip or age >= 21):
    print("Full access granted")     # Full access granted

# Truth table reminder:
# ┌───────┬───────┬─────────┬────────┬──────────┐
# │   A   │   B   │ A and B │ A or B │  not A   │
# ├───────┼───────┼─────────┼────────┼──────────┤
# │ True  │ True  │  True   │  True  │  False   │
# │ True  │ False │  False  │  True  │  False   │
# │ False │ True  │  False  │  True  │  True    │
# │ False │ False │  False  │  False │  True    │
# └───────┴───────┴─────────┴────────┴──────────┘

# ------------------------------------------------------------
# PART 8: Chained comparisons
# ------------------------------------------------------------

# Python allows a very elegant syntax for range checks.
# Instead of: x >= 0 and x <= 100
# You can write: 0 <= x <= 100

grade = 85

# Standard way (works fine):
if grade >= 0 and grade <= 100:
    print("Valid grade")

# Pythonic way (much cleaner!):
if 0 <= grade <= 100:
    print("Valid grade")         # Valid grade

# More examples:
temperature = 22
if 18 <= temperature <= 26:
    print("Comfortable temperature")    # Comfortable temperature

age = 25
if 18 <= age <= 65:
    print("Working age")               # Working age

pH = 7.4
if 7.35 <= pH <= 7.45:
    print("Normal blood pH")           # Normal blood pH

# You can chain more than two comparisons:
x = 5
if 1 < x < 10 < 100:
    print("All conditions met")        # All conditions met

# ------------------------------------------------------------
# PART 9: if with 'in' and 'not in'
# ------------------------------------------------------------

# We covered 'in' and 'not in' in Module 02.
# They work perfectly inside if conditions.

# Checking membership in a string:
dna = "ATCGATCG"
if "ATG" in dna:
    print("Start codon found")         # Start codon found

# Checking if character is a vowel:
letter = "e"
if letter in "aeiou":
    print(f"'{letter}' is a vowel")    # 'e' is a vowel

# Checking if something is NOT present:
username = "john_doe"
if " " not in username:
    print("Username is valid")         # Username is valid

# Combining in with and:
email = "user@gmail.com"
if "@" in email and "." in email:
    print("Email format OK")           # Email format OK

# ------------------------------------------------------------
# PART 10: if with functions and methods
# ------------------------------------------------------------

# You can use any function/method call as a condition
# as long as it returns something truthy or falsy.

# String methods:
word = "Python"
if word.isupper():
    print("All uppercase")             # (skipped)

if word.startswith("Py"):
    print("Starts with Py")            # Starts with Py

if word.endswith("on"):
    print("Ends with on")              # Ends with on

# Using len():
name = "Anna"
if len(name) >= 3:
    print("Name is long enough")       # Name is long enough

text = ""
if len(text) == 0:
    print("Text is empty")             # Text is empty

# Using input():
answer = input("Enter 'yes' to continue: ")
if answer.lower() == "yes":
    print("Continuing...")

# Using type():
value = 42
if type(value) == int:
    print("It's an integer")           # It's an integer

# Better way to check type - using isinstance():
if isinstance(value, int):
    print("It's an integer")           # It's an integer

if isinstance(value, (int, float)):
    print("It's a number")             # It's a number

# ------------------------------------------------------------
# PART 11: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Using = instead of ==

x = 10
# if x = 10:           ← SyntaxError!
#     print("ten")

# ✅ Fix:
if x == 10:
    print("ten")                       # ten

# ❌ MISTAKE 2: Forgetting the colon

# if x > 5           ← SyntaxError! Missing :
#     print("yes")

# ✅ Fix:
if x > 5:
    print("yes")                       # yes

# ❌ MISTAKE 3: Wrong indentation

# if x > 5:
# print("yes")        ← IndentationError!

# ✅ Fix:
if x > 5:
    print("yes")                       # yes

# ❌ MISTAKE 4: Comparing with wrong type

age = "25"           # string, not int!
# if age >= 18:      ← TypeError! Can't compare str and int

# ✅ Fix: convert first
if int(age) >= 18:
    print("Adult")                     # Adult

# ❌ MISTAKE 5: Confusing 'and' with 'or'

# "User must be over 18 AND have a ticket"
# Beginner mistake: using 'or' when 'and' is needed

age = 20
has_ticket = False

if age >= 18 or has_ticket:    # ← wrong! This lets in adults without tickets
    print("Entry allowed")

if age >= 18 and has_ticket:   # ← correct! Both required
    print("Entry allowed")     # (skipped - no ticket)

# ❌ MISTAKE 6: Checking float equality with ==

result = 0.1 + 0.2
print(result)                  # 0.30000000000000004 (floating point issue!)

if result == 0.3:
    print("Equal")             # (skipped! Not exactly 0.3)

# ✅ Fix: use a small tolerance
if abs(result - 0.3) < 0.0001:
    print("Equal enough")      # Equal enough

# ❌ MISTAKE 7: Unnecessary comparison with True/False

is_valid = True
if is_valid == True:           # works, but redundant
    print("Valid")

# ✅ Better:
if is_valid:                   # cleaner and more Pythonic
    print("Valid")

# ❌ MISTAKE 8: Empty if block (causes SyntaxError)

# if x > 5:                   ← SyntaxError - block cannot be empty
#
# ✅ Fix: use 'pass' as a placeholder

if x > 5:
    pass                       # does nothing, but syntactically correct

# ------------------------------------------------------------
# PART 12: Real-world use cases
# ------------------------------------------------------------

# Use case 1: Login system
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "secret123":
    print("Login successful! Welcome, admin.")

# Use case 2: Age verification
age = int(input("Enter your age: "))
if age >= 18:
    print("Access granted. Welcome!")

# Use case 3: Grade evaluation
score = float(input("Enter your score (0-100): "))
if score >= 90:
    print("Grade: A - Excellent!")

# Use case 4: DNA sequence validation
sequence = input("Enter DNA sequence: ").upper()
valid_bases = "ATCG"
is_valid = True
for base in sequence:
    if base not in valid_bases:
        is_valid = False
if is_valid:
    print("Valid DNA sequence")

# Use case 5: Temperature alert
temp = float(input("Enter body temperature (°C): "))
if temp >= 38.0:
    print("⚠ Fever detected! Consult a doctor.")

# Use case 6: Number classification
number = int(input("Enter a number: "))
if number > 0:
    print("Positive number")
if number % 2 == 0:
    print("Even number")
if number > 0 and number % 2 == 0:
    print("Positive AND even")

# ------------------------------------------------------------
# PART 13: pass statement
# ------------------------------------------------------------

# Sometimes you want to write an if statement
# but haven't decided what to put inside yet.
# Python requires at least one line in every block.
# 'pass' is a placeholder that does nothing.

x = 10
if x > 5:
    pass    # TODO: add logic here later

# This is useful during development.
# It lets you write the structure first,
# fill in the logic later.
# Without 'pass', Python would raise a SyntaxError.

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ if condition:          → basic syntax
# ✅ condition is True      → block executes
# ✅ condition is False     → block is skipped
# ✅ Colon : is required    → don't forget it!
# ✅ 4 spaces indentation   → all lines in block must be indented
# ✅ == for comparison      → not = (that's assignment)
# ✅ and / or / not         → combine multiple conditions
# ✅ 0 <= x <= 100          → chained comparison (Pythonic)
# ✅ Truthy / Falsy         → any value can be used as condition
# ✅ pass                   → empty block placeholder

# Quick reference:
# ┌─────────────────────────────────────────────────────┐
# │ if x > 0:               → positive check            │
# │ if x == "yes":          → equality check            │
# │ if x != 0:              → not equal check           │
# │ if 0 <= x <= 100:       → range check               │
# │ if x and y:             → both truthy               │
# │ if x or y:              → at least one truthy       │
# │ if not x:               → x is falsy                │
# │ if "a" in text:         → membership check          │
# │ if len(text) > 0:       → non-empty check           │
# │ if isinstance(x, int):  → type check                │
# └─────────────────────────────────────────────────────┘