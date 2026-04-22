# ============================================================
# MODULE 02 | EXERCISES 13 - String Indexing
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Create a variable called 'city' with the value "Warsaw"
# Print the first character of the string.
# Print the last character of the string.
# Expected output:
#   W
#   w



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Given the string below, print:
#   - character at index 0
#   - character at index 4
#   - character at index 7
# Expected output:
#   P
#   r
#   m

language = "Programming"



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Create a variable 'dna' with the value "ATCGTA"
# Print each character on a separate line using indexing.
# Do NOT use a loop - access each index manually.
# Expected output:
#   A
#   T
#   C
#   G
#   T
#   A



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# The string below has spaces in it.
# Print the character at index 2 and index 6.
# Before running - PREDICT what the output will be.
# Write your prediction as a comment first.

text = "Hi there"
# Prediction: index 2 = ?   index 6 = ?



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Create a variable with your full name as a single string.
# Example: "Anna Kowalska"
# Using indexing, print:
#   - The first letter of the first name (index 0)
#   - The first letter of the last name (you need to find the right index)
# Then combine them into a variable called 'initials' and print it.



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use a variable as the index (not a literal number).
# Create a string 'word' = "Python"
# Create a variable 'position' = 4
# Print the character at that position using the variable.
# Then change 'position' to 1 and print again.
# Expected output:
#   o
#   y



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Given the string below, print the character at index (2 * 3).
# Do NOT calculate it yourself - write the expression inside []
# Then print the character at index (10 - 7)
# Write a comment explaining what each result is.

alphabet = "abcdefghijklmnop"



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Given the phone number string below:
# Extract and print:
#   - The country code (first 2 characters - index 0 and 1)
#   - Combine them into one string called 'country_code'
#   - Print country_code

phone = "48502111222"



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Look at the code below.
# WITHOUT running it first, predict the output.
# Write your predictions as comments.
# Then run and verify.

sentence = "Data Science"
# Prediction: sentence[0]  = ?
print(sentence[0])
# Prediction: sentence[4]  = ?
print(sentence[4])
# Prediction: sentence[5]  = ?
print(sentence[5])
# Prediction: sentence[11] = ?
print(sentence[11])



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a string: "Python3.11"
# Using ONLY indexing, build and print the following strings:
#   - "P" (first character)
#   - "Py" (first + second character concatenated)
#   - "3" (the digit)
#   - ".11" (dot + 1 + 1 concatenated from their indexes)
# Do NOT write the characters literally - use indexing!



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# The variable below contains a DNA codon (3 nucleotides).
# A codon is always exactly 3 characters: position 0, 1, 2.
# Print each nucleotide with a descriptive label.
# Then check: what is the type of codon[0]?
# Expected output:
#   First nucleotide: A
#   Second nucleotide: T
#   Third nucleotide: G
#   Type: <class 'str'>

codon = "ATG"



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Try to find ALL the errors in the code below.
# Write what each error is as a comment.
# Then fix the code so it runs without errors.

word = "Python"
print(word[6])          # Error: ?
print(word[1.0])        # Error: ?

text = "Hi"
text[0] = "B"           # Error: ?
print(text)



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a string variable 'sentence' with this value:
#   "The quick brown fox"
# Without running first, map out ALL the indexes on paper
# (or as a comment in your code).
# Then verify by printing:
#   - The character at index 3
#   - The character at index 10
#   - The character at index 16
# Write a comment explaining what each character is
# and whether your mapping was correct.



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# You are given a product code in this format:
#   characters 0-1 : category code (e.g. "EL")
#   character  2   : separator (always "-")
#   characters 3-6 : product number (e.g. "4521")
#   character  7   : separator (always "-")
#   characters 8-9 : warehouse code (e.g. "WW")
#
# Using ONLY indexing (no slicing yet!), extract and print:
#   - category_code  (combine index 0 and 1)
#   - product_number (combine index 3, 4, 5, 6)
#   - warehouse_code (combine index 8 and 9)
# Print them with labels.
# Expected output:
#   Category: EL
#   Product number: 4521
#   Warehouse: WW

product_code = "EL-4521-WW"



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# This exercise tests your deep understanding of indexing.
#
# Part A:
# Create a string with at least 10 characters of your choice.
# Print every OTHER character manually using indexing
# (index 0, 2, 4, 6, 8) - combine them into one string.
#
# Part B:
# Given the string "racecar" - it reads the same forwards
# and backwards (palindrome).
# Using ONLY indexing, verify this manually by printing:
#   - first and last character (should match)
#   - second and second-to-last character (should match)
#   - third and third-to-last character (should match)
#   - middle character
# Write a comment: is "racecar" a palindrome based on what you see?
#
# Part C:
# What happens if you do this:
#   text = ""
#   print(text[0])
# Predict the result, write it as a comment, then run and verify.