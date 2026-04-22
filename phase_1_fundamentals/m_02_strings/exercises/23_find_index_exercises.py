# ============================================================
# MODULE 02 | EXERCISES 23 - .find() and .index()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Use .find() to locate substrings in the text below.
# Print the position of each. If not found, print a message.

text = "Python programming is fun and Python is powerful"

# Find: "Python" (first occurrence)
# Find: "programming"
# Find: "fun"
# Find: "Java"
# Find: "is"



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate the difference between .find() and .index()
# when the substring is NOT found.
#
# Part A: Use .find() on a substring that doesn't exist.
#         Print the result. Does it crash?
#
# Part B: Use .index() on the same substring.
#         Write what happens as a comment BEFORE running.
#         Then run and verify.
#
# Part C: Use .index() on a substring that DOES exist.
#         Show it works the same as .find() in this case.

text = "Hello World Python"
search = "Java"



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output of each line BEFORE running.
# Write predictions as comments, then verify.

text = "the cat sat on the mat"
# Prediction: ?
print(text.find("the"))
# Prediction: ?
print(text.find("cat"))
# Prediction: ?
print(text.find("at"))
# Prediction: ?
print(text.rfind("the"))
# Prediction: ?
print(text.rfind("at"))
# Prediction: ?
print(text.find("dog"))
# Prediction: ?
print(text.find("the", 5))
# Prediction: ?
print(text.find("at", 0, 10))



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate case sensitivity of .find().
# For each search term, try finding it in both
# its original case AND uppercase/lowercase version.
# Print the results and write a comment explaining
# what you observe.

text = "Hello World Python"
# Find "hello", "Hello", "HELLO"
# Find "world", "World", "WORLD"
# Then find using .lower() trick for case-insensitive search.



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Use .find() to split a string at a found position.
# Given the strings below, find the separator and use
# the position to extract the two parts with slicing.

# a) Split "name:Anna" at ":"
#    Expected: key="name", value="Anna"

# b) Split "score = 95" at " = "
#    Expected: key="score", value="95"

# c) Split "Python -> programming" at " -> "
#    Expected: left="Python", right="programming"



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Parse an email address using .find() and slicing.
# For each email below, extract:
#   - username (before @)
#   - full domain (after @)
#   - domain name (between @ and last .)
#   - TLD - top level domain (after last .)
# Print each part with a label.

email1 = "anna.kowalska@university.edu"
email2 = "jan.nowak@gmail.com"
email3 = "info@bioinformatics.org"



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use .rfind() to extract file extensions correctly.
# Some filenames have multiple dots - rfind handles this!
# For each filename, extract:
#   - name (everything before last dot)
#   - extension (everything after last dot)
# Print both with labels.

file1 = "report.pdf"
file2 = "genome_data.fasta"
file3 = "my.important.report.final.docx"
file4 = "archive.tar.gz"
file5 = "script.v2.test.py"



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Find multiple occurrences using .find() with start parameter.
# For the text below, find ALL occurrences of "the" manually
# (without loops - find each one by starting after the previous).
# Print each position.
# When no more are found (-1), stop.
# Also count how many you found.

text = "the cat sat on the mat near the fence by the tree"



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Extract content between markers using .find().
#
# Part A: Extract text between [ and ]:
text1 = "Result: [SUCCESS] - operation completed"
# Expected: "SUCCESS"

# Part B: Extract text between ( and ):
text2 = "function_call(param1, param2) returns value"
# Expected: "param1, param2"

# Part C: Extract text between <title> and </title>:
text3 = "<html><head><title>Python Tutorial</title></head></html>"
# Expected: "Python Tutorial"
# Hint: find the > after <title>, then find < before </title>

# Part D: Extract text between the first and second comma:
text4 = "Anna, Kowalska, 25, Warsaw"
# Expected: " Kowalska"



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# DNA restriction site analysis using .find().
#
# A restriction enzyme cuts DNA at its recognition sequence.
# Given the DNA sequence below:
#
# Part A: Find the position of EcoRI site "GAATTC"
#         Print: "EcoRI site found at position X"
#         If not found: "EcoRI site not found"
#
# Part B: Find ALL occurrences of "GAATTC" manually
#         (use .find() with start parameter repeatedly)
#         Print each position found.
#
# Part C: If EcoRI cuts between G and AATTC,
#         the actual cut happens between position X and X+1.
#         Show what the two fragments would be after cutting
#         at the FIRST site using slicing.
#
# Part D: Check if HindIII site "AAGCTT" exists in the sequence.
#         Use an appropriate method and print result.

dna = "ATGCCCGAATTCGCATTAGAATTCGTCGAAAGCTTCGA"



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Safe vs unsafe use of .find() result.
#
# Part A:
# Show the DANGEROUS behavior:
text = "Hello World"
pos = text.find("xyz")      # -1
# What does text[pos] return? Predict first, then check.
# Write a comment explaining WHY this is a bug.
#
# Part B:
# Show the SAFE pattern:
# Write proper code that checks for -1 before using the result.
# If found: print the character at that position.
# If not found: print "Substring not found".
# Test with both "World" and "xyz".
#
# Part C:
# Why is .find() returning -1 a potential trap in Python
# specifically? (Hint: think about what -1 means as an index)
# Write a detailed explanation as a comment.



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL errors and unexpected behaviors in the code below.
# Write a comment for each line explaining what's wrong.
# Then fix all actual errors.

text = "Hello World Python"

result = text.Find("World")             # Error: ?
print(result)

result2 = text.find("world")
print(result2)                          # Surprising? Explain.

result3 = text.index("Java")           # Error at runtime: ?
print(result3)

pos = text.find("World")
print(text[pos])                        # What prints? Is it correct?

# This one is the dangerous bug from Exercise 11:
pos2 = text.find("xyz")
print(text[pos2])                       # What prints? Is it what we want?



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Parse a complex structured string using .find() and slicing.
#
# The string below is a simplified HTTP request line:
# "GET /api/users/profile?id=42&token=abc123 HTTP/1.1"
#
# Extract:
#   a) The method: "GET"
#      (everything before first space)
#   b) The full path: "/api/users/profile?id=42&token=abc123"
#      (between first and last space)
#   c) The protocol: "HTTP/1.1"
#      (everything after last space)
#   d) The path without query string: "/api/users/profile"
#      (everything in path before "?")
#   e) The query string: "id=42&token=abc123"
#      (everything in path after "?")
#   f) The value of "id": "42"
#      (between "id=" and "&")
#   g) The value of "token": "abc123"
#      (after "token=")
# Print each with a label.

request = "GET /api/users/profile?id=42&token=abc123 HTTP/1.1"



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a simple template engine using .find() and slicing.
#
# A template uses {{placeholder}} syntax.
# Your task: find each placeholder and replace it with a value.
# (We know .replace() exists - this exercise builds understanding
# of HOW find+slice can achieve the same thing manually)
#
# Template: "Hello, {{name}}! You have {{count}} messages."
# Values: name="Anna", count="5"
#
# Part A:
# Manually find and replace {{name}}:
#   1. Find "{{name}}" position
#   2. Build new string: before + "Anna" + after
#
# Part B:
# Then find and replace {{count}} in the result from Part A.
#
# Part C:
# Write a comment: what does this tell you about how
# .replace() probably works internally?
#
# Part D:
# What if the placeholder appears TWICE?
# Template2: "Dear {{name}}, your code is {{code}}. Goodbye {{name}}."
# Replace {{name}} with "Anna" (both occurrences) and {{code}} with "XK9".
# Use .find() with start parameter to find the second {{name}}.

template = "Hello, {{name}}! You have {{count}} messages."
template2 = "Dear {{name}}, your code is {{code}}. Goodbye {{name}}."



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Multi-part challenge: comprehensive string search analysis.
#
# Part A:
# Given: sentence = "I love Python and Python loves me and I love coding"
# Without using .count() (next lecture!):
# Manually find ALL occurrences of "love" using .find() with start.
# Store each position in a separate variable (pos1, pos2, pos3...).
# Print each position.
# After each .find() call, check if result is -1 to stop.
# Count how many times "love" appears.
#
# Part B:
# Using the positions found in Part A:
# For each occurrence, use slicing to verify the character
# at that position is indeed the start of "love".
# Print: "Position X: 'love' verified: True/False"
#
# Part C:
# Find the position of "Python" in the sentence.
# Using only the position (no other string methods):
# Extract the word "Python" using slicing.
# Extract the 5 characters BEFORE "Python" (with slicing).
# Extract the 5 characters AFTER "Python" (with slicing).
# Print all three.
#
# Part D:
# Implement a "find between" operation:
# Given start_marker = "and" and end_marker = "and":
# Find the content BETWEEN the first "and" and the second "and".
# Use .find() with start parameter for the second search.
# Print the content between them (stripped of extra spaces).
#
# Part E:
# Compare .find() vs .rfind() on the sentence:
# For the word "I", "love", "and", "Python":
# Print the first and last position of each.
# For words that appear only once: verify first == last.
# For words that appear multiple times: show the difference.