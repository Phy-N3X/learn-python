# ============================================================
# MODULE 01 | LECTURE 09 - Comparison Operators
# ============================================================
# What you will learn:
#   - All comparison operators
#   - Comparing numbers
#   - Comparing strings
#   - Comparing different types
#   - Chained comparisons
#   - Identity operators (is / is not)
#   - Membership operators (in / not in)
#   - Comparison in practice
#   - Common pitfalls
# ============================================================


# ------------------------------------------------------------
# PART 1: What are Comparison Operators?
# ------------------------------------------------------------

# Comparison operators ALWAYS return a boolean: True or False
# They compare two values and tell you the relationship

# The 6 comparison operators:
# ==    equal to
# !=    not equal to
# >     greater than
# <     less than
# >=    greater than or equal to
# <=    less than or equal to

# Every comparison produces True or False:
print(5 == 5)           # True
print(5 == 6)           # False
print(type(5 == 5))     # <class 'bool'>

# You can store the result in a variable:
result = 10 > 5
print(result)           # True
print(type(result))     # <class 'bool'>


# ------------------------------------------------------------
# PART 2: Equal (==) and Not Equal (!=)
# ------------------------------------------------------------

# == checks if two values are EQUAL in value
print(5   == 5)         # True
print(5   == 6)         # False
print(5.0 == 5)         # True   int and float can be equal!
print("a" == "a")       # True
print("a" == "A")       # False  case sensitive!
print(True  == 1)       # True   bool is int!
print(False == 0)       # True   bool is int!
print(None  == None)    # True
print([]    == [])      # True   same contents

# != checks if two values are NOT EQUAL
print(5 != 6)           # True
print(5 != 5)           # False
print("hello" != "world")   # True
print(True != False)        # True
print(1 != 1.0)             # False  (equal in value!)

# Common mistake: = vs ==
x = 5               # assignment - sets x to 5
print(x == 5)       # comparison - checks if x equals 5
# if x = 5:         # SyntaxError! cannot assign inside if


# ------------------------------------------------------------
# PART 3: Greater and Less Than
# ------------------------------------------------------------

# > greater than
print(10 > 5)           # True
print(5  > 10)          # False
print(5  > 5)           # False  (strictly greater!)
print(5.1 > 5)          # True

# < less than
print(5  < 10)          # True
print(10 < 5)           # False
print(5  < 5)           # False  (strictly less!)
print(4.9 < 5)          # True

# >= greater than or equal to
print(10 >= 5)          # True
print(5  >= 5)          # True   (equal counts!)
print(4  >= 5)          # False

# <= less than or equal to
print(5  <= 10)         # True
print(5  <= 5)          # True   (equal counts!)
print(6  <= 5)          # False

# Practical: range checking
temperature = 98.6
is_normal = 97.0 <= temperature <= 99.0     # chained! (Part 6)
print(f"Normal temperature: {is_normal}")   # True

age = 25
can_rent_car = age >= 25
print(f"Can rent car: {can_rent_car}")      # True


# ------------------------------------------------------------
# PART 4: Comparing Numbers in Depth
# ------------------------------------------------------------

# int vs int - straightforward
print(100 > 99)         # True
print(-5 < 0)           # True
print(0 >= 0)           # True

# int vs float - works seamlessly
print(5 == 5.0)         # True
print(5 >  4.9)         # True
print(5 <  5.1)         # True
print(3 >= 3.0)         # True

# float precision warning!
print(0.1 + 0.2 == 0.3)    # False! floating point issue
print(0.1 + 0.2)            # 0.30000000000000004

# Safe float comparison - use math.isclose()
import math
print(math.isclose(0.1 + 0.2, 0.3))        # True
print(math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9))  # True

# Comparing with infinity
print(math.inf > 999999999)     # True
print(-math.inf < -999999999)   # True
print(math.inf == math.inf)     # True
print(math.nan == math.nan)     # False! NaN is never equal to anything
print(math.isnan(math.nan))     # True  ← correct way to check NaN


# ------------------------------------------------------------
# PART 5: Comparing Strings
# ------------------------------------------------------------

# Strings compare LEXICOGRAPHICALLY (like a dictionary)
# Python compares character by character using Unicode values

# Alphabetical order:
print("apple"  == "apple")      # True
print("apple"  == "Apple")      # False  case matters!
print("apple"  < "banana")      # True   'a' before 'b'
print("banana" > "apple")       # True
print("abc"    < "abd")         # True   third char: 'c' < 'd'
print("abc"    < "abcd")        # True   shorter = smaller when prefix matches

# Case comparison - uppercase letters come BEFORE lowercase in Unicode!
print("Z" < "a")                # True!  Z=90, a=97 in Unicode
print("A" < "z")                # True   A=65, z=122
print("apple" > "Apple")        # True   'a'(97) > 'A'(65)

# Check Unicode value with ord():
print(ord("A"))     # 65
print(ord("Z"))     # 90
print(ord("a"))     # 97
print(ord("z"))     # 122
print(ord("0"))     # 48
print(ord("9"))     # 57

# Digits in strings - compared by Unicode, not value!
print("9" < "10")              # False! "9" > "1" (first char)
print("09" < "10")             # True   '0'(48) < '1'(49)
print(9 < 10)                  # True   numeric comparison

# Always use numbers for numeric comparisons!
# String "9" and "10" are NOT numerically comparable

# Case-insensitive comparison:
a = "Hello"
b = "hello"
print(a == b)                           # False
print(a.lower() == b.lower())           # True  ← correct approach
print(a.casefold() == b.casefold())     # True  ← even better for unicode

# String length comparison:
print(len("hello") == len("world"))     # True  (both 5)
print(len("hi") < len("hello"))         # True  (2 < 5)

# Empty string:
print("" == "")                 # True
print("" < "a")                 # True   empty < anything
print("" > "a")                 # False


# ------------------------------------------------------------
# PART 6: Chained Comparisons
# ------------------------------------------------------------

# Python supports chaining comparisons - very readable!
# a < b < c   is equivalent to   a < b and b < c

x = 5

# Chained:
print(1 < x < 10)              # True   ← Pythonic!
print(0 <= x <= 10)            # True
print(5 <= x <= 5)             # True   (x exactly equals 5)
print(1 < x < 4)               # False

# Equivalent without chaining:
print(1 < x and x < 10)        # True   (same result, less readable)

# You can chain more than two:
y = 7
print(1 < x < y < 10)         # True
print(0 < x < y < 5)          # False  (y=7 is not < 5)

# Mixed operators:
print(1 < x <= 5)              # True   (x=5, 5<=5 is True)
print(1 < x < 5)               # False  (x=5, 5<5 is False)
print(5 >= x > 0)              # True

# Real world use - checking ranges:
score = 85
is_b_grade = 80 <= score < 90
print(f"B grade: {is_b_grade}")     # True

bmi = 22.5
is_normal = 18.5 <= bmi < 25.0
print(f"Normal BMI: {is_normal}")   # True

# pH scale (0-14):
ph = 6.8
is_acidic  = ph < 7.0
is_neutral = 6.5 <= ph <= 7.5
is_basic   = ph > 7.0
print(f"Acidic: {is_acidic}, Neutral: {is_neutral}, Basic: {is_basic}")


# ------------------------------------------------------------
# PART 7: Comparing Different Types
# ------------------------------------------------------------

# Comparing int and float - works!
print(5   == 5.0)       # True
print(5   >  4.9)       # True
print(type(5) == type(5.0))     # False  int != float

# Comparing bool and int - bool IS int!
print(True  == 1)       # True
print(False == 0)       # True
print(True  == 2)       # False  (True is 1, not 2)
print(True  >  False)   # True   (1 > 0)
print(True  >= 1)       # True

# Comparing with None:
print(None == None)     # True
print(None == 0)        # False
print(None == "")       # False
print(None == False)    # False

# Cannot compare incompatible types with > < >= <=
# print("hello" > 5)    # TypeError!
# print(None > 0)       # TypeError!
# print([1,2] > [1,3])  # True (lists compare element by element - preview)

# Checking type equality:
x = 42
print(type(x) == int)       # True
print(type(x) == float)     # False
print(type(x) == str)       # False
print(isinstance(x, int))   # True  ← better approach
print(isinstance(x, (int, float)))  # True  ← checks multiple types


# ------------------------------------------------------------
# PART 8: Identity Operators (is / is not)
# ------------------------------------------------------------

# is  - checks if two variables point to the SAME object in memory
# ==  - checks if two variables have the SAME VALUE

# They are DIFFERENT!

# Example with lists:
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)       # True  ← same values
print(a is b)       # False ← different objects in memory!
print(a is c)       # True  ← c points to exact same object as a

# Modifying c also modifies a (same object):
c.append(4)
print(a)            # [1, 2, 3, 4]  ← a was modified through c!
print(c)            # [1, 2, 3, 4]

# is not - opposite of is
print(a is not b)   # True   ← different objects
print(a is not c)   # False  ← same object

# WHEN TO USE is:
# Only for None, True, False - these are SINGLETONS in Python
# (only one instance of None exists)

x = None
print(x is None)        # True  ← CORRECT way to check for None
print(x == None)        # True  ← works but PEP 8 says use is
print(x is not None)    # False

# Integer caching - Python caches small integers (-5 to 256)
a = 5
b = 5
print(a is b)           # True  ← Python reuses cached object

a = 1000
b = 1000
print(a == b)           # True  ← same value
print(a is b)           # False ← different objects (outside cache range)
# This is why you should NEVER use is for numbers!

# String interning - similar to integer caching
s1 = "hello"
s2 = "hello"
print(s1 is s2)         # True  ← Python interns short strings
s3 = "hello world"
s4 = "hello world"
print(s3 is s4)         # may be True or False depending on Python version!
# Never use is for strings - use ==


# ------------------------------------------------------------
# PART 9: Membership Operators (in / not in)
# ------------------------------------------------------------

# in     - checks if value EXISTS in a collection
# not in - checks if value does NOT EXIST in a collection
# Both return True or False

# in with strings - checks for substring
text = "Hello World Python"
print("Hello"  in text)        # True
print("hello"  in text)        # False  case sensitive!
print("Python" in text)        # True
print("Java"   in text)        # False
print(""       in text)        # True   empty string is in everything!

# not in with strings
print("Java" not in text)      # True
print("Hello" not in text)     # False

# in with lists
fruits = ["apple", "banana", "cherry", "date"]
print("apple"  in fruits)      # True
print("mango"  in fruits)      # False
print("Apple"  in fruits)      # False  case sensitive!

# not in with lists
print("mango" not in fruits)   # True
print("apple" not in fruits)   # False

# in with tuples - same as lists
coords = (10, 20, 30)
print(10 in coords)            # True
print(40 in coords)            # False

# in with dictionaries - checks KEYS by default!
person = {"name": "Anna", "age": 25, "city": "Warsaw"}
print("name"  in person)       # True   ← checks keys!
print("Anna"  in person)       # False  ← "Anna" is a value, not a key!
print("Anna"  in person.values())   # True  ← check values explicitly
print("name"  in person.keys())     # True  ← explicit key check
print(("name", "Anna") in person.items())   # True  ← check pairs

# in with sets - very fast lookup!
valid_nucleotides = {"A", "T", "G", "C"}
print("A" in valid_nucleotides)     # True
print("X" in valid_nucleotides)     # False
print("a" in valid_nucleotides)     # False  case sensitive!

# in with range
print(5 in range(10))          # True   (0-9)
print(10 in range(10))         # False  (0-9, not including 10)
print(5 in range(0, 10, 2))    # False  (0,2,4,6,8)
print(4 in range(0, 10, 2))    # True   (0,2,4,6,8)


# ------------------------------------------------------------
# PART 10: Comparison in Practice
# ------------------------------------------------------------

# Pattern 1: Validating input
def is_valid_age(age):
    """Check if age is a valid human age."""
    return 0 <= age <= 150

print(is_valid_age(25))         # True
print(is_valid_age(-1))         # False
print(is_valid_age(200))        # False

# Pattern 2: Grade classification
def get_grade(score):
    """Return letter grade for a score 0-100."""
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    else:
        return "F"

print(get_grade(95))    # A
print(get_grade(83))    # B
print(get_grade(55))    # F

# Pattern 3: Checking DNA validity
dna = "ATCGGCTA"
valid_chars = {"A", "T", "G", "C"}
is_valid = all(char in valid_chars for char in dna)
print(f"Valid DNA: {is_valid}")         # True

bad_dna = "ATCGXCTA"
is_valid = all(char in valid_chars for char in bad_dna)
print(f"Valid DNA: {is_valid}")         # False

# Pattern 4: Finding min/max without built-ins
numbers = [34, 12, 67, 23, 89, 45]
maximum = numbers[0]
minimum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num
print(f"Max: {maximum}, Min: {minimum}")    # Max: 89, Min: 12

# Pattern 5: Comparing results
expected = 42
actual   = 6 * 7
print(f"Test passed: {actual == expected}")     # True

# Pattern 6: None checks
def find_value(data, target):
    """Return index of target or None if not found."""
    for i, val in enumerate(data):
        if val == target:
            return i
    return None

result = find_value([10, 20, 30], 20)
if result is not None:              # use is not None, not != None
    print(f"Found at index: {result}")
else:
    print("Not found")


# ------------------------------------------------------------
# PART 11: Common Pitfalls ⚠️
# ------------------------------------------------------------

# PITFALL 1: = vs ==
x = 5
# if x = 10:        # SyntaxError! use == not =
if x == 10:
    print("ten")

# PITFALL 2: Float comparison
print(0.1 + 0.2 == 0.3)     # False! Use math.isclose()
print(math.isclose(0.1 + 0.2, 0.3))    # True

# PITFALL 3: is vs == for values
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)       # True  ← use this for value comparison
print(a is b)       # False ← don't use is for value comparison

# PITFALL 4: Case sensitivity in string comparison
print("Hello" == "hello")   # False
# Always normalize case first:
print("Hello".lower() == "hello".lower())   # True

# PITFALL 5: String vs number comparison
age_str = "25"              # from input()
age_int = 25
print(age_str == age_int)   # False! str != int
print(int(age_str) == age_int)  # True ← convert first

# PITFALL 6: Comparing with None using ==
x = None
print(x == None)    # works but not recommended
print(x is None)    # correct! None is a singleton

# PITFALL 7: Chaining == does NOT work like you expect
x = 5
print(1 == x == 1)              # False (1==5 is False)
print(1 < x < 10)               # True  (this works!)
# print("a" == "a" == "b")      # False (not the same as "a"=="a" or "a"=="b")

# PITFALL 8: NaN comparisons
nan = float("nan")
print(nan == nan)           # False! NaN != NaN by definition
print(nan != nan)           # True!
print(math.isnan(nan))      # True  ← correct way to check


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ ==          equal to (value)
# ✅ !=          not equal to (value)
# ✅ >  <        strictly greater/less than
# ✅ >= <=       greater/less than OR equal to
# ✅ Chaining    1 < x < 10  (very Pythonic!)
# ✅ is          same object in memory (identity)
# ✅ is not      not same object in memory
# ✅ in          exists in collection (membership)
# ✅ not in      does not exist in collection
# ✅ math.isclose() safe float comparison
# ✅ isinstance() better than type() ==
# ⚠️  = is assignment, == is comparison
# ⚠️  0.1+0.2 != 0.3  use math.isclose()
# ⚠️  is vs ==  is checks identity, not value
# ⚠️  is None   correct, == None is discouraged
# ⚠️  "9" < "10" is False! strings compare lexicographically
# ⚠️  NaN != NaN  use math.isnan() instead
# ⚠️  in dict checks KEYS not values
# ⚠️  all comparisons are case sensitive for strings