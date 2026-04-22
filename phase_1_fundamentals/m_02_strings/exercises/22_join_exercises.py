# ============================================================
# MODULE 02 | EXERCISES 22 - .join()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Join the lists below using the specified separator.
# Print each result with a descriptive label.

words = ["Hello", "World", "Python"]
# a) Join with space
# b) Join with comma
# c) Join with " - "
# d) Join with empty string ""
# e) Join with " AND "



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate that .join() is the complement of .split().
# Start with a string, split it, then join it back.
# Verify the result equals the original using ==.
# Do this for 3 different strings and separators.

string1 = "Hello World Python"           # separator: " "
string2 = "Anna,Kowalska,25,Warsaw"      # separator: ","
string3 = "2024-03-15"                   # separator: "-"



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output of each line BEFORE running.
# Write your predictions as comments, then verify.

words = ["A", "B", "C", "D"]
# Prediction: ?
print(" ".join(words))
# Prediction: ?
print("".join(words))
# Prediction: ?
print(" | ".join(words))
# Prediction: ?
print("-".join("Python"))
# Prediction: ?
print(" ".join([]))
# Prediction: ?
print(",".join(["Hello"]))



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate the immutability rule:
# .join() returns a NEW string, the list is unchanged.
# Show:
#   a) Call .join() without storing → list unchanged
#   b) Store the result → new string created
#   c) Print types of both (list vs str)

words = ["Hello", "World", "Python"]



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Normalize whitespace using split() + join().
# For each messy string below:
#   1. Split (no argument)
#   2. Join with single space
# Print before (with repr()) and after.
# Also print length before and after.

messy1 = "Hello    World     Python"
messy2 = "  The   quick  brown   fox  "
messy3 = "one\ttwo\tthree\tfour"
messy4 = "  \n  Hello  \t  World  \n  "



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Convert between different data formats using split + join.
# For each string, convert it to the specified format.

# a) CSV to pipe-separated:
csv = "Anna,Kowalska,25,Warsaw"
# Expected: "Anna|Kowalska|25|Warsaw"

# b) Dash-separated date to slash-separated:
date_dash = "2024-03-15"
# Expected: "2024/03/15"

# c) Space-separated to underscore-separated (like a variable name):
phrase = "hello world python"
# Expected: "hello_world_python"

# d) Snake_case to space-separated title:
snake = "first_name_last_name"
# Expected: "First Name Last Name"



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Convert dates between formats using split + join.
# Input:  "2024-03-15"  (YYYY-MM-DD)
# Output: "15.03.2024"  (DD.MM.YYYY)
# Do it in TWO steps:
#   1. Split on "-" → get [year, month, day]
#   2. Join in reversed order with "."
# Print both the original and converted date.
# Do this for all three dates.

date1 = "2024-03-15"
date2 = "1999-12-31"
date3 = "2000-01-01"



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Demonstrate the TypeError when joining non-strings.
# Then fix each case by converting to strings first.
#
# Part A: Try to join these (show/explain the error as comment):
numbers = [1, 2, 3, 4, 5]
# " ".join(numbers)  ← what error? write as comment

# Part B: Fix by converting each element manually:
# (without loops - do it manually for this small list)

# Part C: Do the same for:
prices = [9.99, 14.50, 3.75]
flags = [True, False, True, False]



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build structured output using .join().
#
# Given the data below, build:
#   a) A CSV line: "Anna,Kowalska,25,Warsaw,Poland"
#   b) A pipe-separated line: "Anna | Kowalska | 25 | Warsaw | Poland"
#   c) A formatted display:
#      "Name: Anna Kowalska | Age: 25 | Location: Warsaw, Poland"
#   d) A URL slug: "anna-kowalska-25-warsaw-poland" (all lowercase, dashes)

first_name = "Anna"
last_name  = "Kowalska"
age        = "25"
city       = "Warsaw"
country    = "Poland"



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# DNA sequence processing using .join().
#
# Part A:
# Join these codons into a full DNA sequence (no separator):
codons = ["ATG", "CCC", "GCA", "TTA", "GTC", "GAA"]

# Part B:
# Join the same codons with a space (for readable display):

# Part C:
# Join the same codons with a dash (some notations use this):

# Part D:
# You have individual nucleotides as a list.
# Join them into a sequence AND also display them
# with " - " between each one (for annotation purposes):
nucleotides = ["A", "T", "G", "C", "C", "C"]

# Part E:
# Split the full sequence from Part A back into codons
# (groups of 3). Use slicing to get each codon,
# put them in a list, then join with " | ".
# Expected: "ATG | CCC | GCA | TTA | GTC | GAA"



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a SQL SELECT query dynamically using .join().
#
# Given the components below, build the query:
# "SELECT name, age, city, email FROM users WHERE country = 'Poland'"
#
# Build it step by step:
#   1. Join the columns with ", " for the SELECT clause
#   2. Combine everything into the final query using f-string
# Print the final query.
# Then modify it: add "score" to the columns and rebuild.

columns = ["name", "age", "city", "email"]
table = "users"
condition = "country = 'Poland'"



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Implement the Oxford comma rule using .join().
# The Oxford comma: "apples, bananas, and oranges"
# Rules:
#   - 0 items → ""
#   - 1 item  → "apples"
#   - 2 items → "apples and bananas"
#   - 3+ items → "apples, bananas, and oranges"
#                 (comma before "and" for last item)
#
# Implement this for all four test cases below.
# Use .join() for the multi-item cases.

items0 = []
items1 = ["apples"]
items2 = ["apples", "bananas"]
items3 = ["apples", "bananas", "oranges"]
items4 = ["apples", "bananas", "oranges", "grapes", "melons"]



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL errors and unexpected behaviors in the code below.
# For each line write a comment explaining what's wrong
# or surprising. Then fix all actual errors.

words = ["Hello", "World", "Python"]

words.join(" ")                         # Error: ?
print(words)                            # What prints?

result = " ".join(words)
result.join(["a", "b"])                 # Issue: ?

numbers = [1, 2, 3]
print(",".join(numbers))                # Error: ?

print(42.join(["a", "b"]))              # Error: ?

empty = []
print(",".join(empty))                  # Error or surprise? What prints?

print(" ".join("Hello"))                # Surprise? What prints? Explain.



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a complete CSV file content using .join() and .split().
#
# You have this raw data (each person's data as a string):
person1 = "Anna | Kowalska | 25 | Warsaw | anna@email.com"
person2 = "Jan | Nowak | 32 | Krakow | jan@email.com"
person3 = "Maria | Schmidt | 28 | Berlin | maria@email.com"
#
# Part A:
# Convert each person's data from pipe-separated to CSV (comma-separated).
# Use split(" | ") then join(",").
#
# Part B:
# Create a CSV header: "first_name,last_name,age,city,email"
# Join it with the three data rows (using "\n" between lines)
# to create the complete CSV file content.
# Print it.
#
# Part C:
# From the complete CSV content, split it back into lines
# using .splitlines().
# Split the first line (header) on "," to get column names.
# Split the second line (first data row) on "," to get values.
# Pair them up and print: "column: value" for each pair.
#
# Part D:
# Count the total number of characters in the CSV content.
# Count the total number of lines (including header).
# Count the total number of fields (all values across all rows).



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Multi-part challenge: string reconstruction puzzle.
#
# Part A:
# Given this scrambled sentence (words in wrong order):
scrambled = "Python learning love I programming and"
# Split into words, manually reorder them into correct sentence,
# then join back. The correct sentence is:
# "I love Python programming and learning"
# Use indexing on the split result to pick words in right order.
#
# Part B:
# Given these lines of a poem (also scrambled):
line1 = "roses are red"
line2 = "I love Python"
line3 = "violets are blue"
line4 = "and so should you"
# Join them in the correct order (1, 3, 2, 4) with newlines.
# Print the result.
#
# Part C:
# Given: word = "Python"
# Using ONLY "".join() and list operations (indexing, slicing):
#   - Reverse it: "nohtyP"      (join the reversed characters)
#   - Interleave with "-": "P-y-t-h-o-n"  (join the string with "-")
#   - Double each character: "PPyytthhoonn"
#     (for each char, repeat it twice - do manually for each char)
#   - Build "PyPy": take chars at index 0,1,0,1 and join
#
# Part D:
# Verify this mathematical relationship:
# For any string s and separator sep:
#   sep.join(s.split(sep)) == s
# IF AND ONLY IF sep does not appear consecutively or at edges.
# Test with:
#   s = "hello,world,python" and sep = ","    → should be True
#   s = "hello,,world"       and sep = ","    → is it True? Why?
#   s = ",hello,world,"      and sep = ","    → is it True? Why?
# Print the results and explain each case in a comment.