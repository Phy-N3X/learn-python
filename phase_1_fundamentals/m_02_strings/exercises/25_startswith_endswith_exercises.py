# ============================================================
# MODULE 02 | EXERCISES 25 - .startswith() and .endswith()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Use .startswith() and .endswith() on the strings below.
# BEFORE running, predict each result (True/False) as a comment.
# Then verify.

text = "Python programming is fun"

# Prediction: ?
print(text.startswith("Python"))
# Prediction: ?
print(text.startswith("python"))
# Prediction: ?
print(text.startswith("programming"))
# Prediction: ?
print(text.endswith("fun"))
# Prediction: ?
print(text.endswith("Fun"))
# Prediction: ?
print(text.endswith("is fun"))
# Prediction: ?
print(text.startswith(""))
# Prediction: ?
print(text.endswith(""))



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Check file types using .endswith().
# For each filename below, print what type of file it is.
# Use simple if/elif/else.
# Types to check: Python (.py), CSV (.csv), PDF (.pdf),
#                 Image (.jpg, .png), FASTA (.fasta)
# If none match: print "Unknown type"

file1 = "analysis.py"
file2 = "results.csv"
file3 = "report.pdf"
file4 = "photo.jpg"
file5 = "genome.fasta"
file6 = "archive.zip"
file7 = "diagram.png"



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate the TUPLE feature.
# For each string, check against multiple options using a tuple.
# Print the result and a short explanation.

# a) Check if url starts with any web protocol:
url1 = "https://www.example.com"
url2 = "ftp://files.example.com"
url3 = "http://old-site.com"
# Check against ("http://", "https://")

# b) Check if filename ends with any image extension:
files = ["photo.jpg", "data.csv", "image.PNG", "chart.jpeg"]
# Check each against (".jpg", ".jpeg", ".png", ".gif")

# c) Check if DNA ends with a stop codon:
sequences = ["ATGCCCGCATAA", "ATGCCCGCATAG",
             "ATGCCCGCATGA", "ATGCCCGCAAAA"]
# Check each against ("TAA", "TAG", "TGA")



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate case sensitivity and the .lower() workaround.
# For each case:
#   1. Check WITHOUT converting case (show it might fail)
#   2. Check WITH .lower() (show it works reliably)
# Write comments explaining what you observe.

filename1 = "REPORT.PDF"
filename2 = "Genome.FASTA"
filename3 = "Data.CSV"

# Check each ends with lowercase extension (.pdf, .fasta, .csv)



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Use .startswith() to check URL protocols.
# Given the URLs below, classify each as:
#   "Secure"   → starts with "https://"
#   "Insecure" → starts with "http://"
#   "FTP"      → starts with "ftp://"
#   "Other"    → anything else
# Print: "url → classification"

url1 = "https://www.python.org"
url2 = "http://old-website.com"
url3 = "ftp://files.server.com"
url4 = "mailto:anna@example.com"
url5 = "https://api.github.com"
url6 = "file:///home/user/doc.txt"



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# DNA codon analysis using .startswith() and .endswith().
# For each DNA sequence:
#   a) Check if it has a start codon (starts with "ATG")
#   b) Check if it has a stop codon (ends with "TAA", "TAG", or "TGA")
#   c) Check if length is divisible by 3
#   d) Print "VALID ORF" if all three are True, else "INVALID"
#      (ORF = Open Reading Frame)

seq1 = "ATGCCCGCATAA"
seq2 = "ATGCCCGCATAG"
seq3 = "ATGCCCGCATGA"
seq4 = "ATGCCCGCAAAA"
seq5 = "CCCGCATAATAA"
seq6 = "ATGCCCGCATA"



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use start and end parameters with .startswith()/.endswith().
# Given: text = "Hello World Python"
#
# Part A: Check if characters [6:11] start with "World"
# Part B: Check if characters [0:5] end with "Hello"
# Part C: Check if characters [12:] start with "Python"
# Part D: Check if characters [0:11] end with "World"
#
# For each: predict first, then verify.

text = "Hello World Python"



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Combine .startswith() and .endswith() with boolean logic.
# For each condition below, write the check and print the result.
# Use 'and', 'or', 'not' as appropriate.

filename = "genome_data_2024.fasta"
url = "https://api.university.edu/data"
dna = "ATGCCCGCATAG"

# a) filename starts with "genome" AND ends with ".fasta"
# b) filename starts with "data" OR starts with "genome"
# c) filename does NOT end with ".pdf"
# d) url starts with "https://" AND ends with "/data"
# e) dna starts with "ATG" AND ends with any stop codon
# f) url starts with "https://" AND (".edu" in url)



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a file type classifier using tuple in .endswith().
# Given a list of filenames, separate them into categories.
# Print each category with its files.
#
# Categories:
#   bioinformatics: .fasta, .fastq, .fa, .bam, .vcf, .sam
#   data:           .csv, .tsv, .json, .xml, .xlsx
#   code:           .py, .js, .java, .cpp, .c, .r
#   document:       .pdf, .docx, .doc, .txt, .md
#   image:          .jpg, .jpeg, .png, .gif, .svg
#   other:          anything else

files = [
    "genome.fasta", "results.csv", "analysis.py",
    "report.pdf", "photo.jpg", "reads.fastq",
    "data.json", "script.r", "diagram.svg",
    "thesis.docx", "variants.vcf", "archive.zip",
    "notes.txt", "config.xml", "unknown.xyz",
    "assembly.fa", "code.java", "image.PNG"
]



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Command-line argument parser using .startswith().
# Given the list of "command line arguments" below:
# Categorize each argument:
#   - Starts with "--": long option (e.g., "--verbose")
#   - Starts with "-" but not "--": short option (e.g., "-v")
#   - Starts with digit or letter (not -): positional argument
# Print each category with its arguments.

args = [
    "--verbose", "-v", "input.fasta",
    "--output", "-o", "results.csv",
    "--threads", "-t", "4",
    "genome.fa", "--help", "-h",
    "--format", "json", "-q"
]



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Investigate edge cases. For each case:
# Predict the output BEFORE running, then verify.
# Write a comment explaining WHY the result is what it is.

# Case 1: prefix longer than string
short = "Hi"
# Prediction: ?
print(short.startswith("Hello World"))

# Case 2: empty prefix/suffix
word = "Python"
# Prediction: ?
print(word.startswith(""))
# Prediction: ?
print(word.endswith(""))

# Case 3: exact match
word = "Python"
# Prediction: ?
print(word.startswith("Python"))
# Prediction: ?
print(word.endswith("Python"))

# Case 4: using list instead of tuple (error!)
word = "hello.py"
extensions = [".py", ".js"]
# What happens when you run this?
# Predict, write as comment, then try:
# print(word.endswith(extensions))

# Case 5: tuple with empty string
word = "Hello"
# Prediction: ?
print(word.startswith(("", "H")))
# Prediction: ?
print(word.startswith(("x", "")))



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL errors and unexpected behaviors in the code below.
# Write a comment for each line explaining what's wrong
# or surprising. Then fix all actual errors.

text = "Hello World Python"

print(text.Startswith("Hello"))         # Error: ?
print(text.startswith("hello"))         # Surprising? Explain.
print(text.endswith(["World", "Python"])) # Error: ?
print(text.startswith("Hello", "World")) # Error: ?

result = text.startswith("Hello")
if result == "True":                    # Logic error: ?
    print("Starts with Hello!")

# What does this print and why?
print("Python".startswith("Python"))    # Prediction: ?
print("Python".endswith("Python"))      # Prediction: ?



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Python code analyzer using .startswith() and .endswith().
# Given the code snippet below (as a multi-line string):
# Analyze each line and categorize it.
#
# Categories (check in this order):
#   1. Empty line (after strip): "EMPTY"
#   2. Comment line (starts with # after strip): "COMMENT"
#   3. Function definition (starts with "def "): "FUNCTION DEF"
#   4. Class definition (starts with "class "): "CLASS DEF"
#   5. Import statement (starts with "import " or "from "): "IMPORT"
#   6. Return statement (starts with "return "): "RETURN"
#   7. Decorator (starts with "@"): "DECORATOR"
#   8. Anything else: "CODE"
#
# Print: "Line X: CATEGORY | content"

code = """import os
from pathlib import Path

# This is a comment

class MyClass:
    def __init__(self):
        self.value = 42

    @staticmethod
    def hello():
        # Say hello
        return "Hello World"

x = 10
print(x)
"""



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a comprehensive URL validator and parser.
#
# Given a URL, perform these checks and extractions:
#
# Part A: Validation
#   1. Starts with valid protocol: ("http://", "https://", "ftp://")
#   2. Does NOT start with "http://" (must use https or ftp for security)
#      → print warning if it does
#   3. Ends with a valid TLD from this list:
#      (".com", ".org", ".edu", ".gov", ".net", ".io", ".pl")
#      OR ends with common path extensions:
#      ("/", "/data", "/api")
#   4. Contains "www." after the protocol (optional - just check and report)
#
# Part B: Extraction (using .find() + slicing + .startswith()/.endswith())
#   1. Extract the protocol
#   2. Extract the domain (between "://" and next "/")
#   3. Check if domain ends with ".edu" → print "Academic resource"
#   4. Check if domain ends with ".gov" → print "Government resource"
#
# Test with these URLs:
url1 = "https://www.python.org/docs/"
url2 = "http://old-site.com"
url3 = "https://api.university.edu/data"
url4 = "ftp://files.government.gov"
url5 = "https://github.io/project"



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Multi-part challenge: comprehensive bioinformatics validator.
#
# Part A: ORF (Open Reading Frame) Validator
# An ORF must:
#   1. Start with ATG (start codon)
#   2. End with TAA, TAG, or TGA (stop codon)
#   3. Have length divisible by 3
#   4. Contain ONLY A, T, G, C (uppercase)
#   5. The stop codon must be at the END (not in the middle)
#      → just check condition 2 for now
# Validate all sequences and print detailed report.

sequences = [
    "ATGCCCGCATAA",       # valid
    "ATGCCCGCATAG",       # valid
    "atgcccgcataa",       # invalid: lowercase
    "ATGCCCGCATA",        # invalid: not divisible by 3
    "CCCGCATAATAA",       # invalid: no start
    "ATGCCCGCAAAA",       # invalid: no stop
    "ATGCCCGCATGCCC",     # invalid: no stop (but has ATG in middle)
    "ATGAAATGA",          # valid: TGA stop
]

# Part B: Primer Validator
# A PCR primer must:
#   1. Be 18-25 nucleotides long
#   2. Start with G or C (stronger binding at 5' end)
#   3. End with G or C (stronger binding at 3' end)
#   4. NOT start with more than 3 of the same nucleotide
#      → check: not primer.startswith("AAAA") etc.
# Validate these primers:

primers = [
    "GCATCGATCGATCGATCG",    # valid?
    "ATATATATATATATATAT",    # valid?
    "GCATCGATCG",            # valid?
    "GCATCGATCGATCGATCGAAA", # valid?
    "AAAAGCATCGATCGATCGAT",  # valid?
    "CATCGATCGATCGATCGC",    # valid?
]

# Part C: File naming convention checker
# Bioinformatics files should follow naming conventions:
#   - Sample files: start with "sample_", end with ".fastq" or ".fasta"
#   - Result files: start with "result_", end with ".csv" or ".tsv"
#   - Report files: start with "report_", end with ".pdf" or ".html"
#   - Reference files: start with "ref_", end with ".fa" or ".fasta"
# Check each filename and print whether it follows convention.

bio_files = [
    "sample_001.fastq",
    "result_analysis.csv",
    "report_final.pdf",
    "ref_genome.fa",
    "sample_001.csv",       # wrong extension for sample
    "data_result.tsv",      # wrong prefix for result
    "report_summary.docx",  # wrong extension for report
    "genome.fasta",         # no convention prefix
]