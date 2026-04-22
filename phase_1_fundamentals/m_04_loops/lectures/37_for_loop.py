# ============================================================
# MODULE 04 | LECTURE 37 - for loop
# ============================================================
# What you will learn:
# - What a loop is and why we need it
# - How the for loop works in Python
# - Iterating over strings
# - Iterating over lists (preview)
# - Iterating over tuples (preview)
# - Iterating over dictionaries (preview)
# - Loop variable naming conventions
# - Modifying behavior inside a loop
# - Combining loops with if statements
# - Common patterns and idioms
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is a loop and why do we need it?
# ------------------------------------------------------------

# Imagine you want to print every letter of the word "Python".
# Without a loop, you would write:

print("P")
print("y")
print("t")
print("h")
print("o")
print("n")

# That's 6 lines for a 6-letter word.
# What if the word had 100 letters? 1000?
# What if you didn't know the length in advance?
#
# A LOOP solves this by repeating code automatically.
# Instead of writing the same action many times,
# you write it ONCE and tell Python to repeat it.
#
# Real life analogy:
# ┌─────────────────────────────────────────────────────┐
# │ Without loop:                                       │
# │ "Read page 1"                                       │
# │ "Read page 2"                                       │
# │ "Read page 3"                                       │
# │ ... (200 times)                                     │
# │                                                     │
# │ With loop:                                          │
# │ "For each page in the book: read the page"          │
# └─────────────────────────────────────────────────────┘
#
# Python has two types of loops:
# 1. for loop  → repeats for each item in a sequence
# 2. while loop → repeats as long as a condition is True
#
# This lecture covers the FOR loop.

# ------------------------------------------------------------
# PART 2: Basic for loop syntax
# ------------------------------------------------------------

# Syntax:
#     for variable in iterable:
#         code to repeat
#
# Key terms:
# - 'for'      → keyword that starts the loop
# - 'variable' → temporary name for each item (you choose the name)
# - 'in'       → keyword connecting variable to iterable
# - 'iterable' → something Python can iterate over (string, list, etc.)
# - ':'        → colon ends the for line (like if statements)
# - indented block → code that runs on each iteration
#
# How it works:
# 1. Python takes the FIRST item from the iterable
# 2. Assigns it to the variable
# 3. Runs the indented block
# 4. Goes back to step 1 with the NEXT item
# 5. Repeats until all items are processed
# 6. Continues with code AFTER the loop

# Simplest example - iterating over a string:

for letter in "Python":
    print(letter)

# Output:
# P
# y
# t
# h
# o
# n

# What happens step by step:
# Iteration 1: letter = "P" → print("P")
# Iteration 2: letter = "y" → print("y")
# Iteration 3: letter = "t" → print("t")
# Iteration 4: letter = "h" → print("h")
# Iteration 5: letter = "o" → print("o")
# Iteration 6: letter = "n" → print("n")
# Loop ends → continue with next code

# Visual diagram:
#
# "Python"
#  │
#  ├─ "P" ──→ letter = "P" ──→ print(letter)
#  ├─ "y" ──→ letter = "y" ──→ print(letter)
#  ├─ "t" ──→ letter = "t" ──→ print(letter)
#  ├─ "h" ──→ letter = "h" ──→ print(letter)
#  ├─ "o" ──→ letter = "o" ──→ print(letter)
#  └─ "n" ──→ letter = "n" ──→ print(letter)
#                               ↓
#                          (loop ends)

# Code AFTER the loop runs once, after ALL iterations:

for letter in "Hi":
    print(f"Letter: {letter}")
print("Loop finished!")    # runs ONCE after the loop

# Output:
# Letter: H
# Letter: i
# Loop finished!

# ------------------------------------------------------------
# PART 3: The loop variable
# ------------------------------------------------------------

# The loop variable is created by YOU.
# You can name it anything (following normal naming rules).
# It only exists and changes INSIDE the loop.
# After the loop, it holds the LAST value it had.

# Good naming conventions:
# - Name it after what each item IS
# - Use singular form when iterating a collection

# ✅ Good names:
for letter in "DNA":
    print(letter)

for character in "ATCG":
    print(character)

# After the loop:
print(character)    # "G" - last value assigned

# ❌ Bad names (work but unclear):
for x in "DNA":
    print(x)

for i in "DNA":     # 'i' is fine for index but not for characters
    print(i)

# The variable is REASSIGNED on each iteration:

word = "cat"
for letter in word:
    print(f"Current letter: {letter}")
    # letter changes each time

print(f"After loop, letter = '{letter}'")    # 't' - last value

# Output:
# Current letter: c
# Current letter: a
# Current letter: t
# After loop, letter = 't'

# ------------------------------------------------------------
# PART 4: Iterating over strings
# ------------------------------------------------------------

# Strings are sequences of characters.
# A for loop visits each character one at a time.

# Example 1: Print each character with its position

word = "biology"
position = 0
for char in word:
    print(f"Position {position}: '{char}'")
    position += 1

# Output:
# Position 0: 'b'
# Position 1: 'i'
# Position 2: 'o'
# Position 3: 'l'
# Position 4: 'o'
# Position 5: 'g'
# Position 6: 'y'

# Example 2: Count specific characters

dna = "ATCGATCGATCG"
count_a = 0
for base in dna:
    if base == "A":
        count_a += 1
print(f"Number of A bases: {count_a}")    # Number of A bases: 4

# Example 3: Build a new string character by character

original = "hello"
reversed_word = ""
for char in original:
    reversed_word = char + reversed_word    # prepend each character
print(reversed_word)    # olleh

# Example 4: Check if string is a palindrome

word = "racecar"
is_palindrome = True
reversed_w = ""
for char in word:
    reversed_w = char + reversed_w
if word == reversed_w:
    print(f"'{word}' IS a palindrome")
else:
    print(f"'{word}' is NOT a palindrome")
# 'racecar' IS a palindrome

# Example 5: Count vowels

sentence = "bioinformatics"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in sentence:
    if char in vowels:
        vowel_count += 1
print(f"Vowels in '{sentence}': {vowel_count}")
# Vowels in 'bioinformatics': 7

# Example 6: Uppercase every other character

word = "python"
result = ""
index = 0
for char in word:
    if index % 2 == 0:
        result += char.upper()
    else:
        result += char.lower()
    index += 1
print(result)    # PyThOn

# ------------------------------------------------------------
# PART 5: Iterating over lists (preview)
# ------------------------------------------------------------

# Lists are ordered collections of items.
# We'll cover lists in depth in Module 05.
# For now, just understand that for loops work the same way.

# A list is written with square brackets: [item1, item2, item3]

# Example 1: Simple list of strings

fruits = ["apple", "banana", "cherry", "date"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# Output:
# Fruit: apple
# Fruit: banana
# Fruit: cherry
# Fruit: date

# Example 2: List of numbers

scores = [85, 92, 78, 95, 88]
total = 0
for score in scores:
    total += score
average = total / len(scores)
print(f"Total: {total}")
print(f"Average: {average:.1f}")

# Output:
# Total: 438
# Average: 87.6

# Example 3: List of DNA codons

codons = ["ATG", "GCT", "TAC", "GAA", "TAA"]
for codon in codons:
    if codon == "ATG":
        print(f"{codon} ← START codon")
    elif codon in ["TAA", "TAG", "TGA"]:
        print(f"{codon} ← STOP codon")
    else:
        print(f"{codon}")

# Output:
# ATG ← START codon
# GCT
# TAC
# GAA
# TAA ← STOP codon

# Example 4: Find maximum value manually

temperatures = [22.5, 18.3, 25.1, 19.8, 30.2, 24.7]
max_temp = temperatures[0]    # start with first value
for temp in temperatures:
    if temp > max_temp:
        max_temp = temp
print(f"Highest temperature: {max_temp}°C")    # 30.2°C

# Example 5: Filter items

amino_acids = ["Ala", "Gly", "Trp", "Phe", "Val", "Ile"]
aromatic = ["Phe", "Trp", "Tyr", "His"]

print("Aromatic amino acids in list:")
for aa in amino_acids:
    if aa in aromatic:
        print(f"  → {aa}")

# Output:
# Aromatic amino acids in list:
#   → Trp
#   → Phe

# ------------------------------------------------------------
# PART 6: Iterating over tuples (preview)
# ------------------------------------------------------------

# Tuples are like lists but IMMUTABLE (cannot be changed).
# Written with parentheses: (item1, item2, item3)
# For loops work identically with tuples.

# Example 1: Simple tuple

coordinates = (10, 20, 30)
for coord in coordinates:
    print(coord)

# Output:
# 10
# 20
# 30

# Example 2: Tuple of biological data

elements_in_proteins = ("Carbon", "Hydrogen", "Oxygen", "Nitrogen", "Sulfur")
for element in elements_in_proteins:
    print(f"Proteins contain: {element}")

# Example 3: Tuple of tuples (2D data)

student_scores = (
    ("Anna", 95),
    ("Bob", 78),
    ("Carol", 88),
    ("David", 92),
)

for student, score in student_scores:    # unpacking!
    grade = "A" if score >= 90 else "B" if score >= 80 else "C"
    print(f"{student}: {score} → {grade}")

# Output:
# Anna: 95 → A
# Bob: 78 → C
# Carol: 88 → B
# David: 92 → A

# ------------------------------------------------------------
# PART 7: Iterating over dictionaries (preview)
# ------------------------------------------------------------

# Dictionaries store key-value pairs.
# We'll cover them in Module 05.
# By default, iterating over a dict gives you the KEYS.

# Example 1: Iterate over keys (default)

codon_table = {
    "ATG": "Methionine",
    "TAA": "STOP",
    "GCT": "Alanine",
    "TGT": "Cysteine",
}

for codon in codon_table:
    print(codon)

# Output:
# ATG
# TAA
# GCT
# TGT

# Example 2: Iterate over keys and values with .items()

for codon, amino_acid in codon_table.items():
    print(f"{codon} → {amino_acid}")

# Output:
# ATG → Methionine
# TAA → STOP
# GCT → Alanine
# TGT → Cysteine

# Example 3: Iterate over values only with .values()

for amino_acid in codon_table.values():
    print(amino_acid)

# Output:
# Methionine
# STOP
# Alanine
# Cysteine

# ------------------------------------------------------------
# PART 8: Accumulator pattern
# ------------------------------------------------------------

# One of the most important patterns in programming.
# Start with an initial value, then update it each iteration.
# Used for: sum, product, count, building strings, etc.

# Pattern:
#     accumulator = initial_value
#     for item in collection:
#         accumulator = accumulator + (something based on item)

# Example 1: Sum

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0                    # initial value
for num in numbers:
    total += num             # accumulate
print(f"Sum: {total}")       # Sum: 55

# Example 2: Product (factorial-like)

digits = [1, 2, 3, 4, 5]
product = 1                  # initial value (NOT 0! multiplication)
for num in digits:
    product *= num
print(f"Product: {product}") # Product: 120

# Example 3: Count occurrences

sequence = "ATCGATCGATCGATCG"
target = "G"
count = 0
for base in sequence:
    if base == target:
        count += 1
print(f"'{target}' appears {count} times")    # 'G' appears 4 times

# Example 4: Build a string

bases = ["A", "T", "G", "C", "A", "T"]
dna_string = ""
for base in bases:
    dna_string += base
print(f"Built sequence: {dna_string}")    # Built sequence: ATGCAT

# Example 5: Collect matching items

amino_acids = ["Gly", "Ala", "Trp", "Phe", "Val", "Tyr", "Ile"]
aromatic = ["Phe", "Trp", "Tyr", "His"]
found_aromatic = []              # empty list to accumulate into
for aa in amino_acids:
    if aa in aromatic:
        found_aromatic.append(aa)
print(f"Aromatic: {found_aromatic}")    # Aromatic: ['Trp', 'Phe', 'Tyr']

# ------------------------------------------------------------
# PART 9: Combining for loops with if statements
# ------------------------------------------------------------

# The most powerful combination in programming.
# Loop through items, make decisions on each one.

# Example 1: Classify each item

temperatures = [36.1, 38.5, 37.0, 39.2, 36.8, 40.1, 37.3]

print("Body temperature analysis:")
for temp in temperatures:
    if temp >= 39.0:
        status = "🔴 High fever"
    elif temp >= 38.0:
        status = "🟡 Fever"
    elif temp >= 37.5:
        status = "🟠 Slightly elevated"
    elif temp >= 36.1:
        status = "🟢 Normal"
    else:
        status = "🔵 Hypothermia"
    print(f"  {temp}°C → {status}")

# Output:
# Body temperature analysis:
#   36.1°C → 🟢 Normal
#   38.5°C → 🟡 Fever
#   37.0°C → 🟢 Normal
#   39.2°C → 🔴 High fever
#   36.8°C → 🟢 Normal
#   40.1°C → 🔴 High fever
#   37.3°C → 🟢 Normal

# Example 2: Find and count

dna = "ATGCGATACGCTTAG"
start_positions = []
position = 0
for base in dna:
    if dna[position:position+3] == "ATG":
        start_positions.append(position)
    position += 1
print(f"ATG found at positions: {start_positions}")

# Example 3: Grade statistics

grades = [78, 92, 65, 88, 45, 95, 72, 83, 91, 55]
pass_count = 0
fail_count = 0
total = 0

for grade in grades:
    total += grade
    if grade >= 60:
        pass_count += 1
    else:
        fail_count += 1

print(f"Total students: {len(grades)}")
print(f"Passed: {pass_count}")
print(f"Failed: {fail_count}")
print(f"Average: {total/len(grades):.1f}")
print(f"Pass rate: {pass_count/len(grades)*100:.1f}%")

# Output:
# Total students: 10
# Passed: 8
# Failed: 2
# Average: 76.4
# Pass rate: 80.0%

# Example 4: Validate each item

sequences = ["ATCG", "ATXG", "GCTA", "A1CG", "TTTT"]
valid_bases = "ATCG"

for seq in sequences:
    is_valid = True
    for char in seq:              # nested loop!
        if char not in valid_bases:
            is_valid = False
    status = "✅ Valid" if is_valid else "❌ Invalid"
    print(f"{seq}: {status}")

# Output:
# ATCG: ✅ Valid
# ATXG: ❌ Invalid
# GCTA: ✅ Valid
# A1CG: ❌ Invalid
# TTTT: ✅ Valid

# ------------------------------------------------------------
# PART 10: Looping over a string with index
# ------------------------------------------------------------

# Sometimes you need BOTH the character AND its position.
# You can maintain a counter variable manually.

word = "PYTHON"
index = 0
for char in word:
    print(f"Index {index}: {char}")
    index += 1

# Output:
# Index 0: P
# Index 1: Y
# Index 2: T
# Index 3: H
# Index 4: O
# Index 5: N

# A better way (we'll cover in Lecture 10 - enumerate):
# for index, char in enumerate(word):
#     print(f"Index {index}: {char}")

# Accessing specific positions while looping:

dna = "ATCGATCG"
index = 0
for base in dna:
    # Check every 3rd position (0, 3, 6...) - start of codon
    if index % 3 == 0:
        print(f"Codon starts at position {index}: {dna[index:index+3]}")
    index += 1

# Output:
# Codon starts at position 0: ATC
# Codon starts at position 3: GAT
# Codon starts at position 6: CG

# ------------------------------------------------------------
# PART 11: Looping a specific number of times
# ------------------------------------------------------------

# Sometimes you just want to repeat something N times.
# We'll cover range() in Lecture 02, but here's a quick preview.

# Using range() to loop 5 times:
for i in range(5):
    print(f"Iteration {i}")

# Output:
# Iteration 0
# Iteration 1
# Iteration 2
# Iteration 3
# Iteration 4

# Using a list of numbers:
for count in [1, 2, 3, 4, 5]:
    print(f"Count: {count}")

# Repeating an action N times:
n = int(input("How many times to print hello? "))
for _ in range(n):        # _ means "I don't need the loop variable"
    print("Hello!")

# The underscore _ convention:
# When you need to loop N times but don't need the counter value,
# use _ as the variable name. It signals "throwaway variable".

for _ in range(3):
    print("*" * 10)

# Output:
# **********
# **********
# **********

# ------------------------------------------------------------
# PART 12: What can be iterated? (iterables)
# ------------------------------------------------------------

# Python can iterate over many types of objects.
# Anything "iterable" can be used in a for loop.

# STRINGS - each character:
for char in "ABC":
    print(char)      # A, B, C

# LISTS - each element:
for item in [1, 2, 3]:
    print(item)      # 1, 2, 3

# TUPLES - each element:
for item in (10, 20, 30):
    print(item)      # 10, 20, 30

# RANGE - each number in the range:
for num in range(3):
    print(num)       # 0, 1, 2

# DICTIONARY - each key by default:
for key in {"a": 1, "b": 2}:
    print(key)       # a, b

# SET - each element (unordered!):
for item in {1, 2, 3}:
    print(item)      # some order of 1, 2, 3

# Things that are NOT iterable (will cause TypeError):
# integers: for x in 5:       ← TypeError!
# floats:   for x in 3.14:    ← TypeError!
# booleans: for x in True:    ← TypeError!

# You CAN convert some things to make them iterable:
number = 12345
for digit in str(number):    # convert int to string first!
    print(digit)

# Output: 1, 2, 3, 4, 5

# ------------------------------------------------------------
# PART 13: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Forgetting the colon

# for letter in "hello"      ← SyntaxError! Missing colon
#     print(letter)

# ✅ Fix:
for letter in "hello":
    print(letter)

# ❌ MISTAKE 2: Wrong indentation

# for letter in "hello":
# print(letter)              ← IndentationError!

# ✅ Fix:
for letter in "hello":
    print(letter)            # 4 spaces

# ❌ MISTAKE 3: Modifying the iterable while iterating

# This can cause unexpected behavior (we'll cover it in Module 05)
# For now: don't change what you're looping over inside the loop.

# ❌ MISTAKE 4: Trying to iterate over a non-iterable

# for digit in 12345:        ← TypeError! int is not iterable
#     print(digit)

# ✅ Fix: convert to string first
for digit in str(12345):
    print(digit)

# ❌ MISTAKE 5: Using the loop variable after expecting it to reset

for char in "ABC":
    pass                     # char ends as "C"

print(char)                  # "C" - NOT reset after loop!
# The loop variable retains its last value after the loop ends.

# ❌ MISTAKE 6: Confusing the loop variable with the iterable

fruits = ["apple", "banana", "cherry"]

# Wrong - 'fruits' is the list, 'fruit' is one item:
# for fruits in fruits:      ← overwrites the list variable!
#     print(fruits)

# ✅ Fix: use different names:
for fruit in fruits:
    print(fruit)

# ❌ MISTAKE 7: Off-by-one in manual index

word = "Python"
idx = 0
for char in word:
    print(f"{idx}: {char}")
    idx += 1                 # ✅ increment AFTER using idx

# If you forget to increment → idx stays 0 forever!
# If you increment BEFORE using → first index is 1 instead of 0!

# ❌ MISTAKE 8: Empty body without pass

# for char in "hello":      ← SyntaxError! Empty body
#
# ✅ Fix: use pass as placeholder:
for char in "hello":
    pass    # TODO: add logic later

# ❌ MISTAKE 9: Expecting loop to start from a non-zero index automatically

# Python always starts from the FIRST element.
# If you want to skip elements, use slicing or conditions.

word = "Python"
# Skip first two characters:
for char in word[2:]:    # slicing!
    print(char)

# Output: t, h, o, n

# ------------------------------------------------------------
# PART 14: Real-world use cases
# ------------------------------------------------------------

# Use case 1: DNA sequence analysis

dna_sequence = "ATGCGATACGCTTAAGGCCCCTAA"
base_counts = {"A": 0, "T": 0, "C": 0, "G": 0}

for base in dna_sequence:
    if base in base_counts:
        base_counts[base] += 1

total = len(dna_sequence)
print("DNA Base Composition:")
print("=" * 30)
for base, count in base_counts.items():
    percentage = count / total * 100
    bar = "█" * count
    print(f"{base}: {count:2d} ({percentage:.1f}%) {bar}")

gc_content = (base_counts["G"] + base_counts["C"]) / total * 100
print(f"\nGC Content: {gc_content:.1f}%")

# Use case 2: Student grade report

students = [
    ("Anna Kowalski", [88, 92, 79, 95, 84]),
    ("Bob Smith", [72, 68, 75, 80, 71]),
    ("Carol White", [95, 98, 92, 97, 99]),
    ("David Brown", [55, 62, 58, 70, 65]),
]

print("\n" + "=" * 50)
print("STUDENT GRADE REPORT")
print("=" * 50)

for name, grades in students:
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)

    if average >= 90:
        letter = "A"
        status = "Excellence Award 🌟"
    elif average >= 80:
        letter = "B"
        status = "Good Standing ✅"
    elif average >= 70:
        letter = "C"
        status = "Satisfactory"
    elif average >= 60:
        letter = "D"
        status = "Needs Improvement ⚠"
    else:
        letter = "F"
        status = "Academic Probation ❌"

    print(f"\n{name}")
    print(f"  Grades: {grades}")
    print(f"  Average: {average:.1f} ({letter})")
    print(f"  Status: {status}")

# Use case 3: Protein sequence analysis

protein = "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEVQAPSVTAFHTDAHIVDSQHMLSDLFNKLVQEISDHVQAQKRGDIYLKHGDFKQCFASEGFDEMLKEKIGKDKLALLEQAKAKIDDVKKLQ"

amino_acid_properties = {
    "nonpolar": "GAVILMPFW",
    "polar": "STCYNQ",
    "positive": "KRH",
    "negative": "DE",
    "aromatic": "FWY"
}

counts = {prop: 0 for prop in amino_acid_properties}
unknown_count = 0

for aa in protein:
    found = False
    for prop, group in amino_acid_properties.items():
        if aa in group:
            counts[prop] += 1
            found = True
    if not found:
        unknown_count += 1

print("\nProtein Sequence Analysis")
print("=" * 35)
print(f"Length: {len(protein)} amino acids")
for prop, count in counts.items():
    pct = count / len(protein) * 100
    print(f"{prop.capitalize():12}: {count:3d} ({pct:.1f}%)")

# Use case 4: File-like text processing (simulated)

log_lines = [
    "INFO: Server started at 09:00:00",
    "INFO: Connection from 192.168.1.1",
    "ERROR: Database timeout at 09:00:15",
    "INFO: Retry attempt 1",
    "WARNING: High memory usage: 87%",
    "ERROR: Connection refused at 09:00:32",
    "INFO: Connection restored",
    "INFO: Processing complete",
]

error_count = 0
warning_count = 0
info_count = 0
errors = []

for line in log_lines:
    if line.startswith("ERROR"):
        error_count += 1
        errors.append(line)
    elif line.startswith("WARNING"):
        warning_count += 1
    elif line.startswith("INFO"):
        info_count += 1

print("\nLog Analysis Report")
print("=" * 35)
print(f"Total lines:  {len(log_lines)}")
print(f"INFO:         {info_count}")
print(f"WARNING:      {warning_count}")
print(f"ERROR:        {error_count}")
print("\nErrors found:")
for error in errors:
    print(f"  ⚠ {error}")

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ for variable in iterable:   → basic syntax
# ✅ Loop visits each item once, in order
# ✅ Loop variable holds the current item each iteration
# ✅ Indented block runs for EVERY item
# ✅ Code after loop runs ONCE when loop is done
# ✅ Works with: strings, lists, tuples, dicts, range, sets
# ✅ Loop variable retains last value after loop ends
# ✅ Use _ as variable name when you don't need the value
# ✅ Accumulator pattern: start empty, add each iteration
# ✅ Combine with if for powerful filtering/classification
# ✅ Don't modify the iterable while iterating over it

# Quick reference:
# ┌──────────────────────────────────────────────────────────┐
# │ for char in "hello":      ← iterate over string         │
# │ for item in [1, 2, 3]:    ← iterate over list           │
# │ for item in (1, 2, 3):    ← iterate over tuple          │
# │ for key in my_dict:       ← iterate over dict keys      │
# │ for k, v in d.items():    ← iterate keys AND values     │
# │ for _ in range(5):        ← repeat 5 times              │
# │                                                          │
# │ Pattern: accumulate       total = 0                      │
# │                           for x in items: total += x    │
# │                                                          │
# │ Pattern: filter           for x in items:               │
# │                               if condition: do_something │
# └──────────────────────────────────────────────────────────┘