# ============================================================
# MODULE 02 | LECTURE 27 - Special Characters
# ============================================================
# What you will learn:
#   - What special characters (escape sequences) are
#   - Why they exist and why they are necessary
#   - The most important escape sequences: \n \t \\ \' \"
#   - Less common but useful: \r \b \f \a \v
#   - Unicode escape sequences: \u \U \N \x
#   - How special characters affect len() and indexing
#   - How to SEE special characters using repr()
#   - Special characters in print() vs in the string itself
#   - Common mistakes and how to avoid them
# ============================================================


# ------------------------------------------------------------
# PART 1: What are special characters?
# ------------------------------------------------------------

# Some characters cannot be typed directly into a string.
# For example:
#   - A NEWLINE (pressing Enter) would just break the code line
#   - A TAB might not render consistently
#   - A BACKSLASH has special meaning in Python strings
#   - A QUOTE would end the string prematurely

# Python solves this with ESCAPE SEQUENCES.
# An escape sequence starts with a BACKSLASH (\)
# followed by one or more characters.
# Together, the backslash + character(s) represent
# a SINGLE special character in the string.

# Example:
text = "Hello\nWorld"   # \n = newline
print(text)
# Hello
# World
# ↑ The \n caused a line break!

# The string "Hello\nWorld" has 11 characters, not 12:
print(len("Hello\nWorld"))  # 11  ← \n is ONE character
print(len("Hello"))         # 5
print(len("\n"))             # 1   ← \n = single character!


# ------------------------------------------------------------
# PART 2: The backslash - the escape character
# ------------------------------------------------------------

# The backslash \ is called the ESCAPE CHARACTER.
# When Python sees \ inside a string, it "escapes" from
# the normal meaning of the next character.
#
# Backslash + something = special character (escape sequence)
#
# Think of it like a modifier key (like Ctrl or Alt):
# On its own, Ctrl does nothing.
# Ctrl+C = copy (different meaning!)
# Similarly:
# \  alone would be a syntax error at end of line
# \n = completely different thing: newline character

# The backslash itself:
print("\\")     # \   ← one backslash in output
print("\\\\")   # \\  ← two backslashes in output

# A backslash at the END of a line = line continuation (different!):
long_string = "This is a very " \
              "long string"
print(long_string)  # This is a very long string


# ------------------------------------------------------------
# PART 3: \n - Newline
# ------------------------------------------------------------

# \n = newline character (ASCII 10)
# Moves to the NEXT LINE when printed.
# Most commonly used escape sequence in Python!

# ── Basic usage ──
print("First line\nSecond line\nThird line")
# First line
# Second line
# Third line

# ── In a variable ──
poem = "Roses are red\nViolets are blue\nPython is great\nAnd so are you"
print(poem)
# Roses are red
# Violets are blue
# Python is great
# And so are you

# ── Multiple \n in a row ~~
print("Before\n\nAfter")    # blank line between!
# Before
#
# After

print("A\n\n\nB")           # two blank lines!
# A
#
#
# B

# ── \n is ONE character ~~
text = "Hello\nWorld"
print(len(text))    # 11  ← 5 + 1 + 5 = 11 (not 12!)
print(text[5])      # ← prints a newline (invisible!)
print(repr(text[5])) # '\n'  ← repr() shows it clearly

# ── \n in different contexts ~~
# In a string it's a character.
# In print() it causes actual line break.
# In a file it represents the end of a line.

# ── The end parameter of print() ~~
# By default, print() adds \n at the end automatically!
print("Hello")  # Python actually does: print("Hello" + "\n")
# That's why each print() starts on a new line.
# You can change this with end parameter:
print("Hello", end="")     # no newline at end
print(" World")            # continues on same line
# Output: Hello World

print("A", end=" | ")
print("B", end=" | ")
print("C")
# Output: A | B | C


# ------------------------------------------------------------
# PART 4: \t - Tab
# ------------------------------------------------------------

# \t = horizontal tab character (ASCII 9)
# Moves to the next "tab stop" (usually every 8 characters).
# Used for indentation and alignment in plain text.

# ── Basic usage ~~
print("Name\tAge\tCity")
print("Anna\t25\tWarsaw")
print("Jan\t32\tKrakow")
# Name	Age	City
# Anna	25	Warsaw
# Jan	32	Krakow

# ── Tab vs spaces ~~
# Tab is ONE character but takes variable visual space.
# This makes it tricky for precise alignment (prefer .format()!).
print("A\tB")       # A    B  (tab stop at 8)
print("AB\tB")      # AB   B  (tab stop at 8)
print("ABCDEFG\tB") # ABCDEFG B (tab stop at 8)
print("ABCDEFGH\tB")# ABCDEFGH    B (tab stop at 16!)

# ── \t is ONE character ~~
print(len("\t"))    # 1
print(repr("\t"))   # '\t'

# ── \t in data processing ~~
# TSV files (Tab-Separated Values) use \t as delimiter
tsv_line = "Anna\tKowalska\t25\tWarsaw"
fields = tsv_line.split("\t")
print(fields)   # ['Anna', 'Kowalska', '25', 'Warsaw']


# ------------------------------------------------------------
# PART 5: \\ - Literal backslash
# ------------------------------------------------------------

# Since \ is the escape character, to get a REAL backslash
# in your string, you need to ESCAPE the backslash: \\
# Two backslashes in code → one backslash in the string.

# ── File paths (Windows uses backslashes!) ~~
# ❌ Wrong:
# path = "C:\Users\Anna\Documents"  # \U and \A look like escape sequences!
# This might work by accident or cause weird characters

# ✅ Correct - escape each backslash:
path = "C:\\Users\\Anna\\Documents"
print(path)     # C:\Users\Anna\Documents  ← correct!

# ✅ Alternative - raw string (covered in next lecture!):
path = r"C:\Users\Anna\Documents"
print(path)     # C:\Users\Anna\Documents  ← also correct

# ── Counting backslashes ~~
print(len("\\"))    # 1  ← two chars in code, ONE in string!
print(len("\\\\"))  # 2  ← four chars in code, TWO in string!

# ── Backslash in regex (preview) ~~
# Regular expressions use \d, \w, \s etc.
# In a normal string: "\\d" = literal \d
# In a raw string: r"\d" = literal \d (easier to read)

# ── Displaying backslash ~~
print("\\")         # \
print("\\\\")       # \\
print("a\\b")       # a\b
print("C:\\Python") # C:\Python


# ------------------------------------------------------------
# PART 6: \' and \" - Quote characters
# ------------------------------------------------------------

# Normally, a quote character ENDS the string.
# \' lets you use a single quote inside a single-quoted string.
# \" lets you use a double quote inside a double-quoted string.

# ── Single quote in single-quoted string ~~
# ❌ This would cause a SyntaxError:
# text = 'It's a great day'   # ' after It ends the string!

# ✅ Fix 1: escape the quote
text = 'It\'s a great day'
print(text)     # It's a great day

# ✅ Fix 2: use double quotes for the string
text = "It's a great day"
print(text)     # It's a great day  ← easier!

# ── Double quote in double-quoted string ~~
# ❌ This would cause a SyntaxError:
# text = "She said "hello" to me"

# ✅ Fix 1: escape the quote
text = "She said \"hello\" to me"
print(text)     # She said "hello" to me

# ✅ Fix 2: use single quotes for the string
text = 'She said "hello" to me'
print(text)     # She said "hello" to me  ← easier!

# ── Both quote types in one string ~~
# When you need BOTH types, you must escape one of them:
text = "It's called \"Python\""
print(text)     # It's called "Python"

text = 'It\'s called "Python"'
print(text)     # It's called "Python"

# Or use triple quotes (covered separately):
text = """It's called "Python" """
print(text)     # It's called "Python"


# ------------------------------------------------------------
# PART 7: \r - Carriage Return
# ------------------------------------------------------------

# \r = carriage return (ASCII 13)
# Moves the cursor to the BEGINNING of the current line
# WITHOUT moving to the next line.
# Historical origin: typewriter carriage return.

# ── Windows line ending: \r\n ~~
# Windows uses \r\n (carriage return + newline) as line ending.
# Unix/Linux/Mac uses just \n.
# Python handles this for you when reading files (usually).

windows_line = "Hello\r\nWorld"
print(windows_line)
# Hello
# World  ← same result as \n on most systems

# ── \r in terminal output - overwrite effect ~~
# In a terminal, \r moves cursor to start of line.
# Next output overwrites the current line!
# This is used for progress bars!

import time
import sys

print("Loading: [          ]", end="\r")    # print then go to start
time.sleep(0.5)
print("Loading: [###       ]", end="\r")    # overwrite same line!
time.sleep(0.5)
print("Loading: [######    ]", end="\r")
time.sleep(0.5)
print("Loading: [##########]")              # final state with newline

# ── \r vs \n ~~
# \n = go to next line (most common)
# \r = go to START of current line (used for overwriting)
# \r\n = Windows line ending (go to start, then next line)


# ------------------------------------------------------------
# PART 8: \b - Backspace
# ------------------------------------------------------------

# \b = backspace character (ASCII 8)
# Moves the cursor ONE position to the LEFT.
# In a terminal, this can effectively delete the previous character.

# ── Basic behavior ~~
print("Hello\b")            # "Hell" in some terminals (o deleted)
print("ABC\b\b\bXYZ")       # might show "XYZ" (overwrote ABC)

# Note: behavior depends on the terminal/console!
# In Python IDLE or some editors, \b might just print as-is.
# In actual terminal it works as expected.

# \b is rarely used in modern Python code.
# It's mainly useful for terminal-based animations.

print(len("\b"))    # 1  ← still ONE character
print(repr("\b"))   # '\b'


# ------------------------------------------------------------
# PART 9: \f - Form Feed
# ------------------------------------------------------------

# \f = form feed (ASCII 12)
# Historically used to advance to the next PAGE on printers.
# In modern usage: rarely seen, mostly in old codebases.

text = "Page 1\fPage 2"
print(text)         # behavior varies by system/terminal
print(len("\f"))    # 1
print(repr("\f"))   # '\f'

# In some contexts, \f is just treated like a whitespace character.
# The .strip() method strips \f along with spaces, \t, \n etc.
print("  \f  hello  \f  ".strip())     # hello


# ------------------------------------------------------------
# PART 10: \a - Bell / Alert
# ------------------------------------------------------------

# \a = alert/bell character (ASCII 7)
# On old terminals, this would ring the physical bell!
# On modern systems: might produce a beep sound (system-dependent).

print("\a")     # might beep! (or do nothing)
print(len("\a"))    # 1
print(repr("\a"))   # '\a'

# Rarely used in modern Python code.
# You might see it in legacy code or terminal applications.


# ------------------------------------------------------------
# PART 11: \v - Vertical Tab
# ------------------------------------------------------------

# \v = vertical tab (ASCII 11)
# Historically moved the paper/cursor down to the next tab stop.
# In modern usage: essentially equivalent to \n in most contexts.

text = "Hello\vWorld"
print(text)         # behavior varies
print(len("\v"))    # 1
print(repr("\v"))   # '\v'

# Like \f, very rarely used in modern code.
# .strip() also strips \v along with other whitespace.


# ------------------------------------------------------------
# PART 12: \x - Hexadecimal escape
# ------------------------------------------------------------

# \xNN where NN is a two-digit hexadecimal number (00-FF)
# Represents the character with that ASCII/Unicode code point.

# ── Common ASCII characters via hex ~~
print("\x48\x65\x6c\x6c\x6f")  # Hello
# H=0x48, e=0x65, l=0x6c, l=0x6c, o=0x6f

print("\x41")   # A  (65 in decimal = 0x41 in hex)
print("\x61")   # a  (97 in decimal = 0x61 in hex)
print("\x30")   # 0  (48 in decimal = 0x30 in hex)
print("\x0A")   # newline (10 in decimal = 0x0A in hex)

# ── Verify with ord() and chr() ~~
print(ord("A"))     # 65   ← ASCII code of 'A'
print(hex(65))      # 0x41 ← hex representation
print("\x41")       # A    ← character from hex code

# ── Useful for non-printable characters ~~
null_byte = "\x00"  # NULL character (ASCII 0)
print(len(null_byte))   # 1
print(repr(null_byte))  # '\x00'

# ── Mixed with normal characters ~~
text = "ABC\x44EF"     # D = 0x44
print(text)             # ABCDEF


# ------------------------------------------------------------
# PART 13: \u and \U - Unicode escape sequences
# ------------------------------------------------------------

# Python strings are Unicode by default.
# You can include ANY Unicode character using escape sequences.

# \uXXXX  = Unicode character with 4-digit hex code (BMP)
# \UXXXXXXXX = Unicode character with 8-digit hex code (full Unicode)

# ── Common Unicode characters ~~
print("\u00e9")     # é  (Latin small letter e with acute)
print("\u00f1")     # ñ  (Latin small letter n with tilde)
print("\u03b1")     # α  (Greek small letter alpha)
print("\u03b2")     # β  (Greek small letter beta)
print("\u03c0")     # π  (Greek small letter pi)
print("\u2665")     # ♥  (heart symbol)
print("\u2603")     # ☃  (snowman)
print("\u2713")     # ✓  (check mark)
print("\u2717")     # ✗  (cross mark)
print("\u221e")     # ∞  (infinity)
print("\u0394")     # Δ  (Greek capital delta)
print("\u00b0")     # °  (degree symbol)

# ── DNA/Biology unicode symbols ~~
print("\u2192")     # →  (right arrow - used in reactions)
print("\u2190")     # ←  (left arrow)
print("\u21cc")     # ⇌  (equilibrium arrows)

# ── \U for characters outside BMP (rare) ~~
print("\U0001F600") # 😀 (emoji - requires 8-digit code)
print("\U0001F40D") # 🐍 (snake emoji - perfect for Python!)
print("\U0001F9EC") # 🧬 (DNA emoji)

# ── \N{name} - Unicode named characters ~~
# You can also use Unicode character NAMES:
print("\N{SNOWMAN}")            # ☃
print("\N{BLACK HEART SUIT}")   # ♥
print("\N{GREEK SMALL LETTER PI}")  # π
print("\N{DEGREE SIGN}")        # °


# ------------------------------------------------------------
# PART 14: repr() - seeing escape sequences
# ------------------------------------------------------------

# When you have a string with escape sequences,
# print() shows the RENDERED result (newlines, tabs etc.)
# repr() shows the RAW representation with visible escape sequences.

# This is ESSENTIAL for debugging whitespace and special chars!

text = "Hello\nWorld\t!"
print(text)         # Hello
                    # World	!
print(repr(text))   # 'Hello\nWorld\t!'  ← escape sequences visible!

# ── Use repr() when debugging ~~
line_from_file = "Anna Kowalska\n"
print(line_from_file)       # Anna Kowalska (+ invisible newline)
print(repr(line_from_file)) # 'Anna Kowalska\n'  ← newline visible!

# ── repr() on single characters ~~
print(repr("\n"))   # '\n'
print(repr("\t"))   # '\t'
print(repr("\\"))   # '\\'
print(repr("\x41")) # 'A'  ← already a printable character

# ── The difference ~~
# print() is for human-readable output
# repr() is for programmer/debugging output


# ------------------------------------------------------------
# PART 15: Special characters and string operations
# ------------------------------------------------------------

# Special characters behave exactly like regular characters
# in ALL string operations. The key insight: ONE escape
# sequence = ONE character.

# ── len() ~~
print(len("\n"))        # 1   ← newline is ONE char
print(len("\t"))        # 1   ← tab is ONE char
print(len("\\"))        # 1   ← backslash is ONE char
print(len("\u03b1"))    # 1   ← alpha is ONE char
print(len("Hello\n"))   # 6   ← 5 + 1

# ── Indexing ~~
text = "A\nB"
print(text[0])      # A
print(text[1])      # (newline - invisible when printed)
print(repr(text[1]))# '\n'  ← use repr() to see it!
print(text[2])      # B

# ── Slicing ~~
text = "Line1\nLine2"
print(text[:5])     # Line1
print(text[6:])     # Line2
print(text[5])      # (newline)
print(repr(text[5]))# '\n'

# ── .split() with special characters ~~
text = "Hello\nWorld\nPython"
lines = text.split("\n")
print(lines)    # ['Hello', 'World', 'Python']

text = "col1\tcol2\tcol3"
cols = text.split("\t")
print(cols)     # ['col1', 'col2', 'col3']

# ── .replace() with special characters ~~
text = "Hello\nWorld\nPython"
# Replace newlines with spaces:
clean = text.replace("\n", " ")
print(clean)    # Hello World Python

# Replace Windows line endings with Unix:
windows = "Line1\r\nLine2\r\nLine3"
unix = windows.replace("\r\n", "\n")
print(repr(unix))   # 'Line1\nLine2\nLine3'

# ── .count() with special characters ~~
text = "Line1\nLine2\nLine3\nLine4"
newline_count = text.count("\n")
line_count = newline_count + 1
print(f"Lines: {line_count}")   # Lines: 4

# ── .strip() removes ALL whitespace including \t \n \r ~~
messy = "\t\n  Hello World  \n\t"
print(repr(messy))              # '\t\n  Hello World  \n\t'
print(repr(messy.strip()))      # 'Hello World'


# ------------------------------------------------------------
# PART 16: Common mistakes with special characters
# ------------------------------------------------------------

# ── Mistake 1: Forgetting \\ for backslash ~~
# Windows path:
# ❌ path = "C:\new_folder\test.txt"
#           ↑ \n = newline! \t = tab!
# print(path)  # C:
#              # ew_folder	est.txt  ← wrong!

# ✅ Fix:
path = "C:\\new_folder\\test.txt"
print(path)     # C:\new_folder\test.txt

# ── Mistake 2: Confusing printed output with string content ~~
text = "Hello\nWorld"
# print(text) shows TWO lines - looks like TWO strings!
# But it's ONE string with a newline IN it.
print(len(text))    # 11  ← one string!
print(type(text))   # <class 'str'>

# ── Mistake 3: Not using repr() when debugging whitespace ~~
text1 = "Hello "
text2 = "Hello"
print(text1 == text2)   # False  ← but why?? looks the same!
print(repr(text1))      # 'Hello '  ← trailing space revealed!
print(repr(text2))      # 'Hello'

# ── Mistake 4: Escaping characters that don't need it ~~
print("\p")     # might work or give \p literally (implementation-dependent)
print("\q")     # same - undefined escape sequences
# Python 3.12+ raises DeprecationWarning for invalid escapes
# Use raw strings when you don't want escape processing

# ── Mistake 5: \n inside f-strings (Python < 3.12) ~~
# Before Python 3.12, you couldn't use \n inside f-string {}:
name = "Anna"
# ❌ Old Python: f"{'\\n'.join(['a', 'b'])}"
# ✅ Better approach: build the string first, then use f-string
separator = "\n"
result = f"Hello {name}"
print(result)


# ------------------------------------------------------------
# PART 17: Complete reference table
# ------------------------------------------------------------

# ┌──────────┬──────────────┬───────┬───────────────────────────┐
# │ Sequence │ Name         │ ASCII │ Description               │
# ├──────────┼──────────────┼───────┼───────────────────────────┤
# │ \\       │ Backslash    │  92   │ Literal backslash \       │
# │ \'       │ Single quote │  39   │ Literal '                 │
# │ \"       │ Double quote │  34   │ Literal "                 │
# │ \n       │ Newline      │  10   │ New line (most common!)   │
# │ \t       │ Tab          │   9   │ Horizontal tab            │
# │ \r       │ Carriage ret │  13   │ Return to line start      │
# │ \b       │ Backspace    │   8   │ Move cursor left one      │
# │ \f       │ Form feed    │  12   │ Next page (printers)      │
# │ \a       │ Alert/Bell   │   7   │ Audible beep              │
# │ \v       │ Vertical tab │  11   │ Vertical tab              │
# │ \0       │ Null         │   0   │ Null character            │
# │ \xNN     │ Hex escape   │  var  │ Char with hex code NN     │
# │ \uNNNN   │ Unicode BMP  │  var  │ Unicode char (4 hex digits)│
# │ \UNNNNNN │ Unicode full │  var  │ Unicode char (8 hex digits)│
# │ \N{name} │ Unicode name │  var  │ Unicode char by name      │
# └──────────┴──────────────┴───────┴───────────────────────────┘

# Quick test of the main ones:
print("Backslash:     \\")
print("Newline:       before\nafter")
print("Tab:           before\tafter")
print("Single quote:  it\'s")
print("Double quote:  say \"hi\"")
print("Unicode pi:    \u03c0")
print("Degree:        100\u00b0C")
print("DNA:           \U0001F9EC")


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Escape sequences start with backslash \
# ✅ Each escape sequence = ONE character (affects len()!)
# ✅ \n  → newline (most important!)
# ✅ \t  → horizontal tab
# ✅ \\  → literal backslash (use in Windows paths!)
# ✅ \'  → literal single quote
# ✅ \"  → literal double quote
# ✅ \r  → carriage return (Windows line endings: \r\n)
# ✅ \b  → backspace
# ✅ \a  → alert/bell
# ✅ \f  → form feed
# ✅ \v  → vertical tab
# ✅ \xNN    → character by hex code
# ✅ \uNNNN  → Unicode character (4 hex digits)
# ✅ \UNNNNNN→ Unicode character (8 hex digits)
# ✅ \N{name}→ Unicode character by name
# ✅ repr() reveals hidden escape sequences (use for debugging!)
# ✅ print() renders them; repr() shows them as code
# ✅ All string operations (len, index, slice, count) treat
#    each escape sequence as ONE character
# ✅ .strip() removes \n \t \r \f \v along with spaces
# ✅ Windows paths need \\ or use raw strings r"C:\path"