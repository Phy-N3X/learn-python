# ============================================================
# MODULE 02 | LECTURE 20 - .replace()
# ============================================================
# What you will learn:
#   - What .replace() does and how to use it
#   - The full syntax: .replace(old, new, count)
#   - How .replace() handles multiple occurrences
#   - The optional 'count' parameter
#   - Case sensitivity of .replace()
#   - Replacing with an empty string (deletion)
#   - Chaining multiple .replace() calls
#   - What .replace() does NOT do (regex, patterns)
#   - Real world use cases
#   - Common mistakes and misconceptions
# ============================================================


# ------------------------------------------------------------
# PART 1: What is .replace()?
# ------------------------------------------------------------

# .replace() is a string method that finds a substring
# and replaces it with another substring.
#
# It answers the question:
# "Find THIS in my string, and swap it for THAT."
#
# Syntax:
#   string.replace(old, new)
#   string.replace(old, new, count)
#
#   old   = the substring you want to FIND
#   new   = the substring you want to PUT IN ITS PLACE
#   count = (optional) how many replacements to make
#
# It returns a NEW string with the replacements done.
# The original string is NEVER modified (immutable!).

sentence = "I love cats"
result = sentence.replace("cats", "dogs")
print(result)       # I love dogs
print(sentence)     # I love cats  ← original unchanged!

# The simplest case: replace one word with another
text = "Hello World"
print(text.replace("World", "Python"))  # Hello Python


# ------------------------------------------------------------
# PART 2: .replace() replaces ALL occurrences by default
# ------------------------------------------------------------

# If the 'old' substring appears multiple times,
# .replace() replaces ALL of them by default.

sentence = "the cat sat on the mat near the cat"
result = sentence.replace("cat", "dog")
print(result)
# the dog sat on the mat near the dog
# ↑ both "cat" occurrences were replaced!

# Another example:
text = "banana"
print(text.replace("a", "o"))   # bonono
# All three 'a' characters replaced with 'o'

# And another:
text = "aabbaacc"
print(text.replace("a", "x"))   # xxbbxxcc
# All four 'a' characters replaced

# This behavior is different from some other languages
# where you might replace only the first occurrence.
# In Python: no count argument = replace ALL.


# ------------------------------------------------------------
# PART 3: The optional 'count' parameter
# ------------------------------------------------------------

# If you want to limit how many replacements are made,
# use the third argument: count.
#
# .replace(old, new, count)
# → replaces only the FIRST 'count' occurrences

sentence = "the cat sat on the mat near the cat"

# Replace only the first occurrence:
result = sentence.replace("the", "a", 1)
print(result)
# a cat sat on the mat near the cat
# ↑ only the first "the" was replaced!

# Replace only the first 2 occurrences:
result = sentence.replace("the", "a", 2)
print(result)
# a cat sat on a mat near the cat
# ↑ first two "the" replaced, third one unchanged

# Replace all (no count = default behavior):
result = sentence.replace("the", "a")
print(result)
# a cat sat on a mat near a cat
# ↑ all three "the" replaced

# count = 0 → no replacements made:
result = sentence.replace("the", "a", 0)
print(result)
# the cat sat on the mat near the cat  ← unchanged!

# count larger than occurrences → just replaces all that exist:
result = sentence.replace("cat", "dog", 999)
print(result)
# the dog sat on the mat near the dog  ← both replaced, no error


# ------------------------------------------------------------
# PART 4: Case sensitivity
# ------------------------------------------------------------

# .replace() is CASE SENSITIVE.
# "cat" and "Cat" and "CAT" are treated as different substrings!

text = "Cat cat CAT"

print(text.replace("cat", "dog"))   # Cat dog CAT
#                   ↑ only lowercase "cat" replaced!

print(text.replace("Cat", "dog"))   # dog cat CAT
#                   ↑ only "Cat" (capital C) replaced!

print(text.replace("CAT", "dog"))   # Cat cat dog
#                   ↑ only "CAT" (all caps) replaced!

# ── How to do case-insensitive replacement ──
# Python's .replace() cannot do this directly.
# The workaround: convert to one case, then replace.
# But this changes the case of the whole string.

# ✅ Workaround (if you don't care about preserving case):
text = "Cat cat CAT"
result = text.lower().replace("cat", "dog")
print(result)       # dog dog dog  ← all lowercase now

# For true case-insensitive replacement preserving case,
# you need the 're' module (regular expressions - advanced topic).
# For now, just remember: .replace() is case-sensitive!


# ------------------------------------------------------------
# PART 5: Replacing with an empty string (deletion)
# ------------------------------------------------------------

# A very powerful use of .replace():
# Replace something with "" (empty string) = DELETE it!
#
# .replace("something", "")  ← removes "something" entirely

# Remove all spaces:
text = "Hello World Python"
print(text.replace(" ", ""))    # HelloWorldPython

# Remove all vowels:
word = "Hello World"
result = word.replace("a", "")
result = result.replace("e", "")
result = result.replace("i", "")
result = result.replace("o", "")
result = result.replace("u", "")
print(result)       # Hll Wrld

# Remove punctuation:
sentence = "Hello, World! How are you?"
result = sentence.replace(",", "")
result = result.replace("!", "")
result = result.replace("?", "")
print(result)       # Hello World How are you

# Remove a specific word:
text = "I really really love Python"
print(text.replace("really ", ""))  # I love Python
# ↑ note: include the space after "really" to avoid double space


# ------------------------------------------------------------
# PART 6: Replacing substrings, not just single characters
# ------------------------------------------------------------

# .replace() works on ANY substring, not just single characters.
# The 'old' and 'new' can be words, phrases, or any string.

# ── Replace a word ──
text = "I love Java programming"
print(text.replace("Java", "Python"))   # I love Python programming

# ── Replace a phrase ──
text = "Good morning, how are you?"
print(text.replace("Good morning", "Good evening"))
# Good evening, how are you?

# ── Replace multiple characters at once ──
text = "Hello\nWorld\nPython"    # newlines between words
print(text.replace("\n", " "))   # Hello World Python  ← newlines → spaces

# ── Replace tab with spaces ──
text = "Name\tAge\tCity"
print(text.replace("\t", "    "))   # Name    Age    City

# ── Replace a longer string with a shorter one ──
text = "I do not like Mondays"
print(text.replace("do not like", "love"))  # I love Mondays

# ── Replace with something longer ──
text = "Python"
print(text.replace("P", "www.P"))   # www.Python


# ------------------------------------------------------------
# PART 7: What happens when 'old' is not found
# ------------------------------------------------------------

# If the substring you're looking for doesn't exist,
# .replace() simply returns the original string unchanged.
# NO error is raised!

text = "Hello World"
result = text.replace("Python", "Java")
print(result)       # Hello World  ← unchanged, no error!
print(text == result)   # True  ← identical strings

# This is safe behavior - you don't need to check
# if the substring exists before calling .replace().

# Compare with indexing (which DOES raise an error):
# text[100]  # ← IndexError!
# text.replace("xyz", "abc")  # ← no error, returns original


# ------------------------------------------------------------
# PART 8: Replacing with the same string
# ------------------------------------------------------------

# Replacing 'old' with 'old' itself → string unchanged.
# This seems useless, but it's worth understanding.

text = "Hello World"
result = text.replace("Hello", "Hello")
print(result)           # Hello World
print(text == result)   # True  ← identical content

# This can happen accidentally in code.
# If you see this, it's probably a logic error.


# ------------------------------------------------------------
# PART 9: Chaining multiple .replace() calls
# ------------------------------------------------------------

# Since .replace() returns a new string,
# you can chain multiple calls one after another.
# Each replacement is applied to the result of the previous one.

# ── Clean up multiple characters ──
text = "Hello, World! How are you?"
clean = text.replace(",", "").replace("!", "").replace("?", "")
print(clean)        # Hello World How are you

# ── Replace multiple words ──
text = "I love cats and cats love me"
result = text.replace("cats", "dogs").replace("love", "adore")
print(result)       # I adore dogs and dogs adore me

# ── Normalize different types of whitespace ──
messy = "Hello\tWorld\nPython"
normalized = messy.replace("\t", " ").replace("\n", " ")
print(normalized)   # Hello World Python

# ── Convert between naming conventions ──
snake_case = "first_name_last_name"
camel_ish = snake_case.replace("_n", " N").replace("_l", " L")
# This is a simplified example - real conversion needs loops
print(snake_case.replace("_", " ").title().replace(" ", ""))
# FirstNameLastName  ← CamelCase (using title + replace)

# ── Order matters in chaining! ──
text = "aabbcc"
# Replace 'a' with 'b', then 'b' with 'c':
result = text.replace("a", "b").replace("b", "c")
print(result)       # cccccc
# Step 1: "aabbcc" → "bbbbcc"  (a→b)
# Step 2: "bbbbcc" → "cccccc"  (b→c, ALL b's including new ones!)

# Compare with reversed order:
result2 = text.replace("b", "c").replace("a", "b")
print(result2)      # bbcccc
# Step 1: "aabbcc" → "aacccc"  (b→c)
# Step 2: "aacccc" → "bbcccc"  (a→b)
# Different result! ORDER MATTERS.


# ------------------------------------------------------------
# PART 10: .replace() and immutability - very common mistake
# ------------------------------------------------------------

# This cannot be repeated enough because it trips up
# almost every beginner at some point.

# .replace() NEVER modifies the original string.
# You MUST store or use the return value!

text = "Hello World"

# ❌ Very common mistake:
text.replace("World", "Python")     # return value thrown away!
print(text)                         # Hello World  ← not changed!

# ✅ Fix 1: store in a new variable
result = text.replace("World", "Python")
print(result)                       # Hello Python

# ✅ Fix 2: reassign the same variable
text = text.replace("World", "Python")
print(text)                         # Hello Python

# ── Why do beginners make this mistake? ──
# Because in everyday language:
# "Replace the word" suggests modifying in place.
# In Python, ALL string methods work by returning NEW strings.
# The original is always preserved.


# ------------------------------------------------------------
# PART 11: .replace() does NOT use patterns or wildcards
# ------------------------------------------------------------

# .replace() finds EXACT substrings only.
# It does NOT support:
#   - wildcards like * or ?
#   - patterns like "any digit" or "any letter"
#   - regular expressions

# For example: you cannot replace "all digits" with .replace()
# You would need multiple .replace() calls or the 're' module.

text = "Phone: 123-456-7890"

# ❌ This doesn't work (Python takes it literally):
# text.replace("[0-9]", "X")  → would look for the literal "[0-9]"

# ✅ For simple cases, chain multiple replacements:
result = text.replace("1", "X").replace("2", "X").replace("3", "X")
print(result)       # Phone: XXX-456-7890  ← only replaced specific digits

# For true pattern-based replacement, use re.sub() (Module 10+)
# But for straightforward replacements, .replace() is perfect.


# ------------------------------------------------------------
# PART 12: Practical use cases
# ------------------------------------------------------------

# ── Use case 1: Sanitize user input ──
username = "Anna Kowalska"
# Usernames can't have spaces - replace with underscore:
safe_username = username.replace(" ", "_").lower()
print(safe_username)    # anna_kowalska

# ── Use case 2: Format a template ──
template = "Hello, NAME! You have MESSAGES new messages."
name = "Anna"
messages = "5"
result = template.replace("NAME", name).replace("MESSAGES", messages)
print(result)
# Hello, Anna! You have 5 new messages.

# ── Use case 3: Clean up DNA sequence ──
dna = "ATG-CCC-GCA-TTA"
# Remove dashes:
clean_dna = dna.replace("-", "")
print(clean_dna)    # ATGCCCGCATTA

# ── Use case 4: Convert file paths between OS formats ──
windows_path = "C:\\Users\\Anna\\Documents\\file.txt"
unix_path = windows_path.replace("\\", "/")
print(unix_path)    # C:/Users/Anna/Documents/file.txt

# ── Use case 5: Number formatting ──
# In some locales, comma is used as decimal separator
number_eu = "1.234,56"      # European format: . for thousands, , for decimal
# Convert to Python float format:
number_us = number_eu.replace(".", "").replace(",", ".")
print(number_us)    # 1234.56
print(float(number_us))  # 1234.56

# ── Use case 6: Censor words ──
message = "This is a bad word in a bad sentence"
censored = message.replace("bad", "***")
print(censored)     # This is a *** word in a *** sentence

# ── Use case 7: Convert between snake_case and spaces ──
variable_name = "first_name_last_name"
readable = variable_name.replace("_", " ").title()
print(readable)     # First Name Last Name

# ── Use case 8: Normalize newlines ──
# Windows uses \r\n, Unix uses \n
windows_text = "Line 1\r\nLine 2\r\nLine 3"
unix_text = windows_text.replace("\r\n", "\n")
print(repr(unix_text))  # 'Line 1\nLine 2\nLine 3'

# ── Use case 9: Simple encryption (Caesar-style) ──
message = "hello world"
# Replace vowels with symbols:
encoded = message.replace("a", "@").replace("e", "3").replace("i", "1")
encoded = encoded.replace("o", "0").replace("u", "v")
print(encoded)      # h3ll0 w0rld

# ── Use case 10: Fix common typos ──
text = "recieve the acheivment"
fixed = text.replace("recieve", "receive").replace("acheivment", "achievement")
print(fixed)        # receive the achievement


# ------------------------------------------------------------
# PART 13: .replace() vs other methods - when to use which
# ------------------------------------------------------------

# .replace() is great for:
#   ✅ Replacing exact substrings
#   ✅ Deleting characters/substrings (replace with "")
#   ✅ Simple text transformations
#   ✅ Template filling (replace placeholders)

# .replace() is NOT for:
#   ❌ Pattern-based replacement → use re.sub()
#   ❌ Case-insensitive replacement → use re.sub() with re.IGNORECASE
#   ❌ Replacing at a specific position → use slicing
#   ❌ Complex transformations → use loops or re module

# When you just need to change case → use .upper() / .lower()
# When you need to remove edges → use .strip()
# When you need exact substitution → use .replace()

# Example: "change position 3 to X"
# ❌ Wrong tool: text.replace(text[3], "X")  ← replaces ALL occurrences of text[3]!
# ✅ Right tool: text[:3] + "X" + text[4:]   ← slicing for position-specific change


# ------------------------------------------------------------
# PART 14: Counting occurrences before replacing
# ------------------------------------------------------------

# Sometimes you want to know HOW MANY replacements will be made.
# Use .count() (next lecture!) to find out:

text = "the cat sat on the mat near the cat"

occurrences = text.count("cat")     # preview of .count()
print(f"Found {occurrences} occurrences of 'cat'")  # Found 2

result = text.replace("cat", "dog")
print(result)
# the dog sat on the mat near the dog

# ── Verify the replacement changed the length ──
old_len = len(text)
new_len = len(result)
print(f"Original length: {old_len}")    # 35
print(f"New length:      {new_len}")    # 35  ← same! cat and dog are same length

# What if lengths differ?
text = "Hello World"
result = text.replace("World", "Everyone in the World")
print(f"Original: {len(text)} chars")   # 11
print(f"New:      {len(result)} chars") # 27  ← longer!
print(result)   # Hello Everyone in the World


# ------------------------------------------------------------
# PART 15: Edge cases
# ------------------------------------------------------------

# ── Replace empty string ──
# This is an interesting edge case.
# Replacing "" with something inserts it BETWEEN every character
# AND at the start and end!

text = "abc"
print(text.replace("", "-"))   # -a-b-c-
# Inserts "-" between every character including edges!
# This is rarely useful but good to know.

# ── Replace with itself ──
text = "Hello"
print(text.replace("l", "l"))   # Hello  ← unchanged

# ── Very long replacement chains ──
text = "a1b2c3"
# Remove all digits:
clean = (text
         .replace("0", "")
         .replace("1", "")
         .replace("2", "")
         .replace("3", "")
         .replace("4", "")
         .replace("5", "")
         .replace("6", "")
         .replace("7", "")
         .replace("8", "")
         .replace("9", ""))
print(clean)    # abc  ← all digits removed

# ── Replace preserves everything else ──
text = "Hello, World! 123"
print(text.replace("World", "Python"))
# Hello, Python! 123  ← comma, space, !, space, 123 all preserved

# ── Replacing a substring that spans what you think are words ──
text = "the theme is theoretical"
print(text.replace("the", "X"))
# X Xme is Xoretical  ← replaces "the" everywhere including inside words!
# "theme" → "Xme", "theoretical" → "Xoretical"
# .replace() doesn't know about word boundaries!
# For word-boundary-aware replacement, use the 're' module.


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ .replace(old, new) → replaces ALL occurrences of old with new
# ✅ .replace(old, new, count) → replaces only first 'count' occurrences
# ✅ Returns a NEW string - original is NEVER modified (immutable!)
# ✅ Always store or use the return value!
# ✅ Case sensitive: "cat" ≠ "Cat" ≠ "CAT"
# ✅ If 'old' not found → returns original string, NO error
# ✅ .replace("something", "") → DELETES the substring
# ✅ Can be chained: .replace().replace().replace()
# ✅ ORDER MATTERS when chaining!
# ✅ Works on any substring (single char, word, phrase, \n, \t...)
# ✅ Does NOT support wildcards or patterns (use re module for that)
# ✅ .replace("", "x") → inserts x between every character and at edges
# ✅ Does NOT know about word boundaries - replaces anywhere it finds 'old'