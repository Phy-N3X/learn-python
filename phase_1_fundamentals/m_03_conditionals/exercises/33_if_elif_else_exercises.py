# ============================================================
# MODULE 03 | LECTURE 33 - if / elif / else
# ============================================================
# What you will learn:
# - Why we need elif
# - How elif works
# - The difference between elif and separate ifs
# - Chaining multiple elif blocks
# - elif with complex conditions
# - Order matters - how Python evaluates elif chains
# - Common patterns: ranges, menus, categories
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: The problem with just if / else
# ------------------------------------------------------------

# In Lecture 02 we learned if / else - two paths.
# But real programs often need MORE than two paths.
#
# Imagine a grading system:
# 90-100 → A
# 80-89  → B
# 70-79  → C
# 60-69  → D
# 0-59   → F
#
# That's FIVE possible outcomes, not two.
#
# You could try to solve it with nested if / else:

score = 85

if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")
    else:
        if score >= 70:
            print("C")
        else:
            if score >= 60:
                print("D")
            else:
                print("F")

# This works... but look how deeply nested it gets!
# Each level adds more indentation.
# It's hard to read, hard to maintain, easy to make mistakes.
# Imagine 10 categories - it would be a nightmare.
#
# Python solves this elegantly with 'elif'.

# ------------------------------------------------------------
# PART 2: What is elif?
# ------------------------------------------------------------

# 'elif' is short for "else if".
# It adds another condition to check IF the previous ones failed.
# You can have as many elif blocks as you need.
#
# Syntax:
#     if condition_1:
#         runs if condition_1 is True
#     elif condition_2:
#         runs if condition_1 False AND condition_2 True
#     elif condition_3:
#         runs if condition_1 False AND condition_2 False AND condition_3 True
#     else:
#         runs if ALL conditions above are False
#
# Key rules:
# 1. Must start with 'if' - elif cannot exist without it
# 2. Can have zero or more elif blocks
# 3. Can have zero or one else block (at the end only)
# 4. EXACTLY ONE block runs - the first one whose condition is True
# 5. Once a match is found - remaining elifs and else are SKIPPED
# 6. Each condition ends with a colon ':'
# 7. Each block must be indented

# The grading system - clean version with elif:

score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")       # This runs! 85 >= 80 is True
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Output: Grade: B

# Much cleaner! Same indentation level for all branches.
# Easy to read, easy to add new categories.

# ------------------------------------------------------------
# PART 3: How Python evaluates elif - step by step
# ------------------------------------------------------------

# Python checks conditions ONE BY ONE, from top to bottom.
# The FIRST condition that is True → its block runs.
# ALL remaining conditions are SKIPPED (not even checked).
# If NO condition is True → else block runs (if it exists).

# Let's trace through with score = 75:

score = 75

# Step 1: score >= 90?  →  75 >= 90?  →  False → skip
# Step 2: score >= 80?  →  75 >= 80?  →  False → skip
# Step 3: score >= 70?  →  75 >= 70?  →  True  → RUN THIS BLOCK
# Step 4: (score >= 60 is never checked - already found a match)
# Step 5: (else is never checked - already found a match)

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")       # This runs!
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Output: Grade: C

# Visual flow:
#
#  score = 75
#      │
#  ┌───▼────────────┐
#  │ score >= 90?   │── False ──┐
#  └────────────────┘           │
#                           ┌───▼────────────┐
#                           │ score >= 80?   │── False ──┐
#                           └────────────────┘           │
#                                                    ┌───▼────────────┐
#                                                    │ score >= 70?   │── True ──→ print "C"
#                                                    └────────────────┘
#                                                    (everything below skipped)

# Now with score = 45:

score = 45

# Step 1: score >= 90?  →  False → skip
# Step 2: score >= 80?  →  False → skip
# Step 3: score >= 70?  →  False → skip
# Step 4: score >= 60?  →  False → skip
# Step 5: else → ALL conditions failed → run else block

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")       # This runs!

# Output: Grade: F

# ------------------------------------------------------------
# PART 4: elif vs separate ifs - critical difference
# ------------------------------------------------------------

# This is perhaps the most important concept in this lecture.
# elif and separate ifs behave VERY DIFFERENTLY.

# Example: score = 95

score = 95

# VERSION A: elif chain (CORRECT for grades)
print("--- elif chain ---")
if score >= 90:
    print("Grade: A")       # True → runs, rest SKIPPED
elif score >= 80:
    print("Grade: B")       # never checked
elif score >= 70:
    print("Grade: C")       # never checked

# Output:
# --- elif chain ---
# Grade: A

# VERSION B: separate ifs (WRONG for grades)
print("--- separate ifs ---")
if score >= 90:
    print("Grade: A")       # True → runs
if score >= 80:
    print("Grade: B")       # True → runs too! (95 >= 80 is True)
if score >= 70:
    print("Grade: C")       # True → runs too! (95 >= 70 is True)

# Output:
# --- separate ifs ---
# Grade: A
# Grade: B
# Grade: C     ← WRONG! A student can't have three grades

# The difference:
# elif chain: STOPS after first match
# separate ifs: CHECKS ALL conditions independently

# When to use which?
#
# Use elif when:
# - Categories are mutually exclusive (only one can be true)
# - You want EXACTLY ONE block to run
# - Conditions overlap (like >= checks)
#
# Use separate ifs when:
# - Conditions are truly independent
# - Multiple blocks should be able to run
# - Conditions don't overlap

# Example where separate ifs are correct:

age = 25
score = 90

# These are independent - both could be true:
if age >= 18:
    print("Adult")           # runs
if score >= 90:
    print("Excellent score") # also runs - independent condition!

# Both print - and that's correct behavior here.

# ------------------------------------------------------------
# PART 5: elif without else
# ------------------------------------------------------------

# 'else' is optional. You can have if / elif / elif with no else.
# If no conditions match - nothing runs.

day_number = int(input("Enter day number (1-7): "))

if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
# No else - if user enters 8, nothing prints

# With else for safety:

if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print(f"Invalid day number: {day_number}. Enter 1-7.")

# ------------------------------------------------------------
# PART 6: elif with equality checks - menus and categories
# ------------------------------------------------------------

# A very common use case: checking what the user chose
# from a set of specific options.

print("=== MENU ===")
print("1. Start")
print("2. Load")
print("3. Settings")
print("4. Quit")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Starting new game...")
elif choice == "2":
    print("Loading saved game...")
elif choice == "3":
    print("Opening settings...")
elif choice == "4":
    print("Goodbye!")
else:
    print(f"Invalid choice: '{choice}'. Please enter 1-4.")

# Another menu example - text commands:

command = input("Enter command: ").lower().strip()

if command == "help":
    print("Available commands: help, start, stop, status, quit")
elif command == "start":
    print("System starting...")
elif command == "stop":
    print("System stopping...")
elif command == "status":
    print("System is running normally.")
elif command == "quit":
    print("Exiting program. Goodbye!")
else:
    print(f"Unknown command: '{command}'")
    print("Type 'help' for available commands.")

# ------------------------------------------------------------
# PART 7: elif with range checks
# ------------------------------------------------------------

# Another very common pattern - checking which range a value falls in.
# Remember: ORDER MATTERS with range checks!

# Example 1: BMI categories

bmi = float(input("Enter your BMI: "))

if bmi < 0:
    print("Invalid BMI - cannot be negative")
elif bmi < 18.5:
    print("Category: Underweight")
    print("Consider consulting a nutritionist.")
elif bmi < 25.0:
    print("Category: Normal weight")
    print("Great job maintaining a healthy weight!")
elif bmi < 30.0:
    print("Category: Overweight")
    print("Consider increasing physical activity.")
elif bmi < 35.0:
    print("Category: Obese (Class I)")
    print("Please consult a doctor.")
elif bmi < 40.0:
    print("Category: Obese (Class II)")
    print("Medical supervision recommended.")
else:
    print("Category: Obese (Class III)")
    print("Urgent medical attention recommended.")

# Example 2: Temperature description

temp = float(input("Enter temperature in Celsius: "))

if temp < -30:
    print("Extreme cold ❄❄❄ - life threatening")
elif temp < -10:
    print("Very cold ❄❄ - heavy winter clothing required")
elif temp < 0:
    print("Freezing ❄ - winter clothing required")
elif temp < 10:
    print("Cold 🧥 - coat recommended")
elif temp < 20:
    print("Cool 🌤 - jacket recommended")
elif temp < 25:
    print("Comfortable 😊 - perfect weather")
elif temp < 35:
    print("Warm ☀ - light clothing")
elif temp < 40:
    print("Hot 🌡 - stay hydrated")
else:
    print("Extreme heat 🔥 - avoid going outside")

# Example 3: Age groups

age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age < 2:
    print("Infant")
elif age < 5:
    print("Toddler")
elif age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 30:
    print("Young adult")
elif age < 60:
    print("Adult")
elif age < 80:
    print("Senior")
else:
    print("Elderly")

# ------------------------------------------------------------
# PART 8: ORDER MATTERS - a critical lesson
# ------------------------------------------------------------

# The ORDER of elif conditions is crucial.
# Python stops at the FIRST True condition.
# Wrong order = wrong results!

# ❌ WRONG ORDER - ranges checked from small to large:

score = 95

if score >= 60:
    print("Grade: D")       # WRONG! 95 >= 60 is True → stops here!
elif score >= 70:
    print("Grade: C")       # never reached
elif score >= 80:
    print("Grade: B")       # never reached
elif score >= 90:
    print("Grade: A")       # never reached

# Output: Grade: D  ← WRONG for score 95!

# ✅ CORRECT ORDER - ranges checked from large to small:

if score >= 90:
    print("Grade: A")       # True → stops here ✅
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

# Output: Grade: A ✅

# The rule:
# When checking overlapping ranges with >=
# → start from the HIGHEST value and go DOWN
#
# When checking overlapping ranges with <=
# → start from the LOWEST value and go UP

# Example with <=:

speed_kmh = 45

if speed_kmh <= 0:
    print("Not moving")
elif speed_kmh <= 30:
    print("Slow")           # correct - checked after <=0
elif speed_kmh <= 60:
    print("Moderate")       # 45 <= 60 is True → runs ✅
elif speed_kmh <= 100:
    print("Fast")
elif speed_kmh <= 200:
    print("Very fast")
else:
    print("Extremely fast")

# Output: Moderate ✅

# Another order example - always put more specific conditions FIRST:

text = "Hello World"

# ❌ Wrong order - general condition catches everything:
if "o" in text:
    print("Contains o")        # catches EVERYTHING with 'o'
elif "Hello" in text:
    print("Contains Hello")    # never reached if "Hello" has 'o'!

# ✅ Correct order - specific first:
if "Hello" in text:
    print("Contains Hello")    # more specific
elif "o" in text:
    print("Contains o")        # fallback

# ------------------------------------------------------------
# PART 9: elif with compound conditions
# ------------------------------------------------------------

# Each elif condition can be as complex as needed.
# You can use and, or, not, in, etc.

# Example 1: Blood pressure categories

systolic = int(input("Enter systolic pressure (mmHg): "))
diastolic = int(input("Enter diastolic pressure (mmHg): "))

if systolic < 90 or diastolic < 60:
    print("⚠ Low blood pressure (Hypotension)")
elif systolic < 120 and diastolic < 80:
    print("✅ Normal blood pressure")
elif systolic < 130 and diastolic < 80:
    print("⚠ Elevated blood pressure")
elif systolic < 140 or diastolic < 90:
    print("⚠ High blood pressure - Stage 1")
elif systolic < 180 or diastolic < 120:
    print("🚨 High blood pressure - Stage 2")
else:
    print("🚨 Hypertensive Crisis - seek emergency care!")

# Example 2: Shipping cost calculator

weight_kg = float(input("Enter package weight (kg): "))
distance_km = int(input("Enter shipping distance (km): "))

if weight_kg <= 0 or distance_km <= 0:
    print("Invalid input - weight and distance must be positive")
elif weight_kg <= 1 and distance_km <= 100:
    print("Shipping cost: 10 PLN (light, local)")
elif weight_kg <= 1 and distance_km <= 500:
    print("Shipping cost: 15 PLN (light, regional)")
elif weight_kg <= 5 and distance_km <= 100:
    print("Shipping cost: 20 PLN (medium, local)")
elif weight_kg <= 5 and distance_km <= 500:
    print("Shipping cost: 30 PLN (medium, regional)")
elif weight_kg <= 20:
    print("Shipping cost: 50 PLN (heavy)")
else:
    print("Shipping cost: contact us for quote (very heavy)")

# Example 3: Triangle type classifier

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# First validate triangle inequality:
if a + b <= c or a + c <= b or b + c <= a:
    print("These sides cannot form a triangle!")
elif a == b == c:
    print("Equilateral triangle (all sides equal)")
elif a == b or b == c or a == c:
    print("Isosceles triangle (two sides equal)")
else:
    print("Scalene triangle (all sides different)")

# ------------------------------------------------------------
# PART 10: elif for input validation
# ------------------------------------------------------------

# A very practical pattern: validate input step by step,
# each elif catching a different type of problem.

# Example 1: Username validator

username = input("Choose a username: ").strip()

if len(username) == 0:
    print("❌ Error: Username cannot be empty")
elif len(username) < 3:
    print("❌ Error: Username too short (minimum 3 characters)")
elif len(username) > 20:
    print("❌ Error: Username too long (maximum 20 characters)")
elif " " in username:
    print("❌ Error: Username cannot contain spaces")
elif username[0].isdigit():
    print("❌ Error: Username cannot start with a number")
else:
    print(f"✅ Username '{username}' is valid!")

# Example 2: Grade input validator

grade_input = input("Enter grade (A/B/C/D/F): ").upper().strip()

if len(grade_input) == 0:
    print("❌ No grade entered")
elif len(grade_input) > 1:
    print("❌ Enter a single letter grade only")
elif grade_input not in "ABCDF":
    print(f"❌ '{grade_input}' is not a valid grade")
elif grade_input == "A":
    print("✅ Excellent!")
elif grade_input == "B":
    print("✅ Good!")
elif grade_input == "C":
    print("✅ Average")
elif grade_input == "D":
    print("⚠ Below average - consider studying more")
else:
    print("❌ Failed - please retake the exam")

# ------------------------------------------------------------
# PART 11: Returning a value based on elif
# ------------------------------------------------------------

# A very common pattern: using elif to determine a value,
# then using that value later.

# Example 1: Determine label

score = 78

if score >= 90:
    label = "Excellent"
    emoji = "🌟"
elif score >= 75:
    label = "Good"
    emoji = "✅"
elif score >= 60:
    label = "Passing"
    emoji = "👍"
else:
    label = "Failing"
    emoji = "❌"

print(f"{emoji} Result: {label} (score: {score})")
# ✅ Result: Good (score: 78)

# Example 2: Determine price tier

quantity = int(input("Enter quantity: "))

if quantity >= 1000:
    unit_price = 5.00
    tier = "Platinum"
elif quantity >= 500:
    unit_price = 7.50
    tier = "Gold"
elif quantity >= 100:
    unit_price = 10.00
    tier = "Silver"
elif quantity >= 10:
    unit_price = 12.50
    tier = "Bronze"
else:
    unit_price = 15.00
    tier = "Standard"

total = quantity * unit_price
print(f"Tier: {tier}")
print(f"Unit price: {unit_price:.2f} PLN")
print(f"Total: {total:.2f} PLN")

# Example 3: Determine season

month = int(input("Enter month number (1-12): "))

if month in [12, 1, 2]:       # 'in' works with lists too (preview!)
    season = "Winter ❄"
elif month in [3, 4, 5]:
    season = "Spring 🌸"
elif month in [6, 7, 8]:
    season = "Summer ☀"
elif month in [9, 10, 11]:
    season = "Autumn 🍂"
else:
    season = "Invalid month"

print(f"Month {month} → {season}")

# ------------------------------------------------------------
# PART 12: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: elif before if

# elif x > 5:          ← SyntaxError! elif without if
#     print("yes")

# ❌ MISTAKE 2: else before elif

score = 75
# if score >= 90:
#     print("A")
# else:
#     print("other")
# elif score >= 80:    ← SyntaxError! elif after else
#     print("B")

# ✅ Correct order: if → elif → elif → else

# ❌ MISTAKE 3: condition after else

# else score < 60:     ← SyntaxError! else has no condition
#     print("F")

# ✅ else never has a condition

# ❌ MISTAKE 4: wrong order of conditions (overlapping ranges)

score = 95

# Wrong - all scores >= 60 go to first branch:
if score >= 60:
    print("D")          # 95 >= 60 → True → stops here!
elif score >= 70:
    print("C")          # never reached
elif score >= 80:
    print("B")          # never reached
elif score >= 90:
    print("A")          # never reached

# ✅ Correct - highest threshold first:
if score >= 90:
    print("A")          # 95 >= 90 → True ✅
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")

# ❌ MISTAKE 5: using elif when separate ifs are needed

age = 25
score = 95

# Wrong - only one of these can run:
if age >= 18:
    print("Adult")
elif score >= 90:       # never checked if age >= 18!
    print("Excellent")

# ✅ Correct - these are independent checks:
if age >= 18:
    print("Adult")
if score >= 90:
    print("Excellent")  # checked independently

# ❌ MISTAKE 6: forgetting else for invalid input

day = int(input("Enter day (1-7): "))

if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
# ... etc.
# No else → user entering 99 gets no feedback!

# ✅ Always add else for user input:
if day == 1:
    print("Monday")
elif day == 2:
    print("Tuesday")
else:
    print(f"Invalid day: {day}")    # catches everything unexpected

# ❌ MISTAKE 7: repeating the same condition

x = 50

if x > 100:
    print("large")
elif x > 100:           # identical to the if! Will never run
    print("also large") # dead code
else:
    print("small")

# ❌ MISTAKE 8: missing colon

# if x > 5:
#     print("yes")
# elif x > 0       ← SyntaxError! Missing colon
#     print("positive")

# ✅ Every branch needs a colon:
if x > 100:
    print("large")
elif x > 0:
    print("positive")
else:
    print("zero or negative")

# ------------------------------------------------------------
# PART 13: Real-world use cases
# ------------------------------------------------------------

# Use case 1: Blood type compatibility
blood_type = input("Enter blood type (A/B/AB/O): ").upper()

if blood_type == "O":
    print("Universal donor - can donate to: A, B, AB, O")
elif blood_type == "A":
    print("Can donate to: A, AB")
elif blood_type == "B":
    print("Can donate to: B, AB")
elif blood_type == "AB":
    print("Universal recipient - can receive from: A, B, AB, O")
else:
    print(f"Unknown blood type: {blood_type}")

# Use case 2: pH scale interpreter
ph = float(input("Enter pH value (0-14): "))

if ph < 0 or ph > 14:
    print("Invalid pH - must be between 0 and 14")
elif ph < 2:
    print("Strongly acidic (e.g. battery acid)")
elif ph < 5:
    print("Weakly acidic (e.g. vinegar, coffee)")
elif ph < 6:
    print("Mildly acidic (e.g. skin, rain)")
elif ph < 7:
    print("Slightly acidic")
elif ph == 7:
    print("Neutral (e.g. pure water)")
elif ph < 8:
    print("Slightly alkaline")
elif ph < 10:
    print("Mildly alkaline (e.g. baking soda)")
elif ph < 12:
    print("Weakly alkaline (e.g. soap)")
else:
    print("Strongly alkaline (e.g. bleach)")

# Use case 3: GC content interpreter for DNA
sequence = input("Enter DNA sequence: ").upper()
g_count = sequence.count("G")
c_count = sequence.count("C")
total = len(sequence)

if total == 0:
    print("Empty sequence!")
else:
    gc_content = (g_count + c_count) / total * 100

    if gc_content < 35:
        print(f"GC content: {gc_content:.1f}% - Low")
        print("Sequence may have low thermal stability")
    elif gc_content < 50:
        print(f"GC content: {gc_content:.1f}% - Moderate-Low")
    elif gc_content < 60:
        print(f"GC content: {gc_content:.1f}% - Moderate-High")
        print("Good stability for PCR")
    elif gc_content < 75:
        print(f"GC content: {gc_content:.1f}% - High")
        print("High thermal stability")
    else:
        print(f"GC content: {gc_content:.1f}% - Very High")
        print("May require special PCR conditions")

# Use case 4: Enzyme activity based on pH and temperature
ph = float(input("Enter pH: "))
temp = float(input("Enter temperature (°C): "))

if ph < 0 or ph > 14:
    print("Invalid pH")
elif temp < 0 or temp > 100:
    print("Invalid temperature")
elif 6.5 <= ph <= 7.5 and 35 <= temp <= 40:
    print("Optimal conditions - maximum enzyme activity!")
elif 6.0 <= ph <= 8.0 and 30 <= temp <= 45:
    print("Good conditions - high enzyme activity")
elif 5.0 <= ph <= 9.0 and 20 <= temp <= 50:
    print("Suboptimal conditions - reduced activity")
else:
    print("Poor conditions - minimal or no enzyme activity")

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ elif = "else if" - adds more conditions to check
# ✅ Syntax: if → elif → elif → ... → else
# ✅ EXACTLY ONE block runs - the first True condition
# ✅ else is optional - catches everything if all elifs fail
# ✅ elif ≠ separate ifs - elif stops at first match!
# ✅ ORDER MATTERS - wrong order = wrong results
# ✅ For >= ranges: start from highest value and go down
# ✅ For <= ranges: start from lowest value and go up
# ✅ elif can use complex conditions (and, or, not, in)
# ✅ Always add else to handle unexpected/invalid input

# Quick reference:
# ┌──────────────────────────────────────────────────────────┐
# │ if condition_1:       ← checked first                   │
# │     block_1                                              │
# │ elif condition_2:     ← checked only if condition_1 False│
# │     block_2                                              │
# │ elif condition_3:     ← checked only if all above False  │
# │     block_3                                              │
# │ else:                 ← runs if ALL conditions False     │
# │     block_default                                        │
# │                                                          │
# │ ✅ Only ONE block runs                                   │
# │ ✅ First True condition wins                             │
# │ ✅ Order matters for overlapping ranges                  │
# │ ✅ else has no condition                                 │
# │ ✅ elif cannot exist without if                          │
# └──────────────────────────────────────────────────────────┘
```

---

```python
# ============================================================
# MODULE 03 | EXERCISES 03 - if / elif / else
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Create a variable 'score' and set it to any value.
# Write an if/elif/else chain to print the letter grade:
# - 90 to 100 → "Grade: A - Excellent!"
# - 80 to 89  → "Grade: B - Good!"
# - 70 to 79  → "Grade: C - Average"
# - 60 to 69  → "Grade: D - Below average"
# - 0 to 59   → "Grade: F - Failed"
#
# Test with at least 5 different values (one per category).
#
# Example output (score = 85):
# Grade: B - Good!
#
# Example output (score = 42):
# Grade: F - Failed

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what each elif chain will print BEFORE running.
# Write your prediction as a comment.
# Then run and verify.
#
# x = 50
#
# if x > 100:
#     print("A")          # prediction: ?
# elif x > 75:
#     print("B")          # prediction: ?
# elif x > 50:
#     print("C")          # prediction: ?
# elif x > 25:
#     print("D")          # prediction: ?
# else:
#     print("E")          # prediction: ?
#
# ---
#
# y = 75
#
# if y > 100:
#     print("F")          # prediction: ?
# elif y >= 75:
#     print("G")          # prediction: ?
# elif y >= 50:
#     print("H")          # prediction: ?
# else:
#     print("I")          # prediction: ?
#
# ---
#
# z = 0
#
# if z:
#     print("J")          # prediction: ?
# elif z == 0:
#     print("K")          # prediction: ?
# else:
#     print("L")          # prediction: ?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL the errors in the code below.
# Write what each error is as a comment next to each line.
# Then fix all errors so the code runs correctly.
#
# score = 75
#
# elif score >= 90:
#     print("A")
# if score >= 80:
#     print("B")
# elif score >= 70
#     print("C")
# else score >= 60:
#     print("D")
# else:
#     print("F")
# elif score == 75:
#     print("Exactly 75")

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Ask the user to enter a month number (1-12).
# Print the name of the month and what season it belongs to.
# Handle invalid input (numbers outside 1-12).
#
# Seasons:
# Winter: December (12), January (1), February (2)
# Spring: March (3), April (4), May (5)
# Summer: June (6), July (7), August (8)
# Autumn: September (9), October (10), November (11)
#
# Example interaction 1:
# Enter month number (1-12): 7
# Month: July
# Season: Summer ☀
#
# Example interaction 2:
# Enter month number (1-12): 15
# Invalid month number. Please enter 1-12.

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Build a simple command interpreter.
# Ask the user to enter a command (as text).
# Convert to lowercase and strip whitespace.
#
# Commands and responses:
# "hello" or "hi"  → "Hello! How can I help you?"
# "help"           → "Commands: hello, help, time, date, quit"
# "time"           → "Sorry, I don't have a clock!"
# "date"           → "Sorry, I don't know today's date!"
# "quit" or "exit" → "Goodbye! See you next time."
# anything else    → "Unknown command. Type 'help' for options."
#
# Tip: use 'or' in your conditions to handle multiple inputs.
#
# Example interaction 1:
# Enter command: Hello
# Hello! How can I help you?
#
# Example interaction 2:
# Enter command: fly
# Unknown command. Type 'help' for options.

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Order matters! Fix the broken grading system below.
# The conditions are in the wrong order - fix them.
# Do NOT change the values, only reorder the elif blocks.
# Explain in a comment WHY the original order was wrong.
#
# score = 88
#
# if score >= 60:
#     print("Grade: D")
# elif score >= 70:
#     print("Grade: C")
# elif score >= 80:
#     print("Grade: B")
# elif score >= 90:
#     print("Grade: A")
# else:
#     print("Grade: F")
#
# Current (wrong) output: Grade: D
# Expected output:        Grade: B

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a wind speed classifier using the Beaufort scale
# (simplified version).
#
# Wind speed categories:
# 0 km/h         → Calm
# 1-5 km/h       → Light air
# 6-11 km/h      → Light breeze
# 12-19 km/h     → Gentle breeze
# 20-28 km/h     → Moderate breeze
# 29-38 km/h     → Fresh breeze
# 39-49 km/h     → Strong breeze
# 50-61 km/h     → Near gale
# 62-74 km/h     → Gale
# 75-88 km/h     → Strong gale
# 89-102 km/h    → Storm
# Above 102 km/h → Violent storm / Hurricane
#
# Ask user for wind speed in km/h.
# Validate that it's not negative.
# Print the category and a brief description.
#
# Example interaction:
# Enter wind speed (km/h): 45
# Category: Strong breeze
# Large branches move, difficult to use umbrella

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a ticket price calculator with multiple categories.
#
# Pricing:
# Age < 3          → FREE
# Age 3-5          → 10 PLN (toddler)
# Age 6-12         → 20 PLN (child)
# Age 13-17        → 25 PLN (teen)
# Age 18-64        → 40 PLN (adult)
# Age 65+          → 22 PLN (senior)
# Invalid age (<0) → "Invalid age"
#
# Additionally:
# - If it's a Monday → apply 20% discount to any non-free ticket
# - Print the original and final price
#
# Ask user for age and whether it's Monday (yes/no).
#
# Example interaction 1:
# Enter age: 10
# Is it Monday? (yes/no): yes
# Category: Child
# Original price: 20 PLN
# Monday discount: -4.00 PLN
# Final price: 16.00 PLN
#
# Example interaction 2:
# Enter age: 2
# Is it Monday? (yes/no): yes
# Category: Toddler
# Price: FREE (no discount applicable)

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this code and predict ALL outputs.
# Write predictions as comments BEFORE each print.
# Then run and verify.
#
# def classify(n):                         ← ignore 'def' for now
#     if n < 0:                               just trace the logic
#         return "negative"
#     elif n == 0:
#         return "zero"
#     elif n < 10:
#         return "small"
#     elif n < 100:
#         return "medium"
#     elif n < 1000:
#         return "large"
#     else:
#         return "huge"
#
# values = [-5, 0, 7, 50, 500, 9999]
#
# For each value, predict what classify() returns:
# classify(-5)   → prediction: ?
# classify(0)    → prediction: ?
# classify(7)    → prediction: ?
# classify(50)   → prediction: ?
# classify(500)  → prediction: ?
# classify(9999) → prediction: ?
#
# Write the if/elif/else chain yourself (without def/return)
# and test it manually for each value using a variable 'n'.
#
# Final question (answer as comment):
# Why does classify(10) return "medium" and not "small"?
# What would you change to make 10 → "small"?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a full BMI calculator with health advice.
#
# Ask user for weight (kg) and height (m).
# Validate both inputs (must be positive numbers).
# Calculate BMI = weight / height²
#
# Categories (WHO standard):
# BMI < 16.0      → Severe thinness
# BMI 16.0-16.9   → Moderate thinness
# BMI 17.0-18.4   → Mild thinness
# BMI 18.5-24.9   → Normal weight ✅
# BMI 25.0-29.9   → Pre-obesity (Overweight)
# BMI 30.0-34.9   → Obese class I
# BMI 35.0-39.9   → Obese class II
# BMI >= 40.0     → Obese class III
#
# Print:
# - Calculated BMI (2 decimal places)
# - Category name
# - Whether BMI is below, within, or above normal range
# - One specific health tip per category
#
# Example interaction:
# Enter weight (kg): 70
# Enter height (m): 1.75
#
# BMI: 22.86
# Category: Normal weight ✅
# Status: Within healthy range
# Tip: Maintain your current diet and activity level!

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a pH level analyzer for laboratory use.
#
# Ask user for pH value.
# Validate: must be between 0.0 and 14.0.
#
# Categories:
# 0.0 - 1.0   → Strongly acidic (e.g. gastric acid)
# 1.1 - 3.0   → Highly acidic (e.g. lemon juice)
# 3.1 - 5.0   → Moderately acidic (e.g. coffee, wine)
# 5.1 - 6.9   → Mildly acidic (e.g. milk, skin)
# 7.0         → Neutral (pure water)
# 7.1 - 8.0   → Mildly alkaline (e.g. blood, sea water)
# 8.1 - 10.0  → Moderately alkaline (e.g. baking soda)
# 10.1 - 12.0 → Highly alkaline (e.g. ammonia)
# 12.1 - 14.0 → Strongly alkaline (e.g. bleach, NaOH)
#
# Print:
# - The pH value
# - The category
# - A real-world example substance
# - Whether it's safe to handle without protection (pH 4-10)
# - How far it is from neutral (pH 7.0)
#
# Example interaction:
# Enter pH value: 3.5
# pH: 3.5
# Category: Moderately acidic
# Example substance: coffee, wine, vinegar
# Safety: ⚠ Handle with caution - wear gloves
# Distance from neutral: 3.5 units below pH 7.0

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a water state classifier based on temperature and pressure.
#
# Under standard pressure (1 atm):
# Temperature < -273.15°C  → Invalid (below absolute zero)
# Temperature < 0°C        → Ice (solid) ❄
# Temperature == 0°C       → Melting point (solid/liquid boundary)
# Temperature < 100°C      → Liquid water 💧
# Temperature == 100°C     → Boiling point (liquid/gas boundary)
# Temperature >= 100°C     → Steam (gas) 💨
#
# Ask user for temperature and pressure (atm).
# If pressure < 1 atm → boiling point is lower:
#   approximate boiling point = 100 - (1 - pressure) * 28.6
# If pressure > 1 atm → boiling point is higher:
#   approximate boiling point = 100 + (pressure - 1) * 28.6
#
# Recalculate states based on adjusted boiling point.
#
# Print:
# - Temperature and pressure entered
# - Adjusted boiling point (if different from 100°C)
# - State of water
# - A brief scientific explanation
#
# Example interaction:
# Enter temperature (°C): 85
# Enter pressure (atm): 0.5
# Adjusted boiling point: 85.7°C
# State: Boiling point (liquid/gas boundary)
# At 0.5 atm, water boils at a lower temperature than at sea level.

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a codon to amino acid translator (partial).
#
# A codon is a 3-letter DNA sequence that codes for an amino acid.
# Implement translation for these codons:
#
# ATG → Methionine (Met) - START codon
# TAA → STOP
# TAG → STOP
# TGA → STOP
# GCT → Alanine (Ala)
# TGT → Cysteine (Cys)
# GAT → Aspartic acid (Asp)
# GAA → Glutamic acid (Glu)
# TTT → Phenylalanine (Phe)
# GGT → Glycine (Gly)
# CAT → Histidine (His)
# ATT → Isoleucine (Ile)
# AAA → Lysine (Lys)
# anything else → "Unknown codon"
#
# Ask user for a 3-letter codon.
# Convert to uppercase.
# Validate: must be exactly 3 characters.
# Validate: must contain only A, T, C, G.
# Print the amino acid or stop/unknown message.
# Also print whether it's a START, STOP, or coding codon.
#
# Example interaction 1:
# Enter codon: atg
# Codon: ATG
# Amino acid: Methionine (Met)
# Type: START codon - begins protein synthesis
#
# Example interaction 2:
# Enter codon: TAA
# Codon: TAA
# Amino acid: STOP
# Type: STOP codon - ends protein synthesis
#
# Example interaction 3:
# Enter codon: XYZ
# ❌ Invalid: contains non-DNA characters

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a comprehensive weather advisory system.
#
# Ask user for:
# - Temperature in Celsius (float)
# - Wind speed in km/h (float)
# - Humidity percentage (0-100, int)
# - Is it raining? (yes/no)
#
# Validate all inputs first:
# - Temperature: -90 to 60°C (Earth's range)
# - Wind speed: 0 to 400 km/h
# - Humidity: 0 to 100%
#
# Calculate:
# 1. Heat index (feels like temperature when hot):
#    Only applies when temp >= 27°C AND humidity >= 40%
#    feels_like = temp + (0.33 * humidity / 100 * 6.105) - 4.0
#    (simplified formula)
#
# 2. Wind chill (feels like temperature when cold):
#    Only applies when temp <= 10°C AND wind > 4.8 km/h
#    feels_like = 13.12 + 0.6215*temp - 11.37*(wind**0.16)
#                 + 0.3965*temp*(wind**0.16)
#
# Classify overall conditions as:
# "Dangerous" / "Severe" / "Poor" / "Moderate" / "Good" / "Excellent"
# Based on combination of all factors.
#
# Print a full weather report with:
# - All input values
# - Feels-like temperature (if applicable)
# - Condition classification
# - At least 3 specific safety/clothing recommendations
#   based on the conditions
#
# Example interaction:
# Temperature: -15
# Wind speed: 40
# Humidity: 80
# Raining: no
#
# ===== WEATHER REPORT =====
# Temperature:    -15.0°C
# Wind speed:     40.0 km/h
# Humidity:       80%
# Precipitation:  None
# Feels like:     -26.3°C (wind chill)
# Conditions:     Severe ⚠
#
# Recommendations:
# → Wear insulated waterproof jacket
# → Cover all exposed skin - frostbite risk in 30 min
# → Limit time outdoors to under 20 minutes

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a DNA sequence quality analyzer.
#
# Ask user for a DNA sequence (string of letters).
#
# Perform ALL of the following analyses using if/elif/else:
#
# 1. VALIDATION:
#    - Empty sequence → stop and report
#    - Contains invalid characters (not A/T/C/G) → report which ones
#    - Length < 6 → "Too short for meaningful analysis"
#
# 2. LENGTH CLASSIFICATION:
#    < 20 bp          → "Oligonucleotide (primer-sized)"
#    20 - 99 bp       → "Short sequence"
#    100 - 999 bp     → "Medium sequence (gene fragment)"
#    1000 - 9999 bp   → "Long sequence (small gene)"
#    >= 10000 bp      → "Very long sequence (large gene / operon)"
#
# 3. GC CONTENT ANALYSIS:
#    Calculate GC% = (G+C) / total * 100
#    < 20%    → "Very low GC - AT rich, low stability"
#    20-35%   → "Low GC content"
#    35-50%   → "Moderate GC content"
#    50-65%   → "High GC content - good PCR stability"
#    65-80%   → "Very high GC content"
#    > 80%    → "Extremely high GC - may cause PCR problems"
#
# 4. START/STOP CODON DETECTION:
#    - Check if sequence starts with ATG → has start codon
#    - Check if sequence ends with TAA, TAG, or TGA → has stop codon
#    - Report all four possibilities (both/one/neither)
#
# 5. HOMOPOLYMER CHECK:
#    - Check if sequence contains AAAA, TTTT, CCCC, or GGGG
#    - If yes → "⚠ Contains homopolymer run - may affect sequencing"
#    - If no  → "No homopolymer issues detected"
#
# Print a full lab report with all 5 sections clearly labeled.
#
# Example interaction:
# Enter DNA sequence: ATGCGATACGCTTAAGGCCCCTAA
#
# ===== DNA SEQUENCE ANALYSIS REPORT =====
#
# [VALIDATION]
# ✅ Sequence is valid
# Sequence: ATGCGATACGCTTAAGGCCCCTAA
# Length: 24 bp
#
# [LENGTH]
# Category: Short sequence
#
# [GC CONTENT]
# G count: 5, C count: 7, Total GC: 12
# GC content: 50.0%
# Category: High GC content - good PCR stability
#
# [START/STOP CODONS]
# Start codon (ATG): ✅ Found at position 0
# Stop codon at end: ✅ Found (TAA)
# → Complete ORF detected!
#
# [HOMOPOLYMER CHECK]
# No homopolymer issues detected
# ============================================================