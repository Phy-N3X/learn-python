# ============================================================
# MODULE 02 | LECTURE 24 - .count()
# ============================================================
# What you will learn:
#   - What .count() does and how to use it
#   - Counting single characters
#   - Counting substrings (multiple characters)
#   - The start and end parameters
#   - Case sensitivity
#   - What .count() returns for non-existent substrings
#   - How .count() handles overlapping patterns
#   - Combining .count() with other methods
#   - Real world use cases
#   - Common mistakes
# ============================================================


# ------------------------------------------------------------
# PART 1: What is .count()?
# ------------------------------------------------------------

# .count() counts how many times a substring appears
# inside a string.
#
# Syntax:
#   string.count(substring)
#   string.count(substring, start)
#   string.count(substring, start, end)
#
# Returns: an INTEGER (0 or more)
# Never raises an error - if nothing found, returns 0.

# Basic examples:
text = "hello world hello python hello"
print(text.count("hello"))      # 3  ← "hello" appears 3 times
print(text.count("world"))      # 1  ← "world" appears once
print(text.count("java"))       # 0  ← "java" not found, returns 0!
print(text.count("l"))          # 7  ← letter "l" appears 7 times
print(text.count("o"))          # 4  ← letter "o" appears 4 times

# The return value is always an integer ≥ 0
result = text.count("hello")
print(type(result))     # <class 'int'>
print(result)           # 3


# ------------------------------------------------------------
# PART 2: Counting single characters
# ------------------------------------------------------------

# .count() works perfectly for counting individual characters.
# This is very useful for analysis and validation.

# ── Count specific letters ──
word = "mississippi"
print(word.count("s"))      # 4  ← four 's' characters
print(word.count("p"))      # 2  ← two 'p' characters
print(word.count("i"))      # 4  ← four 'i' characters
print(word.count("m"))      # 1  ← one 'm' character
print(word.count("z"))      # 0  ← zero 'z' characters

# ── Count vowels (separately) ──
text = "Python programming"
print(text.count("a"))      # 1
print(text.count("e"))      # 0
print(text.count("i"))      # 1
print(text.count("o"))      # 2
print(text.count("u"))      # 0
# Total vowels = 1 + 0 + 1 + 2 + 0 = 4

# ── Count spaces ──
sentence = "Hello World Python is great"
spaces = sentence.count(" ")
print(spaces)       # 4  ← 4 spaces = 5 words (approximately)
word_count = spaces + 1
print(word_count)   # 5  ← simple word count (works if no extra spaces)

# ── Count digits in a string ──
data = "Phone: 48-502-111-222, Code: 1234"
print(data.count("1"))      # 3
print(data.count("2"))      # 4
print(data.count("-"))      # 3


# ------------------------------------------------------------
# PART 3: Counting substrings (multiple characters)
# ------------------------------------------------------------

# .count() is not limited to single characters.
# It counts any substring of any length.

# ── Count words ──
text = "the cat sat on the mat and the cat slept"
print(text.count("the"))    # 3  ← "the" appears 3 times
print(text.count("cat"))    # 2  ← "cat" appears 2 times
print(text.count("sat"))    # 1
print(text.count("dog"))    # 0

# ── Count multi-character patterns ──
dna = "ATGATGATGCCCATG"
print(dna.count("ATG"))     # 4  ← start codon appears 4 times
print(dna.count("CCC"))     # 1
print(dna.count("TGA"))     # 0

# ── Count a phrase ──
text = "I love Python. I really love Python. Python is great."
print(text.count("Python"))         # 3
print(text.count("love Python"))    # 2  ← only "love Python" together
print(text.count("I love"))         # 2
print(text.count("great"))          # 1

# ── Count separators in structured data ──
csv = "Anna,Kowalska,25,Warsaw,Poland"
commas = csv.count(",")
print(commas)               # 4  ← 4 commas = 5 fields
fields = commas + 1
print(fields)               # 5

path = "/home/user/documents/file.txt"
slashes = path.count("/")
print(slashes)              # 4  ← 4 slashes = 4 directory levels + root


# ------------------------------------------------------------
# PART 4: .count() is case sensitive
# ------------------------------------------------------------

# Like all string methods, .count() is case sensitive.
# Uppercase and lowercase are counted separately.

text = "Python python PYTHON PyThOn"

print(text.count("Python"))     # 1  ← only exact "Python"
print(text.count("python"))     # 1  ← only exact "python"
print(text.count("PYTHON"))     # 1  ← only exact "PYTHON"
print(text.count("PyThOn"))     # 1  ← only exact "PyThOn"

# ── Case-insensitive counting ──
# Convert to one case first, then count:
text = "Python python PYTHON PyThOn"
total = text.lower().count("python")
print(total)        # 4  ← all variants counted!

# Or uppercase:
total = text.upper().count("PYTHON")
print(total)        # 4  ← same result

# ── When case matters ──
dna = "ATGatgATGAtg"
print(dna.count("ATG"))         # 2  ← only uppercase ATG
print(dna.count("atg"))         # 2  ← only lowercase atg
print(dna.upper().count("ATG")) # 4  ← all variants

# ── Counting specific case patterns ──
text = "Hello World HELLO world HeLLo"
print(text.count("Hello"))      # 1  ← only "Hello" (H upper, rest lower)
print(text.count("HELLO"))      # 1  ← only "HELLO" (all upper)
print(text.count("hello"))      # 0  ← no all-lowercase "hello"


# ------------------------------------------------------------
# PART 5: The start parameter
# ------------------------------------------------------------

# .count(substring, start) counts occurrences
# starting from index 'start'.
# Everything before 'start' is ignored.

text = "the cat sat on the mat and the cat"
#       0         1         2         3
#       0123456789012345678901234567890123

# Count "the" in full string:
print(text.count("the"))            # 3

# Count "the" starting from position 5:
print(text.count("the", 5))         # 2  ← skips first "the" at index 0

# Count "the" starting from position 18:
print(text.count("the", 18))        # 1  ← only last "the"

# Count "the" starting from position 30:
print(text.count("the", 30))        # 0  ← no "the" after position 30

# ── Practical use: count in second half of string ──
text = "Python is great and Python is powerful"
half = len(text) // 2
first_half_count  = text.count("Python", 0, half)
second_half_count = text.count("Python", half)
print(f"First half:  {first_half_count}")   # 1
print(f"Second half: {second_half_count}")  # 1


# ------------------------------------------------------------
# PART 6: The start AND end parameters
# ------------------------------------------------------------

# .count(substring, start, end) counts only within
# the slice string[start:end].
# The end is EXCLUDED (same rule as slicing!).

text = "abcabcabcabc"
#       012345678901

# Count "abc" in full string:
print(text.count("abc"))            # 4

# Count "abc" in first 6 characters [0:6]:
print(text.count("abc", 0, 6))     # 2  ← "abcabc"

# Count "abc" in characters [3:9]:
print(text.count("abc", 3, 9))     # 2  ← "abcabc"

# Count "abc" in characters [1:7]:
print(text.count("abc", 1, 7))     # 1  ← "bcabca" → only one complete "abc"

# Count "abc" in characters [0:3]:
print(text.count("abc", 0, 3))     # 1  ← "abc" exactly

# Count "abc" in characters [0:2]:
print(text.count("abc", 0, 2))     # 0  ← "ab" → no complete "abc"

# ── Real use case: count in a specific section ──
log = "ERROR: disk full | WARNING: low memory | ERROR: permission denied"
# Count errors in the full log:
print(log.count("ERROR"))          # 2

# Count only in first half:
half = len(log) // 2
print(log.count("ERROR", 0, half)) # 1  ← only first ERROR in first half


# ------------------------------------------------------------
# PART 7: Non-overlapping counting - a critical detail!
# ------------------------------------------------------------

# .count() counts NON-OVERLAPPING occurrences.
# This matters when the substring could overlap with itself.

# ── Simple case: no overlap possible ──
text = "abcabcabc"
print(text.count("abc"))    # 3  ← three non-overlapping "abc"

# ── Overlapping case: .count() does NOT count overlaps ──
text = "aaaa"
print(text.count("aa"))     # 2  ← NOT 3!
# Why 2 and not 3?
# Python finds "aa" at index 0 → counts it
# Then continues from index 2 (after the found "aa")
# Finds "aa" at index 2 → counts it
# Then continues from index 4 → end of string
# Total: 2
#
# The overlapping "aa" at index 1 is NOT counted!
# "aaaa"
#  ↑↑   → first match (index 0-1)
#    ↑↑ → second match (index 2-3)
#   ↑↑  → this overlap at index 1-2 is IGNORED

# More examples:
print("aaa".count("aa"))    # 1  ← finds at 0, next start at 2, too short
print("aaaa".count("aa"))   # 2
print("aaaaa".count("aa"))  # 2  ← finds at 0 and 2, index 4 is too short

text = "abababab"
print(text.count("ab"))     # 4  ← no overlap issue with "ab"
print(text.count("aba"))    # 2  ← "aba" at 0 and 4 (not 2 because overlap)
# "abababab"
#  ↑↑↑       → first "aba" at index 0
#     ↑↑↑    → skips index 1 (overlap!), finds "aba" at index 2... wait
# Let's verify:
print("abababab".count("aba"))  # 2
# indices: 0-2 → "aba" ✓
# next start: 3
# indices: 3-5 → "bab" ✗
# indices: 4-6 → would be "aba" but starts at 3 not 4...
# actually let me retrace: after finding at 0, next try is index 3
# index 3: "bab" ✗, index 4: "aba" ✓, total: 2... let's just verify:

# The key rule: after finding a match, the next search
# starts AFTER the end of the found match (non-overlapping).


# ------------------------------------------------------------
# PART 8: Counting empty string ""
# ------------------------------------------------------------

# Counting an empty string is a special edge case.
# .count("") returns len(string) + 1
# (one "empty" between each character, plus one at each end)

text = "abc"
print(text.count(""))   # 4
# Positions: before 'a', between 'a' and 'b',
#            between 'b' and 'c', after 'c' = 4 positions

print("".count(""))     # 1  ← empty string has one empty position
print("a".count(""))    # 2  ← before and after 'a'
print("ab".count(""))   # 3

# This is rarely useful in practice but good to know.
# It follows the same logic as "".join() inserting between characters.


# ------------------------------------------------------------
# PART 9: .count() returns 0 for not-found, NEVER -1
# ------------------------------------------------------------

# Unlike .find() which returns -1 when not found,
# .count() ALWAYS returns 0 or a positive integer.
# It NEVER returns -1!

text = "Hello World"
print(text.count("xyz"))    # 0  ← not found → 0 (not -1!)
print(text.count("Java"))   # 0
print(text.count("z"))      # 0

# This means you can use .count() directly in conditions:
if text.count("World") > 0:
    print("World is in the text!")

# Even simpler: use 'in' operator for existence check:
if "World" in text:
    print("World is in the text!")

# Use .count() when you need THE NUMBER, not just existence.
# Use 'in' when you just need to know if it's there.


# ------------------------------------------------------------
# PART 10: Combining .count() with other methods
# ------------------------------------------------------------

# .count() is often combined with other string methods
# for powerful text analysis.

# ── Count words (basic) ──
sentence = "The quick brown fox jumps over the lazy dog"
word_count = len(sentence.split())
print(word_count)           # 9

# ── Count specific word (case-insensitive) ──
text = "Python python PYTHON PyThOn"
count = text.lower().count("python")
print(count)                # 4

# ── Count after stripping ──
text = "   hello hello hello   "
count = text.strip().count("hello")
print(count)                # 3

# ── Count and validate ──
email = "anna@university.edu"
at_count = email.count("@")
if at_count == 1:
    print("Valid: exactly one @ symbol")
elif at_count == 0:
    print("Invalid: no @ symbol")
else:
    print("Invalid: multiple @ symbols")

# ── Count and calculate percentage ──
dna = "ATGCCCGCATTAGTCGA"
total = len(dna)
a_count = dna.count("A")
t_count = dna.count("T")
g_count = dna.count("G")
c_count = dna.count("C")

print(f"A: {a_count} ({a_count/total*100:.1f}%)")
print(f"T: {t_count} ({t_count/total*100:.1f}%)")
print(f"G: {g_count} ({g_count/total*100:.1f}%)")
print(f"C: {c_count} ({c_count/total*100:.1f}%)")
print(f"Total: {a_count + t_count + g_count + c_count}")
print(f"Verified: {a_count + t_count + g_count + c_count == total}")

# ── Count punctuation ──
text = "Hello, World! How are you? I'm fine, thank you."
commas     = text.count(",")
periods    = text.count(".")
excl_marks = text.count("!")
quest_marks = text.count("?")
apostrophes = text.count("'")

print(f"Commas: {commas}")          # 2
print(f"Periods: {periods}")        # 1
print(f"Exclamation: {excl_marks}") # 1
print(f"Questions: {quest_marks}")  # 1
print(f"Apostrophes: {apostrophes}")# 1


# ------------------------------------------------------------
# PART 11: .count() for validation and quality checks
# ------------------------------------------------------------

# .count() is excellent for validating string format.

# ── Validate password complexity ──
password = "MyPass123!"
upper_count = sum(1 for c in password if c.isupper())  # preview
lower_count = sum(1 for c in password if c.islower())  # preview
# Manual count for specific characters:
has_digit  = (password.count("0") + password.count("1") +
              password.count("2") + password.count("3") +
              password.count("4") + password.count("5") +
              password.count("6") + password.count("7") +
              password.count("8") + password.count("9"))
print(f"Digits: {has_digit}")   # 3

# ── Validate email format (basic) ~~
def is_valid_email_format(email):
    at_count  = email.count("@")
    dot_count = email.count(".")
    return at_count == 1 and dot_count >= 1

print(is_valid_email_format("anna@email.com"))      # True
print(is_valid_email_format("annaemailcom"))         # False
print(is_valid_email_format("anna@@email.com"))      # False

# ── Check balanced brackets (simple case) ──
text = "Hello (World (Python))"
open_count  = text.count("(")
close_count = text.count(")")
if open_count == close_count:
    print("Brackets are balanced!")
else:
    print(f"Unbalanced! ( = {open_count}, ) = {close_count}")

# ── Count fields in CSV ──
csv_header = "name,age,city,country,email,score"
field_count = csv_header.count(",") + 1
print(f"Number of fields: {field_count}")   # 6

# ── Validate DNA sequence ──
sequence = "ATGCCCGCA"
valid_nucleotides = (sequence.count("A") +
                     sequence.count("T") +
                     sequence.count("G") +
                     sequence.count("C"))
is_valid = valid_nucleotides == len(sequence)
print(f"Valid DNA: {is_valid}")     # True


# ------------------------------------------------------------
# PART 12: .count() vs .find() vs 'in' - choosing the right tool
# ------------------------------------------------------------

# Three tools for searching strings. Which to use?

text = "Python is great and Python is fun"

# ── 'in' operator: JUST checking existence (True/False) ──
print("Python" in text)         # True  ← simplest, most readable

# ── .find(): need the POSITION ──
pos = text.find("Python")
print(pos)                      # 0  ← first occurrence position

# ── .count(): need the QUANTITY ──
qty = text.count("Python")
print(qty)                      # 2  ← how many times it appears

# Decision guide:
# "Does X exist in the string?"          → use 'in'
# "Where is X in the string?"            → use .find()
# "How many times does X appear?"        → use .count()
# "Where is the last X in the string?"   → use .rfind()

# ── Combining all three ~~
word = "Python"
if word in text:                        # exists?
    pos = text.find(word)               # where?
    qty = text.count(word)              # how many?
    print(f"'{word}' found {qty} time(s), first at position {pos}")
else:
    print(f"'{word}' not found")


# ------------------------------------------------------------
# PART 13: Real world applications
# ------------------------------------------------------------

# ── Application 1: GC content of DNA ──
# GC content = percentage of G and C nucleotides
# Important metric in bioinformatics!

dna = "ATGCCCGCATTAGTCGAAATGCCC"
g_count = dna.count("G")
c_count = dna.count("C")
gc_content = (g_count + c_count) / len(dna) * 100
print(f"GC content: {gc_content:.1f}%")    # GC content: 50.0%

# ── Application 2: Word frequency analysis ──
text = "to be or not to be that is the question"
words_to_count = ["to", "be", "or", "not", "the"]
for word in words_to_count:
    count = text.count(word)
    print(f"'{word}': {count} time(s)")

# ── Application 3: Count sentences ~~
paragraph = "Python is great. I love coding. Do you code? Yes, I do!"
sentences = (paragraph.count(".") +
             paragraph.count("!") +
             paragraph.count("?"))
print(f"Approximate sentence count: {sentences}")   # 4

# ── Application 4: Validate IP address format ~~
ip = "192.168.1.100"
dots = ip.count(".")
if dots == 3:
    print("Correct number of dots for IPv4")
else:
    print(f"Wrong number of dots: {dots} (expected 3)")

# ── Application 5: Count code lines ~~
code = """def hello():
    print("Hello")
    return True

def world():
    print("World")
"""
line_count = code.count("\n")
print(f"Lines: {line_count}")   # 7

# ── Application 6: Count HTML tags ~~
html = "<p>Hello</p><p>World</p><p>Python</p>"
open_tags  = html.count("<p>")
close_tags = html.count("</p>")
print(f"Open tags: {open_tags}")    # 3
print(f"Close tags: {close_tags}")  # 3
print(f"Balanced: {open_tags == close_tags}")  # True

# ── Application 7: Count restriction sites ~~
dna = "ATGCCCGAATTCGCATTAGAATTCGTCGAAAGCTTCGA"
ecori_count   = dna.count("GAATTC")
hindiii_count = dna.count("AAGCTT")
print(f"EcoRI sites:   {ecori_count}")    # 2
print(f"HindIII sites: {hindiii_count}")  # 1

# ── Application 8: Analyze text composition ~~
text = "Hello, World! 123"
letters = sum(text.count(c) for c in "abcdefghijklmnopqrstuvwxyz"
              + "ABCDEFGHIJKLMNOPQRSTUVWXYZ")
digits  = sum(text.count(c) for c in "0123456789")
spaces  = text.count(" ")
other   = len(text) - letters - digits - spaces

print(f"Letters: {letters}")    # 10
print(f"Digits:  {digits}")     # 3
print(f"Spaces:  {spaces}")     # 2
print(f"Other:   {other}")      # 2 (comma and exclamation mark)
print(f"Total:   {len(text)}")  # 17


# ------------------------------------------------------------
# PART 14: Mathematical relationship with other methods
# ------------------------------------------------------------

# .count() has interesting relationships with other methods.

text = "hello world hello python hello"

# ── Relationship with .split() ~~
# For single-space separated text:
# word_count via split:
words = text.split()
print(len(words))           # 5  ← five words

# word_count via count (less accurate for complex whitespace):
spaces = text.count(" ")
print(spaces + 1)           # 5  ← also five (works here)

# ── Relationship with .replace() ~~
# Replacing a substring shrinks the string by:
# count * len(old) - count * len(new)
old = "hello"
new = "hi"
count = text.count(old)
expected_new_len = len(text) - count * (len(old) - len(new))
new_text = text.replace(old, new)
print(len(new_text))                # verify
print(expected_new_len)             # should match!
print(len(new_text) == expected_new_len)  # True

# ── Relationship with .find() ~~
# If count is 0, then find returns -1:
sub = "java"
print(text.count(sub) == 0)     # True
print(text.find(sub) == -1)     # True  ← consistent!

# If count > 0, then find returns a valid index:
sub = "hello"
print(text.count(sub) > 0)         # True
print(text.find(sub) >= 0)         # True  ← consistent!


# ------------------------------------------------------------
# PART 15: Common mistakes with .count()
# ------------------------------------------------------------

# ── Mistake 1: Confusing .count() with .find() ~~
text = "Hello World"
# .count() returns HOW MANY (a count/quantity)
# .find()  returns WHERE    (a position/index)

print(text.count("World"))  # 1  ← one occurrence
print(text.find("World"))   # 6  ← found at index 6
# Very different meanings!

# ── Mistake 2: Forgetting case sensitivity ~~
text = "Python python PYTHON"
print(text.count("python"))         # 1  ← only lowercase!
print(text.lower().count("python")) # 3  ← all variants

# ── Mistake 3: Expecting -1 when not found ~~
text = "Hello"
result = text.count("xyz")
print(result)           # 0  ← NOT -1! Returns 0!
# ❌ Wrong check:
if result == -1:        # this will NEVER be true for .count()!
    print("Not found")
# ✅ Correct check:
if result == 0:
    print("Not found")

# ── Mistake 4: Not accounting for overlaps ~~
text = "aaaa"
print(text.count("aa"))     # 2  ← NOT 3!
# Some beginners expect 3 because:
# "aa" at 0, "aa" at 1, "aa" at 2
# But .count() is NON-OVERLAPPING:
# "aa" at 0 consumed, next search starts at 2
# "aa" at 2 consumed, next search starts at 4 → end

# ── Mistake 5: Using .count() when 'in' is cleaner ~~
text = "Hello World"
# ❌ Verbose:
if text.count("World") > 0:
    print("Found!")
# ✅ Cleaner:
if "World" in text:
    print("Found!")
# Use .count() only when you need the NUMBER, not just existence.


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ .count(sub)           → counts non-overlapping occurrences
# ✅ .count(sub, start)    → count from 'start' onward
# ✅ .count(sub, start, end) → count within [start:end]
# ✅ Returns INTEGER ≥ 0, NEVER returns -1!
# ✅ Not found → returns 0 (not -1!)
# ✅ Case sensitive: "Python" ≠ "python"
# ✅ For case-insensitive: use .lower().count() or .upper().count()
# ✅ NON-OVERLAPPING: after match, search continues past the match
# ✅ .count("") → len(string) + 1 (edge case, rarely useful)
# ✅ Works for single chars AND multi-char substrings
# ✅ Never raises an error (even for empty string or not-found)
# ✅ Use 'in' for existence, .find() for position, .count() for quantity
# ✅ GC content, word frequency, validation → classic .count() uses