# ============================================================
# MODULE 02 | EXERCISES 18 - .upper() and .lower()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Apply .upper() and .lower() to each string below.
# Print the original, uppercase, and lowercase version.
# Label each output clearly.

word1 = "Python"
word2 = "BIOINFORMATICS"
word3 = "hElLo WoRlD"



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate that methods do NOT modify the original string.
# Create: word = "Hello"
# Call word.upper() WITHOUT storing the result.
# Print word - what do you see?
# Then fix it by storing the result correctly.
# Write a comment explaining what happened.



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Use .isupper() and .islower() to check each string.
# Print: "'string' isupper: True/False   islower: True/False"

word1 = "PYTHON"
word2 = "python"
word3 = "Python"
word4 = "PYTHON123"
word5 = "123"
word6 = ""



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output of each line BEFORE running.
# Write predictions as comments, then verify.

word = "Hello World 123!"
# Prediction: ?
print(word.upper())
# Prediction: ?
print(word.lower())
# Prediction: ?
print(word.upper().lower())
# Prediction: ?
print(len(word) == len(word.upper()))
# Prediction: ?
print(word.upper().isupper())



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Apply .capitalize() and .title() to each string below.
# Print both results and write a comment explaining
# the difference between them.

sentence1 = "hello world"
sentence2 = "the quick brown fox"
sentence3 = "HELLO WORLD"
sentence4 = "hElLo WoRlD"



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Ask the user to type a word.
# Print the word in all 5 forms:
#   - original
#   - uppercase
#   - lowercase
#   - capitalized
#   - title case
# Label each output.



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Case-insensitive comparison.
# Ask the user to enter their favorite programming language.
# Check (case-insensitively) if it equals "python".
# If yes: print "Great choice!"
# If no:  print "Interesting! Have you tried Python?"
# The check must work regardless of capitalization.
# Test it with: python, PYTHON, Python, pYtHoN



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use method chaining to normalize these messy strings.
# For each string:
#   Step 1: convert to lowercase
#   Step 2: convert to title case
# Do it in ONE line using chaining.
# Print the result.

messy1 = "THE QUICK BROWN FOX"
messy2 = "hElLo WoRlD"
messy3 = "introduction TO bioinformatics"



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# DNA sequences should always be in uppercase.
# Given the sequences below:
#   - Check if each is already uppercase using .isupper()
#   - If yes: print "OK: " + sequence
#   - If no:  print "Fixed: " + corrected uppercase version
# Do this for all four sequences.

dna1 = "ATGCCCGCA"
dna2 = "atgcccgca"
dna3 = "AtGcCcGcA"
dna4 = "ATGCCC123"



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Generate a username and email from a person's name.
# Given: first_name and last_name (in any case)
# Rules:
#   - username = first_name + last_name, all lowercase
#   - email    = username + "@university.edu", all lowercase
#   - display  = first_name + " " + last_name, title case
# Print all three with labels.
# Test with these inputs:
#   first_name = "ANNA"
#   last_name  = "kowalska"

first_name = "ANNA"
last_name  = "kowalska"



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Use .swapcase() creatively.
# Given the strings below:
#   - Print the swapcased version
#   - Verify that applying .swapcase() TWICE gives back the original
#     (use == and print True/False)
#   - Find a string where .swapcase() gives the SAME result as .upper()
#     (think: what kind of string would that be?)
#   - Write your answer as a comment

word1 = "Hello World"
word2 = "PyThOn"
word3 = "BIOINFORMATICS"



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL the errors in the code below.
# Write what each error is as a comment.
# Then fix all errors so the code runs correctly
# and produces meaningful output.

word = "hello"
word.Upper()                        # Error: ?
result = word.upper
print(result)                       # Error: ?
print("hello".upper() + 123)        # Error: ?
print(word.upper().isupper)         # Error: ?



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Build a simple password validator using case methods.
# Given a password string, check ALL of the following:
#   a) Is it at least 8 characters long?
#   b) Is it NOT all lowercase? (i.e., has some uppercase)
#   c) Is it NOT all uppercase? (i.e., has some lowercase)
#   d) Does the uppercase version differ from the lowercase version?
#      (This means: it contains at least one letter)
#
# Print the result of each check (True/False) with a label.
# Then print: "Strong password" if ALL checks pass, else "Weak password"
#
# Test with:
#   password1 = "abc123"         (too short)
#   password2 = "ABCDEFGH"       (all uppercase)
#   password3 = "abcdefgh"       (all lowercase)
#   password4 = "12345678"       (no letters)
#   password5 = "Abc12345"       (should pass all checks)



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a Caesar cipher encoder using only what we know so far.
# (A Caesar cipher shifts each letter by a fixed amount)
#
# We'll do a simplified version: ROT-CASE cipher
# Rules:
#   - If a letter is LOWERCASE → convert to UPPERCASE
#   - If a letter is UPPERCASE → convert to LOWERCASE
#   - Non-letter characters → leave unchanged
#
# This is actually just .swapcase()! But do it MANUALLY:
# Given the message below, go character by character using indexing
# (no loops - do the first 8 characters manually)
# and build the encoded string using concatenation.
# Compare your result with message.swapcase() to verify.
#
# message = "HeLLo WoRLD!"
# Expected: hEllO wOrld!

message = "HeLLo WoRLD!"



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# This is a multi-part challenge.
#
# Part A:
# Write a "title normalizer" for book titles.
# Some words in titles should NOT be capitalized
# (articles, prepositions) unless they are the first word.
# Words that stay lowercase: "a", "an", "the", "of", "in",
#                             "on", "at", "to", "and", "or"
#
# Given: title = "the introduction to the art of programming"
# Expected: "The Introduction to the Art of Programming"
#
# Without loops, do it manually for this specific title:
#   1. Split the title into words (preview: use .split() - or
#      just hardcode the positions using slicing for now)
#   2. Capitalize the first word always
#   3. For the rest: check if the word is in the "small words" list
#      and apply .lower() or .capitalize() accordingly
#
# Hint: since we haven't covered loops, work with the specific
# words in this title manually - it's OK to hardcode word positions.
# The goal is to practice using the case methods creatively.
#
# Part B:
# Given a string, determine which "mode" it's in:
#   - "UPPER MODE"     if isupper() is True
#   - "lower mode"     if islower() is True
#   - "Title Mode"     if it equals its own .title() version
#   - "Capitalized"    if it equals its own .capitalize() version
#   - "Mixed"          if none of the above
#
# Test with these strings and print the mode for each:
strings = ["HELLO WORLD", "hello world", "Hello World",
           "Hello world", "hElLo WoRlD"]