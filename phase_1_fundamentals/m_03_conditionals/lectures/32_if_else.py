# ============================================================
# MODULE 03 | LECTURE 32 - if / else
# ============================================================
# What you will learn:
# - What the else clause is and why we need it
# - How if / else works together
# - The difference between two separate ifs and if / else
# - Nested logic with if / else
# - Common patterns and idioms
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: The problem with just 'if'
# ------------------------------------------------------------

# In the previous lecture, we learned that 'if' runs a block
# ONLY when the condition is True.
# When the condition is False - nothing happens.
#
# But very often we need TWO paths:
# "If this is True - do X. Otherwise - do Y."
#
# Real life examples:
# ┌─────────────────────────────────────────────────┐
# │ IF it is raining                                │
# │     take an umbrella                            │
# │ OTHERWISE                                       │
# │     wear sunglasses                             │
# │                                                 │
# │ IF the password is correct                      │
# │     let the user in                             │
# │ OTHERWISE                                       │
# │     show an error message                       │
# │                                                 │
# │ IF the number is even                           │
# │     print "even"                                │
# │ OTHERWISE                                       │
# │     print "odd"                                 │
# └─────────────────────────────────────────────────┘
#
# That's exactly what 'else' does.
# It handles the case when the if condition is False.

# ------------------------------------------------------------
# PART 2: Basic if / else syntax
# ------------------------------------------------------------

# Syntax:
#     if condition:
#         code runs when condition is True
#     else:
#         code runs when condition is False
#
# Rules:
# 1. 'else' MUST come after an 'if' block
# 2. 'else' has NO condition - it catches everything else
# 3. 'else' ends with a colon ':'
# 4. The else block must also be indented
# 5. Exactly ONE of the two blocks will always run

# Simplest possible example:

x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# Output: x is greater than 5

# Now with the other case:

x = 3

if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# Output: x is 5 or less

# Visual flow diagram:
#
#        condition
#        (True/False)
#             │
#          ┌──▼──┐
#    YES ──│True │── NO
#    │     └─────┘   │
#    ▼               ▼
# if block       else block
#    │               │
#    └───────┬────────┘
#            ▼
#      program continues

# Key point: EXACTLY ONE block always runs.
# There is no situation where both run.
# There is no situation where neither runs.

# ------------------------------------------------------------
# PART 3: if / else vs two separate ifs
# ------------------------------------------------------------

# This is a very important distinction that beginners often miss.

# TWO SEPARATE IFs - both conditions are checked independently:

score = 85

if score >= 60:
    print("You passed")        # checked: True → prints
if score < 60:
    print("You failed")        # checked: False → skipped

# Output: You passed

# IF / ELSE - only one condition is checked, one block runs:

if score >= 60:
    print("You passed")        # condition True → runs
else:
    print("You failed")        # skipped

# Output: You passed

# In this simple case, results look the same.
# But the difference becomes clear in more complex situations:

score = 50

# Two separate ifs:
if score >= 60:
    print("You passed")        # False → skipped
if score < 60:
    print("You failed")        # True → prints

# if / else:
if score >= 60:
    print("You passed")        # False → skipped
else:
    print("You failed")        # runs as fallback

# When should you use which?
#
# Use TWO SEPARATE IFs when:
# - The conditions are truly independent
# - Both could be True at the same time
# - You want both checked regardless of results
#
# Use IF / ELSE when:
# - The conditions are mutually exclusive
# - Exactly one case should run
# - The second case is "everything else"

# Example where separate ifs make more sense:

temperature = 35
is_sunny = True

if temperature > 30:
    print("It's hot")          # these are independent -
if is_sunny:
    print("It's sunny")        # both can be True at the same time

# Output:
# It's hot
# It's sunny

# Example where if/else makes more sense:

number = 7

if number % 2 == 0:
    print("Even")              # a number is EITHER even OR odd
else:
    print("Odd")               # never both, never neither

# Output: Odd

# ------------------------------------------------------------
# PART 4: Multiple lines in each block
# ------------------------------------------------------------

# Both the if block and else block can contain
# as many lines as you need.
# All lines must be indented at the same level.

age = 20

if age >= 18:
    print("You are an adult.")
    print("You can vote.")
    print("You can drive.")
    print("Welcome!")
else:
    print("You are a minor.")
    print("You cannot vote yet.")
    print("Come back in", 18 - age, "years.")

# Output:
# You are an adult.
# You can vote.
# You can drive.
# Welcome!

# All indented lines belong to their respective block.
# After the else block, the program continues normally.

print("Age check complete.")   # always runs, not part of if/else

# ------------------------------------------------------------
# PART 5: if / else with user input
# ------------------------------------------------------------

# One of the most practical uses - responding to user input.

# Example 1: Yes / No question

answer = input("Do you want to continue? (yes/no): ")

if answer.lower() == "yes":
    print("Great! Let's continue.")
else:
    print("Okay, stopping here.")

# Example 2: Number guessing

secret = 42
guess = int(input("Guess the number: "))

if guess == secret:
    print("🎉 Correct! You guessed it!")
else:
    print("❌ Wrong! Better luck next time.")

# Example 3: Password check

correct_password = "python123"
entered = input("Enter password: ")

if entered == correct_password:
    print("✅ Access granted. Welcome!")
else:
    print("❌ Wrong password. Access denied.")

# Example 4: Even or odd

number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is even")
else:
    print(f"{number} is odd")

# ------------------------------------------------------------
# PART 6: if / else with calculations
# ------------------------------------------------------------

# Often the two branches perform different calculations.

# Example 1: Absolute value (manually)

number = -15

if number >= 0:
    absolute = number
else:
    absolute = -number

print(f"Absolute value of {number} is {absolute}")
# Absolute value of -15 is 15

# Example 2: Discount calculator

price = 200
is_member = True

if is_member:
    final_price = price * 0.80    # 20% discount
else:
    final_price = price           # no discount

print(f"Original price: {price} PLN")
print(f"Final price: {final_price} PLN")
# Original price: 200 PLN
# Final price: 160.0 PLN

# Example 3: Speed converter

speed_kmh = 120
unit = input("Convert to mph or ms? ").lower()

if unit == "mph":
    converted = speed_kmh * 0.621371
    print(f"{speed_kmh} km/h = {converted:.2f} mph")
else:
    converted = speed_kmh / 3.6
    print(f"{speed_kmh} km/h = {converted:.2f} m/s")

# Example 4: Pass or fail

score = float(input("Enter exam score: "))
passing_score = 60.0

if score >= passing_score:
    grade_points = (score - 60) / 10
    print(f"PASSED ✅ - Score: {score}")
    print(f"Points above passing: {score - passing_score:.1f}")
else:
    deficit = passing_score - score
    print(f"FAILED ❌ - Score: {score}")
    print(f"Points needed to pass: {deficit:.1f}")

# ------------------------------------------------------------
# PART 7: Storing the result of if / else
# ------------------------------------------------------------

# A very common pattern - using if/else to SET a variable,
# then using that variable later.

# Pattern:
#     result = None
#     if condition:
#         result = value_A
#     else:
#         result = value_B
#     # now use result

# Example 1: Determine label

temperature = 28

if temperature >= 25:
    weather_label = "warm"
else:
    weather_label = "cool"

print(f"The weather is {weather_label} today.")
# The weather is warm today.

# Example 2: Determine status

age = int(input("Enter age: "))

if age >= 18:
    status = "adult"
else:
    status = "minor"

print(f"Status: {status}")
print(f"User is {status.upper()}")

# Example 3: Determine fee

is_student = True

if is_student:
    ticket_price = 15
else:
    ticket_price = 30

print(f"Ticket price: {ticket_price} PLN")
# Ticket price: 15 PLN

# Example 4: Calculate with condition

weight_kg = float(input("Enter weight in kg: "))
unit = input("Convert to lbs or stone? ").lower()

if unit == "lbs":
    result = weight_kg * 2.20462
    unit_label = "lbs"
else:
    result = weight_kg * 0.157473
    unit_label = "stone"

print(f"{weight_kg} kg = {result:.2f} {unit_label}")

# ------------------------------------------------------------
# PART 8: if / else with strings
# ------------------------------------------------------------

# Comparing strings works just like numbers.
# Remember: case-sensitive!

# Example 1: Greeting based on time of day

time_of_day = input("Enter time of day (morning/afternoon/evening): ")

if time_of_day.lower() == "morning":
    greeting = "Good morning! ☀"
else:
    greeting = "Hello! 👋"

print(greeting)

# Example 2: Language detector (basic)

text = input("Enter some text: ")

if "ą" in text or "ę" in text or "ó" in text:
    print("This looks like Polish text!")
else:
    print("This doesn't look like Polish.")

# Example 3: Username validator

username = input("Choose a username: ")

if " " in username:
    print("❌ Username cannot contain spaces.")
else:
    print(f"✅ Username '{username}' is accepted.")

# Example 4: DNA vs RNA detector

sequence = input("Enter nucleotide sequence: ").upper()

if "U" in sequence:
    print("This is an RNA sequence (contains Uracil)")
else:
    print("This might be a DNA sequence (no Uracil found)")

# ------------------------------------------------------------
# PART 9: Nested if / else (preview)
# ------------------------------------------------------------

# You can put an if/else INSIDE another if/else.
# This is called nesting.
# We'll cover this in depth in Lecture 04,
# but here's a basic preview.

# Simple nesting example:

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed - ID verified")
    else:
        print("Entry denied - no ID")
else:
    print("Entry denied - must be 18+")

# Output: Entry allowed - ID verified

# Another example:

number = int(input("Enter a number: "))

if number > 0:
    if number % 2 == 0:
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    print("Not positive")

# Tip: Don't nest too deeply - it gets hard to read!
# If you find yourself nesting 3+ levels, consider restructuring.

# ------------------------------------------------------------
# PART 10: Boolean assignment pattern
# ------------------------------------------------------------

# A common and clean Python pattern:
# setting a boolean based on a condition.

# Version 1 - verbose (works but not ideal):

number = 15
if number > 10:
    is_large = True
else:
    is_large = False

# Version 2 - direct assignment (much cleaner!):

is_large = number > 10    # the comparison itself returns True/False!

print(is_large)           # True

# More examples:

score = 85
passed = score >= 60          # True
is_perfect = score == 100     # False
in_range = 80 <= score <= 90  # True

print(passed)      # True
print(is_perfect)  # False
print(in_range)    # True

# You don't always need if/else just to store a boolean.
# If your if/else only sets True or False -
# just assign the comparison directly.

# ❌ Overly verbose:
x = 42
if x > 0:
    is_positive = True
else:
    is_positive = False

# ✅ Clean and Pythonic:
is_positive = x > 0

print(is_positive)    # True

# ------------------------------------------------------------
# PART 11: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: else without if

# else:                   ← SyntaxError! No matching if
#     print("something")

# ❌ MISTAKE 2: condition after else

# else x > 5:             ← SyntaxError! else has no condition
#     print("something")

# ✅ else never has a condition - that's the point!

# ❌ MISTAKE 3: forgetting colon after else

# if x > 5:
#     print("yes")
# else               ← SyntaxError! Missing colon
#     print("no")

# ✅ Fix:
x = 10
if x > 5:
    print("yes")
else:
    print("no")

# ❌ MISTAKE 4: wrong indentation in else block

# if x > 5:
#     print("yes")
# else:
# print("no")        ← IndentationError!

# ✅ Fix:
if x > 5:
    print("yes")
else:
    print("no")      # must be indented

# ❌ MISTAKE 5: unreachable else (logic error)

number = 10

if number > 5:
    print("greater than 5")
if number <= 5:               # separate if - not an else!
    print("5 or less")        # this is checked independently

# ✅ Better - use if/else when mutually exclusive:
if number > 5:
    print("greater than 5")
else:
    print("5 or less")

# ❌ MISTAKE 6: both blocks doing the same thing

value = 10
if value > 0:
    print("Value is: " + str(value))
else:
    print("Value is: " + str(value))   # pointless! same either way

# ✅ Fix: move shared code outside if/else
print("Value is:", value)              # just print it unconditionally

# ❌ MISTAKE 7: comparing strings without .lower()

answer = input("Continue? (Yes/No): ")

if answer == "yes":            # won't match "Yes", "YES", "YeS"...
    print("Continuing")

# ✅ Fix:
if answer.lower() == "yes":    # handles any capitalization
    print("Continuing")

# ❌ MISTAKE 8: using = instead of == in condition

x = 5
# if x = 10:       ← SyntaxError! Assignment inside condition
#     print("ten")

# ✅ Fix:
if x == 10:
    print("ten")
else:
    print("not ten")           # not ten

# ------------------------------------------------------------
# PART 12: Real-world use cases
# ------------------------------------------------------------

# Use case 1: Grade pass/fail system

score = float(input("Enter score: "))
if score >= 50:
    print(f"PASS ✅ ({score}/100)")
else:
    print(f"FAIL ❌ ({score}/100) - need {50 - score:.1f} more points")

# Use case 2: Unit converter

value = float(input("Enter value: "))
direction = input("Convert kg→lbs or lbs→kg? ").lower()

if "kg" in direction and direction.index("kg") < direction.index("lbs"):
    result = value * 2.20462
    print(f"{value} kg = {result:.3f} lbs")
else:
    result = value / 2.20462
    print(f"{value} lbs = {result:.3f} kg")

# Use case 3: ATM withdrawal

balance = 1500.00
withdrawal = float(input("Enter withdrawal amount: "))

if withdrawal <= balance:
    balance -= withdrawal
    print(f"✅ Withdrawal successful!")
    print(f"Dispensing: {withdrawal:.2f} PLN")
    print(f"Remaining balance: {balance:.2f} PLN")
else:
    print(f"❌ Insufficient funds!")
    print(f"Your balance: {balance:.2f} PLN")
    print(f"Requested: {withdrawal:.2f} PLN")

# Use case 4: DNA complement

base = input("Enter a DNA base (A/T/C/G): ").upper()

if base == "A":
    complement = "T"
else:
    complement = "A"    # simplified - full version needs elif (Lecture 03)

print(f"Complement of {base} is {complement}")

# Use case 5: Leap year checker

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year 📅")
else:
    print(f"{year} is not a leap year")

# ------------------------------------------------------------
# PART 13: The 'else' as a safety net
# ------------------------------------------------------------

# A very important use of else: catching unexpected input
# and providing a default behavior.

# Without else - silent failure:

command = input("Enter command (start/stop): ")
if command == "start":
    print("Starting...")
if command == "stop":
    print("Stopping...")
# If user types "hello" - nothing happens! No feedback.

# With else - always gives feedback:

command = input("Enter command (start/stop): ")
if command == "start":
    print("Starting...")
else:
    print(f"Unknown command: '{command}'")
    print("Valid commands: start, stop")

# This is crucial for user-facing programs.
# Always handle the unexpected case!

# Another example - type checking:

user_input = input("Enter a number: ")

if user_input.isdigit():
    number = int(user_input)
    print(f"You entered: {number}")
else:
    print(f"'{user_input}' is not a valid number!")

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ if / else gives you TWO paths
# ✅ Exactly ONE block always runs
# ✅ else has NO condition - catches everything else
# ✅ else must follow directly after the if block
# ✅ Both blocks must be properly indented (4 spaces)
# ✅ Don't forget colons after 'if condition:' and 'else:'
# ✅ if / else ≠ two separate ifs
# ✅ Use else as a safety net for unexpected input
# ✅ is_positive = x > 0  is cleaner than if/else for booleans
# ✅ Always use .lower() when comparing user-entered strings

# Quick reference:
# ┌──────────────────────────────────────────────────────┐
# │ if condition:                                        │
# │     runs when True                                   │
# │ else:                                                │
# │     runs when False                                  │
# │                                                      │
# │ ✅ One of the two ALWAYS runs                        │
# │ ✅ else has no condition                             │
# │ ✅ else cannot exist without if                      │
# │ ✅ Both blocks need proper indentation               │
# └──────────────────────────────────────────────────────┘

# Visual summary:
#
# if True:    → if block runs,   else block skipped
# if False:   → if block skipped, else block runs