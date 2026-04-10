# ============================================================
# MODULE 01 | LECTURE 07 - Comments
# ============================================================
# What you will learn:
#   - What a comment is and why it matters
#   - Single-line comments (#)
#   - Multi-line comments (""" or ''')
#   - Inline comments
#   - Docstrings
#   - Commenting best practices
#   - What NOT to do with comments
#   - Comments as a learning tool
# ============================================================


# ------------------------------------------------------------
# PART 1: What is a Comment?
# ------------------------------------------------------------

# A comment is text in your code that Python completely ignores
# It exists ONLY for humans - you, your teammates, your future self
# Python skips everything after # on that line

# This is a comment - Python ignores this line
print("Hello")  # Python runs this but ignores everything after #

# Comments do NOT affect how your program runs
# They are there to explain WHY the code does what it does

# Without comments - confusing:
x = 86400
y = x * 7

# With comments - clear:
seconds_per_day  = 86400        # 60 seconds * 60 minutes * 24 hours
seconds_per_week = seconds_per_day * 7

print(seconds_per_week)         # 604800


# ------------------------------------------------------------
# PART 2: Single-Line Comments (#)
# ------------------------------------------------------------

# The # symbol starts a single-line comment
# Everything after # on that line is ignored by Python

# This entire line is a comment
print("This line runs")     # This part is a comment

# Comments can appear:
# 1. On their own line (above or below code)
# 2. At the end of a line of code (inline comment)
# 3. Anywhere in the file

# Commenting out code - temporarily disable a line:
print("This runs")
# print("This does NOT run - it is commented out")
print("This runs too")

# Keyboard shortcut in VSCode:
# Windows/Linux : Ctrl + /
# Mac           : Cmd  + /
# This toggles comments on selected lines!


# ------------------------------------------------------------
# PART 3: Multi-Line Comments
# ------------------------------------------------------------

# Python has NO official multi-line comment syntax
# The # approach - comment each line individually:

# This is line one of a multi-line comment
# This is line two of a multi-line comment
# This is line three of a multi-line comment

# The """ approach - triple quotes as a workaround:
# Python treats this as a string that is never assigned
# It is not technically a comment but works the same way

"""
This is a multi-line
string used as a comment.
Python creates this string but immediately discards it
because it is not assigned to any variable.
"""

'''
You can also use single triple quotes.
Both work identically.
Most style guides prefer double quotes.
'''

# When to use each:
# # comments    → preferred for most cases
# """ strings   → preferred for docstrings (see Part 5)
#                 and temporarily disabling large blocks of code

# Temporarily disable a block of code:
"""
x = some_function()
y = another_function(x)
z = complex_calculation(x, y)
print(z)
"""
# The above block is "commented out" using triple quotes


# ------------------------------------------------------------
# PART 4: Inline Comments
# ------------------------------------------------------------

# Inline comments appear on the same line as code
# They should be separated by at least 2 spaces

# PEP 8 style guide recommendation:
x = 42              # answer to everything
pi = 3.14159        # approximation of π
name = "Anna"       # user's first name

# Inline comments should explain WHY, not WHAT
# Bad inline comment (states the obvious):
x = x + 1          # add 1 to x         ← pointless!

# Good inline comment (explains why):
x = x + 1          # compensate for zero-based indexing

# Inline comments for units - very useful!
distance = 384400   # km  - distance to the Moon
speed    = 299792   # km/s - speed of light
mass     = 70       # kg  - average human mass
temp     = 37.0     # °C  - normal body temperature

# Inline comments for magic numbers:
timeout  = 30       # seconds - API request timeout
max_retry = 3       # maximum connection attempts
buffer   = 1024     # bytes - read buffer size


# ------------------------------------------------------------
# PART 5: Docstrings
# ------------------------------------------------------------

# Docstrings are special strings that document:
#   - Functions
#   - Classes
#   - Modules
# They use triple quotes and appear as the FIRST statement

# They are NOT regular comments - Python stores them!
# You can access them with help() or .__doc__

# Simple one-line docstring:
def greet(name):
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"

# Multi-line docstring - Google style (most common):
def calculate_gc_content(sequence):
    """
    Calculate the GC content of a DNA sequence.

    Args:
        sequence (str): DNA sequence containing A, T, G, C characters.

    Returns:
        float: GC content as a percentage between 0.0 and 100.0.

    Examples:
        >>> calculate_gc_content("ATCG")
        50.0
        >>> calculate_gc_content("GGCC")
        100.0
    """
    sequence = sequence.upper()
    gc_count = sequence.count("G") + sequence.count("C")
    return (gc_count / len(sequence)) * 100

# Accessing a docstring:
print(greet.__doc__)
# Return a greeting message for the given name.

print(calculate_gc_content.__doc__)
# (prints the full docstring)

# help() shows docstring in a formatted way:
help(greet)

# Module docstring - at the very top of a file:
# """
# my_module.py
#
# This module provides utility functions for DNA analysis.
#
# Author: Your Name
# Date: 2025-01-01
# Version: 1.0
# """


# ------------------------------------------------------------
# PART 6: What Makes a GOOD Comment
# ------------------------------------------------------------

# RULE 1: Explain WHY, not WHAT
# The code shows WHAT - comments explain WHY

# Bad - explains what (obvious from code):
total = price * quantity     # multiply price by quantity

# Good - explains why:
total = price * quantity     # subtotal before tax and shipping

# Bad:
i = i + 2                   # add 2 to i

# Good:
i = i + 2                   # skip every other nucleotide (step = 2)


# RULE 2: Keep comments up to date
# Outdated comments are WORSE than no comments!

# Bad example (comment lies about what code does):
# Multiply by 2
result = x * 3              # ← someone changed *2 to *3 but forgot comment!

# Good practice: update comment when you update code


# RULE 3: Don't state the obvious
# If the code is self-explanatory, skip the comment

# Bad:
name = "Anna"               # set name to Anna
age  = 25                   # set age to 25
print(name)                 # print name

# Good (no comments needed - code is clear):
name = "Anna"
age  = 25
print(name)


# RULE 4: Use comments for complex logic
# Anything non-obvious SHOULD have a comment

# Without comment - hard to understand:
result = n & (n - 1) == 0

# With comment - now it makes sense:
result = n & (n - 1) == 0   # checks if n is a power of 2 (bitwise trick)


# RULE 5: Use comments for important warnings
# ⚠️  IMPORTANT: sequence must be uppercase before calling this function
# ⚠️  DO NOT change the order of these operations
# TODO: handle edge case when sequence is empty
# FIXME: this crashes when input contains spaces
# NOTE: this function is deprecated, use parse_v2() instead
# HACK: temporary workaround for bug #123


# RULE 6: Comment at the right level of detail
# Too much detail is as bad as too little

# Too detailed (over-commented):
x = 5           # assign integer value 5 to variable x
y = 10          # assign integer value 10 to variable y
z = x + y       # add x and y together and store result in z
print(z)        # print the value of z to standard output

# Right level (no comments needed here):
x = 5
y = 10
z = x + y
print(z)


# ------------------------------------------------------------
# PART 7: Common Comment Tags (TODO, FIXME, etc.)
# ------------------------------------------------------------

# Many developers use standard tags that IDEs can highlight

# TODO  - something to implement later
# TODO: add input validation here
# TODO: refactor this function when time allows

# FIXME - broken code that needs fixing
# FIXME: crashes when sequence contains lowercase letters
# FIXME: off-by-one error in the loop below

# NOTE  - important information the reader should know
# NOTE: this algorithm assumes sorted input
# NOTE: returns None if no match found

# HACK  - temporary or non-obvious solution
# HACK: workaround for BioPython version < 1.79

# WARNING or ⚠️  - dangerous or tricky section
# WARNING: do not modify this value - affects all downstream calculations

# DEPRECATED - code that should no longer be used
# DEPRECATED: use calculate_gc_v2() instead

# In VSCode these tags are highlighted with extensions like:
# "Todo Tree" or "Better Comments"


# ------------------------------------------------------------
# PART 8: File Header Comments
# ------------------------------------------------------------

# Many projects use a standard header at the top of each file
# It provides key information at a glance

# Example file header:
"""
============================================================
filename    : 07_comments.py
description : Lecture on Python comments and docstrings
author      : Your Name
created     : 2025-01-01
modified    : 2025-01-15
version     : 1.0
============================================================
"""

# Simpler version for student projects:
# ============================================================
# Module 01 | Lecture 07 - Comments
# Author   : Your Name
# Date     : 2025-01-01
# ============================================================


# ------------------------------------------------------------
# PART 9: Section Separator Comments
# ------------------------------------------------------------

# Large files benefit from visual section separators
# They make navigation much easier

# Style 1 - simple:
# --- Input ---
# --- Processing ---
# --- Output ---

# Style 2 - with borders:
# ========================
# INPUT SECTION
# ========================

# Style 3 - with dashes (used in this lecture):
# ------------------------------------------------------------
# SECTION NAME
# ------------------------------------------------------------

# Style 4 - numbered sections:
# --- 1. Load Data ---
# --- 2. Clean Data ---
# --- 3. Analyze Data ---
# --- 4. Save Results ---

# Choose ONE style and use it consistently in your project!


# ------------------------------------------------------------
# PART 10: Comments as a Learning Tool
# ------------------------------------------------------------

# Comments are ESPECIALLY valuable when you are learning
# Use them to:
#   1. Explain what you are trying to do BEFORE writing code
#   2. Note what you don't understand yet
#   3. Track what you have learned
#   4. Leave breadcrumbs for your future self

# Example of learning-style comments:

# GOAL: calculate the percentage of G and C in DNA sequence
sequence = "ATCGGCTATCGA"

# Step 1: count each nucleotide
# I learned that .count() returns how many times a substring appears
count_g = sequence.count("G")   # 2
count_c = sequence.count("C")   # 2
total   = len(sequence)         # 12

# Step 2: calculate percentage
# Formula: (G + C) / total * 100
# Multiplying by 100 converts decimal to percentage
gc_percent = (count_g + count_c) / total * 100

# Step 3: display result
# :.1f means show 1 decimal place
print(f"GC content: {gc_percent:.1f}%")    # GC content: 33.3%

# I need to remember: .count() is case sensitive!
# "atcg".count("G") returns 0, not 1


# ------------------------------------------------------------
# PART 11: What NOT to Do with Comments
# ------------------------------------------------------------

# BAD PRACTICE 1: Commented-out code left permanently
# Clean up old commented code - use Git to go back if needed!
# x = old_function()       ← delete this, don't leave it commented
# y = another_old_approach()

# BAD PRACTICE 2: Lying comments
x = 10
# x = 20                   ← comment says x is 20, code says 10!

# BAD PRACTICE 3: Redundant comments everywhere
def add(a, b):
    # add a and b
    result = a + b      # calculate sum
    return result       # return the result

# Better:
def add(a, b):
    """Return the sum of a and b."""
    return a + b

# BAD PRACTICE 4: Wall of text comments
# This function takes a sequence parameter which should be a string
# containing only the characters A T G and C representing the four
# nucleotides adenine thymine guanine and cytosine respectively and
# calculates the ratio of G and C nucleotides to the total length...

# Better:
def gc_content(sequence):
    """Calculate GC% of a DNA sequence (A/T/G/C only)."""
    gc = sequence.count("G") + sequence.count("C")
    return gc / len(sequence) * 100

# BAD PRACTICE 5: Funny or unprofessional comments
# this is so stupid why does python do this
# I have no idea why this works but it does
# don't touch this or everything breaks lol

# Better:
# Counterintuitive: Python's // floors toward negative infinity
# This works due to short-circuit evaluation (see Part 6)
# ⚠️  This value is used in 3 other functions - change carefully


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ # comment          - single line, everything after # ignored
# ✅ # comment          - Ctrl+/ to toggle in VSCode
# ✅ """ text """       - multi-line (technically a string)
# ✅ Docstrings         - first line of function/class, use """
# ✅ Inline comments    - 2 spaces before #, explain WHY
# ✅ TODO / FIXME       - standard tags for future work
# ✅ File headers       - key info at top of file
# ✅ Section separators - navigate large files easily
# ✅ Explain WHY        - not WHAT (code shows what)
# ✅ Keep updated       - outdated comments are dangerous
# ⚠️  Don't over-comment - obvious code needs no comment
# ⚠️  Don't lie         - wrong comments are worse than none
# ⚠️  Don't leave junk  - remove old commented-out code
# ⚠️  Don't be funny    - keep comments professional