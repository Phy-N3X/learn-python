# ============================================================
# MODULE 02 | LECTURE 18 - .upper() and .lower()
# ============================================================
# What you will learn:
#   - What string methods are and how they differ from functions
#   - What .upper() does and how to use it
#   - What .lower() does and how to use it
#   - What .isupper() and .islower() do
#   - What .capitalize() and .title() do (bonus methods)
#   - What .swapcase() does (bonus method)
#   - How these methods handle non-letter characters
#   - Why strings are immutable and what that means for methods
#   - Method chaining
#   - Real world use cases
#   - Common mistakes
# ============================================================


# ------------------------------------------------------------
# PART 1: What is a string METHOD?
# ------------------------------------------------------------

# So far we have used FUNCTIONS like:
#   print()   → standalone function
#   len()     → standalone function
#   type()    → standalone function
#   input()   → standalone function

# A METHOD is different.
# A method is a function that BELONGS TO an object.
# It is called using DOT NOTATION:
#
#   object.method()
#   ↑      ↑
#   string the action it performs

# For strings, the syntax is:
#   string.method()
#
# The string comes FIRST, then a dot, then the method name.

word = "python"
result = word.upper()
print(result)       # PYTHON

# Compare:
# len(word)     ← function: word goes INSIDE the parentheses
# word.upper()  ← method:   word comes BEFORE the dot

# Why does Python have both functions and methods?
# Functions are general tools (work on many types).
# Methods are specialized tools (belong to a specific type).
# len() works on strings, lists, tuples, dicts...
# .upper() only makes sense for strings.


# ------------------------------------------------------------
# PART 2: .upper() - convert to UPPERCASE
# ------------------------------------------------------------

# .upper() returns a NEW string where ALL letters
# are converted to their UPPERCASE version.

word = "python"
print(word.upper())     # PYTHON

word = "Hello World"
print(word.upper())     # HELLO WORLD

word = "my name is anna"
print(word.upper())     # MY NAME IS ANNA

# .upper() does NOT modify the original string!
# Remember: strings are IMMUTABLE.
# It always returns a NEW string.

original = "python"
uppercased = original.upper()

print(original)         # python    ← unchanged!
print(uppercased)       # PYTHON    ← new string

# You can also call it directly without storing:
print("hello".upper())  # HELLO

# Or call it on a variable directly in print:
name = "anna"
print(name.upper())     # ANNA
print(name)             # anna  ← still unchanged!

# To "permanently" change a variable, reassign it:
name = name.upper()
print(name)             # ANNA  ← now it's updated


# ------------------------------------------------------------
# PART 3: .lower() - convert to LOWERCASE
# ------------------------------------------------------------

# .lower() returns a NEW string where ALL letters
# are converted to their LOWERCASE version.

word = "PYTHON"
print(word.lower())     # python

word = "Hello World"
print(word.lower())     # hello world

word = "MY NAME IS ANNA"
print(word.lower())     # my name is anna

# Just like .upper(), it does NOT modify the original:
original = "PYTHON"
lowercased = original.lower()

print(original)         # PYTHON    ← unchanged!
print(lowercased)       # python    ← new string

# Works on mixed case too:
mixed = "PyThOn"
print(mixed.lower())    # python
print(mixed.upper())    # PYTHON


# ------------------------------------------------------------
# PART 4: How methods handle non-letter characters
# ------------------------------------------------------------

# .upper() and .lower() ONLY affect letters (a-z, A-Z).
# All other characters are left EXACTLY as they are:
#   - digits (0-9)     → unchanged
#   - spaces           → unchanged
#   - punctuation      → unchanged
#   - symbols          → unchanged

# Examples:
print("hello123".upper())       # HELLO123   ← digits unchanged
print("HELLO123".lower())       # hello123   ← digits unchanged

print("hello world!".upper())   # HELLO WORLD!  ← space and ! unchanged
print("HELLO WORLD!".lower())   # hello world!

print("hello@email.com".upper())    # HELLO@EMAIL.COM
print("HELLO@EMAIL.COM".lower())    # hello@email.com

print("Python 3.11".upper())    # PYTHON 3.11  ← dot and digits unchanged
print("PYTHON 3.11".lower())    # python 3.11

print("abc-DEF_123!".upper())   # ABC-DEF_123!
print("ABC-DEF_123!".lower())   # abc-def_123!

# This is very useful! You can safely call .upper() or .lower()
# on ANY string without worrying about breaking non-letter parts.


# ------------------------------------------------------------
# PART 5: The most important use case - case-insensitive comparison
# ------------------------------------------------------------

# This is THE most common reason to use .lower() or .upper().
# When comparing strings, Python is case-sensitive by default:

print("python" == "Python")     # False  ← different case!
print("python" == "PYTHON")     # False  ← different case!
print("Python" == "Python")     # True   ← identical

# This causes problems when users type input:
# User might type: "Python", "python", "PYTHON", "PyThOn"
# All mean the same thing, but Python sees them as different!

# ── Solution: convert both sides to the same case before comparing ──
user_input = "PYTHON"
correct    = "python"

# ❌ Without normalization:
print(user_input == correct)                        # False  ← wrong!

# ✅ With normalization:
print(user_input.lower() == correct.lower())        # True   ← correct!
print(user_input.upper() == correct.upper())        # True   ← also correct!

# ── Real example: language check ──
language = input("Enter your favorite language: ")
# User might type: Python, python, PYTHON, pYtHoN...

if language.lower() == "python":
    print("Great choice!")
else:
    print("Interesting!")
# This works regardless of how the user capitalized it!

# ── Real example: yes/no question ──
answer = input("Do you want to continue? (yes/no): ")
if answer.lower() == "yes":
    print("Continuing...")
elif answer.lower() == "no":
    print("Stopping.")
else:
    print("Please type yes or no.")
# Works for: YES, Yes, yes, YeS, yEs, etc.


# ------------------------------------------------------------
# PART 6: .isupper() and .islower() - checking case
# ------------------------------------------------------------

# These methods CHECK whether a string is already
# all uppercase or all lowercase.
# They return a BOOLEAN: True or False.

# .isupper() → True if ALL letters are uppercase
print("PYTHON".isupper())       # True
print("Python".isupper())       # False  ← 'ython' is lowercase
print("python".isupper())       # False

# .islower() → True if ALL letters are lowercase
print("python".islower())       # True
print("Python".islower())       # False  ← 'P' is uppercase
print("PYTHON".islower())       # False

# Important: non-letter characters are IGNORED in the check!
print("PYTHON123".isupper())    # True   ← digits ignored!
print("python123".islower())    # True   ← digits ignored!
print("PYTHON!".isupper())      # True   ← punctuation ignored!
print("python!".islower())      # True   ← punctuation ignored!
print("123".isupper())          # False  ← no letters at all!
print("123".islower())          # False  ← no letters at all!
print("".isupper())             # False  ← empty string
print("".islower())             # False  ← empty string

# Mixed case examples:
print("Hello".isupper())        # False
print("Hello".islower())        # False
# Neither! It's mixed case.

# Practical use:
word = "DNA"
if word.isupper():
    print(f"'{word}' is already uppercase")
else:
    print(f"'{word}' is not all uppercase")
# Output: 'DNA' is already uppercase


# ------------------------------------------------------------
# PART 7: .capitalize() - first letter uppercase only
# ------------------------------------------------------------

# .capitalize() returns a new string where:
#   - The FIRST character is uppercase
#   - ALL OTHER characters are lowercase

print("python".capitalize())        # Python
print("PYTHON".capitalize())        # Python  ← rest forced to lower!
print("hELLO wORLD".capitalize())   # Hello world
print("hello world".capitalize())   # Hello world
print("123abc".capitalize())        # 123abc  ← no letter at start

# Important: .capitalize() LOWERCASES everything except the first letter!
# This might not be what you want for strings that are already correct.

name = "anna KOWALSKA"
print(name.capitalize())    # Anna kowalska  ← KOWALSKA got lowercased!

# Compare with .title() which handles this better:
# (covered in Part 8)


# ------------------------------------------------------------
# PART 8: .title() - first letter of EACH word uppercase
# ------------------------------------------------------------

# .title() returns a new string where:
#   - The FIRST letter of EACH word is uppercase
#   - All other letters are lowercase
# This is called "Title Case"

print("hello world".title())            # Hello World
print("the quick brown fox".title())    # The Quick Brown Fox
print("python programming".title())     # Python Programming
print("HELLO WORLD".title())            # Hello World  ← corrects ALL CAPS too
print("hElLo WoRlD".title())            # Hello World  ← corrects mixed case

# .title() considers any non-letter as a word separator:
print("hello-world".title())            # Hello-World
print("hello_world".title())            # Hello_World
print("it's a test".title())            # It'S A Test  ← apostrophe splits!
# Note: "It'S" is a quirk! The 's' after apostrophe
# is treated as start of new word.

# Common use: formatting names and titles
book_title = "introduction to bioinformatics"
print(book_title.title())   # Introduction To Bioinformatics

full_name = "anna maria kowalska"
print(full_name.title())    # Anna Maria Kowalska


# ------------------------------------------------------------
# PART 9: .swapcase() - flip the case of every letter
# ------------------------------------------------------------

# .swapcase() returns a new string where:
#   - Uppercase letters → lowercase
#   - Lowercase letters → uppercase
# Every letter's case is FLIPPED.

print("Python".swapcase())          # pYTHON
print("Hello World".swapcase())     # hELLO wORLD
print("python".swapcase())          # PYTHON  ← all lower → all upper
print("PYTHON".swapcase())          # python  ← all upper → all lower
print("PyThOn".swapcase())          # pYtHoN
print("Hello123!".swapcase())       # hELLO123!  ← non-letters unchanged

# .swapcase() applied twice gives back the original:
word = "Hello World"
print(word.swapcase().swapcase())   # Hello World  ← back to start!
print(word.swapcase().swapcase() == word)   # True

# Practical use: less common than upper/lower/title,
# but useful for encoding tricks or stylistic purposes.


# ------------------------------------------------------------
# PART 10: Method chaining
# ------------------------------------------------------------

# Since each method returns a NEW string,
# you can call multiple methods one after another.
# This is called METHOD CHAINING.

# Syntax:
#   string.method1().method2().method3()
#
# Python evaluates left to right:
#   1. string.method1() → returns new string
#   2. (new string).method2() → returns another new string
#   3. (another new string).method3() → returns final string

word = "  hello world  "

# Chain: strip (remove spaces) → capitalize → (result)
# (we cover .strip() in next lecture, preview here)
result = word.strip().capitalize()
print(result)       # Hello world

# Chain: upper → ... back to lower:
word = "Hello"
print(word.upper().lower())     # hello
# "Hello" → "HELLO" → "hello"

# Chain: lower → title:
sentence = "THE QUICK BROWN FOX"
print(sentence.lower().title())     # The Quick Brown Fox
# "THE QUICK BROWN FOX" → "the quick brown fox" → "The Quick Brown Fox"

# This is better than:
# step1 = sentence.lower()
# step2 = step1.title()
# print(step2)
# ← same result but more lines

# ── Practical chain: normalize user input ──
raw_input = "  ANNA KOWALSKA  "
normalized = raw_input.strip().lower().title()
print(normalized)   # Anna Kowalska
# step 1: "  ANNA KOWALSKA  ".strip() → "ANNA KOWALSKA"
# step 2: "ANNA KOWALSKA".lower()     → "anna kowalska"
# step 3: "anna kowalska".title()     → "Anna Kowalska"

# ── Be careful: chaining changes the string progressively ──
word = "python"
print(word.upper().lower().capitalize())    # Python
# "python" → "PYTHON" → "python" → "Python"


# ------------------------------------------------------------
# PART 11: Methods do NOT modify the original string
# ------------------------------------------------------------

# This is worth repeating because it's a very common mistake.
# ALL string methods return NEW strings.
# The original string is NEVER changed (immutable!).

word = "hello"

# Calling the method without storing the result:
word.upper()            # ← this does NOTHING useful!
print(word)             # hello  ← still lowercase!

# ✅ You must STORE the result:
upper_word = word.upper()
print(upper_word)       # HELLO

# OR reassign to the same variable:
word = word.upper()
print(word)             # HELLO  ← now the variable is updated

# This mistake is extremely common for beginners:
name = "anna"
name.capitalize()       # ← result is THROWN AWAY
print(name)             # anna  ← not changed!

# ✅ Fix:
name = "anna"
name = name.capitalize()
print(name)             # Anna


# ------------------------------------------------------------
# PART 12: Combining with len(), indexing and slicing
# ------------------------------------------------------------

# String methods work beautifully together with
# len(), indexing, and slicing.

# ── Check first character case ──
word = "Python"
if word[0].isupper():
    print(f"'{word}' starts with uppercase letter")
else:
    print(f"'{word}' starts with lowercase letter")
# Output: 'Python' starts with uppercase letter

# ── Count uppercase letters using indexing ──
# (We'll do this properly with loops in Module 04)
# For now, manual example:
word = "PyThOn"
uppercase_count = 0
for char in word:           # preview of loops - don't worry!
    if char.isupper():
        uppercase_count += 1
print(uppercase_count)      # 3  ← P, T, O

# ── Normalize then slice ──
title = "  THE QUICK BROWN FOX  "
normalized = title.strip().lower().title()  # preview: .strip() removes spaces
first_word = normalized[:3]
print(first_word)           # The

# ── Compare lengths after case change ──
word = "Hello"
upper = word.upper()
print(len(word) == len(upper))  # True  ← case change never changes length!
# This is always true: upper/lower never add or remove characters


# ------------------------------------------------------------
# PART 13: Real world applications
# ------------------------------------------------------------

# ── Application 1: Case-insensitive login ──
stored_username = "AnnaKowalska"
entered_username = input("Enter username: ")

if entered_username.lower() == stored_username.lower():
    print("Username recognized!")
else:
    print("Username not found.")

# ── Application 2: Normalize city names ──
cities = ["warsaw", "KRAKOW", "gdANsk", "POZNAN", "wroclaw"]
for city in cities:
    print(city.title())
# Output:
# Warsaw
# Krakow
# Gdansk
# Poznan
# Wroclaw

# ── Application 3: Generate username from name ──
first_name = "Anna"
last_name = "Kowalska"
username = (first_name + last_name).lower()
print(username)         # annakowalska

# ── Application 4: Shout mode ──
message = "please read this carefully"
print(message.upper() + "!!!")  # PLEASE READ THIS CAREFULLY!!!

# ── Application 5: Check if DNA sequence is uppercase ──
dna = "ATGCCCGCA"
if dna.isupper():
    print("DNA sequence is properly formatted (uppercase)")
else:
    print("Warning: DNA sequence contains lowercase letters")
    dna = dna.upper()
    print(f"Corrected: {dna}")

# ── Application 6: Format a book title ──
raw_title = "introduction to computational biology"
formatted = raw_title.title()
print(formatted)    # Introduction To Computational Biology

# ── Application 7: Check yes/no more robustly ──
answer = input("Continue? ").strip().lower()
if answer in ("yes", "y"):
    print("Continuing!")
elif answer in ("no", "n"):
    print("Stopping.")
else:
    print("Invalid answer.")

# ── Application 8: Create acronym ──
phrase = "artificial intelligence"
words = phrase.title().split()      # preview: .split() in Lecture 09
acronym = ""
for word in words:
    acronym += word[0]
print(acronym)      # AI


# ------------------------------------------------------------
# PART 14: Complete method summary table
# ------------------------------------------------------------

word = "hello world"

# ┌──────────────┬─────────────────────────────┬──────────────────┐
# │ Method       │ What it does                │ Example result   │
# ├──────────────┼─────────────────────────────┼──────────────────┤
# │ .upper()     │ All letters → UPPERCASE     │ "HELLO WORLD"    │
# │ .lower()     │ All letters → lowercase     │ "hello world"    │
# │ .capitalize()│ First letter upper, rest    │ "Hello world"    │
# │              │ lower                       │                  │
# │ .title()     │ First letter of each word   │ "Hello World"    │
# │              │ upper, rest lower           │                  │
# │ .swapcase()  │ Flip every letter's case    │ "HELLO WORLD"→   │
# │              │                             │ "hello world"    │
# │ .isupper()   │ Are ALL letters uppercase?  │ True / False     │
# │ .islower()   │ Are ALL letters lowercase?  │ True / False     │
# └──────────────┴─────────────────────────────┴──────────────────┘

print("hello world".upper())       # HELLO WORLD
print("HELLO WORLD".lower())       # hello world
print("hello world".capitalize())  # Hello world
print("hello world".title())       # Hello World
print("Hello World".swapcase())    # hELLO wORLD
print("HELLO".isupper())           # True
print("hello".islower())           # True


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Methods are called with DOT NOTATION: string.method()
# ✅ .upper()      → ALL LETTERS to uppercase
# ✅ .lower()      → all letters to lowercase
# ✅ .capitalize() → First letter upper, rest lower
# ✅ .title()      → First Letter Of Each Word Upper
# ✅ .swapcase()   → fLIPS eVERY lETTER's cASE
# ✅ .isupper()    → True if all letters are uppercase
# ✅ .islower()    → True if all letters are lowercase
# ✅ Non-letter characters are NEVER affected
# ✅ Methods NEVER modify the original (strings are immutable!)
# ✅ Methods always return a NEW string
# ✅ Store the result or reassign: word = word.upper()
# ✅ Methods can be CHAINED: word.lower().title()
# ✅ Case change NEVER changes the length of a string
# ✅ Most common use: case-insensitive comparison with .lower()