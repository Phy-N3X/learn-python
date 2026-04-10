# ============================================================
# MODULE 01 | LECTURE 01 - Variables
# ============================================================
# What you will learn:
#   - What a variable is
#   - How to create a variable
#   - Naming rules and conventions
#   - Multiple assignment
#   - Checking variable type
# ============================================================


# ------------------------------------------------------------
# PART 1: What is a variable?
# ------------------------------------------------------------

# A variable is a named container that stores a value.
# Think of it as a labeled box:
#
#   name = "John"
#   ┌──────────┐
#   │  "John"  │  ← box label: name
#   └──────────┘

# Creating a variable - syntax:
# variable_name = value

age = 25
name = "John"
height = 1.82
is_student = True

print(age)          # 25
print(name)         # John
print(height)       # 1.82
print(is_student)   # True


# ------------------------------------------------------------
# PART 2: Variable types are assigned automatically
# ------------------------------------------------------------

# Python figures out the type on its own
# You do NOT write: int age = 25 (that's Java/C++)
# You just write:   age = 25

x = 10          # Python knows this is int
y = 3.14        # Python knows this is float
z = "hello"     # Python knows this is str
q = True        # Python knows this is bool

# Check the type with type()
print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
print(type(q))  # <class 'bool'>


# ------------------------------------------------------------
# PART 3: Naming rules - what is REQUIRED
# ------------------------------------------------------------

# ✅ ALLOWED:
my_name = "John"        # snake_case - standard in Python!
myName = "John"         # camelCase - allowed but not preferred
name2 = "John"          # numbers allowed - but not at start
_name = "John"          # underscore at start - allowed
MY_CONSTANT = 3.14      # ALL CAPS = convention for constants

# ❌ NOT ALLOWED:
# 2name = "John"        # cannot start with a number
# my-name = "John"      # hyphens not allowed
# my name = "John"      # spaces not allowed
# class = "John"        # reserved keyword!

# Reserved keywords you cannot use as variable names:
# if, else, for, while, def, class, return,
# import, True, False, None, and, or, not...


# ------------------------------------------------------------
# PART 4: Naming conventions - what is RECOMMENDED
# ------------------------------------------------------------

# Python standard = snake_case
# Words separated by underscores, all lowercase

# ✅ Good names - clear and descriptive:
user_age = 25
first_name = "Anna"
total_price = 99.99
is_logged_in = True
max_attempts = 3

# ❌ Bad names - unclear:
a = 25              # what is 'a'?
x1 = "Anna"         # what is 'x1'?
tp = 99.99          # abbreviation = hard to read
flag = True         # 'flag' tells us nothing


# ------------------------------------------------------------
# PART 5: Changing a variable value
# ------------------------------------------------------------

# A variable can be changed at any time
score = 0
print(score)    # 0

score = 10
print(score)    # 10

score = 99
print(score)    # 99

# The type can also change (Python is dynamically typed)
x = 5
print(type(x))  # <class 'int'>

x = "now I am a string"
print(type(x))  # <class 'str'>


# ------------------------------------------------------------
# PART 6: Multiple assignment
# ------------------------------------------------------------

# Assign the same value to multiple variables at once
x = y = z = 0
print(x, y, z)      # 0 0 0

# Assign different values in one line
name, age, city = "Anna", 25, "Warsaw"
print(name)         # Anna
print(age)          # 25
print(city)         # Warsaw

# Swap two variables - Python does this elegantly!
a = 10
b = 20
print(a, b)         # 10 20

a, b = b, a         # swap!
print(a, b)         # 20 10

# In other languages you need a temporary variable:
# temp = a
# a = b
# b = temp
# Python does it in one line!


# ------------------------------------------------------------
# PART 7: Variables and memory
# ------------------------------------------------------------

# When you write x = 5
# Python creates the value 5 in memory
# and points the label 'x' at it

x = 5
y = x           # y points to the same value

print(x)        # 5
print(y)        # 5

x = 10          # x now points to a NEW value
print(x)        # 10
print(y)        # 5 ← y still points to the old value!

# id() shows the memory address
a = 5
b = 5
print(id(a))    # some address e.g. 140712345
print(id(b))    # same address! Python reuses small integers


# ------------------------------------------------------------
# PART 8: None - the empty variable
# ------------------------------------------------------------

# None means "no value" / "empty"
# It is its own type: NoneType

result = None
print(result)           # None
print(type(result))     # <class 'NoneType'>

# Often used as a placeholder
user_input = None       # will be filled in later

# Check if variable is None
if result is None:
    print("No result yet")


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ variable_name = value
# ✅ snake_case for naming
# ✅ Descriptive names
# ✅ type() to check type
# ✅ Multiple assignment: a, b = 1, 2
# ✅ Swap: a, b = b, a
# ✅ None = empty value