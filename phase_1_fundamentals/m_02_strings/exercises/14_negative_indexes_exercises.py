# ============================================================
# MODULE 02 | EXERCISES 14 - Negative Indexes
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create a variable 'animal' with the value "elephant".

# Using negative indexing, print:
#   - the last character
#   - the second to last character

# Expected output:
#   t
#   n
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("Exercise 1:")

animal = "elephant"

print(animal[-1])
print(animal[-2])



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Print all characters of the word "Python" using only negative
# indexes (-1 through -6). Print one character per line.

# Expected output:
#   n
#   o
#   h
#   t
#   y
#   P
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 2:")

word = "Python"

print(word[-1])
print(word[-2])
print(word[-3])
print(word[-4])
print(word[-5])
print(word[-6])



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# For the string below, print the character at index -1 using three
# different strings of different lengths. Observe that [-1] always
# gives the last character regardless of length.

# short  = "Hi"
# medium = "Python"
# long_s = "Bioinformatics"

# Print word[-1] for all three and add a comment explaining what you observe.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 3:")

short  = "Hi"
medium = "Python"
long_s = "Bioinformatics"

print(short[-1])
print(medium[-1])
print(long_s[-1])



# ------------------------------------------------------------
# EXERCISE 4 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Without running the code first, predict the output.
# Write your prediction as a comment, then verify.

# word = "Biology"

# print(word[-1])      # Prediction: word[-1]  = ?
# print(word[-3])      # Prediction: word[-3]  = ?
# print(word[-7])      # Prediction: word[-7]  = ?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 4:")

word = "Biology"

print(word[-1])        # Prediction: word[-1]  = y
print(word[-3])        # Prediction: word[-3]  = o
print(word[-7])        # Prediction: word[-7]  = B



# ------------------------------------------------------------
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given the string "racecar":

# Using indexing (positive or negative), print:
#   - first character
#   - last character

# Then check if they are equal using == and print the result.

# Expected output:
#   r
#   r
#   True
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 5:")

string = "racecar"

print(string[0])
print(string[-1])
print(string[0] == string[-1])




# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# The string below represents a filename.

# filename = "annual_report.pdf"

# Using only negative indexing, print the last 3 characters one
# by one (each on separate line). Then combine them into a
# variable called 'extension' and print it.

# Expected output:
#   p
#   d
#   f
#   pdf
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 6:")

filename = "annual_report.pdf"

print(filename[-3])
print(filename[-2])
print(filename[-1])

extension = filename[-3] + filename[-2] + filename[-1]

print(extension)



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# For the string "Python":

# Using the mathematical relationship:
#   word[-i] == word[-i + length]

# Verify manually (using print and ==) that:
#   - word[-1] gives the same result as word[5]
#   - word[-2] gives the same result as word[4]
#   - word[-6] gives the same result as word[0]

# Print True/False for each comparison.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 7:")

string = "Python"
index = 1

print(f"{string[-index]} == {string[-index + len(string)]}")

print(f"{string[-1] == string[-1 + len(string)]}")
print(f"{string[-2] == string[-2 + len(string)]}")
print(f"{string[-6] == string[-6 + len(string)]}")



# ------------------------------------------------------------
# EXERCISE 8 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Use a variable as a negative index. Given:

# word = "Genetics"
# i = -1

# Print word[i], then change i to -4, print again. Then use an
# expression: print word[-(2 * 2)].
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 8:")

word = "Genetics"
i = -1

print(word[i])
print(word[-(2 * 2)])



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create a string with random full name: "FirstName LastName"

# Using a combination of positive and negative indexes:
#   - Print the first character of first name (positive)
#   - Print the last character of last name (negative)
#   - Print the first character of last name
#     (you need to find the right index - either positive or negative)
#   - Combine all three into 'initials' and print
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 9:")

full_name = "John Smith"

print(full_name[0])
print(full_name[-1])
print(full_name[-5])

initials = full_name[0] + "." + full_name[-5] + "."

print(initials)



# ------------------------------------------------------------
# EXERCISE 10 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given the DNA sequence below:

# dna = "ATGCCCTTA"

# Print the following using appropriate indexes:
#   - First nucleotide (positive index)
#   - Last nucleotide (negative index)
#   - Third nucleotide from the end (negative index)
#   - Check if first == last, print True or False
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 10:")

dna = "ATGCCCTTA"

print(dna[0])
print(dna[-1])
print(dna[-3])
print(dna[0] == dna[-1])



# ------------------------------------------------------------
# EXERCISE 11 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Find the errors in the code below.

# word = "Python"

# print(word[-7])       # Prediction = ?
# print(word[-0])       # Prediction = ?
# print(word[-6.0])     # Prediction = ?

# Write what each error is as a comment, then fix the code.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 11:")

# word = "Python"

# print(word[-7])       # Prediction = ?
# print(word[-0])       # Prediction = ?
# print(word[-6.0])     # Prediction = ?

word = "Python"

print(word[-6])         # out of range
print(word[-0])         # prints "P" because -0 == 0
print(word[-6])         # float index instead of int



# ------------------------------------------------------------
# EXERCISE 12 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Without running the code first, predict all outputs.
# Write each prediction as a comment, then run and verify.

# text = "Hello World"

# print(text[-1])                 # Prediction: ?
#
# print(text[-6])                 # Prediction: ?
#
# print(text[-11])                # Prediction: ?
#
# print(text[0] == text[-11])     # Prediction: ?
#
# print(text[4] == text[-7])      # Prediction: ?
#
# print(text[-1] == text[-5])     # Prediction: ?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 12:")

text = "Hello World"

print(text[-1])                 # Prediction: d

print(text[-6])                 # Prediction: " "

print(text[-11])                # Prediction: H

print(text[0] == text[-11])     # Prediction: True

print(text[4] == text[-7])      # Prediction: True

print(text[-1] == text[-5])     # Prediction: False



# ------------------------------------------------------------
# EXERCISE 13 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create a product code string: "CAT-2024-XL"

# Using only negative indexes, extract and print:
#   - The last two characters (size: "XL")
#   - The dash before the size (3rd from end)
#   - The last 4 characters of the year part (positions -7 to -4)

# Add a descriptive label to each print statement.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 13:")

product_code = "CAT-2024-XL"

size = product_code[-2] + product_code[-1]
dash = product_code[-3]
year = product_code[-7] + product_code[-6] + product_code[-5] + product_code[-4]

print(f"Size: {size}")
print(f"Year: {year}")

print(f"Full code: {product_code} / CAT{dash}{year}{dash}{size}")



# ------------------------------------------------------------
# EXERCISE 14 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given the string:

# word1 = "madam"
# word2 = "python"

# manually check if it is a palindrome using negative indexes.
# Print each comparison (True/False). Then print a final conclusion
# as a string: "Is palindrome: True" or "Is palindrome: False"
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 14:")

word1 = "madam"
word2 = "python"

print(f"{word1[-1]} == {word1[0]}: {word1[-1] == word1[0]}")
print(f"{word1[-2]} == {word1[1]}: {word1[-2] == word1[1]}")
print(f"{word1} is palindrome: True")

print()

print(f"{word2[-1]} == {word2[0]}: {word2[-1] == word2[0]}")
print(f"{word2[-2]} == {word2[1]}: {word2[-2] == word2[1]}")
print(f"{word2} is palindrome: False")



# ------------------------------------------------------------
# EXERCISE 15 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# You are given a secret message encoded as a string.
# Each "real" character is hidden at specific positions.

# The message = "xPzywtzhhzoqnaz"

# The real characters are at these indexes:
#   -14, -12, -10, -7, -5, -3

# Part A:
#   Extract each character at those indexes manually
#   and combine them into a variable called 'decoded'.
#   Print 'decoded'.

# Part B:
#   Also extract the characters at positive indexes:
#     1, 3, 5, 8, 10, 12
#   Combine them into 'decoded2' and print it.
#   Are decoded and decoded2 the same? Print True/False.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 15:")

message = "xPzywtzhhzoqnaz"

print("Part A:")

decoded = message[-14] + message[-12] + message[-10] + message[-7] + message[-5] + message[-3]

print(decoded)

print("Part B:")

decoded2 = message[1] + message[3] + message[5] + message[8] + message[10] + message[12]

print(decoded2)

print(f"Is {decoded} == {decoded2}: {decoded == decoded2}")