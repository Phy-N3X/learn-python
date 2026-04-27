# ============================================================
# MODULE 01 | EXERCISES 03 - Strings
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create the same string three ways:
#   1. Using single quotes
#   2. Using double quotes
#   3. Using triple quotes (multiline - at least 3 lines)

# Content of string: John Arthur Smith
# Print all three and their types.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("Exercise 1:")

string_1 = "John Arthur Smith"
string_2 = 'John Arthur Smith'
string_3 = """John
Arthur
Smith
"""

print(string_1, type(string_1))
print(string_2, type(string_2))
print(string_3, type(string_3))



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given string: word = "Bioinformatics"

# Using only indexing (no slicing yet):
#   1. Print the first character
#   2. Print the last character
#   3. Print the 5th character (index 4)
#   4. Print the 3rd character from the end
#   5. Print the length of the string
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 2:")

word = "Bioinformatics"

print("1. ", word[0])
print("2. ", word[13])
print("3. ", word[4])
print("4. ", word[-3])
print("5. ", len(word))



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given string: text = "Hello World Python"

# Using only slicing:
#   1. Extract "Hello"
#   2. Extract "World"
#   3. Extract "Python"
#   4. Extract the entire string using [:]
#   5. Extract every 2nd character from the whole string
#   6. Reverse the entire string using [::-1]
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 3:")

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
# PROBLEM:
# ------------------------------------------------------------
# Given:
#   first  = "Hello"
#   second = "World"

# Using only string operators (+ and *):
#   1. Concatenate them with a space between
#   2. Repeat "Hello" 4 times
#   3. Create a divider line: "=" repeated 30 times
#   4. Build: "HelloHelloHello World"
# Print all results.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 4:")

first = "Hello"
second = "World"

print("1. ", first + " " + second)
print("2. ", first * 4)
print("3. ", "=" * 30)
print("4. ", first * 3 + " " + second)



# ------------------------------------------------------------
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given: text = "  Hello World  "

# Apply and print the result of:
#   1. .upper()
#   2. .lower()
#   3. .strip()
#   4. .strip() then .title()
#   5. .strip() then .swapcase()

# After each step print the result and its length.
# Notice how length changes after strip()!
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 5:")

text = "  Hello World  "

print("1. ", text.upper(), len(text.upper()))
print("2. ", text.lower(), len(text.lower()))
print("3. ", text.strip(), len(text.strip()))
print("4. ", text.strip().title(), len(text.strip().title()))
print("5. ", text.strip().swapcase(), len(text.strip().swapcase()))



# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given: text = "Python is great and Python is fun"

# Using search methods:
#   1. Find the index of first "Python"
#   2. Find the index of last "Python" using rfind()
#   3. Count how many times "Python" appears
#   4. Count how many times "is" appears
#   5. Does text start with "Python"?
#   6. Does text end with "fun"?
#   7. Print all results with labels.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 6:")

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
# PROBLEM:
# ------------------------------------------------------------
# Test all isX() methods on these strings.
# For each string, print which methods return True.

# strings to test:
#   a = "hello"
#   b = "HELLO"
#   c = "Hello World"
#   d = "hello123"
#   e = "12345"
#   f = "   "

# Methods to check:
# .isalpha() .isdigit() .isalnum() .isspace() .isupper() .islower() .istitle()
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 7:")

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
# PROBLEM:
# ------------------------------------------------------------
# Given messy data:
#   data = "  ***ATCGGCTA***  "

#   1. Remove all whitespace from both ends
#   2. Then remove all * characters from both ends
#   3. Print the cleaned string
#   4. Convert to lowercase
#   5. Replace all 'a' with 'A' (back to uppercase A only)
#   6. Print final result and its length

# Expected final result: "ATcggcTA" ... wait, figure it out!
# Trace through each step carefully.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 8:")

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
# PROBLEM:
# ------------------------------------------------------------
# Given: sentence = "the quick brown fox jumps over the lazy dog"

#   1. Split into a list of words
#   2. Print the list
#   3. Print number of words using len()
#   4. Join the words back with "-" separator
#   5. Join the words back with " | " separator
#   6. Split the original by "o" (not space) - what do you get?
#   7. Print how many times letter "o" appears using count()
#      Verify: does it match len(split_by_o) - 1?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 9:")

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
# PROBLEM:
# ------------------------------------------------------------
# Given: name = "python"

# Use alignment methods to create this exact output
# (total width = 20 characters for each):
#
#        python         (centered with spaces)
# -------python-------- (centered with -)
# python..............  (left justified with .)
# ..............python  (right justified with .)
# 00000000000000python  (right justified with 0... use rjust!)

# Print each line and verify length == 20 using len()
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 10:")

name = "python"

print(name.center(20), len(name.center(20)))
print(name.center(20, "-"), len(name.center(20, "-")))
print(name.ljust(20, "."), len(name.ljust(20, ".")))
print(name.rjust(20, "."), len(name.rjust(20, ".")))
print(name.rjust(20, "0"), len(name.rjust(20, "0")))



# ------------------------------------------------------------
# EXERCISE 11 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Print exactly this output:
#   Line 1
#   Line 2
#   Line 3
#   Name:	John
#   City:	Warsaw
#   Path: C:\Users\John\Documents
#   Quote: He said "hello" and she said "hi"
#   Apostrophe: It's a beautiful day

# Use \n, \t, \\, \", \' in a single print statement or multiple.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 11:")

print("Line 1\nLine 2\nLine 3\n\nName:\tJohn\nCity:\tWarsaw")
print("\nPath: C:\\Users\\John\\Documents\nQuote: He said \"hello\" and she said \"hi\"")
print("Apostrophe: It\'s a beautiful day")



# ------------------------------------------------------------
# EXERCISE 12 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given:
#   product = "Python Course"
#   price = 149.99
#   discount = 0.15
#   students = 1234567

# Print exactly this output using f-strings:
#   ================================
#   Product:    Python Course
#   Price:      $149.99
#   Discount:   15.00%
#   You save:   $22.50
#   Final:      $127.49
#   Students:   1,234,567
#   ================================

# Requirements:
#   - Use f-strings with format specifiers
#   - Prices must show exactly 2 decimal places
#   - Students must have thousands separator (,)
#   - Discount must show as percentage
#   - Calculate savings and final price inside f-string
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 12:")

product = "Python Course"
price = 149.99
discount = 0.15
students = 1234567

print("=" * 25)
print(f"Product:   {product}")
print(f"Price: ${price:10.2f}")
print(f"Discount: {discount:6.1%}")
print(f"You save: %{price * discount:6.2f}")
print(f"Final: ${price - (price * discount):10.2f}")
print(f"Students:  {students:,}")
print("=" * 25)



# ------------------------------------------------------------
# EXERCISE 13 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given 'text' - extract information.
# text = "To be or not to be that is the question"

#   1. Total characters (including spaces)
#   2. Total characters (without spaces)
#      Hint: replace spaces with "" then len()
#   3. Number of words
#   4. Number of unique words
#      Hint: split() gives list, set() removes duplicates, len() counts
#   5. Most common letter. Print count of each vowel
#   6. Is the text a palindrome?
#   7. Print text in title case
#   8. Print entire text reversed
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 13:")

text = "To be or not to be that is the question"

print("1. Total characters (with spaces): ", len(text))
print("2. Total characters (without spaces): ", len(text.replace(" ", "")))
print("3. Total numbers of words: ", len(text.split()))
print("4. Total numbers of unique words: ", len(set(text.lower().split())))
print(f"5. Most common letter: A: {text.count("a")}, E: {text.count("e")}, I: {text.count("i")}, O: {text.count("o")}, U :{text.count("u")}")
print("6. Is a palindrome: ", text == text[::-1])
print("7. Text in title case: ", text.title())
print("8. Reversed text: ", text[::-1])



# ------------------------------------------------------------
# EXERCISE 14 🔄 | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# CSV parser - string manipulation.

# raw_data = """
# name,age,city,score
# Alice,25,Warsaw,98.5
# Bob,30,Krakow,87.2
# Charlie,22,Gdansk,95.0
# Diana,28,Poznan,91.7
# """

# Using only string methods:
#   1. Strip the raw_data to remove leading/trailing whitespace
#   2. Split into lines using splitlines()
#   3. Print the header line (first line)
#   4. Print each data line separately (lines 2-5)
#   5. For each data line, split by "," and print:
#      "Name: X | Age: X | City: X | Score: X"
#   6. Count total number of data rows (not counting header)
#   7. Find the longest name using len() comparisons
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 14:")

raw_data = """
name,age,city,score
Alice,25,Warsaw,98.5
Bob,30,Krakow,87.2
Charlie,22,Gdansk,95.0
Diana,28,Poznan,91.7
"""

lines = raw_data.strip().splitlines()

header = lines[0]

line1 = lines[1]
line2 = lines[2]
line3 = lines[3]
line4 = lines[4]






print(header)
print(data)







# ------------------------------------------------------------
# EXERCISE 15 🔄 | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given a list of raw strings (messy input):

# entries = [
#     "  john smith  ",
#     "ANNA KOWALSKI",
#     "bob   jones",
#     "   MARIA garcia   ",
#     "TOM brown"
# ]

# For each entry, apply all of these transformations:
#   1. Strip whitespace from both ends
#   2. Remove extra spaces between words
#      Hint: " ".join(entry.split())
#   3. Convert to title case
#   4. Replace spaces with underscore
#   5. Add a 3-digit ID at the start: "001_", "002_" etc.
#      Hint: use zfill() for the number

# Expected output:
#   001_John_Smith
#   002_Anna_Kowalski
#   003_Bob_Jones
#   004_Maria_Garcia
#   005_Tom_Brown

# Print each transformed entry on a new line.
# BONUS: print total character count for each entry.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 15:")




