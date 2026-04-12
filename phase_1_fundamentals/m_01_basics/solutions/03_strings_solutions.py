# ============================================================
# MODULE 01 | EXERCISES 03 - Strings
# ============================================================
# 15 exercises - strings only
# Allowed from previous lectures:
#   - variables, print(), type()     (lecture 01)
#   - len(), round()                 (lecture 02)
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
string_1 = "John Smith Goldlock"
string_2 = 'John Smith Goldlock'
string_3 = """John
Smith
Goldlock
"""

print(string_1, type(string_1))
print(string_2, type(string_2))
print(string_3, type(string_3))



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
word = "Bioinformatics"

print("1. ", word[0])
print("2. ", word[13])
print("3. ", word[4])
print("4. ", word[-3])
print("5. ", len(word))



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
text = "Hello World Python"

print("1. ", text[0:5])
print("2. ", text[6:11])
print("3. ", text[12:18])
print("4. ", text[:])
print("5. ", text[::2])
print("6. ", text[::-1])



# ------------------------------------------------------------
# EXERCISE 4 ✅ | EASY
# ------------------------------------------------------------
first = "Hello"
second = "World"

print("1. ", first + " " + second)
print("2. ", first * 4)
print("3. ", "=" * 30)
print("4. ", first * 3 + " " + second)



# ------------------------------------------------------------
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
text = "  Hello World  "

print("1. ", text.upper(), len(text.upper()))
print("2. ", text.lower(), len(text.lower()))
print("3. ", text.strip(), len(text.strip()))
print("4. ", text.strip().title(), len(text.strip().title()))
print("5. ", text.strip().swapcase(), len(text.strip().swapcase()))



# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
text = "Python is great and Python is fun"

print("First index of 'Python': ", text.find("Python"))
print("Last index of 'Python': ", text.rfind("Python"))
print("How many times 'Python' occurs: " , text.count("Python"))
print("How many times 'is' occurs: ", text.count("is"))
print("Does text start with 'Python'? ", text.startswith("Python"))
print("Does text ends with 'fun'? ", text.endswith("fun"))



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
a = "hello"
print('1. "hello" has only alphabet: ', a.isalpha())
print('2. "hello" has only digits: ', a.isdigit())
print('3. "hello" has letters AND/OR digits: ', a.isalnum())
print('4. "hello" has only whitespaces: ', a.isspace())
print('5. "hello" has only big letters: ', a.isupper())
print('6. "hello" has only small: ', a.islower())
print('7. "hello" has capital first letters: ', a.istitle())

b = "HELLO"
print('1. "HELLO" has only alphabet: ', a.isalpha())
print('2. "HELLO" has only digits: ', a.isdigit())
print('3. "HELLO" has letters AND/OR digits: ', a.isalnum())
print('4. "HELLO" has only whitespaces: ', a.isspace())
print('5. "HELLO" has only big letters: ', a.isupper())
print('6. "HELLO" has only small: ', a.islower())
print('7. "HELLO" has capital first letters: ', a.istitle())

c = "Hello World"
print('1. "Hello World" has only alphabet: ', a.isalpha())
print('2. "Hello World" has only digits: ', a.isdigit())
print('3. "Hello World" has letters AND/OR digits: ', a.isalnum())
print('4. "Hello World" has only whitespaces: ', a.isspace())
print('5. "Hello World" has only big letters: ', a.isupper())
print('6. "Hello World" has only small: ', a.islower())
print('7. "Hello World" has capital first letters: ', a.istitle())

d = "hello123"
print('1. "hello123" has only alphabet: ', a.isalpha())
print('2. "hello123" has only digits: ', a.isdigit())
print('3. "hello123" has letters AND/OR digits: ', a.isalnum())
print('4. "hello123" has only whitespaces: ', a.isspace())
print('5. "hello123" has only big letters: ', a.isupper())
print('6. "hello123" has only small: ', a.islower())
print('7. "hello123" has capital first letter: ', a.istitle())

e = "12345"
print('1. "12345" has only alphabet: ', a.isalpha())
print('2. "12345" has only digits: ', a.isdigit())
print('3. "12345" has letters AND/OR digits: ', a.isalnum())
print('4. "12345" has only whitespaces: ', a.isspace())
print('5. "12345" has only big letters: ', a.isupper())
print('6. "12345" has only small: ', a.islower())
print('7. "12345" has capital first letter: ', a.istitle())

f = "   "
print('1. "   " has only alphabet: ', a.isalpha())
print('2. "   " has only digits: ', a.isdigit())
print('3. "   " has letters AND/OR digits: ', a.isalnum())
print('4. "   " has only whitespaces: ', a.isspace())
print('5. "   " has only big letters: ', a.isupper())
print('6. "   " has only small: ', a.islower())
print('7. "   " has capital first letter: ', a.istitle())



# ------------------------------------------------------------
# EXERCISE 8 ✅ | MEDIUM
# ------------------------------------------------------------
data = "  ***ATCGGCTA***  "

data_stripped = data.strip()

clear_data = data_stripped.strip("*")
print(clear_data)

clear_data_lower = clear_data.lower()
print(clear_data_lower)

clear_data_replaced = clear_data_lower.replace("a", "A")
print(clear_data_replaced, len(clear_data_replaced))



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
sentence = "the quick brown fox jumps over the lazy dog"

word_list = sentence.split()
print(word_list)
print(len(word_list))

print("-".join(word_list))
print("|".join(word_list))

split_by_o = sentence.split("o")
print(split_by_o)
print(sentence.count("o"))
print(len(split_by_o))



# ------------------------------------------------------------
# EXERCISE 10 ✅ | MEDIUM
# ------------------------------------------------------------
name = "python"

print(name.center(20), len(name.center(20)))
print(name.center(20, "-"), len(name.center(20, "-")))
print(name.ljust(20, "."), len(name.ljust(20, ".")))
print(name.rjust(20, "."), len(name.rjust(20, ".")))
print(name.rjust(20, "0"), len(name.rjust(20, "0")))



# ------------------------------------------------------------
# EXERCISE 11 🔄 | MEDIUM
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
# EXERCISE 12 🔄 | MEDIUM-HARD
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
# EXERCISE 13 🔄 | MEDIUM-HARD
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

text = "To be or not to be that is the question"
print("1. Total characters (with spaces): ", len(text))
print("2. Total characters (without spaces): ", len(text.replace(" ", "")))
print("3. Total numbers of words: ", len(text.split()))
print("4. Total numbers of unique words: ")
print("5. Most common letter: ")
print("6. Is a palindrome: ", )
print("7. Text in title case: ", text.title())
print("8. Reversed text: ", text[::-1])




# ------------------------------------------------------------
# EXERCISE 14 🔄 | HARD
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
# EXERCISE 15 🔄 | HARD
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