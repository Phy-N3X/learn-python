# ============================================================
# MODULE 02 | EXERCISES 19 - .strip(), .lstrip(), .rstrip()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Apply .strip(), .lstrip(), and .rstrip() to the string below.
# Print the result of each method AND its length.
# Add a comment explaining what each method removed.

text = "   Hello World   "



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate that .strip() does NOT touch the middle.
# Given the string below:
#   - Print the original
#   - Print after .strip()
#   - Print the length before and after
# Write a comment explaining what was and wasn't removed.

text = "   Hello   World   "



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output of each line BEFORE running.
# Write predictions as comments, then verify.
# Use repr() to make whitespace visible.

text = "\t\n  Python  \n\t"
# Prediction: ?
print(repr(text.strip()))
# Prediction: ?
print(repr(text.lstrip()))
# Prediction: ?
print(repr(text.rstrip()))
# Prediction: ?
print(len(text))
# Prediction: ?
print(len(text.strip()))



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate the common beginner mistake:
# calling .strip() without storing the result.
#
# Part A: Show the mistake - call .strip() without storing,
#         then print the original. Show it's unchanged.
# Part B: Fix it by storing the result correctly.
# Part C: Fix it by reassigning the variable.
# Write a comment explaining what happened in Part A.

text = "   Hello   "



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Strip specific characters (not whitespace).
# Apply the appropriate strip method to each case
# and print the result.

word1 = "###Python###"           # strip all #
word2 = "...Hello..."            # strip all .
word3 = "***important***"        # strip all *
word4 = "###***Hello***###"      # strip both # and *
word5 = "000042"                 # remove leading zeros only
word6 = '"Hello World"'          # remove surrounding quotes



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# These two strings LOOK the same but are not equal.
# Use repr() to find the hidden difference.
# Then fix the comparison using .strip() so it returns True.
# Print the repr of each string before fixing.

string1 = "Python"
string2 = "Python   "

print(string1 == string2)   # currently False
# Use repr() to diagnose the problem:
# Then fix with strip and verify:



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Simulate user input cleaning.
# The strings below represent what a user might type
# (with accidental spaces).
# For each one:
#   - Print the "raw" value with repr()
#   - Clean it with .strip().lower()
#   - Check if it equals the expected value
#   - Print True or False

raw1 = "  Python  "        # expected: "python"
raw2 = "  YES  "           # expected: "yes"
raw3 = "\tBioinformatics\n"# expected: "bioinformatics"
raw4 = "  42  "            # expected: "42"



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use .strip() to check for empty input.
# The strings below represent user inputs.
# For each one, check if it is "effectively empty"
# (empty after stripping).
# Print: "'raw_value' → empty: True/False"

inputs = ["", "   ", "\t\n", "Hello", "  a  ", "\n\n\n"]
# Do each manually (no loops yet).



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Clean and normalize these "raw" name inputs.
# For each name:
#   Step 1: .strip()     → remove accidental whitespace
#   Step 2: .lower()     → normalize case
#   Step 3: .title()     → proper capitalization
# Do it in ONE chained expression.
# Print the result.

name1 = "  ANNA KOWALSKA  "
name2 = "\tjan NOWAK\n"
name3 = "   maria   WIŚNIEWSKA   "
name4 = "  PIOTR kowalczyk  "



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Parse a simple "key: value" configuration string.
# Given the raw config line below:
#   - Find the position of the colon using .index(":")
#     (we cover .index() in detail in Lecture 11)
#   - Extract the key using slicing: everything before the colon
#   - Extract the value using slicing: everything after the colon
#   - Strip BOTH key and value to remove any extra whitespace
#   - Print: "Key: 'key' | Value: 'value'"

config1 = "  username  :  anna_kowalska  "
config2 = "  max_attempts  :  3  "
config3 = "  debug_mode  :  True  "



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Simulate reading lines from a file.
# Each string below represents a line that was read from a file.
# Each line has a "\n" at the end (as real file lines do).
# Clean each line using the most appropriate strip method:
#   - Remove ONLY the trailing newline (use .rstrip("\n"))
#   - Print the cleaned line
#   - Print its length before and after cleaning

lines = [
    "Anna Kowalska\n",
    "  Jan Nowak  \n",
    "Python Programming\n",
    "\tBioinformatics\t\n",
]
# Do each manually (no loops yet).



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL errors and unexpected behaviors in the code below.
# For each line, write a comment explaining:
#   a) Is it an error? If so, what kind?
#   b) If not an error, is the output what you'd expect?
# Then fix all actual errors.

text = "   Hello   "
text.strip()                        # Issue: ?
print(text)                         # What prints here?

print("Hello".strip("Hello"))       # What does this print?
print("   ".strip())                # What does this print?
print(len("   ".strip()))           # What does this print?

word = "aabbccHelloaabbcc"
print(word.strip("abc"))            # What does this print? Explain.



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Build a "text cleaner" that processes messy data.
# Given the list of raw data strings below,
# clean each entry manually (no loops - do each individually):
#   1. Strip all whitespace
#   2. Remove any leading/trailing # or * characters
#      (use strip with the characters argument)
#   3. Convert to title case
#   4. Check if the result is empty after cleaning
#      (if so, print "EMPTY ENTRY" instead)
# Print the cleaned version of each entry.

entry1 = "  ###  python programming  ###  "
entry2 = "  ***  bioinformatics  ***  "
entry3 = "  ###***###  "              # this one should be empty after cleaning!
entry4 = "\t***  data science  ***\n"
entry5 = "  ###  MACHINE LEARNING  "



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# This exercise tests deep understanding of strip behavior.
#
# Part A:
# Explain (as comments) exactly what happens step by step
# when Python executes: "abcXYZcba".strip("abc")
# Which characters are removed and in what order?
# Verify by running and checking the result.
#
# Part B:
# Predict the output of each of these (without running first):

word = "abacabacHelloabacabac"
# Prediction: ?
print(word.strip("abc"))
# Prediction: ?
print(word.lstrip("abc"))
# Prediction: ?
print(word.rstrip("abc"))

# Part C:
# Why does this NOT remove the word "Hello"?
word2 = "HelloWorldHello"
print(word2.strip("Hello"))     # What prints? Why?
# Write a detailed explanation as a comment.
#
# Part D:
# Find a string and a strip argument where lstrip and rstrip
# give the SAME result. Explain why.



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Multi-part challenge: build a complete input validator.
#
# Part A:
# Write validation logic for a username input.
# Given a raw username string:
#   1. Strip whitespace
#   2. Check it's not empty (after stripping)
#   3. Check it's at least 3 characters long
#   4. Check it's at most 20 characters long
#   5. Check the first character is a letter
#      (use .isalpha() on the first character - new method preview!)
#   6. Convert to lowercase for storage
# Print a summary of all checks (True/False) and the
# final stored value (or "INVALID" if any check failed).
#
# Test with:
raw1 = "  Anna_K  "           # should pass all
raw2 = "  "                   # fails: empty
raw3 = "  Ab  "               # fails: too short
raw4 = "  " + "a" * 25 + "  "  # fails: too long
raw5 = "  123username  "      # fails: starts with digit
#
# Part B:
# Use repr() to display the "before" and "after" state
# of each raw input, so you can clearly see what was stripped.
#
# Part C:
# Given two cleaned usernames, check if they are the same
# (case-insensitive, stripped).
# Print True or False.
user_a = "  AnnaK  "
user_b = "annak"