# ============================================================
# MODULE 02 | EXERCISES 02 - Negative Indexes
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Create a variable 'animal' with the value "elephant"
# Using NEGATIVE indexing, print:
#   - the last character
#   - the second to last character
# Expected output:
#   t
#   n



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Print ALL characters of the word "Python"
# using ONLY negative indexes (-1 through -6).
# Print one character per line.
# Expected output:
#   n
#   o
#   h
#   t
#   y
#   P



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# For the string below, print the character at index -1
# using THREE different strings of different lengths.
# Observe that [-1] always gives the last character
# regardless of length.

short  = "Hi"
medium = "Python"
long_s = "Bioinformatics"
# Print word[-1] for all three and add a comment
# explaining what you observe.



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Without running the code first, predict the output.
# Write your prediction as a comment, then verify.

word = "Biology"
# Prediction: word[-1]  = ?
print(word[-1])
# Prediction: word[-3]  = ?
print(word[-3])
# Prediction: word[-7]  = ?
print(word[-7])



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Given the string "racecar":
# Using indexing (positive OR negative), print:
#   - first character
#   - last character
# Then check if they are equal using == and print the result.
# Expected output:
#   r
#   r
#   True



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# The string below represents a filename.
# Using ONLY negative indexing, print the last 3 characters
# one by one (each on separate line - no slicing yet!).
# Then combine them into a variable called 'extension'
# and print it.
# Expected output:
#   p
#   d
#   f
#   pdf

filename = "annual_report.pdf"



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# For the string "Python":
# Using the mathematical relationship:
#   word[-i] == word[-i + length]
# Verify manually (using print and ==) that:
#   word[-1] gives the same result as word[5]
#   word[-2] gives the same result as word[4]
#   word[-6] gives the same result as word[0]
# Print True/False for each comparison.



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use a variable as a negative index.
# Create: word = "Genetics"
# Create: i = -1
# Print word[i], then change i to -4, print again.
# Then use an expression: print word[-(2*2)]
# Write a comment explaining what each output is.



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a string with your full name: "FirstName LastName"
# Using a combination of POSITIVE and NEGATIVE indexes:
#   - Print the first character of your first name (positive)
#   - Print the last character of your last name (negative)
#   - Print the first character of your last name
#     (you need to find the right index - either positive or negative)
#   - Combine all three into 'initials' and print



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Given the DNA sequence below:
# Print the following using appropriate indexes:
#   - First nucleotide (positive index)
#   - Last nucleotide (negative index)
#   - Third nucleotide from the end (negative index)
#   - Check if first == last, print True or False

dna = "ATGCCCTTA"



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Find the errors in the code below.
# Write what each error is as a comment.
# Then fix the code so it runs correctly.

word = "Python"
print(word[-7])         # Error: ?
print(word[-0])         # Not an error, but what does it print?
                        # Write your observation as a comment.
print(word[-6.0])       # Error: ?



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# This exercise is about reading and predicting carefully.
# Without running the code first, predict ALL outputs.
# Write each prediction as a comment, then run and verify.

text = "Hello World"

# Prediction: ?
print(text[-1])

# Prediction: ?
print(text[-6])

# Prediction: ?
print(text[-11])

# Prediction: ?
print(text[0] == text[-11])

# Prediction: ?
print(text[4] == text[-7])

# Prediction: ?
print(text[-1] == text[-5])



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a product code string: "CAT-2024-XL"
# Using ONLY negative indexes, extract and print:
#   - The last character (size indicator)
#   - The last two characters (full size: "XL")
#     (combine them character by character - no slicing!)
#   - The dash before the size (3rd from end)
#   - The last 4 characters of the year part (positions -7 to -4)
#     (combine them character by character - no slicing!)
# Add a descriptive label to each print statement.



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Palindrome checker using only indexing.
#
# A palindrome reads the same forwards and backwards.
# "racecar" → r-a-c-e-c-a-r → same both ways.
#
# Given the string below, manually check if it is a palindrome
# by comparing:
#   position[0]  with position[-1]
#   position[1]  with position[-2]
#   position[2]  with position[-3]
#   position[3]  with position[-4]
#   (the middle character doesn't need a pair)
#
# Print each comparison (True/False).
# Then print a final conclusion as a string:
#   "Is palindrome: True" or "Is palindrome: False"
#
# Do this for BOTH words below:

word1 = "madam"
word2 = "python"



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# This is a challenge exercise combining everything so far.
#
# You are given a secret message encoded as a string.
# Each "real" character is hidden at specific positions.
#
# The message = "xPzywtzhhzoqnaz"
# The real characters are at these indexes:
#   -15, -13, -11, -7, -5, -3, -1
#   (all negative indexes)
#
# Part A:
# Extract each character at those indexes manually
# and combine them into a variable called 'decoded'.
# Print 'decoded'.
#
# Part B:
# Also extract the characters at positive indexes:
#   1, 3, 5, 9, 11, 13
# Combine them into 'decoded2' and print it.
# Are decoded and decoded2 the same? Print True/False.
#
# Part C:
# Write a comment explaining why they are (or aren't) the same,
# using what you learned about the relationship between
# positive and negative indexes.