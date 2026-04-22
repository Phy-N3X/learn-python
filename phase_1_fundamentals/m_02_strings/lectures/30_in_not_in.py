# ============================================================
# MODULE 02 | LECTURE 30 - in / not in
# ============================================================
# What you will learn:
# - What the 'in' operator does
# - What the 'not in' operator does
# - How to search inside strings
# - Case sensitivity and how to handle it
# - Combining in / not in with logic
# - Common mistakes and edge cases
# - Practical real-world use cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is 'in'?
# ------------------------------------------------------------

# 'in' is a membership operator.
# It checks whether something EXISTS inside something else.
# It always returns True or False (a boolean value).

# Syntax:
#     something in container

# For strings specifically:
#     substring in string
# → checks if substring appears anywhere inside string

# Basic examples:

text = "Hello, Python!"

print("Python" in text)      # True  - "Python" is inside text
print("Java" in text)        # False - "Java" is NOT inside text
print("Hello" in text)       # True
print("hello" in text)       # False - lowercase! (case-sensitive)
print("!" in text)           # True  - single character works too
print("on" in text)          # True  - partial word works too

# Visual diagram:
#
# text = "Hello, Python!"
#          0123456789...
#
# "Python" in text
#  → Python scans the string left to right
#  → Looks for the exact sequence P-y-t-h-o-n
#  → Finds it starting at index 7
#  → Returns True
#
# "java" in text
#  → Scans the entire string
#  → Never finds j-a-v-a
#  → Returns False

# ------------------------------------------------------------
# PART 2: What is 'not in'?
# ------------------------------------------------------------

# 'not in' is the opposite of 'in'.
# It returns True if something does NOT exist inside.
# It returns False if it DOES exist.

# Syntax:
#     something not in container

text = "Welcome to Python"

print("Python" not in text)    # False - Python IS there
print("Java" not in text)      # True  - Java is NOT there
print("Welcome" not in text)   # False - Welcome IS there
print("welcome" not in text)   # True  - lowercase, not found!

# You could always write:
#     not ("Java" in text)
# But 'not in' is cleaner and more readable.
# Python style guide (PEP8) recommends using 'not in'.

# Compare:
text = "Hello"

# Less readable:
if not ("xyz" in text):
    print("not found")

# More readable (preferred):
if "xyz" not in text:
    print("not found")

# Both work identically - but the second is better Python style.

# ------------------------------------------------------------
# PART 3: in / not in are case-sensitive
# ------------------------------------------------------------

# This is one of the most common sources of confusion.
# Python treats uppercase and lowercase as DIFFERENT characters.

sentence = "The Quick Brown Fox"

print("Quick" in sentence)     # True  - exact match
print("quick" in sentence)     # False - different case!
print("QUICK" in sentence)     # False - different case!
print("Fox" in sentence)       # True
print("fox" in sentence)       # False
print("THE" in sentence)       # False - "The" not "THE"

# How to search in a case-insensitive way?
# Convert BOTH sides to the same case before checking.

# Option 1: convert everything to lowercase
print("quick" in sentence.lower())    # True  ✅
print("QUICK" in sentence.lower())    # True  ✅
print("FOX" in sentence.lower())      # True  ✅

# Option 2: convert everything to uppercase
print("QUICK" in sentence.upper())    # True  ✅
print("quick" in sentence.upper())    # False ❌ - must match the case you convert TO

# Best practice - always use .lower() on both sides:
search = "fox"
text = "The Quick Brown Fox"

if search.lower() in text.lower():
    print(f"Found '{search}' (case-insensitive)")
# Found 'fox' (case-insensitive)

# ------------------------------------------------------------
# PART 4: Searching for single characters
# ------------------------------------------------------------

# 'in' works perfectly for single characters too.
# This is useful for checking if a string contains
# specific letters, digits, or symbols.

word = "programming"

print("a" in word)     # True  - 'a' appears in "programming"
print("z" in word)     # False
print("g" in word)     # True  - appears twice, but result is still True
print("m" in word)     # True

# Checking for digits in a string:
code = "ABC123"
print("1" in code)     # True
print("9" in code)     # False

# Checking for spaces:
sentence = "hello world"
print(" " in sentence)       # True  - there is a space
print(" " in "helloworld")   # False - no space

# Checking for special characters:
email = "user@example.com"
print("@" in email)    # True  - valid email has @
print("." in email)    # True

password = "mypassword"
print("@" in password) # False

# ------------------------------------------------------------
# PART 5: Searching for substrings (multiple characters)
# ------------------------------------------------------------

# 'in' checks if the ENTIRE substring appears
# as a continuous sequence inside the string.
# The characters must be together and in the right order.

text = "bioinformatics"

print("bio" in text)        # True  - starts with "bio"
print("info" in text)       # True  - "bioinFORMatics" - wait, let's check:
print("form" in text)       # True  - "bioinFORMatics"
print("tics" in text)       # True  - ends with "tics"
print("bio" in text)        # True
print("boi" in text)        # False - letters exist but NOT in this order!

# "boi" vs "bio":
# text: b-i-o-i-n-f-o-r-m-a-t-i-c-s
# "bio" → b then i then o → found at position 0 ✅
# "boi" → b then o then i → NOT consecutive in text ❌

# Another example:
dna = "ATCGATCG"
print("ATC" in dna)    # True
print("GAT" in dna)    # True
print("ACT" in dna)    # False - A, C, T exist but not in this order continuously
print("ATCGATCG" in dna)  # True - the whole string matches itself

# ------------------------------------------------------------
# PART 6: in / not in with if statements
# ------------------------------------------------------------

# The most common use: decision making based on content.

# Basic if / else:
username = "admin_user"

if "admin" in username:
    print("Administrator detected")
else:
    print("Regular user")
# Administrator detected

# With not in:
message = "Hello, how are you?"

if "error" not in message:
    print("No errors found")
# No errors found

# Real-world example - checking user input:
answer = input("Do you want to continue? (yes/no): ")

if answer.lower() in "yes":
    print("Continuing...")
else:
    print("Stopping.")

# Better version - check against specific options:
valid_yes = ["yes", "y", "yeah", "yep"]
# (we will learn lists soon - for now just use 'in' with a string)

if answer.lower() in "yes":
    print("OK!")

# ------------------------------------------------------------
# PART 7: Combining in / not in with and, or, not
# ------------------------------------------------------------

# You can chain multiple membership checks with logical operators.

email = "user@gmail.com"

# Check if it looks like a valid email (basic check):
if "@" in email and "." in email:
    print("Looks like a valid email")
else:
    print("Invalid email format")
# Looks like a valid email

# Check multiple conditions:
text = "Python is great for data science"

if "Python" in text and "data" in text:
    print("This is about Python and data!")
# This is about Python and data!

if "Java" not in text and "C++" not in text:
    print("No other languages mentioned")
# No other languages mentioned

# Check if ANY of several words appear:
review = "This product is absolutely terrible and awful"
bad_words = "terrible"

if "terrible" in review or "awful" in review or "bad" in review:
    print("Negative review detected")
# Negative review detected

# More complex example:
password = "MyPass123!"

has_upper = any(c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for c in password)
has_digit = any(c in "0123456789" for c in password)
has_special = any(c in "!@#$%^&*()" for c in password)

# Don't worry about 'any' and 'for' yet - we'll cover them later.
# The key point: 'in' works inside these structures too.

# ------------------------------------------------------------
# PART 8: in with empty strings
# ------------------------------------------------------------

# Interesting edge case: empty string behavior.

text = "Hello"

print("" in text)      # True  ← surprising!
print("" in "")        # True
print("" in "abc")     # True

# Why? Because an empty string is technically
# found at every position in any string.
# It's a mathematical/programming convention.

# This is rarely useful in practice.
# Just be aware of it so it doesn't surprise you.

# Practical consequence:
word = ""
if word in "Hello":
    print("found")    # This will print! Even though word is empty.

# Better to check for empty string first:
word = ""
if word and word in "Hello":
    print("found")
else:
    print("word is empty or not found")
# word is empty or not found

# ------------------------------------------------------------
# PART 9: in / not in - checking the result
# ------------------------------------------------------------

# Remember: 'in' returns a boolean value.
# You can STORE the result in a variable.

text = "Python programming is fun"

contains_python = "Python" in text
contains_java = "Java" in text

print(contains_python)      # True
print(contains_java)        # False
print(type(contains_python)) # <class 'bool'>

# You can use stored booleans in conditions:
if contains_python:
    print("Python mentioned!")

if not contains_java:
    print("Java not mentioned.")

# This is useful when you need to check the same thing multiple times:
search_term = "error"
log = "System started. Connection established. No issues found."

found = search_term in log
print(f"Error found: {found}")    # Error found: False

if found:
    print("Alert! Check the log.")
else:
    print("System running normally.")
# System running normally.

# ------------------------------------------------------------
# PART 10: Practical use case - input validation
# ------------------------------------------------------------

# One of the most useful real-world applications.

# Example 1: Check if email contains @
email = input("Enter your email: ")

if "@" not in email:
    print("Error: email must contain @")
elif "." not in email:
    print("Error: email must contain a dot")
else:
    print("Email format looks OK")

# Example 2: Check if username contains forbidden characters
username = input("Choose a username: ")
forbidden = "!@#$%^&*() "

# Check character by character:
has_forbidden = False
for char in forbidden:
    if char in username:
        has_forbidden = True

if has_forbidden:
    print("Username contains forbidden characters!")
else:
    print("Username is valid.")

# Example 3: Menu choice validation
print("Options: start, stop, pause")
choice = input("Enter your choice: ")

if choice not in "startstoppause":    # simple but imperfect
    print("Invalid choice")

# Better approach (we'll learn lists soon):
# valid_choices = ["start", "stop", "pause"]
# if choice not in valid_choices:
#     print("Invalid choice")

# ------------------------------------------------------------
# PART 11: Practical use case - text analysis
# ------------------------------------------------------------

# Analyzing content of strings.

# Example 1: Count how many vowels a word contains
word = "programming"
vowels = "aeiou"
count = 0

for letter in word:
    if letter in vowels:
        count += 1

print(f"'{word}' contains {count} vowels")
# 'programming' contains 3 vowels

# Example 2: Check if a string is a palindrome (reads same backwards)
text = "racecar"
if text == text[::-1]:
    print(f"'{text}' is a palindrome")

# Example 3: Check DNA sequence validity
dna_sequence = "ATCGATCGTA"
valid_bases = "ATCG"
is_valid = True

for base in dna_sequence:
    if base not in valid_bases:
        is_valid = False

if is_valid:
    print("Valid DNA sequence")
else:
    print("Invalid DNA sequence - unknown base found")
# Valid DNA sequence

invalid_dna = "ATCXGATCG"
for base in invalid_dna:
    if base not in valid_bases:
        print(f"Invalid base found: '{base}'")
# Invalid base found: 'X'

# ------------------------------------------------------------
# PART 12: Practical use case - filtering and searching
# ------------------------------------------------------------

# Example 1: Simple keyword search in text
article = """
Python is a versatile programming language.
It is widely used in data science, web development,
and artificial intelligence. Many beginners choose
Python as their first language.
"""

keywords = ["data science", "artificial intelligence", "machine learning"]

for keyword in keywords:
    if keyword in article.lower():
        print(f"Found: '{keyword}'")
    else:
        print(f"Not found: '{keyword}'")

# Found: 'data science'
# Found: 'artificial intelligence'
# Not found: 'machine learning'

# Example 2: Check log messages for errors
logs = [
    "INFO: Server started",
    "INFO: Connection established",
    "ERROR: Database connection failed",
    "INFO: Retry attempt 1",
    "ERROR: Timeout exceeded",
]

for log in logs:
    if "ERROR" in log:
        print(f"⚠ {log}")
    else:
        print(f"✓ {log}")

# ✓ INFO: Server started
# ✓ INFO: Connection established
# ⚠ ERROR: Database connection failed
# ✓ INFO: Retry attempt 1
# ⚠ ERROR: Timeout exceeded

# ------------------------------------------------------------
# PART 13: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Forgetting case sensitivity

name = "Anna"
print("anna" in name)     # False! Not True!

# ✅ Fix:
print("anna" in name.lower())    # True

# ❌ MISTAKE 2: Confusing 'in' with == (equals)

color = "blue"
print(color in "blue")    # True - but this checks if "blue" is in "blue"
print(color == "blue")    # True - this checks if they are exactly equal

# The difference matters with longer strings:
text = "I like blue colors"
print(color in text)      # True  - "blue" found somewhere in text
print(color == text)      # False - "blue" is NOT equal to the whole text

# ❌ MISTAKE 3: Using 'in' to check if a variable exists

# x = 5
# print(x in something)  ← this checks membership, not existence!
# To check if a variable is defined, just try to use it.

# ❌ MISTAKE 4: Wrong order (what's inside what)

text = "Hello"
print("Hello" in text)    # True  ✅ - is "Hello" inside text?
print(text in "Hello")    # True  ✅ - is text inside "Hello"? (same here)

# But with different strings:
text = "Hello, World!"
print("Hello" in text)    # True  - "Hello" is PART of the longer text
print(text in "Hello")    # False - the long text is NOT inside short "Hello"

# Always think: "Is [LEFT] found inside [RIGHT]?"

# ❌ MISTAKE 5: Checking a number with in (on a string)

text = "I am 25 years old"
# print(25 in text)    # TypeError! 25 is int, text is str

# ✅ Fix: convert number to string first:
print("25" in text)    # True

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ "abc" in text       → True if "abc" found anywhere in text
# ✅ "abc" not in text   → True if "abc" NOT found in text
# ✅ Always returns bool  → True or False
# ✅ Case-sensitive       → "Hello" ≠ "hello"
# ✅ Fix case:           → use .lower() on both sides
# ✅ Works with:         → single chars, substrings, full strings
# ✅ "" in anything      → always True (empty string edge case)
# ✅ Combine with:       → and, or, not for complex checks
# ✅ Store result:       → found = "x" in text  (stores bool)

# Quick reference:
# ┌──────────────────────────────────────────────────┐
# │ "py" in "python"          →  True                │
# │ "PY" in "python"          →  False (case!)       │
# │ "PY" in "python".upper()  →  True                │
# │ "java" in "python"        →  False               │
# │ "java" not in "python"    →  True                │
# │ "@" in "user@email.com"   →  True                │
# │ "" in "anything"          →  True (edge case)    │
# │ "x" in ""                 →  False               │
# └──────────────────────────────────────────────────┘