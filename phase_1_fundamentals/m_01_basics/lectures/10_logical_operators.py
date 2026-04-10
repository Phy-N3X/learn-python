# ============================================================
# MODULE 01 | LECTURE 10 - Logical Operators
# ============================================================
# What you will learn:
#   - and, or, not in depth
#   - Truth tables
#   - Short-circuit evaluation
#   - Operator precedence with logical operators
#   - Truthy and Falsy values (deep dive)
#   - and/or returning original values
#   - Logical operators in practice
#   - De Morgan's Laws
#   - Common pitfalls
# ============================================================


# ------------------------------------------------------------
# PART 1: The Three Logical Operators
# ------------------------------------------------------------

# Python has exactly three logical operators:
# and  - True if BOTH operands are True
# or   - True if AT LEAST ONE operand is True
# not  - reverses the boolean value

# Basic syntax:
print(True and True)        # True
print(True and False)       # False
print(False and True)       # False
print(False and False)      # False

print(True or True)         # True
print(True or False)        # True
print(False or True)        # True
print(False or False)       # False

print(not True)             # False
print(not False)            # True

# They always work with any values - not just booleans
# (more on this in Part 5 and Part 6)


# ------------------------------------------------------------
# PART 2: Truth Tables - Complete Reference
# ------------------------------------------------------------

# AND truth table:
# A      B      A and B
# True   True   True
# True   False  False
# False  True   False
# False  False  False
# RULE: both must be True → result is True

# OR truth table:
# A      B      A or B
# True   True   True
# True   False  True
# False  True   True
# False  False  False
# RULE: at least one must be True → result is True

# NOT truth table:
# A      not A
# True   False
# False  True
# RULE: simply reverses the value

# Print all combinations programmatically:
print("\n--- AND truth table ---")
for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<6} and {str(b):<6} = {a and b}")

print("\n--- OR truth table ---")
for a in [True, False]:
    for b in [True, False]:
        print(f"{str(a):<6} or  {str(b):<6} = {a or b}")

print("\n--- NOT truth table ---")
for a in [True, False]:
    print(f"not {str(a):<6} = {not a}")


# ------------------------------------------------------------
# PART 3: Combining Logical Operators
# ------------------------------------------------------------

# You can combine multiple logical operators
# Use parentheses to make intent clear!

a = True
b = False
c = True

# Combining and + or:
print(a and b or c)             # True  → (a and b) or c → False or True
print(a and (b or c))           # True  → a and (False or True) → True and True
print(a or b and c)             # True  → a or (b and c) → True or False
print((a or b) and c)           # True  → True and True

# Combining not with and/or:
print(not a and b)              # False → (not True) and False → False and False
print(not (a and b))            # True  → not False → True
print(not a or b)               # False → False or False
print(not (a or b))             # False → not True

# Three or more conditions:
x = 5
print(x > 0 and x < 10 and x != 7)     # True
print(x > 0 and x < 10 and x == 5)     # True
print(x > 0 or x < -10 or x == 99)     # True  (first is True)
print(x > 10 or x < 0 or x == 99)      # False (all False)

# Real world: checking multiple conditions
age        = 25
has_license = True
has_insurance = True
car_available = False

can_drive = age >= 18 and has_license and has_insurance and car_available
print(f"Can drive: {can_drive}")        # False (car_available is False)


# ------------------------------------------------------------
# PART 4: Operator Precedence with Logical Operators
# ------------------------------------------------------------

# Full precedence order (highest to lowest):
# 1. ()          parentheses
# 2. **          exponentiation
# 3. +x -x       unary operators
# 4. * / // %    multiplication, division
# 5. + -         addition, subtraction
# 6. == != > < >= <= is in  comparisons
# 7. not         logical NOT
# 8. and         logical AND
# 9. or          logical OR

# not binds tighter than and, which binds tighter than or
# not > and > or

# Examples:
print(not True or False)        # False → (not True) or False → False or False
print(not (True or False))      # False → not True → False

print(True or False and False)  # True  → True or (False and False) → True or False
print((True or False) and False)# False → True and False → False

print(not True and not False)   # False → False and True → False
print(not (True and not False)) # False → not (True and True) → not True

# Comparison operators have higher priority than logical operators:
x = 5
print(x > 3 and x < 10)        # True  → True and True
print(x > 3 or x > 10)         # True  → True or False
print(not x > 3)                # False → not True
print(not x == 5)               # False → not True

# This means you can write:
# if x > 0 and x < 10:
# instead of:
# if (x > 0) and (x < 10):
# (parentheses around comparisons are optional but sometimes clearer)

# GOLDEN RULE: when in doubt, add parentheses!
# Explicit is better than implicit (Python Zen)


# ------------------------------------------------------------
# PART 5: Truthy and Falsy Values - Deep Dive
# ------------------------------------------------------------

# Every Python value is either Truthy or Falsy
# This is why logical operators work with ANY values

# FALSY values - treated as False in boolean context:
falsy_values = [
    False,      # bool
    None,       # NoneType
    0,          # int zero
    0.0,        # float zero
    0j,         # complex zero
    "",         # empty string
    [],         # empty list
    {},         # empty dict
    (),         # empty tuple
    set(),      # empty set
]

print("--- Falsy values ---")
for val in falsy_values:
    print(f"bool({repr(val):<12}) = {bool(val)}")

# TRUTHY values - everything else:
truthy_values = [
    True,       # bool
    1,          # any non-zero int
    -1,         # negative numbers are truthy!
    0.001,      # any non-zero float
    "hello",    # any non-empty string
    " ",        # even just a space!
    [0],        # list with one element (even False!)
    [False],    # list containing False - still truthy!
    {"a": 1},   # non-empty dict
    (0,),       # non-empty tuple
    {0},        # non-empty set
]

print("\n--- Truthy values ---")
for val in truthy_values:
    print(f"bool({repr(val):<12}) = {bool(val)}")

# Practical implications:
name = "Anna"
if name:                    # same as: if name != "" and name is not None
    print(f"Hello, {name}")

items = []
if not items:               # same as: if len(items) == 0
    print("Cart is empty")

score = 0
# CAREFUL! 0 is falsy - this might not be what you want:
if score:
    print("Has score")      # won't print even though score exists!
# Better:
if score is not None:
    print(f"Score: {score}")    # prints "Score: 0"


# ------------------------------------------------------------
# PART 6: Short-Circuit Evaluation - In Depth
# ------------------------------------------------------------

# Python is LAZY - stops evaluating as soon as result is known

# AND short-circuit:
# If first operand is Falsy → return it immediately (don't check second)
# If first operand is Truthy → evaluate and return second

# OR short-circuit:
# If first operand is Truthy → return it immediately (don't check second)
# If first operand is Falsy  → evaluate and return second

# Demonstration with side effects:
def show(name, value):
    """Return value and print that it was evaluated."""
    print(f"  evaluating {name} = {value}")
    return value

print("\n--- AND short-circuit ---")
print("False and True:")
result = show("A", False) and show("B", True)
print(f"  result: {result}")
# Only A is evaluated! B is never checked.

print("\nTrue and False:")
result = show("A", True) and show("B", False)
print(f"  result: {result}")
# Both evaluated because A was True.

print("\n--- OR short-circuit ---")
print("True or False:")
result = show("A", True) or show("B", False)
print(f"  result: {result}")
# Only A is evaluated! B is never checked.

print("\nFalse or True:")
result = show("A", False) or show("B", True)
print(f"  result: {result}")
# Both evaluated because A was False.

# Practical use 1: safe attribute access
# Without short-circuit - could crash:
text = ""
# if len(text) > 0 and text[0] == "A":    ← safe because of short-circuit

# Without short-circuit protection:
# if text[0] == "A":    ← IndexError if text is empty!

# With short-circuit:
if len(text) > 0 and text[0] == "A":
    print("Starts with A")
else:
    print("Empty or doesn't start with A")  # safe!

# Practical use 2: avoid division by zero
denominator = 0
# if denominator != 0 and (100 / denominator) > 5:
if denominator != 0 and (100 / denominator) > 5:
    print("Big ratio")
else:
    print("Zero denominator - skipped division")  # safe!

# Practical use 3: None guard
user = None
# if user and user["name"] == "Anna":   ← safe! if user is None, stops
if user and user["name"] == "Anna":
    print("Found Anna")
else:
    print("No user")    # safe - didn't try to access None["name"]


# ------------------------------------------------------------
# PART 7: and/or Return Original Values (Not Just Bool)
# ------------------------------------------------------------

# This is one of Python's most useful features!
# and returns the first Falsy value, or the LAST value if all Truthy
# or  returns the first Truthy value, or the LAST value if all Falsy

print("\n--- and returns ---")
print(1   and 2)            # 2       both truthy → returns last
print(0   and 2)            # 0       first is falsy → returns it
print(""  and "hello")      # ""      first is falsy → returns it
print("hi" and "hello")     # hello   both truthy → returns last
print(1   and 2 and 3)      # 3       all truthy → returns last
print(1   and 0 and 3)      # 0       0 is falsy → returns it

print("\n--- or returns ---")
print(1    or 2)            # 1       first is truthy → returns it
print(0    or 2)            # 2       first falsy → tries next
print(""   or "hello")      # hello   first falsy → tries next
print("hi" or "hello")      # hi      first truthy → returns it
print(0    or "" or [])     # []      all falsy → returns last
print(0    or "" or "found")# found   last is truthy → returns it

# WHY THIS MATTERS - practical patterns:

# Pattern 1: Default values
username     = ""
display_name = username or "Anonymous"
print(display_name)         # Anonymous ← username is falsy

username     = "Anna"
display_name = username or "Anonymous"
print(display_name)         # Anna ← username is truthy

# Pattern 2: First available value
config_value  = None
env_value     = None
default_value = "localhost"
host = config_value or env_value or default_value
print(host)                 # localhost

# Pattern 3: Conditional execution with and
# and as a one-line conditional (use sparingly):
debug = True
debug and print("Debug mode is ON")  # prints only if debug is True
debug = False
debug and print("Debug mode is ON")  # prints nothing

# Pattern 4: Safe method call with and
text = "hello"
result = text and text.upper()
print(result)               # HELLO

text = ""
result = text and text.upper()
print(result)               # "" ← didn't call .upper() on empty string

# Pattern 5: Ternary with or (older Python style)
# Modern Python: x = value_if_true if condition else value_if_false
# Old style:     x = condition and value_if_true or value_if_false
# (avoid old style - can have bugs with falsy values)
x = 5
result = "positive" if x > 0 else "non-positive"
print(result)               # positive ← use this modern form


# ------------------------------------------------------------
# PART 8: De Morgan's Laws
# ------------------------------------------------------------

# De Morgan's Laws are fundamental rules of boolean logic:
#
# Law 1: not (A and B)  ==  (not A) or  (not B)
# Law 2: not (A or  B)  ==  (not A) and (not B)
#
# They help simplify complex boolean expressions!

# Verify Law 1:
print("\n--- De Morgan's Law 1: not(A and B) == (not A) or (not B) ---")
for a in [True, False]:
    for b in [True, False]:
        left  = not (a and b)
        right = (not a) or (not b)
        print(f"A={a}, B={b}: {left} == {right} → {left == right}")

# Verify Law 2:
print("\n--- De Morgan's Law 2: not(A or B) == (not A) and (not B) ---")
for a in [True, False]:
    for b in [True, False]:
        left  = not (a or b)
        right = (not a) and (not b)
        print(f"A={a}, B={b}: {left} == {right} → {left == right}")

# Practical application:
# Original condition (hard to read):
age     = 25
is_vip  = False

# if not (age >= 18 and is_vip):   ← confusing
#     print("Access denied")

# After applying De Morgan's Law 1:
# not (age >= 18 and is_vip)
# = (not age >= 18) or (not is_vip)
# = age < 18 or not is_vip

if age < 18 or not is_vip:         # ← clearer!
    print("Access denied")

# Another example:
# Original: not (x == 0 or y == 0)
# De Morgan: x != 0 and y != 0
x, y = 5, 3
print(not (x == 0 or y == 0))      # True
print(x != 0 and y != 0)           # True  ← same result, more readable

# When to use De Morgan's Laws:
# - Simplify negations of complex conditions
# - Make if/else conditions more readable
# - Convert between and/or when refactoring


# ------------------------------------------------------------
# PART 9: Logical Operators in Practice
# ------------------------------------------------------------

# Pattern 1: Input validation
def is_valid_username(username):
    """
    Validate a username.

    Args:
        username (str): Username to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # All conditions must be True:
    has_length    = 3 <= len(username) <= 20
    no_spaces     = " " not in username
    not_empty     = bool(username)          # truthy check
    return has_length and no_spaces and not_empty

print(is_valid_username("anna"))        # True
print(is_valid_username(""))            # False
print(is_valid_username("a b"))         # False
print(is_valid_username("x" * 25))     # False (too long)

# Pattern 2: Feature flags
is_admin  = True
is_logged = True
has_perm  = False

can_edit   = is_logged and (is_admin or has_perm)
can_delete = is_logged and is_admin
can_view   = is_logged or is_admin

print(f"Edit:   {can_edit}")    # True  (admin)
print(f"Delete: {can_delete}")  # True  (admin)
print(f"View:   {can_view}")    # True  (logged in)

# Pattern 3: Complex filter
def should_include(item, min_price, max_price, in_stock):
    """Check if item meets filter criteria."""
    price_ok   = min_price <= item["price"] <= max_price
    stock_ok   = not in_stock or item["in_stock"]
    return price_ok and stock_ok

products = [
    {"name": "Widget",  "price": 25,  "in_stock": True},
    {"name": "Gadget",  "price": 150, "in_stock": False},
    {"name": "Doohickey","price": 75, "in_stock": True},
]

for product in products:
    if should_include(product, 20, 100, in_stock=True):
        print(f"Include: {product['name']}")

# Pattern 4: Early exit with or
def find_first_positive(numbers):
    """Return first positive number or None."""
    for n in numbers:
        if n > 0:
            return n
    return None

result = find_first_positive([-3, -1, 5, 2, -4])
found  = result or "No positive number"
print(found)    # 5

# Pattern 5: all() and any() - logical operators for collections
scores    = [85, 92, 78, 96, 88]
threshold = 60

all_passing  = all(score >= threshold for score in scores)
any_failing  = any(score < threshold  for score in scores)
any_perfect  = any(score == 100       for score in scores)

print(f"All passing: {all_passing}")    # True
print(f"Any failing: {any_failing}")    # False
print(f"Any perfect: {any_perfect}")    # False

# all() returns True if ALL elements are truthy
# any() returns True if ANY element is truthy
print(all([True, True, True]))          # True
print(all([True, False, True]))         # False
print(any([False, False, True]))        # True
print(any([False, False, False]))       # False


# ------------------------------------------------------------
# PART 10: Common Pitfalls ⚠️
# ------------------------------------------------------------

# PITFALL 1: and/or precedence vs not
print(not True or False)        # False → (not True) or False
print(not (True or False))      # False → not True
# These are different! Use parentheses when unsure.

# PITFALL 2: or doesn't mean "either or both" in English
# "You must be 18 or have parental consent"
age = 16
has_consent = True
# WRONG reading: exactly one must be True (that's XOR)
# CORRECT reading: at least one must be True (that's or)
can_proceed = age >= 18 or has_consent
print(can_proceed)      # True ← correct!

# PITFALL 3: not in vs != combined with membership
fruits = ["apple", "banana"]
# WRONG:
print(not "mango" in fruits)    # True but confusing
# CORRECT:
print("mango" not in fruits)    # True ← clearer!

# PITFALL 4: Chaining or for equality check
x = 5
# WRONG - this doesn't do what you think!
print(x == 3 or 5)              # 5 ← not True/False!
# "x == 3 or 5" = "(x==3) or 5" = "False or 5" = 5 (truthy)
# CORRECT:
print(x == 3 or x == 5)         # True ← correct!
print(x in [3, 5])              # True ← even better!

# PITFALL 5: and for "either" in common speech
# "Check if both name and age are provided"
name = "Anna"
age  = 0         # age IS provided but it's 0 (falsy!)
# WRONG:
if name and age:
    print("Both provided")      # won't print! 0 is falsy
# CORRECT:
if name and age is not None:
    print("Both provided")      # prints correctly

# PITFALL 6: Modifying variable with or default
# The "or default" pattern fails for 0, "", False, []
score = 0
display = score or "No score"
print(display)      # "No score" ← WRONG! score IS 0, which is valid
# CORRECT:
display = score if score is not None else "No score"
print(display)      # 0 ← correct!

# PITFALL 7: not not idiom
x = "hello"
print(not not x)    # True ← converts to bool (unusual, use bool() instead)
print(bool(x))      # True ← clearer!

# PITFALL 8: De Morgan applied incorrectly
x = 5
# Original: not (x > 3 and x < 10)
# WRONG De Morgan: not x > 3 and not x < 10
# (This is: (not x > 3) and (not x < 10) due to precedence)
# CORRECT De Morgan: (not x > 3) or (not x < 10)
#                  = x <= 3 or x >= 10
print(not (x > 3 and x < 10))          # False
print((not x > 3) or (not x < 10))     # False ← same!
print(x <= 3 or x >= 10)               # False ← same, most readable!


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ and         both must be True → True
# ✅ or          at least one True → True
# ✅ not         reverses boolean value
# ✅ Precedence  not > and > or  (comparisons bind tighter than all!)
# ✅ Short-circuit and stops on first Falsy
# ✅ Short-circuit or  stops on first Truthy
# ✅ and returns first Falsy or last value
# ✅ or  returns first Truthy or last value
# ✅ Falsy: False None 0 0.0 "" [] {} () set()
# ✅ Truthy: everything else
# ✅ De Morgan: not(A and B) == (not A) or (not B)
# ✅ De Morgan: not(A or B)  == (not A) and (not B)
# ✅ all()  True if ALL elements truthy
# ✅ any()  True if ANY element truthy
# ⚠️  not True or False  !=  not (True or False)
# ⚠️  x == 3 or 5  is NOT  x == 3 or x == 5
# ⚠️  "or default" fails for 0, "", False, []
# ⚠️  0 is falsy but is a valid value - use is not None
# ⚠️  "not x in y" works but "x not in y" is clearer