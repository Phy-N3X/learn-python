# ============================================================
# MODULE 01 | EXERCISES 11 - Type Conversion
# ============================================================
# 15 exercises - type conversion only
# Allowed from previous lectures:
#   - variables, type()                 (lecture 01)
#   - numbers, math operators           (lecture 02)
#   - string methods, slicing           (lecture 03)
#   - bool, truthy/falsy                (lecture 04)
#   - print(), f-strings                (lecture 05)
#   - input() patterns                  (lecture 06)
#   - comments and docstrings           (lecture 07)
#   - math operators                    (lecture 08)
#   - comparison operators              (lecture 09)
#   - logical operators                 (lecture 10)
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Implicit conversion investigation.
# Predict the result AND type for each expression.
# Write prediction as comment BEFORE running.
#
# True + 1
# True + 1.0
# False + 0
# False * 100
# True + True + True
# 1 + 2.0
# 3 * 1.0
# 10 / 2
# 10 // 2
# True + False + True + True
#
# After predictions, also print type() for each.
# Write a comment explaining the promotion chain:
# "bool → __ → __ → __"



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# int() conversion - predict then verify.
# Write prediction as comment BEFORE running.
# Mark ones that will FAIL with # FAILS: reason
#
# int(3.9)
# int(3.1)
# int(-3.9)
# int(-3.1)
# int("42")
# int("  42  ")
# int("-17")
# int("3.14")        ← will this work?
# int("hello")       ← will this work?
# int(True)
# int(False)
# int("0")
# int(float("3.99")) ← two-step conversion
# int("FF", 16)
# int("1010", 2)



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# float() conversion - predict then verify.
# Write prediction as comment BEFORE running.
# Mark ones that will FAIL with # FAILS: reason
#
# float(42)
# float("3.14")
# float("42")
# float("  3.14  ")
# float("-17.5")
# float("1e10")
# float("1.5e-3")
# float("inf")
# float("-inf")
# float("nan")
# float(True)
# float(False)
# float("hello")     ← will this work?
# float("")          ← will this work?
# float(None)        ← will this work?



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# str() conversion - predict then verify.
# str() almost NEVER fails. Predict the exact string output.
# Write prediction as comment BEFORE running.
#
# str(42)
# str(-17)
# str(3.14)
# str(True)
# str(False)
# str(None)
# str(0)
# str(0.0)
# str([1, 2, 3])
# str((1, 2, 3))
# str({"a": 1})
# str(3+4j)
# str(float("inf"))
# str(float("nan"))
# str("")



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# bool() conversion - predict then verify.
# This tests your understanding of truthy/falsy.
# Write prediction as comment BEFORE running.
#
# bool(0)
# bool(1)
# bool(-1)
# bool(0.0)
# bool(0.001)
# bool("")
# bool(" ")
# bool("0")
# bool("False")
# bool("false")
# bool([])
# bool([0])
# bool([False])
# bool({})
# bool(None)
# bool(False)
# bool(True)
#
# After running, write a comment listing values that
# surprised you and why.



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# type() vs isinstance() comparison.
#
# Given these values:
#   a = True
#   b = 42
#   c = 3.14
#   d = "hello"
#   e = None
#
# For each value, print results of:
#   1. type(value)
#   2. type(value) == bool  (and int, float, str, type(None))
#   3. isinstance(value, bool)
#   4. isinstance(value, int)
#   5. isinstance(value, (int, float))
#
# Format as a table:
#   Value    type()   ==bool  ==int  is_bool  is_int  is_num
#   -------- -------- ------- ------ -------- ------- ------
#   True     bool     True    False  True     True    True
#   ...
#
# Key question: why does isinstance(True, int) return True?
# Write the answer as a comment.



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Base conversion round-trip.
#
# Using bin(), hex(), oct() and int() with base parameter:
#
# For each number: 0, 1, 10, 42, 255, 1024
#   1. Print decimal value
#   2. Convert to binary string (use bin()[2:])
#   3. Convert to hex string (use hex()[2:].upper())
#   4. Convert to octal string (use oct()[2:])
#   5. Convert BACK from binary to int
#   6. Convert BACK from hex to int
#   7. Verify round-trip: original == int(binary, 2)
#
# Format output:
#   Dec:  42
#   Bin:  101010
#   Hex:  2A
#   Oct:  52
#   Round-trip: True
#   ---



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# The bool("False") pitfall - deep investigation.
#
# Part A: Show the pitfall clearly
#   1. raw = "False"
#      Print bool(raw) and explain why it's True
#
#   2. raw = "0"
#      Print bool(raw) and explain why it's True
#
#   3. raw = "no"
#      Print bool(raw) and explain why it's True
#
# Part B: Write a proper str_to_bool() function
# with full docstring that correctly handles:
#   "true", "True", "TRUE", "yes", "YES", "1", "y", "Y", "on"
#       → should return True
#   "false", "False", "FALSE", "no", "NO", "0", "n", "N", "off"
#       → should return False
#   anything else
#       → should raise ValueError with helpful message
#
# Test with ALL values listed above.
# Also test with: "maybe", "2", "", "  True  " (with spaces)



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# int() truncation vs round() - when it matters.
#
# Part A: Show the difference
# For each value, print int() AND round() result:
#   2.1, 2.4, 2.5, 2.6, 2.9
#   -2.1, -2.4, -2.5, -2.6, -2.9
#
# Format:
#   Value  | int()  | round()
#   -------|--------|--------
#   2.1    |  2     |  2
#   ...
#
# Part B: Real-world scenario
# You have prices in float. Two strategies to get integer price:
#   prices = [9.99, 14.49, 7.50, 22.99, 4.01]
#
# Strategy 1: int() - truncate (floor toward zero)
# Strategy 2: round() - round to nearest
# Strategy 3: math.ceil() - always round up
# Strategy 4: math.floor() - always round down
#
# For each price, show all 4 results.
# Which strategy is best for pricing? Write a comment.



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build safe conversion functions with full docstrings.
#
# Write these four functions:
#
#   safe_int(value, default=0)
#     - Try int(float(str(value).strip()))
#     - Return default on any error
#     - Test: "42", "3.14", "hello", None, "", "  25  ", True
#
#   safe_float(value, default=0.0)
#     - Try float(str(value).strip())
#     - Return default on any error
#     - Test: "3.14", "42", "hello", None, "", "1e5", "inf"
#
#   safe_str(value, default="")
#     - Try str(value)
#     - Return default if result is "None" (from None input)
#     - Test: 42, 3.14, True, None, "", [1,2,3]
#
#   safe_bool(value, default=False)
#     - Use the str_to_bool logic for strings
#     - For numbers: return value != 0
#     - For None: return default
#     - Test: True, False, 1, 0, "true", "false", "yes", "no",
#             "maybe", None, [], [1]
#
# For each function, print a test table showing
# input → output for all test cases.



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Type conversion pipeline.
# Each step converts the output of the previous step.
#
# Start: number = 255
#
# Step 1: int → binary string
# Step 2: binary string → back to int (using base 2)
# Step 3: int → hex string (uppercase, no "0x")
# Step 4: hex string → back to int (using base 16)
# Step 5: int → float
# Step 6: float → bool (True/False)
# Step 7: bool → str ("True" or "False")
# Step 8: str → back to bool using str_to_bool()
# Step 9: bool → int (1 or 0)
# Step 10: int → complex (real part only)
#
# Print after EACH step:
#   Step X: value (type)
#
# Expected:
#   Step 1: 11111111 (<class 'str'>)
#   Step 2: 255 (<class 'int'>)
#   ...
#
# Final: verify step 10's real part == 255.0



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Input processing pipeline.
# Simulate receiving raw data and converting it properly.
#
# raw_data = [
#     ("age",        "25"),
#     ("height",     "175.5"),
#     ("weight",     "70"),
#     ("is_active",  "True"),
#     ("score",      "92.5"),
#     ("level",      "3"),
#     ("username",   "anna"),
#     ("balance",    "1234.56"),
#     ("attempts",   "0"),
#     ("verified",   "yes"),
# ]
#
# Expected types:
# expected_types = {
#     "age": int, "height": float, "weight": float,
#     "is_active": bool, "score": float, "level": int,
#     "username": str, "balance": float,
#     "attempts": int, "verified": bool,
# }
#
# For each (key, raw_value) pair:
#   1. Convert to the expected type using safe converters
#   2. Verify the type is correct
#   3. Print: "age: '25' → 25 (int) ✓"
#
# Use your safe_int, safe_float, safe_bool from exercise 10.
# For bool: use str_to_bool logic.
# At the end print: "All conversions successful: True/False"



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Number system converter.
# Build a complete number base conversion tool.
#
# Write a function convert_base(number, from_base, to_base)
# with full docstring that:
#   1. Takes a number string in from_base
#   2. Converts to to_base
#   3. Returns result as string (uppercase for hex)
#
# Supported bases: 2, 8, 10, 16
#
# Hint:
#   Step 1: convert input to base-10 int using int(n, from_base)
#   Step 2: convert to target base using bin/oct/hex or str()
#
# Test cases:
#   "1010"  base 2  → base 10  = "10"
#   "FF"    base 16 → base 10  = "255"
#   "255"   base 10 → base 16  = "FF"
#   "255"   base 10 → base 2   = "11111111"
#   "77"    base 8  → base 2   = "111111"
#   "1010"  base 2  → base 16  = "A"
#
# Print a conversion table for numbers 0-16:
#   Dec | Bin      | Oct | Hex
#   ----|----------|-----|----
#   0   | 0        | 0   | 0
#   1   | 1        | 1   | 1
#   ...
#   16  | 10000    | 20  | 10



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Type conversion edge cases and precision.
#
# Part A: Float precision in conversions
#   1. Show that int(0.9999999999999999) != int(0.9)
#      Why? (float precision - some values round internally)
#   2. Show big int → float precision loss:
#      n = 9999999999999999
#      Print n, float(n), int(float(n))
#      Are they all equal? Why not?
#   3. Show that 0.1 + 0.2 converted:
#      str(0.1 + 0.2) vs f"{0.1+0.2:.1f}"
#      What's different?
#
# Part B: Complex number conversions
#   1. Create c = 5 + 0j
#      Try int(c) - what happens?
#      Show the correct way: int(c.real)
#   2. Create c = 3.7 + 0j
#      Get integer part correctly
#   3. Show: complex(3) == 3 + 0j (True/False and why)
#   4. Show: complex("3+4j") works
#      Show: complex("3 + 4j") fails (space not allowed)
#
# Part C: Chain conversion precision
#   Start with pi = 3.14159265358979
#   Show what happens through this chain:
#   float → str → float → int → float → bool → int
#   Print value and type at each step.
#   Where is precision lost?



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Build a complete type-safe data parser.
# This simulates reading mixed-type data from a file or API.
#
# raw_records = [
#     "Alice,25,165.5,True,92.5,Warsaw",
#     "Bob,30,180.0,False,85.0,Krakow",
#     "Charlie,,175.0,yes,78.5,Gdansk",     ← missing age!
#     "Diana,28,abc,True,95.0,Poznan",      ← invalid height!
#     "Edward,17,170.0,no,88.0,Wroclaw",
#     "Fiona,35,160.5,True,invalid,Lodz",   ← invalid score!
# ]
#
# Schema (field name, expected type, default):
# schema = [
#     ("name",       str,   "Unknown"),
#     ("age",        int,   0),
#     ("height",     float, 0.0),
#     ("is_active",  bool,  False),
#     ("score",      float, 0.0),
#     ("city",       str,   "Unknown"),
# ]
#
# For each record:
#   1. Split by comma
#   2. Convert each field to expected type using safe converters
#   3. Use default if conversion fails
#   4. Track which fields had conversion errors
#
# Print for each record:
#   Record 1: Alice
#   ├── name:      Alice (str) ✓
#   ├── age:       25 (int) ✓
#   ├── height:    165.5 (float) ✓
#   ├── is_active: True (bool) ✓
#   ├── score:     92.5 (float) ✓
#   └── city:      Warsaw (str) ✓
#   Status: OK
#
#   Record 3: Charlie
#   ├── name:      Charlie (str) ✓
#   ├── age:       0 (int) ✗ (used default - empty value)
#   ...
#   Status: 1 error(s)
#
# At the end print summary:
#   Total records:  6
#   Clean records:  X
#   Records with errors: X
#   Most common error field: X

