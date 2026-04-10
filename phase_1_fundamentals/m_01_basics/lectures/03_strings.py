# ============================================================
# MODULE 01 | LECTURE 03 - Strings
# ============================================================
# What you will learn:
#   - What a string is and how to create one
#   - Indexing and negative indexing
#   - Slicing
#   - String methods
#   - String operators
#   - Checking string content
#   - Special characters and raw strings
#   - String formatting
# ============================================================


# ------------------------------------------------------------
# PART 1: What is a String?
# ------------------------------------------------------------

# A string is a sequence of characters enclosed in quotes
# Characters can be: letters, digits, symbols, spaces

# Three ways to create a string:
single = 'Hello'
double = "Hello"
multi  = """Hello
World
this is
multiline"""

print(single)           # Hello
print(double)           # Hello
print(multi)            # Hello
                        # World
                        # this is
                        # multiline

# Single and double quotes are identical in Python
# Convention: be consistent throughout your project
# Use double quotes when string contains apostrophe:
sentence = "It's a beautiful day"
print(sentence)         # It's a beautiful day

# Use single quotes when string contains double quotes:
quote = 'He said "hello"'
print(quote)            # He said "hello"

# Strings are IMMUTABLE - you cannot change a character
# You can only create a NEW string
word = "hello"
# word[0] = "H"         # ← TypeError! Cannot modify string
word = "Hello"          # ← This works - creates a NEW string


# ------------------------------------------------------------
# PART 2: String as a Sequence - Indexing
# ------------------------------------------------------------

# A string is a sequence - each character has a position (index)
# Python counts from ZERO

word = "Python"
#       P  y  t  h  o  n
#       0  1  2  3  4  5   ← positive indexes
#      -6 -5 -4 -3 -2 -1   ← negative indexes

print(word[0])          # P  ← first character
print(word[1])          # y
print(word[5])          # n  ← last character
print(word[-1])         # n  ← last character (negative)
print(word[-2])         # o  ← second to last
print(word[-6])         # P  ← same as word[0]

# Index out of range - this causes an error!
# print(word[10])       # IndexError: string index out of range

# len() - number of characters in string
print(len(word))        # 6
print(len(""))          # 0  ← empty string
print(len("  "))        # 2  ← spaces count!


# ------------------------------------------------------------
# PART 3: Slicing
# ------------------------------------------------------------

# Slicing extracts a portion of a string
# Syntax: string[start:stop:step]
#   start = index to begin (INCLUDED)
#   stop  = index to end   (EXCLUDED!)
#   step  = how many to skip (default = 1)

word = "Python"

# Basic slicing [start:stop]
print(word[0:3])        # Pyt  ← indexes 0, 1, 2 (NOT 3!)
print(word[2:5])        # tho  ← indexes 2, 3, 4
print(word[1:4])        # yth

# Omitting start or stop
print(word[:3])         # Pyt  ← from beginning to index 2
print(word[3:])         # hon  ← from index 3 to end
print(word[:])          # Python ← entire string (copy)

# Negative indexes in slicing
print(word[-3:])        # hon  ← last 3 characters
print(word[:-3])        # Pyt  ← everything except last 3
print(word[-4:-1])      # tho  ← from -4 to -2

# Step - every nth character
text = "abcdefghij"
print(text[::2])        # acegi  ← every 2nd character
print(text[::3])        # adgj   ← every 3rd character
print(text[1::2])       # bdfhj  ← every 2nd starting from 1

# Negative step - reverse!
print(text[::-1])       # jihgfedcba ← reversed string
print(word[::-1])       # nohtyP    ← reversed Python

# Combining start, stop, step
print(text[8:1:-2])     # igec  ← from 8 backwards every 2nd


# ------------------------------------------------------------
# PART 4: String Operators
# ------------------------------------------------------------

# Concatenation - joining strings with +
first = "Hello"
second = "World"
result = first + " " + second
print(result)           # Hello World

# You CANNOT concatenate string with number!
# print("Age: " + 25)   # TypeError!
# Solution: convert to string first
print("Age: " + str(25))   # Age: 25

# Repetition - repeating string with *
line = "-" * 30
print(line)             # ------------------------------

laugh = "ha" * 3
print(laugh)            # hahaha

# Membership - checking if substring exists
text = "Hello World"
print("Hello" in text)      # True
print("hello" in text)      # False ← case sensitive!
print("xyz" in text)        # False
print("xyz" not in text)    # True

# Comparison - strings compare alphabetically (lexicographic)
print("apple" == "apple")   # True
print("apple" == "Apple")   # False ← case sensitive!
print("apple" < "banana")   # True  ← 'a' comes before 'b'
print("b" > "a")            # True
print("abc" < "abd")        # True  ← compares char by char


# ------------------------------------------------------------
# PART 5: String Methods - Case
# ------------------------------------------------------------

# Methods are functions that belong to a string
# Syntax: string.method()
# Important: strings are IMMUTABLE - methods return NEW strings!

text = "hello world"

print(text.upper())         # HELLO WORLD
print(text.lower())         # hello world
print(text.capitalize())    # Hello world  ← only first letter
print(text.title())         # Hello World  ← first letter of each word
print(text.swapcase())      # HELLO WORLD  ← swap upper/lower

mixed = "HeLLo WoRLd"
print(mixed.upper())        # HELLO WORLD
print(mixed.lower())        # hello world

# Original is unchanged!
print(text)                 # hello world  ← still lowercase


# ------------------------------------------------------------
# PART 6: String Methods - Searching and Checking
# ------------------------------------------------------------

text = "Hello World Hello Python"

# find() - returns index of FIRST occurrence, -1 if not found
print(text.find("Hello"))       # 0
print(text.find("World"))       # 6
print(text.find("Python"))      # 18
print(text.find("Java"))        # -1  ← not found

# find() with start and end position
print(text.find("Hello", 1))    # 12  ← start searching from index 1

# index() - same as find() but raises ValueError if not found
print(text.index("World"))      # 6
# print(text.index("Java"))     # ValueError!  ← difference from find()

# rfind() - finds LAST occurrence
print(text.rfind("Hello"))      # 12  ← last Hello

# count() - how many times substring appears
print(text.count("Hello"))      # 2
print(text.count("l"))          # 5
print(text.count("xyz"))        # 0

# startswith() and endswith()
print(text.startswith("Hello")) # True
print(text.startswith("World")) # False
print(text.endswith("Python"))  # True
print(text.endswith("Java"))    # False

# startswith() with tuple - check multiple options
print(text.startswith(("Hello", "Hi", "Hey")))  # True


# ------------------------------------------------------------
# PART 7: String Methods - Checking Content
# ------------------------------------------------------------

# These methods return True or False

print("hello".isalpha())        # True  ← only letters
print("hello123".isalpha())     # False ← has digits
print("123".isalpha())          # False

print("123".isdigit())          # True  ← only digits
print("123.4".isdigit())        # False ← dot is not digit
print("hello".isdigit())        # False

print("hello123".isalnum())     # True  ← letters AND/OR digits
print("hello 123".isalnum())    # False ← space not allowed

print("   ".isspace())          # True  ← only whitespace
print("".isspace())             # False ← empty string!

print("Hello World".istitle())  # True  ← title case
print("Hello world".istitle())  # False

print("HELLO".isupper())        # True
print("Hello".isupper())        # False

print("hello".islower())        # True
print("Hello".islower())        # False


# ------------------------------------------------------------
# PART 8: String Methods - Cleaning
# ------------------------------------------------------------

# strip() - removes whitespace from both ends
messy = "   hello world   "
print(messy.strip())            # "hello world"
print(messy.lstrip())           # "hello world   " ← left only
print(messy.rstrip())           # "   hello world" ← right only

# strip() with specific characters
text = "***hello***"
print(text.strip("*"))          # hello
print(text.lstrip("*"))         # hello***
print(text.rstrip("*"))         # ***hello

# remove specific combo of characters (any combo, any order!)
text2 = "xxhelloyx"
print(text2.strip("xy"))        # hello ← removes x and y from edges

# replace() - replaces ALL occurrences
text = "hello world hello"
print(text.replace("hello", "hi"))      # hi world hi
print(text.replace("hello", "hi", 1))  # hi world hello ← limit 1


# ------------------------------------------------------------
# PART 9: String Methods - Splitting and Joining
# ------------------------------------------------------------

# split() - splits string into a LIST
sentence = "hello world python"
words = sentence.split()            # splits on whitespace by default
print(words)                        # ['hello', 'world', 'python']
print(type(words))                  # <class 'list'>

# split() with separator
csv_line = "John,25,Warsaw,Python"
fields = csv_line.split(",")
print(fields)           # ['John', '25', 'Warsaw', 'Python']

# split() with limit
text = "a-b-c-d-e"
print(text.split("-"))      # ['a', 'b', 'c', 'd', 'e']
print(text.split("-", 2))   # ['a', 'b', 'c-d-e'] ← max 2 splits

# splitlines() - splits on line breaks
multiline = "line1\nline2\nline3"
print(multiline.splitlines())   # ['line1', 'line2', 'line3']

# join() - joins a LIST into a string
# Syntax: "separator".join(list)
words = ["hello", "world", "python"]
print(" ".join(words))          # hello world python
print("-".join(words))          # hello-world-python
print("".join(words))           # helloworldpython
print(", ".join(words))         # hello, world, python

# join() is opposite of split()
original = "hello world python"
split_result = original.split()
joined_back = " ".join(split_result)
print(original == joined_back)  # True


# ------------------------------------------------------------
# PART 10: String Methods - Alignment and Padding
# ------------------------------------------------------------

text = "hello"

# center() - center in given width
print(text.center(20))          # "       hello        "
print(text.center(20, "-"))     # "-------hello--------"

# ljust() - left justify
print(text.ljust(20))           # "hello               "
print(text.ljust(20, "."))      # "hello..............."

# rjust() - right justify
print(text.rjust(20))           # "               hello"
print(text.rjust(20, "."))      # "...............hello"

# zfill() - pad with zeros on the left
print("42".zfill(8))            # 00000042
print("3.14".zfill(8))          # 00003.14


# ------------------------------------------------------------
# PART 11: Special Characters (Escape Sequences)
# ------------------------------------------------------------

# \n - newline
print("line1\nline2\nline3")
# line1
# line2
# line3

# \t - tab
print("name:\tJohn")            # name:   John

# \\ - literal backslash
print("C:\\Users\\John")        # C:\Users\John

# \" and \' - quotes inside string
print("He said \"hello\"")      # He said "hello"
print('It\'s fine')             # It's fine

# \r - carriage return (rarely used)
# \b - backspace
# \0 - null character

# Raw strings - ignore ALL escape sequences
path = r"C:\Users\John\Documents"
print(path)                     # C:\Users\John\Documents  ← no escape!

regex = r"\n\t\d+"
print(regex)                    # \n\t\d+  ← literal backslashes


# ------------------------------------------------------------
# PART 12: String Formatting
# ------------------------------------------------------------

name = "Anna"
age = 25
gpa = 4.75

# Method 1: f-strings (Python 3.6+) ← RECOMMENDED
print(f"Name: {name}, Age: {age}, GPA: {gpa}")

# Expressions inside f-strings
print(f"Next year: {age + 1}")
print(f"Upper: {name.upper()}")

# Format specifiers in f-strings
pi = 3.14159265
print(f"{pi:.2f}")              # 3.14     ← 2 decimal places
print(f"{pi:.5f}")              # 3.14159  ← 5 decimal places
print(f"{pi:10.2f}")            # "      3.14" ← width 10, 2 decimals
print(f"{1000000:,}")           # 1,000,000   ← thousands separator
print(f"{0.004:.2%}")           # 0.40%       ← percentage
print(f"{42:08d}")              # 00000042    ← zero padded
print(f"{'hello':>20}")         # "               hello" ← right align
print(f"{'hello':<20}")         # "hello               " ← left align
print(f"{'hello':^20}")         # "       hello        " ← center

# Method 2: .format() - older but still used
print("Name: {}, Age: {}".format(name, age))
print("Name: {0}, Age: {1}, Again: {0}".format(name, age))
print("Name: {n}, Age: {a}".format(n=name, a=age))

# Method 3: % formatting - oldest, avoid in new code
print("Name: %s, Age: %d, GPA: %.2f" % (name, age, gpa))


# ------------------------------------------------------------
# PART 13: Useful String Patterns
# ------------------------------------------------------------

# Check if string is empty
s = ""
print(len(s) == 0)      # True
print(not s)            # True  ← empty string is falsy
print(bool(s))          # False ← empty string is False

# Remove duplicated spaces
text = "hello    world   python"
cleaned = " ".join(text.split())
print(cleaned)          # hello world python

# Reverse a string
word = "Python"
reversed_word = word[::-1]
print(reversed_word)    # nohtyP

# Check if palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racecar"))     # True
print(is_palindrome("hello"))       # False
print(is_palindrome("A man a plan a canal Panama"))  # True

# Count words in a sentence
sentence = "the quick brown fox jumps over the lazy dog"
word_count = len(sentence.split())
print(f"Word count: {word_count}")  # Word count: 9

# Capitalize first letter of each word
title = "the lord of the rings"
print(title.title())    # The Lord Of The Rings

# Check if string contains only one type of character
print("aaa".count("a") == len("aaa"))  # True - all same character


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Strings created with ' " or """
# ✅ Immutable - methods return NEW strings
# ✅ Indexing from 0, negative from -1
# ✅ Slicing: [start:stop:step] - stop is EXCLUDED
# ✅ Operators: + (concat) * (repeat) in (membership)
# ✅ Case:      .upper() .lower() .title() .capitalize() .swapcase()
# ✅ Search:    .find() .index() .rfind() .count() .startswith() .endswith()
# ✅ Check:     .isalpha() .isdigit() .isalnum() .isspace() .isupper() .islower()
# ✅ Clean:     .strip() .lstrip() .rstrip() .replace()
# ✅ Split:     .split() .splitlines()
# ✅ Join:      " ".join(list)
# ✅ Align:     .center() .ljust() .rjust() .zfill()
# ✅ Escape:    \n \t \\ \" \'
# ✅ Raw:       r"string" - ignores escape sequences
# ✅ Format:    f"{variable:.2f}" ← recommended
# ⚠️  Case sensitive! "Hello" != "hello"
# ⚠️  stop in slicing is EXCLUDED
# ⚠️  Cannot concatenate str + int directly