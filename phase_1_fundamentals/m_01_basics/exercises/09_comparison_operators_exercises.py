# ============================================================
# MODULE 01 | EXERCISES 09 - Comparison Operators
# ============================================================
# 15 exercises - comparison operators only
# Allowed from previous lectures:
#   - variables, type()                 (lecture 01)
#   - numbers, math operators           (lecture 02)
#   - string methods, slicing           (lecture 03)
#   - bool, logical operators           (lecture 04)
#   - print(), f-strings                (lecture 05)
#   - input() patterns                  (lecture 06)
#   - comments and docstrings           (lecture 07)
#   - math operators, math module       (lecture 08)
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output of every comparison below.
# Write prediction as comment BEFORE running.
# If wrong, explain why in a comment.
#
# a = 15
# b = 15.0
# c = "15"
#
# a == b
# a == c
# a != b
# a != c
# b == float(c)
# type(a) == type(b)
# type(a) == type(c)
# isinstance(a, (int, float))
# isinstance(b, (int, float))
# isinstance(c, (int, float))



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict the string comparison results.
# Write prediction as comment BEFORE running.
# If wrong, look up Unicode values with ord() and explain.
#
# "apple"  == "apple"
# "apple"  == "Apple"
# "apple"  <  "banana"
# "banana" <  "apple"
# "abc"    <  "abd"
# "abc"    <  "abcd"
# "z"      >  "A"
# "Z"      <  "a"
# "9"      <  "10"
# ""       <  "a"
# "hello".lower() == "HELLO".lower()

# After predictions, print ord() for:
# "A", "Z", "a", "z", "0", "9"
# Write a comment explaining the ordering pattern.



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Chained comparisons - predict then verify.
# Write prediction as comment BEFORE running.
#
# x = 7
#
# 1 < x < 10
# 1 < x < 7
# 7 <= x <= 7
# 0 < x < 5
# 5 < x < 10
# 1 < x < x + 1
# x == 7 == 7
# x > 5 > 3
# 10 > x > 5
# 1 <= x <= 10 <= 100



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# is vs == investigation.
#
# Part A - predict True or False for each:
#
# a = [1, 2, 3]
# b = [1, 2, 3]
# c = a
#
# a == b
# a is b
# a == c
# a is c
# b is c
#
# Part B - None checks:
# x = None
# y = None
#
# x == None
# x is None
# x == y
# x is y
# x is not None
#
# Part C - integer caching:
# p = 5
# q = 5
# r = 1000
# s = 1000
#
# p is q     ← predict
# r is s     ← predict
# p == q     ← predict
# r == s     ← predict
#
# Write a comment explaining WHY p is q might be True
# but r is s might be False.



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Membership operators - predict then verify.
# Write prediction as comment BEFORE running.
#
# text   = "Hello World Python"
# fruits = ["apple", "banana", "cherry"]
# nums   = (1, 2, 3, 4, 5)
# info   = {"name": "Anna", "age": 25}
# chars  = {"A", "T", "G", "C"}
#
# "Hello"   in text
# "hello"   in text
# ""        in text
# "apple"   in fruits
# "Apple"   in fruits
# "mango"   not in fruits
# 3         in nums
# 6         not in nums
# "name"    in info
# "Anna"    in info
# "Anna"    in info.values()
# "A"       in chars
# "a"       in chars
# 5         in range(10)
# 10        in range(10)



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Float comparison pitfall and safe solution.
#
# 1. Print and show these are NOT equal with ==:
#    0.1 + 0.2  vs  0.3
#    1.1 + 2.2  vs  3.3
#    0.7 + 0.1  vs  0.8
#
# 2. For each pair, use math.isclose() to compare safely.
#    Print True/False for each.
#
# 3. Show NaN behavior:
#    nan = float("nan")
#    Print: nan == nan
#    Print: nan != nan
#    Print: math.isnan(nan)
#    Write a comment: why is NaN != NaN?
#
# 4. Show infinity comparisons:
#    Print: math.inf > 999999999999
#    Print: -math.inf < -999999999999
#    Print: math.inf == math.inf
#    Print: math.inf > math.inf



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a complete input validator using ONLY comparison
# operators and membership operators.
# No if statements - just True/False expressions!
#
# Given:
#   username = "anna_99"
#   password = "Secret123!"
#   age      = 20
#   score    = 85.5
#   grade    = "B"
#
# Calculate True/False for each rule:
#   username_length_ok   = length between 4 and 20
#   username_no_spaces   = " " not in username
#   password_long_enough = length >= 8
#   age_adult            = age >= 18
#   age_realistic        = 0 < age < 150
#   score_valid          = 0.0 <= score <= 100.0
#   grade_valid          = grade in ["A","B","C","D","F"]
#   score_grade_match    = (score >= 80) == (grade in ["A","B"])
#
# Print each rule result with a label.
# Then print overall: all_valid = all rules are True
# Hint: use and to combine all boolean variables



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# DNA sequence validator using membership operators.
#
# valid_dna_chars = {"A", "T", "G", "C"}
# valid_rna_chars = {"A", "U", "G", "C"}
#
# Test these sequences:
#   seq1 = "ATCGGCTATCGA"
#   seq2 = "ATCGXCTA"
#   seq3 = "AUCGGCUAUCGA"
#   seq4 = "atcggcta"
#   seq5 = ""
#   seq6 = "ATCG1234"
#
# For each sequence, print:
#   1. Is it valid DNA?
#      (all chars in valid_dna_chars)
#      Hint: all(char in valid_dna_chars for char in seq)
#
#   2. Is it valid RNA?
#      (all chars in valid_rna_chars)
#
#   3. Is it all uppercase?
#      Hint: seq == seq.upper() or seq.isupper()
#
#   4. Is it empty?
#      Hint: seq == "" or not seq or len(seq) == 0
#
# Format output:
#   seq1: DNA=True  RNA=False Upper=True  Empty=False



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Grade book using chained comparisons.
# Write a function with full docstring.
#
# def classify_score(score):
#     Returns letter grade AND category based on score.
#     Grading:
#       90-100  → "A" → "Excellent"
#       80-89   → "B" → "Good"
#       70-79   → "C" → "Satisfactory"
#       60-69   → "D" → "Needs improvement"
#       0-59    → "F" → "Failing"
#       other   → "?" → "Invalid score"
#
# Requirements:
#   - Use chained comparisons for ranges
#   - Return a tuple: (grade, category)
#
# Test with: 100, 95, 85, 75, 65, 55, 0, -1, 101
# Print: "Score 95: A - Excellent"



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Sorting check using comparison operators.
# Do NOT use .sort() or sorted() - only comparisons!
#
# Given: numbers = [34, 12, 67, 23, 89, 45, 11]
#
#   1. Find the maximum value using only > comparison
#      (loop through and keep track)
#
#   2. Find the minimum value using only < comparison
#
#   3. Check if the list is already sorted in ascending order
#      Hint: check if each element <= next element
#      Use a for loop with range(len(numbers)-1)
#
#   4. Check if sorted in descending order
#
#   5. Count how many elements are:
#      - greater than the average
#      - less than the average
#      - equal to the average
#
# Print all results with labels.



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# String comparison deep dive.
#
# Given these names:
# names = ["Charlie", "alice", "Bob", "DIANA", "eve"]
#
# Using ONLY comparison operators (no .sort()):
#
#   1. Find the "smallest" name (lexicographically)
#      using < comparisons in a loop
#
#   2. Find the "largest" name using > comparisons
#
#   3. Check if "Bob" is in the list (case sensitive)
#
#   4. Check if "bob" is in the list (case insensitive)
#      Hint: any(name.lower() == "bob" for name in names)
#
#   5. Count names that come before "Charlie" alphabetically
#      (case insensitive - convert to lower first)
#
#   6. Are all names different? (no duplicates)
#      Hint: compare len(names) with len(set(names))
#
# Print all results with labels.



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Build a number guessing game LOGIC (no actual input needed).
# Simulate 5 rounds with predefined guesses.
#
# secret_number = 42
# guesses = [10, 70, 35, 45, 42]
#
# For each guess, using ONLY comparison operators, determine:
#   - Is it correct?    (== secret_number)
#   - Too high?         (> secret_number)
#   - Too low?          (< secret_number)
#   - How far off?      (abs difference - use abs())
#   - Within 10?        (abs difference <= 10)
#   - Within 5?         (abs difference <= 5)
#
# Print for each guess:
#   Guess 1: 10
#   Result:  Too low
#   Off by:  32
#   Close:   False (not within 10)
#   ---
#
# At the end print which guess number was correct.



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Version number comparison.
# Software versions like "3.11.2" need special comparison.
#
# Given these version strings:
#   v1 = "3.11.2"
#   v2 = "3.9.15"
#   v3 = "4.0.0"
#   v4 = "3.11.2"
#
# For each pair, determine which is newer (larger).
#
# Instructions:
#   1. Split version by "." → ["3", "11", "2"]
#   2. Convert each part to int
#   3. Compare major, then minor, then patch
#
# Note: "3.11.2" > "3.9.15" because 11 > 9
#       But "3.9.15" > "3.9.2" as strings! ("15" < "2" lexicographically)
#       That is why we need int conversion!
#
# Print:
#   v1 vs v2: v1 is newer (3.11.2 > 3.9.15)
#   v1 vs v3: v3 is newer (4.0.0 > 3.11.2)
#   v1 vs v4: equal (3.11.2 == 3.11.2)
#
# Hint:
#   parts1 = [int(x) for x in v1.split(".")]
#   Then compare parts1[0] vs parts2[0], etc.



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Temperature classification system.
#
# Write a complete temperature analyzer with docstrings.
# Use chained comparisons throughout.
#
# Temperature scales and classifications:
#
# Celsius ranges:
#   < -40    → "Extreme cold"
#   -40 - -1 → "Cold"
#   0 - 15   → "Cool"
#   16 - 25  → "Comfortable"
#   26 - 35  → "Warm"
#   36 - 37  → "Body temperature"
#   > 37     → "Hot"
#
# Functions to write:
#   celsius_to_fahrenheit(c)
#   celsius_to_kelvin(c)
#   classify_temperature(c)     → returns category string
#   is_water_state(c)           → returns "solid"/"liquid"/"gas"
#     (water: solid below 0, gas above 100, liquid between)
#   temperatures_equal(c1, c2)  → uses math.isclose() for safety
#
# Test with: -50, -20, 5, 20, 30, 37, 50, 100, 150
# For each temperature print:
#   -50°C = -58.0°F = 223.15K | Extreme cold | solid water



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Complete comparison operator challenge.
# Build a student ranking system using ONLY comparison operators.
#
# students = [
#     {"name": "Alice",   "score": 92.5, "age": 22},
#     {"name": "Bob",     "score": 85.0, "age": 25},
#     {"name": "Charlie", "score": 92.5, "age": 20},
#     {"name": "Diana",   "score": 78.3, "age": 22},
#     {"name": "Edward",  "score": 95.1, "age": 23},
# ]
#
# Using ONLY comparison operators and loops:
#
#   1. Find the student with the HIGHEST score
#      (if tie, younger student wins)
#
#   2. Find the student with the LOWEST score
#
#   3. Count students with score >= 90 ("Honor Roll")
#
#   4. Count students with score in range 80-89 (inclusive)
#
#   5. Are ANY two students exactly tied in score?
#      Print True/False and which students (if tied)
#
#   6. Is the list sorted by score (descending)?
#
#   7. Find students whose score is above the class average
#      (calculate average first using sum and len logic)
#
# Print a complete report with all findings.
# All comparisons must use == != > < >= <= is in not in

