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
is_enrolled = True
has_passed = True
is_full_time = False
has_scholarship = False

print("Exercise 1:")
print(is_enrolled, type(is_enrolled), int(is_enrolled))
print(has_passed, type(has_passed), int(has_passed))
print(is_full_time, type(is_full_time), int(is_full_time))
print(has_scholarship, type(has_scholarship), int(has_scholarship))



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
a = 15
b = 30
c = 15

print("\nExercise 2:")
print(a == c)        # True
print(a == b)        # False
print(a != b)        # True
print(b > a)         # True
print(a >= c)        # True
print(b <= a)        # False
print(a < b < 50)    # True
print(10 < a < 20)   # True



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
print("\nExercise 3:")
print(True and True)              # True
print(True and False)             # False
print(False and False)            # False
print(True or False)              # True
print(False or False)             # False
print(not True)                   # False
print(not False)                  # True
print(not (True and False))       # True
print(True and True or False )    # True
print(True and (True or False))   # True



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
print("\nExercise 4:")
print(bool(0))         # False
print(bool(1))         # True
print(bool(-1))        # True
print(bool(0.0))       # False
print(bool(0.1))       # True
print(bool(""))        # False
print(bool(" "))       # True
print(bool("False"))   # True
print(bool([]))        # False
print(bool([0]))       # True
print(bool({}))        # False
print(bool(None))      # False
print(bool(True))      # True
print(bool(False))     # False



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
text   = "Bioinformatics is amazing"
vowels = ["a", "e", "i", "o", "u"]
nums   = (2, 4, 6, 8, 10)

print("\nExercise 5:")
print('1. Is "Bio" in text?', "Bio" in text)            # True
print('2. Is "bio" in text?', "bio" in text)            # False
print('3. Is "amazing" in text?', "amazing" in text)    # True
print('4. Is "e" in vowels?', "e" in vowels)            # True
print('5. Is "b" in vowels?', "b" in vowels)            # False
print('6. Is "b" NOT in vowels?', "b" not in vowels)    # True
print('7. Is 6 in nums?', 6 in nums)                    # True
print('8. Is 7 not in nums?', 7 not in nums)            # True



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
a = None
b = None
c = True
d = 1
e = []
f = []

print("\nExercise 6:")
print(a is None)    # True
print(a is b)       # True
print(c is True)    # True
print(c == d)       # True
print(c is d)       # False
print(e == f)       # True
print(e is f)       # False



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
username = "anna_99"
password = "Secret123"
age      = 17
email    = "anna@email.com"

# Calculate and print True/False for each validation rule:
#
#   1. username_valid:
#      - length between 4 and 20 (inclusive)
#      - contains no spaces (" " not in username)
#
is_username_valid = (4 < len(username) < 20)

#   2. password_valid:
#      - length >= 8
#      - is not all lowercase (not password.islower())
#      - is not all uppercase (not password.isupper())

is_password_valid = (len(password) >= 8) and not password.islower() and not password.isupper()


#   3. age_valid:
#      - age >= 18
#
is_adult = age >= 18

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

print("\nExercise 14:")
print("Full user report:")
print("Username valid: ", is_username_valid)
print("Password valid: ", is_password_valid)
print("Age valid: ", is_adult)
print("Email valid: ", is_username_valid)
print("-" * 25)



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