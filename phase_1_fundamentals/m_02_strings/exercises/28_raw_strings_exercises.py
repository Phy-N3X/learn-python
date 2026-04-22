# ============================================================
# MODULE 02 | EXERCISES 28 - Raw Strings
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Compare regular strings with raw strings.
# For each pair, predict what will print BEFORE running.
# Use repr() and len() to verify.

# Pair 1:
a = "Hello\nWorld"
b = r"Hello\nWorld"
# Prediction: same output? same length?

# Pair 2:
c = "\t"
d = r"\t"
# Prediction: same output? same length?

# Pair 3:
e = "C:\\Users\\Anna"
f = r"C:\Users\Anna"
# Prediction: same output? same length? are they equal?

# For each pair:
# - print both
# - print repr() of both
# - print len() of both
# - print whether they are equal (==)



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Fix the Windows paths below.
# Each path is currently WRONG because of escape sequences.
# Fix each path TWO ways:
#   Way 1: use doubled backslashes \\
#   Way 2: use raw string r"..."
# Verify both fixes give the same result using ==
# and print the corrected path.

# Hint: uncomment and run each to see what's wrong first,
# then fix.

# path1 = "C:\new_folder\test.txt"
# path2 = "C:\Users\Anna\Documents"
# path3 = "C:\temp\backup\archive.zip"
# path4 = "D:\Python\training\module2"



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate that raw strings are still str objects.
# For each raw string below:
#   - Print type()
#   - Use .upper() on it
#   - Use len()
#   - Use indexing [0] and [-1]
#   - Check if it equals its regular string equivalent

path = r"C:\Users\Anna"
pattern = r"\d+\.\d+"
text = r"Hello\nWorld"



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# The ONE limitation: raw strings cannot end with single backslash.
#
# Part A: Explain why this is a SyntaxError (as a comment):
# path = r"C:\Users\Anna\"
#
# Part B: Show THREE different workarounds for:
# "I need the path C:\Users\Anna\ (with trailing backslash)"
#
# Workaround 1: raw string + concatenation
# Workaround 2: doubled backslashes throughout
# Workaround 3: raw string + replace or other method
# Print all three results and verify they are equal.



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Raw strings with triple quotes.
# Create raw triple-quoted strings and explore their behavior.

# Part A: Create this multi-line raw string and print it:
# Line 1: \n is not a newline here
# Line 2: \t is not a tab here
# Line 3: \\ is two characters here
# (The ACTUAL line breaks between lines still work!)

# Part B: Show that actual line breaks in the source
# ARE preserved in raw triple-quoted strings.

# Part C: What is the len() of r"\n\t\\"?
# Predict first, then verify.



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Predict the output of each line BEFORE running.
# This tests your understanding of raw vs regular strings.
# Write detailed predictions as comments.

# Prediction: ?
print(r"\n")

# Prediction: ?
print(len(r"\n\t\\"))

# Prediction: ?
print(r"\n" == "\\n")

# Prediction: ?
print(r"Hello\nWorld".split("\n"))

# Prediction: ?
print(r"Hello\nWorld".split("\\n"))

# Prediction: ?
path = r"C:\Users\Anna"
print(path.split("\\"))

# Prediction: ?
print(r"test".upper())

# Prediction: ?
print(repr(r"\t"))



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Raw f-strings (rf"...").
# Combine raw strings with f-string variable insertion.
# For each task, use rf"..." syntax.

username = "anna_k"
folder = "Documents"
filename = "report"

# a) Build a Windows path dynamically:
#    Expected: C:\Users\anna_k\Documents\report.pdf
#    (use rf"..." with the variables above)

# b) Build a message with literal \n (NOT a newline):
#    Expected: Hello anna_k\nWelcome to the system!
#    (the \n should appear literally in output)

# c) Build a regex-like description:
#    Expected: Pattern for anna_k: \w+@\w+\.\w+
#    (backslashes should be literal)

# For each: print the result and verify \n is NOT a newline.



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Raw strings with string operations.
# Apply various string methods to raw strings.
# Show that they work exactly like regular strings.

path = r"C:\Users\Anna\Documents\Python\report.pdf"

# a) Split on "\\" to get path components
#    (What character are you splitting on?)

# b) Use .endswith() to check file extension

# c) Use .replace() to convert to Unix path (\ → /)

# d) Use .find() to locate "Anna"

# e) Use .count() to count backslashes

# f) Use indexing to get the first and last character

# g) Use slicing to get just the filename (everything after last \)
#    Hint: use .rfind("\\") + 1



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Compare raw and regular string behavior in split().
# This reveals something important about raw strings.

# Given this text - it looks like it has \n separators:
text_raw     = r"Line1\nLine2\nLine3"
text_regular = "Line1\nLine2\nLine3"

# Part A:
# Print both strings. What do you see?
# Use repr() to show what they really contain.

# Part B:
# Split text_regular on "\n" - how many parts?
# Split text_raw on "\n"    - how many parts? Explain.
# Split text_raw on "\\n"   - how many parts? Explain.

# Part C:
# Replace "\n" in text_regular with "|" - what happens?
# Replace "\n" in text_raw with "|"     - what happens?
# Replace "\\n" in text_raw with "|"    - what happens?

# Part D:
# How many "lines" does .count("\n") find in each?
# How many "lines" does .count("\\n") find in each?
# Write a comment explaining the pattern you observe.



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# File path operations using raw strings.
# Given these file paths, perform the operations described.

paths = [
    r"C:\Users\Anna\Documents\report.pdf",
    r"C:\Users\Anna\Pictures\holiday.jpg",
    r"C:\Program Files\Python 3.11\python.exe",
    r"D:\Projects\BioInfo\data\genome.fasta",
    r"C:\Windows\System32\drivers\etc\hosts",
]

# For each path (access manually with index):
# a) Extract the filename (everything after the last \)
#    Use .rsplit("\\", 1)[-1] or similar
# b) Extract the file extension
# c) Extract the drive letter (first character)
# d) Count the number of directory levels (count \\)
# e) Convert to Unix format (replace \\ with /)

# Process the first two paths manually (no loops yet).



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Raw strings in regex context (preview).
# Even without knowing full regex, this exercise shows
# WHY raw strings matter for patterns.

# Compare these PAIRS of strings.
# For each pair, they should be EQUAL (same content).
# Verify with == and print the content.

# Pair 1: digit pattern
regular1 = "\\d+"
raw1 = r"\d+"
# Are they equal? What do they contain?

# Pair 2: whitespace + word
regular2 = "\\s\\w+"
raw2 = r"\s\w+"
# Are they equal? What do they contain?

# Pair 3: decimal number
regular3 = "\\d+\\.\\d+"
raw3 = r"\d+\.\d+"
# Are they equal? What do they contain?

# Pair 4: email-like pattern
regular4 = "[\\w\\.]+@[\\w\\.]+\\.\\w+"
raw4 = r"[\w\.]+@[\w\.]+\.\w+"
# Are they equal? Which is easier to read?

# For each pair: print both, print ==, write comment on readability.



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL errors and unexpected behaviors below.
# For each line write a detailed comment explaining
# what's wrong or surprising. Fix all actual errors.

# Error or surprise?
path1 = "C:\new_users\data"
print(repr(path1))              # What does this reveal?

# Error or surprise?
# path2 = r"C:\Users\Anna\"    # What's wrong here?

# Error or surprise?
text = r"Hello\nWorld"
print(text.split("\n"))         # How many parts? Why?

# Error or surprise?
raw = r"\n"
normal = "\n"
print(raw == normal)            # True or False? Explain.
print(len(raw), len(normal))    # What are the lengths?

# Error or surprise?
print(r"\")                     # What happens? Why?

# Error or surprise?
result = r"test" + "\n" + r"test"
print(repr(result))             # What does this contain?



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Deep understanding: raw strings and repr().
#
# For each string below:
#   1. Write what repr() will show (predict!)
#   2. Write the len() (predict!)
#   3. Run and verify
#   4. Write explanation as comment

s1 = r"\n\t\\"
s2 = "\n\t\\"
s3 = "\\n\\t\\\\"
s4 = r"C:\Users\Anna"
s5 = "C:\\Users\\Anna"
s6 = r"\u03b1"          # NOT the alpha character!
s7 = "\u03b1"           # IS the alpha character!

# For each: predict repr(), predict len(), run, verify, explain.
# Final question: which pairs are equal (==)?



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a path manipulation library using raw strings.
# (No loops - work with specific paths)
#
# Given these Windows paths:
path1 = r"C:\Users\Anna\Documents\Python\lecture1.py"
path2 = r"C:\Users\Anna\Documents\Data\genome.fasta"
path3 = r"D:\Projects\BioInfo\src\analysis.py"
path4 = r"C:\Program Files\Python 3.11\Lib\os.py"

# For each path, implement these operations:
#
# Part A: Decomposition
# Split each path into: drive, directories, filename, extension
# Example for path1:
#   Drive: C:
#   Dirs: ['Users', 'Anna', 'Documents', 'Python']
#   Filename: lecture1
#   Extension: .py
#
# Part B: Path manipulation
# For path1: create the sibling path (same directory, different file):
#   r"C:\Users\Anna\Documents\Python\lecture2.py"
# Hint: split, modify last component, rejoin with "\\"
#
# Part C: Path comparison
# Which paths share the same drive? (Compare first 2 chars)
# Which paths are Python files? (endswith ".py")
# Which paths are under C:\Users? (startswith r"C:\Users")
#
# Part D: Unix conversion
# Convert all paths to Unix format:
#   Remove drive letter and colon
#   Replace \\ with /
# Expected for path1: /Users/Anna/Documents/Python/lecture1.py



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Multi-part challenge: raw strings mastery.
#
# Part A: The repr() roundtrip
# For a regular string s, repr(s) shows the string as it
# would appear in Python source code.
# Verify this for these strings:
strings = [
    "Hello\nWorld",
    "C:\\Users\\Anna",
    "\t\t\tIndented",
    "Quote: \"hello\"",
    "Unicode: \u03b1",
]
# For each: print(repr(s)) and then verify that
# eval(repr(s)) == s  (eval converts the repr back to string)
# This proves repr() gives you valid Python source code!
# Print: "eval(repr(s)) == s: True/False" for each.
#
# Part B: String archaeology from repr()
# You are given these repr() outputs.
# What is the ACTUAL content of each string?
# What would print(s) show?
# What is len(s)?
# Write answers as comments, then create and verify each.

repr1 = r"'Hello\\nWorld'"        # (this is the repr output, not code)
repr2 = r"'C:\\\\Users\\\\Anna'"  # (repr output)
repr3 = r"'\t\t\tPython'"         # (repr output)
# Hint: repr output shows strings as they appear in code.
# 'Hello\\nWorld' means the string contains: Hello\nWorld (with literal \n)

# Part C: Raw string quiz
# For each, write True or False and WHY (as a comment):

# Q1: r"\n" == "\n"
# Q2: r"\n" == "\\n"
# Q3: len(r"\n") == len("\n")
# Q4: len(r"\\") == len("\\")
# Q5: r"hello" == "hello"
# Q6: r"\t\n" == "\\t\\n"
# Q7: r"test\\" ends with one backslash
# Q8: You can use r"..." and regular "..." strings
#     interchangeably when there are no backslashes
# Verify each with Python after writing your prediction.
#
# Part D: Real-world application
# You are building a bioinformatics pipeline that needs to:
#   1. Handle Windows paths for data files
#   2. Use regex to validate DNA sequences
#   3. Use regex to find restriction sites
#   4. Convert paths between Windows and Unix format
#
# Create these components using raw strings:
#
#   data_path    = Windows path to: D:\BioData\Project1\sequences\
#                  (trailing backslash needed → use workaround!)
#   valid_dna    = regex pattern: only A, T, G, C, one or more
#   ecori_site   = regex pattern: GAATTC
#   codon_pattern = regex pattern: any 3 nucleotides [ATGC]{3}
#
# Then demonstrate:
#   - Using the path with a filename appended
#   - Testing the DNA pattern against "ATGCCC" and "ATGXYZ"
#     (just use re.fullmatch(pattern, string) and print result)
#   - Converting the data_path to Unix format