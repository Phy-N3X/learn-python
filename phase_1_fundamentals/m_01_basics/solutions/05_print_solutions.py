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
print("Exercise 1: ")
print("integer", 2024, sep=": ")
print("float", 3.14159, sep=": ")
print("boolean", True, sep=": ")
print("None", sep=": ")
print("string", "Bioinformatics", sep=": ")
print()
print(2024, 3.14159, True, None, "Bioinformatics",sep=" | ")



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
print("\nExercise 2: ")
print(2024, "01", 15, sep="-")
print(192, 168, 1, 100, sep=".")
print("www", "python", "org", sep=".")
print("John", 25, "Warsaw", "Python", sep=", ")
print(1, 2, 3, 4, 5, sep=" | ")



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

print("\nExercise 3: ")




# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
name_1, name_2, name_3 = "Alice", "Bob", "Charlie"
age_1, age_2, age_3 = 25, 30, 22
city_1, city_2, city_3 = "Warsaw", "Krakow", "Gdansk"
score_1, score_2, score_3 = 98.5, 87.2, 95.0

print("\nExercise 4: ")
print("Name", "Age", "City", "Score", sep="\t ")
print("-" * 40)
print(name_1, age_1, city_1, score_1, sep=" \t ")
print(name_2, age_2, city_2, score_2, sep=" \t ")
print(name_3, age_3, city_3, score_3, sep="\t  ")



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
print("\nExercise 5: ")
print("Line 1\nLine 2\nLine 3\n\nName:\tAnna\nCity:\tWarsaw")
print("\nPath: C:\\Users\\Anna\\Documents\nQuote: She said \"hello\"")



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
x = 42
name = "Anna"
pi = 3.14159
is_valid = True
result = x * 2 + 10

print("\nExercise 6: ")
print(f"{x=}")
print(f"{name=}")
print(f"{pi=}")
print(f"{is_valid=}")
print(f"{result=}")

print(f"{x * 2 + 10=}")



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
title    = "DNA Analysis Report"
organism = "E. coli"
length   = 4639221
gc       = 50.8

print("\nExercise 7: ")
print("=" * 40)
print(title)
print("=" * 40)
print("Organism", ":", sep=" ", end="  ")
print(organism)
print("Length", ":", sep="   ", end="  ")
print(length)
print("Gc", ":", sep="       ", end="  ")
print(gc)
print("=" * 40)



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

print("\nExercise 7: ")
print("a (repr()): ")



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
