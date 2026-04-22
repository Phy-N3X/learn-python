# ============================================================
# MODULE 02 | LECTURE 23 - .find() and .index()
# ============================================================
# What you will learn:
#   - What .find() does and how to use it
#   - What .index() does and how it differs from .find()
#   - The full syntax: start and end parameters
#   - .rfind() and .rindex() - searching from the right
#   - Searching for substrings vs single characters
#   - What happens when the substring is NOT found
#   - How to use the result with slicing and indexing
#   - Real world use cases
#   - Common mistakes
# ============================================================


# ------------------------------------------------------------
# PART 1: The problem - finding things inside strings
# ------------------------------------------------------------

# So far we know HOW to access characters (indexing, slicing).
# But what if we don't KNOW the position we're looking for?
# What if we need to FIND something first?

# Example:
email = "anna.kowalska@university.edu"
# Where is the "@" symbol?
# We need to know its position to split username from domain.

# Without .find(), we'd have to check every character manually:
# email[0] == "@"?  No.
# email[1] == "@"?  No.
# ...
# email[13] == "@"? Yes!
# This is obviously terrible.

# With .find():
position = email.find("@")
print(position)     # 13  ← found at index 13!

# Now we can use this position:
username = email[:position]
domain   = email[position+1:]
print(username)     # anna.kowalska
print(domain)       # university.edu


# ------------------------------------------------------------
# PART 2: .find() - basic usage
# ------------------------------------------------------------

# .find() searches for a substring inside a string.
# It returns the INDEX of the FIRST occurrence.
# If not found, it returns -1.
#
# Syntax:
#   string.find(substring)
#   string.find(substring, start)
#   string.find(substring, start, end)

# ── Basic search ──
text = "Hello World Python"

print(text.find("World"))   # 6   ← "World" starts at index 6
print(text.find("Python"))  # 12  ← "Python" starts at index 12
print(text.find("Hello"))   # 0   ← "Hello" starts at index 0
print(text.find("o"))       # 4   ← FIRST "o" is at index 4

# ── Not found → returns -1 ──
print(text.find("Java"))    # -1  ← "Java" not in text
print(text.find("xyz"))     # -1

# -1 is a special return value meaning "not found"
# It is NOT a valid index to use for accessing characters
# (well, -1 IS a valid index in Python, but it would give
# you the LAST character, not the "not found" character!)

# ── Single character search ──
text = "Hello World"
print(text.find("o"))   # 4   ← first "o" (in "Hello")
print(text.find("l"))   # 2   ← first "l" (in "Hello")
print(text.find(" "))   # 5   ← the space character

# ── Substring search ──
text = "Python programming is fun"
print(text.find("pro"))     # 7   ← "pro" in "programming"
print(text.find("is"))      # 19  ← "is" starts at 19
print(text.find("gram"))    # 10  ← "gram" in "programming"


# ------------------------------------------------------------
# PART 3: .find() is case sensitive
# ------------------------------------------------------------

# Like all string methods, .find() is CASE SENSITIVE.

text = "Hello World"

print(text.find("hello"))   # -1  ← lowercase "hello" not found
print(text.find("Hello"))   # 0   ← uppercase "Hello" found!
print(text.find("WORLD"))   # -1  ← uppercase "WORLD" not found
print(text.find("World"))   # 6   ← "World" found!

# ── Case-insensitive search ──
# Convert both to the same case before searching:
text = "Hello World"
search = "hello"
position = text.lower().find(search.lower())
print(position)     # 0  ← found! (case-insensitive)

# But be careful: the position refers to the LOWERCASED version!
# For most purposes this is fine since lengths don't change.


# ------------------------------------------------------------
# PART 4: .find() with start parameter
# ------------------------------------------------------------

# .find(substring, start) begins searching from index 'start'.
# Everything before 'start' is ignored.

text = "Hello World Hello"
#       0123456789...

# Find "Hello" starting from the beginning:
print(text.find("Hello"))       # 0  ← first "Hello"

# Find "Hello" starting from index 1 (skip first character):
print(text.find("Hello", 1))    # 12 ← second "Hello"

# Find "Hello" starting from index 5:
print(text.find("Hello", 5))    # 12 ← second "Hello"

# Find "Hello" starting from index 13:
print(text.find("Hello", 13))   # -1 ← no "Hello" from index 13 onward

# ── Practical use: find the SECOND occurrence ──
text = "the cat sat on the mat"
first  = text.find("the")           # 0
second = text.find("the", first+1)  # 15  ← search after first occurrence
print(first)    # 0
print(second)   # 15

# ── Find occurrence after a specific marker ──
data = "name:Anna;age:25;city:Warsaw"
# Find ":" after position 5 (skipping the first colon):
second_colon = data.find(":", 5)
print(second_colon)     # 13  ← the colon before "25"


# ------------------------------------------------------------
# PART 5: .find() with start AND end parameters
# ------------------------------------------------------------

# .find(substring, start, end) searches ONLY within
# the slice string[start:end].
# The end index is EXCLUDED (same rule as slicing!).

text = "Hello World Python Hello"
#       0         1         2
#       0123456789012345678901234

# Search only within characters 0 to 10:
print(text.find("Hello", 0, 10))    # 0  ← found within [0:10]
print(text.find("Python", 0, 10))   # -1 ← "Python" not in [0:10]

# Search only within characters 5 to 20:
print(text.find("Hello", 5, 20))    # -1  ← no "Hello" between [5:20]
print(text.find("Python", 5, 20))   # 12  ← "Python" is within [5:20]

# Search within the last half of the string:
half = len(text) // 2
print(text.find("Hello", half))     # 19  ← second "Hello"

# ── Practical: search within a specific section ──
log = "2024-03-15 ERROR: file not found | 2024-03-16 INFO: started"
# Find "ERROR" only in the first 30 characters:
print(log.find("ERROR", 0, 30))     # 11  ← found in first section
# Find "INFO" only in the first 30 characters:
print(log.find("INFO", 0, 30))      # -1  ← not in first 30 chars


# ------------------------------------------------------------
# PART 6: .index() - same as .find() but raises an exception
# ------------------------------------------------------------

# .index() works EXACTLY like .find() with one key difference:
# When the substring is NOT found:
#   .find()  → returns -1      (silent failure)
#   .index() → raises ValueError (loud failure - crash!)
#
# Syntax:
#   string.index(substring)
#   string.index(substring, start)
#   string.index(substring, start, end)

# ── When substring IS found: identical behavior ──
text = "Hello World Python"

print(text.find("World"))   # 6
print(text.index("World"))  # 6  ← same result!

print(text.find("o"))       # 4
print(text.index("o"))      # 4  ← same result!

# ── When substring is NOT found: very different! ──
text = "Hello World"

result = text.find("Java")      # -1  ← no crash, returns -1
print(result)

# text.index("Java")
# ❌ ValueError: substring not found
# ← CRASH! Program stops here unless you handle it.


# ------------------------------------------------------------
# PART 7: .find() vs .index() - when to use which?
# ------------------------------------------------------------

# This is an important design decision.

# ── Use .find() when: ──
# You want to CHECK if something exists without crashing.
# The substring might or might not be there - both are valid.
# You handle the -1 case yourself.

email = "anna@university.edu"
at_position = email.find("@")
if at_position != -1:
    username = email[:at_position]
    domain   = email[at_position+1:]
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Invalid email: no @ symbol found!")

# ── Use .index() when: ──
# You are CERTAIN the substring must be there.
# If it's not found, it's a genuine error that should crash.
# You want Python to raise the error automatically.

# Example: parsing a required format
def parse_version(version_string):
    # Version MUST have a dot - if not, it's bad data
    dot_pos = version_string.index(".")  # crash if format wrong
    major = version_string[:dot_pos]
    minor = version_string[dot_pos+1:]
    return major, minor

# This design says: "I expect a dot. No dot = programming error."

# In practice:
# .find() is used MORE often because it's safer.
# .index() is used when the absence is truly unexpected.


# ------------------------------------------------------------
# PART 8: Checking existence with .find() - the -1 pattern
# ------------------------------------------------------------

# The standard pattern for checking if a substring exists:

text = "Python programming is fun"

# ── Method 1: use .find() and check for -1 ──
if text.find("programming") != -1:
    print("Found!")
else:
    print("Not found!")

# ── Method 2: use 'in' operator (simpler! - Lecture 18) ──
if "programming" in text:
    print("Found!")

# ── Method 3: use .find() result directly ──
position = text.find("programming")
if position >= 0:           # -1 means not found
    print(f"Found at position {position}")

# The 'in' operator is cleaner for just checking existence.
# Use .find() when you also NEED the position.

# ── Common mistake with -1 return value ──
text = "Hello World"
pos = text.find("xyz")  # returns -1
print(pos)              # -1

# ❌ DANGER: using -1 as an index!
print(text[pos])        # 'd'  ← gives LAST character! Not an error!
# This is a subtle bug: you wanted "not found" but got last char.

# ✅ Always check before using the result:
pos = text.find("xyz")
if pos != -1:
    print(text[pos])    # safe!
else:
    print("Not found")


# ------------------------------------------------------------
# PART 9: .rfind() - searching from the RIGHT
# ------------------------------------------------------------

# .rfind() is like .find() but searches from the RIGHT side.
# It returns the index of the LAST occurrence.
# If not found → returns -1 (same as .find()).

text = "Hello World Hello"
#       0         1
#       01234567890123456

# .find() → finds FIRST occurrence (from left):
print(text.find("Hello"))   # 0   ← first "Hello"

# .rfind() → finds LAST occurrence (from right):
print(text.rfind("Hello"))  # 12  ← last "Hello"

# ── When they give the same result ──
# Only one occurrence → same result:
text = "Hello World"
print(text.find("World"))   # 6
print(text.rfind("World"))  # 6  ← same! only one "World"

# ── .rfind() with single characters ──
text = "Hello World"
print(text.find("o"))       # 4   ← first "o" (in "Hello")
print(text.rfind("o"))      # 7   ← last "o" (in "World")

print(text.find("l"))       # 2   ← first "l"
print(text.rfind("l"))      # 9   ← last "l"

# ── Practical: get file extension with .rfind() ──
filename = "my.important.report.final.pdf"
dot_pos = filename.rfind(".")       # find the LAST dot
extension = filename[dot_pos+1:]    # everything after last dot
name_only = filename[:dot_pos]      # everything before last dot
print(extension)    # pdf
print(name_only)    # my.important.report.final

# Compare with .find():
first_dot = filename.find(".")
print(filename[first_dot+1:])   # important.report.final.pdf  ← wrong!
# .rfind() is the correct tool for file extensions!


# ------------------------------------------------------------
# PART 10: .rindex() - searching from the right, raises error
# ------------------------------------------------------------

# .rindex() is to .rfind() as .index() is to .find().
# Searches from the right, raises ValueError if not found.

text = "Hello World Hello"
print(text.rindex("Hello"))     # 12  ← last "Hello"
print(text.rfind("Hello"))      # 12  ← same result

# Not found:
# text.rindex("Java")   # ❌ ValueError: substring not found
result = text.rfind("Java")     # -1  ← no crash

# Same rule: use .rfind() for safe searching,
# use .rindex() when absence is an error.


# ------------------------------------------------------------
# PART 11: Using .find() results with slicing
# ------------------------------------------------------------

# The real power of .find() comes from using its result
# to perform precise slicing operations.

# ── Split at a found position ──
text = "name:Anna"
colon = text.find(":")
key   = text[:colon]        # "name"
value = text[colon+1:]      # "Anna"
print(key)      # name
print(value)    # Anna

# ── Extract content between markers ──
text = "Hello [World] Python"
start = text.find("[") + 1      # character AFTER "["
end   = text.find("]")          # character AT "]"
content = text[start:end]
print(content)  # World

# ── Extract content between quotes ──
text = 'He said "hello there" to me'
first_quote = text.find('"') + 1
second_quote = text.find('"', first_quote)   # find closing quote
quoted = text[first_quote:second_quote]
print(quoted)   # hello there

# ── Extract URL protocol ──
url = "https://www.example.com/path"
colon_pos = url.find(":")
protocol = url[:colon_pos]
print(protocol)     # https

# ── Find and replace (manual version) ──
text = "Hello World"
pos = text.find("World")
if pos != -1:
    replaced = text[:pos] + "Python" + text[pos + len("World"):]
    print(replaced)     # Hello Python
# (In practice, use .replace() for this - but good to understand!)

# ── Extract between two markers ──
html = "<title>Python Tutorial</title>"
open_tag_end   = html.find(">") + 1
close_tag_start = html.find("<", open_tag_end)
title = html[open_tag_end:close_tag_start]
print(title)    # Python Tutorial


# ------------------------------------------------------------
# PART 12: Finding all occurrences manually
# ------------------------------------------------------------

# .find() only returns ONE position at a time.
# To find ALL occurrences, you use .find() repeatedly
# with the start parameter. (Proper way uses loops - Module 04)

# Manual approach (for a known small number of occurrences):
text = "the cat sat on the mat near the fence"

first  = text.find("the")
second = text.find("the", first + 1)
third  = text.find("the", second + 1)
fourth = text.find("the", third + 1)   # -1 if no fourth occurrence

print(first)    # 0
print(second)   # 15
print(third)    # 27
print(fourth)   # -1  ← no fourth occurrence!

# Count occurrences using .count() (next lecture!)
# For now: keep calling .find() with updated start

# ── Manual "find all" with known count ──
sentence = "I like Python and Python is great and Python rocks"
pos1 = sentence.find("Python")
pos2 = sentence.find("Python", pos1 + 1)
pos3 = sentence.find("Python", pos2 + 1)
pos4 = sentence.find("Python", pos3 + 1)

print(f"Python at: {pos1}, {pos2}, {pos3}")  # 7, 18, 38
print(f"Fourth: {pos4}")                     # -1


# ------------------------------------------------------------
# PART 13: .find() on specific sections using start/end
# ------------------------------------------------------------

# The start and end parameters make .find() very precise.

# ── Search within a "window" of the string ──
text = "ATGCCCATGAAATG"
#       01234567890123

# Find "ATG" in the full string:
print(text.find("ATG"))             # 0  ← first ATG

# Find "ATG" starting from position 1:
print(text.find("ATG", 1))         # 6  ← second ATG

# Find "ATG" starting from position 7:
print(text.find("ATG", 7))         # 12 ← third ATG

# Find "ATG" starting from position 13:
print(text.find("ATG", 13))        # -1 ← no more ATG after position 13

# Find "ATG" only in positions 0-9:
print(text.find("ATG", 0, 9))      # 0  ← first ATG is within [0:9]
print(text.find("ATG", 1, 9))      # 6  ← second ATG is within [1:9]

# ── Verify substring at specific position ──
# "Does 'ATG' appear at position 6?"
pos = 6
if text.find("ATG", pos, pos + 3) == pos:
    print(f"ATG found at position {pos}")   # yes!
else:
    print(f"ATG not at position {pos}")


# ------------------------------------------------------------
# PART 14: Real world applications
# ------------------------------------------------------------

# ── Application 1: Parse email ──
email = "anna.kowalska@university.edu"
at = email.find("@")
if at != -1:
    username = email[:at]
    domain = email[at+1:]
    dot_in_domain = domain.find(".")
    domain_name = domain[:dot_in_domain]
    tld = domain[dot_in_domain+1:]
    print(f"Username: {username}")      # anna.kowalska
    print(f"Domain: {domain}")          # university.edu
    print(f"Domain name: {domain_name}")# university
    print(f"TLD: {tld}")               # edu

# ── Application 2: Parse key-value pair ──
config = "max_retries = 5"
eq_pos = config.find("=")
key   = config[:eq_pos].strip()
value = config[eq_pos+1:].strip()
print(f"Key: '{key}', Value: '{value}'")    # Key: 'max_retries', Value: '5'

# ── Application 3: Find file extension ──
filename = "genome_assembly.final.fasta"
last_dot = filename.rfind(".")
name = filename[:last_dot]
ext  = filename[last_dot+1:]
print(f"Name: {name}")      # genome_assembly.final
print(f"Ext: {ext}")        # fasta

# ── Application 4: Extract HTML tag content ──
html_tag = "<h1>Introduction to Python</h1>"
open_end  = html_tag.find(">") + 1
close_start = html_tag.rfind("<")
content = html_tag[open_end:close_start]
print(content)  # Introduction to Python

# ── Application 5: Find restriction site in DNA ──
dna = "ATGCCCGAATTCGCATTAGAATTCG"
ecori = "GAATTC"
pos1 = dna.find(ecori)
pos2 = dna.find(ecori, pos1 + 1)
print(f"EcoRI site 1 at position: {pos1}")  # 6
print(f"EcoRI site 2 at position: {pos2}")  # 18

# ── Application 6: Validate format ──
phone = "48-502-111-222"
# Check it has exactly 3 dashes:
first_dash  = phone.find("-")
second_dash = phone.find("-", first_dash + 1)
third_dash  = phone.find("-", second_dash + 1)
fourth_dash = phone.find("-", third_dash + 1)

if first_dash != -1 and second_dash != -1 and \
   third_dash != -1 and fourth_dash == -1:
    print("Valid phone format")
else:
    print("Invalid phone format")

# ── Application 7: Extract content between parentheses ──
text = "function(argument1, argument2)"
open_paren  = text.find("(") + 1
close_paren = text.find(")")
args = text[open_paren:close_paren]
print(args)     # argument1, argument2

# ── Application 8: Find position for insertion ──
sentence = "I Python programming"
# Where to insert "love " (after "I "):
insert_pos = sentence.find("Python")
new_sentence = sentence[:insert_pos] + "love " + sentence[insert_pos:]
print(new_sentence)     # I love Python programming


# ------------------------------------------------------------
# PART 15: Summary table - all four methods
# ------------------------------------------------------------

# ┌──────────────┬───────────────┬──────────────┬───────────────┐
# │ Method       │ Direction     │ Not found    │ Use when      │
# ├──────────────┼───────────────┼──────────────┼───────────────┤
# │ .find()      │ Left → Right  │ Returns -1   │ Safe search   │
# │ .index()     │ Left → Right  │ ValueError   │ Must exist    │
# │ .rfind()     │ Right → Left  │ Returns -1   │ Safe, last    │
# │ .rindex()    │ Right → Left  │ ValueError   │ Must exist    │
# └──────────────┴───────────────┴──────────────┴───────────────┘

text = "Hello World Hello"

print(text.find("Hello"))       # 0   ← first, from left
print(text.index("Hello"))      # 0   ← same, but crashes if missing
print(text.rfind("Hello"))      # 12  ← last, from right
print(text.rindex("Hello"))     # 12  ← same, but crashes if missing

print(text.find("Java"))        # -1  ← not found, no crash
# text.index("Java")            # ❌ ValueError
print(text.rfind("Java"))       # -1  ← not found, no crash
# text.rindex("Java")           # ❌ ValueError


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ .find(sub)           → index of FIRST occurrence, -1 if not found
# ✅ .find(sub, start)    → search from 'start' onward
# ✅ .find(sub, start, end) → search within [start:end]
# ✅ .index(sub)          → same as .find() but raises ValueError if missing
# ✅ .rfind(sub)          → index of LAST occurrence, -1 if not found
# ✅ .rindex(sub)         → same as .rfind() but raises ValueError if missing
# ✅ All four are CASE SENSITIVE
# ✅ All four work on substrings of any length
# ✅ .find() is safer (returns -1), .index() is stricter (crashes)
# ✅ Always check result != -1 before using as index!
# ✅ Using -1 as index = LAST CHARACTER (silent bug!)
# ✅ Combine with slicing to extract content around found position
# ✅ Use 'in' operator if you only need to check existence (not position)
# ✅ .rfind() is essential for getting file extensions correctly