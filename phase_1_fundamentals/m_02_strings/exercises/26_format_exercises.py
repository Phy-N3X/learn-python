# ============================================================
# MODULE 02 | EXERCISES 26 - .format()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Use .format() with basic {} placeholders.
# Complete each print statement using .format().
# Do NOT use concatenation or f-strings.

name = "Anna"
age = 25
city = "Warsaw"
language = "Python"

# a) Print: "Hello, Anna!"
print("Hello, {}!".format(___))

# b) Print: "Anna is 25 years old."
print(___)

# c) Print: "Anna lives in Warsaw and loves Python."
print(___)

# d) Print: "25 + 25 = 50"
print("{} + {} = {}".format(___, ___, ___))



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate indexed {0}, {1} placeholders.
# For each task, use indexed placeholders.
#
# a) Print: "Jan and Anna" using format("Anna", "Jan")
#    (Note: arguments are in REVERSE order from output!)
#
# b) Print: "Python Python Python" using only ONE argument
#
# c) Print: "(x, y) and (y, x)" using format("x", "y")
#
# d) Print: "Warsaw is in Poland. Poland is great. Warsaw is beautiful."
#    using only TWO arguments: "Warsaw" and "Poland"



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Use named placeholders {name}, {value}.
# Complete each using keyword arguments in .format().

# a) Print: "Name: Anna | Age: 25 | City: Warsaw"
print("Name: {name} | Age: {age} | City: {city}".format(___))

# b) Store this template and use it THREE times with different data:
template = "Student: {name} | Score: {score} | Grade: {grade}"
# Use with: Anna/95/A, Jan/78/C+, Maria/88/B+

# c) Print: "The {animal} sat on the {object}."
#    First with animal="cat", object="mat"
#    Then with animal="dog", object="rug"



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate immutability of .format().
# Show that .format() does NOT modify the original string.
# Show the common mistake of not storing the result.
# Then show the correct approach.

template = "Hello, {}!"
# Step 1: Call .format() without storing - show template unchanged
# Step 2: Store the result correctly
# Step 3: Print type of template and result
# Write comments explaining each step.



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Format width and alignment.
# BEFORE running, predict the output of each line.
# Write predictions as comments, then verify.
# Use | on both sides to make width visible.

# Prediction: ?
print("|{:10}|".format("hi"))
# Prediction: ?
print("|{:10}|".format(42))
# Prediction: ?
print("|{:<10}|".format("hi"))
# Prediction: ?
print("|{:>10}|".format("hi"))
# Prediction: ?
print("|{:^10}|".format("hi"))
# Prediction: ?
print("|{:*^10}|".format("hi"))
# Prediction: ?
print("|{:->10}|".format("hi"))



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Format floats with different precision.
# Given pi = 3.141592653589793, format it as:
#   a) Default float (no format spec)
#   b) 2 decimal places
#   c) 4 decimal places
#   d) 0 decimal places
#   e) Width 15, 3 decimal places, right-aligned
#   f) Width 15, 3 decimal places, with * fill, centered
# Print each with a label.

pi = 3.141592653589793



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Format percentages and large numbers.
#
# Part A: Format these ratios as percentages with 1 decimal place:
ratios = [0.7543, 0.123, 1.0, 0.0, 0.5]

# Part B: Format these large numbers with comma separators:
numbers = [1000000, 9876543, 1234567890, 42]

# Part C: Format these prices as currency (2 decimal places, commas):
prices = [9.99, 1299.0, 149.5, 0.5, 99999.99]
# Format: "$  9.99", "$1,299.00" etc. (right-aligned in width 12)



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a formatted table using .format().
# Given the data below, print a nicely formatted table.
# Requirements:
#   - Header row with column names
#   - Separator lines (use "-" * total_width)
#   - Name: left-aligned in 20 chars
#   - Age: right-aligned in 5 chars
#   - Score: right-aligned in 8 chars, 1 decimal place
#   - Grade: center-aligned in 8 chars

students = [
    ("Anna Kowalska",    25, 94.3, "A"),
    ("Jan Nowak",        32, 78.6, "C+"),
    ("Maria Schmidt",    28, 88.0, "B+"),
    ("Piotr Wiśniewski", 21, 62.5, "D"),
    ("Zofia Lis",        24, 97.1, "A+"),
]



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Binary, octal, and hexadecimal formatting.
#
# For each number below, print it in ALL formats:
#   decimal, binary, octal, hex (lower), hex (upper)
# Format as a table with headers.
# Each number should take width 12 in its column.

numbers = [0, 1, 10, 42, 127, 255, 256, 1000]

# Expected format (example for 255):
# Dec    Bin           Oct    Hex    HEX
# 255    11111111      377    ff     FF



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# DNA sequence analysis report using .format().
# Given the DNA sequence below:
#   1. Count A, T, G, C
#   2. Calculate GC content
#   3. Format a complete analysis report
#
# The report should include:
#   - Centered title in width 45
#   - Separator lines
#   - Each nucleotide: name, count, percentage (1 decimal)
#   - GC content (1 decimal %)
#   - Total length
#   - All numbers right-aligned

dna = "ATGCCCGCATTAGTCGAAATGCCCGGCATTATGAAACCCGTA"



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Template-based email generator.
# Store the template as a variable (a named string).
# Use named placeholders throughout.
# Generate 3 different emails from the same template.

email_template = """Dear {title} {last_name},

Thank you for registering for {course_name}.
Your registration ID is {reg_id}.
The course starts on {start_date}.

Your current enrollment status: {status}
Seats remaining: {seats_left}

Best regards,
{sender_name}
{institution}"""

# Generate emails for:
# 1. Dr. Kowalska, Bioinformatics 101, REG-2024-001, 2024-03-01, Confirmed, 5
# 2. Prof. Nowak, Python for Scientists, REG-2024-002, 2024-04-15, Pending, 12
# 3. Ms. Schmidt, Data Analysis, REG-2024-003, 2024-05-01, Confirmed, 3
# Sender: Dr. Admin, University of Science



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL errors and unexpected behaviors below.
# Write a comment for each explaining what's wrong.
# Then fix all actual errors.

name = "Anna"
score = 94.567

# Error: ?
print("Hello, {name}!".format(name))

# Error: ?
print("{} and {0}".format("a", "b"))

# Error: ?
result = "Score: {:.2f}".format(score)
result.format()
print(result)

# Surprising behavior - explain:
print("{:.3}".format(score))        # What prints? Why?
print("{:.3}".format("Hello"))      # What prints? Why?

# Error: ?
print("{:10,d}".format(3.14))

# Error: ?
print("{".format("test"))



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Scientific data formatting.
# Given the molecular data below, create a formatted report.
# Requirements:
#   - Title: centered in width 60, filled with =
#   - Column headers and data rows aligned
#   - Molecular weight: 2 decimal places, right in width 12
#   - Concentration: scientific notation, 3 decimal places, width 15
#   - Purity: percentage, 1 decimal place, width 10
#   - Melting point: 1 decimal place with + sign if positive, width 10

molecules = [
    ("Glucose",        180.16,  2.500e-3,  0.9943,  146.0),
    ("Ethanol",         46.07,  8.500e-2,  0.9985,  -114.1),
    ("Aspirin",        180.16,  1.200e-4,  0.9990,  135.0),
    ("Caffeine",       194.19,  3.750e-5,  0.9875,  235.0),
    ("NaCl",            58.44,  5.000e-1,  0.9999,  800.7),
]



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a complete invoice generator using .format().
#
# Requirements:
#   - Company header centered in width 50
#   - Invoice number and date right-aligned
#   - Itemized list: item name (left, 25), qty (right, 5),
#     unit price (right, 10, 2 dec), total (right, 12, 2 dec)
#   - Subtotal, tax (23%), total - all right-aligned
#   - All money amounts with comma separator and 2 decimal places
#   - Use separator lines appropriately

company = "BioTech Solutions Sp. z o.o."
invoice_num = "INV-2024-00142"
date = "2024-03-15"

items = [
    ("Python Programming Course",  1, 299.00),
    ("Lab Equipment - Set A",      2, 149.99),
    ("DNA Sequencing Kit",         5,  89.50),
    ("Bioinformatics Software",    1, 599.00),
    ("Lab Notebook (pack of 10)", 3,  24.99),
]

tax_rate = 0.23



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Multi-part challenge: dynamic report system.
#
# Part A: Progress bar
# Build a text progress bar using .format().
# The bar should be 40 characters wide.
# Format: [████████████████████░░░░░░░░░░░░░░░░░░░░] 50.0% (50/100)
# Generate bars for: 0%, 25%, 50%, 75%, 100%
# All percentage values right-aligned in width 6, 1 decimal.
#
# Part B: Alignment puzzle
# Using ONLY .format() (no f-strings, no concatenation):
# Create this exact output (verify character by character):
# ┌─────────────────────────────────┐
# │       PYTHON IS AMAZING         │
# │  Left   │  Center  │    Right   │
# │ ◄text   │  text    │      text► │
# └─────────────────────────────────┘
# Hint: use fill characters, width, and alignment creatively.
#
# Part C: Number formatting showcase
# For the number 9876543.21, print it formatted as:
#   - Plain integer (no decimals)
#   - With 2 decimal places
#   - With comma separator and 2 decimals
#   - In scientific notation (3 decimal places)
#   - As percentage (treat as ratio: 9876543.21 is the value)
#   - As binary (convert to int first)
#   - As hexadecimal (convert to int first)
#   - Right-aligned in width 25, with . as fill, 2 decimal places
# Print each on its own line with a label (left-aligned in width 30).
#
# Part D: Template reuse demonstration
# Create ONE template string that can generate BOTH:
#   1. A CSV line: "Anna,25,Warsaw,94.3%"
#   2. A display line: "| Anna             |  25 | Warsaw     | 94.3% |"
# Hint: you'll need TWO different templates but can store
# the DATA in variables and reuse across both templates.
# Show that .format() separates DATA from PRESENTATION.