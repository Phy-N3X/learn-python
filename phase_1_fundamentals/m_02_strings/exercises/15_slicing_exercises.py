# ============================================================
# MODULE 02 | EXERCISES 15 - Slicing
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create a variable 'language' = "Programming"

# Using slicing, print:
#   - first 4 characters
#   - last 4 characters
#   - characters from index 2 to index 6

# Expected output:
#   Prog
#   ming
#   ogra
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("Exercise 1:")

language = "Programming"

print(language[0:4])
print(language[-4:])
print(language[2:6])



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Using the string

# word = "Bioinformatics"

# demonstrate the difference between omitting start and omitting stop.

# Print:
#   - word[:5]   and explain in a comment what it does
#   - word[5:]   and explain in a comment what it does
#   - word[:]    and explain in a comment what it does
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 2:")

word = "Bioinformatics"

print(word[:5])     # "Bioin"
print(word[5:])     # "formatics"
print(word[:])      # "Bioinformatics"



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Predict the output of each slice before running.
# Write your prediction as a comment, then verify.

# text = "Hello World"

# print(text[0:5])     # Prediction: ?
# print(text[6:11])    # Prediction: ?
# print(text[:5])      # Prediction: ?
# print(text[6:])      # Prediction: ?
# print(text[:])       # Prediction: ?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 3:")

text = "Hello World"

print(text[0:5])     # Prediction: "Hello"
print(text[6:11])    # Prediction: "World"
print(text[:5])      # Prediction: "Hello"
print(text[6:])      # Prediction: "World"
print(text[:])       # Prediction: "Hello World"



# ------------------------------------------------------------
# EXERCISE 4 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Use negative indexes in slices. Given:

# word = "Python"

# Print:
#   - last 3 characters using negative start
#   - everything except last character using negative stop
#   - everything except first and last character

# Add comments explaining each slice.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 4:")

word = "Python"

print(word[-3:])      # hon
print(word[:-1])      # Pytho
print(word[1:-1])     # ytho



# ------------------------------------------------------------
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given the date string:

# date = "2024-07-19"

# below, extract:
#   - year  (first 4 characters)
#   - month (characters 5 and 6)
#   - day   (last 2 characters)

# Print each with a label.

# Expected output:
#   Year: 2024
#   Month: 07
#   Day: 19
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 5:")

date = "2024-07-19"

year = date[0:4]
month = date[5:7]
day = date[-2:]

print(f"Day: {day} | Month: {month} | Year: {year}")



# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given the filename: filename = "genome_data.fasta"

# - Extract the name without extension (before the dot)
# - Extract only the extension (after the dot, without dot)
# - Extract the extension including the dot

# Use slicing. You may hardcode the index of the dot.
# Print each with a label.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 6:")

file = "genome_data.fasta"

file_name = file[:-6]
file_extension = file[-5:]
file_full_extension = file[-6:]

print(file_name + file_full_extension)



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Demonstrate that slicing does not raise IndexError even when
# indexes are out of range.

# Given: word = "Python"

# Print the result of these slices and write a comment explaining
# what Python does in each case:
#   word[0:100]         # Prediction: ?
#   word[-100:3]        # Prediction: ?
#   word[10:20]         # Prediction: ?
#   word[3:3]           # Prediction: ?
#   word[5:2]           # Prediction: ?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 7:")

word = "Python"

print(word[0:100])      # Prediction: "Python"
print(word[-100:3])     # Prediction: "Pyt"
print(word[10:20])      # Prediction: ""
print(word[3:3])        # Prediction: ""
print(word[5:2])        # Prediction: ""



# ------------------------------------------------------------
# EXERCISE 8 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Use slicing to "fix" the strings below.

# a) a = "PPython"  → "Python"
# b) b = "Pythonn"  → "Python"
# c) c = "xPythonx" → "Python"

# Each string has a problem - use slicing (and concatenation
# if needed) to produce the correct result. Print the fixed version.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 8:")

a = "PPython"
b = "Pythonn"
c = "xPythonx"

d = a[1:]
e = b[0:6]
f = c[1:-1]

print(d)
print(e)
print(f)



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given the DNA sequence below:

# dna = "ATGCCCGCATTAGTCGA"

# A codon is a group of 3 nucleotides. Extract and print the
# first four codons using slicing. Label each codon.

# Expected output:
#   Codon 1: ATG
#   Codon 2: CCC
#   Codon 3: GCA
#   Codon 4: TTA
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 9:")

dna = "ATGCCCGCATTAGTCGA"

dna_1 = dna[0:3]
dna_2 = dna[3:6]
dna_3 = dna[6:9]
dna_4 = dna[9:12]

print(f"Codon 1: {dna_1}")
print(f"Codon 2: {dna_2}")
print(f"Codon 3: {dna_3}")
print(f"Codon 4: {dna_4}")



# ------------------------------------------------------------
# EXERCISE 10 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Rearrange the date format using slicing.

# Input format:  "2024-03-15"  (YYYY-MM-DD)
# Output format: "15/03/2024"  (DD/MM/YYYY)

# Use slicing to extract parts and concatenation to rebuild.
# Print the result.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 10:")

date = "2024-03-15"

year = date[0:4]
month = date[5:7]
day = date[-2:]

european_date_format = day + "/" + month + "/" + year

print(f"Input format: {date} (YYYY-MM-DD)")
print(f"Output format: {european_date_format} (DD/MM/YYYY)")



# ------------------------------------------------------------
# EXERCISE 11 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Use slicing to extract the username and domain from the email
# address below. Then print them with labels.

# email = "anna.kowalska@university.edu"

# Expected output:
#   Username: anna.kowalska
#   Domain: university.edu
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 11:")

email = "anna.kowalska@university.edu"

domain_name = email[-14:]
username = email[0:13]

print(f"Username: {username}")
print(f"Domain: {domain_name}")



# ------------------------------------------------------------
# EXERCISE 12 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given: full_name = "Smith John"

# Rearrange it to: "John Smith"

# Steps to think about:
#   1. Find where the space is
#   2. Extract the surname using a slice
#   3. Extract the first name using a slice
#   4. Combine them in the new order

# Print the result.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 12:")

full_name = "Smith John"

first_name = full_name[-4:]
last_name = full_name[0:5]
new_full_name = first_name + " " + last_name

print(f"Full name: {new_full_name}")



# ------------------------------------------------------------
# EXERCISE 13 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Predict all outputs before running. This tests your understanding
# of the stop-is-excluded rule and negative indexes in slices.

# word = "abcdefghij"
#
# print(word[2:5])       # Prediction: ?
# print(word[-5:-2])     # Prediction: ?
# print(word[1:-1])      # Prediction: ?
# print(word[-3:])       # Prediction: ?
# print(word[:-3])       # Prediction: ?
# print(word[-5:5])      # Prediction: ?
# print(word[5:-5])      # Prediction: ?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 13:")

word = "abcdefghij"

print(word[2:5])       # Prediction: cde
print(word[-5:-2])     # Prediction: fgh
print(word[1:-1])      # Prediction: bcdefghi
print(word[-3:])       # Prediction: hij
print(word[:-3])       # Prediction: abcdefg
print(word[-5:5])      # Prediction: ""
print(word[5:-5])      # Prediction: ""



# ------------------------------------------------------------
# EXERCISE 14 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# You are given a product code in this format:

# "CAT-PRODUCTNAME-2024-XL"

# CAT = category (3 chars)
# PRODUCTNAME = variable length product name
# 2024 = year (4 chars)
# XL = size (2 chars)

# For the specific code below:
#   - Extract category using a slice
#   - Extract product name using a slice
#   - Extract year using a slice from the end (negative)
#   - Extract size using a slice from the end (negative)

# Print all four with labels.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 14:")

product_code = "ELE-UltraMonitor-2024-XL"

product_category = product_code[0:3]
product_year = product_code[-7:-3]
product_size = product_code[-2:]
product_name = product_code[4:-8]

print(f"Product code: {product_code}")
print(f"Category: {product_category}")
print(f"Name: {product_name}")
print(f"Year: {product_year}")
print(f"Size: {product_size}")



# ------------------------------------------------------------
# EXERCISE 15 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# This is a multi-part challenge.

# Part A:
#   Given: sentence = "The quick brown fox jumps over the lazy dog"
#   Using only slicing and concatenation:
#     - Extract "quick" and store in variable
#     - Extract "fox" and store in variable
#     - Extract "lazy dog" and store in variable
#     - Build a new sentence: "The lazy dog jumps over the quick fox"
#   Print the new sentence.

# Part B:
#   Given: text = "abcdefghij"
#   Using slicing, split it into three parts.
#   Print each part on a separate line.
#   Expected output:
#     abcd
#     efgh
#     ij

# Part C:
#   Given: word = "Python"
#   Using slicing, verify that these two operations give the same result:
#     1. word[:-1][:-1]   (slice twice)
#     2. word[:-2]        (slice once)
#   Print both results and compare with ==
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 15:")

print("Part A:")

sentence = "The quick brown fox jumps over the lazy dog"

quick = sentence[4:9]
fox = sentence[16:19]
lazy_dog = sentence[-8:]
new_sentence = "The " + lazy_dog + " jumps over the " + quick + " " + fox

print(new_sentence)

print("Part B:")

text = "abcdefghij"

text_1 = text[0:4]
text_2 = text[4:8]
text_3 = text[8:12]

print(text_1)
print(text_2)
print(text_3)

print("Part C:")

word = "Python"

print(word[:-1][:-1])
print(word[:-2])

print(f"Is {word[:-1][:-1]} == {word[:-2]}: {word[:-1][:-1] == word[:-2]}")