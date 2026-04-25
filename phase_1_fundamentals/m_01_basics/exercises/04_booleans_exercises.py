# ============================================================
# MODULE 01 | EXERCISES 04 - Booleans
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create four boolean variables describing a student:
#   is_enrolled, has_passed, is_full_time, has_scholarship

# Assign realistic True/False values.
# Print each variable with its type.
# Then print int() of each - what do you notice?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("Exercise:")

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
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given:
#   a = 15
#   b = 30
#   c = 15

# Without running the code first, predict True or False
# for each comparison. Write prediction as comment, then verify:
#   a == c
#   a == b
#   a != b
#   b > a
#   a >= c
#   b <= a
#   a < b < 50
#   10 < a < 20
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 2:")

a = 15
b = 30
c = 15

print(a == c)        # True
print(a == b)        # False
print(a != b)        # True
print(b > a)         # True
print(a >= c)        # True
print(b <= a)        # False
print(a < b < 50)    # True
print(10 < a < 20)   # True



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Predict the output of all logical operator combinations.
# Write prediction as comment first, then verify.
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
# CODE:
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
# EXERCISE 4 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Test all these values with bool() and print the result.
# Before running, predict True or False for each:
#   0, 1, -1, 0.0, 0.1, "", " ", "False",
#   [], [0], {}, None, True, False
# ------------------------------------------------------------
# CODE:
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
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given:
#   text = "Bioinformatics is amazing"
#   vowels = ["a", "e", "i", "o", "u"]
#   nums = (2, 4, 6, 8, 10)

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
# CODE:
# ------------------------------------------------------------
print("\nExercise 5:")

text = "Bioinformatics is amazing"
vowels = ["a", "e", "i", "o", "u"]
nums = (2, 4, 6, 8, 10)

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
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given:
#   a = None
#   b = None
#   c = True
#   d = 1
#   e = []
#   f = []

# Predict and verify:
#   a is None
#   a is b
#   c is True
#   c == d
#   c is d
#   e == f
#   e is f
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 6:")

a = None
b = None
c = True
d = 1
e = []
f = []

print(a is None)        # True
print(a is b)           # True
print(c is True)        # True
print(c == d)           # True
print(c is d)           # False
print(e == f)           # True
print(e is f)           # False



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Predict what gets printed (not just the result).
# Consider which functions get called.

# def always_true():
#     print("evaluated A")
#     return True

# def always_false():
#     print("evaluated B")
#     return False

# Expression 1: always_false() and always_true()
# Expression 2: always_true() or always_false()
# Expression 3: always_true() and always_false()
# Expression 4: always_false() or always_true()

# Write prediction as comment for each, then verify.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 7:")

def always_true():
    print("evaluated A")
    return True

def always_false():
    print("evaluated B")
    return False

print("\nExercise 7:")
always_false() and always_true()    # False - "evaluated B"
always_true() or always_false()     # True - "evaluated A"
always_true() and always_false()    # False - "evaluated B"
always_false() or always_true()     # True - "evaluated A"



# ------------------------------------------------------------
# EXERCISE 8 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# and/or return original values - not just True/False.
# Predict the exact output (not just True/False) for each:
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

# Write predictions as comments, then verify.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 8:")

print(1 and 2)                                  # True - 2
print(0 and 2)                                  # False - 0
print(1 or 2)                                   # True - 1
print(0 or 2)                                   # True - 2
print("" or "hello")                            # True - "hello"
print("hi" or "hello")                          # True - "hello"
print("" and "hello")                           # False - ""
print("hi" and "hello")                         # True - "hello"
print(0 or "" or [] or None or "found it")      # True - "found it"
print(1 and 2 and 3 and 4)                      # True - 4



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given these variables (some empty/None):
#   username = ""
#   nickname = None
#   full_name = "Anna Kowalski"
#   city = ""
#   country = "Poland"

# Use the "or" default pattern to print:
#   display_name = username or nickname or full_name or "Unknown"
#   location = city or country or "Location unknown"
#
# Then change username = "anna123" and repeat.
# What changes and why?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 9:")

username = ""
nickname = None
full_name = "Anna Kowalski"
city = ""
country = "Poland"

display_name = username or nickname or full_name or "Unknown"
location = city or country or "Location unknown"

print(display_name)
print(location)



# ------------------------------------------------------------
# EXERCISE 10 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given:
#   name = "John"
#   score = 0
#   items = []
#   data = None
#   ratio = 0.0

# For each variable print whether it is truthy or falsy using bool()

# Then fix this buggy check:
#   if score:
#       print("Player scored!")
#   else:
#       print("No score recorded")

# Why is this buggy? Write corrected version.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 10:")

name  = "John"
score = 0
items = []
data  = None
ratio = 0.0

print("1. Name: ", bool(name))     # True
print("2. Score: ", bool(score))   # False
print("3. Items: ", bool(items))   # False
print("4. Data: ", bool(data))     # False
print("5. Ratio: ", bool(ratio))   # False

if score > 0:
    print("Player scored!")
else:
    print("No score recorded")



# ------------------------------------------------------------
# EXERCISE 11 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given:
#   results = [True, False, True, True, False, True, False, True]

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
# CODE:
# ------------------------------------------------------------
print("\nExercise 11:")

results = [True, False, True, True, False, True]

mean = results.count(True) / len(results)

print("1. How many True values in results: ", results.count(True))
print("2. How many False values in results: ", results.count(False))
print(f"3. Pass rate: {mean:.1%}")
print(f"4. Pass rate is above 50%: {mean >= 0.50}")
print("5. True + True + False + True: ", True + True + False + True, type(True + True + False + True))



# ------------------------------------------------------------
# EXERCISE 12 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# You are building a validation system.
# Given:
#   age = 23
#   score = 85
#   gpa = 3.7
#   is_enrolled = True

# Using chained comparisons and logical operators,
# calculate and print True/False for each rule:

#   Rule 1: age is between 18 and 30 (inclusive)
#   Rule 2: score is between 70 and 100 (inclusive)
#   Rule 3: gpa is above 3.5 and score is above 80
#   Rule 4: is_enrolled is True and age >= 18
#   Rule 5: (gpa > 3.5 OR score > 90) and is_enrolled
#   Rule 6: not (age < 18 OR score < 60)

# Then print final verdict:
#   is_eligible = Rule 1 and Rule 2 and Rule 4 and Rule 5
#   Print: "Eligible: True/False"
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 12:")

age = 23
score = 85
gpa = 3.7
is_enrolled = True

rule_1 = 18 <= age <= 30
rule_2 = 70 <= score <= 100
rule_3 = 3.5 < gpa and 80 < score
rule_4 = is_enrolled is True and age >= 18
rule_5 = (gpa > 3.5 or score > 90) and is_enrolled
rule_6 = not (age < 18 or score < 60)

is_eligible = rule_1 and rule_2 and rule_3 and rule_4 and rule_5 and rule_6

print("Eligible: ", is_eligible)



# ------------------------------------------------------------
# EXERCISE 13 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Predict the result of each without running.
# Write prediction as comment, then verify.

#   not True or False
#   not (True or False)
#   True or False and False
#   (True or False) and False
#   not True and not False
#   not (True and not False)
#   True and False or True and True
#   not False and not False or False
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 13:")

print(not True or False)                 # False
print(not (True or False))               # False
print(True or False and False)           # True
print((True or False) and False)         # False
print(not True and not False)            # False
print(not (True and not False))          # False
print(True and False or True and True)   # True
print(not False and not False or False)  # True



# ------------------------------------------------------------
# EXERCISE 14 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Build a complete input validator using only booleans.
# Do not use if statements

# Given this user data:
#   username = "anna_99"
#   password = "Secret123"
#   age = 17
#   email = "anna@email.com"

# Calculate and print True/False for each validation rule:

#   1. username_valid:
#      - length between 4 and 20 (inclusive)
#      - contains no spaces (" " not in username)

#   2. password_valid:
#      - length >= 8
#      - is not all lowercase (not password.islower())
#      - is not all uppercase (not password.isupper())

#   3. age_valid:
#      - age >= 18

#   4. email_valid:
#      - contains "@"
#      - contains "."
#      - does not start with "@"
#      - does not end with "."

#   5. all_valid:
#      - ALL four above are True

# Print a report:
#   Username valid:  True/False
#   Password valid:  True/False
#   Age valid:       True/False
#   Email valid:     True/False
#   -------------------------
#   All valid:       True/False
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 14:")

username = "anna_99"
password = "Secret123"
age = 17
email = "anna@email.com"

is_username_valid = (4 < len(username) < 20) and not " " in username
is_password_valid = (len(password) >= 8) and not password.islower() and not password.isupper()
is_adult = age >= 18
is_email_valid = not email.startswith("@") and not email.endswith(".") and "@" in email and "." in email
all_valid = is_username_valid and is_password_valid and is_adult and is_email_valid

print("Full user report:")
print("Username valid: ".ljust(20), is_username_valid)
print("Password valid: ".ljust(20), is_password_valid)
print("Age valid: ".ljust(20), is_adult)
print("Email valid: ".ljust(20), is_email_valid)
print("-" * 26)
print("All valid: ".ljust(20), all_valid)



# ------------------------------------------------------------
# EXERCISE 15 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# De Morgan's Laws state:
#   not (A and B) == (not A) or  (not B)
#   not (A or  B) == (not A) and (not B)

# Part 1: Verify De Morgan's Laws
#   For all combinations of A and B (True/True, True/False,
#   False/True, False/False), verify both laws hold.
#   Print each combination and whether the law holds (True/False)

# Part 2: Simplify these expressions using De Morgan's Laws
#   Compute both the original and simplified version
#   and verify they are equal:

#   Original 1: not (score > 60 and grade == "A")
#   Original 2: not (is_active or is_admin)
#   Original 3: not (age < 18 or score < 50)

# Use these values:
#   score = 75
#   grade = "B"
#   is_active = True
#   is_admin = False
#   age = 20
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 15:")

print("De Morgans' First Law: not (A and B) == (not A) or (not B): ")
print("-" * 60)
print("1. not (True and True) == (not True) or (not True): ", not (True and True) == (not True) or (not True))
print("2. not (True and False) == (not True) or (not False): ", not (True and False) == (not True) or (not False))
print("3. not (False and True) == (not False) or (not True): ", not (False and True) == (not False) or (not True))
print("4. not (False and False) == (not False) or (not False): ", not (False and False) == (not False) or (not False))
print()
print("De Morgans' Second Law: not (A or B) == (not A) and (not B): ")
print("-" * 60)
print("1. not (True or True) == (not True) and (not True): ", (not (True or True)) == ((not True) and (not True)))
print("2. not (True or False) == (not True) and (not False): ", (not (True or False)) == ((not True) and (not False)))
print("3. not (False or True) == (not False) and (not True): ", (not (False or True)) == ((not False) and (not True)))
print("4. not (False or False) == (not False) and (not False): ", (not (False or False)) == ((not False) and (not False)))

score = 75
grade = "B"
is_active = True
is_admin  = False
age = 20

print()
print('Original 1: not (score > 60 and grade == "A": ', not (score > 60 and grade == "A"))
print('Patched 1: (not score > 60) or (not grade == "A"): ', (not score > 60) or (not grade == "A"))

print()
print("Original 2: not (is_active or is_admin): ", not (is_active or is_admin))
print("Patched 2: (not is_active) and (not is_admin): ",(not is_active) and (not is_admin))

print()
print("Original 2: not (age < 18 or score < 50): ", not (age < 18 or score < 50))
print("Patched 3: (not age < 18) and (not score < 50): ", (not age < 18) and (not score < 50))