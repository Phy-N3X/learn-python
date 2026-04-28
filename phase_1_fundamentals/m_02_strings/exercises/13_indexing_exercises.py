# ============================================================
# MODULE 02 | EXERCISES 13 - String Indexing
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create a variable called 'city' with the value "Warsaw"
# Print the first character of the string.
# Print the last character of the string.

# Expected output:
#   W
#   w
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("Exercise 1:")

city = "Warsaw"

print(city[0])
print(city[5])



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given the string:

# language = "Programming"

# Print:
#   - character at index 0
#   - character at index 4
#   - character at index 7

# Expected output:
#   P
#   r
#   m
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 2:")

language = "Programming"

print(language[0])  # "P"
print(language[4])  # "r"
print(language[7])  # "m"



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create a variable 'dna' with the value "ATCGTA"
# Print each character on a separate line using indexing.

# Expected output:
#   A
#   T
#   C
#   G
#   T
#   A
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 3:")

dna = "ATCGTA"

print(dna[0])
print(dna[1])
print(dna[2])
print(dna[3])
print(dna[4])
print(dna[5])



# ------------------------------------------------------------
# EXERCISE 4 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# The string below has spaces in it.

# text = "Hi there"

# Print the character at index 2 and index 6.

# Before running - predict what the output will be.
# Write your prediction as a comment first.

# Prediction: index 2 = ?   index 6 = ?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 4:")

text = "Hi there"

print(text[2])      # " "
print(text[6])      # "r"



# ------------------------------------------------------------
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create a variable with random full name as a single string.
# Example: "John Smith"

# Using indexing, print:
#   - The first letter of the first name
#   - The first letter of the last name

# Then combine them into a variable called 'initials' and print it.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 5:")

full_name = "John Smith"

print(full_name[0])
print(full_name[5])

initials = full_name[0] + "." + full_name[5] + "."

print(initials)



# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
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
# CODE:
# ------------------------------------------------------------
print("\nExercise 6:")

word = "Python"
position = 4

print(word[position])



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given the string:

# alphabet = "abcdefghijklmnop"

# Print the character at index (2 * 3).
# Then print the character at index (10 - 7)
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 7:")

alphabet = "abcdefghijklmnop"

print(alphabet[2 * 3])
print(alphabet[10 - 7])



# ------------------------------------------------------------
# EXERCISE 8 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given the phone number string:

# phone = "48502111222"

# Extract and print:
#   - The country code (first 2 characters - index 0 and 1)
#   - Combine them into one string called 'country_code'
#   - Print country_code
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 8:")

phone = "48502111222"

country_code = "+" + phone[0] + phone[1]

print(f"Country code: {country_code}")



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Look at the code below without running it first, predict the output.
# Write your predictions as comments. Then run and verify.

# sentence = "Data Science"

# print(sentence[0])  # Prediction: sentence[0]  = ?
# print(sentence[4])  # Prediction: sentence[4]  = ?
# print(sentence[5])  # Prediction: sentence[5]  = ?
# print(sentence[11]) # Prediction: sentence[11] = ?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 9:")

sentence = "Data Science"

print(sentence[0])  # Prediction: sentence[0]  = D
print(sentence[4])  # Prediction: sentence[4]  = " "
print(sentence[5])  # Prediction: sentence[5]  = S
print(sentence[11]) # Prediction: sentence[11] = e



# ------------------------------------------------------------
# EXERCISE 10 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create a string: "Python3.11"

# Using only indexing, build and print the following strings:
#   1. "P" (first character)
#   2. "Py" (first + second character concatenated)
#   3. "3" (the digit)
#   4. ".11" (dot + 1 + 1 concatenated from their indexes)

# Do not write the characters literally - use indexing!
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 10:")

text = "Python3.11"

print(f"1. {text[0]}")
print(f"2. {text[0] + text[1]}")
print(f"3. {text[6]}")
print(f"4. {text[7] + text[8] + text[9]}")



# ------------------------------------------------------------
# EXERCISE 11 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# The variable below contains a DNA codon (3 nucleotides).

# codon = "ATG"

# A codon is always exactly 3 characters: position 0, 1, 2.
# Print each nucleotide with a descriptive label and then
# check: what is the type of codon[0]?

# Expected output:
#   First nucleotide: A
#   Second nucleotide: T
#   Third nucleotide: G
#   Type: <class 'str'>
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 11:")

codon = "ATG"

print(f"First nucleotide: {codon[0]}")
print(f"Second nucleotide: {codon[1]}")
print(f"Third nucleotide: {codon[2]}")
print(f"Type: {type(codon[0])}")



# ------------------------------------------------------------
# EXERCISE 12 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Try to find all the errors in the code below:
#   word = "Python"
#   print(word[6])          # Error: ?
#   print(word[1.0])        # Error: ?

#   text = "Hi"
#   text[0] = "B"           # Error: ?
#   print(text)

# Write what each error is as a comment.
# Then fix the code so it runs without errors.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 12:")

# word = "Python"
# print(word[6])          # Error: index out of range
# print(word[1.0])        # Error: float index instead of int
#
# text = "Hi"
# text[0] = "B"           # Error: cannot modify existing string
# print(text)


word = "Python"
print(word[5])
print(word[1])

text = "Hi"
text = "B"
print(text)



# ------------------------------------------------------------
# EXERCISE 13 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create a string variable 'sentence' with this value:
#   "The quick brown fox"

# Without running first, map out all the indexes as a comment.

# Then verify by printing:
#   - The character at index 3
#   - The character at index 10
#   - The character at index 16
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 13:")

sentence = "The quick brown fox"

print(f"Index 0:  {sentence[0]}")         # T
print(f"Index 1:  {sentence[1]}")         # h
print(f"Index 2:  {sentence[2]}")         # e
print(f"Index 3:  {sentence[3]}")         #
print(f"Index 4:  {sentence[4]}")         # q
print(f"Index 5:  {sentence[5]}")         # u
print(f"Index 6:  {sentence[6]}")         # i
print(f"Index 7:  {sentence[7]}")         # c
print(f"Index 8:  {sentence[8]}")         # k
print(f"Index 9:  {sentence[9]}")         #
print(f"Index 10:  {sentence[10]}")        # b
print(f"Index 11:  {sentence[11]}")        # r
print(f"Index 12:  {sentence[12]}")        # o
print(f"Index 13:  {sentence[13]}")        # w
print(f"Index 14:  {sentence[14]}")        # n
print(f"Index 15:  {sentence[15]}")        #
print(f"Index 16:  {sentence[16]}")        # f
print(f"Index 17:  {sentence[17]}")        # o
print(f"Index 18:  {sentence[18]}")        # x

print()

print(f"Index 3: {sentence[3]}")
print(f"Index 10: {sentence[10]}")
print(f"Index 16: {sentence[16]}")



# ------------------------------------------------------------
# EXERCISE 14 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# You are given a product code in this format:
#   characters 0-1 : category code (e.g. "EL")
#   character  2   : separator (always "-")
#   characters 3-6 : product number (e.g. "4521")
#   character  7   : separator (always "-")
#   characters 8-9 : warehouse code (e.g. "WW")

# product_code = "EL-4521-WW"

# Using only indexing, extract and print:
#   - category_code
#   - product_number
#   - warehouse_code

# Print them with labels.

# Expected output:
#   Category: EL
#   Product number: 4521
#   Warehouse: WW
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 14:")

product_code = "EL-4521-WW"

category_code = product_code[0] + product_code[1]
product_number = product_code[3] + product_code[4] + product_code[5] + product_code[6]
warehouse_code = product_code[8] + product_code[9]

print(f"Category: {category_code}")
print(f"Product name: {product_number}")
print(f"Warehouse: {warehouse_code}")



# ------------------------------------------------------------
# EXERCISE 15 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# This exercise tests your deep understanding of indexing.

# Part A:
#   Create a string with at least 10 characters of your choice.
#   Print every other character manually using indexing
#   (index 0, 2, 4, 6, 8) - combine them into one string and print.

# Part B:
#   Given string: "racecar" is a palindrome.

#   Using only indexing, verify this manually by printing:
#     - first and last character (should match)
#     - second and second-to-last character (should match)
#     - third and third-to-last character (should match)
#     - middle character

# Part C:
#   What happens if you do this:
#     text = ""
#     print(text[0])
#   Predict the result, write it as a comment, then run and verify.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 15:")

print("Part A:")

string = "understanding"
mixed = string[0] + string[2] + string[4] + string[6] + string[8] + string[10] + string[12]

print(mixed)

print("Part B:")

palindrome = "racecar"

print(f"First and last character: {palindrome[0]} = {palindrome[6]}")
print(f"Second and secont-to-last character: {palindrome[1]} = {palindrome[5]}")
print(f"Third and third-to-last character: {palindrome[2]} = {palindrome[4]}")
print(f"Middle character: {palindrome[3]}")

print("Part C:")

text = ""

print(text[0])    # out of range error