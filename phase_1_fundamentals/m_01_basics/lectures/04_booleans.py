# ============================================================
# MODULE 01 | LECTURE 04 - Booleans
# ============================================================
# What you will learn:
#   - What a boolean is
#   - True and False
#   - Comparison operators
#   - Logical operators
#   - Truthy and Falsy values
#   - Boolean in practice
#   - Common pitfalls
# ============================================================


# ------------------------------------------------------------
# PART 1: What is a Boolean?
# ------------------------------------------------------------

# A boolean is the simplest data type in Python
# It has exactly TWO possible values: True or False
# Named after mathematician George Boole (1815-1864)

is_sunny = True
is_raining = False

print(is_sunny)             # True
print(is_raining)           # False
print(type(is_sunny))       # <class 'bool'>
print(type(is_raining))     # <class 'bool'>

# IMPORTANT: Capital T and F - these are NOT strings!
print(True)                 # True
print(False)                # False
# print(true)               # NameError! - lowercase not valid
# print(false)              # NameError! - lowercase not valid

# Booleans ARE integers in Python (bool is subclass of int)
print(isinstance(True, int))    # True  ← bool IS an int!
print(True  == 1)               # True
print(False == 0)               # True
print(True  + True)             # 2
print(True  + False)            # 1
print(False + False)            # 0
print(True  * 5)                # 5
print(False * 5)                # 0


# ------------------------------------------------------------
# PART 2: Comparison Operators - Producing Booleans
# ------------------------------------------------------------

# Comparison operators ALWAYS return True or False

a = 10
b = 20

# Equal to
print(a == b)           # False
print(a == 10)          # True

# Not equal to
print(a != b)           # True
print(a != 10)          # False

# Greater than
print(a > b)            # False
print(b > a)            # True

# Less than
print(a < b)            # True
print(b < a)            # False

# Greater than or equal to
print(a >= 10)          # True  ← equal counts!
print(a >= 11)          # False

# Less than or equal to
print(a <= 10)          # True  ← equal counts!
print(a <= 9)           # False

# Comparing strings - lexicographic (alphabetical) order
print("apple" == "apple")   # True
print("apple" == "Apple")   # False ← case sensitive!
print("apple" < "banana")   # True  ← 'a' before 'b'
print("b" > "a")            # True
print("abc" < "abd")        # True  ← compares char by char
print("z" > "A")            # True  ← lowercase > uppercase in ASCII

# Comparing different types
print(1 == 1.0)             # True  ← int and float can be equal
print(1 == "1")             # False ← int and str are never equal
print(0 == False)           # True  ← bool is int!
print(1 == True)            # True  ← bool is int!

# Chained comparisons - very Pythonic!
x = 5
print(1 < x < 10)           # True  ← x is between 1 and 10
print(1 < x < 4)            # False
print(0 <= x <= 10)         # True
print(10 < x < 20)          # False

# Equivalent to:
print(1 < x and x < 10)     # True  ← same thing, less readable


# ------------------------------------------------------------
# PART 3: Identity and Membership Operators
# ------------------------------------------------------------

# is / is not - checks if two variables point to SAME object
# == checks if values are EQUAL
# is  checks if they are the EXACT SAME object in memory

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)       # True  ← same values
print(a is b)       # False ← different objects in memory!
print(a is c)       # True  ← c points to same object as a

# is None - the correct way to check for None
x = None
print(x is None)        # True  ← correct!
print(x == None)        # True  ← works but not recommended
print(x is not None)    # False

# in / not in - membership testing (returns bool)
fruits = ["apple", "banana", "cherry"]
print("apple" in fruits)        # True
print("mango" in fruits)        # False
print("mango" not in fruits)    # True

text = "Hello World"
print("Hello" in text)          # True
print("hello" in text)          # False ← case sensitive!

numbers = (1, 2, 3, 4, 5)
print(3 in numbers)             # True
print(6 in numbers)             # False


# ------------------------------------------------------------
# PART 4: Logical Operators
# ------------------------------------------------------------

# Three logical operators: and, or, not
# They combine boolean expressions

# AND - both must be True
print(True  and True)       # True
print(True  and False)      # False
print(False and True)       # False
print(False and False)      # False

# OR - at least one must be True
print(True  or True)        # True
print(True  or False)       # True
print(False or True)        # True
print(False or False)       # False

# NOT - reverses the boolean
print(not True)             # False
print(not False)            # True

# Truth table summary:
# A      B      A and B    A or B    not A
# True   True   True       True      False
# True   False  False      True      False
# False  True   False      True      True
# False  False  False      False     True


# ------------------------------------------------------------
# PART 5: Logical Operators with Real Values
# ------------------------------------------------------------

age = 25
income = 50000
has_job = True

# Combining conditions
is_eligible_loan = age >= 18 and income >= 30000
print(is_eligible_loan)     # True

can_enter = age >= 18 or has_job
print(can_enter)            # True

is_minor = not (age >= 18)
print(is_minor)             # False

# Complex conditions - use parentheses for clarity!
score = 75
grade = "B"
is_passing = score >= 60 and (grade == "A" or grade == "B")
print(is_passing)           # True

# Without parentheses - and has higher priority than or!
print(True or False and False)      # True  ← (False and False) first = False, then True or False = True
print((True or False) and False)    # False ← different result!

# Operator priority: not > and > or
# When in doubt - use parentheses!


# ------------------------------------------------------------
# PART 6: Short-Circuit Evaluation ⚡
# ------------------------------------------------------------

# Python is LAZY - stops evaluating as soon as result is known

# AND short-circuit:
# If first is False → result is False → don't check second!
def check_a():
    print("checking A")
    return False

def check_b():
    print("checking B")
    return True

print(check_a() and check_b())
# Output:
# checking A    ← only A is checked!
# False         ← B is never called because A is False

print("---")

print(check_b() or check_a())
# Output:
# checking B    ← only B is checked!
# True          ← A is never called because B is True

# Practical use: safe checking
name = ""
# This would crash without short-circuit:
# if len(name) > 0 and name[0] == "A":  ← safe because of short-circuit
result = len(name) > 0 and name[0] == "A"
print(result)   # False ← name[0] never evaluated (would crash on empty string!)


# ------------------------------------------------------------
# PART 7: Truthy and Falsy Values
# ------------------------------------------------------------

# In Python, EVERY value is either Truthy or Falsy
# You can use ANY value in a boolean context (if, while, and, or)

# FALSY values - these are treated as False:
print(bool(False))      # False
print(bool(None))       # False
print(bool(0))          # False  ← zero integer
print(bool(0.0))        # False  ← zero float
print(bool(""))         # False  ← empty string
print(bool([]))         # False  ← empty list
print(bool({}))         # False  ← empty dictionary
print(bool(()))         # False  ← empty tuple
print(bool(set()))      # False  ← empty set

print("---")

# TRUTHY values - everything else is treated as True:
print(bool(True))       # True
print(bool(1))          # True  ← any non-zero number
print(bool(-1))         # True  ← negative numbers too!
print(bool(0.1))        # True  ← any non-zero float
print(bool("hello"))    # True  ← any non-empty string
print(bool(" "))        # True  ← even just a space!
print(bool([1, 2]))     # True  ← any non-empty list
print(bool([False]))    # True  ← list with one element - even False!

# Practical use - checking if something exists/has value
name = "Anna"
if name:                        # same as: if name != ""
    print("Name is set")        # Name is set

name = ""
if not name:                    # same as: if name == ""
    print("Name is empty")      # Name is empty

items = []
if not items:                   # same as: if len(items) == 0
    print("List is empty")      # List is empty

score = 0
if not score:                   # CAREFUL! 0 is falsy!
    print("No score")           # No score  ← even though 0 is valid!
# Better:
if score is None:
    print("Score not set")
# or
if score == 0:
    print("Score is zero")


# ------------------------------------------------------------
# PART 8: Boolean and/or Return Values (Advanced)
# ------------------------------------------------------------

# and/or don't HAVE to return True/False
# They return one of the ORIGINAL values!

# AND returns first Falsy value, or last value if all Truthy
print(1 and 2)              # 2     ← both truthy, returns last
print(0 and 2)              # 0     ← 0 is falsy, returns it
print("" and "hello")       # ""    ← "" is falsy, returns it
print("hi" and "hello")     # hello ← both truthy, returns last

# OR returns first Truthy value, or last value if all Falsy
print(1 or 2)               # 1     ← 1 is truthy, returns it
print(0 or 2)               # 2     ← 0 is falsy, tries next
print("" or "hello")        # hello ← "" is falsy, tries next
print("" or 0)              # 0     ← all falsy, returns last

# Practical pattern - default values
user_name = ""
display_name = user_name or "Anonymous"
print(display_name)         # Anonymous ← user_name is falsy

user_name = "Anna"
display_name = user_name or "Anonymous"
print(display_name)         # Anna ← user_name is truthy


# ------------------------------------------------------------
# PART 9: bool() and Converting to Boolean
# ------------------------------------------------------------

# Explicit conversion to bool
print(bool(1))          # True
print(bool(0))          # False
print(bool("hello"))    # True
print(bool(""))         # False
print(bool(None))       # False
print(bool([1, 2, 3]))  # True
print(bool([]))         # False

# int() on bool
print(int(True))        # 1
print(int(False))       # 0

# Counting True values in a list (True = 1, False = 0)
results = [True, False, True, True, False, True]
print(sum(results))     # 4  ← counts True values!
print(sum(results) / len(results))  # 0.666... ← percentage of True


# ------------------------------------------------------------
# PART 10: Common Pitfalls ⚠️
# ------------------------------------------------------------

# PITFALL 1: = vs == (assignment vs comparison)
x = 5
# if x = 10:            # SyntaxError! use == for comparison
if x == 10:
    print("ten")

# PITFALL 2: is vs == for value comparison
a = 1000
b = 1000
print(a == b)           # True  ← correct for value comparison
print(a is b)           # may be False! ← don't use is for numbers

# is should ONLY be used with None, True, False
print(x is None)        # correct use of is
print(x is True)        # correct use of is

# PITFALL 3: not in vs != with membership
fruits = ["apple", "banana"]
print("mango" not in fruits)    # True  ← correct!
# print(not "mango" in fruits)  # works but confusing - avoid

# PITFALL 4: Chained comparison vs separate
x = 5
print(1 < x < 10)               # True  ← Python chaining
print(1 < x and x < 10)         # True  ← same result
# print(1 < x > 3)              # True but confusing - avoid

# PITFALL 5: 0 and False, 1 and True confusion
print(0 == False)       # True
print(1 == True)        # True
print(2 == True)        # False! ← 2 is truthy but not == True
print(bool(2))          # True   ← 2 IS truthy
# Solution: use bool() explicitly when needed

# PITFALL 6: Empty string vs None
name_a = ""
name_b = None
print(not name_a)       # True   ← empty string is falsy
print(not name_b)       # True   ← None is also falsy
print(name_a is None)   # False  ← "" is not None!
# If you need to distinguish between "" and None:
print(name_a is None)           # False ← not None
print(name_b is None)           # True  ← is None
print(name_a == "")             # True  ← is empty string


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ bool has exactly two values: True and False (capital!)
# ✅ bool is subclass of int: True==1, False==0
# ✅ Comparison: == != > < >= <=
# ✅ Identity:   is, is not  (use only with None/True/False)
# ✅ Membership: in, not in
# ✅ Logical:    and, or, not
# ✅ Priority:   not > and > or
# ✅ Short-circuit: and stops on first False, or stops on first True
# ✅ Falsy: False None 0 0.0 "" [] {} () set()
# ✅ Truthy: everything else
# ✅ and/or return original values, not just True/False
# ✅ bool() converts any value to boolean
# ⚠️  = is assignment, == is comparison
# ⚠️  is checks identity, == checks equality
# ⚠️  0 is falsy but 0 != True is not the same as bool(0)!
# ⚠️  "hello" is truthy but "hello" != True