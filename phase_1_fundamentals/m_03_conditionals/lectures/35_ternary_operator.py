# ============================================================
# MODULE 03 | LECTURE 35 - One-line if (Ternary Operator)
# ============================================================
# What you will learn:
# - What the ternary operator is
# - Syntax and how to read it
# - How it differs from regular if/else
# - When to use it and when NOT to use it
# - Nested ternary operators (and why to avoid them)
# - Common patterns and idioms
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is the ternary operator?
# ------------------------------------------------------------

# So far, if/else always takes multiple lines:
#
# if condition:
#     value_A
# else:
#     value_B
#
# Sometimes this feels like a lot of code for a simple decision.
# Python offers a shorter, one-line version called
# the TERNARY OPERATOR (or conditional expression).
#
# The word "ternary" means "consisting of three parts".
# The three parts are:
# 1. The value if True
# 2. The condition
# 3. The value if False
#
# Real life analogy:
# "I'll take an umbrella IF it's raining, OTHERWISE sunglasses"
# → one sentence, one decision, two possible outcomes
#
# In Python it looks like this:
# value_if_true  if  condition  else  value_if_false
#
# You read it left to right, just like English:
# "Give me THIS if CONDITION is true, otherwise give me THAT"

# ------------------------------------------------------------
# PART 2: Basic syntax
# ------------------------------------------------------------

# Syntax:
#     result = value_if_true if condition else value_if_false
#
# Compared to regular if/else:
#
# Regular (3 lines):           Ternary (1 line):
# if x > 0:                    label = "positive" if x > 0 else "not positive"
#     label = "positive"
# else:
#     label = "not positive"
#
# Both produce EXACTLY the same result.

# Simplest example:

x = 10
label = "positive" if x > 0 else "not positive"
print(label)    # positive

x = -5
label = "positive" if x > 0 else "not positive"
print(label)    # not positive

# The ternary expression EVALUATES to a value.
# You can use it anywhere a value is expected:
# - in assignment
# - inside print()
# - inside f-strings
# - as function arguments
# - in calculations

# Using directly in print():
age = 20
print("adult" if age >= 18 else "minor")    # adult

# Using inside f-string:
score = 75
result = f"You {'passed' if score >= 60 else 'failed'} the exam!"
print(result)    # You passed the exam!

# Using in a calculation:
is_member = True
price = 100
final_price = price * 0.8 if is_member else price
print(final_price)    # 80.0

# ------------------------------------------------------------
# PART 3: Reading ternary expressions
# ------------------------------------------------------------

# The key to reading ternary expressions is to find 'if' and 'else'
# and understand what each part means.
#
# Example:
# result = "even" if number % 2 == 0 else "odd"
#
# Read as:
# result = ...
#          "even"           ← value if True
#                   if     ← separator
#          number % 2 == 0 ← the condition
#                        else ← separator
#                   "odd"  ← value if False
#
# Translation: "result gets 'even' if number is divisible by 2,
#               otherwise result gets 'odd'"

number = 7
result = "even" if number % 2 == 0 else "odd"
print(result)    # odd

number = 8
result = "even" if number % 2 == 0 else "odd"
print(result)    # even

# More examples with annotations:

temperature = 35
#   ↓ value if True      ↓ condition         ↓ value if False
msg = "hot"        if temperature > 30 else "not hot"
print(msg)    # hot

name = ""
#      ↓ value if True  ↓ condition  ↓ value if False
display = name         if name      else "Anonymous"
print(display)    # Anonymous  (empty string is falsy)

# ------------------------------------------------------------
# PART 4: Ternary vs regular if/else - when to use which
# ------------------------------------------------------------

# The ternary operator is NOT always better.
# It's a TOOL, and like any tool, it has the right use cases.

# ✅ USE TERNARY WHEN:
# - Simple assignment based on one condition
# - Short values that fit comfortably on one line
# - The logic is easy to read at a glance
# - Inside f-strings for simple decisions

# ❌ AVOID TERNARY WHEN:
# - You need to execute multiple statements
# - The condition or values are long/complex
# - You need elif (multiple branches)
# - Readability suffers (line too long or hard to understand)

# Example: ternary makes sense here

is_weekend = True
day_type = "weekend" if is_weekend else "weekday"
print(f"Today is a {day_type}")    # Today is a weekend

# Example: regular if/else is better here

temperature = 35

# ❌ Too complex for ternary - forced and hard to read:
action = "drink water and find shade and avoid direct sunlight" if temperature > 30 else "enjoy the weather"

# ✅ Better as regular if/else:
if temperature > 30:
    print("Drink water")
    print("Find shade")
    print("Avoid direct sunlight")
else:
    print("Enjoy the weather")

# Example: multiple statements - ternary CANNOT do this

score = 85

# ❌ This is NOT valid Python - ternary can't run two statements:
# (print("Good") and print("Well done")) if score >= 60 else print("Failed")

# ✅ Use regular if/else when multiple lines needed:
if score >= 60:
    print("Good")
    print("Well done")
else:
    print("Failed")

# The Golden Rule:
# ┌────────────────────────────────────────────────────────┐
# │ If the ternary expression makes code CLEARER → use it  │
# │ If it makes code HARDER to read → use regular if/else  │
# └────────────────────────────────────────────────────────┘

# ------------------------------------------------------------
# PART 5: Ternary in different contexts
# ------------------------------------------------------------

# Context 1: Simple variable assignment (most common use)

age = 22
status = "adult" if age >= 18 else "minor"
print(status)    # adult

is_logged_in = False
greeting = "Welcome back!" if is_logged_in else "Please log in"
print(greeting)    # Please log in

# Context 2: Inside print() directly

x = -7
print("positive" if x > 0 else "non-positive")    # non-positive
print(f"The number {x} is {'even' if x % 2 == 0 else 'odd'}")
# The number -7 is odd

# Context 3: Inside f-strings

score = 95
report = f"Score: {score} - {'PASS ✅' if score >= 60 else 'FAIL ❌'}"
print(report)    # Score: 95 - PASS ✅

name = "Anna"
message = f"Hello, {'dear ' + name if name else 'stranger'}!"
print(message)    # Hello, dear Anna!

name = ""
message = f"Hello, {'dear ' + name if name else 'stranger'}!"
print(message)    # Hello, stranger!

# Context 4: As function arguments

def greet(name):
    print(f"Hello, {name}!")

username = "Bob"
greet(username if username else "Guest")    # Hello, Bob!

username = ""
greet(username if username else "Guest")    # Hello, Guest!

# Context 5: In mathematical expressions

price = 100
discount_rate = 0.2 if True else 0    # is_member = True
discounted = price * (1 - discount_rate)
print(f"Price after discount: {discounted}")    # Price after discount: 80.0

# Context 6: In list/string operations

items_count = 3
summary = f"{items_count} {'item' if items_count == 1 else 'items'} in cart"
print(summary)    # 3 items in cart

items_count = 1
summary = f"{items_count} {'item' if items_count == 1 else 'items'} in cart"
print(summary)    # 1 item in cart

# ------------------------------------------------------------
# PART 6: Default values with ternary
# ------------------------------------------------------------

# One of the most common real-world uses:
# providing a default value when something is empty/None/falsy.

# Pattern: value = input_value if input_value else default_value

# Example 1: Default username

username = input("Enter username (or press Enter for Guest): ")
display_name = username if username else "Guest"
print(f"Hello, {display_name}!")

# Example 2: Default values from calculations

def get_user_score():
    return None    # simulating no score yet

raw_score = get_user_score()
score = raw_score if raw_score is not None else 0
print(f"Score: {score}")    # Score: 0

# Example 3: Fallback text

description = ""
display = description if description else "No description available"
print(display)    # No description available

# Example 4: Handling zero vs None differently

value = 0
# ❌ Wrong - 0 is falsy, treated same as None:
result = value if value else "no value"
print(result)    # no value  ← but 0 IS a valid value!

# ✅ Correct - check for None specifically:
result = value if value is not None else "no value"
print(result)    # 0  ← correctly treats 0 as valid

# This is an important subtlety!
# 'if value' catches all falsy values (0, "", [], None)
# 'if value is not None' only catches None specifically

# ------------------------------------------------------------
# PART 7: Ternary with string operations
# ------------------------------------------------------------

# Ternary works great for small string decisions.

# Example 1: Pluralization

count = 5
word = "apple" if count == 1 else "apples"
print(f"You have {count} {word}")    # You have 5 apples

count = 1
word = "apple" if count == 1 else "apples"
print(f"You have {count} {word}")    # You have 1 apple

# Example 2: Yes/No display

is_active = True
display = "Yes" if is_active else "No"
print(f"Account active: {display}")    # Account active: Yes

# Example 3: Emoji indicator

temperature = 25
emoji = "☀" if temperature > 20 else "🌧"
print(f"{emoji} {temperature}°C")    # ☀ 25°C

# Example 4: Pass/Fail with color codes (terminal colors)

score = 85
indicator = "✅ PASS" if score >= 60 else "❌ FAIL"
print(f"Result: {indicator}")    # Result: ✅ PASS

# Example 5: Direction indicator

value_change = -15
arrow = "↑" if value_change > 0 else ("→" if value_change == 0 else "↓")
print(f"Change: {arrow} {abs(value_change)}")    # Change: ↓ 15

# (Note: the above uses a nested ternary - we'll discuss this next)

# ------------------------------------------------------------
# PART 8: Nested ternary operators
# ------------------------------------------------------------

# You CAN nest ternary operators inside each other.
# This handles the "elif" case in one line.
# But use with EXTREME caution - it gets confusing fast.

# Syntax:
# value_A if condition_1 else value_B if condition_2 else value_C
#
# Python reads this as:
# value_A if condition_1 else (value_B if condition_2 else value_C)

# Example: grade letter (simple version)

score = 75

# Nested ternary:
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(grade)    # C

# This is equivalent to:
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(grade)    # C

# The nested ternary works but is hard to read.
# With more than 2 levels it becomes nearly unreadable:

# ❌ Very hard to read - too many levels:
score = 85
result = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"
print(result)    # B

# ✅ Much cleaner - use regular if/elif/else:
if score >= 90:
    result = "A"
elif score >= 80:
    result = "B"
elif score >= 70:
    result = "C"
elif score >= 60:
    result = "D"
else:
    result = "F"
print(result)    # B

# Rule of thumb for nested ternaries:
# ✅ One level of nesting (A if X else B if Y else C) - acceptable
# ❌ Two or more levels - use if/elif/else instead

# Acceptable nested ternary (3 clear outcomes):

temperature = 20
description = "hot" if temperature > 30 else "cold" if temperature < 10 else "comfortable"
print(description)    # comfortable

# This reads reasonably well:
# "hot if > 30, cold if < 10, otherwise comfortable"

# ------------------------------------------------------------
# PART 9: Ternary in list comprehensions (preview)
# ------------------------------------------------------------

# Ternary operators are VERY commonly used inside
# list comprehensions, which we'll cover in a later module.
# Here's a brief preview to show the potential.

numbers = [1, -2, 3, -4, 5, -6]

# For each number: keep it if positive, replace with 0 if negative
cleaned = [n if n > 0 else 0 for n in numbers]
print(cleaned)    # [1, 0, 3, 0, 5, 0]

# Labels for each number
labels = ["positive" if n > 0 else "negative" for n in numbers]
print(labels)    # ['positive', 'negative', 'positive', 'negative', 'positive', 'negative']

# Absolute values using ternary
absolutes = [n if n >= 0 else -n for n in numbers]
print(absolutes)    # [1, 2, 3, 4, 5, 6]

# Don't worry about the 'for n in numbers' part yet.
# Just notice how ternary fits naturally inside it.

# ------------------------------------------------------------
# PART 10: Practical patterns using ternary
# ------------------------------------------------------------

# Pattern 1: Clamping a value to a range

value = 150
clamped = 100 if value > 100 else (0 if value < 0 else value)
print(clamped)    # 100

value = -10
clamped = 100 if value > 100 else (0 if value < 0 else value)
print(clamped)    # 0

value = 50
clamped = 100 if value > 100 else (0 if value < 0 else value)
print(clamped)    # 50

# Pattern 2: Safe division

numerator = 10
denominator = 0
result = numerator / denominator if denominator != 0 else 0
print(result)    # 0  (avoids ZeroDivisionError)

denominator = 4
result = numerator / denominator if denominator != 0 else 0
print(result)    # 2.5

# Pattern 3: Boolean to human-readable string

flags = {
    "is_admin": True,
    "is_active": False,
    "has_verified_email": True,
}

for flag_name, flag_value in flags.items():
    readable = "Yes" if flag_value else "No"
    print(f"{flag_name}: {readable}")

# Output:
# is_admin: Yes
# is_active: No
# has_verified_email: Yes

# Pattern 4: Sign of a number

number = -42
sign = "+" if number > 0 else ("-" if number < 0 else "")
print(f"{sign}{abs(number)}")    # -42

number = 15
sign = "+" if number > 0 else ("-" if number < 0 else "")
print(f"{sign}{abs(number)}")    # +15

# Pattern 5: Percentage formatting

ratio = 0.756
percentage = f"{ratio * 100:.1f}%"
quality = "good" if ratio >= 0.7 else "poor"
print(f"Accuracy: {percentage} ({quality})")    # Accuracy: 75.6% (good)

# Pattern 6: Greeting based on hour

hour = 14    # 2 PM

greeting = (
    "Good morning" if hour < 12
    else "Good afternoon" if hour < 18
    else "Good evening"
)
print(greeting)    # Good afternoon

# Note: multi-line ternary using parentheses for readability.
# This is much cleaner than one very long line.
# Python allows you to break inside parentheses.

# ------------------------------------------------------------
# PART 11: Multi-line ternary for readability
# ------------------------------------------------------------

# When a ternary expression is too long for one line,
# you can split it across multiple lines using parentheses.
# Python ignores line breaks inside parentheses.

# ❌ Too long for one line:
# discount = original_price * 0.25 if customer_is_premium_member_with_active_subscription else original_price * 0.10 if customer_has_coupon else 0

# ✅ Split across lines with parentheses:

original_price = 200
customer_is_premium = True
customer_has_coupon = False

discount = (
    original_price * 0.25 if customer_is_premium
    else original_price * 0.10 if customer_has_coupon
    else 0
)
print(f"Discount: {discount}")    # Discount: 50.0

# Another example - classification:

bmi = 22.5

category = (
    "Underweight" if bmi < 18.5
    else "Normal" if bmi < 25
    else "Overweight" if bmi < 30
    else "Obese"
)
print(f"BMI {bmi}: {category}")    # BMI 22.5: Normal

# This is much more readable than cramming it on one line.
# When using multi-line ternary, each branch gets its own line.

# ------------------------------------------------------------
# PART 12: Ternary vs other Python idioms
# ------------------------------------------------------------

# Python has several ways to provide default values.
# Understanding each helps you choose the right one.

# METHOD 1: Ternary operator (explicit, handles any condition)
name = ""
display = name if name else "Anonymous"
print(display)    # Anonymous

# METHOD 2: 'or' operator (works for falsy defaults)
name = ""
display = name or "Anonymous"    # if name is falsy, use "Anonymous"
print(display)    # Anonymous

name = "Anna"
display = name or "Anonymous"
print(display)    # Anna

# METHOD 1 vs METHOD 2:
# 'or' is shorter but less explicit.
# Ternary is clearer about WHAT you're checking.

# ❌ 'or' can surprise you with numbers:
count = 0
display = count or "no items"    # 0 is falsy!
print(display)    # no items  ← but 0 IS a valid count!

# ✅ Ternary handles it correctly:
count = 0
display = count if count is not None else "no items"
print(display)    # 0  ← correct!

# METHOD 3: Walrus operator := (Python 3.8+) - advanced, skip for now

# Summary of when to use each:
# ternary:    when condition is complex or specific
# or:         quick default for falsy values (and you're sure 0/"" aren't valid)

# ------------------------------------------------------------
# PART 13: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Reversed order (forgetting the syntax order)

x = 10

# Wrong - confusing if and else positions:
# result = if x > 0 "positive" else "negative"   ← SyntaxError

# ✅ Correct order: value_if_true IF condition ELSE value_if_false
result = "positive" if x > 0 else "negative"
print(result)    # positive

# ❌ MISTAKE 2: Trying to use ternary for multiple statements

score = 85

# Wrong - ternary can only return ONE value, not run statements:
# print("Good") if score >= 60 else print("Failed")  ← works but bad style

# ✅ Use regular if/else for statements:
if score >= 60:
    print("Good")
    print("Keep it up!")
else:
    print("Failed")
    print("Study more!")

# ❌ MISTAKE 3: Missing else (ternary ALWAYS needs else)

# result = "positive" if x > 0   ← SyntaxError! Missing else
# (unlike regular if which can exist without else,
#  ternary MUST have both if AND else)

# ✅ Fix:
result = "positive" if x > 0 else "not positive"

# ❌ MISTAKE 4: Using ternary when elif is needed (too complex)

score = 75

# ❌ Hard to read nested ternary:
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

# ✅ Use if/elif/else:
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(grade)    # C

# ❌ MISTAKE 5: Confusing ternary with other languages

# In Java/C++: condition ? value_if_true : value_if_false
# In Python:   value_if_true if condition else value_if_false
# They're opposite order! Beginners from other languages often get confused.

# ❌ MISTAKE 6: Line too long - readability lost

is_premium = True
original_price = 199.99
# Too long - hard to read at a glance:
final_price = original_price * 0.75 if is_premium else original_price * 0.90 if True else original_price

# ✅ Use parentheses to split:
final_price = (
    original_price * 0.75 if is_premium
    else original_price * 0.90 if True
    else original_price
)
print(f"Final price: {final_price:.2f}")

# ❌ MISTAKE 7: Overusing ternary (making simple things complex)

x = 5
# Unnecessary ternary:
y = x if x else x    # ← pointless, always returns x!

# Unnecessary ternary for boolean:
is_big = True if x > 3 else False    # ← redundant!
# ✅ Just write:
is_big = x > 3    # the comparison already returns True/False

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Syntax: value_if_true if condition else value_if_false
# ✅ Returns a value - can be used anywhere a value is expected
# ✅ Must ALWAYS have both 'if' and 'else' parts
# ✅ Great for: simple assignments, f-strings, default values
# ✅ Avoid for: multiple statements, complex conditions, elif chains
# ✅ Can be nested (one level max for readability)
# ✅ Use parentheses to split long ternary across multiple lines
# ✅ 'or' can replace simple ternary for falsy defaults
# ✅ is_big = x > 3 is better than is_big = True if x > 3 else False

# Quick reference:
# ┌─────────────────────────────────────────────────────────┐
# │ x = "yes" if condition else "no"    ← assignment        │
# │ print("A" if x > 0 else "B")       ← in print           │
# │ f"{'pass' if s >= 60 else 'fail'}" ← in f-string        │
# │ val = input or "default"           ← falsy default      │
# │                                                         │
# │ ✅ Always needs 'else'                                  │
# │ ✅ One expression, one value returned                   │
# │ ✅ Order: TRUE_VALUE if CONDITION else FALSE_VALUE      │
# │ ✅ Use () to split long ternary across lines            │
# └─────────────────────────────────────────────────────────┘