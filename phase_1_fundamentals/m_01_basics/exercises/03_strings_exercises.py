# ============================================================
# MODULE 01 | EXERCISES 03 - Strings
# ============================================================
# 15 exercises - strings only
# Allowed from previous lectures:
#   - variables, print(), type()     (lecture 01)
#   - len(), round()                 (lecture 02)
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Create the same string THREE ways:
#   1. Using single quotes
#   2. Using double quotes
#   3. Using triple quotes (multiline - at least 3 lines)
#
# Content of string: your full name
# Print all three and their types.



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Given string: word = "Bioinformatics"
#
# Using ONLY indexing (no slicing yet):
#   1. Print the first character
#   2. Print the last character
#   3. Print the 5th character (index 4)
#   4. Print the 3rd character from the end
#   5. Print the length of the string



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Given string: text = "Hello World Python"
#
# Using ONLY slicing:
#   1. Extract "Hello"
#   2. Extract "World"
#   3. Extract "Python"
#   4. Extract the entire string using [:]
#   5. Extract every 2nd character from the whole string
#   6. Reverse the entire string using [::-1]



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Given:
#   first  = "Hello"
#   second = "World"
#
# Using ONLY string operators (+ and *):
#   1. Concatenate them with a space between
#   2. Repeat "Hello" 4 times
#   3. Create a divider line: "=" repeated 30 times
#   4. Build: "HelloHelloHello World"
# Print all results.



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Given: text = "  Hello World  "
#
# Apply and print the result of:
#   1. .upper()
#   2. .lower()
#   3. .strip()
#   4. .strip() then .title()
#   5. .strip() then .swapcase()
#
# After each step print the result AND its length.
# Notice how length changes after strip()!



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Given: text = "Python is great and Python is fun"
#
# Using search methods:
#   1. Find the index of FIRST "Python"
#   2. Find the index of LAST "Python" using rfind()
#   3. Count how many times "Python" appears
#   4. Count how many times "is" appears
#   5. Does text start with "Python"?
#   6. Does text end with "fun"?
#   7. Print all results with labels.



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Test ALL isX() methods on these strings.
# For each string, print which methods return True.
#
# strings to test:
#   a = "hello"
#   b = "HELLO"
#   c = "Hello World"
#   d = "hello123"
#   e = "12345"
#   f = "   "
#
# Methods to check:
# .isalpha() .isdigit() .isalnum() .isspace() .isupper() .islower() .istitle()



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# Given messy data (common in real bioinformatics!):
#   data = "  ***ATCGGCTA***  "
#
#   1. Remove ALL whitespace from both ends
#   2. Then remove ALL * characters from both ends
#   3. Print the cleaned string
#   4. Convert to lowercase
#   5. Replace all 'a' with 'A' (back to uppercase A only)
#   6. Print final result and its length
#
# Expected final result: "ATcggcTA" ... wait, figure it out!
# Trace through each step carefully.



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Given: sentence = "the quick brown fox jumps over the lazy dog"
#
#   1. Split into a list of words
#   2. Print the list
#   3. Print number of words using len()
#   4. Join the words back with "-" separator
#   5. Join the words back with " | " separator
#   6. Split the original by "o" (not space) - what do you get?
#   7. Print how many times letter "o" appears using count()
#      Verify: does it match len(split_by_o) - 1?



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Given: name = "python"
#
# Use alignment methods to create this exact output
# (total width = 20 characters for each):
#
#        python         (centered with spaces)
# -------python-------- (centered with -)
# python..............  (left justified with .)
# ..............python  (right justified with .)
# 00000000000000python  (right justified with 0... use rjust!)
#
# Print each line and verify length == 20 using len()



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Escape sequences practice.
# Print EXACTLY this output (copy it exactly):
#
# Line 1
# Line 2
# Line 3
#
# Name:	John
# City:	Warsaw
#
# Path: C:\Users\John\Documents
# Quote: He said "hello" and she said "hi"
# Apostrophe: It's a beautiful day
#
# Use \n, \t, \\, \", \' in a single print statement
# or multiple - your choice. No hardcoding newlines in IDE!



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# f-string formatting challenge.
# Given:
#   product = "Python Course"
#   price = 149.99
#   discount = 0.15
#   students = 1234567
#
# Print EXACTLY this output using f-strings:
#
# ================================
# Product:    Python Course
# Price:      $149.99
# Discount:   15.00%
# You save:   $22.50
# Final:      $127.49
# Students:   1,234,567
# ================================
#
# Requirements:
#   - Use f-strings with format specifiers
#   - Prices must show exactly 2 decimal places
#   - Students must have thousands separator (,)
#   - Discount must show as percentage
#   - Calculate savings and final price inside f-string



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# String analysis - given any text, extract information.
#
# text = "To be or not to be that is the question"
#
#   1. Total characters (including spaces)
#   2. Total characters (WITHOUT spaces)
#      Hint: replace spaces with "" then len()
#   3. Number of words
#   4. Number of unique words
#      Hint: split() gives list, set() removes duplicates, len() counts
#   5. Most common letter (just check a,e,i,o,u manually with count())
#      Print count of each vowel
#   6. Is the text a palindrome? (it's not, but check anyway)
#   7. Print text in title case
#   8. Print text reversed (entire string)



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# CSV parser - real world string manipulation.
#
# raw_data = """
# name,age,city,score
# Alice,25,Warsaw,98.5
# Bob,30,Krakow,87.2
# Charlie,22,Gdansk,95.0
# Diana,28,Poznan,91.7
# """
#
# Using ONLY string methods (no pandas, no csv module):
#   1. Strip the raw_data to remove leading/trailing whitespace
#   2. Split into lines using splitlines()
#   3. Print the header line (first line)
#   4. Print each data line separately (lines 2-5)
#   5. For each data line, split by "," and print:
#      "Name: X | Age: X | City: X | Score: X"
#   6. Count total number of data rows (not counting header)
#   7. Find the longest name using len() comparisons



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# String manipulation challenge - build a formatter.
#
# Given a list of raw strings (messy input):
#
# entries = [
#     "  john smith  ",
#     "ANNA KOWALSKI",
#     "bob   jones",
#     "   MARIA garcia   ",
#     "TOM brown"
# ]
#
# For each entry, apply ALL of these transformations:
#   1. Strip whitespace from both ends
#   2. Remove extra spaces between words
#      Hint: " ".join(entry.split())
#   3. Convert to title case
#   4. Replace spaces with underscore
#   5. Add a 3-digit ID at the start: "001_", "002_" etc.
#      Hint: use zfill() for the number
#
# Expected output:
#   001_John_Smith
#   002_Anna_Kowalski
#   003_Bob_Jones
#   004_Maria_Garcia
#   005_Tom_Brown
#
# Print each transformed entry on a new line.
# BONUS: also print total character count for each entry.