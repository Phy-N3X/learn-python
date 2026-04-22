# ============================================================
# MODULE 02 | LECTURE 13 - String Indexing
# ============================================================
# What you will learn:
#   - What a sequence is and why strings are sequences
#   - What an index is and how it works
#   - Why indexing starts at 0 (not 1)
#   - How to access individual characters
#   - What IndexError is and how to avoid it
#   - Why strings are immutable
#   - How to use indexing in real scenarios
#   - How spaces and special characters are indexed
#   - Indexing with variables and expressions
# ============================================================


# ------------------------------------------------------------
# PART 1: Strings are sequences
# ------------------------------------------------------------

# Before we talk about indexing, we need to understand
# what kind of thing a string actually IS.

# A string is not just "some text".
# A string is a SEQUENCE - an ordered collection of characters.
# The word "ordered" is crucial here.

# What does "ordered" mean?
#   - Every character has a fixed, specific position
#   - The order never changes unless you create a new string
#   - "Python" is NOT the same as "Ptyohn" - order matters!

# This is different from, say, a bag of letters
# where order doesn't matter.
# A string is more like a row of seats in a cinema:
# seat 1, seat 2, seat 3... each has a specific position.

word = "Python"
print(word)     # Python

# The string "Python" always has:
#   P at position 0
#   y at position 1
#   t at position 2
#   h at position 3
#   o at position 4
#   n at position 5
# This never changes.


# ------------------------------------------------------------
# PART 2: What is an index?
# ------------------------------------------------------------

# An INDEX is a number that represents the POSITION
# of a character inside a string.

# Think of a street with houses:
#   House 0: P
#   House 1: y
#   House 2: t
#   House 3: h
#   House 4: o
#   House 5: n

# To visit house number 3, you go to address [3].
# In Python, you do the same with square brackets:

word = "Python"
print(word[0])  # P
print(word[1])  # y
print(word[2])  # t
print(word[3])  # h
print(word[4])  # o
print(word[5])  # n

# The syntax is always:
#   string[index]
#   ↑              ↑
#   your string    position you want

# The result is always a STRING of length 1
# (a single character is still a string in Python)

character = word[2]
print(character)        # t
print(type(character))  # <class 'str'>


# ------------------------------------------------------------
# PART 3: Why does indexing start at 0?
# ------------------------------------------------------------

# This is one of the most common questions beginners ask.
# "Why not start at 1? That's more natural!"

# The short answer: it comes from mathematics and C language.
# The index represents an OFFSET from the beginning.

# Offset = how many steps away from the start?
#
#   word[0] → 0 steps from the start → FIRST character
#   word[1] → 1 step from the start  → SECOND character
#   word[2] → 2 steps from the start → THIRD character
#
# It's like measuring distance:
#   You are standing at the door (position 0).
#   The first room IS the door (0 steps away).
#   The second room is 1 step away.

# Most programming languages use 0-based indexing:
# Python, JavaScript, C, C++, Java, C#, Go, Ruby...
# Some use 1-based: Lua, MATLAB, R, Fortran
# Python follows the majority convention.

# Pro tip: after a few weeks of practice,
# 0-based indexing will feel completely natural.
# Every programmer struggles with this at first!

sentence = "Hello"
#  H  e  l  l  o
#  0  1  2  3  4

print(sentence[0])  # H  ← position 0 = first
print(sentence[4])  # o  ← position 4 = fifth (last)


# ------------------------------------------------------------
# PART 4: Visualizing indexes - the full picture
# ------------------------------------------------------------

# Let's map out several strings completely:

# ── Example 1: short word ──
# word = "cat"
#  c  a  t
#  0  1  2

# ── Example 2: longer word ──
# word = "programming"
#  p  r  o  g  r  a  m  m  i  n  g
#  0  1  2  3  4  5  6  7  8  9  10

# ── Example 3: with spaces ──
# phrase = "I love Python"
#  I     l  o  v  e     P  y  t  h  o  n
#  0  1  2  3  4  5  6  7  8  9 10 11 12
#  ↑        ↑           ↑
# 'I'    space         'P'
# Yes! Spaces are characters too and have indexes!

phrase = "I love Python"
print(phrase[0])    # I
print(phrase[1])    # (space)
print(phrase[7])    # P
print(phrase[12])   # n

# ── Example 4: with numbers in the string ──
# code = "A1B2C3"
#  A  1  B  2  C  3
#  0  1  2  3  4  5

code = "A1B2C3"
print(code[0])  # A
print(code[1])  # 1  ← this is the CHARACTER "1", not the number 1!
print(code[4])  # C


# ------------------------------------------------------------
# PART 5: Spaces, punctuation, and special characters
# ------------------------------------------------------------

# Every single character in a string has an index.
# This includes:
#   - spaces
#   - punctuation marks (. , ! ? ; :)
#   - digits inside strings ("1", "2")
#   - symbols (@ # $ % &)
#   - special characters (\n, \t - we cover these later)

sentence = "Hi, World!"
#  H  i  ,     W  o  r  l  d  !
#  0  1  2  3  4  5  6  7  8  9

print(sentence[0])  # H
print(sentence[2])  # ,   ← comma!
print(sentence[3])  # (space)
print(sentence[4])  # W
print(sentence[9])  # !   ← exclamation mark!

# This is important for parsing text:
# knowing exactly where punctuation is located.


# ------------------------------------------------------------
# PART 6: IndexError - the most common beginner mistake
# ------------------------------------------------------------

# If you try to access an index that doesn't exist,
# Python raises an IndexError and your program CRASHES.

word = "Python"   # valid indexes: 0, 1, 2, 3, 4, 5

# print(word[6])
# ❌ IndexError: string index out of range
#
# "Python" has 6 characters.
# The LAST valid index is always: length - 1
# length = 6, so last index = 6 - 1 = 5

# Common mistake: thinking the last index equals the length
# ❌ Wrong thinking: "6 characters → last index is 6"
# ✅ Right thinking: "6 characters → last index is 5"

# Why? Because we start counting at 0:
# 0, 1, 2, 3, 4, 5 → that's 6 numbers, last one is 5

# Another common mistake: negative numbers (we cover in next lecture)
# print(word[-1])  # This actually WORKS - explained in Lecture 02!

# For now: keep indexes between 0 and length-1
# We'll learn len() in Lecture 05 to calculate this safely.

word = "hi"     # valid indexes: 0, 1 only
print(word[0])  # h ✅
print(word[1])  # i ✅
# print(word[2]) # ❌ IndexError!


# ------------------------------------------------------------
# PART 7: Strings are IMMUTABLE
# ------------------------------------------------------------

# You can READ any character using its index.
# But you CANNOT CHANGE a character using its index.
# This is because strings in Python are IMMUTABLE.

# Immutable = cannot be modified after creation.

# Think of it like a printed book:
# You can open page 42 and READ it.
# But you cannot reach into the book and CHANGE a letter.
# If you want a different version, you print a NEW book.

word = "Python"
print(word[0])      # P  ← reading ✅

# word[0] = "J"
# ❌ TypeError: 'str' object does not support item assignment
#
# Python refuses to change the string in place.

# ✅ If you want to "change" a string, create a NEW one:
word = "J" + word[1:]   # we'll learn slicing soon!
print(word)             # Jython

# Why immutable? It's a design choice.
# Immutable strings are:
#   - safer (no accidental modifications)
#   - faster (Python can optimize them in memory)
#   - hashable (can be used as dictionary keys - later topic)


# ------------------------------------------------------------
# PART 8: Indexing with variables and expressions
# ------------------------------------------------------------

# The index inside [] doesn't have to be a literal number.
# It can be any expression that evaluates to an integer.

word = "Python"

# Using a variable as index:
i = 3
print(word[i])          # h  ← same as word[3]

# Using a calculation as index:
print(word[1 + 2])      # h  ← 1+2=3, same as word[3]
print(word[2 * 2])      # o  ← 2*2=4, same as word[4]

# This becomes VERY powerful with loops (Module 04):
# for i in range(6):
#     print(word[i])    # prints P, y, t, h, o, n one by one

# For now, let's do it manually to understand the concept:
dna = "ATCG"
position = 0
print(dna[position])    # A

position = 1
print(dna[position])    # T

position = 2
print(dna[position])    # C

position = 3
print(dna[position])    # G


# ------------------------------------------------------------
# PART 9: Indexing string literals directly
# ------------------------------------------------------------

# You don't always need to store a string in a variable first.
# You can index a string literal directly:

print("Hello"[0])       # H
print("Hello"[4])       # o
print("Python"[2])      # t

# You can also index the result of a function:
name = input("Enter your name: ")
print(name[0])          # First letter of whatever user typed

# Or index a concatenated string:
first = "Good"
second = "Morning"
combined = first + " " + second
print(combined[5])      # M  ← first letter of "Morning"


# ------------------------------------------------------------
# PART 10: Practical use cases
# ------------------------------------------------------------

# Indexing is not just an academic exercise.
# Here are real situations where it's useful:

# ── Use case 1: Get initials ──
first_name = "Anna"
last_name = "Kowalska"
initials = first_name[0] + "." + last_name[0] + "."
print(initials)         # A.K.

# ── Use case 2: Check file extension character ──
filename = "report.pdf"
# Is the 7th character a dot?
print(filename[6])      # .   ← yes, it's the dot before extension

# ── Use case 3: Read a specific nucleotide ──
dna_sequence = "ATGCTAGCTA"
codon_start = dna_sequence[0]   # First nucleotide
print(codon_start)              # A

# ── Use case 4: Get area code from phone number ──
phone = "48123456789"
first_digit = phone[0]
second_digit = phone[1]
area_code = first_digit + second_digit
print(area_code)        # 48

# ── Use case 5: Check if a string starts with uppercase ──
word = "Python"
first_char = word[0]
print(first_char)           # P
print(first_char.isupper()) # True  ← method we learn later!


# ------------------------------------------------------------
# PART 11: How Python stores strings in memory
# ------------------------------------------------------------

# When you write: word = "Python"
# Python creates a block of memory that looks like this:
#
#   ┌───┬───┬───┬───┬───┬───┐
#   │ P │ y │ t │ h │ o │ n │
#   └───┴───┴───┴───┴───┴───┘
#     0   1   2   3   4   5
#
# The variable 'word' points to the START of this block.
# When you write word[3], Python:
#   1. Finds the start of the string
#   2. Jumps exactly 3 positions forward
#   3. Returns the character at that position
#
# This is WHY indexing is so fast - it's a direct jump,
# not a search through the whole string.
# word[0] and word[1000] take the same amount of time!

# This also explains why indexes start at 0:
# 0 means "jump 0 positions = start right here"

word = "Python"
print(word[0])  # P ← no jump, read immediately
print(word[5])  # n ← jump 5 positions, read


# ------------------------------------------------------------
# PART 12: Single-character strings
# ------------------------------------------------------------

# In Python, there is NO separate "character" type.
# A single character is just a string of length 1.

word = "Python"
char = word[0]

print(char)             # P
print(type(char))       # <class 'str'>  ← still a string!
print(len(char))        # 1  ← length is 1

# You can do everything with it that you do with strings:
print(char.lower())     # p
print(char + "!")       # P!
print(char * 3)         # PPP  ← string multiplication (Lecture 17)

# Compare with other languages:
# In C/Java: char c = 'P';  ← separate data type
# In Python: c = "P"        ← just a string of length 1


# ------------------------------------------------------------
# PART 13: Checking if index exists safely
# ------------------------------------------------------------

# Before we learn len() (Lecture 05), here's the concept:
# The safe range of indexes for a string is: 0 to len-1

# UNSAFE - might crash:
# user_input = input("Enter something: ")
# print(user_input[5])  # What if user typed only 2 characters?

# SAFE - check first:
# (We'll learn this properly with if statements in Module 03)
# if len(user_input) > 5:
#     print(user_input[5])
# else:
#     print("String is too short!")

# For now, just remember:
# Always make sure the index exists before using it!

text = "Hi"
print(len(text))    # 2  ← only indexes 0 and 1 are valid


# ------------------------------------------------------------
# PART 14: Summary table
# ------------------------------------------------------------

# Let's put it all together with one example:

word = "Bioinformatics"
#  B  i  o  i  n  f  o  r  m  a  t  i  c  s
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13

print(word[0])   # B   ← first character
print(word[1])   # i
print(word[9])   # a
print(word[13])  # s   ← last character (length=14, last index=13)

# Key rules to remember:
# ✅ First character is always at index 0
# ✅ Last character is always at index length-1
# ✅ Spaces and punctuation have indexes too
# ✅ Strings are immutable - read only via indexing
# ✅ Index can be a variable or expression
# ✅ IndexError happens when index >= length


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ A string is an ORDERED SEQUENCE of characters
# ✅ Each character has a POSITION called an INDEX
# ✅ Indexes start at 0 (not 1!)
# ✅ Syntax: string[index]
# ✅ First character → index 0
# ✅ Last character  → index length - 1
# ✅ Spaces and punctuation are characters with indexes
# ✅ Strings are IMMUTABLE - you can read but not change
# ✅ IndexError = you went out of bounds
# ✅ A single character is still a string (type = str)
# ✅ Index can be a variable or any integer expression
# ✅ Indexing is O(1) - instant access regardless of position