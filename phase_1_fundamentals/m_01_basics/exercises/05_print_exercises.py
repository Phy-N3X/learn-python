# ============================================================
# MODULE 01 | EXERCISES 05 - print()
# ============================================================
# 15 exercises - print() only
# Allowed from previous lectures:
#   - variables, type()                 (lecture 01)
#   - numbers, math operators           (lecture 02)
#   - string methods, slicing           (lecture 03)
#   - bool, comparison operators        (lecture 04)
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Print each of these values using a SEPARATE print() call:
#   - integer: 2024
#   - float: 3.14159
#   - boolean: True
#   - None
#   - string: "Bioinformatics"
#   - empty line (just blank space between outputs)
#
# Then print ALL of them in ONE single print() call
# with " | " as separator.
# Expected single-line output:
#   2024 | 3.14159 | True | None | Bioinformatics



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Using ONLY sep parameter (no f-strings, no concatenation):
# Print the following outputs exactly:
#
#   2024-01-15
#   192.168.1.100
#   www.python.org
#   John, 25, Warsaw, Python
#   1 | 2 | 3 | 4 | 5
#
# Each line is a SEPARATE print() call.
# Use variables for the values, not hardcoded strings.



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Using ONLY end parameter, produce this EXACT output
# using exactly 6 print() calls (one per word/symbol):
#
#   Hello, World! How are you?
#
# Each print() prints ONE word or symbol.
# Hint: think carefully about spaces and the question mark.



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Print this formatted table using sep="\t":
#
#   Name        Age     City        Score
#   ----------------------------------------
#   Alice       25      Warsaw      98.5
#   Bob         30      Krakow      87.2
#   Charlie     22      Gdansk      95.0
#
# Use variables for all values.
# The separator line should be exactly 40 "-" characters.



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Special characters practice.
# Using escape sequences, produce this EXACT output
# in as FEW print() calls as possible:
#
#   Line 1
#   Line 2
#   Line 3
#
#   Name:   Anna
#   City:   Warsaw
#
#   Path: C:\Users\Anna\Documents
#   Quote: She said "hello"



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Python 3.8+ debug format: f"{variable=}"
# Given:
#   x = 42
#   name = "Anna"
#   pi = 3.14159
#   is_valid = True
#   result = x * 2 + 10
#
# Use f"{variable=}" to print each variable.
# Expected output format:
#   x=42
#   name='Anna'
#   pi=3.14159
#   is_valid=True
#   result=94
#
# Then also print:
#   x * 2 + 10 = 94    (using f"{x * 2 + 10=}")



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a formatted report using ONLY print() and sep/end.
# NO f-strings allowed in this exercise!
#
# Given:
#   title    = "DNA Analysis Report"
#   organism = "E. coli"
#   length   = 4639221
#   gc       = 50.8
#
# Produce this EXACT output:
#   ========================================
#   DNA Analysis Report
#   ========================================
#   Organism : E. coli
#   Length   : 4639221
#   GC%      : 50.8
#   ========================================
#
# Hint: use sep="" to control spacing precisely.



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# repr() vs str() investigation.
# Given these strings:
#   a = "hello\nworld"
#   b = "name:\tAnna"
#   c = "C:\\Users\\Anna"
#   d = "   spaces   "
#
# For each string, print BOTH str() and repr() versions.
# Format:
#   str:  hello
#         world
#   repr: 'hello\nworld'
#
# Write a comment explaining when repr() is more useful
# than str() for debugging.



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Write to a file using print(file=f).
#
# Create a file called "student_report.txt" containing:
#
#   ================================
#   STUDENT REPORT
#   ================================
#   Name:    Anna Kowalski
#   Age:     22
#   GPA:     3.85
#   Status:  Active
#   ================================
#
# Use variables for all values.
# After writing, READ the file and print its contents
# to the screen to verify.
# Use print(file=f) for writing - NOT f.write()!



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Inline progress simulation using end="" and flush=True.
#
# Simulate a loading bar that looks like this
# (each step prints after 0.3 second delay):
#
#   Loading: [          ]   0%
#   Loading: [=         ]  10%
#   Loading: [==        ]  20%
#   ...
#   Loading: [==========] 100%
#   Complete!
#
# Requirements:
#   - Use \r to overwrite the same line each time
#   - Use end="" and flush=True
#   - Use import time and time.sleep(0.3)
#   - Bar width = 10 characters
#   - Show percentage
#
# Hint: filled = "=" * step, empty = " " * (10 - step)



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Predict the EXACT output of each print() call.
# Write prediction as comment BEFORE running.
#
# print("a", "b", "c")
# print("a", "b", "c", sep="")
# print("a", "b", "c", sep="\n")
# print("a", "b", "c", end="")
# print("a", "b", "c", sep="-", end="!\n")
# print("x", end=" "); print("y", end=" "); print("z")
# print("go", end="..."); print("stop")
# print(*[1, 2, 3, 4, 5])
# print(*[1, 2, 3, 4, 5], sep="-")
# print(*"hello")



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Unicode art - print this pattern using unicode characters
# and print() only:
#
#   ╔══════════════════════╗
#   ║   PYTHON LEARNING    ║
#   ║   🐍 Module 01 🐍   ║
#   ╚══════════════════════╝
#
# Unicode box characters:
#   ╔ = \u2554    ═ = \u2550    ╗ = \u2557
#   ║ = \u2551                  ║ = \u2551
#   ╚ = \u255A    ═ = \u2550    ╝ = \u255D
#
# Use variables for the box width so it's easy to resize.
# Content must be centered within the box.
# Hint: use string multiplication for ═ lines.



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Print a multiplication table using sep and end.
# Produce this EXACT output:
#
#     1   2   3   4   5
#     2   4   6   8  10
#     3   6   9  12  15
#     4   8  12  16  20
#     5  10  15  20  25
#
# Requirements:
#   - Use nested loops (preview: for i in range(1,6))
#   - Each number takes 4 characters (right aligned)
#     Hint: f"{num:4d}" or rjust(4)
#   - Use end="" to stay on same line
#   - Use print() to move to next line after each row
#   - NO sep parameter needed



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a complete pretty-printer for any data.
# Given this data:
#
# students = [
#     ("Alice",   22, "Warsaw",  98.5, True),
#     ("Bob",     30, "Krakow",  87.2, False),
#     ("Charlie", 22, "Gdansk",  95.0, True),
#     ("Diana",   28, "Poznan",  91.7, True),
#     ("Edward",  35, "Wroclaw", 72.3, False),
# ]
#
# Print this EXACT formatted table:
#
#   ┌─────────┬─────┬─────────┬───────┬────────┐
#   │ Name    │ Age │ City    │ Score │ Active │
#   ├─────────┼─────┼─────────┼───────┼────────┤
#   │ Alice   │  22 │ Warsaw  │  98.5 │ True   │
#   │ Bob     │  30 │ Krakow  │  87.2 │ False  │
#   │ Charlie │  22 │ Gdansk  │  95.0 │ True   │
#   │ Diana   │  28 │ Poznan  │  91.7 │ True   │
#   │ Edward  │  35 │ Wroclaw │  72.3 │ False  │
#   └─────────┴─────┴─────────┴───────┴────────┘
#
# Box drawing characters:
#   ┌ \u250C  ─ \u2500  ┬ \u252C  ┐ \u2510
#   │ \u2502             ┼ \u253C  │ \u2502
#   ├ \u251C  ─ \u2500  ┼ \u253C  ┤ \u2524
#   └ \u2514  ─ \u2500  ┴ \u2534  ┘ \u2518
#
# Use f-strings for alignment within cells.



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Build a real-time file logger using print(file=f, flush=True)
#
# Requirements:
#   1. Import time and sys
#   2. Create a file "session_log.txt"
#   3. Every 0.5 seconds, print a log entry BOTH to:
#      - the screen (normal print)
#      - the log file (print with file=f)
#   4. Run for exactly 5 entries
#   5. Each entry format (both screen and file):
#      [2024-01-15 10:30:00] Entry 1/5 - Status: OK
#      [2024-01-15 10:30:00] Entry 2/5 - Status: OK
#      ...
#
#   For timestamp use:
#      import time
#      timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
#
#   6. After all entries, print to screen only:
#      "Log saved to session_log.txt"
#   7. Read and print the log file to verify.
