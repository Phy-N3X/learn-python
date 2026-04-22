# ============================================================
# MODULE 02 | EXERCISES 27 - Special Characters
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Basic escape sequences.
# For each escape sequence, write a string that uses it
# and print the result. Then print len() of the escape
# sequence alone to confirm it's ONE character.

# a) Print "Hello" and "World" on separate lines using \n
# b) Print "Name", "Age", "City" separated by tabs using \t
# c) Print: It's a beautiful day  (using \')
# d) Print: She said "Python!"    (using \")
# e) Print: C:\Users\Anna         (using \\)



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Verify that each escape sequence is ONE character.
# For each, print:
#   - The escape sequence itself (or its effect)
#   - len() of just the escape sequence
#   - repr() of just the escape sequence

sequences = ["\n", "\t", "\\", "\'", "\"", "\r", "\b", "\a"]
# Process each manually (no loops yet)
# Format: "repr: X | len: Y"



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output BEFORE running each line.
# Write predictions as comments, then verify.
# For invisible outputs, use repr() to confirm.

# Prediction: how many lines of output?
print("A\nB\nC")

# Prediction: what does len() return?
print(len("Hello\nWorld"))

# Prediction: what character is at index 5?
text = "Hello\nWorld"
print(repr(text[5]))

# Prediction: how many characters?
print(len("\n\t\\"))

# Prediction: what prints?
print("one\ttwo\tthree")

# Prediction: what is the result?
print("Line1\nLine2".count("\n"))



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use repr() as a debugging tool.
# The strings below all "look" the same when printed
# but are actually different. Use repr() to reveal
# the hidden differences. Write a comment explaining each.

text1 = "Hello"
text2 = "Hello\n"
text3 = "Hello\t"
text4 = "Hello "
text5 = "Hello\r"

# For each: print(repr(textX)) and explain what you see.
# Then check: which are equal to "Hello"?
# Use == to verify.



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Windows path problem.
# The path below is WRONG - fix it two different ways.
# Explain what goes wrong without the fix.

# ❌ Wrong (uncomment to see the issue):
# wrong_path = "C:\new_folder\test.txt"
# print(wrong_path)     # What does this print? Why is it wrong?

# ✅ Fix 1: use \\ for each backslash
# ✅ Fix 2: use raw string (preview of next lecture - r"...")

# After fixing, verify with repr() that the path is correct.
# Expected: 'C:\\new_folder\\test.txt'



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Multi-line text using \n.
# Create these strings using \n (NOT triple quotes).
# Print each and verify the output looks correct.

# a) A poem (4 lines):
#    Roses are red
#    Violets are blue
#    Python is great
#    And so are you

# b) A simple address:
#    Anna Kowalska
#    ul. Słoneczna 15
#    00-001 Warsaw
#    Poland

# c) Print a simple "box" using only one print() call:
#    +----------+
#    |  Python  |
#    +----------+



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Special characters with string operations.
# For the string below, use what you know about
# indexing, slicing, len(), and split() with special chars.

text = "Hello\tWorld\nPython\tProgramming"

# a) What is len(text)?  Predict first, then verify.
# b) What is text[5]?    Use repr() to show the answer.
# c) What is text[11]?   Use repr() to show the answer.
# d) Split on "\n" - how many parts?
# e) Split on "\t" - how many parts?
# f) Replace all \t with spaces and all \n with " | "
# g) Print repr(text) to see everything at once.



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Unicode characters.
# Use \u escape sequences to print these characters.
# Then use \N{name} for the same characters.

# a) Greek letters: α β γ δ π Σ
#    (\u03b1, \u03b2, \u03b3, \u03b4, \u03c0, \u03a3)

# b) Mathematical symbols: ∞ ≈ ≠ ≤ ≥ √ ±
#    (\u221e, \u2248, \u2260, \u2264, \u2265, \u221a, \u00b1)

# c) Arrows: → ← ↑ ↓ ⇌
#    (\u2192, \u2190, \u2191, \u2193, \u21cc)

# d) Biology/Chemistry: ° (degree), µ (micro), Å (angstrom)
#    (\u00b0, \u00b5, \u00c5)

# e) Print your name with a heart: "Anna ♥ Python"
#    (\u2665)



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# TSV file processing using \t.
# The string below represents a TSV (Tab-Separated Values) file.
# Each line is a record, each field is separated by \t.

tsv_data = "name\tage\tcity\tcountry\nAnna\t25\tWarsaw\tPoland\nJan\t32\tKrakow\tPoland\nMaria\t28\tBerlin\tGermany"

# Tasks:
# a) Split into lines using \n
# b) Split the first line (header) on \t to get column names
# c) Split the second line on \t to get Anna's data
# d) Print Anna's name and city with labels
# e) How many records are there (excluding header)?
# f) Replace all \t with "," and all \n with "\n" to convert to CSV
#    (hint: just replace \t with ",")
# g) Print the original and CSV version using repr()



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Building formatted text with special characters.
# Create each of the following using ONLY special characters
# (\n, \t, \\) - no .format() or f-strings needed.
#
# a) A simple table (use \t for columns, \n for rows):
#    Name       Age    City
#    Anna       25     Warsaw
#    Jan        32     Krakow
#
# b) A file tree (use \t for indentation, \n for lines):
#    home\
#        user\
#            documents\
#                report.pdf
#                data.csv
#            pictures\
#                photo.jpg
#
# c) A formatted receipt:
#    ========================
#    Item           Price
#    ========================
#    Python Book    29.99
#    DNA Kit        149.99
#    ========================
#    TOTAL          179.98
#    ========================
# (Use \n between lines, \t between columns)



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Count and analyze special characters in text.
# Given the text below:

text = "Line 1\nLine 2\nLine 3\n\nLine 5\tTabbed\nLine 6"

# a) How many newlines? (use .count("\n"))
# b) How many tabs?
# c) How many lines? (newlines + 1, but check for empty lines!)
# d) Split into lines - print each line with its line number
# e) How many EMPTY lines are there?
#    (hint: split on \n, count elements that are "" or "")
# f) Strip the whole text and count newlines again - same result?
# g) Replace all \t with 4 spaces and print repr() of result



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL errors and unexpected behaviors below.
# Write a comment for each line explaining what's wrong.
# Then fix all actual errors.

# What does this print? Is it what you'd expect?
path = "C:\new_folder\test.txt"
print(path)                         # Surprising? Explain.
print(repr(path))                   # What does repr reveal?

# What is the length?
text = "Hello\nWorld"
print(len(text))                    # Prediction: ?

# What prints?
print("A" + "\n" + "B")            # Prediction: ?

# Error or not?
# print("unterminated \")           # Issue: ?

# What does this produce?
print("\x48\x65\x6c\x6c\x6f")      # Prediction: ?

# Explain this:
print(len("\n\t\\\'\"\r"))          # Prediction: ?



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Progress bar using \r (carriage return).
# Build a text-based progress bar that:
#   1. Shows a bar: [████████░░░░░░░░░░░░] 40% (4/10)
#   2. Updates IN PLACE using \r (overwrites the same line)
#   3. Runs for 10 steps (0 to 10)
#   4. Shows "Done!" at the end on a new line
#
# Bar format:
#   [filled_chars + empty_chars] percentage% (current/total)
#   Total bar width: 20 characters
#   Filled: use "█" (\u2588)
#   Empty:  use "░" (\u2591)
#
# Use time.sleep(0.3) between steps.
# Use print(..., end="\r") to overwrite.

import time
total = 10
bar_width = 20

# Write the progress bar loop manually (no loops yet -
# write print statements for steps 0, 2, 4, 6, 8, 10
# or use range() if you know it from previous exposure)



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Multi-part: special characters in real data processing.
#
# Part A: Email body formatter
# Create a properly formatted email body string using \n.
# The email should have:
#   - Subject line (not part of body but label it)
#   - Blank line after greeting
#   - Paragraph with \n between sentences
#   - Blank line before signature
#   - Signature block
# Store as ONE string variable. Print it. Check len().
# Use repr() to verify \n placement.
#
# Part B: Log file parser
# Given this log string (with \n between entries and \t between fields):

log = ("2024-03-15\t14:30:22\tINFO\tServer started\n"
       "2024-03-15\t14:30:45\tERROR\tDatabase connection failed\n"
       "2024-03-15\t14:31:00\tINFO\tRetrying connection\n"
       "2024-03-15\t14:31:05\tERROR\tRetry 1 failed\n"
       "2024-03-15\t14:31:10\tWARNING\tHigh memory usage\n"
       "2024-03-15\t14:31:15\tINFO\tConnection restored")

# Tasks:
#   1. Split into individual log entries (split on \n)
#   2. For each entry, split into fields (split on \t)
#   3. Count entries by level (INFO, ERROR, WARNING)
#      (do it manually for each level using .count() on the whole log)
#   4. Find all ERROR messages (check if "\tERROR\t" in line)
#   5. Convert the log to CSV format:
#      replace \t with "," for each line
#   6. Print a summary:
#      "Total entries: X | INFO: Y | ERROR: Z | WARNING: W"
#
# Part C: Unicode message
# Create a scientifically formatted string using Unicode:
# "DNA Analysis Results\n"
# "Sequence length: 42 bp\n"
# "GC Content: 52.4%\n"
# "Temperature: 72°C\n"    ← use \u00b0
# "Status: ✓ Valid ORF\n"  ← use \u2713
# "Direction: 5'→3'\n"    ← use \u2192
# Print it and verify with repr().



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Multi-part challenge: complete special character mastery.
#
# Part A: String archaeology
# Given the following string (shown as repr output):
# 'Hello\tWorld\n\n\tPython\t\tProgramming\n'
# Without running it:
#   1. How many characters does it contain? Calculate manually.
#   2. What is at index 5? index 11? index 12?
#   3. What does split("\n") produce? How many elements?
#   4. What does split("\t") produce? How many elements?
#   5. What does strip() produce?
# Then create this string in code and verify all your answers.
#
# Part B: Character frequency analysis
# Given this text with special characters:
text = ("Python\tis\tgreat!\n"
        "I\tlove\tcoding.\n"
        "Do\tyou\tcode?\n"
        "Yes!\tI\tdo.\n")

# Count:
#   - Number of \n characters
#   - Number of \t characters
#   - Number of regular spaces (there are none but verify)
#   - Number of letters (total - special chars - punctuation)
#   - Number of words (split on whitespace including \t and \n)
# Print a summary.
#
# Part C: Encoding and decoding
# Create a simple "encoding" that replaces:
#   spaces with \t
#   vowels (a,e,i,o,u) with their \xNN hex equivalent:
#     a → \x61, e → \x65, i → \x69, o → \x6f, u → \x75
#   Wait - those ARE the vowels! Let's shift them:
#     a → \x62 (b), e → \x66 (f), i → \x6a (j),
#     o → \x70 (p), u → \x76 (v)
# Apply this encoding to "hello world" using .replace():
#   1. Replace spaces with \t
#   2. Replace each vowel with the shifted character
# Print encoded. Then reverse the process to decode.
# Verify: decode(encode(text)) == text.lower()
#
# Part D: Build a Unicode art banner
# Using Unicode characters and \n, create this banner:
# ╔══════════════════════════╗
# ║    🐍 Python Course 🐍   ║
# ║    ─────────────────     ║
# ║    Module 02: Strings    ║
# ╚══════════════════════════╝
# Hint: ╔ = \u2554, ═ = \u2550, ╗ = \u2557
#       ║ = \u2551, ╚ = \u255a, ╝ = \u255d
#       ─ = \u2500, 🐍 = \U0001F40D
# Store as ONE string with \n between lines. Print it.