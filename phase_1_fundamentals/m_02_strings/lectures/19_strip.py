# ============================================================
# MODULE 02 | LECTURE 19 - .strip(), .lstrip(), .rstrip()
# ============================================================
# What you will learn:
#   - What whitespace is and why it causes problems
#   - What .strip() does and how to use it
#   - What .lstrip() and .rstrip() do
#   - Stripping specific characters (not just whitespace)
#   - Why .strip() is essential for user input
#   - Combining .strip() with other methods
#   - Real world use cases
#   - Common mistakes and misconceptions
# ============================================================


# ------------------------------------------------------------
# PART 1: What is whitespace?
# ------------------------------------------------------------

# Before we talk about .strip(), we need to understand
# what WHITESPACE is.

# Whitespace = any character that represents "empty space"
# but is still a real character with a real ASCII code.

# The main whitespace characters:
#   " "  → regular space       (most common)
#   "\t" → tab character       (horizontal jump)
#   "\n" → newline character   (line break)
#   "\r" → carriage return     (old Windows line ending)

# We can SEE the effects of whitespace even if we can't see
# the characters themselves:

print("Hello")          # Hello
print("   Hello")       # (3 spaces)Hello
print("Hello   ")       # Hello(3 spaces)  ← hard to see!
print("Hello\tWorld")   # Hello	World    ← tab between words
print("Hello\nWorld")   # Hello
                        # World            ← newline!

# Whitespace is INVISIBLE but it's still there.
# This causes many subtle bugs in real programs!

# Example of the bug:
name1 = "Anna"
name2 = "Anna "     # extra space at the end - invisible!

print(name1 == name2)   # False  ← different strings!
print(len(name1))       # 4
print(len(name2))       # 5  ← the space is counted!

# This is exactly the problem .strip() solves.


# ------------------------------------------------------------
# PART 2: What is .strip()?
# ------------------------------------------------------------

# .strip() removes ALL leading and trailing whitespace
# from a string.
#
# Leading  = whitespace at the START (left side)
# Trailing = whitespace at the END   (right side)
#
# Whitespace in the MIDDLE of the string is NOT touched.

# Basic usage:
word = "   Hello   "
print(word)             #    Hello    (with spaces)
print(word.strip())     # Hello       (spaces removed)

# Visual representation:
# Before: "   Hello   "
#          ^^^       ^^^  ← these are removed
#             ^^^^^       ← this is kept
# After:  "Hello"

# Works with tabs and newlines too:
messy = "\t\tHello World\n\n"
print(messy.strip())    # Hello World  ← tabs and newlines removed

# Multiple types of whitespace mixed:
messy2 = "  \t  Hello  \n  "
print(messy2.strip())   # Hello


# ------------------------------------------------------------
# PART 3: .strip() does NOT touch the middle
# ------------------------------------------------------------

# This is crucial to understand.
# .strip() ONLY removes from the edges.
# Whitespace inside the string is ALWAYS preserved.

text = "   Hello   World   "
print(text.strip())     # Hello   World
#                         ↑↑↑           ← leading spaces removed
#                                    ↑↑↑ ← trailing spaces removed
#                              ↑↑↑       ← middle spaces KEPT!

# Another example:
sentence = "  Python   is   great  "
print(sentence.strip())     # Python   is   great
# Leading "  " removed, trailing "  " removed
# But the spaces between words stay exactly as they are!

# Empty string stays empty:
print("".strip())           # ""  ← nothing to remove

# String with only spaces → becomes empty string:
spaces = "     "
print(spaces.strip())       # ""  ← all whitespace, all removed
print(len(spaces.strip()))  # 0


# ------------------------------------------------------------
# PART 4: .lstrip() - strip from the LEFT only
# ------------------------------------------------------------

# .lstrip() removes whitespace ONLY from the LEFT (leading).
# Right side (trailing) whitespace is left untouched.
#
# "l" in lstrip = LEFT

text = "   Hello   "
print(text.lstrip())    # "Hello   "
#                          ↑↑↑  removed from left
#                               ↑↑↑  still there on right

# More examples:
print("   Python   ".lstrip())      # "Python   "
print("\t\nHello\t\n".lstrip())     # "Hello\t\n"  ← right side intact
print("Hello   ".lstrip())          # "Hello   "   ← nothing on left to remove

# Visual:
# "   Hello   "
#  ^^^         ← removed by lstrip
#       ^^^^^  ← kept
#            ^^^ ← also kept (right side)


# ------------------------------------------------------------
# PART 5: .rstrip() - strip from the RIGHT only
# ------------------------------------------------------------

# .rstrip() removes whitespace ONLY from the RIGHT (trailing).
# Left side (leading) whitespace is left untouched.
#
# "r" in rstrip = RIGHT

text = "   Hello   "
print(text.rstrip())    # "   Hello"
#                          ↑↑↑  still there on left
#                               ↑↑↑  removed from right

# More examples:
print("   Python   ".rstrip())      # "   Python"
print("\t\nHello\t\n".rstrip())     # "\t\nHello"  ← left side intact
print("   Hello".rstrip())          # "   Hello"   ← nothing on right to remove

# Visual:
# "   Hello   "
#  ^^^         ← kept (left side)
#     ^^^^^    ← kept (middle)
#          ^^^ ← removed by rstrip


# ------------------------------------------------------------
# PART 6: Comparing all three methods
# ------------------------------------------------------------

text = "   Hello World   "
#       ^^^             ^^^  ← whitespace on both sides

print(f"Original : '{text}'")           # '   Hello World   '
print(f".strip()  : '{text.strip()}'")  # 'Hello World'
print(f".lstrip() : '{text.lstrip()}'") # 'Hello World   '
print(f".rstrip() : '{text.rstrip()}'") # '   Hello World'

# Summary table:
# ┌──────────────┬──────────────────────────────────────────┐
# │ Method       │ What it removes                          │
# ├──────────────┼──────────────────────────────────────────┤
# │ .strip()     │ Whitespace from BOTH sides               │
# │ .lstrip()    │ Whitespace from LEFT side only           │
# │ .rstrip()    │ Whitespace from RIGHT side only          │
# └──────────────┴──────────────────────────────────────────┘

# In practice: .strip() is used 90% of the time.
# .lstrip() and .rstrip() are used when you need
# to preserve whitespace on one specific side.


# ------------------------------------------------------------
# PART 7: Stripping SPECIFIC characters
# ------------------------------------------------------------

# By default, .strip() removes whitespace.
# But you can pass a STRING ARGUMENT to specify
# which characters to remove!

# Syntax:
#   string.strip(characters)
#   string.lstrip(characters)
#   string.rstrip(characters)

# The argument is a string of characters to remove.
# Python removes ANY combination of those characters
# from the edges.

# ── Remove specific characters ──
word = "###Hello###"
print(word.strip("#"))      # Hello  ← removes all # from both sides

word = "...Python..."
print(word.strip("."))      # Python

word = "***important***"
print(word.strip("*"))      # important

# ── Remove multiple specific characters ──
# Pass a STRING containing all characters you want removed:
word = "##**Hello**##"
print(word.strip("#*"))     # Hello  ← removes both # and *

word = "xXxHello WorldxXx"
print(word.strip("xX"))     # Hello World  ← removes x and X

# ── Order doesn't matter in the argument string ──
word = "###Hello###"
print(word.strip("#"))      # Hello
print(word.strip("##"))     # Hello  ← same result!
print(word.strip("###"))    # Hello  ← same result!
# Python removes characters, not the exact string pattern!

# ── Important: it removes character by character from edges ──
word = "abcHelloabc"
print(word.strip("abc"))    # Hello
# Removes: a, then b, then c, then a again... until it hits 'H'
# 'H' is not in "abc" so it stops!

word = "abcaHelloacba"
print(word.strip("abc"))    # Hello
# a,b,c,a removed from left → "Helloacba"
# then a,b,c,a removed from right → "Hello"

# ── It only removes from the EDGES ──
word = "aHelloa"
print(word.strip("a"))      # Hello  ← 'a' at edges removed
word = "aHeaalloa"
print(word.strip("a"))      # Heaallo  ← middle 'a's NOT removed!


# ------------------------------------------------------------
# PART 8: Stripping specific characters with lstrip/rstrip
# ------------------------------------------------------------

# The same logic applies to .lstrip() and .rstrip():

word = "###Hello###"
print(word.lstrip("#"))     # Hello###   ← only left # removed
print(word.rstrip("#"))     # ###Hello   ← only right # removed

# ── Real use case: remove leading zeros from a number string ──
number = "000042"
print(number.lstrip("0"))   # 42   ← leading zeros removed!
print(number.rstrip("0"))   # 000042  ← trailing zeros (none here)

number = "420000"
print(number.rstrip("0"))   # 42   ← trailing zeros removed!

# ── Remove quotes from a string ──
quoted = '"Hello World"'
print(quoted.strip('"'))    # Hello World  ← quotes removed

quoted2 = "'Python'"
print(quoted2.strip("'"))   # Python


# ------------------------------------------------------------
# PART 9: .strip() and immutability
# ------------------------------------------------------------

# Just like all string methods, .strip() does NOT
# modify the original string. It returns a NEW string.

original = "   Hello   "
stripped = original.strip()

print(original)     # "   Hello   "  ← unchanged!
print(stripped)     # "Hello"        ← new string

# Common mistake:
text = "   Hello   "
text.strip()            # ← result is THROWN AWAY!
print(text)             # "   Hello   "  ← not changed!

# ✅ Fix: store the result
text = "   Hello   "
text = text.strip()     # ← reassign!
print(text)             # "Hello"


# ------------------------------------------------------------
# PART 10: The most important use case - user input
# ------------------------------------------------------------

# When users type input, they OFTEN accidentally add spaces.
# This is extremely common and causes many bugs.
# .strip() on user input is considered BEST PRACTICE.

# Example of the problem:
stored_password = "secret123"
entered = "secret123 "    # user accidentally pressed space!
print(entered == stored_password)   # False  ← bug!

# ✅ Fix with .strip():
print(entered.strip() == stored_password)   # True  ← correct!

# ── Always strip user input ──
name = input("Enter your name: ")
name = name.strip()     # remove accidental leading/trailing spaces
print(f"Hello, {name}!")

# ── Combine with .lower() for robust comparison ──
answer = input("Do you want to continue? ").strip().lower()
if answer == "yes":
    print("Continuing!")

# ── Full input normalization pipeline ──
raw = input("Enter city name: ")
city = raw.strip().lower().title()
# strip()  → remove accidental spaces
# lower()  → normalize case
# title()  → proper capitalization
print(f"City: {city}")

# If user types: "  wARSAW  "
# After strip():  "wARSAW"
# After lower():  "warsaw"
# After title():  "Warsaw"  ← perfect!


# ------------------------------------------------------------
# PART 11: .strip() with newlines - reading files
# ------------------------------------------------------------

# When reading text files (Module 08), each line
# comes with a "\n" newline character at the end.
# .strip() or .rstrip() is used to clean them up.
# This is a preview of a very common pattern:

# Imagine reading a line from a file:
line_from_file = "Anna Kowalska\n"
clean_line = line_from_file.strip()
print(clean_line)       # Anna Kowalska  ← newline removed
print(len(line_from_file))  # 14  ← includes the \n
print(len(clean_line))      # 13  ← without \n

# Or more specifically, just remove the trailing newline:
line_from_file = "Anna Kowalska\n"
clean_line = line_from_file.rstrip("\n")
print(clean_line)       # Anna Kowalska  ← only \n removed from right

# This is one of the MOST COMMON uses of .rstrip() in Python!


# ------------------------------------------------------------
# PART 12: Combining .strip() with other methods
# ------------------------------------------------------------

# .strip() is almost always used as the FIRST step
# in a chain of string processing methods.
# You clean up the string first, then process it.

# ── Standard input cleaning pipeline ──
raw = "  HELLO WORLD  "
result = raw.strip().lower().title()
print(result)           # Hello World

# ── Checking content after stripping ──
user_input = "   "
if len(user_input.strip()) == 0:
    print("Please enter something!")
# Output: Please enter something!
# Without .strip(): len("   ") = 3, not 0! The check would fail.

# ── Strip then compare ──
command = "  quit  "
if command.strip().lower() == "quit":
    print("Quitting...")
# Works regardless of spaces or capitalization!

# ── Strip then check length ──
username = "  ab  "
clean_username = username.strip()
if len(clean_username) < 3:
    print(f"Username '{clean_username}' is too short!")
# Output: Username 'ab' is too short!
# Without strip: len("  ab  ") = 6 → would pass the check incorrectly!

# ── Strip specific chars then process ──
data = "###42.5###"
value = float(data.strip("#"))  # removes # then converts to float
print(value)            # 42.5
print(type(value))      # <class 'float'>


# ------------------------------------------------------------
# PART 13: Edge cases and interesting behaviors
# ------------------------------------------------------------

# ── Stripping a character that's not there ──
word = "Hello"
print(word.strip("x"))      # Hello  ← nothing to remove, no error

# ── Stripping everything ──
word = "aaa"
print(word.strip("a"))      # ""  ← all characters removed!
print(word.strip("abc"))    # ""  ← 'a' is in "abc" so it's removed

# ── Strip is greedy - removes ALL matching chars from edge ──
word = "#####Hello#####"
print(word.strip("#"))      # Hello  ← removes ALL # from both sides
# NOT just one # from each side!

# ── Numbers in the strip argument ──
code = "123Hello123"
print(code.strip("123"))    # Hello  ← digits as strip chars!
print(code.lstrip("123"))   # Hello123
print(code.rstrip("123"))   # 123Hello

# ── Whitespace within the strip argument ──
text = "   Hello   "
print(text.strip(" "))      # Hello  ← same as default .strip()

# ── Multiple whitespace types ──
messy = "\t\n  Hello  \n\t"
print(messy.strip())        # Hello  ← all whitespace types removed

# ── Stripping from only one end preserves the other ──
text = "\n\nHello\n\n"
print(repr(text.lstrip("\n")))  # 'Hello\n\n'  ← left newlines gone
print(repr(text.rstrip("\n")))  # '\n\nHello'  ← right newlines gone

# repr() shows the string with escape characters visible
# useful for debugging whitespace issues!
print(repr("  Hello  "))    # '  Hello  '  ← spaces visible


# ------------------------------------------------------------
# PART 14: repr() - a debugging tool for whitespace
# ------------------------------------------------------------

# When debugging whitespace issues, repr() is your best friend.
# repr() shows the string in a "raw" form with
# escape characters visible (\n, \t, spaces clearly bounded).

text1 = "Hello"
text2 = "Hello   "
text3 = "Hello\n"
text4 = "\tHello\t"

print(repr(text1))      # 'Hello'
print(repr(text2))      # 'Hello   '   ← trailing spaces visible!
print(repr(text3))      # 'Hello\n'    ← newline visible!
print(repr(text4))      # '\tHello\t'  ← tabs visible!

# Compare before and after strip:
messy = "\t  Hello World  \n"
print(repr(messy))              # '\t  Hello World  \n'
print(repr(messy.strip()))      # 'Hello World'

# This is extremely useful when debugging:
# "Why doesn't my comparison work?"
# Answer: repr() might reveal hidden whitespace!

value = "42 "
print(value == "42")            # False  ← why??
print(repr(value))              # '42 '  ← there's a trailing space!
print(value.strip() == "42")    # True   ← fixed!


# ------------------------------------------------------------
# PART 15: Real world applications
# ------------------------------------------------------------

# ── Application 1: Clean CSV data ──
# CSV files often have extra spaces around values
raw_data = "  Anna  ,  25  ,  Warsaw  "
# Split by comma (preview of .split() - next lecture!)
# For now, just strip the whole thing to show the concept
print(raw_data.strip())     # Anna  ,  25  ,  Warsaw

# ── Application 2: Remove file path artifacts ──
filepath = "  /home/user/documents/file.txt  \n"
clean_path = filepath.strip()
print(clean_path)       # /home/user/documents/file.txt

# ── Application 3: Process configuration values ──
config_value = "   True   "
is_enabled = config_value.strip().lower() == "true"
print(is_enabled)       # True  (Python boolean)

# ── Application 4: Remove decorative borders from text ──
decorated = "=== Python Tutorial ==="
clean = decorated.strip("= ")
print(clean)            # Python Tutorial

decorated2 = "--- Chapter 1 ---"
clean2 = decorated2.strip("- ")
print(clean2)           # Chapter 1

# ── Application 5: Validate non-empty input ──
user_input = "   "       # user just pressed space
if not user_input.strip():  # strip → empty string → falsy
    print("Error: Please enter a non-empty value!")
# Output: Error: Please enter a non-empty value!

# ── Application 6: Clean up multiline text ──
lines = ["  First line  \n", "\tSecond line\t\n", "  Third line  "]
# Without loops (preview - using manual access):
print(lines[0].strip())     # First line
print(lines[1].strip())     # Second line
print(lines[2].strip())     # Third line

# ── Application 7: Parse key-value pairs ──
raw_pair = "  name  :  Anna Kowalska  "
# Split at colon (preview):
colon_pos = raw_pair.index(":")     # find the colon
key   = raw_pair[:colon_pos].strip()    # "  name  " → "name"
value = raw_pair[colon_pos+1:].strip()  # "  Anna Kowalska  " → "Anna Kowalska"
print(f"Key:   '{key}'")    # Key:   'name'
print(f"Value: '{value}'")  # Value: 'Anna Kowalska'


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Whitespace = spaces, tabs (\t), newlines (\n) - invisible but real!
# ✅ .strip()  → removes whitespace from BOTH sides
# ✅ .lstrip() → removes whitespace from LEFT side only
# ✅ .rstrip() → removes whitespace from RIGHT side only
# ✅ Middle whitespace is NEVER touched by any strip method
# ✅ .strip("chars") → removes specific characters from both sides
# ✅ Strip argument = a SET of characters, not a pattern!
# ✅ Strip is GREEDY - removes all matching chars from the edge
# ✅ Returns a NEW string, original is unchanged (immutable!)
# ✅ Always strip() user input - accidental spaces are very common
# ✅ .rstrip("\n") → essential when reading files line by line
# ✅ Use repr() to debug invisible whitespace issues
# ✅ Chain: input.strip().lower() → standard input normalization
# ✅ Empty string after strip → user entered only whitespace