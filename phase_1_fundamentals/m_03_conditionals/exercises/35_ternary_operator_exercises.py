# ============================================================
# MODULE 03 | EXERCISES 35 - One-line if (Ternary Operator)
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Convert each regular if/else into a ternary expression.
# The logic must remain exactly the same.
#
# BLOCK A:
# if temperature > 30:
#     weather = "hot"
# else:
#     weather = "not hot"
#
# BLOCK B:
# if age >= 18:
#     status = "adult"
# else:
#     status = "minor"
#
# BLOCK C:
# if is_raining:
#     take = "umbrella"
# else:
#     take = "sunglasses"
#
# BLOCK D:
# if score >= 60:
#     result = "PASS"
# else:
#     result = "FAIL"
#
# Print all four results after conversion.
# Use these values: temperature=25, age=20,
#                   is_raining=False, score=75

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what each ternary expression evaluates to.
# Write your prediction as a comment.
# Then run and verify.
#
# a = 10
# b = 20
#
# r1 = "yes" if a > b else "no"
# # prediction: r1 = ?
# print(r1)
#
# r2 = a if a > b else b
# # prediction: r2 = ?
# print(r2)
#
# r3 = "equal" if a == b else "not equal"
# # prediction: r3 = ?
# print(r3)
#
# r4 = "truthy" if a else "falsy"
# # prediction: r4 = ?
# print(r4)
#
# r5 = a + b if a < b else a - b
# # prediction: r5 = ?
# print(r5)
#
# name = ""
# r6 = name if name else "Anonymous"
# # prediction: r6 = ?
# print(r6)
#
# Final question (answer as comment):
# Why does r4 evaluate to "truthy"?
# What value of 'a' would make r4 = "falsy"?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL errors in the ternary expressions below.
# Write what each error is as a comment.
# Then fix all errors so the code runs correctly.
#
# x = 10
#
# r1 = if x > 5 "big" else "small"
#
# r2 = "positive" if x > 0
#
# r3 = "even" if x % 2 = 0 else "odd"
#
# r4 = "large" if x > 100 elif x > 50 "medium" else "small"
#
# r5 = else "negative" if x < 0 "positive"

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use ternary expressions inside f-strings.
# Create these variables:
# name = "Anna"
# score = 88
# items = 1
# is_vip = True
#
# Build these f-strings using ternary INSIDE them:
#
# 1. "Hello, Anna!" or "Hello, stranger!" (based on name being set)
# 2. "Score: 88 - PASS" or "Score: X - FAIL" (based on score >= 60)
# 3. "1 item in cart" or "N items in cart" (singular/plural)
# 4. "Access level: VIP 🌟" or "Access level: Standard"
#
# Expected output:
# Hello, Anna!
# Score: 88 - PASS
# 1 item in cart
# Access level: VIP 🌟

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Ask the user to enter their name.
# Use a ternary to set display_name:
# - If they entered something → use their name
# - If they pressed Enter (empty) → use "Guest"
#
# Then ask for their age.
# Use a ternary to set age_group:
# - age >= 65 → "Senior"
# - age >= 18 → "Adult"
# - (hint: use a simple nested ternary or just two conditions)
#
# Print a personalized greeting:
# "Welcome, [name]! You are logged in as [age_group]."
#
# Example interaction 1:
# Enter name: Anna
# Enter age: 30
# Welcome, Anna! You are logged in as Adult.
#
# Example interaction 2:
# Enter name:
# Enter age: 70
# Welcome, Guest! You are logged in as Senior.

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Rewrite this nested if/else as a multi-line ternary
# using parentheses for readability.
#
# temperature = float(input("Enter temperature: "))
#
# if temperature > 35:
#     description = "extremely hot 🔥"
# elif temperature > 25:
#     description = "warm ☀"
# elif temperature > 15:
#     description = "comfortable 😊"
# elif temperature > 5:
#     description = "cool 🌤"
# else:
#     description = "cold ❄"
#
# Use this format for the ternary:
# description = (
#     "..." if temperature > 35
#     else "..." if temperature > 25
#     ...
# )
#
# Then print: "Temperature: X°C - [description]"
# Test with values: 40, 28, 18, 8, -5

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a discount calculator using only ternary expressions.
# No regular if/else allowed in this exercise!
#
# Ask user for:
# - Original price (float)
# - Is customer a member? (yes/no)
# - Quantity bought (int)
#
# Calculate discount using ternary:
# - Member discount: 15% if member, else 0%
# - Bulk discount: 10% if quantity >= 10, else 5% if quantity >= 5, else 0%
# - Total discount = member_discount + bulk_discount
#   (but cap at 25% max using ternary)
#
# All three calculations must use ternary expressions.
# Print original price, discount %, and final price.
#
# Example interaction:
# Price: 100
# Member: yes
# Quantity: 12
# Original: 100.00 PLN
# Discount: 25% (capped)
# Final price: 75.00 PLN

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a DNA base complement finder using ternary.
#
# The complement rules:
# A → T
# T → A
# C → G
# G → C
#
# Ask user for a single DNA base.
# Convert to uppercase.
# Use a NESTED ternary to find the complement:
# complement = "T" if base == "A" else "A" if base == "T" else ...
#
# Also use ternary to create a validity message:
# valid_msg = "✅ Valid base" if base in "ATCG" else "❌ Invalid base"
#
# Print both the complement (if valid) and validity message.
#
# Example interaction 1:
# Enter DNA base: g
# Base: G
# Complement: C
# ✅ Valid base
#
# Example interaction 2:
# Enter DNA base: X
# Base: X
# Complement: Unknown
# ❌ Invalid base

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through these ternary expressions step by step.
# Predict the value of each result BEFORE running.
# Write your prediction as a comment.
#
# x = 15
# y = 0
# name = "Python"
# items = []
#
# r1 = x if x > 10 else 10
# # prediction: r1 = ?
# print(r1)
#
# r2 = "zero" if not y else "nonzero"
# # prediction: r2 = ?
# print(r2)
#
# r3 = len(name) if name else 0
# # prediction: r3 = ?
# print(r3)
#
# r4 = "has items" if items else "empty"
# # prediction: r4 = ?
# print(r4)
#
# r5 = x * 2 if x % 3 == 0 else x * 3 if x % 5 == 0 else x
# # prediction: r5 = ?
# print(r5)
#
# r6 = (x + y) if (x > 0 and y > 0) else (x - y) if x > y else 0
# # prediction: r6 = ?
# print(r6)
#
# Answer as comments:
# In r5, which condition is checked first?
# In r6, why does it not evaluate to x + y?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a scientific measurement formatter using ternary.
#
# Scientists often need to display values with appropriate units
# and precision depending on the scale of the value.
#
# Ask user for a measurement value (float) and type:
# "length", "mass", or "time"
#
# For LENGTH:
# value >= 1000    → display in km (divide by 1000)
# value >= 1       → display in m
# value >= 0.01    → display in cm (multiply by 100)
# value < 0.01     → display in mm (multiply by 1000)
#
# For MASS:
# value >= 1000    → display in kg (divide by 1000)
# value >= 1       → display in g
# value >= 0.001   → display in mg (multiply by 1000)
# value < 0.001    → display in μg (multiply by 1000000)
#
# For TIME:
# value >= 3600    → display in hours (divide by 3600)
# value >= 60      → display in minutes (divide by 60)
# value >= 1       → display in seconds
# value < 1        → display in milliseconds (multiply by 1000)
#
# Use multi-line ternary (with parentheses) for each conversion.
# Format output to 4 decimal places.
#
# Example interaction:
# Value: 0.0045
# Type: length
# 0.0045 m = 0.4500 cm

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a report card generator using ternary expressions.
# Use ONLY ternary (no regular if/else).
#
# Ask user for:
# - Student name
# - Math score (0-100)
# - Science score (0-100)
# - English score (0-100)
#
# For each score, calculate using ternary:
# 1. Letter grade: A(>=90), B(>=80), C(>=70), D(>=60), F(<60)
# 2. Pass/fail indicator: ✅ or ❌ (pass if >= 60)
# 3. One-word assessment: "Excellent"/"Good"/"Average"/"Poor"/"Failed"
#
# Calculate average and use ternary for:
# 4. Overall grade letter (based on average)
# 5. Honor roll status: "Honor Roll 🏆" if average >= 90 else ""
# 6. Scholarship eligible: "Yes" if average >= 85 else "No"
#
# Print a formatted report card.
#
# Example output:
# ╔══════════════════════════════════╗
# ║     REPORT CARD - Anna           ║
# ╠══════════════════════════════════╣
# ║ Math:    88  B  ✅  Good         ║
# ║ Science: 92  A  ✅  Excellent    ║
# ║ English: 74  C  ✅  Average      ║
# ╠══════════════════════════════════╣
# ║ Average: 84.7  B                 ║
# ║ Scholarship: Yes                 ║
# ╚══════════════════════════════════╝

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a protein sequence formatter using ternary.
#
# Ask user for a protein sequence (single-letter amino acid codes).
#
# Classify amino acids by properties using ternary:
# Hydrophobic (nonpolar): A, V, I, L, M, F, W, P
# Hydrophilic (polar):    S, T, C, Y, N, Q
# Charged positive:       K, R, H
# Charged negative:       D, E
# Special:                G (glycine - smallest)
# Unknown:                anything else
#
# For each amino acid in the sequence:
# Use a nested ternary to classify it.
#
# Then calculate using ternary:
# - Charge balance: "positive" if more + than -, "negative" if more - than +, "neutral"
# - Length class: "short" < 50, "medium" < 200, "long" >= 200 aa
# - Has special glycine: "Yes" if G in sequence else "No"
#
# Print:
# - Original sequence
# - Classification of each amino acid (as a string like "H P H C...")
#   H=hydrophobic, P=hydrophilic, +=positive, -=negative, G=glycine, ?=unknown
# - Charge balance
# - Length class
#
# Example interaction:
# Enter protein: MKTDGE
# Sequence: MKTDGE
# Profile:  H + P - - +  (wait - check actual rules)
# Charge: neutral (1 positive K, 1 negative D... etc)
# Length: short

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a smart number formatter using ternary.
# Numbers should be formatted differently based on their magnitude
# and type (int vs float).
#
# Ask user for a number.
# Try to convert to int first, then float if that fails.
# Use ternary for ALL decisions - no regular if/else.
#
# Formatting rules:
# Integers:
# - Negative → show with minus sign and absolute value
# - 0 → "zero"
# - 1-9 → word (one, two... nine) using nested ternary or dict
# - 10-999 → plain number
# - 1000-999999 → format as "Xk" (e.g. 5000 → "5k")
# - >= 1000000 → format as "XM" (e.g. 2000000 → "2M")
#
# Floats:
# - Show 2 decimal places if < 1000
# - Show 0 decimal places (rounded) if >= 1000
# - Show scientific notation if < 0.001 or >= 1000000
#   (use Python's f"{value:.2e}" format)
#
# Also use ternary to determine:
# - Sign label: "positive", "negative", or "zero"
# - Type label: "integer" or "decimal"
# - Even/odd (integers only): "even", "odd", or "N/A" (for floats)
#
# Print the formatted number and all labels.
#
# Example interaction 1:
# Enter number: 5000
# Original: 5000
# Formatted: 5k
# Type: integer | Sign: positive | Even/Odd: even
#
# Example interaction 2:
# Enter number: 3.14159
# Original: 3.14159
# Formatted: 3.14
# Type: decimal | Sign: positive | Even/Odd: N/A

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a complete lab result interpreter using ternary.
# A patient's blood test results need to be interpreted.
#
# Ask user for these lab values:
# - Hemoglobin (g/dL): normal range 12.0-17.5
# - White blood cells (10³/μL): normal range 4.5-11.0
# - Platelets (10³/μL): normal range 150-400
# - Blood glucose (mg/dL): normal range 70-100 (fasting)
# - Cholesterol (mg/dL): desirable < 200, borderline 200-239, high >= 240
# - Patient sex for hemoglobin: M or F
#   (male normal: 13.5-17.5, female normal: 12.0-15.5)
#
# For EACH value, use ternary to determine:
# 1. Status: "Low" / "Normal" / "High" (or "Desirable"/"Borderline"/"High" for cholesterol)
# 2. Indicator: "⬇" / "✅" / "⬆"
# 3. Clinical significance:
#    - Low hemoglobin → "Possible anemia"
#    - High WBC → "Possible infection/inflammation"
#    - Low WBC → "Possible immunosuppression"
#    - Low platelets → "Bleeding risk"
#    - High glucose → "Possible diabetes/prediabetes"
#    - Low glucose → "Hypoglycemia"
#    - High cholesterol → "Cardiovascular risk"
#    - Normal → "Within reference range"
#
# Print a formatted lab report:
# ┌─────────────────────────────────────────────────┐
# │           LABORATORY RESULTS REPORT             │
# ├──────────────────┬────────┬────────┬────────────┤
# │ Test             │ Value  │ Status │ Note       │
# ├──────────────────┼────────┼────────┼────────────┤
# │ Hemoglobin       │ 11.2   │ ⬇ Low  │ Possible.. │
# │ ...              │ ...    │ ...    │ ...        │
# └──────────────────┴────────┴────────┴────────────┘
# Overall: X values normal, Y abnormal
# Recommendation: (ternary: "Consult doctor" if any abnormal else "All clear")

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a text analysis tool that uses ONLY ternary expressions
# for ALL decisions (no regular if/else anywhere in the solution).
#
# Ask user for a paragraph of text.
#
# Analyze the text and calculate/display ALL of the following
# using ternary expressions:
#
# 1. LENGTH ANALYSIS:
# - Character count (with/without spaces)
# - Word count (split by spaces)
# - Sentence count (count . ! ?)
# - Length category: use ternary
#   < 50 chars → "very short", < 200 → "short",
#   < 500 → "medium", < 1000 → "long", else → "very long"
#
# 2. CONTENT ANALYSIS (all using ternary):
# - Has numbers: "Yes" if any digit in text else "No"
# - Has uppercase: "Yes" if any upper in text else "No"
# - Has punctuation: "Yes" if any of ".!?," in text else "No"
# - Language guess: "Likely Polish" if any of "ąęóśźżćńł" in text
#                   else "Likely English" if all chars are ASCII
#                   else "Unknown/Mixed"
#
# 3. READABILITY SCORE (simplified Flesch):
# avg_word_length = total_chars_no_spaces / word_count
# score = 100 - (avg_word_length * 10)  (simplified)
# Use ternary to classify:
# score >= 80 → "Very Easy"
# score >= 60 → "Easy"
# score >= 40 → "Moderate"
# score >= 20 → "Difficult"
# else        → "Very Difficult"
#
# 4. SENTIMENT HINTS (simple keyword check, using ternary):
# positive_words = "good great excellent amazing wonderful love best"
# negative_words = "bad terrible awful horrible worst hate never"
# pos_count = sum of positive words found in text.lower()
# neg_count = sum of negative words found in text.lower()
# sentiment = "Positive 😊" if pos > neg else "Negative 😞" if neg > pos else "Neutral 😐"
#
# Print a complete text analysis report.
# ALL classification decisions must use ternary (no if/else).
# ============================================================