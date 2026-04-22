# ============================================================
# MODULE 02 | EXERCISES 17 - len()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Find the length of each string below using len().
# Print the result with a descriptive label.
# Before running, PREDICT each length as a comment.

word1 = "Python"
word2 = "Hello World"
word3 = "a"
word4 = ""
word5 = "   "
# Predictions:
# word1: ?    word2: ?    word3: ?    word4: ?    word5: ?



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# For each string below:
#   - Print its length
#   - Print its last character using len() (not negative index)
#   - Print its last character using negative index
#   - Verify they are equal with ==

word1 = "Bioinformatics"
word2 = "cat"
word3 = "X"



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Ask the user to input their name.
# Print:
#   - The length of their name
#   - The first character
#   - The last character
# Use len() for the last character (not [-1]).
# Label each output clearly.



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use len() to check: are these two strings the same length?
# Print True or False for each pair.
# Also print the length of each string.

pair1_a = "cat"
pair1_b = "dog"

pair2_a = "Python"
pair2_b = "Django"

pair3_a = "Hello"
pair3_b = "Hi"



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output of each line BEFORE running.
# Write predictions as comments, then verify.

word = "Genetics"
# Prediction: ?
print(len(word))
# Prediction: ?
print(len(word) - 1)
# Prediction: ?
print(word[len(word) - 1])
# Prediction: ?
print(word[len(word) - 1] == word[-1])
# Prediction: ?
print(len(word) % 2)



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use len() to find and print:
#   - The middle character of an ODD-length string
#   - The two middle characters of an EVEN-length string
# Use the formula: middle = len(word) // 2

word_odd  = "racecar"     # length 7 → true middle exists
word_even = "Python"      # length 6 → two middle chars



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use len() combined with slicing to:
#   - Print the first half of each string
#   - Print the second half of each string
# Use len() // 2 to calculate the split point.

word1 = "Python"
word2 = "Bioinformatics"
word3 = "abcdefgh"



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Count the number of digits in these numbers
# using len() and str().
# Print: "The number X has N digits."

num1 = 42
num2 = 1000000
num3 = 9876543210
num4 = 7



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Validate the strings below using len().
# For each string, check:
#   a) Is it empty? (length == 0)
#   b) Is it exactly 6 characters? (valid password length for this exercise)
#   c) Is it longer than 10 characters?
# Print a summary for each string with all three answers.

string1 = ""
string2 = "abc123"
string3 = "toolongpassword"
string4 = "Hi"



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Given the DNA sequence below:
# Use len() to:
#   - Print the total length
#   - Check if it's divisible by 3 (complete codons)
#   - Print how many complete codons it contains (length // 3)
#   - Print the first codon using len()-based slicing
#   - Print the last codon using len()-based slicing
#     (Hint: last codon starts at len(dna) - 3)

dna = "ATGCCCGCATTAGTCGA"



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Use len() to truncate a long string.
# Given the title below:
#   - If longer than 25 characters: print first 25 chars + "..."
#   - If exactly 25 characters: print as is
#   - If shorter than 25 characters: print as is
# Then do the same for title2 and title3.

title1 = "Introduction to Python Programming"
title2 = "Python"
title3 = "Introduction to Python Pro"



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL the errors in the code below.
# Write what each error is as a comment.
# Then fix all errors so the code runs correctly.

word = "Python"
print(word[len(word)])          # Error: ?
print("Length: " + len(word))   # Error: ?
print(len(123))                 # Error: ?
print(len())                    # Error: ?



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Use len() to split a string into THREE equal parts.
# If the string cannot be split into exactly 3 equal parts,
# print a message saying so.
# Test with all three strings below.
#
# For strings that CAN be split:
# Print each part with a label (Part 1, Part 2, Part 3).

string1 = "abcdefghi"     # length 9  → divisible by 3 ✅
string2 = "abcdefghij"    # length 10 → NOT divisible by 3 ❌
string3 = "PythonRocks"   # length 11 → NOT divisible by 3 ❌ wait, check!
# Hint: check len() % 3 == 0 before splitting



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a simple text centering function using len().
# (We haven't learned functions yet - just write the logic directly)
#
# Given a word and a total width of 30 characters:
#   - Calculate how many spaces are needed on each side
#   - If the remaining spaces are odd, put the extra space on the right
#   - Print the word centered within 30 characters
#   - Surround with | on each side to make it visible
#
# Do this for all three words below.
# Example output for "Python" in width 30:
#   |            Python            |
#   (verify: total between | | is 30 characters)

width = 30
word1 = "Python"
word2 = "Hi"
word3 = "Bioinformatics"
# Hint:
#   total_spaces = width - len(word)
#   left_spaces  = total_spaces // 2
#   right_spaces = total_spaces - left_spaces  (handles odd remainder)



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# This is a multi-part challenge combining len() with
# everything you have learned so far.
#
# Part A:
# Given: sentence = "The quick brown fox jumps over the lazy dog"
# Using len() and slicing:
#   - Print the total character count
#   - Print the first 10 characters
#   - Print the last 10 characters
#   - Print the middle 10 characters
#     (centered around len(sentence) // 2)
#   - Print every other character of the whole sentence
#
# Part B:
# Given: word = "Bioinformatics"
# Using ONLY len(), indexing, and slicing (no other methods yet):
#   - Print the word forwards
#   - Print the word backwards
#   - Print the word with first and last character swapped
#     (Hint: last_char + middle_slice + first_char)
#   - Check if the word is a palindrome (it isn't, but verify!)
#
# Part C:
# Given two strings:
#   s1 = "Python"
#   s2 = "Monty"
# Without using any comparison of the strings themselves,
# using ONLY len():
#   - Print which string is longer
#   - Print the difference in length
#   - Slice the longer string so it becomes the same length
#     as the shorter one (take from the beginning)
#   - Then check if the sliced version equals the shorter string