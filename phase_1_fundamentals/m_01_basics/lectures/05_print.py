# ============================================================
# MODULE 01 | LECTURE 05 - print()
# ============================================================
# What you will learn:
#   - print() basic usage
#   - Multiple arguments
#   - sep parameter
#   - end parameter
#   - file parameter
#   - flush parameter
#   - Printing different data types
#   - Common patterns and tricks
# ============================================================


# ------------------------------------------------------------
# PART 1: Basic print()
# ------------------------------------------------------------

# print() displays output to the screen
# It is a built-in function - no import needed

print("Hello World")        # Hello World
print(42)                   # 42
print(3.14)                 # 3.14
print(True)                 # True
print(None)                 # None

# Empty print() - prints a blank line
print()                     # (blank line)

# print() always adds a newline at the end by default
print("line 1")
print("line 2")
print("line 3")
# Output:
# line 1
# line 2
# line 3


# ------------------------------------------------------------
# PART 2: Multiple Arguments
# ------------------------------------------------------------

# print() accepts multiple arguments separated by commas
# They are printed with a SPACE between them by default

print("Hello", "World")                     # Hello World
print("Name:", "Anna")                      # Name: Anna
print("Age:", 25)                           # Age: 25  ← no str() needed!
print("Pi:", 3.14, "is", "useful")          # Pi: 3.14 is useful
print(1, 2, 3, 4, 5)                        # 1 2 3 4 5
print("a", "b", "c", 1, 2, True, None)     # a b c 1 2 True None

# This is why print() is easier than concatenation for debugging:
name = "Anna"
age = 25
gpa = 4.75

# Concatenation - requires str() conversion:
print("Name: " + name + " Age: " + str(age))

# Multiple arguments - no conversion needed:
print("Name:", name, "Age:", age, "GPA:", gpa)


# ------------------------------------------------------------
# PART 3: sep parameter
# ------------------------------------------------------------

# sep defines what goes BETWEEN multiple arguments
# Default is a single space: sep=" "

# Default (space)
print("a", "b", "c")               # a b c

# No separator
print("a", "b", "c", sep="")       # abc

# Custom separators
print("a", "b", "c", sep="-")      # a-b-c
print("a", "b", "c", sep=", ")     # a, b, c
print("a", "b", "c", sep=" | ")    # a | b | c
print("a", "b", "c", sep="\n")     # a
                                    # b
                                    # c
print("a", "b", "c", sep="🧬")    # a🧬b🧬c

# Practical examples
print("2024", "01", "15", sep="-")          # 2024-01-15  (date)
print("192", "168", "0", "1", sep=".")      # 192.168.0.1 (IP address)
print("www", "python", "org", sep=".")      # www.python.org
print(1, 2, 3, 4, 5, sep=", ")             # 1, 2, 3, 4, 5

# sep with numbers - no str() needed!
year, month, day = 2024, 1, 15
print(year, month, day, sep="/")            # 2024/1/15


# ------------------------------------------------------------
# PART 4: end parameter
# ------------------------------------------------------------

# end defines what goes at the END of print()
# Default is newline: end="\n"

# Default (newline)
print("Hello")
print("World")
# Hello
# World

# No newline at end - next print continues on same line!
print("Hello", end="")
print("World")
# HelloWorld

# Space at end
print("Hello", end=" ")
print("World")
# Hello World

# Custom ending
print("Hello", end="!!!\n")
print("World")
# Hello!!!
# World

# Combining sep and end
print("a", "b", "c", sep="-", end="!!!\n")     # a-b-c!!!

# Practical: printing on same line in a loop (preview of loops)
# Instead of:
print("Loading", end="")
print(".", end="")
print(".", end="")
print(".", end="")
print(" Done!")
# Loading... Done!

# end="" is very useful for building output progressively


# ------------------------------------------------------------
# PART 5: Printing Different Data Types
# ------------------------------------------------------------

# print() handles ALL types automatically
# No conversion needed unlike string concatenation

# Basic types
print(42)                   # int
print(3.14)                 # float
print(True)                 # bool
print(None)                 # NoneType
print("hello")              # str

# Collections (preview - covered in later modules)
print([1, 2, 3])            # [1, 2, 3]
print((1, 2, 3))            # (1, 2, 3)
print({"a": 1, "b": 2})    # {'a': 1, 'b': 2}
print({1, 2, 3})            # {1, 2, 3}

# Mixed types in one print
print("int:", 42, "float:", 3.14, "bool:", True, "none:", None)

# Printing the type itself
print(type(42))             # <class 'int'>
print(type("hello"))        # <class 'str'>


# ------------------------------------------------------------
# PART 6: print() vs f-strings vs str concatenation
# ------------------------------------------------------------

name = "Anna"
age = 25
score = 98.765

# Method 1: Multiple arguments (good for quick debugging)
print("Name:", name, "Age:", age, "Score:", score)

# Method 2: f-string (best for formatted output)
print(f"Name: {name} | Age: {age} | Score: {score:.2f}")

# Method 3: str concatenation (avoid - requires str())
print("Name: " + name + " Age: " + str(age))

# Method 4: .format() (older style, still valid)
print("Name: {} Age: {} Score: {:.2f}".format(name, age, score))

# When to use which:
# print("x:", x)          ← quick debug - use multiple args
# print(f"x = {x:.2f}")  ← formatted output - use f-string
# print(x, y, sep="\t")  ← table-like output - use sep


# ------------------------------------------------------------
# PART 7: Printing Special Characters
# ------------------------------------------------------------

# Newline \n
print("line1\nline2\nline3")

# Tab \t - useful for alignment
print("Name\tAge\tCity")
print("Anna\t25\tWarsaw")
print("Bob\t30\tKrakow")
# Name    Age     City
# Anna    25      Warsaw
# Bob     30      Krakow

# Backslash \\
print("Path: C:\\Users\\Anna")      # Path: C:\Users\Anna

# Quotes inside strings
print("He said \"hello\"")          # He said "hello"
print('She said \'hi\'')            # She said 'hi'

# Unicode characters
print("\u03B1")     # α  (alpha)
print("\u03B2")     # β  (beta)
print("\u03B3")     # γ  (gamma)
print("\u2192")     # →  (right arrow)
print("\u2713")     # ✓  (checkmark)
print("\u2717")     # ✗  (cross)

# Emoji (directly or unicode)
print("🧬 DNA")
print("🐍 Python")
print("\U0001F9EC")     # 🧬 (DNA emoji via unicode)


# ------------------------------------------------------------
# PART 8: file parameter
# ------------------------------------------------------------

# print() can write to a FILE instead of screen
# This is how you write to files using print()!

import sys

# Write to standard error (useful for error messages)
print("This is an error message", file=sys.stderr)

# Write to a file
with open("output.txt", "w") as f:
    print("Hello File!", file=f)
    print("Line 2", file=f)
    print("Name:", "Anna", file=f)
    print(1, 2, 3, sep=", ", file=f)

# The file output.txt now contains:
# Hello File!
# Line 2
# Name: Anna
# 1, 2, 3

print("Written to output.txt!")

# Read and verify what was written
with open("output.txt", "r") as f:
    content = f.read()
    print("File contents:")
    print(content)


# ------------------------------------------------------------
# PART 9: flush parameter
# ------------------------------------------------------------

# By default Python BUFFERS output - collects it before printing
# flush=True forces immediate output - useful for:
#   - Progress bars
#   - Real-time logging
#   - Long-running programs

import time

# Without flush (output might be delayed):
print("Processing", end="")
print(".", end="", flush=True)      # flush=True forces immediate print
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(".", end="", flush=True)
time.sleep(0.5)
print(" Done!", flush=True)

# You will mainly use flush=True with progress indicators


# ------------------------------------------------------------
# PART 10: Useful print() Patterns
# ------------------------------------------------------------

# Pattern 1: Separator lines for readability
print("=" * 40)
print("REPORT TITLE")
print("=" * 40)
print("Data here")
print("-" * 40)

# Pattern 2: Debugging multiple variables at once
x, y, z = 10, 20, 30
print(f"{x=}")          # x=10  ← Python 3.8+ debug format!
print(f"{y=}")          # y=20
print(f"{z=}")          # z=30
print(f"{x+y=}")        # x+y=30

# Pattern 3: Table-like output with sep="\t"
print("Name", "Age", "City", "Score", sep="\t")
print("-" * 40)
print("Anna",  25, "Warsaw", 98.5,  sep="\t")
print("Bob",   30, "Krakow", 87.2,  sep="\t")
print("Carol", 22, "Gdansk", 95.0,  sep="\t")

# Pattern 4: Inline progress (same line)
steps = ["Downloading", "Processing", "Saving", "Done"]
for step in steps:
    print(f"\r{step}...", end="", flush=True)
    time.sleep(0.5)
print()     # final newline

# Pattern 5: Print with index (using enumerate preview)
items = ["Python", "BioPython", "NumPy", "Pandas"]
for i, item in enumerate(items, 1):
    print(f"{i}. {item}")
# 1. Python
# 2. BioPython
# 3. NumPy
# 4. Pandas

# Pattern 6: Conditional print (one-liner)
score = 85
print("Pass" if score >= 60 else "Fail")    # Pass


# ------------------------------------------------------------
# PART 11: repr() vs str() in print context
# ------------------------------------------------------------

# str()  - human readable output (what print() uses)
# repr() - developer representation - shows exact type info

text = "hello\nworld"

print(str(text))        # hello
                        # world    ← \n becomes actual newline

print(repr(text))       # 'hello\nworld'  ← shows \n literally

# Useful for debugging strings with hidden characters
messy = "hello   \t world  \n"
print(str(messy))       # hard to see the tabs and newlines
print(repr(messy))      # 'hello   \t world  \n'  ← clearly visible!


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ print()              - basic output, adds \n at end
# ✅ print(a, b, c)       - multiple args, space between by default
# ✅ sep=","              - custom separator between arguments
# ✅ end=""               - custom ending (default is \n)
# ✅ file=f               - write to file instead of screen
# ✅ flush=True           - force immediate output
# ✅ print(f"{x=}")       - debug format showing variable name
# ✅ print("="*40)        - separator lines
# ✅ \n \t \\ \" \'       - special characters
# ✅ repr()               - developer-friendly string representation
# ⚠️  print() with multiple args adds spaces automatically
# ⚠️  end="" removes the automatic newline
# ⚠️  flush=True needed for real-time progress output