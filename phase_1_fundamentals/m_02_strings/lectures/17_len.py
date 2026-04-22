# ============================================================
# MODULE 02 | LECTURE 17 - len()
# ============================================================
# What you will learn:
#   - What len() is and what it does
#   - How to use len() with strings
#   - Why len() is so important
#   - len() combined with indexing
#   - len() combined with slicing
#   - len() combined with step slicing
#   - len() with different types of strings
#   - Practical real-world use cases
#   - Common mistakes with len()
# ============================================================


# ------------------------------------------------------------
# PART 1: What is len()?
# ------------------------------------------------------------

# len() is a built-in Python function.
# It returns the NUMBER OF CHARACTERS in a string.
# This number is called the LENGTH of the string.

# Syntax:
#   len(string)
#
# It takes ONE argument (the string you want to measure)
# and returns ONE integer (the number of characters).

word = "Python"
length = len(word)
print(length)       # 6

# "Python" has 6 characters: P, y, t, h, o, n
# len() counts ALL of them and returns 6.

# You can also use len() directly inside print():
print(len("Python"))    # 6
print(len("Hello"))     # 5
print(len("a"))         # 1
print(len(""))          # 0  ← empty string has length 0!


# ------------------------------------------------------------
# PART 2: What counts as a character?
# ------------------------------------------------------------

# len() counts EVERY character - no exceptions.
# Spaces, punctuation, digits, symbols - all count!

# Spaces count:
print(len("Hello World"))   # 11  ← 5 + 1 space + 5 = 11

# Punctuation counts:
print(len("Hello!"))        # 6   ← H,e,l,l,o,! = 6

# Digits inside strings count:
print(len("Python3"))       # 7   ← P,y,t,h,o,n,3 = 7

# Symbols count:
print(len("a@b.com"))       # 7   ← a,@,b,.,c,o,m = 7

# Mixed everything:
sentence = "Hi, I'm 25 years old!"
print(len(sentence))        # 21
# H,i,,, ,I,',m, ,2,5, ,y,e,a,r,s, ,o,l,d,! = 21

# Empty string:
empty = ""
print(len(empty))           # 0  ← zero characters


# ------------------------------------------------------------
# PART 3: Why is len() so important?
# ------------------------------------------------------------

# Remember from Lecture 01 (Indexing)?
# We said: "last index = length - 1"
# But HOW do you know the length without counting manually?
# Answer: len()!

# len() is the bridge between:
#   - the LENGTH of a string (how many characters)
#   - the INDEXES of a string (how to access them)

# ── The critical relationship ──
# For any string s:
#   First valid index  = 0
#   Last valid index   = len(s) - 1
#   First neg. index   = -len(s)
#   Last neg. index    = -1

word = "Python"
length = len(word)
print(length)               # 6

print(word[0])              # P  ← first character
print(word[length - 1])     # n  ← last character (= word[5])
print(word[-1])             # n  ← same thing with negative index
print(word[-length])        # P  ← first character via negative index (= word[-6])

# Now you can access the last character of ANY string
# without knowing its length in advance!

name = input("Enter your name: ")
print(name[len(name) - 1])  # last character of whatever user typed
# OR more elegantly:
print(name[-1])             # same result!


# ------------------------------------------------------------
# PART 4: len() and safe indexing
# ------------------------------------------------------------

# Before len(), we had no safe way to use indexing
# on strings of unknown length.
# Now we can check before accessing!

# ── Safe last character ──
text = "Hello"
if len(text) > 0:               # make sure string is not empty!
    print(text[-1])             # o  ← safe!

# ── Safe access at any position ──
text = "Hi"
position = 5

if position < len(text):        # check if position exists
    print(text[position])
else:
    print(f"Position {position} doesn't exist! String is only {len(text)} chars long.")
# Output: Position 5 doesn't exist! String is only 2 chars long.

# ── Safe middle character ──
word = "Python"
middle_index = len(word) // 2   # integer division (we cover // in Module 01)
print(word[middle_index])       # t  ← middle character (approximately)
# len("Python") = 6
# 6 // 2 = 3
# word[3] = h  ← actually 'h'!
# (The exact middle depends on even/odd length)


# ------------------------------------------------------------
# PART 5: len() with indexing - finding the last index
# ------------------------------------------------------------

# The relationship len(s) - 1 = last index is fundamental.
# Let's explore it thoroughly.

# ── Different strings, same pattern ──
strings = ["cat", "Python", "Bioinformatics", "a", "Hello World"]

for s in strings:
    last_index = len(s) - 1
    print(f"'{s}' → length={len(s)}, last index={last_index}, last char='{s[-1]}'")

# Output:
# 'cat' → length=3, last index=2, last char='t'
# 'Python' → length=6, last index=5, last char='n'
# 'Bioinformatics' → length=14, last index=13, last char='s'
# 'a' → length=1, last index=0, last char='a'
# 'Hello World' → length=11, last index=10, last char='d'

# ── Verify: word[len(word)-1] == word[-1] ──
word = "Genetics"
print(word[len(word) - 1])  # s
print(word[-1])              # s
print(word[len(word) - 1] == word[-1])  # True  ← always!


# ------------------------------------------------------------
# PART 6: len() combined with slicing
# ------------------------------------------------------------

# len() becomes extremely powerful when combined with slicing.
# You can calculate slice positions dynamically!

# ── Get the second half of a string ──
word = "Python"
half = len(word) // 2      # 6 // 2 = 3
first_half  = word[:half]  # word[:3] = "Pyt"
second_half = word[half:]  # word[3:] = "hon"
print(first_half)           # Pyt
print(second_half)          # hon

# ── Works for ANY string ──
text = "Bioinformatics"
half = len(text) // 2      # 14 // 2 = 7
print(text[:half])          # Bioinf
print(text[half:])          # ormatics

# ── Get the first third of a string ──
word = "abcdefghilmno"
third = len(word) // 3     # 13 // 3 = 4
print(word[:third])         # abcd

# ── Get last n characters using len() ──
# (Alternatively use negative slicing, but len() makes it explicit)
word = "Python"
n = 3
print(word[len(word) - n:])     # hon  ← last 3 characters
print(word[-n:])                 # hon  ← same, using negative index

# ── Dynamic center slice ──
word = "abcdefg"         # length 7
center = len(word) // 2  # 3
print(word[center-1:center+2])  # cde  ← 3 characters around center


# ------------------------------------------------------------
# PART 7: len() combined with step slicing
# ------------------------------------------------------------

# len() helps you calculate step sizes and ranges dynamically.

# ── Take every nth character where n = length // 3 ──
word = "abcdefghilmn"  # length 12
step = len(word) // 3  # 12 // 3 = 4
print(word[::step])    # aei  ← every 4th character

# ── Verify a string reversal ──
word = "Python"
reversed_word = word[::-1]
print(len(word))         # 6
print(len(reversed_word))# 6  ← same length! reversal never changes length

# ── Use len() to find the middle for palindrome check ──
word = "racecar"
length = len(word)
half = length // 2

# Check first half against reversed second half:
print(word[:half])              # rac
print(word[length - half:][::-1])   # rac  ← second half reversed
print(word[:half] == word[length - half:][::-1])  # True → palindrome!


# ------------------------------------------------------------
# PART 8: len() with empty strings and edge cases
# ------------------------------------------------------------

# ── Empty string ──
empty = ""
print(len(empty))       # 0

# Trying to index an empty string → IndexError!
# print(empty[0])       # ❌ IndexError

# Safe way:
if len(empty) > 0:
    print(empty[0])
else:
    print("String is empty!")  # This runs

# ── Single character string ──
single = "X"
print(len(single))      # 1
print(single[0])        # X   ← valid
print(single[-1])       # X   ← valid (same character!)
print(single[0] == single[-1])  # True

# ── String with only spaces ──
spaces = "   "           # 3 spaces
print(len(spaces))      # 3  ← spaces ARE characters!

# ── String with newline characters ──
multiline = "Hello\nWorld"   # \n is ONE character (newline)
print(len(multiline))   # 11  ← H,e,l,l,o,\n,W,o,r,l,d = 11

# ── String with tab character ──
tabbed = "Hello\tWorld"   # \t is ONE character (tab)
print(len(tabbed))      # 11  ← same count as above


# ------------------------------------------------------------
# PART 9: len() stored vs inline
# ------------------------------------------------------------

# You can use len() in two ways:
# 1. Store the result in a variable first
# 2. Call it inline directly where you need it

word = "Python"

# ── Storing in a variable (better when using multiple times) ──
length = len(word)
print(length)                   # 6
print(word[length - 1])         # n
print(word[length // 2])        # h
print(word[:length // 2])       # Pyt

# ── Inline (better for one-time use) ──
print(len(word))                # 6
print(word[len(word) - 1])      # n
print(word[len(word) // 2])     # h

# ── When to store vs inline? ──
# Store when you use the length MORE THAN ONCE in your code.
# Calling len() multiple times on the same string is fine
# (Python is fast), but storing improves readability.

# ✅ Good - store when used multiple times:
length = len(word)
first_half = word[:length // 2]
second_half = word[length // 2:]
last_char = word[length - 1]

# ✅ Also fine - inline when used once:
print(len(word) > 5)            # True


# ------------------------------------------------------------
# PART 10: len() and comparison
# ------------------------------------------------------------

# len() returns an integer, so you can use it in comparisons.

# ── Compare lengths of two strings ──
word1 = "cat"
word2 = "elephant"
print(len(word1) < len(word2))      # True   (3 < 8)
print(len(word1) == len(word2))     # False
print(len(word1) > len(word2))      # False

# ── Check minimum length ──
password = "abc123"
if len(password) >= 8:
    print("Password is long enough")
else:
    print(f"Password too short! ({len(password)}/8 characters)")
# Output: Password too short! (6/8 characters)

# ── Check exact length ──
code = "AB12"
if len(code) == 4:
    print("Valid code format")
else:
    print("Invalid code format")
# Output: Valid code format

# ── Check if string is empty ──
text = ""
if len(text) == 0:
    print("Empty string!")
# Output: Empty string!

# Pythonic way (more advanced, preview):
# if not text:  ← empty string is "falsy" in Python
#     print("Empty!")


# ------------------------------------------------------------
# PART 11: len() in arithmetic expressions
# ------------------------------------------------------------

# Since len() returns an integer, you can do math with it!

word = "Bioinformatics"
n = len(word)           # 14

print(n)                # 14
print(n + 1)            # 15
print(n - 1)            # 13  ← last valid index!
print(n * 2)            # 28
print(n // 2)           # 7   ← midpoint
print(n % 2)            # 0   ← even length (0 = even, 1 = odd)

# Is the string length even or odd?
if len(word) % 2 == 0:
    print(f"'{word}' has EVEN length ({len(word)})")
else:
    print(f"'{word}' has ODD length ({len(word)})")
# Output: 'Bioinformatics' has EVEN length (14)

# ── Find true center of odd-length string ──
word = "racecar"         # length 7 → true center at index 3
n = len(word)
center = n // 2
print(word[center])     # e  ← the true center character!

# ── Find center of even-length string ──
word = "Python"          # length 6 → no single center, two middle chars
n = len(word)
left_center  = n // 2 - 1  # index 2 → t
right_center = n // 2      # index 3 → h
print(word[left_center])    # t
print(word[right_center])   # h


# ------------------------------------------------------------
# PART 12: Common mistakes with len()
# ------------------------------------------------------------

# ── Mistake 1: Using len() as if it's the last index ──
word = "Python"
# ❌ Wrong:
# print(word[len(word)])    # IndexError! len()=6, last index=5

# ✅ Correct:
print(word[len(word) - 1])  # n  ← subtract 1!

# ── Mistake 2: Forgetting len() returns int, not string ──
word = "Hello"
length = len(word)
# ❌ Wrong:
# print("Length: " + length)  # TypeError: can only concatenate str to str

# ✅ Correct:
print("Length: " + str(length))    # Length: 5
print(f"Length: {length}")          # Length: 5  ← f-string is easier!

# ── Mistake 3: Calling len() on a number ──
number = 12345
# print(len(number))    # ❌ TypeError: object of type 'int' has no len()

# ✅ Convert to string first if you need length of digits:
print(len(str(number))) # 5  ← number has 5 digits

# ── Mistake 4: Confusing length with last index ──
word = "Python"
# Length = 6  (how many characters)
# Last index = 5  (length - 1)
# These are DIFFERENT numbers!
print(len(word))            # 6  ← the LENGTH
print(len(word) - 1)        # 5  ← the LAST INDEX


# ------------------------------------------------------------
# PART 13: Real world applications
# ------------------------------------------------------------

# ── Application 1: Validate username length ──
username = "anna_kowalska"
min_length = 3
max_length = 20

if len(username) < min_length:
    print(f"Username too short! Minimum {min_length} characters.")
elif len(username) > max_length:
    print(f"Username too long! Maximum {max_length} characters.")
else:
    print(f"Username '{username}' is valid! ({len(username)} characters)")
# Output: Username 'anna_kowalska' is valid! (13 characters)

# ── Application 2: Truncate long text ──
title = "Introduction to Bioinformatics and Computational Biology"
max_length = 30

if len(title) > max_length:
    truncated = title[:max_length] + "..."
    print(truncated)
else:
    print(title)
# Output: Introduction to Bioinformat...

# ── Application 3: Center a string in a fixed width ──
word = "Python"
width = 20
spaces_total = width - len(word)
spaces_left = spaces_total // 2
centered = " " * spaces_left + word
print(centered)         # "       Python"

# ── Application 4: Count digits in a number ──
number = 123456789
digit_count = len(str(number))
print(f"The number {number} has {digit_count} digits.")
# Output: The number 123456789 has 9 digits.

# ── Application 5: Validate fixed-length code ──
product_code = "EL-4521-WW"
if len(product_code) == 10:
    print("Valid product code format")
else:
    print(f"Invalid! Expected 10 characters, got {len(product_code)}")

# ── Application 6: Split string into two equal halves ──
word = "Python"
if len(word) % 2 == 0:              # only works for even length
    mid = len(word) // 2
    print(word[:mid])               # Pyt
    print(word[mid:])               # hon
else:
    print("Odd length - cannot split evenly")

# ── Application 7: Check if DNA sequence is valid length ──
dna = "ATGCCCGCA"
if len(dna) % 3 == 0:
    print(f"Valid! Sequence length {len(dna)} is divisible by 3 (complete codons).")
else:
    print(f"Warning! Sequence length {len(dna)} is NOT divisible by 3.")
# Output: Valid! Sequence length 9 is divisible by 3 (complete codons).


# ------------------------------------------------------------
# PART 14: len() preview - works on more than strings!
# ------------------------------------------------------------

# len() is not limited to strings.
# It works on ANY sequence in Python.
# You'll use it constantly with lists, tuples, and more.

# String (current topic):
print(len("Python"))        # 6

# List (Module 05 - coming soon):
# print(len([1, 2, 3, 4]))  # 4

# Tuple (Module 05):
# print(len((1, 2, 3)))     # 3

# Dictionary (Module 05):
# print(len({"a": 1, "b": 2}))  # 2

# The concept is always the same:
# len() = "how many items are in this container?"
# For strings: how many characters?
# For lists:   how many elements?
# etc.

# So mastering len() with strings now means you
# already understand it for everything else too!


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ len(string) returns the number of characters as an integer
# ✅ ALL characters count: spaces, punctuation, digits, symbols
# ✅ Empty string "" has length 0
# ✅ Last valid index = len(s) - 1   (NOT len(s)!)
# ✅ First negative index = -len(s)
# ✅ len() returns int → use str() or f-string to print with text
# ✅ len() on int → TypeError (convert with str() first)
# ✅ len() + indexing → safe access to any position
# ✅ len() + slicing → dynamic, length-independent slices
# ✅ len() + arithmetic → midpoint, thirds, even/odd checks
# ✅ len() + comparison → validate, truncate, check lengths
# ✅ Store in variable when used multiple times
# ✅ len() works on lists, tuples, dicts too (Module 05)