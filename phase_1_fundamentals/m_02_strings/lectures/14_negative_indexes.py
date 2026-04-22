# ============================================================
# MODULE 02 | LECTURE 14 - Negative Indexes
# ============================================================
# What you will learn:
#   - What negative indexes are
#   - Why they exist and why they are useful
#   - How negative indexing maps to positive indexing
#   - The full index map (positive AND negative)
#   - Common use cases for negative indexes
#   - How to avoid mistakes with negative indexes
#   - Combining positive and negative indexes
# ============================================================


# ------------------------------------------------------------
# PART 1: The problem that negative indexes solve
# ------------------------------------------------------------

# In Lecture 01 we learned positive indexing.
# It works great for accessing characters from the LEFT side.
# But what if you want the LAST character of a string?

# With positive indexing you need to know the length:
word = "Python"
# last character = word[5]   ← but how do I know it's 5?
# last character = word[length - 1]

# What if the string changes length?
# What if you receive a string from the user
# and you don't know how long it is?

name = input("Enter your name: ")  # could be 3 or 30 characters
# last_char = name[???]   ← you don't know the index!

# This is exactly the problem negative indexes solve.
# Python lets you count from the RIGHT side using negative numbers.

word = "Python"
print(word[-1])     # n  ← last character, always!
# No matter how long the string is, [-1] is always the last.


# ------------------------------------------------------------
# PART 2: How negative indexes work - the concept
# ------------------------------------------------------------

# Negative indexes count from the END of the string.
# They start at -1 (not -0, because -0 == 0).

# Think of it like this:
# Positive indexes count from the LEFT  → 0, 1, 2, 3...
# Negative indexes count from the RIGHT → -1, -2, -3...

# Imagine a number line:
#
#   ◄── negative side    positive side ──►
#   -6  -5  -4  -3  -2  -1  |  0   1   2   3   4   5
#    P   y   t   h   o   n  |  P   y   t   h   o   n
#
# Both sides describe the SAME string!
# -1 and 5 both point to "n"
# -6 and 0 both point to "P"

word = "Python"
print(word[-1])     # n
print(word[-2])     # o
print(word[-3])     # h
print(word[-4])     # t
print(word[-5])     # y
print(word[-6])     # P


# ------------------------------------------------------------
# PART 3: The complete index map
# ------------------------------------------------------------

# Every character has TWO valid indexes: positive and negative.
# Let's map them out completely:

# word = "Python"
#
#  ┌────┬────┬────┬────┬────┬────┐
#  │ P  │ y  │ t  │ h  │ o  │ n  │
#  ├────┼────┼────┼────┼────┼────┤
#  │  0 │  1 │  2 │  3 │  4 │  5 │  ← positive indexes
#  │ -6 │ -5 │ -4 │ -3 │ -2 │ -1 │  ← negative indexes
#  └────┴────┴────┴────┴────┴────┘

# Verification - both indexes give the same character:
word = "Python"

print(word[0],  word[-6])   # P P   ← same character!
print(word[1],  word[-5])   # y y
print(word[2],  word[-4])   # t t
print(word[3],  word[-3])   # h h
print(word[4],  word[-2])   # o o
print(word[5],  word[-1])   # n n

# The relationship between positive and negative index:
# negative_index = positive_index - length
# positive_index = negative_index + length
#
# Example: length = 6
# positive[0] → negative = 0 - 6 = -6 ✅
# positive[5] → negative = 5 - 6 = -1 ✅
# negative[-1] → positive = -1 + 6 = 5 ✅
# negative[-6] → positive = -6 + 6 = 0 ✅


# ------------------------------------------------------------
# PART 4: Why -1 and not -0?
# ------------------------------------------------------------

# Good question! Why does negative indexing start at -1?
# Why isn't the last character at index -0?

# Mathematical reason:
# In Python (and most languages): -0 == 0
# They are the same number!
# So -0 would just be the same as 0 (first character).
# That would be confusing and useless.

print(-0 == 0)      # True  ← -0 and 0 are identical!

# So Python starts negative indexing at -1 (last character)
# and goes further back: -2, -3, -4...

# This means:
# word[-1]  → last character
# word[-2]  → second to last
# word[-3]  → third to last
# ... and so on


# ------------------------------------------------------------
# PART 5: Negative index out of range
# ------------------------------------------------------------

# Just like positive indexes, negative indexes have limits.
# You cannot go further than -(length) from the right.

word = "Python"  # length = 6
# Valid negative indexes: -1, -2, -3, -4, -5, -6
# Invalid: -7, -8, -100...

print(word[-6])     # P  ✅ valid (same as word[0])

# print(word[-7])
# ❌ IndexError: string index out of range
#
# -7 would mean "7 positions from the right"
# but the string only has 6 characters!

# Summary of valid indexes for a string of length n:
#   Positive: 0 to n-1
#   Negative: -n to -1

# For "Python" (n=6):
#   Positive: 0 to 5
#   Negative: -6 to -1


# ------------------------------------------------------------
# PART 6: The most useful negative index - [-1]
# ------------------------------------------------------------

# By far the most common use of negative indexing is [-1].
# It always gives you the LAST character,
# regardless of the string's length.

# This is extremely useful in real code:

# ── Example 1: Check the last character ──
word1 = "hello"
word2 = "programming"
word3 = "a"

print(word1[-1])    # o
print(word2[-1])    # g
print(word3[-1])    # a  ← works even for single character!

# ── Example 2: Check file extension ──
filename1 = "report.pdf"
filename2 = "data.csv"
filename3 = "script.py"

print(filename1[-3:])   # pdf  ← slicing (next lecture!)
print(filename1[-1])    # f    ← last character

# ── Example 3: Check last digit of a number (as string) ──
id_number = "9876543210"
last_digit = id_number[-1]
print(last_digit)       # 0


# ------------------------------------------------------------
# PART 7: Common negative indexes and their meaning
# ------------------------------------------------------------

word = "abcdefgh"
#  a  b  c  d  e  f  g  h
# -8 -7 -6 -5 -4 -3 -2 -1

print(word[-1])     # h  ← last character
print(word[-2])     # g  ← second to last
print(word[-3])     # f  ← third to last
print(word[-4])     # e  ← middle-ish

# A useful way to remember:
# [-1]  = last
# [-2]  = second to last
# [-3]  = third to last
# ...and so on


# ------------------------------------------------------------
# PART 8: Combining positive and negative indexes
# ------------------------------------------------------------

# You can freely mix positive and negative indexes.
# Use whichever is more convenient for the situation.

word = "Python"

# From the left side (positive):
first = word[0]     # P
second = word[1]    # y

# From the right side (negative):
last = word[-1]         # n
second_to_last = word[-2]   # o

print(first)            # P
print(second)           # y
print(last)             # n
print(second_to_last)   # o

# ── Real example: get first and last character ──
text = "Hello"
print(text[0] + text[-1])      # Ho

text = "Supercalifragilistic"
print(text[0] + text[-1])      # Sc  ← works for any length!

# ── Real example: check if string is symmetric ──
word = "racecar"
print(word[0] == word[-1])     # True  ← first = last
print(word[1] == word[-2])     # True  ← second = second-to-last
print(word[2] == word[-3])     # True


# ------------------------------------------------------------
# PART 9: Negative indexes with variables
# ------------------------------------------------------------

# Just like positive indexes, you can use variables
# and expressions as negative indexes.

word = "Python"

i = -1
print(word[i])          # n

i = -3
print(word[i])          # h

# Using expressions:
print(word[-1 * 2])     # o  ← -2, second to last
print(word[-(1 + 2)])   # h  ← -3, third to last

# This becomes powerful with loops (Module 04):
# for i in range(-1, -7, -1):
#     print(word[i])    # prints n, o, h, t, y, P (reversed!)

# For now, manually:
name = "Anna"
print(name[-1])     # a
print(name[-2])     # n
print(name[-3])     # n
print(name[-4])     # A


# ------------------------------------------------------------
# PART 10: Practical use cases
# ------------------------------------------------------------

# ── Use case 1: Get file extension ──
filename = "genome_data.fasta"
# Extension starts 6 characters from the end: .fasta
# Or we can just grab individual chars:
print(filename[-5])     # f  ← start of "fasta"
print(filename[-6])     # .  ← the dot

# ── Use case 2: Check last letter for grammar ──
noun = "cats"
if noun[-1] == "s":
    print("This noun is probably plural")
else:
    print("This noun might be singular")

# ── Use case 3: Get last digit of a year ──
year = "2024"
print(year[-1])         # 4

# ── Use case 4: Reverse engineering a code ──
secret_code = "XK9Z"
print("First char:", secret_code[0])    # X
print("Last char:", secret_code[-1])    # Z

# ── Use case 5: Check both ends of a DNA sequence ──
dna = "ATGCCCGCATTA"
print("Start codon starts with:", dna[0])   # A
print("Last nucleotide:", dna[-1])          # A


# ------------------------------------------------------------
# PART 11: Negative indexes and string length relationship
# ------------------------------------------------------------

# There is a precise mathematical relationship:
# For any valid index i:
#   word[i] == word[i + len(word)]   (for negative i)
#   word[i] == word[i - len(word)]   (for positive i)

word = "Python"
length = len(word)   # 6

# Verify:
print(word[-1] == word[-1 + length])    # True → word[-1] == word[5]
print(word[-3] == word[-3 + length])    # True → word[-3] == word[3]
print(word[0]  == word[0 - length])     # True → word[0]  == word[-6]
print(word[2]  == word[2 - length])     # True → word[2]  == word[-4]

# Python internally converts negative indexes to positive ones:
# word[-1] → word[-1 + 6] → word[5] → "n"
# This conversion happens automatically behind the scenes.


# ------------------------------------------------------------
# PART 12: Negative indexing on different string types
# ------------------------------------------------------------

# Negative indexing works on ANY string, no matter how it's created.

# String literal directly:
print("Hello"[-1])          # o
print("Hello"[-3])          # l

# String from variable:
greeting = "Good morning"
print(greeting[-1])         # g
print(greeting[-7])         # m

# String from concatenation:
first = "Good"
space = " "
second = "morning"
combined = first + space + second
print(combined[-1])         # g

# String from multiplication:
repeated = "ab" * 3         # "ababab"
print(repeated[-1])         # b
print(repeated[-2])         # a

# Single character string:
single = "X"
print(single[-1])           # X  ← works! -1 == 0 for length-1 string
print(single[0] == single[-1])  # True


# ------------------------------------------------------------
# PART 13: The full picture - both index types together
# ------------------------------------------------------------

# Let's do a complete example with a longer string:

sentence = "I love Python"
#
#  I     l  o  v  e     P  y  t  h  o  n
#  0  1  2  3  4  5  6  7  8  9 10 11 12   ← positive
# -13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1  ← negative

print(sentence[0])      # I
print(sentence[-13])    # I  ← same character!

print(sentence[7])      # P
print(sentence[-6])     # P  ← same character!

print(sentence[12])     # n
print(sentence[-1])     # n  ← same character!

# Which one to use?
# Use POSITIVE when counting from the LEFT is more natural.
# Use NEGATIVE when counting from the RIGHT is more natural.
# Always choose the one that makes your code MORE READABLE.

# ✅ Clear and readable:
first_char = sentence[0]        # first character
last_char = sentence[-1]        # last character

# ❌ Confusing (works but hard to read):
first_char = sentence[-13]      # why -13?? hard to understand
last_char = sentence[12]        # you need to know the length


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Negative indexes count from the RIGHT side of the string
# ✅ They start at -1 (not -0, because -0 == 0)
# ✅ word[-1]  = last character
# ✅ word[-2]  = second to last character
# ✅ word[-n]  = first character (where n = length)
# ✅ Every character has two valid indexes: positive and negative
# ✅ Valid range: -length to -1 (negative), 0 to length-1 (positive)
# ✅ IndexError if you go beyond -length
# ✅ Use positive for "from the left", negative for "from the right"
# ✅ Internally: word[-i] == word[-i + length]
# ✅ Mixing positive and negative indexes is perfectly fine