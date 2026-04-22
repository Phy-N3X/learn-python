# ============================================================
# MODULE 02 | LECTURE 22 - .join()
# ============================================================
# What you will learn:
#   - What .join() does and why it exists
#   - The syntax (which feels "backwards" at first!)
#   - How .join() is the complement of .split()
#   - Joining with different separators
#   - Joining with empty string
#   - What .join() requires (strings only!)
#   - Converting non-strings before joining
#   - Common patterns: normalize whitespace, build paths, etc.
#   - Performance: why .join() beats concatenation in loops
#   - Real world use cases
#   - Common mistakes
# ============================================================


# ------------------------------------------------------------
# PART 1: The problem .join() solves
# ------------------------------------------------------------

# In the previous lecture we learned .split():
# It takes ONE string and breaks it into a LIST of strings.

# .join() does the OPPOSITE:
# It takes a LIST of strings and combines them into ONE string.

# Without .join(), you might try to build a string from a list
# using concatenation in a loop (Module 04 topic),
# or manually piece by piece:

words = ["Hello", "World", "Python"]

# ❌ Manual concatenation - tedious and error-prone:
result = words[0] + " " + words[1] + " " + words[2]
print(result)   # Hello World Python
# This breaks if the list has more or fewer items!

# ✅ With .join() - elegant and flexible:
result = " ".join(words)
print(result)   # Hello World Python
# Works for a list of ANY length!

# .join() is used constantly in real Python code.
# It's the standard, idiomatic way to build strings from lists.


# ------------------------------------------------------------
# PART 2: The syntax - "backwards" but logical
# ------------------------------------------------------------

# The syntax of .join() surprises many beginners:
#
#   separator.join(iterable)
#   ↑                ↑
#   the string       the list of strings to join
#   that goes
#   BETWEEN items
#
# You call .join() ON the separator string,
# and pass the LIST as the argument.
#
# Why? Because .join() is a STRING METHOD.
# The separator is a string, so the method belongs to it.

# Examples:
words = ["Hello", "World", "Python"]

# Join with space:
print(" ".join(words))      # Hello World Python

# Join with comma:
print(",".join(words))      # Hello,World,Python

# Join with dash:
print("-".join(words))      # Hello-World-Python

# Join with " | ":
print(" | ".join(words))    # Hello | World | Python

# Join with nothing (empty string):
print("".join(words))       # HelloWorldPython

# The separator can be ANY string - including multi-character ones!
print(" AND ".join(words))  # Hello AND World AND Python
print("...".join(words))    # Hello...World...Python


# ------------------------------------------------------------
# PART 3: .join() is the complement of .split()
# ------------------------------------------------------------

# .split() and .join() are mirror operations.
# You can go back and forth between string and list.

# ── String → List → String ──
original = "Hello World Python"

# Split into list:
word_list = original.split(" ")
print(word_list)        # ['Hello', 'World', 'Python']

# Join back into string:
rejoined = " ".join(word_list)
print(rejoined)         # Hello World Python

# Are they equal?
print(original == rejoined)     # True  ← perfect round-trip!

# ── The classic: normalize whitespace ──
# split() removes extra whitespace, join() rebuilds cleanly
messy = "Hello    World     Python"
normalized = " ".join(messy.split())
print(normalized)       # Hello World Python
# This is one of the most elegant Python idioms!

# ── Change separator ──
# Split on one separator, join with another:
csv = "Anna,25,Warsaw"
parts = csv.split(",")          # ['Anna', '25', 'Warsaw']
pipe_separated = "|".join(parts)
print(pipe_separated)           # Anna|25|Warsaw

date_dashes = "2024-03-15"
parts = date_dashes.split("-")  # ['2024', '03', '15']
date_slashes = "/".join(parts)
print(date_slashes)             # 2024/03/15


# ------------------------------------------------------------
# PART 4: Joining with empty string ""
# ------------------------------------------------------------

# Joining with "" (empty string) concatenates all items
# with NOTHING between them.
# This is very useful for building strings from characters.

letters = ["P", "y", "t", "h", "o", "n"]
word = "".join(letters)
print(word)         # Python

# ── Reversing a string using split + join ──
# (We already know [::-1], but this shows another approach)
word = "Python"
reversed_word = "".join(reversed(word))  # reversed() is a built-in
print(reversed_word)    # nohtyP

# ── Remove specific characters from a string ──
# This is a powerful pattern!
text = "Hello, World! 123"

# Remove all punctuation (manual approach without loops):
# (With loops this is much easier - Module 04)
# For now, the concept:
chars = ["H","e","l","l","o"," ","W","o","r","l","d"," ","1","2","3"]
# Filter manually... but this shows the principle.

# More practical example - remove spaces:
text = "Hello World Python"
no_spaces = "".join(text.split())
print(no_spaces)    # HelloWorldPython

# ── Build a string from characters (list) ──
chars = ["D", "N", "A"]
print("".join(chars))       # DNA

nucleotides = ["A", "T", "G", "C", "C", "C"]
sequence = "".join(nucleotides)
print(sequence)     # ATGCCC


# ------------------------------------------------------------
# PART 5: What .join() requires - strings only!
# ------------------------------------------------------------

# .join() ONLY works with an iterable of STRINGS.
# If ANY element is not a string → TypeError!

# ✅ All strings → works:
words = ["Hello", "World"]
print(" ".join(words))      # Hello World

# ❌ Mixed types → TypeError:
mixed = ["Hello", 42, "World"]
# print(" ".join(mixed))
# TypeError: sequence item 1: expected str instance, int found

# ❌ List of numbers → TypeError:
numbers = [1, 2, 3]
# print(",".join(numbers))
# TypeError: sequence item 0: expected str instance, int found

# ✅ Fix: convert all items to strings first using str():
numbers = [1, 2, 3]
result = ",".join(str(n) for n in numbers)  # generator - preview!
print(result)       # 1,2,3

# OR manually (without loops/generators):
numbers = [1, 2, 3]
str_numbers = [str(numbers[0]), str(numbers[1]), str(numbers[2])]
print(",".join(str_numbers))    # 1,2,3

# This is WHY knowing the types in your list matters!
# Always make sure all elements are strings before joining.


# ------------------------------------------------------------
# PART 6: Converting non-strings before joining
# ------------------------------------------------------------

# The standard pattern for joining non-string data:
# convert each item to str() before or during the join.

# ── Joining integers ──
ages = [25, 30, 28, 35]
# Convert each to string:
age_strings = [str(ages[0]), str(ages[1]), str(ages[2]), str(ages[3])]
result = ", ".join(age_strings)
print(result)       # 25, 30, 28, 35

# ── Joining floats ──
prices = [9.99, 14.50, 3.75]
price_strings = [str(prices[0]), str(prices[1]), str(prices[2])]
result = " | ".join(price_strings)
print(result)       # 9.99 | 14.5 | 3.75

# ── Joining booleans ──
flags = [True, False, True]
flag_strings = [str(flags[0]), str(flags[1]), str(flags[2])]
result = ",".join(flag_strings)
print(result)       # True,False,True

# When we learn list comprehensions (Module 11), this becomes:
# result = ",".join(str(x) for x in ages)
# But for now, the manual approach works fine.


# ------------------------------------------------------------
# PART 7: Joining a single-item list
# ------------------------------------------------------------

# If the list has only ONE item, .join() returns that item
# without any separator (there's nothing to put it between).

single = ["Hello"]
print(" ".join(single))     # Hello  ← no separator added
print("-".join(single))     # Hello  ← still no separator
print("".join(single))      # Hello  ← same

# If the list is EMPTY, .join() returns an empty string "":
empty_list = []
print(" ".join(empty_list))     # ""  ← empty string, no error!
print(repr(" ".join(empty_list)))   # ''

# This safe behavior means you don't need to check
# if the list is empty before calling .join().


# ------------------------------------------------------------
# PART 8: .join() with strings directly (not just lists)
# ------------------------------------------------------------

# .join() works with ANY iterable of strings.
# This includes strings themselves! (A string is iterable)

# Joining a STRING iterates over its characters:
word = "Python"
print("-".join(word))   # P-y-t-h-o-n
# Each character of "Python" is joined with "-"!

print(" ".join("DNA"))  # D N A
print("..".join("Hi"))  # H..i

# This is occasionally useful for formatting:
print(", ".join("ATCG"))    # A, T, C, G
# Useful for displaying individual characters with separators


# ------------------------------------------------------------
# PART 9: Building strings efficiently - .join() vs concatenation
# ------------------------------------------------------------

# This is important for writing GOOD Python code.
# When building a string by adding many pieces together,
# .join() is FAR more efficient than repeated concatenation.

# Why? Strings are immutable.
# Each "+" creates a NEW string and copies all previous content.
# With 1000 pieces, that's 1000 copy operations!

# .join() calculates the final size first, allocates once,
# then fills it in. Much faster for large data.

# ── Concatenation (inefficient for many pieces) ──
words = ["Hello", "World", "Python", "is", "great"]

# ❌ Don't do this with many items:
result = ""
result = result + words[0]
result = result + " " + words[1]
result = result + " " + words[2]
# ... gets worse with more items

# ✅ Do this instead:
result = " ".join(words)
print(result)   # Hello World Python is great

# For small numbers of pieces (2-3), concatenation is fine.
# For larger collections, always use .join().

# In practice: whenever you have a LIST of strings
# and want to combine them → use .join(). Always.


# ------------------------------------------------------------
# PART 10: Common .join() patterns
# ------------------------------------------------------------

# These patterns appear constantly in real Python code.
# Memorize them!

# ── Pattern 1: Join words with space ──
words = ["The", "quick", "brown", "fox"]
sentence = " ".join(words)
print(sentence)     # The quick brown fox

# ── Pattern 2: Create CSV line ──
fields = ["Anna", "Kowalska", "25", "Warsaw"]
csv_line = ",".join(fields)
print(csv_line)     # Anna,Kowalska,25,Warsaw

# ── Pattern 3: Build file path ──
parts = ["home", "user", "documents", "file.txt"]
path = "/".join(parts)
print(path)         # home/user/documents/file.txt
print("/" + path)   # /home/user/documents/file.txt (absolute path)

# ── Pattern 4: Build URL ──
segments = ["https://api.example.com", "users", "profile", "settings"]
url = "/".join(segments)
print(url)          # https://api.example.com/users/profile/settings

# ── Pattern 5: Normalize whitespace ──
messy = "  Hello    World   Python  "
clean = " ".join(messy.split())
print(clean)        # Hello World Python

# ── Pattern 6: Join characters into word ──
chars = ["D", "N", "A"]
word = "".join(chars)
print(word)         # DNA

# ── Pattern 7: Add separator between characters ──
code = "ABC123"
spaced = " ".join(code)
print(spaced)       # A B C 1 2 3

# ── Pattern 8: Build separator line ──
print("-" * 40)     # we already know this
# But for dynamic separators:
items = ["Name", "Age", "City"]
header = " | ".join(items)
separator = "-" * len(header)
print(header)       # Name | Age | City
print(separator)    # ------------------

# ── Pattern 9: Join lines into paragraph ──
lines = ["First sentence.", "Second sentence.", "Third sentence."]
paragraph = " ".join(lines)
print(paragraph)    # First sentence. Second sentence. Third sentence.

# Or keep them as separate lines:
multiline = "\n".join(lines)
print(multiline)
# First sentence.
# Second sentence.
# Third sentence.

# ── Pattern 10: Convert number list to string ──
numbers = [1, 2, 3, 4, 5]
# Manual conversion (without loops):
num_strings = [str(numbers[0]), str(numbers[1]), str(numbers[2]),
               str(numbers[3]), str(numbers[4])]
result = ", ".join(num_strings)
print(result)       # 1, 2, 3, 4, 5


# ------------------------------------------------------------
# PART 11: .join() in data processing pipelines
# ------------------------------------------------------------

# .join() is almost always part of a pipeline:
# split → process → join

# ── Pipeline 1: change CSV separator ──
csv_comma = "Anna,Kowalska,25,Warsaw"
csv_pipe = "|".join(csv_comma.split(","))
print(csv_pipe)     # Anna|Kowalska|25|Warsaw

# ── Pipeline 2: change date format ──
date_iso = "2024-03-15"     # YYYY-MM-DD
parts = date_iso.split("-")
date_eu = ".".join(parts)   # DD.MM.YYYY (if we reverse)
date_eu = ".".join(reversed(parts))
print(date_eu)      # 15.03.2024

# Wait - reversed() returns an iterator, not a list.
# Let's do it explicitly:
year, month, day = date_iso.split("-")
date_eu = ".".join([day, month, year])
print(date_eu)      # 15.03.2024

# ── Pipeline 3: title case each word, then join ──
sentence = "hello world python"
words = sentence.split()
# Title case each word:
titled = [words[0].title(), words[1].title(), words[2].title()]
result = " ".join(titled)
print(result)       # Hello World Python

# ── Pipeline 4: strip each word, then join ──
messy_csv = "  Anna  ,  25  ,  Warsaw  "
parts = messy_csv.split(",")
# Strip each part:
clean_parts = [parts[0].strip(), parts[1].strip(), parts[2].strip()]
result = ",".join(clean_parts)
print(result)       # Anna,25,Warsaw  ← clean!


# ------------------------------------------------------------
# PART 12: Real world applications
# ------------------------------------------------------------

# ── Application 1: Build a formatted report line ──
name    = "Anna Kowalska"
age     = "25"
city    = "Warsaw"
country = "Poland"

fields = [name, age, city, country]
csv_line = ",".join(fields)
print(csv_line)     # Anna Kowalska,25,Warsaw,Poland

# ── Application 2: Build a SQL query (simplified) ──
columns = ["name", "age", "city", "email"]
select_clause = ", ".join(columns)
query = f"SELECT {select_clause} FROM users"
print(query)        # SELECT name, age, city, email FROM users

# ── Application 3: Build an HTML list ──
items = ["Python", "Bioinformatics", "Data Science"]
li_items = ["<li>" + item + "</li>" for item in items]
# (This uses list comprehension - preview! For now manually:)
li_items = [
    "<li>" + items[0] + "</li>",
    "<li>" + items[1] + "</li>",
    "<li>" + items[2] + "</li>"
]
html_list = "<ul>\n" + "\n".join(li_items) + "\n</ul>"
print(html_list)
# <ul>
# <li>Python</li>
# <li>Bioinformatics</li>
# <li>Data Science</li>
# </ul>

# ── Application 4: Reconstruct DNA from codons ──
codons = ["ATG", "CCC", "GCA", "TTA"]
full_sequence = "".join(codons)
print(full_sequence)    # ATGCCCGCATTA

# Or with spaces for readability:
readable = " ".join(codons)
print(readable)         # ATG CCC GCA TTA

# ── Application 5: Build a file path ──
root = "/home"
user = "anna"
folder = "documents"
filename = "thesis.pdf"
path = "/".join([root, user, folder, filename])
print(path)     # /home/anna/documents/thesis.pdf

# Better: strip the root's leading slash issue:
parts = [root.strip("/"), user, folder, filename]
path = "/" + "/".join(parts)
print(path)     # /home/anna/documents/thesis.pdf

# ── Application 6: Create a formatted table header ──
columns = ["Name", "Age", "City", "Score"]
col_widths = [15, 5, 10, 7]

# Pad each column name to its width:
padded = [columns[i].ljust(col_widths[i]) for i in range(len(columns))]
# Manual version:
padded = [
    columns[0].ljust(col_widths[0]),    # "Name           "
    columns[1].ljust(col_widths[1]),    # "Age  "
    columns[2].ljust(col_widths[2]),    # "City      "
    columns[3].ljust(col_widths[3])     # "Score  "
]
header = " | ".join(padded)
print(header)   # Name            | Age   | City       | Score

# ── Application 7: Join words with Oxford comma ──
items = ["apples", "bananas", "oranges"]
if len(items) <= 1:
    result = "".join(items)
elif len(items) == 2:
    result = " and ".join(items)
else:
    result = ", ".join(items[:-1]) + ", and " + items[-1]
print(result)   # apples, bananas, and oranges

# ── Application 8: Build a regex pattern (preview) ──
keywords = ["python", "java", "javascript"]
pattern = "|".join(keywords)
print(pattern)  # python|java|javascript  ← regex OR pattern!


# ------------------------------------------------------------
# PART 13: .join() vs f-strings vs concatenation
# ------------------------------------------------------------

# Three ways to build strings - when to use each:

name = "Anna"
age = "25"
city = "Warsaw"

# ── f-string: best for FIXED structure with variables ──
result = f"{name}, {age}, {city}"
print(result)   # Anna, 25, Warsaw
# Use when: you know exactly what goes where

# ── Concatenation: fine for 2-3 pieces ──
result = name + ", " + age + ", " + city
print(result)   # Anna, 25, Warsaw
# Use when: very simple, few pieces

# ── .join(): best for VARIABLE number of items from a list ──
fields = [name, age, city]
result = ", ".join(fields)
print(result)   # Anna, 25, Warsaw
# Use when: you have a list of unknown size, or many items

# The rule of thumb:
# Fixed structure → f-string
# 2-3 pieces      → concatenation or f-string
# List of items   → .join()


# ------------------------------------------------------------
# PART 14: Edge cases and surprising behaviors
# ------------------------------------------------------------

# ── Empty list → empty string ──
print("".join([]))      # ""
print(" ".join([]))     # ""
print(repr(" ".join([])))   # ''

# ── Single item → no separator ──
print("-".join(["Hello"]))  # Hello  ← no dash!

# ── Joining a string directly ──
print("-".join("ABC"))  # A-B-C  ← iterates characters!

# ── Joining list of empty strings ──
empties = ["", "", ""]
print(",".join(empties))    # ,,  ← two commas, no content!

# ── Separator longer than items ──
words = ["a", "b", "c"]
print(" -- ".join(words))   # a -- b -- c

# ── Joining after split with different separator ──
text = "one::two::three"
parts = text.split("::")    # ['one', 'two', 'three']
result = " | ".join(parts)
print(result)               # one | two | three

# ── Verify: split then join on same sep = original ──
original = "Hello,World,Python"
reconstructed = ",".join(original.split(","))
print(original == reconstructed)    # True  ← always!
# (as long as separator doesn't appear in the items)


# ------------------------------------------------------------
# PART 15: Common mistakes with .join()
# ------------------------------------------------------------

# ── Mistake 1: Backwards syntax ──
words = ["Hello", "World"]

# ❌ Wrong - trying to call join on the LIST:
# words.join(" ")   # AttributeError: list has no attribute 'join'

# ✅ Correct - call join on the SEPARATOR STRING:
result = " ".join(words)
print(result)   # Hello World

# ── Mistake 2: Forgetting it's a string method ──
# The separator is a string, .join() is called on the separator!
# This is confusing but remember:
# " ".join(words) = "put ' ' between every item in words"

# ── Mistake 3: Joining non-strings ──
numbers = [1, 2, 3]
# " ".join(numbers)    # ❌ TypeError!

# ✅ Fix:
result = " ".join([str(1), str(2), str(3)])
print(result)   # 1 2 3

# ── Mistake 4: Not storing the result ──
words = ["Hello", "World"]
" ".join(words)         # ← thrown away!
print(words)            # ['Hello', 'World']  ← still a list!

# ✅ Fix:
result = " ".join(words)
print(result)           # Hello World

# ── Mistake 5: Expecting join to add separator at start/end ──
words = ["Hello", "World", "Python"]
result = ",".join(words)
print(result)           # Hello,World,Python
# Note: NO comma at the start or end!
# separator goes BETWEEN items only.

# If you need a trailing separator:
result_with_trailing = ",".join(words) + ","
print(result_with_trailing)     # Hello,World,Python,

# ── Mistake 6: Joining with wrong type separator ──
# The SEPARATOR must also be a string!
# 42.join(["a", "b"])  # ❌ AttributeError: 'int' has no attribute 'join'
# Use: str(42).join(...)  or just "42".join(...)
print("42".join(["a", "b"]))    # a42b


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ .join() combines a list of strings into ONE string
# ✅ Syntax: "separator".join(list_of_strings)
# ✅ The SEPARATOR is what you call .join() ON
# ✅ The LIST is passed as the argument
# ✅ Complement of .split(): split breaks apart, join rebuilds
# ✅ "".join(list)  → concatenate with nothing between items
# ✅ " ".join(list) → join with spaces
# ✅ ",".join(list) → join with commas (CSV!)
# ✅ "\n".join(list)→ join with newlines (multiline text!)
# ✅ ALL items in the list MUST be strings → TypeError otherwise!
# ✅ Convert non-strings with str() before joining
# ✅ Empty list → returns ""
# ✅ Single-item list → returns that item, no separator added
# ✅ .join() on a string → joins its characters!
# ✅ Separator goes BETWEEN items only (not at start or end)
# ✅ .join() is faster than concatenation for many pieces
# ✅ Use f-strings for fixed structure, .join() for lists