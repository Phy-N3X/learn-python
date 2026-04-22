# ============================================================
# MODULE 03 | EXERCISES 32 - if / else
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Create a variable 'temperature' and set it to any value.
# Write an if/else statement:
# - If temperature > 30 → print "It's hot! Stay hydrated."
# - Otherwise → print "The temperature is comfortable."
#
# Test your code with two different values:
# once above 30, once below 30.
#
# Expected output (temperature = 35):
# It's hot! Stay hydrated.
#
# Expected output (temperature = 22):
# The temperature is comfortable.

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what each if/else block will print.
# Write your prediction as a comment BEFORE running.
# Then run and verify.
#
# a = 10
# b = 20
#
# if a > b:
#     print("A")          # prediction: ?
# else:
#     print("B")          # prediction: ?
#
# if a != b:
#     print("C")          # prediction: ?
# else:
#     print("D")          # prediction: ?
#
# if a == 10 and b == 10:
#     print("E")          # prediction: ?
# else:
#     print("F")          # prediction: ?
#
# if not a:
#     print("G")          # prediction: ?
# else:
#     print("H")          # prediction: ?
#
# x = ""
# if x:
#     print("I")          # prediction: ?
# else:
#     print("J")          # prediction: ?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL the errors in the code below.
# Write what each error is as a comment next to the line.
# Then fix all errors so the code runs correctly.
#
# score = 75
#
# if score >= 50
#     print("Passed")
# Else:
#     print("Failed")
#
# if score > 100:
#     print("Perfect")
# else score < 0:
#     print("Invalid")
#
# if score == 75:
#     print("Exactly 75")
# else:
# print("Not 75")

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Ask the user to enter a number.
# Use if/else to print whether the number is:
# - Positive (greater than 0) → "Positive number"
# - Not positive (0 or below) → "Zero or negative number"
#
# Then on a new line always print:
# "Number entered: X" (where X is the number)
#
# Example interaction 1:
# Enter a number: 7
# Positive number
# Number entered: 7
#
# Example interaction 2:
# Enter a number: -3
# Zero or negative number
# Number entered: -3

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Build a simple even/odd checker.
# Ask the user for an integer.
# Use if/else and the modulo operator (%).
# Print whether the number is even or odd.
# Also print what the remainder is when divided by 2.
#
# Example interaction 1:
# Enter an integer: 8
# 8 is EVEN (remainder: 0)
#
# Example interaction 2:
# Enter an integer: 13
# 13 is ODD (remainder: 1)

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a simple login system.
# Store the correct credentials as variables:
# correct_username = "admin"
# correct_password = "python123"
#
# Ask the user for username and password.
# Use a SINGLE if/else (with 'and') to check both at once.
# Print an appropriate success or failure message.
#
# Example interaction 1:
# Enter username: admin
# Enter password: python123
# ✅ Login successful! Welcome, admin.
# Access level: ADMINISTRATOR
#
# Example interaction 2:
# Enter username: user
# Enter password: wrongpass
# ❌ Login failed. Invalid credentials.
# Please try again.

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build an ATM balance checker.
# Set a starting balance: balance = 1000.00
# Ask the user how much they want to withdraw.
# Convert input to float.
#
# Use if/else:
# - If withdrawal <= balance:
#     subtract from balance
#     print success message with remaining balance
# - Otherwise:
#     print failure message
#     print how much they're short by
#
# Example interaction 1:
# Your balance: 1000.00 PLN
# Enter withdrawal amount: 250
# ✅ Withdrawal successful!
# Dispensed: 250.00 PLN
# Remaining balance: 750.00 PLN
#
# Example interaction 2:
# Your balance: 1000.00 PLN
# Enter withdrawal amount: 1500
# ❌ Insufficient funds!
# Requested: 1500.00 PLN
# Available: 1000.00 PLN
# Shortfall: 500.00 PLN

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a DNA / RNA detector.
# Ask the user to enter a nucleotide sequence.
# Convert it to uppercase.
#
# Use if/else:
# - If "U" is in the sequence → it's RNA
# - Otherwise → it's DNA (or unknown)
#
# Also check if the sequence is empty and handle that case.
#
# Print the sequence length either way.
#
# Example interaction 1:
# Enter sequence: AUGCUAUG
# Type: RNA 🧬
# Contains Uracil (U): Yes
# Sequence length: 8
#
# Example interaction 2:
# Enter sequence: ATCGATCG
# Type: DNA 🔬
# Contains Uracil (U): No
# Sequence length: 8
#
# Example interaction 3:
# Enter sequence:
# ❌ No sequence entered!

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this code step by step.
# Before EACH print statement, write your prediction.
# Then run and verify.
#
# x = 0
# y = 10
# name = "Python"
#
# if x:
#     # prediction: ?
#     print("x is truthy")
# else:
#     # prediction: ?
#     print("x is falsy")
#
# if y > 5 and name == "Python":
#     # prediction: ?
#     print("Both conditions met")
# else:
#     # prediction: ?
#     print("At least one condition failed")
#
# if not name:
#     # prediction: ?
#     print("Name is empty")
# else:
#     # prediction: ?
#     print(f"Name is: {name}")
#
# result = y > x
# if result:
#     # prediction: ?
#     print("y is greater than x")
# else:
#     # prediction: ?
#     print("y is not greater than x")
#
# Answer as comments:
# What is the value of 'result' stored as?
# Could you write the last if/else in one line without if/else?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a ticket price calculator.
# The cinema has the following pricing:
# - Age < 5:   FREE
# - Age 5-12:  15 PLN (child)
# - Age 13-17: 20 PLN (teen)  ← handle with nested if in else
# - Age 18-64: 35 PLN (adult)
# - Age 65+:   18 PLN (senior)
#
# For now, use only if/else (not elif).
# Handle just TWO cases:
# - Under 18 → "Reduced ticket: 20 PLN"
# - 18 or older → determine if adult or senior
#   (use nested if/else inside the else block)
#
# Ask user for age.
# Print ticket category and price.
#
# Example interaction 1:
# Enter your age: 15
# Category: Reduced
# Price: 20 PLN
#
# Example interaction 2:
# Enter your age: 30
# Category: Adult
# Price: 35 PLN
#
# Example interaction 3:
# Enter your age: 70
# Category: Senior
# Price: 18 PLN

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a body temperature analyzer.
# Normal human body temperature: 36.1°C to 37.2°C
#
# Ask the user for their temperature in Celsius.
# Use if/else with compound conditions:
# - If temperature is in normal range → "Normal temperature ✅"
# - Otherwise → determine if it's low or high using nested if/else
#   → below normal: "Hypothermia risk ❄ - seek medical advice"
#   → above normal: "Fever detected 🌡 - seek medical advice"
#
# Also print:
# - The exact temperature entered
# - How far it is from the normal range (if abnormal)
#
# Example interaction 1:
# Enter body temperature (°C): 36.6
# Temperature: 36.6°C
# Status: Normal temperature ✅
#
# Example interaction 2:
# Enter body temperature (°C): 38.5
# Temperature: 38.5°C
# Status: Fever detected 🌡 - seek medical advice
# Above normal by: 1.3°C

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a number comparison tool.
# Ask the user for TWO numbers.
# Use if/else to compare them in multiple ways.
#
# Print ALL of the following using if/else statements:
# 1. Which is larger (or if they're equal)
# 2. Their sum and which range it falls in:
#    sum < 0 → "Negative sum"
#    sum == 0 → "Zero sum"
#    sum > 0 → "Positive sum"
# 3. The larger number divided by the smaller
#    (only if smaller != 0, otherwise print "Cannot divide by zero")
# 4. Whether both numbers have the same sign
#    (both positive, both negative, or mixed)
#
# Example interaction:
# Enter first number: 8
# Enter second number: -3
#
# Comparison: 8 is greater than -3
# Sum: 5 → Positive sum
# Division: 8 / -3 = -2.67
# Signs: Mixed (one positive, one negative)

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a protein molecular weight estimator.
# (simplified - average amino acid weight ≈ 110 Da)
#
# Ask the user for:
# 1. A protein sequence (letters only)
# 2. Whether to display result in Da or kDa
#
# Validate the input:
# - If sequence contains numbers → "Invalid: sequence contains numbers"
# - If sequence is empty → "Invalid: empty sequence"
# - Otherwise → calculate and display
#
# Calculation:
# weight_Da = len(sequence) * 110
# weight_kDa = weight_Da / 1000
#
# Classification based on weight:
# < 10 kDa    → "Small peptide"
# 10-100 kDa  → "Average protein"
# > 100 kDa   → "Large protein"
#
# Example interaction:
# Enter protein sequence: MKTAYIAKQRQISFVK
# Display in Da or kDa? kDa
#
# Sequence: MKTAYIAKQRQISFVK
# Length: 16 amino acids
# Estimated weight: 1.76 kDa
# Classification: Small peptide

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a smart loan eligibility checker.
#
# Ask the user for:
# - Monthly income (float)
# - Monthly expenses (float)
# - Loan amount requested (float)
# - Employment status: employed / self-employed / unemployed
#
# Rules:
# 1. If unemployed → immediately denied, regardless of anything else
# 2. Calculate disposable income: income - expenses
#    If disposable income <= 0 → denied (can't afford repayments)
# 3. Calculate max loan = disposable_income * 36
#    (36 months repayment period)
#    If requested loan > max loan → denied, show max they can get
# 4. If self-employed → approved but with 15% higher interest rate
#    If employed → approved at standard rate
#
# Interest rates:
# Standard: 5.5%
# Self-employed: 5.5% * 1.15 = 6.325%
#
# Monthly repayment = loan * (rate/12) / (1-(1+rate/12)^-36)
# (use this formula or simplify to: loan / 36 for basic version)
#
# Print a full decision report.
#
# Example interaction:
# Monthly income: 5000
# Monthly expenses: 2000
# Loan amount: 50000
# Employment status: employed
#
# ===== LOAN DECISION REPORT =====
# Disposable income: 3000.00 PLN/month
# Maximum eligible loan: 108000.00 PLN
# Requested loan: 50000.00 PLN
# Status: ✅ APPROVED
# Interest rate: 5.50%
# Estimated monthly repayment: 1388.89 PLN

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a scientific unit converter with validation.
#
# Ask the user:
# 1. What they want to convert:
#    "temp" → temperature
#    "mass" → mass
#    "dist" → distance
#    anything else → "Unknown conversion type"
#
# 2. Based on their choice, ask for value and direction.
#
# Temperature conversions:
# C→F: (C * 9/5) + 32
# F→C: (F - 32) * 5/9
# C→K: C + 273.15
# K→C: K - 273.15
# Validate: Kelvin cannot be below 0, Celsius cannot be below -273.15
#
# Mass conversions:
# kg→g:  * 1000
# g→kg:  / 1000
# kg→lb: * 2.20462
# lb→kg: / 2.20462
# Validate: mass cannot be negative
#
# Distance conversions:
# m→km:  / 1000
# km→m:  * 1000
# m→mi:  * 0.000621371
# mi→m:  / 0.000621371
# Validate: distance cannot be negative
#
# For each conversion:
# - Validate the input value FIRST using if/else
# - If invalid → print specific error and stop
# - If valid → convert and print result with 4 decimal places
# - Also print if result is above/below a meaningful threshold:
#   temp: above/below human body temperature (37°C equivalent)
#   mass: above/below 1kg equivalent
#   dist: above/below 1km equivalent
#
# Example interaction:
# What to convert? (temp/mass/dist): temp
# Enter value: -300
# Enter unit (C/F/K): C
# ❌ Invalid: -300°C is below absolute zero (-273.15°C)
#
# What to convert? (temp/mass/dist): mass
# Enter value: 2500
# Enter unit (kg/g/lb): g
# Convert to (kg/lb): kg
# ✅ 2500.0000 g = 2.5000 kg
# Above 1kg threshold ✅
# ============================================================