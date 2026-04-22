# ============================================================
# MODULE 02 | EXERCISES 21 - .split()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Split each sentence into individual words using .split().
# Print the resulting list AND the number of words (use len()).

sentence1 = "Hello World Python"
sentence2 = "The quick brown fox"
sentence3 = "   Extra   spaces   everywhere   "



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Split these strings on their specific separator.
# Print the list and then access and print each element
# individually with a descriptive label.

date = "2024-07-19"
# separator: "-"
# labels: Year, Month, Day

version = "3.11.2"
# separator: "."
# labels: Major, Minor, Patch

csv_row = "Anna,Kowalska,25"
# separator: ","
# labels: First name, Last name, Age



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate the critical difference between
# .split() and .split(" ").
# For each string below, run both versions and
# print the result AND the length of the result.
# Write a comment explaining the difference.

text1 = "Hello    World"
text2 = "  Python  "
text3 = "one two three"



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output of each line BEFORE running.
# Write your predictions as comments, then verify.

text = "the cat sat on the mat"
# Prediction: ?
print(text.split())
# Prediction: ?
print(text.split(" ", 2))
# Prediction: ?
print(len(text.split()))
# Prediction: ?
print(text.split("at"))
# Prediction: ?
print(text.split("xyz"))



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Use .split() to count words in a sentence.
# Ask the user to enter a sentence.
# Print: "Your sentence has X words."
# Then print the first word and the last word.



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Parse an email address using .split().
# Given the email below:
#   - Split on "@" to get username and domain
#   - Split the domain on "." to get domain parts
#   - Print each part with a label:
#       Username: anna.kowalska
#       Domain: university.edu
#       Domain name: university
#       Top-level domain: edu

email = "anna.kowalska@university.edu"



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use .rsplit() vs .split() with maxsplit=1 to extract
# the file extension from these filenames.
# Use .rsplit(".", 1) to correctly handle filenames
# that have multiple dots.
# Print: "Name: X | Extension: Y" for each.

file1 = "report.pdf"
file2 = "genome_data.fasta"
file3 = "my.important.report.final.docx"
file4 = "script.test.py"



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use .splitlines() to process this multiline string.
# Print each line separately with its line number.
# Then compare with .split("\n") on the same string
# that has a trailing newline - show the difference.

multiline = """First line
Second line
Third line
Fourth line"""

with_trailing_newline = "Line 1\nLine 2\nLine 3\n"
# Compare .splitlines() vs .split("\n") for both strings.



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Parse a log file line using .split() with maxsplit.
# The format is: "DATE TIME LEVEL MESSAGE"
# where MESSAGE can contain spaces.
# Extract each field and print with a label.
# Use maxsplit to avoid splitting the message!

log1 = "2024-03-15 14:30:22 ERROR Database connection failed"
log2 = "2024-03-15 14:30:45 INFO User anna logged in successfully"
log3 = "2024-03-15 14:31:00 WARNING Memory usage above 80 percent"



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Normalize whitespace in strings using split and join.
# The pattern: " ".join(text.split()) removes all extra spaces.
# Apply this to each messy string and print before and after.
# Also print the length before and after.

messy1 = "Hello    World     Python"
messy2 = "  The   quick  brown   fox  "
messy3 = "one\ttwo\tthree\tfour"
messy4 = "First\n\nSecond\n\nThird"



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Investigate edge cases with .split(separator).
# For each case, predict the output before running,
# then verify and write a comment explaining the result.

# Case 1: separator at the start
text1 = ",Anna,25,Warsaw"
# Prediction: ?
print(text1.split(","))

# Case 2: separator at the end
text2 = "Anna,25,Warsaw,"
# Prediction: ?
print(text2.split(","))

# Case 3: consecutive separators
text3 = "Anna,,25"
# Prediction: ?
print(text3.split(","))

# Case 4: only the separator
text4 = ","
# Prediction: ?
print(text4.split(","))

# Case 5: separator not found
text5 = "Hello World"
# Prediction: ?
print(text5.split(","))



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL errors and unexpected behaviors in the code below.
# Write a comment for each line explaining:
#   a) Is it a Python error? If so, what kind?
#   b) If not an error, is the output what you'd expect?

text = "Hello World Python"
text.split()                        # Issue: ?
print(text)                         # What prints?

result = text.split()
print(result + "!")                 # Error: ?

print(result[5])                    # Error: ?

data = "Anna"
parts = data.split(",")
print(parts[1])                     # Error: ?

print("Hello".split(""))            # Surprising? What does this do?



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Parse structured data using split.
# Given the product records below (one per variable),
# each in format: "ID|NAME|PRICE|CATEGORY|IN_STOCK"
# Extract each field and print a formatted summary.
# Convert PRICE to float and IN_STOCK to boolean.
# Expected output format:
#   ID: 001 | Name: Python Book | Price: $29.99 | Category: Books | In stock: True

record1 = "001|Python Book|29.99|Books|True"
record2 = "002|DNA Kit|149.99|Science|False"
record3 = "003|Microscope|299.00|Science|True"



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# DNA restriction enzyme analysis using .split().
#
# Restriction enzymes cut DNA at specific recognition sequences.
# When you split DNA on the recognition sequence,
# the fragments are what's left after cutting.
#
# Given the DNA sequence and recognition sites below:
#
# Part A:
# Split the DNA on EcoRI site "GAATTC".
# Print: number of fragments, and each fragment with its length.
#
# Part B:
# Split the DNA on HindIII site "AAGCTT".
# Same output format.
#
# Part C:
# What does it mean if split() returns a list of length 1?
# (i.e., the recognition site is not found)
# Test with a fake recognition site "XXXXXX".
# Print an appropriate message.
#
# Part D:
# After splitting on EcoRI, what is the total length of all fragments?
# Is it equal to len(dna) - (number of cuts * len(recognition_site))?
# Verify this mathematically.

dna = "ATGCCCGAATTCGCATTAGAATTCGTCGAAAGCTTCGA"
ecori   = "GAATTC"
hindiii = "AAGCTT"



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Multi-part challenge: build a complete CSV parser.
#
# Part A:
# Given the CSV data below (as a multiline string),
# split it into individual lines using .splitlines().
# Then split the FIRST line (header) on "," to get column names.
# Print each column name with its index number.

csv_data = """name,age,city,country,email
Anna Kowalska,25,Warsaw,Poland,anna@email.com
Jan Nowak,32,Krakow,Poland,jan@email.com
Maria Schmidt,28,Berlin,Germany,maria@email.com"""

# Part B:
# Split the second line (first data row) on ","
# and print each field paired with its column name.
# Format: "column_name: value"
#
# Part C:
# Count how many data rows there are (lines minus the header).
# Print: "Total records: X"
#
# Part D:
# Extract all email addresses (last field of each data row).
# Print each email on a separate line.
# Then extract just the domains (part after @) from each email.
# Print each domain.
#
# Part E:
# The city "New York" would cause problems in a CSV split by ","
# if it were written as "New York" (it's fine).
# But what if someone put: "Anna Kowalska,25,"Warsaw, Poland",anna@email.com"
# with a comma inside the city field?
# Split this line on "," and show why it breaks.
# Write a comment explaining what the real solution would be
# (hint: proper CSV parsing, not just split).

problematic = 'Anna Kowalska,25,"Warsaw, Poland",anna@email.com'