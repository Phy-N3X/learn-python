# ============================================================
# MODULE 02 | LECTURE 03 - Slicing
# ============================================================
# What you will learn:
#   - What slicing is and why it exists
#   - The basic slicing syntax: string[start:stop]
#   - How start and stop work (including the "stop is excluded" rule)
#   - Slicing from the beginning and to the end
#   - Slicing with negative indexes
#   - Slicing the whole string
#   - What happens with out-of-range slice indexes
#   - Slicing creates a NEW string
#   - Practical real-world use cases
# ============================================================


# ------------------------------------------------------------
# PART 1: The problem that slicing solves
# ------------------------------------------------------------

# In the previous two lectures we learned indexing.
# Indexing gives you ONE character at a time.

# But what if you want a RANGE of characters?
# What if you want:
#   - The first 3 characters of a string?
#   - Characters from position 2 to position 7?
#   - The last 4 characters?
#   - Everything except the first character?

# Without slicing, you would have to do this:
word = "Python"
first_three = word[0] + word[1] + word[2]
print(first_three)      # Pyt

# That works for 3 characters, but what about 50?
# Clearly we need a better tool. That tool is SLICING.

# With slicing:
first_three = word[0:3]
print(first_three)      # Pyt  ← same result, much cleaner!


# ------------------------------------------------------------
# PART 2: Basic slicing syntax
# ------------------------------------------------------------

# Slicing syntax:
#   string[start:stop]
#
# start = index where the slice BEGINS (included)
# stop  = index where the slice ENDS   (NOT included!)
#
# The result is a new string containing characters
# from index 'start' up to BUT NOT INCLUDING index 'stop'.

word = "Python"
#  P  y  t  h  o  n
#  0  1  2  3  4  5

print(word[0:3])    # Pyt   → characters at index 0, 1, 2
print(word[1:4])    # yth   → characters at index 1, 2, 3
print(word[2:5])    # tho   → characters at index 2, 3, 4
print(word[0:6])    # Python → characters at index 0, 1, 2, 3, 4, 5


# ------------------------------------------------------------
# PART 3: The "stop is excluded" rule - WHY?
# ------------------------------------------------------------

# This is the most important rule in slicing,
# and also the one that confuses beginners the most.
#
# word[0:3] gives you characters at index 0, 1, 2
# It does NOT include the character at index 3!
#
# Why? This is a deliberate design decision. Here's why it's smart:

# ── Reason 1: The length of the slice is easy to calculate ──
# word[0:3] → length = 3 - 0 = 3   ✅ simple math!
# word[2:7] → length = 7 - 2 = 5   ✅ simple math!
# If stop were included: word[0:3] would have 4 characters → confusing

# ── Reason 2: Slices join together cleanly ──
word = "Python"
first_half  = word[0:3]     # Pyt
second_half = word[3:6]     # hon
print(first_half + second_half)     # Python  ← perfect join!
# If stop were included, they would overlap!

# ── Reason 3: [0:n] always gives first n characters ──
print(word[0:1])    # P      ← first 1 character
print(word[0:2])    # Py     ← first 2 characters
print(word[0:3])    # Pyt    ← first 3 characters
print(word[0:4])    # Pyth   ← first 4 characters
# Clean, predictable, intuitive once you know the rule!

# Memory trick:
# Think of the indexes as pointing BETWEEN characters:
#
#  | P | y | t | h | o | n |
#  0   1   2   3   4   5   6
#  ↑               ↑
# start=0       stop=3
# → gives: P y t  (everything between pointer 0 and pointer 3)


# ------------------------------------------------------------
# PART 4: Visualizing slicing with the "between" model
# ------------------------------------------------------------

# The best mental model for slicing:
# Imagine the indexes as WALLS between characters.
#
#  ┌───┬───┬───┬───┬───┬───┐
#  │ P │ y │ t │ h │ o │ n │
#  └───┴───┴───┴───┴───┴───┘
#  ↑   ↑   ↑   ↑   ↑   ↑   ↑
#  0   1   2   3   4   5   6
#
# word[1:4] means: take everything between wall 1 and wall 4
#   → y, t, h   → "yth"
#
# word[0:6] means: take everything between wall 0 and wall 6
#   → P, y, t, h, o, n   → "Python"
#
# Notice: wall 6 exists even though character index 6 doesn't!
# That's why word[0:6] works even though word[6] would be IndexError.

word = "Python"
print(word[1:4])    # yth
print(word[0:6])    # Python


# ------------------------------------------------------------
# PART 5: Omitting start or stop
# ------------------------------------------------------------

# Python allows you to OMIT either start or stop (or both).
# When omitted, Python uses default values.

word = "Python"

# ── Omitting start → defaults to 0 (beginning of string) ──
print(word[:3])     # Pyt   ← same as word[0:3]
print(word[:4])     # Pyth  ← same as word[0:4]
print(word[:1])     # P     ← same as word[0:1]

# ── Omitting stop → defaults to end of string ──
print(word[2:])     # thon  ← from index 2 to the end
print(word[4:])     # on    ← from index 4 to the end
print(word[1:])     # ython ← from index 1 to the end

# ── Omitting both → entire string ──
print(word[:])      # Python ← complete copy of the string

# This is very useful in practice:
# word[:n]  = first n characters
# word[n:]  = everything from position n onwards
# word[:]   = full copy of the string

# Real examples:
filename = "report_2024.pdf"
print(filename[:6])     # report  ← first 6 characters (name without _)
print(filename[7:])     # 2024.pdf ← everything after the underscore
print(filename[-3:])    # pdf     ← last 3 characters (extension)


# ------------------------------------------------------------
# PART 6: Slicing with negative indexes
# ------------------------------------------------------------

# You can use negative indexes in slices!
# Remember: negative indexes count from the RIGHT.

word = "Python"
#  P  y  t  h  o  n
# -6 -5 -4 -3 -2 -1

# Get the last 3 characters:
print(word[-3:])    # hon  ← from -3 to the end

# Get everything except the last character:
print(word[:-1])    # Pytho ← from start to (but not including) -1

# Get everything except first and last:
print(word[1:-1])   # ytho  ← from 1 to (but not including) -1

# Get the last 2 characters:
print(word[-2:])    # on

# Get characters from -4 to -1:
print(word[-4:-1])  # tho  ← from -4 to (not including) -1

# Mix positive and negative:
print(word[1:-2])   # yth  ← from index 1 to (not including) -2

# The most common negative slices:
sentence = "Hello, World!"
print(sentence[-6:])    # orld!   ← last 6 characters
print(sentence[:-1])    # Hello, World  ← remove last character
print(sentence[-6:-1])  # orld   ← 5 characters from the end, not last


# ------------------------------------------------------------
# PART 7: Slicing does NOT raise IndexError
# ------------------------------------------------------------

# This is a big difference between indexing and slicing!
# Indexing with an out-of-range index → IndexError
# Slicing with out-of-range indexes → NO error, Python adjusts!

word = "Python"    # length = 6, valid indexes: 0-5

# Indexing out of range → ERROR:
# print(word[10])   # ❌ IndexError

# Slicing out of range → NO ERROR:
print(word[0:100])  # Python  ← Python just takes what exists
print(word[3:100])  # hon     ← from 3 to end (no error)
print(word[-100:3]) # Pyt     ← Python starts from beginning
print(word[10:20])  # ""      ← empty string (nothing to take)

# Why? Slicing is more "forgiving" than indexing.
# Python simply clamps the values to valid range.
# This is very useful when working with unknown-length strings!

# Compare:
text = "Hi"
# print(text[5])    # ❌ IndexError - crashes!
print(text[0:5])    # Hi  ← no error, just returns what exists


# ------------------------------------------------------------
# PART 8: Slicing creates a NEW string
# ------------------------------------------------------------

# When you slice a string, you get a BRAND NEW string.
# The original string is not modified (strings are immutable!).

original = "Python"
sliced = original[0:3]

print(original)     # Python  ← unchanged!
print(sliced)       # Pyt     ← new string

# They are separate objects in memory:
print(id(original)) # some memory address
print(id(sliced))   # different memory address!
print(original is sliced)   # False ← different objects

# Even slicing the whole string creates a new object:
copy = original[:]
print(copy)                 # Python
print(original == copy)     # True  ← same content
print(original is copy)     # False ← but different objects!

# This is safe:
# You can slice freely without worrying about
# accidentally modifying the original string.


# ------------------------------------------------------------
# PART 9: Slicing in practice - real world examples
# ------------------------------------------------------------

# ── Example 1: Extract parts of a date string ──
date = "2024-03-15"
year  = date[0:4]
month = date[5:7]
day   = date[8:10]
print(year)     # 2024
print(month)    # 03
print(day)      # 15

# ── Example 2: Get file name without extension ──
filename = "genome_data.fasta"
# Extension is last 6 characters: .fasta
name_only = filename[:-6]
print(name_only)    # genome_data

# Or split at the dot:
dot_position = 11   # we'll learn .find() to get this automatically
name_only = filename[:dot_position]
print(name_only)    # genome_data

# ── Example 3: Remove prefix from a string ──
full_title = "Dr. Smith"
name_only = full_title[4:]  # skip "Dr. "
print(name_only)    # Smith

# ── Example 4: Get domain from email ──
email = "anna@university.edu"
# @ is at index 4
domain = email[5:]
print(domain)       # university.edu

# ── Example 5: Check first word ──
sentence = "Python is amazing"
first_word = sentence[:6]
print(first_word)   # Python

# ── Example 6: Get area code from phone ──
phone = "+48502111222"
area_code = phone[1:3]
print(area_code)    # 48

# ── Example 7: Extract codon from DNA ──
dna = "ATGCCCGCATTAGTCGA"
first_codon  = dna[0:3]    # ATG
second_codon = dna[3:6]    # CCC
third_codon  = dna[6:9]    # GCA
print(first_codon)          # ATG
print(second_codon)         # CCC
print(third_codon)          # GCA


# ------------------------------------------------------------
# PART 10: Empty slices
# ------------------------------------------------------------

# A slice can result in an empty string "".
# This happens when start >= stop.

word = "Python"

print(word[3:3])    # ""  ← start equals stop → nothing between them
print(word[4:2])    # ""  ← start is after stop → nothing (no error!)
print(word[5:1])    # ""  ← same reason

# This is not an error! It's a valid, empty string.
result = word[3:3]
print(type(result))     # <class 'str'>
print(len(result))      # 0
print(result == "")     # True

# When does this happen in real code?
# When your calculated indexes accidentally cross each other.
# Knowing this prevents confusion when you get unexpected empty strings.


# ------------------------------------------------------------
# PART 11: Slicing to "modify" strings
# ------------------------------------------------------------

# Remember: strings are immutable.
# You CANNOT change a character directly.
# But you CAN use slicing to build a MODIFIED COPY.

# ── Remove first character ──
word = "Python"
without_first = word[1:]
print(without_first)    # ython

# ── Remove last character ──
without_last = word[:-1]
print(without_last)     # Pytho

# ── Remove first AND last character ──
without_both = word[1:-1]
print(without_both)     # ytho

# ── Replace first character (using slicing + concatenation) ──
new_word = "J" + word[1:]
print(new_word)         # Jython

# ── Insert a character in the middle ──
word = "Hllo"
fixed = word[0] + "e" + word[1:]
print(fixed)            # Hello

# ── Remove a character from the middle ──
word = "Hellllo"
fixed = word[:4] + word[5:]
print(fixed)            # Hello

# This pattern (slicing + concatenation) is how you
# "modify" strings in Python even though they're immutable.


# ------------------------------------------------------------
# PART 12: Slicing and the relationship to indexing
# ------------------------------------------------------------

# Slicing and indexing are closely related.
# In fact, single-character indexing is a special case of slicing:
#   word[i]   → one character (type: str, length 1)
#   word[i:i+1] → same character (type: str, length 1)

word = "Python"

print(word[2])      # t
print(word[2:3])    # t   ← same result!

print(word[2] == word[2:3])     # True  ← same content
print(word[2] is word[2:3])     # might be True or False (implementation detail)

# Key difference:
# word[i]   → if i is out of range → IndexError
# word[i:i+1] → if i is out of range → empty string ""

print(word[10:11])  # ""  ← no error!
# print(word[10])   # ❌ IndexError


# ------------------------------------------------------------
# PART 13: Combining multiple slices
# ------------------------------------------------------------

# You can combine slices using concatenation
# to build new strings from parts of an original string.

name = "Anna Kowalska"
#       0123456789...

first = name[:4]        # Anna
last  = name[5:]        # Kowalska

print(first)            # Anna
print(last)             # Kowalska
print(last + ", " + first)  # Kowalska, Anna  ← surname-first format!

# ── Building an acronym ──
phrase = "Artificial Intelligence"
acronym = phrase[0] + phrase[12]
print(acronym)          # AI

# ── Rearranging date format ──
date = "2024-03-15"     # YYYY-MM-DD
year  = date[:4]        # 2024
month = date[5:7]       # 03
day   = date[8:]        # 15
eu_format = day + "." + month + "." + year
print(eu_format)        # 15.03.2024


# ------------------------------------------------------------
# PART 14: Common slicing patterns - a cheat sheet
# ------------------------------------------------------------

word = "Programming"

# First n characters:
print(word[:3])         # Pro   ← first 3

# Last n characters:
print(word[-3:])        # ing   ← last 3

# Skip first n characters:
print(word[3:])         # gramming  ← skip first 3

# Skip last n characters:
print(word[:-3])        # Programm  ← skip last 3

# Middle section (skip first 2, take next 4):
print(word[2:6])        # ogra

# Everything:
print(word[:])          # Programming  ← full copy

# Everything except first and last:
print(word[1:-1])       # rogrammin

# The second half:
half = len(word) // 2   # integer division - we cover this later
print(word[half:])      # ming  (roughly)


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Slicing extracts a SUBSTRING from a string
# ✅ Syntax: string[start:stop]
# ✅ start is INCLUDED, stop is EXCLUDED
# ✅ Omit start → defaults to 0 (beginning)
# ✅ Omit stop  → defaults to end of string
# ✅ Omit both  → full copy of string: string[:]
# ✅ Negative indexes work in slices too
# ✅ Out-of-range slice indexes do NOT raise IndexError
# ✅ start >= stop → empty string ""
# ✅ Slicing creates a NEW string (original unchanged)
# ✅ Use slicing + concatenation to "modify" strings
# ✅ word[:n]  = first n characters
# ✅ word[-n:] = last n characters
# ✅ word[n:]  = skip first n characters
# ✅ word[:-n] = skip last n characters