# ============================================================
# MODULE 01 | EXERCISES 04 - Booleans
# ============================================================
# 15 exercises - booleans only
# Allowed from previous lectures:
#   - variables, print(), type()        (lecture 01)
#   - abs(), round(), len()             (lecture 02)
#   - string methods, f-strings         (lecture 03)
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Create four boolean variables describing a student:
#   is_enrolled, has_passed, is_full_time, has_scholarship
# Assign realistic True/False values.
# Print each variable with its type.
# Then print int() of each - what do you notice?



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Given:
#   a = 15
#   b = 30
#   c = 15
#
# Without running the code first, predict True or False
# for each comparison. Write prediction as comment, then verify:
#
#   a == c
#   a == b
#   a != b
#   b > a
#   a >= c
#   b <= a
#   a < b < 50
#   10 < a < 20



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output of ALL logical operator combinations.
# Write prediction as comment first, then verify.
#
#   True and True
#   True and False
#   False and False
#   True or False
#   False or False
#   not True
#   not False
#   not (True and False)
#   True and True or False
#   True and (True or False)



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Test ALL these values with bool() and print the result.
# Before running, predict True or False for each:
#
#   0, 1, -1, 0.0, 0.1, "", " ", "False",
#   [], [0], {}, None, True, False



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Membership testing.
# Given:
#   text   = "Bioinformatics is amazing"
#   vowels = ["a", "e", "i", "o", "u"]
#   nums   = (2, 4, 6, 8, 10)
#
# Print True or False for:
#   1. Is "Bio" in text?
#   2. Is "bio" in text?
#   3. Is "amazing" in text?
#   4. Is "e" in vowels?
#   5. Is "b" in vowels?
#   6. Is "b" NOT in vowels?
#   7. Is 6 in nums?
#   8. Is 7 not in nums?



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# is vs == investigation.
# Given:
#   a = None
#   b = None
#   c = True
#   d = 1
#   e = []
#   f = []
#
# Predict and verify:
#   a is None
#   a is b
#   c is True
#   c == d
#   c is d
#   e == f
#   e is f
#
# Write a comment explaining the difference between
# is and == based on what you observed.



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Short-circuit evaluation.
# Predict what gets PRINTED (not just the result).
# Consider which functions get called.
#
# def always_true():
#     print("evaluated A")
#     return True
#
# def always_false():
#     print("evaluated B")
#     return False
#
# Expression 1: always_false() and always_true()
# Expression 2: always_true() or always_false()
# Expression 3: always_true() and always_false()
# Expression 4: always_false() or always_true()
#
# Write prediction as comment for each, then verify.



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# and/or return original values - not just True/False.
# Predict the EXACT output (not just True/False) for each:
#
#   1 and 2
#   0 and 2
#   1 or 2
#   0 or 2
#   "" or "hello"
#   "hi" or "hello"
#   "" and "hello"
#   "hi" and "hello"
#   0 or "" or [] or None or "found it"
#   1 and 2 and 3 and 4
#
# Write predictions as comments, then verify.
# Write a comment explaining the pattern you see.



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Default value pattern using or.
# Given these variables (some empty/None):
#
#   username  = ""
#   nickname  = None
#   full_name = "Anna Kowalski"
#   city      = ""
#   country   = "Poland"
#
# Use the "or" default pattern to print:
#   display_name = username OR nickname OR full_name OR "Unknown"
#   location     = city OR country OR "Location unknown"
#
# Then change username = "anna123" and repeat.
# What changes and why?



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Truthy/Falsy in practice.
# Given:
#   name  = "John"
#   score = 0
#   items = []
#   data  = None
#   ratio = 0.0
#
# For each variable:
#   1. Print whether it is truthy or falsy using bool()
#   2. Write a comment: is this the behavior you expected?
#
# Then fix this BUGGY check:
#   if score:
#       print("Player scored!")
#   else:
#       print("No score recorded")
#
# Why is this buggy? Write corrected version.



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Boolean arithmetic - True is 1, False is 0.
#
# Given:
#   results = [True, False, True, True, False, True, False, True]
#
# Using sum() and len() and basic arithmetic:
#   1. Count how many True values are in results
#   2. Count how many False values are in results
#   3. Calculate the percentage of True values
#      Print as: "Pass rate: XX.X%"
#   4. Is the pass rate above 50%?
#      Print True or False
#   5. Using bool arithmetic, calculate:
#      True + True + False + True
#      Print result and its type



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Chained comparisons - real use case.
#
# You are building a validation system.
# Given:
#   age         = 23
#   score       = 85
#   gpa         = 3.7
#   is_enrolled = True
#
# Using chained comparisons and logical operators,
# calculate and print True/False for each rule:
#
#   Rule 1: age is between 18 and 30 (inclusive)
#   Rule 2: score is between 70 and 100 (inclusive)
#   Rule 3: gpa is above 3.5 AND score is above 80
#   Rule 4: is_enrolled is True AND age >= 18
#   Rule 5: (gpa > 3.5 OR score > 90) AND is_enrolled
#   Rule 6: NOT (age < 18 OR score < 60)
#
# Then print final verdict:
#   is_eligible = Rule 1 AND Rule 2 AND Rule 4 AND Rule 5
#   Print: "Eligible: True/False"



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Operator precedence puzzle.
# Predict the result of each WITHOUT running.
# Write prediction as comment, then verify.
# If wrong, write WHY in a comment.
#
#   not True or False
#   not (True or False)
#   True or False and False
#   (True or False) and False
#   not True and not False
#   not (True and not False)
#   True and False or True and True
#   not False and not False or False
#
# After verifying, write the precedence rule as a comment:
# "not binds __, and binds __, or binds __"



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a complete input validator using ONLY booleans.
# Do NOT use if statements (that's next lecture!)
#
# Given this user data:
#   username = "anna_99"
#   password = "Secret123"
#   age      = 17
#   email    = "anna@email.com"
#
# Calculate and print True/False for each validation rule:
#
#   1. username_valid:
#      - length between 4 and 20 (inclusive)
#      - contains no spaces (" " not in username)
#
#   2. password_valid:
#      - length >= 8
#      - is not all lowercase (not password.islower())
#      - is not all uppercase (not password.isupper())
#
#   3. age_valid:
#      - age >= 18
#
#   4. email_valid:
#      - contains "@"
#      - contains "."
#      - does not start with "@"
#      - does not end with "."
#
#   5. all_valid:
#      - ALL four above are True
#
# Print a report:
#   Username valid:  True/False
#   Password valid:  True/False
#   Age valid:       True/False
#   Email valid:     True/False
#   -------------------------
#   All valid:       True/False



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Boolean logic puzzle - De Morgan's Laws.
#
# De Morgan's Laws state:
#   not (A and B) == (not A) or  (not B)
#   not (A or  B) == (not A) and (not B)
#
# Part 1: Verify De Morgan's Laws
# For ALL combinations of A and B (True/True, True/False,
# False/True, False/False), verify both laws hold.
# Print each combination and whether the law holds (True/False)
#
# Part 2: Simplify these expressions using De Morgan's Laws
# Compute both the original and simplified version
# and verify they are equal:
#
#   Original 1: not (score > 60 and grade == "A")
#   Original 2: not (is_active or is_admin)
#   Original 3: not (age < 18 or score < 50)
#
# Use these values:
#   score    = 75
#   grade    = "B"
#   is_active = True
#   is_admin  = False
#   age      = 20
#
# Part 3: Write a comment explaining in plain English
# when De Morgan's Laws are useful in programming.