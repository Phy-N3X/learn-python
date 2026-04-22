# ============================================================
# MODULE 02 | LECTURE 28 - Raw Strings
# ============================================================
# What you will learn:
#   - What raw strings are and why they exist
#   - The r"..." syntax
#   - How raw strings treat backslashes
#   - When to use raw strings vs regular strings
#   - Raw strings with single and double quotes
#   - Raw strings and triple quotes
#   - What raw strings CANNOT do
#   - Raw strings in regular expressions (preview)
#   - Raw strings and file paths
#   - Common mistakes and misconceptions
# ============================================================


# ------------------------------------------------------------
# PART 1: The problem raw strings solve
# ------------------------------------------------------------

# In the previous lecture we learned about escape sequences.
# The backslash \ has SPECIAL MEANING in Python strings.
# This causes problems in certain situations.

# ── Problem 1: Windows file paths ──
# Windows uses backslashes in paths.
# Every backslash needs to be doubled: \\ instead of \

# ❌ Dangerous - \n and \t are escape sequences!
path = "C:\new_users\tom\documents"
print(path)
# C:
# ew_users	om\documents   ← WRONG! \n=newline, \t=tab!
print(repr(path))   # 'C:\new_users\tom\documents'
# Shows \n and \t as actual escape sequences!

# ✅ Fix with doubled backslashes:
path = "C:\\new_users\\tom\\documents"
print(path)         # C:\new_users\tom\documents  ← correct
print(repr(path))   # 'C:\\new_users\\tom\\documents'

# But this is verbose and hard to read.
# The raw string is a much cleaner solution.

# ✅ Fix with raw string:
path = r"C:\new_users\tom\documents"
print(path)         # C:\new_users\tom\documents  ← correct!
print(repr(path))   # 'C:\\new_users\\tom\\documents'

# The r prefix tells Python: "treat all backslashes literally"
# No escape sequence processing happens at all!


# ------------------------------------------------------------
# PART 2: The r"..." syntax
# ------------------------------------------------------------

# A raw string is created by placing the letter r (or R)
# IMMEDIATELY before the opening quote.
#
# Syntax:
#   r"string content"    ← double quotes
#   r'string content'    ← single quotes
#   r"""string content"""← triple double quotes
#   r'''string content'''← triple single quotes
#
# The r can be lowercase OR uppercase: r"..." or R"..."
# Both work identically.

# ── Basic raw string ──
normal = "Hello\nWorld"     # \n = newline
raw    = r"Hello\nWorld"    # \n = literal backslash + n

print(normal)   # Hello
                # World    ← two lines!

print(raw)      # Hello\nWorld   ← literally backslash n, one line!

print(repr(normal))     # 'Hello\nWorld'
print(repr(raw))        # 'Hello\\nWorld'  ← stored as \\ + n

# ── Lengths differ! ──
print(len(normal))  # 11  ← "Hello" + newline + "World"
print(len(raw))     # 12  ← "Hello" + backslash + "n" + "World"
#                              5    +     1      +  1  +   5 = 12


# ------------------------------------------------------------
# PART 3: How raw strings work - no escape processing
# ------------------------------------------------------------

# In a raw string, the backslash is treated as a
# LITERAL BACKSLASH CHARACTER, nothing more.
# Python does NOT interpret \n, \t, \\, \', \" etc.

# ── Every escape sequence becomes literal ──
print(r"\n")    # \n   ← two characters: backslash + n
print(r"\t")    # \t   ← two characters: backslash + t
print(r"\\")    # \\   ← two characters: backslash + backslash
print(r"\'")    # \'   ← two characters: backslash + single quote
print(r"\"")    # \"   ← two characters: backslash + double quote
print(r"\r")    # \r   ← two characters: backslash + r
print(r"\b")    # \b   ← two characters: backslash + b

# ── Verify with len() ──
print(len(r"\n"))   # 2  ← backslash + n (NOT one newline!)
print(len("\n"))    # 1  ← one newline character
print(len(r"\t"))   # 2  ← backslash + t (NOT one tab!)
print(len("\t"))    # 1  ← one tab character

# ── Verify with repr() ──
print(repr(r"\n"))  # '\\n'   ← stored as two characters
print(repr("\n"))   # '\n'    ← stored as one special character

# ── All backslashes are LITERAL in raw strings ──
text = r"C:\Users\Anna\Documents\Python\project.py"
print(text)     # C:\Users\Anna\Documents\Python\project.py
print(len(text))    # 42 (every backslash is one character)

# In a regular string, \U would be a Unicode escape!
# In a raw string, \U is just backslash + U.
regular_risky = "C:\Users"   # \U looks like start of Unicode!
# Python may give a DeprecationWarning or error here
raw_safe = r"C:\Users"       # safe! \U is just backslash + U
print(raw_safe)              # C:\Users


# ------------------------------------------------------------
# PART 4: Raw strings with single and double quotes
# ------------------------------------------------------------

# Raw strings work with both quote types.
# Use whichever is more convenient for your content.

# ── Double-quoted raw strings ──
path1 = r"C:\Users\Anna"
regex1 = r"\d+\.\d+"      # matches decimal numbers
print(path1)    # C:\Users\Anna
print(regex1)   # \d+\.\d+

# ── Single-quoted raw strings ──
path2 = r'C:\Users\Anna'
regex2 = r'\d+\.\d+'
print(path2)    # C:\Users\Anna
print(regex2)   # \d+\.\d+

# ── Choose based on content ──
# If your raw string contains ", use single quotes:
html_attr = r'<div class="main">'
print(html_attr)    # <div class="main">

# If your raw string contains ', use double quotes:
apostrophe = r"it's a raw string"
print(apostrophe)   # it's a raw string

# ── The r prefix works with R too ──
path3 = R"C:\Windows\System32"
print(path3)    # C:\Windows\System32
# r and R are identical - lowercase r is more common.


# ------------------------------------------------------------
# PART 5: Raw strings and the ONE limitation
# ------------------------------------------------------------

# Raw strings have ONE important limitation:
# A raw string CANNOT END with a single backslash!
# (An odd number of backslashes at the end causes SyntaxError)

# ❌ This is a SyntaxError:
# path = r"C:\Users\Anna\"   # ← the \" at end is the issue!

# Why? In a raw string, a backslash at the very end
# "escapes" the closing quote, making the string unterminated.
# Python's tokenizer sees \" as an escaped quote, not end of string.

# ── Even number of backslashes at end is OK ──
path = r"C:\Users\Anna\\"   # ends with \\
print(path)     # C:\Users\Anna\\  ← two backslashes at end!

# ── Workarounds ──
# Option 1: use regular string for the trailing backslash:
path = r"C:\Users\Anna" + "\\"
print(path)     # C:\Users\Anna\  ← one backslash at end!

# Option 2: use regular string with \\ throughout:
path = "C:\\Users\\Anna\\"
print(path)     # C:\Users\Anna\

# Option 3: add the backslash separately:
base = r"C:\Users\Anna"
path = base + "\\"
print(path)     # C:\Users\Anna\


# ------------------------------------------------------------
# PART 6: Raw strings vs regular strings - comparison
# ------------------------------------------------------------

# Let's compare the same content as raw and regular strings:

# ── Windows paths ──
regular = "C:\\Program Files\\Python 3.11\\python.exe"
raw     = r"C:\Program Files\Python 3.11\python.exe"

print(regular == raw)   # True  ← same content!
print(regular)          # C:\Program Files\Python 3.11\python.exe
print(raw)              # C:\Program Files\Python 3.11\python.exe

# They produce IDENTICAL strings!
# raw string is just an easier way to WRITE the same thing.

# ── Regex patterns ──
# Without raw string: every \d needs to be \\d
regular_regex = "\\d+\\.\\d+"      # digits . digits
raw_regex     = r"\d+\.\d+"        # same pattern, much cleaner!

print(regular_regex == raw_regex)   # True  ← identical content!
print(regular_regex)    # \d+\.\d+
print(raw_regex)        # \d+\.\d+

# ── Which to use? ──
# Raw string: when you have MANY backslashes
# Regular:    when you have FEW backslashes (or need escape sequences)


# ------------------------------------------------------------
# PART 7: Raw strings with triple quotes
# ------------------------------------------------------------

# You can combine raw strings with triple quotes
# for multi-line raw strings.

# ── Triple double quotes ──
multiline_raw = r"""
Line 1 with \n (literal backslash-n)
Line 2 with \t (literal backslash-t)
Line 3 with \\ (literal double backslash)
"""
print(multiline_raw)
# (The actual newlines in the source code ARE real newlines)
# (But \n \t \\ inside the text are LITERAL)

# ── Triple single quotes ──
pattern = r'''
^           # start of string
\d{3}       # three digits
-           # literal dash
\d{4}       # four digits
$           # end of string
'''
print(pattern)  # raw multi-line regex pattern

# ── Note: the real line breaks STILL WORK ~~
# In a raw string, ONLY backslash escapes are disabled.
# Actual newlines (pressing Enter in the source) still work!

raw_multiline = r"""First line
Second line
Third line"""
print(raw_multiline)
# First line
# Second line
# Third line
# ↑ REAL newlines work even in raw strings!

# But \n inside the text is NOT a newline:
test = r"First\nSecond"
print(test)     # First\nSecond  ← NOT two lines!
print(len(test.split("\n")))    # 1  ← still one "line" (no real \n!)


# ------------------------------------------------------------
# PART 8: Raw strings in regular expressions
# ------------------------------------------------------------

# This is by far the MOST COMMON use of raw strings.
# Regular expressions use backslash extensively.
# Without raw strings, regex patterns become unreadable.

# We'll preview regex (covered properly in Module 10+).
# For now, just understand WHY raw strings are essential here.

import re   # regular expressions module

# ── Match phone numbers ──
# Pattern: \d{3}-\d{3}-\d{4}  (e.g., 123-456-7890)

# ❌ Regular string version (painful to read):
pattern_regular = "\\d{3}-\\d{3}-\\d{4}"

# ✅ Raw string version (clean and readable):
pattern_raw = r"\d{3}-\d{3}-\d{4}"

# Both work identically in regex:
phone = "Call 123-456-7890 for info"
match_regular = re.search(pattern_regular, phone)
match_raw     = re.search(pattern_raw, phone)
print(match_regular.group())    # 123-456-7890
print(match_raw.group())        # 123-456-7890

# ── Match email addresses ──
email_pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
email = "Contact anna.k@university.edu for help"
match = re.search(email_pattern, email)
print(match.group())    # anna.k@university.edu

# ── Match DNA codons ──
dna_pattern = r"[ATGC]{3}"     # exactly 3 nucleotides
dna = "ATGCCCGCA"
codons = re.findall(dna_pattern, dna)
print(codons)   # ['ATG', 'CCC', 'GCA']

# ── Comparison: how messy without raw strings ──
# With regular strings, every \w, \d, \s etc. needs to be \\w, \\d, \\s
# That doubles ALL the backslashes:
#   r"\w+"     →   "\\w+"    ← much worse!
#   r"\d{2,4}" →   "\\d{2,4}" ← unreadable!
#   r"^\s*\w+" →   "^\\s*\\w+" ← nightmare!

# RULE: ALWAYS use raw strings for regular expressions!


# ------------------------------------------------------------
# PART 9: Raw strings and file paths
# ------------------------------------------------------------

# File paths are the second most common use of raw strings.

# ── Windows paths ──
# Windows uses \ as directory separator.
# This clashes with Python's escape sequences!

# ❌ Risky regular strings:
# These might work by coincidence or might not:
path1 = "C:\Windows"           # \W is undefined, might work
path2 = "C:\new_folder"        # \n = NEWLINE! Definitely wrong!
path3 = "C:\temp\data"         # \t = TAB! Wrong!
path4 = "C:\users\admin"       # \u = Unicode escape! Wrong!

# ✅ Safe regular strings (doubled backslashes):
path1 = "C:\\Windows"
path2 = "C:\\new_folder"
path3 = "C:\\temp\\data"
path4 = "C:\\users\\admin"

# ✅ Safe raw strings (cleanest!):
path1 = r"C:\Windows"
path2 = r"C:\new_folder"
path3 = r"C:\temp\data"
path4 = r"C:\users\admin"

# ── Unix/Linux/Mac paths ──
# Unix uses / as separator - NO backslash! No problem here.
unix_path = "/home/anna/documents/file.txt"
print(unix_path)    # works fine, no backslashes!

# But raw strings still don't hurt on Unix:
unix_raw = r"/home/anna/documents/file.txt"
print(unix_raw)     # same result!

# ── Python's pathlib (modern approach - preview) ~~
# Python 3.4+ has pathlib.Path which handles paths properly.
# But raw strings are still useful with older APIs.
from pathlib import Path
p = Path(r"C:\Users\Anna\Documents")
print(p)    # C:\Users\Anna\Documents (handled properly)


# ------------------------------------------------------------
# PART 10: What raw strings actually ARE internally
# ------------------------------------------------------------

# Raw strings are NOT a different TYPE of string.
# They are just a different NOTATION for writing strings.
# The result is always a regular Python str object.

normal = "C:\\Users\\Anna"
raw    = r"C:\Users\Anna"

# Same content:
print(normal == raw)        # True
print(type(normal))         # <class 'str'>
print(type(raw))            # <class 'str'>  ← same type!
print(id(normal) == id(raw)) # might be True (string interning)

# The r prefix is just syntax sugar that tells the PARSER
# "don't process escape sequences in this string literal".
# Once Python reads the source code, it's just a regular string.

# You CANNOT check at runtime whether a string was
# originally written as a raw string or not!
# r"hello\n" and "hello\\n" are INDISTINGUISHABLE at runtime.
raw_string = r"hello\n"
regular_string = "hello\\n"
print(raw_string == regular_string)     # True
print(repr(raw_string))                 # 'hello\\n'
print(repr(regular_string))             # 'hello\\n'
# Identical!


# ------------------------------------------------------------
# PART 11: Raw strings with string methods
# ------------------------------------------------------------

# Since raw strings are just regular strings,
# ALL string methods work on them exactly the same way!

path = r"C:\Users\Anna\Documents\report.pdf"

# .split() works:
parts = path.split("\\")
print(parts)    # ['C:', 'Users', 'Anna', 'Documents', 'report.pdf']

# .endswith() works:
print(path.endswith(".pdf"))    # True

# .replace() works:
unix_path = path.replace("\\", "/")
print(unix_path)    # C:/Users/Anna/Documents/report.pdf

# .find() works:
pos = path.find("Anna")
print(pos)      # some position

# len() works:
print(len(path))    # 40 (count the characters)

# Indexing works:
print(path[0])      # C
print(path[2])      # \   ← backslash!

# All normal operations work!


# ------------------------------------------------------------
# PART 12: Raw strings and other string prefixes
# ------------------------------------------------------------

# Python has several string prefix letters.
# They can be combined in certain ways.

# ── String prefixes ──
# r or R  → raw string (no escape processing)
# b or B  → bytes literal (not a string, used for binary data)
# f or F  → f-string (formatted string - Module 01)
# u or U  → Unicode (default in Python 3, essentially no-op)

# ── Combining prefixes ──
# rb or br → raw bytes (raw + binary)
raw_bytes = rb"Hello\nWorld"    # \n is literal, and it's bytes
print(type(raw_bytes))          # <class 'bytes'>
print(raw_bytes)                # b'Hello\\nWorld'

# rf or fr → raw f-string (Python 3.6+)
name = "Anna"
raw_fstring = rf"Hello {name}\nThis is a raw f-string"
print(raw_fstring)  # Hello Anna\nThis is a raw f-string
# The {name} IS processed (f-string feature)
# But \n is NOT processed (raw feature)!

# More raw f-string examples:
path = r"C:\Users"
message = rf"Your files are in {path}\Documents"
print(message)  # Your files are in C:\Users\Documents

# ── Order of prefixes ~~
# r before f: rf"..."  ← most common order
# f before r: fr"..."  ← also works, same result
print(rf"test\n{name}")  # test\nAnna
print(fr"test\n{name}")  # test\nAnna  ← identical!


# ------------------------------------------------------------
# PART 13: Common use cases summary
# ------------------------------------------------------------

# ── Use case 1: Windows file paths ──
log_file    = r"C:\Windows\System32\logs\error.log"
config_file = r"C:\Program Files\MyApp\config.ini"
data_folder = r"D:\Projects\Python\data"

print(log_file)
print(config_file)
print(data_folder)

# ── Use case 2: Regular expression patterns ──
import re

# Phone number pattern:
phone_pattern = r"\+?\d{1,3}[-.\s]?\(?\d{1,3}\)?[-.\s]?\d{3,4}[-.\s]?\d{4}"

# Email pattern:
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

# IP address pattern:
ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"

# DNA pattern:
dna_pattern = r"[ATGC]+"

# All clean and readable because of raw strings!

# ── Use case 3: LaTeX strings ──
# LaTeX uses backslash heavily for commands:
latex = r"\begin{document}\section{Introduction}\end{document}"
print(latex)    # \begin{document}\section{Introduction}\end{document}

# ── Use case 4: Network paths (UNC paths) ──
network_path = r"\\server\share\folder\file.txt"
print(network_path)     # \\server\share\folder\file.txt

# ── Use case 5: Template strings ~~
template = r"""
SELECT *
FROM {table}
WHERE name = '\{name\}'
ORDER BY id DESC
"""
# Backslashes in SQL need to be literal


# ------------------------------------------------------------
# PART 14: Raw strings - when NOT to use them
# ------------------------------------------------------------

# Raw strings are great, but don't overuse them.
# Sometimes you actually NEED escape sequences.

# ── Don't use raw strings when you need \n ──
# ❌ Wrong - this won't print on two lines:
text = r"First line\nSecond line"
print(text)     # First line\nSecond line  ← one line! \n not processed

# ✅ Correct:
text = "First line\nSecond line"
print(text)     # First line
                # Second line  ← two lines!

# ── Don't use raw strings when you need \t ~~
header = r"Name\tAge\tCity"     # ❌ \t not a tab!
header = "Name\tAge\tCity"      # ✅ real tabs

# ── Don't use raw strings for simple strings ~~
# If there are no backslashes, raw string adds no value:
text = r"Hello World"   # ← pointless! same as "Hello World"
text = "Hello World"    # ← simpler and clearer

# ── General rule ~~
# Use raw strings ONLY when your string contains backslashes
# that you want to be literal (not escape sequences).
# This is mainly for: file paths, regex patterns, LaTeX.


# ------------------------------------------------------------
# PART 15: Common mistakes with raw strings
# ------------------------------------------------------------

# ── Mistake 1: Trying to end with single backslash ──
# ❌ SyntaxError:
# path = r"C:\Users\Anna\"      # cannot end with odd number of backslashes!

# ✅ Workarounds:
path = r"C:\Users\Anna" + "\\"  # append backslash separately
path = "C:\\Users\\Anna\\"      # use regular string

# ── Mistake 2: Thinking raw strings "fix" all problems ~~
# Raw strings don't escape quote characters the way \' does.
# You still need to use the OTHER quote type if your string
# contains quotes.

# ❌ SyntaxError:
# text = r"She said "hello""   # closing " ends the string!

# ✅ Fix: use single quotes:
text = r'She said "hello"'
print(text)     # She said "hello"

# ── Mistake 3: Confusing source and string ~~
raw = r"\n"         # source has \n, string has backslash + n
normal = "\\n"      # source has \\n, string has backslash + n
print(raw == normal)        # True  ← same string!
print(len(raw))             # 2
print(len(normal))          # 2
# Different SOURCE, same STRING!

# ── Mistake 4: Using raw strings where you need escape seqs ~~
multiline = r"Line 1\nLine 2\nLine 3"  # ← NOT multiline!
print(multiline)    # Line 1\nLine 2\nLine 3  ← one line!

# ✅ Use regular string for actual newlines:
multiline = "Line 1\nLine 2\nLine 3"   # real newlines
print(multiline)
# Line 1
# Line 2
# Line 3

# ── Mistake 5: raw f-string with \n inside {} ~~
name = "Anna"
# In Python < 3.12, \n inside {} of f-string needs care:
# rf"Hello {name}\nWorld"  ← \n outside {} is literal (raw)
# rf"{'\\n'.join(['a','b'])}" ← complex but possible
result = rf"Hello {name}\nThis is on one line"
print(result)   # Hello Anna\nThis is on one line  ← \n is literal!


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Raw strings: prefix r before the quote: r"..." or r'...'
# ✅ In a raw string: ALL backslashes are LITERAL
# ✅ No escape sequence processing: \n stays as \, n (2 chars)
# ✅ Raw strings are STILL regular str objects
# ✅ r"C:\n" and "C:\\n" produce IDENTICAL strings
# ✅ Cannot end with ODD number of backslashes → SyntaxError
# ✅ Workaround: r"path" + "\\" to add trailing backslash
# ✅ Works with single, double, and triple quotes
# ✅ Main use cases:
#     1. Windows file paths: r"C:\Users\Anna"
#     2. Regular expressions: r"\d+\.\d+"
#     3. LaTeX: r"\begin{document}"
# ✅ rf"..." or fr"..." = raw f-string (variables + literal \)
# ✅ rb"..." = raw bytes literal
# ✅ Don't use raw strings when you actually need \n, \t etc.
# ✅ Actual newlines in source code still work in raw strings
# ✅ Use repr() to see what's actually in your string