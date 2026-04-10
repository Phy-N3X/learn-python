# ============================================================
# MODULE 01 | LECTURE 11 - Type Conversion
# ============================================================
# What you will learn:
#   - Implicit vs explicit conversion
#   - int() conversion - all cases
#   - float() conversion - all cases
#   - str() conversion - all cases
#   - bool() conversion - all cases
#   - complex() conversion
#   - Converting between collections (preview)
#   - Type checking
#   - Common patterns
#   - Common pitfalls
# ============================================================


# ------------------------------------------------------------
# PART 1: Two Types of Conversion
# ------------------------------------------------------------

# TYPE CONVERSION = changing a value from one type to another
# Also called "type casting" or "coercion"

# Python has TWO kinds:

# 1. IMPLICIT (automatic) - Python converts without asking
#    Happens when mixing compatible types in operations

print(3 + 4.0)          # 7.0  ← Python converted 3 to 3.0 automatically
print(type(3 + 4.0))    # <class 'float'>

print(True + 1)         # 2    ← Python converted True to 1 automatically
print(True + 1.5)       # 2.5  ← True → 1 → 1.0 → 2.5

# 2. EXPLICIT (manual) - YOU convert using built-in functions
#    int(), float(), str(), bool(), complex()

x = "42"
y = int(x)              # YOU explicitly converted str to int
print(y)                # 42
print(type(y))          # <class 'int'>

# Rule: Python only does implicit conversion when it is SAFE
# It will NEVER implicitly convert str to int (could lose data)
# print("5" + 3)        # TypeError! Python refuses to guess


# ------------------------------------------------------------
# PART 2: Implicit Type Conversion
# ------------------------------------------------------------

# Python promotes to the "wider" type automatically:
# bool → int → float → complex

# bool to int:
print(True  + 0)        # 1    (True  → 1)
print(False + 0)        # 0    (False → 0)
print(True  * 10)       # 10
print(False * 10)       # 0

# int to float:
print(1 + 2.0)          # 3.0
print(10 / 3)           # 3.3333... ← division ALWAYS produces float
print(10 * 1.0)         # 10.0

# int to complex:
print(3 + 2j)           # (3+2j) ← int and complex
print(type(3 + 2j))     # <class 'complex'>

# The promotion chain:
a = True                # bool
b = a + 1               # bool + int = int
c = b + 1.0             # int + float = float
d = c + 1j              # float + complex = complex

print(f"bool:    {a} → {type(a)}")
print(f"int:     {b} → {type(b)}")
print(f"float:   {c} → {type(c)}")
print(f"complex: {d} → {type(d)}")

# String is NEVER implicitly converted:
# print("3" + 3)        # TypeError!
# print("3" * 1.5)      # TypeError!
# print("3" > 3)        # TypeError! (in Python 3)


# ------------------------------------------------------------
# PART 3: int() Conversion - All Cases
# ------------------------------------------------------------

# int() converts to integer
# Syntax: int(value, base=10)

# --- From float ---
print(int(3.9))         # 3    ← truncates toward zero (NOT rounds!)
print(int(3.1))         # 3    ← truncates
print(int(-3.9))        # -3   ← toward zero, NOT -4!
print(int(-3.1))        # -3   ← toward zero
print(int(0.9999))      # 0    ← still truncates!

# int() TRUNCATES - it does NOT round!
# Use round() if you want rounding
print(round(3.9))       # 4    ← rounds
print(int(3.9))         # 3    ← truncates

# --- From string ---
print(int("42"))        # 42
print(int("0"))         # 0
print(int("-17"))       # -17
print(int("  42  "))    # 42   ← strips whitespace automatically!

# String must be a valid INTEGER (no decimal point!)
# print(int("3.14"))    # ValueError!
# print(int("hello"))   # ValueError!
# print(int("42abc"))   # ValueError!
# print(int(""))        # ValueError!

# Convert float string: must go through float first!
print(int(float("3.14")))   # 3

# --- From string with different base ---
print(int("1010", 2))   # 10   ← binary (base 2)
print(int("FF",  16))   # 255  ← hexadecimal (base 16)
print(int("77",   8))   # 63   ← octal (base 8)
print(int("z",   36))   # 35   ← base 36

# --- From bool ---
print(int(True))        # 1
print(int(False))       # 0

# --- From complex ---
# print(int(3+2j))      # TypeError! cannot convert complex to int

# --- What FAILS ---
# print(int(None))      # TypeError!
# print(int([1,2]))     # TypeError!
# print(int("3.14"))    # ValueError! (has decimal point)
# print(int("3,14"))    # ValueError! (comma not valid)


# ------------------------------------------------------------
# PART 4: float() Conversion - All Cases
# ------------------------------------------------------------

# float() converts to floating point number

# --- From int ---
print(float(42))        # 42.0
print(float(-17))       # -17.0
print(float(0))         # 0.0

# --- From string ---
print(float("3.14"))    # 3.14
print(float("42"))      # 42.0  ← integer string works too!
print(float("-17.5"))   # -17.5
print(float("  3.14 ")) # 3.14  ← strips whitespace!
print(float("1e10"))    # 10000000000.0  ← scientific notation!
print(float("1.5e-3"))  # 0.0015
print(float("inf"))     # inf
print(float("-inf"))    # -inf
print(float("nan"))     # nan

# What fails:
# print(float("hello"))     # ValueError!
# print(float("3,14"))      # ValueError! (comma not valid)
# print(float(""))           # ValueError!
# print(float(None))         # TypeError!
# print(float([1.0]))        # TypeError!

# --- From bool ---
print(float(True))      # 1.0
print(float(False))     # 0.0

# --- From complex ---
# print(float(3+2j))    # TypeError! cannot convert complex to float

# --- Special float values ---
print(float("inf"))             # inf
print(float("-inf"))            # -inf
print(float("nan"))             # nan
import math
print(math.isinf(float("inf"))) # True
print(math.isnan(float("nan"))) # True


# ------------------------------------------------------------
# PART 5: str() Conversion - All Cases
# ------------------------------------------------------------

# str() converts ANYTHING to its string representation
# It almost never fails!

# --- From numbers ---
print(str(42))          # "42"
print(str(-17))         # "-17"
print(str(3.14))        # "3.14"
print(str(1e10))        # "10000000000.0"
print(str(1.5e-10))     # "1.5e-10"
print(str(True))        # "True"
print(str(False))       # "False"
print(str(None))        # "None"

# --- From complex ---
print(str(3+2j))        # "(3+2j)"
print(str(3+0j))        # "(3+0j)"

# --- From collections (preview) ---
print(str([1, 2, 3]))   # "[1, 2, 3]"
print(str((1, 2, 3)))   # "(1, 2, 3)"
print(str({"a": 1}))    # "{'a': 1}"
print(str({1, 2, 3}))   # "{1, 2, 3}"

# --- str() vs repr() ---
# str()  → human-readable output
# repr() → developer-friendly, shows exact type info

text = "hello\nworld"
print(str(text))        # hello
                        # world     ← \n becomes newline
print(repr(text))       # 'hello\nworld'  ← shows \n literally

print(str(3.14))        # 3.14
print(repr(3.14))       # 3.14      ← same for numbers

print(str(None))        # None
print(repr(None))       # None      ← same

# --- Format vs str() ---
pi = 3.14159265
print(str(pi))          # 3.14159265  ← all digits
print(f"{pi:.2f}")      # 3.14        ← controlled format
print(f"{pi:.4f}")      # 3.1416

# str() gives full representation
# f-string gives formatted representation


# ------------------------------------------------------------
# PART 6: bool() Conversion - All Cases
# ------------------------------------------------------------

# bool() converts to True or False
# Follows truthy/falsy rules from Lecture 04 and 10

# --- Falsy values → False ---
print(bool(0))          # False
print(bool(0.0))        # False
print(bool(0j))         # False
print(bool(""))         # False
print(bool([]))         # False
print(bool({}))         # False
print(bool(()))         # False
print(bool(set()))      # False
print(bool(None))       # False
print(bool(False))      # False

# --- Truthy values → True ---
print(bool(1))          # True
print(bool(-1))         # True    ← negative is truthy!
print(bool(0.001))      # True
print(bool("hello"))    # True
print(bool("False"))    # True    ← non-empty string!
print(bool("0"))        # True    ← non-empty string!
print(bool([0]))        # True    ← list with element (even 0)
print(bool([False]))    # True    ← list with element (even False)
print(bool(True))       # True

# --- Common mistake with bool() ---
# bool("False") is True!  "False" is a non-empty string
raw_input = "False"
print(bool(raw_input))      # True ← WRONG if you expect False!

# Correct way to convert string to bool:
def str_to_bool(s):
    """Convert string representation to bool."""
    return s.strip().lower() in ("true", "yes", "1", "y", "on")

print(str_to_bool("True"))      # True
print(str_to_bool("False"))     # False
print(str_to_bool("yes"))       # True
print(str_to_bool("no"))        # False
print(str_to_bool("1"))         # True
print(str_to_bool("0"))         # False


# ------------------------------------------------------------
# PART 7: complex() Conversion
# ------------------------------------------------------------

# complex() creates complex numbers
# Syntax: complex(real, imag) or complex(string)

# --- From numbers ---
print(complex(3))           # (3+0j)  ← just real part
print(complex(3, 4))        # (3+4j)  ← real and imaginary
print(complex(0, 1))        # 1j
print(complex(-2, -3))      # (-2-3j)
print(complex(3.14, 2.71))  # (3.14+2.71j)

# --- From string ---
print(complex("3+4j"))      # (3+4j)
print(complex("3j"))        # 3j
print(complex("3"))         # (3+0j)
# Note: NO space allowed in string!
# print(complex("3 + 4j"))  # ValueError!

# --- From bool ---
print(complex(True))        # (1+0j)
print(complex(False))       # 0j

# --- Accessing parts ---
c = 3 + 4j
print(c.real)               # 3.0
print(c.imag)               # 4.0
print(abs(c))               # 5.0   ← magnitude: √(3²+4²)
print(c.conjugate())        # (3-4j)


# ------------------------------------------------------------
# PART 8: Conversion Between Collections (Preview)
# ------------------------------------------------------------

# These will be covered fully in later modules
# but here is a taste of type conversion with collections

# str → list (each character becomes element)
print(list("hello"))        # ['h', 'e', 'l', 'l', 'o']
print(list("ATCG"))         # ['A', 'T', 'C', 'G']

# str → tuple
print(tuple("hello"))       # ('h', 'e', 'l', 'l', 'o')

# str → set (unique characters only!)
print(set("hello"))         # {'h', 'e', 'l', 'o'}  ← no duplicate 'l'
print(set("ATCGATCG"))      # {'A', 'T', 'C', 'G'}

# list → tuple
print(tuple([1, 2, 3]))     # (1, 2, 3)

# list → set (removes duplicates!)
print(set([1, 2, 2, 3, 3, 3]))  # {1, 2, 3}

# set → list
print(list({1, 2, 3}))      # [1, 2, 3] (order not guaranteed!)

# tuple → list
print(list((1, 2, 3)))      # [1, 2, 3]

# range → list
print(list(range(5)))       # [0, 1, 2, 3, 4]
print(list(range(1, 10, 2)))# [1, 3, 5, 7, 9]

# Practical: remove duplicates while preserving order
def unique_ordered(items):
    """Remove duplicates preserving original order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print(unique_ordered(data))     # [3, 1, 4, 5, 9, 2, 6]


# ------------------------------------------------------------
# PART 9: Type Checking
# ------------------------------------------------------------

# type() - returns the exact type
x = 42
print(type(x))              # <class 'int'>
print(type(x) == int)       # True
print(type(x) == float)     # False

# isinstance() - checks if object is instance of type (or subclass!)
print(isinstance(x, int))           # True
print(isinstance(x, float))         # False
print(isinstance(x, (int, float)))  # True  ← check multiple types!
print(isinstance(True, int))        # True  ← bool IS a subclass of int!
print(isinstance(True, bool))       # True

# type() vs isinstance():
print(type(True) == int)        # False ← type() checks exact type
print(isinstance(True, int))    # True  ← isinstance() checks hierarchy

# isinstance() is almost always better:
def process_number(n):
    """Process a numeric value."""
    if isinstance(n, bool):         # check bool FIRST (before int!)
        return f"Boolean: {n}"
    elif isinstance(n, int):
        return f"Integer: {n}"
    elif isinstance(n, float):
        return f"Float: {n}"
    else:
        return f"Not a number: {type(n)}"

print(process_number(True))     # Boolean: True
print(process_number(42))       # Integer: 42
print(process_number(3.14))     # Float: 3.14
print(process_number("hello"))  # Not a number: <class 'str'>

# hasattr() - check if object has an attribute (duck typing)
print(hasattr(42, "__add__"))   # True  ← int has addition
print(hasattr("hi", "upper"))   # True  ← str has upper()
print(hasattr(42, "upper"))     # False ← int has no upper()


# ------------------------------------------------------------
# PART 10: Conversion Patterns in Practice
# ------------------------------------------------------------

# Pattern 1: Safe int conversion
def safe_int(value, default=0):
    """
    Safely convert value to int.

    Args:
        value: Value to convert.
        default: Return value if conversion fails.

    Returns:
        int: Converted value or default.
    """
    try:
        return int(float(str(value).strip()))
    except (ValueError, TypeError):
        return default

print(safe_int("42"))       # 42
print(safe_int("3.14"))     # 3
print(safe_int("hello"))    # 0
print(safe_int(None))       # 0
print(safe_int(""))         # 0
print(safe_int("  25  "))   # 25

# Pattern 2: Safe float conversion
def safe_float(value, default=0.0):
    """
    Safely convert value to float.

    Args:
        value: Value to convert.
        default: Return value if conversion fails.

    Returns:
        float: Converted value or default.
    """
    try:
        return float(str(value).strip())
    except (ValueError, TypeError):
        return default

print(safe_float("3.14"))   # 3.14
print(safe_float("hello"))  # 0.0
print(safe_float(None))     # 0.0

# Pattern 3: Convert number to different bases
def to_binary(n):
    """Convert integer to binary string."""
    return bin(n)[2:]           # bin() returns "0b1010", [2:] removes "0b"

def to_hex(n):
    """Convert integer to hexadecimal string."""
    return hex(n)[2:].upper()   # hex() returns "0xff", [2:] removes "0x"

def to_octal(n):
    """Convert integer to octal string."""
    return oct(n)[2:]           # oct() returns "0o77", [2:] removes "0o"

print(to_binary(42))        # 101010
print(to_hex(255))          # FF
print(to_octal(63))         # 77

# Convert back:
print(int("101010", 2))     # 42
print(int("FF", 16))        # 255
print(int("77", 8))         # 63

# Pattern 4: Normalize user input
def normalize_input(raw):
    """
    Normalize raw user input to clean string.

    Args:
        raw (str): Raw input string.

    Returns:
        str: Cleaned, normalized string.
    """
    return str(raw).strip().lower()

print(normalize_input("  HELLO  "))    # hello
print(normalize_input(42))             # 42  ← even non-strings work
print(normalize_input(None))           # none

# Pattern 5: Type-safe arithmetic
def add_numbers(a, b):
    """
    Add two values, converting to numbers first.

    Args:
        a: First value.
        b: Second value.

    Returns:
        float: Sum of a and b.
    """
    return float(a) + float(b)

print(add_numbers(3, 4))            # 7.0
print(add_numbers("3", "4"))        # 7.0  ← works with strings!
print(add_numbers(3, "4.5"))        # 7.5  ← mixed types!

# Pattern 6: Boolean from various inputs
def to_bool(value):
    """
    Convert various representations to bool.

    Args:
        value: Value to convert.

    Returns:
        bool: Boolean interpretation of value.
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return value != 0
    if isinstance(value, str):
        return value.strip().lower() in ("true", "yes", "1", "y", "on")
    return bool(value)

print(to_bool(True))        # True
print(to_bool(1))           # True
print(to_bool(0))           # False
print(to_bool("true"))      # True
print(to_bool("False"))     # False
print(to_bool("yes"))       # True
print(to_bool("no"))        # False
print(to_bool([1, 2]))      # True  ← non-empty list


# ------------------------------------------------------------
# PART 11: Common Pitfalls ⚠️
# ------------------------------------------------------------

# PITFALL 1: int() truncates, doesn't round
print(int(3.9))             # 3  not 4!
print(int(-3.9))            # -3 not -4!
print(round(3.9))           # 4  ← use round() for rounding

# PITFALL 2: int() fails on float strings
# print(int("3.14"))        # ValueError!
print(int(float("3.14")))   # 3  ← convert via float first

# PITFALL 3: bool("False") is True!
print(bool("False"))        # True  ← "False" is non-empty string!
print(bool("0"))            # True  ← "0" is non-empty string!
# Use str_to_bool() function from Part 6

# PITFALL 4: str() on None gives "None", not ""
x = None
print(str(x))               # "None"  ← the string "None"!
print(str(x) == "")         # False
print(str(x) == "None")     # True
# If you want empty string from None:
result = "" if x is None else str(x)
print(result)               # ""

# PITFALL 5: float precision after conversion
print(int(0.9999999999999999))  # 1  ← float precision rounds it!
print(0.9999999999999999 == 1)  # True! (float precision)
print(int(0.999))               # 0   ← this is 0 as expected

# PITFALL 6: Lost precision int → float → int
big = 9999999999999999
print(big)                  # 9999999999999999
print(float(big))           # 1e+16  ← precision lost!
print(int(float(big)))      # 10000000000000000  ← different!

# PITFALL 7: type() vs isinstance() for bool
print(type(True) == int)        # False ← True IS int but type check fails
print(isinstance(True, int))    # True  ← correct!
# Always use isinstance() not type() == for type checking

# PITFALL 8: Division always returns float
result = int(10) / int(2)
print(result)               # 5.0  not 5!
print(type(result))         # float
# Use // for integer division:
result = int(10) // int(2)
print(result)               # 5
print(type(result))         # int

# PITFALL 9: Complex cannot convert to int/float
c = 3 + 0j
# print(int(c))             # TypeError! even if imaginary is 0
# print(float(c))           # TypeError!
print(int(c.real))          # 3  ← access .real first


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Implicit conversion  Python handles automatically (safe only)
# ✅ Explicit conversion  you call int() float() str() bool()
# ✅ Promotion chain      bool → int → float → complex
# ✅ int(x)              truncates float toward zero
# ✅ int("42")           works, int("3.14") fails!
# ✅ int("FF", 16)       convert from different base
# ✅ float(x)            works with int, bool, valid strings
# ✅ float("inf")        special: inf, -inf, nan
# ✅ str(x)              works with almost everything
# ✅ bool(x)             follows truthy/falsy rules
# ✅ complex(r, i)       create complex number
# ✅ type()              exact type check
# ✅ isinstance()        type check with inheritance (preferred)
# ✅ bin() hex() oct()   convert int to string in other base
# ✅ int("FF", 16)       convert string in base to int
# ⚠️  int() truncates    does NOT round - use round() for that
# ⚠️  int("3.14") fails  use int(float("3.14")) instead
# ⚠️  bool("False")=True non-empty string is always True!
# ⚠️  str(None)="None"   not empty string
# ⚠️  type(True)==int    False! use isinstance(True, int)
# ⚠️  10/2 = 5.0        division always returns float
# ⚠️  int(complex) fails access .real first