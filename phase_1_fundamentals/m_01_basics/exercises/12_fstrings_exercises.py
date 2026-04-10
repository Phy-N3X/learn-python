# ============================================================
# MODULE 01 | EXERCISES 12 - F-Strings
# ============================================================
# 15 exercises - f-strings only
# Allowed from previous lectures: everything from 01-11
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Basic f-string syntax.
# Given:
#   name    = "Alice"
#   age     = 28
#   height  = 1.68
#   city    = "Gdansk"
#   active  = True
#
# Using ONLY f-strings, print:
#   1. "Name: Alice"
#   2. "Alice is 28 years old."
#   3. "Height: 1.68m"
#   4. "Alice lives in Gdansk."
#   5. "Active: True"
#   6. All info in ONE f-string, multiple lines (use \n or triple quotes)
#   7. "Alice" in curly braces: "{Alice}"
#      Hint: use {{ }} to print literal braces



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Expressions inside f-strings.
# Given:
#   a = 15
#   b = 4
#   name = "python programming"
#
# Using f-strings with EXPRESSIONS inside {} (no variables):
#   1. Print sum, difference, product, quotient of a and b
#   2. Print a**b
#   3. Print a % b
#   4. Print name in title case
#   5. Print name in uppercase
#   6. Print length of name
#   7. Print whether a > b (True/False)
#   8. Print "even" or "odd" for a using ternary in {}
#   9. Print first 6 chars of name using slicing in {}
#   10. Print name reversed using slicing in {}



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Float formatting.
# Given: pi = 3.14159265358979
#
# Print pi formatted as:
#   1. Default (no format)
#   2. 0 decimal places
#   3. 2 decimal places
#   4. 5 decimal places
#   5. Width 15, 2 decimal places, right-aligned
#   6. Width 15, 2 decimal places, left-aligned
#   7. Width 15, 2 decimal places, centered
#   8. Zero-padded, width 12, 4 decimal places
#   9. Scientific notation, 3 decimal places
#   10. As percentage (pi * 100 makes no sense but shows syntax)
#       Print 0.314159 as percentage instead



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Integer formatting.
# Given: n = 255
#
# Print n as:
#   1. Decimal (default)
#   2. Binary
#   3. Octal
#   4. Hex lowercase
#   5. Hex uppercase
#   6. Binary with 0b prefix
#   7. Hex with 0x prefix
#   8. Zero-padded decimal, width 8
#   9. With + sign always shown
#   10. With thousands separator (use 1234567 for this one)



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# String alignment and fill.
# Given: word = "Python"
#
# Print word formatted as (width = 20 for all):
#   1. Left-aligned (default)
#   2. Right-aligned
#   3. Centered
#   4. Left-aligned, fill with "."
#   5. Right-aligned, fill with "."
#   6. Centered, fill with "-"
#   7. Centered, fill with "="
#   8. Truncated to 3 characters
#   9. Width 20, truncated to 3 (combined)
#   10. Right-aligned, width 20, truncated to 3
#
# After each line, verify length == 20 using len()
# (except truncation examples)



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Debug format with =.
# Given:
#   x      = 42
#   name   = "Alice"
#   pi     = 3.14159
#   scores = [85, 92, 78]
#   active = True
#
# Use f"{variable=}" to print each.
# Then also print:
#   1. f"{x * 2=}"
#   2. f"{name.upper()=}"
#   3. f"{len(scores)=}"
#   4. f"{sum(scores)=}"
#   5. f"{sum(scores)/len(scores)=:.2f}"
#   6. f"{active and x > 40=}"
#   7. f"{x=:08b}"  ← debug AND format combined
#   8. f"{pi=:.4f}"



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a formatted table using f-strings.
#
# data = [
#     ("Alice",   22, "Warsaw",  98.5,  True),
#     ("Bob",     30, "Krakow",  87.25, False),
#     ("Charlie", 22, "Gdansk",  95.0,  True),
#     ("Diana",   28, "Poznan",  91.75, True),
#     ("Edward",  35, "Wroclaw", 72.3,  False),
# ]
#
# Print this EXACT table:
# ┌───────────┬─────┬──────────┬────────┬────────┐
# │ Name      │ Age │ City     │  Score │ Active │
# ├───────────┼─────┼──────────┼────────┼────────┤
# │ Alice     │  22 │ Warsaw   │  98.50 │ True   │
# │ Bob       │  30 │ Krakow   │  87.25 │ False  │
# │ Charlie   │  22 │ Gdansk   │  95.00 │ True   │
# │ Diana     │  28 │ Poznan   │  91.75 │ True   │
# │ Edward    │  35 │ Wroclaw  │  72.30 │ False  │
# └───────────┴─────┴──────────┴────────┴────────┘
#
# Use f-strings for ALL formatting.
# Column widths: Name=9, Age=3, City=8, Score=6, Active=6



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# Nested f-strings - dynamic formatting.
#
# Given:
#   values = [3.14159, 2.71828, 1.41421, 1.73205]
#   labels = ["Pi", "Euler's e", "Sqrt(2)", "Sqrt(3)"]
#
# Part A: Print each value with 1, 2, 3, 4 decimal places
# using a VARIABLE for precision (nested f-string):
#   for precision in range(1, 5):
#       for label, value in zip(labels, values):
#           print(f"{label:<12} = {value:.{precision}f}")
#   (add blank line between precision groups)
#
# Part B: Print each value centered in a field
# where the width comes from a variable:
#   for width in [10, 15, 20]:
#       print all 4 values centered in that width
#       using f"{value:^{width}.2f}"
#
# Part C: Dynamic fill character:
#   fills = ["*", "-", "=", "."]
#   for fill, label in zip(fills, labels):
#       print f"{label:{fill}^20}"



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Conversion flags !r !s !a.
#
# Given:
#   text1 = "hello\nworld\ttab"
#   text2 = "Zażółć gęślą jaźń"   ← Polish chars
#   text3 = "normal text"
#   num   = 42
#   none  = None
#
# For each value print ALL THREE flags (!s, !r, !a):
#   text1:
#     !s: hello
#         world   tab
#     !r: 'hello\nworld\ttab'
#     !a: 'hello\nworld\ttab'
#   ...
#
# Write a comment after each explaining:
# "!r is useful for debugging because..."
# "!a is useful for..."
# "When would you use !r over just printing the value?"



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a receipt generator using f-strings.
#
# items = [
#     ("Python Course",      149.99, 1),
#     ("BioPython Book",      59.99, 2),
#     ("Jupyter Notebook",    19.99, 3),
#     ("NumPy Tutorial",      39.99, 1),
#     ("VS Code Extension",    9.99, 5),
# ]
# tax_rate = 0.23   # 23% VAT
#
# Generate this EXACT receipt:
#
# ============================================
#            PYTHON STORE RECEIPT
# ============================================
# Item                   Price  Qty    Total
# --------------------------------------------
# Python Course         149.99    1   149.99
# BioPython Book         59.99    2   119.98
# Jupyter Notebook       19.99    3    59.97
# NumPy Tutorial         39.99    1    39.99
# VS Code Extension       9.99    5    49.95
# --------------------------------------------
# Subtotal:                             419.88
# VAT (23%):                             96.57
# TOTAL:                                516.45
# ============================================
# Thank you for your purchase!
# Items: 5 products, 12 units total
# ============================================
#
# All numbers formatted with 2 decimal places.
# Use f-strings for EVERYTHING.



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Progress bar generator using f-strings.
#
# Write a function display_progress(current, total, width=20)
# with full docstring that prints:
#
#   Progress: [████████████░░░░░░░░]  60% (60/100)
#
# Where:
#   ████ = filled portion (use "█" \u2588)
#   ░░░░ = empty portion  (use "░" \u2591)
#   width = total bar width in characters
#
# Test with:
#   display_progress(0,   100)
#   display_progress(25,  100)
#   display_progress(50,  100)
#   display_progress(75,  100)
#   display_progress(100, 100)
#   display_progress(3,   7)     ← non-round numbers
#   display_progress(1,   3, width=30)
#
# Expected output format (width=20):
#   Progress: [░░░░░░░░░░░░░░░░░░░░]   0% (0/100)
#   Progress: [█████░░░░░░░░░░░░░░░]  25% (25/100)
#   Progress: [██████████░░░░░░░░░░]  50% (50/100)
#   Progress: [███████████████░░░░░]  75% (75/100)
#   Progress: [████████████████████] 100% (100/100)
#
# Use f-strings for ALL formatting including the percentage.



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Scientific report generator.
#
# Given DNA analysis results:
# sequences = [
#     {"id": "SEQ001", "organism": "E. coli",
#      "length": 4639221, "gc": 0.508, "valid": True},
#     {"id": "SEQ002", "organism": "H. sapiens chr1",
#      "length": 248956422, "gc": 0.413, "valid": True},
#     {"id": "SEQ003", "organism": "S. cerevisiae",
#      "length": 12157105, "gc": 0.381, "valid": True},
#     {"id": "SEQ004", "organism": "P. falciparum",
#      "length": 23264338, "gc": 0.193, "valid": False},
# ]
#
# Generate this scientific report:
#
# ════════════════════════════════════════════════════════════
#                    DNA SEQUENCE ANALYSIS REPORT
#                    Generated: 2025-01-15 14:30:00
# ════════════════════════════════════════════════════════════
#
#  ID      │ Organism         │      Length │   GC% │ Valid
# ─────────┼──────────────────┼─────────────┼───────┼───────
#  SEQ001  │ E. coli          │   4,639,221 │ 50.8% │  ✓
#  SEQ002  │ H. sapiens chr1  │ 248,956,422 │ 41.3% │  ✓
#  SEQ003  │ S. cerevisiae    │  12,157,105 │ 38.1% │  ✓
#  SEQ004  │ P. falciparum    │  23,264,338 │ 19.3% │  ✗
# ─────────┴──────────────────┴─────────────┴───────┴───────
#
# SUMMARY:
#   Total sequences : 4
#   Valid sequences : 3 (75.0%)
#   Average length  : 72,157,771.5 bp
#   Average GC%     : 37.4%
#   Longest         : H. sapiens chr1 (248,956,422 bp)
#   Shortest        : E. coli (4,639,221 bp)
# ════════════════════════════════════════════════════════════
#
# Use f-strings with format specifiers throughout.
# Use datetime.datetime.now() for the timestamp.



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# F-string edge cases and advanced patterns.
#
# Part A: Escape and quote challenges.
# Print each EXACTLY (including the curly braces and quotes):
#   1. The variable {name} contains: Alice
#   2. f-string syntax: f"{expression}"
#   3. Dictionary: {'key': 'value'}
#   4. Set: {1, 2, 3}
#
# Part B: Complex expressions in f-strings.
# Given: numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6]
#   1. Print max using max() inside {}
#   2. Print min using min() inside {}
#   3. Print sum using sum() inside {}
#   4. Print average: sum/len inside {}
#   5. Print sorted list using sorted() inside {}
#   6. Print count of evens using sum(n%2==0 for n in numbers) inside {}
#
# Part C: Conditional formatting.
# Given: values = [-5, 0, 3, -12, 7, -1, 15]
# For each value, print with:
#   - "+" prefix and green-ish marker if positive
#   - "-" prefix and red-ish marker if negative
#   - "0" prefix and neutral marker if zero
# Format: "[+] +7  │ [0]  0  │ [-] -5 "
# Use ternary inside f-string.



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a complete f-string formatting library.
# Write functions with full docstrings.
#
#   format_currency(amount, symbol="$", decimals=2)
#     → "$1,234.56"  or  "€9.99"
#
#   format_percentage(ratio, decimals=1, show_sign=False)
#     → "85.0%"  or  "+12.5%" (with sign)
#
#   format_scientific(number, decimals=3)
#     → "6.022e+23"
#
#   format_filesize(bytes)
#     → "1.23 KB" or "4.56 MB" or "7.89 GB"
#     Thresholds: KB=1024, MB=1024², GB=1024³
#
#   format_duration(seconds)
#     → "2h 30m 45s" or "45m 00s" or "30s"
#     Only show hours if > 0, only show minutes if > 0
#
#   format_table_row(*values, widths, alignments)
#     → formatted row string with | separators
#     alignments: list of "<", ">", "^"
#
# Test each function with at least 5 different inputs.
# Print a test table showing input → output.



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Complete dashboard generator.
# Combine EVERYTHING from module 01 with f-string formatting.
#
# You have system monitoring data:
# cpu_usage    = 67.3          # percent
# memory_used  = 6_442_450_944 # bytes (6GB)
# memory_total = 17_179_869_184# bytes (16GB)
# disk_used    = 256_060_514_304# bytes
# disk_total   = 512_110_190_592# bytes
# processes    = 247
# uptime_secs  = 359462        # seconds
# temperature  = 68.5          # Celsius
# network_in   = 1_234_567     # bytes/sec
# network_out  = 567_890       # bytes/sec
# errors_today = 3
# warnings     = 17
#
# Generate this EXACT dashboard:
#
# ╔══════════════════════════════════════════════════════════╗
# ║                  SYSTEM MONITOR v1.0                    ║
# ║                  2025-01-15  14:30:00                   ║
# ╠══════════════════════════════════════════════════════════╣
# ║  CPU USAGE                                              ║
# ║  [███████████████░░░░░░░░░░░░░░]  67.3%               ║
# ╠══════════════════════════════════════════════════════════╣
# ║  MEMORY                                                 ║
# ║  Used:  6.00 GB / 16.00 GB                             ║
# ║  [███████████████████░░░░░░░░░░]  37.5%               ║
# ╠══════════════════════════════════════════════════════════╣
# ║  DISK                                                   ║
# ║  Used:  238.47 GB / 476.84 GB                          ║
# ║  [███████████████░░░░░░░░░░░░░░]  50.0%               ║
# ╠══════════════════════════════════════════════════════════╣
# ║  NETWORK                 SYSTEM                        ║
# ║  ↓ In:  1.18 MB/s        Processes: 247               ║
# ║  ↑ Out: 554.58 KB/s      Uptime:    4d 3h 51m 2s     ║
# ║                          Temp:      68.5°C  ✓         ║
# ╠══════════════════════════════════════════════════════════╣
# ║  STATUS: ⚠  3 errors │ 17 warnings today              ║
# ╚══════════════════════════════════════════════════════════╝
#
# Requirements:
#   - All bytes converted to KB/MB/GB automatically
#   - Progress bars width = 30 chars
#   - Uptime broken into days, hours, minutes, seconds
#   - Temperature marked ✓ if < 80°C, ✗ if >= 80°C
#   - Use datetime.datetime.now() for timestamp
#   - ALL formatting done with f-strings

