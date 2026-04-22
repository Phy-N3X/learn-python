# ============================================================
# MODULE 02 | LECTURE 21 - .split()
# ============================================================
# What you will learn:
#   - What .split() does and why it exists
#   - Default behavior: splitting on whitespace
#   - Splitting on a specific separator
#   - The maxsplit parameter
#   - What .split() returns (a LIST)
#   - Accessing elements of the result
#   - .rsplit() - splitting from the right
#   - .splitlines() - splitting on line breaks
#   - Edge cases and surprising behaviors
#   - Real world use cases
#   - Common mistakes
# ============================================================


# ------------------------------------------------------------
# PART 1: The problem .split() solves
# ------------------------------------------------------------

# So far we have worked with strings as a whole unit.
# But very often, data comes as ONE string that contains
# MULTIPLE pieces of information separated by something.

# Examples from real life:
#   "Anna,25,Warsaw,Poland"      ← CSV data (comma-separated)
#   "2024-03-15"                 ← date (dash-separated)
#   "Hello World Python"         ← words (space-separated)
#   "/home/user/documents/file"  ← file path (slash-separated)
#   "ATG CCC GCA TTA"            ← codons (space-separated)

# Without .split(), extracting "25" from "Anna,25,Warsaw,Poland"
# requires manual slicing - tedious and fragile.

# With .split():
data = "Anna,25,Warsaw,Poland"
parts = data.split(",")
print(parts)        # ['Anna', '25', 'Warsaw', 'Poland']
print(parts[1])     # 25  ← easy access to any piece!

# .split() is one of the most frequently used string methods
# in real Python programming.


# ------------------------------------------------------------
# PART 2: What does .split() return?
# ------------------------------------------------------------

# .split() returns a LIST.
# A list is an ordered collection of items (Module 05).
# For now, think of it as a numbered sequence of strings.

# We haven't covered lists in detail yet, but we need to
# understand the basics to use .split() properly.

# A list looks like this:
#   ['item0', 'item1', 'item2', 'item3']
#    ↑                                ↑
#    square brackets, items separated by commas

# You can access items using indexes (just like strings!):
#   result[0] → first item
#   result[1] → second item
#   result[-1] → last item

sentence = "Hello World Python"
words = sentence.split()
print(words)        # ['Hello', 'World', 'Python']
print(words[0])     # Hello   ← first word
print(words[1])     # World   ← second word
print(words[2])     # Python  ← third word
print(words[-1])    # Python  ← last word

# The type of the result:
print(type(words))  # <class 'list'>
# Each element is a string:
print(type(words[0]))   # <class 'str'>

# Length of the result (number of items):
print(len(words))   # 3  ← three words


# ------------------------------------------------------------
# PART 3: Default behavior - splitting on whitespace
# ------------------------------------------------------------

# When called with NO arguments, .split() splits on
# ANY whitespace (spaces, tabs, newlines).
# It also automatically removes ALL leading/trailing whitespace
# and treats MULTIPLE consecutive whitespace as ONE separator.

# ── Basic split on spaces ──
sentence = "Hello World Python"
print(sentence.split())    # ['Hello', 'World', 'Python']

# ── Multiple spaces → treated as one separator ──
sentence = "Hello    World     Python"
print(sentence.split())    # ['Hello', 'World', 'Python']
# Even though there are multiple spaces, we still get 3 items!
# This is DIFFERENT from split(" ") - we'll see this in Part 5.

# ── Leading and trailing whitespace ignored ──
sentence = "   Hello World Python   "
print(sentence.split())    # ['Hello', 'World', 'Python']
# No empty strings at the start or end!

# ── Mixed whitespace types ──
messy = "Hello\tWorld\nPython"    # tab and newline
print(messy.split())              # ['Hello', 'World', 'Python']

# ── Very messy whitespace ──
very_messy = "  Hello  \t  World  \n  Python  "
print(very_messy.split())         # ['Hello', 'World', 'Python']

# This intelligent behavior makes .split() (no args)
# perfect for processing human-readable text.


# ------------------------------------------------------------
# PART 4: Splitting on a specific separator
# ------------------------------------------------------------

# You can pass a separator string as the argument.
# .split(separator) splits the string at EVERY occurrence
# of that separator.

# ── Split on comma ──
csv = "Anna,25,Warsaw,Poland"
parts = csv.split(",")
print(parts)    # ['Anna', '25', 'Warsaw', 'Poland']

# ── Split on dash ──
date = "2024-03-15"
parts = date.split("-")
print(parts)    # ['2024', '03', '15']
year  = parts[0]    # '2024'
month = parts[1]    # '03'
day   = parts[2]    # '15'
print(f"Year: {year}, Month: {month}, Day: {day}")

# ── Split on dot ──
version = "3.11.2"
parts = version.split(".")
print(parts)    # ['3', '11', '2']
major = parts[0]    # '3'
minor = parts[1]    # '11'
patch = parts[2]    # '2'

# ── Split on slash (file path) ──
path = "/home/user/documents/file.txt"
parts = path.split("/")
print(parts)    # ['', 'home', 'user', 'documents', 'file.txt']
# Note the empty string at the start! (before the first /)
filename = parts[-1]    # 'file.txt'
print(filename)

# ── Split on a word ──
text = "oneANDtwoANDthree"
parts = text.split("AND")
print(parts)    # ['one', 'two', 'three']

# ── Split on multiple characters (as a unit) ──
text = "hello::world::python"
parts = text.split("::")
print(parts)    # ['hello', 'world', 'python']
# Note: "::" is treated as ONE separator, not two ":"


# ------------------------------------------------------------
# PART 5: split(" ") vs split() - a critical difference!
# ------------------------------------------------------------

# This is a very common source of confusion.
# split()    → split on ANY whitespace, ignore multiple spaces
# split(" ") → split on EXACTLY one space character

# ── With multiple spaces ──
text = "Hello    World"

print(text.split())     # ['Hello', 'World']        ← 2 items
print(text.split(" "))  # ['Hello', '', '', '', 'World']  ← 5 items!
#                                   ↑   ↑   ↑
#                         empty strings from multiple spaces!

# ── With leading/trailing spaces ──
text = "  Hello World  "

print(text.split())     # ['Hello', 'World']  ← clean!
print(text.split(" "))  # ['', '', 'Hello', 'World', '', '']  ← messy!

# ── When to use which? ──
# split()    → for human-readable text with variable whitespace
# split(" ") → when you need to preserve empty fields
#              (rarely needed, but sometimes important in data processing)

# Example where split(" ") is useful:
# Fixed-width data where empty fields matter:
record = "Anna  25"   # two spaces = empty middle field
print(record.split(" "))    # ['Anna', '', '25']
# The empty string '' represents the empty field


# ------------------------------------------------------------
# PART 6: The maxsplit parameter
# ------------------------------------------------------------

# .split(separator, maxsplit) limits the number of splits.
# After maxsplit splits, the REST of the string is
# kept as ONE final element (no matter what's in it).
#
# .split(sep, maxsplit)
# or
# .split(maxsplit=n)  ← keyword argument (for default separator)

text = "one two three four five"

# Split at most 1 time:
print(text.split(" ", 1))
# ['one', 'two three four five']
# ↑ split once, rest is one string

# Split at most 2 times:
print(text.split(" ", 2))
# ['one', 'two', 'three four five']

# Split at most 3 times:
print(text.split(" ", 3))
# ['one', 'two', 'three', 'four five']

# Split all (no limit):
print(text.split(" "))
# ['one', 'two', 'three', 'four', 'five']

# ── Practical use: split only the first field ──
log_line = "2024-03-15 ERROR Something went wrong in module X"
parts = log_line.split(" ", 2)
date    = parts[0]  # '2024-03-15'
level   = parts[1]  # 'ERROR'
message = parts[2]  # 'Something went wrong in module X'
print(f"Date: {date}")
print(f"Level: {level}")
print(f"Message: {message}")

# ── maxsplit with custom separator ──
csv = "Anna,25,Warsaw,Poland,Europe"
parts = csv.split(",", 2)
print(parts)    # ['Anna', '25', 'Warsaw,Poland,Europe']
# Only split at the first 2 commas!


# ------------------------------------------------------------
# PART 7: .rsplit() - splitting from the RIGHT
# ------------------------------------------------------------

# .rsplit() works exactly like .split() but starts
# splitting from the RIGHT side of the string.
# This matters ONLY when maxsplit is specified.
# Without maxsplit, .rsplit() and .split() give identical results.

text = "one two three four five"

# .split() and .rsplit() without maxsplit → same result:
print(text.split(" "))      # ['one', 'two', 'three', 'four', 'five']
print(text.rsplit(" "))     # ['one', 'two', 'three', 'four', 'five']

# WITH maxsplit: direction matters!
print(text.split(" ", 2))   # ['one', 'two', 'three four five']
#                               ↑ splits from LEFT, remainder at END

print(text.rsplit(" ", 2))  # ['one two three', 'four', 'five']
#                               ↑ splits from RIGHT, remainder at START

# ── Practical use: get filename and extension ──
filepath = "/home/user/documents/report.final.pdf"

# Get extension (split from right, 1 time):
parts = filepath.rsplit(".", 1)
print(parts[0])     # /home/user/documents/report.final
print(parts[1])     # pdf  ← extension!

# Compare with split from left:
parts_left = filepath.split(".", 1)
print(parts_left[0])    # /home/user/documents/report
print(parts_left[1])    # final.pdf  ← not what we wanted!

# .rsplit(".", 1) is the standard way to separate
# a filename from its extension.


# ------------------------------------------------------------
# PART 8: .splitlines() - splitting on line breaks
# ------------------------------------------------------------

# .splitlines() splits a string on line boundaries.
# It handles ALL types of line endings:
#   \n   → Unix/Linux/Mac newline
#   \r\n → Windows newline
#   \r   → old Mac newline

# ── Basic usage ──
text = "Line 1\nLine 2\nLine 3"
print(text.splitlines())
# ['Line 1', 'Line 2', 'Line 3']

# Compare with split("\n"):
print(text.split("\n"))
# ['Line 1', 'Line 2', 'Line 3']  ← same here!

# ── Where they DIFFER: trailing newline ──
text_with_trailing = "Line 1\nLine 2\n"

print(text_with_trailing.split("\n"))
# ['Line 1', 'Line 2', '']  ← empty string at the end!

print(text_with_trailing.splitlines())
# ['Line 1', 'Line 2']  ← no empty string! cleaner.

# ── Windows line endings ──
windows_text = "Line 1\r\nLine 2\r\nLine 3"
print(windows_text.splitlines())
# ['Line 1', 'Line 2', 'Line 3']  ← handles \r\n correctly!

print(windows_text.split("\n"))
# ['Line 1\r', 'Line 2\r', 'Line 3']  ← \r left in! messy.

# ── When to use .splitlines() ──
# Use it when reading text files or multiline strings.
# It handles all line ending styles automatically.
# Prefer it over .split("\n") for file processing.

multiline = """First line
Second line
Third line"""

lines = multiline.splitlines()
print(lines)        # ['First line', 'Second line', 'Third line']
print(len(lines))   # 3
print(lines[0])     # First line


# ------------------------------------------------------------
# PART 9: What the separator is NOT included in the result
# ------------------------------------------------------------

# The separator is used to find split points but
# is NOT included in any of the resulting pieces.

text = "hello:world:python"
parts = text.split(":")
print(parts)    # ['hello', 'world', 'python']
# Note: no ":" in any element!

# This is consistent and expected, but worth noting.
# If you need to keep the separator, you need a different approach
# (re.split() with capturing groups - advanced topic).

# ── The separator is consumed ──
text = "a--b--c"
print(text.split("--"))     # ['a', 'b', 'c']
# "--" is gone from all elements


# ------------------------------------------------------------
# PART 10: Edge cases - empty strings in results
# ------------------------------------------------------------

# When the separator appears at the START, END, or
# CONSECUTIVELY, .split(sep) produces empty strings "".

# ── Separator at the start ──
text = ",Anna,25"
print(text.split(","))      # ['', 'Anna', '25']
#                              ↑ empty string before first comma

# ── Separator at the end ──
text = "Anna,25,"
print(text.split(","))      # ['Anna', '25', '']
#                                           ↑ empty string after last comma

# ── Consecutive separators ──
text = "Anna,,25"
print(text.split(","))      # ['Anna', '', '25']
#                                      ↑ empty string between two commas

# ── All of the above ──
text = ",Anna,,25,"
print(text.split(","))      # ['', 'Anna', '', '25', '']

# Compare: default split() NEVER produces empty strings:
text = "  Hello  World  "
print(text.split())     # ['Hello', 'World']    ← no empty strings
print(text.split(" "))  # ['', '', 'Hello', '', 'World', '', '']  ← empty strings!

# Why does this matter?
# When processing CSV or structured data, empty strings
# represent MISSING VALUES - important information!
# Don't filter them out blindly.


# ------------------------------------------------------------
# PART 11: Splitting on a separator that doesn't exist
# ------------------------------------------------------------

# If the separator is not found in the string,
# .split() returns a list with the WHOLE string as ONE element.

text = "Hello World"
print(text.split(","))      # ['Hello World']  ← one element, no split!
print(len(text.split(","))) # 1

# This is safe - no error is raised.
# But it means you should check the length before assuming
# the split worked!

# ── Check if split was successful ──
data = "Anna,25"
parts = data.split(",")
if len(parts) == 2:
    name = parts[0]
    age  = parts[1]
    print(f"Name: {name}, Age: {age}")
else:
    print("Unexpected format!")


# ------------------------------------------------------------
# PART 12: Combining .split() with other methods
# ------------------------------------------------------------

# .split() is rarely used alone.
# It's usually part of a pipeline:
# clean → split → process each part

# ── Strip then split ──
raw = "  Anna , 25 , Warsaw  "
# First strip the whole thing, then split:
parts = raw.strip().split(",")
print(parts)    # ['Anna ', ' 25 ', ' Warsaw']
# Hmm, there are still spaces around each part!
# We'd need to strip each element too (possible with loops - Module 04)

# ── Split then access specific parts ──
email = "anna.kowalska@university.edu"
parts = email.split("@")
username = parts[0]     # anna.kowalska
domain   = parts[1]     # university.edu
print(f"Username: {username}")
print(f"Domain: {domain}")

# ── Split and convert ──
data = "2024-03-15"
parts = data.split("-")
year  = int(parts[0])   # 2024 as integer
month = int(parts[1])   # 3 as integer
day   = int(parts[2])   # 15 as integer
print(year + 1)         # 2025  ← now we can do math!

# ── Split and upper ──
csv = "anna,25,warsaw"
parts = csv.split(",")
print(parts[0].upper())     # ANNA
print(parts[2].title())     # Warsaw

# ── Count words in a sentence ──
sentence = "The quick brown fox jumps over the lazy dog"
word_count = len(sentence.split())
print(f"Word count: {word_count}")  # Word count: 9


# ------------------------------------------------------------
# PART 13: Reassembling after split - preview of .join()
# ------------------------------------------------------------

# .split() breaks a string apart.
# .join() puts it back together (next lecture!).
# They are COMPLEMENTARY methods.

# Preview:
words = "Hello World Python".split()
print(words)                    # ['Hello', 'World', 'Python']

# Put back together with spaces:
reassembled = " ".join(words)
print(reassembled)              # Hello World Python

# Put together with different separator:
dashed = "-".join(words)
print(dashed)                   # Hello-World-Python

# This split → process → join pattern is extremely common!
# Example: normalize whitespace in a string
messy = "Hello    World     Python"
normalized = " ".join(messy.split())
print(normalized)               # Hello World Python
# split() removes extra spaces, join() puts back single spaces!


# ------------------------------------------------------------
# PART 14: Real world applications
# ------------------------------------------------------------

# ── Application 1: Parse CSV line ──
csv_line = "Anna,Kowalska,25,Warsaw,Poland,anna@email.com"
fields = csv_line.split(",")
first_name = fields[0]  # Anna
last_name  = fields[1]  # Kowalska
age        = fields[2]  # 25
city       = fields[3]  # Warsaw
country    = fields[4]  # Poland
email      = fields[5]  # anna@email.com
print(f"{first_name} {last_name}, age {age}, from {city}, {country}")

# ── Application 2: Parse a date ──
date = "2024-03-15"
year, month, day = date.split("-")      # unpacking! (preview)
print(f"Year: {year}, Month: {month}, Day: {day}")

# ── Application 3: Get file extension ──
filename = "genome_sequence.fasta"
parts = filename.rsplit(".", 1)
name = parts[0]     # genome_sequence
ext  = parts[1]     # fasta
print(f"Name: {name}, Extension: {ext}")

# ── Application 4: Parse a URL ──
url = "https://www.university.edu/bioinformatics/module1"
protocol = url.split("://")[0]          # https
rest = url.split("://")[1]              # www.university.edu/bioinformatics/module1
domain = rest.split("/")[0]             # www.university.edu
path_parts = rest.split("/")[1:]        # ['bioinformatics', 'module1']
print(f"Protocol: {protocol}")
print(f"Domain: {domain}")

# ── Application 5: Count word frequency (simple) ──
text = "the cat sat on the mat and the cat sat"
words = text.split()
cat_count = words.count("cat")      # preview of list.count()
the_count = words.count("the")
print(f"'cat' appears {cat_count} times")   # 2
print(f"'the' appears {the_count} times")   # 3

# ── Application 6: Parse log entries ──
log = "2024-03-15 14:30:22 ERROR Database connection failed"
parts = log.split(" ", 3)
date    = parts[0]  # 2024-03-15
time    = parts[1]  # 14:30:22
level   = parts[2]  # ERROR
message = parts[3]  # Database connection failed
print(f"[{date} {time}] {level}: {message}")

# ── Application 7: Split DNA into codons ──
dna = "ATGCCCGCATTAGTCGA"
# Split into groups of 3 (without loops - manual for now):
codon1 = dna[0:3]   # ATG
codon2 = dna[3:6]   # CCC
codon3 = dna[6:9]   # GCA
# Better with loops (Module 04), but split is useful for other DNA tasks:

# Split DNA on a recognition sequence:
dna_seq = "ATGCCCGAATTCGCATTAGAATTCGTCGA"
recognition = "GAATTC"     # EcoRI restriction enzyme site
fragments = dna_seq.split(recognition)
print(fragments)    # ['ATGCCCG', 'GCATTAGAATTCGTCGA'] wait...
# Actually: ['ATGCCC', 'GCA', 'GTA'] - let's verify:
print(dna_seq.split(recognition))
# Shows where the enzyme would cut the DNA!

# ── Application 8: Normalize whitespace ──
messy_text = "Hello    World   how   are   you"
normalized = " ".join(messy_text.split())
print(normalized)   # Hello World how are you


# ------------------------------------------------------------
# PART 15: Common mistakes with .split()
# ------------------------------------------------------------

# ── Mistake 1: Forgetting .split() returns a LIST ──
text = "Hello World"
result = text.split()
# print(result + "!")  # ❌ TypeError: can only concatenate list to list
print(result[0] + "!")  # ✅ Hello!  ← access the element first

# ── Mistake 2: split() vs split(" ") ──
text = "Hello   World"
print(text.split())     # ['Hello', 'World']         ← 2 items ✅
print(text.split(" "))  # ['Hello', '', '', 'World'] ← 4 items ❌ (usually)

# ── Mistake 3: Index out of range after split ──
data = "Anna"               # no comma!
parts = data.split(",")
print(parts)                # ['Anna']  ← only 1 element
# print(parts[1])           # ❌ IndexError!
# Always check len(parts) before accessing by index

# ── Mistake 4: Not storing the result ──
text = "Hello World Python"
text.split()                # ← thrown away!
print(text)                 # Hello World Python  ← unchanged!

# ✅ Fix:
words = text.split()
print(words)                # ['Hello', 'World', 'Python']

# ── Mistake 5: Expecting split to modify in place ──
text = "Hello World"
parts = text.split()        # returns LIST, text is still a STRING
print(type(text))           # <class 'str'>   ← still a string
print(type(parts))          # <class 'list'>  ← this is the list


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ .split() breaks a string into a LIST of substrings
# ✅ Returns a LIST - access elements with [index]
# ✅ .split()      → split on ANY whitespace, smart handling
# ✅ .split(sep)   → split on specific separator
# ✅ .split(sep, n)→ split at most n times (from left)
# ✅ .rsplit(sep, n)→ split at most n times from RIGHT
# ✅ .splitlines() → split on line breaks (\n, \r\n, \r)
# ✅ split() vs split(" ") → BIG difference with multiple spaces!
# ✅ Separator is NOT included in the result elements
# ✅ Separator not found → returns list with original string as one element
# ✅ Consecutive separators → empty strings "" in result
# ✅ Default split() NEVER produces empty strings
# ✅ .split() returns a new list, original string unchanged
# ✅ Combine with .strip() to clean before splitting
# ✅ Complement of .join() - split apart, join back together
# ✅ Use len(result) to check how many parts were produced