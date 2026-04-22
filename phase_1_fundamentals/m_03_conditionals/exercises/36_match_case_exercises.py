# ============================================================
# MODULE 03 | EXERCISES 36 - match / case
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Write a match/case statement that matches a day number
# (1-7) and prints the corresponding day name.
#
# Create variable: day_number = 3
# Test with at least 3 different values.
#
# Expected output (day_number = 3):
# Wednesday
#
# Expected output (day_number = 7):
# Sunday
#
# Expected output (day_number = 9):
# Invalid day number - please enter 1 to 7

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what each match/case block will print.
# Write your prediction as a comment.
# Then run and verify.
#
# x = 5
#
# match x:
#     case 1:
#         print("A")     # prediction: ?
#     case 5:
#         print("B")     # prediction: ?
#     case 10:
#         print("C")     # prediction: ?
#     case _:
#         print("D")     # prediction: ?
#
# ---
#
# y = "hello"
#
# match y:
#     case "world":
#         print("E")     # prediction: ?
#     case "hello" | "hi":
#         print("F")     # prediction: ?
#     case _:
#         print("G")     # prediction: ?
#
# ---
#
# z = None
#
# match z:
#     case None:
#         print("H")     # prediction: ?
#     case 0:
#         print("I")     # prediction: ?
#     case _:
#         print("J")     # prediction: ?
#
# Final question (answer as comment):
# In the first block, why doesn't case 10 or case _ run?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL errors in the match/case code below.
# Write what each error is as a comment next to the line.
# Then fix all errors so the code runs correctly.
#
# command = "start"
#
# match command
#     case "start":
#         print("Starting")
#     case "stop"
#         print("Stopping")
#     case _:
#         print("Unknown")
#     case "pause":
#         print("Pausing")
#
# ---
#
# score = 85
#
# match score:
#     case score >= 90:
#         print("A")
#     case score >= 80:
#         print("B")
#     case _:
#         print("Other")

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Build an HTTP status code interpreter using match/case.
# Ask the user to enter a status code (as integer).
#
# Map these codes:
# 200 → "OK - Request successful ✅"
# 201 → "Created - New resource created ✅"
# 400 → "Bad Request - Check your input ❌"
# 401 → "Unauthorized - Login required 🔒"
# 403 → "Forbidden - Access denied 🚫"
# 404 → "Not Found - Resource doesn't exist ❌"
# 500 → "Internal Server Error 🔥"
# 503 → "Service Unavailable - Try again later ⏳"
# anything else → "Unknown status code: [code]"
#
# Example interaction 1:
# Enter status code: 404
# 404: Not Found - Resource doesn't exist ❌
#
# Example interaction 2:
# Enter status code: 418
# Unknown status code: 418

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Create a DNA base complement finder using match/case.
# Ask the user to enter a DNA base (A, T, C, or G).
# Convert to uppercase.
#
# Use match/case to find the complement:
# A → T
# T → A
# C → G
# G → C
# anything else → "Invalid base"
#
# Also print whether the base is a purine (A, G)
# or pyrimidine (T, C) using a SECOND match/case.
#
# Example interaction 1:
# Enter DNA base: a
# Base: A
# Complement: T
# Type: Purine
#
# Example interaction 2:
# Enter DNA base: X
# Base: X
# ❌ Invalid DNA base

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a calculator using match/case.
# Ask the user for:
# - First number (float)
# - Operator: +, -, *, /, %, ** (also accept words: add, sub, etc.)
# - Second number (float)
#
# Use match/case on the operator.
# Handle division by zero separately.
# Print the result formatted to 4 decimal places.
#
# Operator mapping (use | for alternatives):
# "+" or "add"      → addition
# "-" or "sub"      → subtraction
# "*" or "mul"      → multiplication
# "/" or "div"      → division (check for zero!)
# "%" or "mod"      → modulo
# "**" or "pow"     → power
# anything else     → "Unknown operator"
#
# Example interaction:
# First number: 10
# Operator: **
# Second number: 3
# 10.0 ** 3.0 = 1000.0000

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create an amino acid classifier using match/case.
# Ask user for a single-letter amino acid code.
# Convert to uppercase.
#
# Match against these groups:
# Nonpolar aliphatic: G, A, V, L, I, P, M
# Aromatic:           F, W, Y
# Polar uncharged:    S, T, C, N, Q
# Positively charged: K, R, H
# Negatively charged: D, E
# Special (START):    M (Methionine - also START codon)
#
# Note: M appears in two groups - handle it specifically first!
# Print: amino acid code, full name, chemical group, charge at pH 7.
#
# Chemical group names:
# Nonpolar → "Hydrophobic"
# Polar uncharged → "Hydrophilic (neutral)"
# Positive → "Basic (+1)"
# Negative → "Acidic (-1)"
# Aromatic → "Aromatic (varies)"
#
# Example interaction:
# Enter amino acid code: K
# Code: K
# Name: Lysine
# Group: Positively charged
# Character: Basic (+1)
# Note: Essential amino acid

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a coordinate system analyzer using match/case
# with TUPLE patterns.
#
# Ask user for x and y coordinates (integers).
# Create a tuple: point = (x, y)
#
# Use match/case with tuple patterns to classify:
# (0, 0)  → "Origin point"
# (x, 0)  → "Point on X-axis at x=[value]"
# (0, y)  → "Point on Y-axis at y=[value]"
# (x, y) where x > 0 and y > 0 → "Quadrant I (++)"
# (x, y) where x < 0 and y > 0 → "Quadrant II (-+)"
# (x, y) where x < 0 and y < 0 → "Quadrant III (--)"
# (x, y) where x > 0 and y < 0 → "Quadrant IV (+-)"
#
# Also calculate and print:
# - Distance from origin (√(x²+y²)) rounded to 2 decimal places
# - Which axis is closer to (X or Y or equal)
#
# Example interaction:
# Enter x: 3
# Enter y: -4
# Quadrant IV (+-)
# Distance from origin: 5.00
# Closer to Y-axis

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this match/case code and predict outputs.
# Write predictions as comments BEFORE each print.
# Then run and verify.
#
# values = [0, 1, -5, 100, "hello", None, True, 3.14]
#
# for val in values:
#     match val:
#         case None:
#             # prediction for None: ?
#             print(f"{val!r} → None type")
#         case True | False:
#             # prediction for True: ?
#             print(f"{val!r} → Boolean")
#         case 0:
#             # prediction for 0: ?
#             print(f"{val!r} → Zero integer")
#         case int():
#             # prediction for 1, -5, 100: ?
#             print(f"{val!r} → Integer")
#         case float():
#             # prediction for 3.14: ?
#             print(f"{val!r} → Float")
#         case str():
#             # prediction for "hello": ?
#             print(f"{val!r} → String")
#         case _:
#             print(f"{val!r} → Unknown type")
#
# Answer as comments:
# Why does True match 'case True | False' before 'case int()'?
# Why does 0 have its own case before 'case int()'?
# What does {val!r} do in the f-string?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a codon to amino acid translator using match/case.
# A codon is a 3-letter DNA sequence.
#
# Ask user for a 3-letter codon.
# Convert to uppercase.
# Validate: must be exactly 3 chars containing only A/T/C/G.
#
# Use match/case to translate (implement at least 15 codons):
# ATG → Methionine (Met) - START
# TAA, TAG, TGA → STOP codon
# GCT, GCC, GCA, GCG → Alanine (Ala)
# TGT, TGC → Cysteine (Cys)
# GAT, GAC → Aspartic acid (Asp)
# GAA, GAG → Glutamic acid (Glu)
# TTT, TTC → Phenylalanine (Phe)
# GGT, GGC, GGA, GGG → Glycine (Gly)
# CAT, CAC → Histidine (His)
# AAA, AAG → Lysine (Lys)
# anything else → "Codon not in database"
#
# Print:
# - Codon entered
# - Amino acid (or STOP/unknown)
# - Whether it's START, STOP, or coding
# - For valid amino acids: one property (e.g. polarity)
#
# Example interaction:
# Enter codon: ggg
# Codon: GGG
# Amino acid: Glycine (Gly)
# Type: Coding codon
# Property: Nonpolar, smallest R-group after Alanine

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a Roman numeral converter using match/case.
# Convert Arabic numbers (1-20) to Roman numerals.
#
# Ask user for a number between 1 and 20.
# Validate: must be an integer between 1 and 20.
#
# Use match/case to convert:
# 1→I, 2→II, 3→III, 4→IV, 5→V, 6→VI, 7→VII, 8→VIII,
# 9→IX, 10→X, 11→XI, 12→XII, 13→XIII, 14→XIV, 15→XV,
# 16→XVI, 17→XVII, 18→XVIII, 19→XIX, 20→XX
#
# Also use a SECOND match/case to classify the Roman numeral:
# I, V, X → "Basic symbol"
# Anything with IV or IX → "Subtractive notation"
# Anything else → "Additive notation"
#
# Print both the Roman numeral and its classification.
#
# Example interaction:
# Enter number (1-20): 9
# Arabic: 9
# Roman: IX
# Type: Subtractive notation
# Fun fact: IX means "one before ten"

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a lab instrument status monitor using match/case.
# Each instrument reports a status code (string).
#
# Instrument codes and their meanings:
# "READY"       → "✅ Ready for operation"
# "BUSY"        → "⏳ Currently processing - please wait"
# "DONE"        → "✅ Analysis complete - retrieve sample"
# "ERR_CAL"     → "⚠ Calibration error - recalibrate instrument"
# "ERR_TEMP"    → "🌡 Temperature out of range"
# "ERR_CONN"    → "🔌 Connection lost - check cables"
# "ERR_SAMPLE"  → "🧪 Sample error - check sample quality"
# "MAINT"       → "🔧 Maintenance mode - do not operate"
# "STANDBY"     → "💤 Standby mode - press power to activate"
# "LOW_BAT"     → "🔋 Low battery - connect to power"
# Any "ERR_*"   → "❌ Unknown error code - contact support"
# Anything else → "❓ Unrecognized status code"
#
# Ask user for status code (convert to uppercase).
# Print status meaning, priority level, and recommended action.
#
# Priority levels (use a second match/case or guard):
# ERR codes → HIGH
# MAINT, BUSY → MEDIUM
# READY, DONE, STANDBY → LOW
# LOW_BAT → MEDIUM
#
# Example interaction:
# Enter instrument status code: err_temp
# Status: ERR_TEMP
# Meaning: 🌡 Temperature out of range
# Priority: HIGH
# Action: Check cooling system and ambient temperature immediately

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a sequence type analyzer using match/case
# with LIST PATTERNS.
#
# The function receives different types of sequence data.
# Use match/case to handle different lengths and structures.
#
# Test with these inputs (store as variables, then match each):
# seq1 = []
# seq2 = [42]
# seq3 = ["ATG", "GCT", "TAA"]
# seq4 = [1, 2, 3, 4, 5]
# seq5 = ["header", 100, 200, 300, 400, 500]
#
# Match patterns:
# [] → "Empty sequence"
# [x] → "Single element: {x}"
# [x, y] → "Pair: {x} and {y}"
# [first, *middle, last] if len = 3 → use guard
# [first, *rest] where first is str → "Named sequence '{first}' with {len(rest)} data points"
# [first, *rest] → "Numeric sequence, {len(rest)+1} elements, first={first}"
#
# For each sequence also print:
# - Total length using len()
# - Type of first element (use type().__name__)
# - Whether all elements are same type (use a loop to check)
#
# Print a full analysis for each sequence.

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a scientific unit system dispatcher using match/case.
# This system converts values between different unit systems
# and routes to the appropriate converter based on unit type.
#
# Ask user for:
# - Value (float)
# - From unit (string)
# - To unit (string)
#
# Use match/case to determine unit CATEGORY first,
# then nested match/case for specific conversion:
#
# TEMPERATURE units: c, f, k, celsius, fahrenheit, kelvin
# MASS units: g, kg, lb, oz, mg, gram, kilogram, pound, ounce
# LENGTH units: m, km, cm, mm, mi, ft, in, inch, meter, mile, foot
# SPEED units: kmh, mph, ms, knot
# PRESSURE units: pa, kpa, bar, atm, psi
#
# Use match/case to:
# 1. First identify the category from the 'from_unit'
# 2. Then match the specific conversion pair (from → to)
#    using tuple pattern: case ("c", "f"):
# 3. Calculate and display result
# 4. Handle unknown units or unsupported conversions
#
# Implement at least 3 conversions per category.
# Print: original value + unit, result + unit, conversion formula used.
#
# Example interaction:
# Value: 100
# From: c
# To: f
# Category: Temperature
# Formula: (°C × 9/5) + 32
# 100.0°C = 212.0000°F
#
# Example interaction 2:
# Value: 70
# From: kg
# To: lb
# Category: Mass
# Formula: kg × 2.20462
# 70.0 kg = 154.3234 lb

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a comprehensive bioinformatics sequence router
# using match/case with multiple pattern types.
#
# The system receives different types of biological sequences
# and automatically determines what they are, then analyzes them.
#
# Ask user for a biological sequence (string).
# Clean it: strip whitespace, convert to uppercase.
#
# STEP 1 - DETERMINE SEQUENCE TYPE using match/case with guards:
# Use the composition of the sequence to classify:
#
# case seq if all chars in "ATCG" and "U" not in seq:
#     → DNA sequence
# case seq if all chars in "AUCG" and "T" not in seq:
#     → RNA sequence
# case seq if all chars in "ATCGU":
#     → Mixed/ambiguous nucleotide sequence
# case seq if all chars in "ACDEFGHIKLMNPQRSTVWY":
#     → Protein sequence (standard 20 amino acids)
# case seq if not seq:
#     → Empty sequence
# case _:
#     → Unknown/invalid characters detected (list which ones)
#
# STEP 2 - BASED ON TYPE, use a second match/case to analyze:
#
# For DNA:
# - Length and length category (< 100 = oligonucleotide, etc.)
# - GC content (%)
# - Has start codon ATG: yes/no
# - Has stop codon (TAA/TAG/TGA): yes/no
# - Complement sequence (A↔T, C↔G)
# - Reverse complement
#
# For RNA:
# - Length
# - GC content
# - Has start codon AUG: yes/no
# - Convert to DNA (U→T)
#
# For Protein:
# - Length in amino acids
# - Molecular weight estimate (length × 110 Da)
# - Has Methionine (M) - start signal: yes/no
# - Has Cysteine (C) - disulfide bonds possible: yes/no
# - Count of charged residues:
#   positive: K, R, H
#   negative: D, E
# - Estimated charge: "positive" / "negative" / "neutral"
#
# For Unknown:
# - List each invalid character found
# - Suggest what it might be (if mostly ATCG → maybe DNA with errors)
#
# Print a complete sequence analysis report
# with all results clearly labeled and formatted.
# ============================================================