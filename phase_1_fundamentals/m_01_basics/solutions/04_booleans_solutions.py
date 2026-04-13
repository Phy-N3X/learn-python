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
# EXERCISE 1 ✅ | EASY
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
# EXERCISE 2 ✅ | EASY
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
# EXERCISE 3 ✅ | EASY
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
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
a = None
b = None
c = True
d = 1
e = []
f = []

print("\nExercise 6:")
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
username  = ""
nickname  = None
full_name = "Anna Kowalski"
city      = ""
country   = "Poland"

display_name = username or nickname or full_name or "Unknown"
location = city or country or "Location unknown"

print("\nExercise 9:")
print(display_name)
print(location)



# ------------------------------------------------------------
# EXERCISE 10 ✅ | MEDIUM
# ------------------------------------------------------------
name  = "John"
score = 0
items = []
data  = None
ratio = 0.0

print("\nExercise 10:")
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
results = [True, False, True, True, False, True]

mean = results.count(True) / len(results)

print("\nExercise 11:")
print("1. How many True values in results: ", results.count(True))
print("2. How many False values in results: ", results.count(False))
print(f"3. Pass rate: {mean:.1%}")
print(f"4. Pass rate is above 50%: {mean >= 0.50}")
print("5. True + True + False + True: ", True + True + False + True, type(True + True + False + True))



# ------------------------------------------------------------
# EXERCISE 12 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
age         = 23
score       = 85
gpa         = 3.7
is_enrolled = True

rule_1 = 18 <= age <= 30
rule_2 = 70 <= score <= 100
rule_3 = 3.5 < gpa and 80 < score
rule_4 = is_enrolled is True and age >= 18
rule_5 = (gpa > 3.5 or score > 90) and is_enrolled
rule_6 = not (age < 18 or score < 60)

is_eligible = rule_1 and rule_2 and rule_3 and rule_4 and rule_5 and rule_6

print("\nExercise 12:")
print("Eligible: ", is_eligible)



# ------------------------------------------------------------
# EXERCISE 13 ✅ | MEDIUM-HARD
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
username = "anna_99"
password = "Secret123"
age      = 17
email    = "anna@email.com"

is_username_valid = (4 < len(username) < 20) and not " " in username
is_password_valid = (len(password) >= 8) and not password.islower() and not password.isupper()
is_adult = age >= 18
is_email_valid = not email.startswith("@") and not email.endswith(".") and "@" in email and "." in email
all_valid = is_username_valid and is_password_valid and is_adult and is_email_valid

print("\nExercise 14:")
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

score    = 75
grade    = "B"
is_active = True
is_admin  = False
age      = 20

print()
print('Original 1: not (score > 60 and grade == "A": ', not (score > 60 and grade == "A"))
print('Patched 1: (not score > 60) or (not grade == "A"): ', (not score > 60) or (not grade == "A"))

print()
print("Original 2: not (is_active or is_admin): ", not (is_active or is_admin))
print("Patched 2: (not is_active) and (not is_admin): ",(not is_active) and (not is_admin))

print()
print("Original 2: not (age < 18 or score < 50): ", not (age < 18 or score < 50))
print("Patched 3: (not age < 18) and (not score < 50): ", (not age < 18) and (not score < 50))