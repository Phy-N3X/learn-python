# ============================================================
# MODULE 03 | EXERCISES 31 - if statement
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Create a variable called 'temperature' and set it to 35.
# Write an if statement that prints "It's hot outside!"
# if the temperature is greater than 30.
#
# Then change temperature to 20 and run again.
# Observe what happens.
#
# Expected output (temperature = 35):
# It's hot outside!
#
# Expected output (temperature = 20):
# (nothing printed)

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what each block will print BEFORE running the code.
# Write your prediction as a comment.
# Then run and verify.
#
# x = 10
#
# if x > 5:
#     print("A")        # prediction: ?
#
# if x == 10:
#     print("B")        # prediction: ?
#
# if x != 10:
#     print("C")        # prediction: ?
#
# if x >= 10:
#     print("D")        # prediction: ?
#
# if x <= 9:
#     print("E")        # prediction: ?
#
# if x:
#     print("F")        # prediction: ?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL the errors in the code below.
# Write what each error is as a comment next to the line.
# Then fix all errors so the code runs correctly.
#
# age = 20
#
# if age = 18:
#     print("Adult")
#
# if age >= 18
#     print("Can vote")
#
# if age > 17:
# print("Not a minor")
#
# If age < 100:
#     print("Not a centenarian")

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Ask the user to enter their age (use input() and int()).
# Write an if statement that prints "You can vote!"
# if the age is 18 or older.
#
# Example interaction 1:
# Enter your age: 20
# You can vote!
#
# Example interaction 2:
# Enter your age: 15
# (nothing printed)

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Create these variables:
# is_raining = True
# has_umbrella = False
# temperature = 5
#
# Write THREE separate if statements:
# 1. If is_raining is True → print "Take an umbrella!"
# 2. If has_umbrella is False → print "You don't have an umbrella!"
# 3. If temperature is below 10 → print "Wear a jacket!"
#
# Expected output:
# Take an umbrella!
# You don't have an umbrella!
# Wear a jacket!

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Ask the user to enter a number.
# Write FOUR separate if statements to check:
# 1. Is the number positive? (> 0)
# 2. Is the number negative? (< 0)
# 3. Is the number equal to zero?
# 4. Is the number even? (use modulo %)
#
# Each condition that is True should print a message.
#
# Example interaction 1 (user enters 4):
# Enter a number: 4
# The number is positive
# The number is even
#
# Example interaction 2 (user enters -3):
# Enter a number: -3
# The number is negative
#
# Example interaction 3 (user enters 0):
# Enter a number: 0
# The number is zero
# The number is even

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use chained comparisons to check if values are in range.
#
# Create these variables:
# score = 85
# ph = 7.4
# age = 25
# temperature = 22
#
# Write an if statement for each using chained comparisons:
# 1. score is between 80 and 89 (inclusive)
#    → print "Grade: B"
# 2. ph is between 7.35 and 7.45 (inclusive)
#    → print "Normal blood pH"
# 3. age is between 18 and 65 (inclusive)
#    → print "Working age"
# 4. temperature is between 18 and 26 (inclusive)
#    → print "Comfortable temperature"
#
# Expected output:
# Grade: B
# Normal blood pH
# Working age
# Comfortable temperature

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a simple login checker.
#
# Store the correct credentials:
# correct_username = "admin"
# correct_password = "python123"
#
# Ask the user for username and password.
# Use 'and' to check BOTH at once.
# If both match → print "Login successful! Welcome, admin."
#
# Example interaction 1:
# Enter username: admin
# Enter password: python123
# Login successful! Welcome, admin.
#
# Example interaction 2:
# Enter username: user
# Enter password: python123
# (nothing - we'll add the error message in the next lecture!)
#
# Note: we only have 'if' today - no 'else' yet.
# The "wrong credentials" case will be handled in Lecture 02.

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this code step by step.
# Before each print, write your prediction as a comment.
# Then run and verify.
#
# a = 15
# b = 3
# name = "Python"
# items = ""
#
# if a > b and a > 10:
#     # prediction: ?
#     print("A is large and greater than b")
#
# if a % b == 0:
#     # prediction: ?
#     print("a is divisible by b")
#
# if name.startswith("Py") and len(name) > 4:
#     # prediction: ?
#     print("Name starts with Py and is long enough")
#
# if not items:
#     # prediction: ?
#     print("Items list is empty")
#
# if a > 10 or b > 10:
#     # prediction: ?
#     print("At least one is greater than 10")
#
# Final question (answer as comments):
# Why does 'if not items' evaluate to True?
# What would happen if items = "something"?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a basic BMI (Body Mass Index) checker.
#
# Formula: bmi = weight / (height ** 2)
# (weight in kg, height in meters)
#
# Ask the user for their weight and height.
# Calculate BMI.
# Use separate if statements to check each category:
# - BMI < 18.5  → print "Underweight"
# - BMI >= 18.5 and BMI < 25.0 → print "Normal weight"
# - BMI >= 25.0 and BMI < 30.0 → print "Overweight"
# - BMI >= 30.0  → print "Obese"
#
# Also print the calculated BMI rounded to 2 decimal places.
#
# Example interaction:
# Enter weight (kg): 70
# Enter height (m): 1.75
# Your BMI: 22.86
# Normal weight

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a DNA base pair validator.
#
# In DNA, bases pair up:
# A pairs with T
# T pairs with A
# C pairs with G
# G pairs with C
#
# Ask the user to enter a DNA base (A, T, C, or G).
# Convert it to uppercase.
# Use if statements to print the correct pair.
# Also check if the input is valid (only A, T, C, G allowed).
#
# Example interaction 1:
# Enter a DNA base: a
# Base: A
# Complementary base: T
#
# Example interaction 2:
# Enter a DNA base: G
# Base: G
# Complementary base: C
#
# Example interaction 3:
# Enter a DNA base: X
# Base: X
# Valid bases: A, T, C, G only.
# Invalid base entered.
#
# Tip: write one if per base pair, and one if for invalid input.
# Use 'in' to check validity: if base not in "ATCG"

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a number properties analyzer.
# Ask the user for a number and analyze ALL its properties.
# Each property gets its own if statement.
#
# Properties to check:
# 1. Is it positive, negative, or zero?
# 2. Is it even or odd?
# 3. Is it divisible by 3?
# 4. Is it divisible by 5?
# 5. Is it divisible by both 3 AND 5?
# 6. Is it a perfect square? (hint: int(x**0.5)**2 == x)
# 7. Is it between 1 and 100 (inclusive)?
#
# Example interaction (user enters 15):
# Enter a number: 15
# → Positive
# → Odd
# → Divisible by 3
# → Divisible by 5
# → Divisible by both 3 and 5 (divisible by 15!)
# → Not a perfect square
# → Between 1 and 100
#
# Example interaction (user enters 25):
# Enter a number: 25
# → Positive
# → Odd
# → Not divisible by 3
# → Divisible by 5
# → Not divisible by both 3 and 5
# → Perfect square! (5 × 5 = 25)
# → Between 1 and 100

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a protein sequence analyzer using only if statements.
#
# Rules:
# - A valid protein sequence contains only these amino acid
#   single-letter codes: ACDEFGHIKLMNPQRSTVWY
# - Sequences shorter than 10 amino acids are considered short
# - Sequences of 10-100 amino acids are considered medium
# - Sequences longer than 100 amino acids are considered long
# - The sequence must be uppercase
#
# Ask the user for a protein sequence.
# Perform all checks and print results.
#
# Example interaction:
# Enter protein sequence: MKTAYIAKQRQISFVKSHFSRQ
#
# Sequence length: 22
# Length category: medium
# All characters valid: True (or False + which char is invalid)
# Starts with Methionine (M): True
# Contains Cysteine (C): False
#
# Tip: for validity check, loop through sequence
# and use 'not in' against the valid amino acids string.

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a temperature conversion and classification system.
#
# Ask the user:
# 1. The temperature value (float)
# 2. The unit: C (Celsius), F (Fahrenheit), or K (Kelvin)
#
# Convert to ALL three units and print them.
# Then classify based on Celsius value:
#
# Formulas:
# C to F: (C * 9/5) + 32
# C to K: C + 273.15
# F to C: (F - 32) * 5/9
# K to C: K - 273.15
#
# Classification (based on Celsius):
# Below -273.15  → Impossible (below absolute zero)
# -273.15 to -89 → Extremely cold (record: -89°C Antarctica)
# -89 to 0       → Freezing
# 0 to 20        → Cold
# 20 to 30       → Comfortable
# 30 to 40       → Hot
# Above 40       → Dangerously hot
#
# Example interaction:
# Enter temperature: 100
# Enter unit (C/F/K): C
# --- Conversions ---
# Celsius:    100.00 °C
# Fahrenheit: 212.00 °F
# Kelvin:     373.15 K
# --- Classification ---
# Dangerously hot

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a smart water intake calculator and advisor.
#
# Collect the following from the user:
# - Weight in kg (float)
# - Activity level: 1 = sedentary, 2 = moderate, 3 = active
# - Is it summer? (yes/no)
# - Do they drink coffee? (yes/no)
# - Are they sick/have fever? (yes/no)
#
# Calculate recommended daily water intake:
# Base: weight * 0.033  (liters)
# If activity level is 2: add 0.5 liters
# If activity level is 3: add 1.0 liters
# If summer: add 0.5 liters
# If drinks coffee: add 0.3 liters per cup
#   (ask how many cups if they said yes)
# If sick/fever: add 1.0 liters
#
# Print:
# - The calculated water intake in liters (rounded to 2 decimals)
# - Whether it's above, below, or equal to the average (2.0L)
# - A personalized tip for each "yes" answer
#
# Example interaction:
# Enter your weight (kg): 70
# Activity level (1/2/3): 2
# Is it summer? (yes/no): yes
# Do you drink coffee? (yes/no): yes
# How many cups per day? 2
# Are you sick or have fever? (yes/no): no
#
# --- Water Intake Report ---
# Base intake:        2.31 L  (70 × 0.033)
# Activity bonus:    +0.50 L
# Summer bonus:      +0.50 L
# Coffee bonus:      +0.60 L  (2 cups)
# Total recommended:  3.91 L
#
# Above average daily intake (avg: 2.0L)
#
# Tips:
# → You're active - great! Stay hydrated during exercise.
# → Hot weather increases water loss through sweat.
# → Coffee is a mild diuretic - extra water helps!
# ============================================================