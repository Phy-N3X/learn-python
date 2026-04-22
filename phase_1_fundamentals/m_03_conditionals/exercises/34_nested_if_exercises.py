# ============================================================
# MODULE 03 | EXERCISES 34 - Nested if
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Create two variables:
# temperature = 35
# is_sunny = True
#
# Write a nested if to determine what to do:
# - If temperature > 30:
#     - If it's sunny → "Go to the beach! 🏖"
#     - If it's not sunny → "Stay home - hot but cloudy"
# - If temperature is not > 30:
#     - If it's sunny → "Nice day for a walk 🚶"
#     - If it's not sunny → "Maybe stay indoors ☁"
#
# Test with all 4 combinations of values.
#
# Expected output (temp=35, sunny=True):
# Go to the beach! 🏖

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what this nested if code will print.
# Write your prediction as a comment before each print.
# Then run and verify.
#
# a = 10
# b = 5
# c = 8
#
# if a > b:
#     if a > c:
#         print("A")        # prediction: ?
#     else:
#         print("B")        # prediction: ?
# else:
#     if b > c:
#         print("C")        # prediction: ?
#     else:
#         print("D")        # prediction: ?
#
# ---
#
# x = 0
# y = 10
#
# if x:
#     if y:
#         print("E")        # prediction: ?
#     else:
#         print("F")        # prediction: ?
# else:
#     if y:
#         print("G")        # prediction: ?
#     else:
#         print("H")        # prediction: ?
#
# Final question (answer as comment):
# In the second block, why does 'if x' go to else?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL errors in the code below.
# Write what each error is as a comment next to the line.
# Then fix all errors so the code runs correctly.
#
# age = 20
# has_license = True
#
# if age >= 18:
#     print("Old enough")
#         if has_license:
#         print("Can drive")
#     else
#         print("Get a license first")
# else:
#     print("Too young to drive")
#     if has_license == True:
#         print("License obtained early?")

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Build a simple zoo animal classifier using nested ifs.
#
# Ask the user:
# 1. Does it have fur? (yes/no)
# 2. Does it lay eggs? (yes/no)
#
# Use nested ifs to classify:
# - Fur + eggs     → "Monotreme (e.g. Platypus)"
# - Fur + no eggs  → "Mammal (e.g. Dog, Cat)"
# - No fur + eggs  → "Reptile or Bird (e.g. Snake, Eagle)"
# - No fur + no eggs → "Amphibian or Fish (e.g. Frog, Salmon)"
#
# Example interaction:
# Does it have fur? (yes/no): yes
# Does it lay eggs? (yes/no): no
# Classification: Mammal (e.g. Dog, Cat)

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Create a simple number analyzer using nested ifs.
# Ask the user to enter a number.
#
# First check: is it positive, negative, or zero?
# If positive:
#   - Nested check: is it even or odd?
#   - Nested check: is it less than 100?
# If negative:
#   - Nested check: is it greater than -100?
# If zero:
#   - Print "You entered zero - neither positive nor negative"
#
# Example interaction 1 (user enters 42):
# 42 is positive
# 42 is even
# 42 is less than 100
#
# Example interaction 2 (user enters -50):
# -50 is negative
# -50 is greater than -100
#
# Example interaction 3 (user enters 0):
# You entered zero - neither positive nor negative

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a train ticket validator using nested ifs.
#
# Variables to use:
# ticket_valid = True
# seat_reserved = False
# is_first_class = False
# train_on_time = True
#
# Logic:
# - If ticket is NOT valid → "Invalid ticket - cannot board"
# - If ticket valid:
#     - If train is not on time → "Train delayed - check departures"
#     - If train on time:
#         - If seat reserved:
#             - If first class → "Welcome to First Class 🥂"
#             - If not first class → "Please proceed to your seat"
#         - If seat not reserved:
#             - "No seat reservation - find any available seat"
#
# Test with different combinations of values.
# For the given values, expected output:
# No seat reservation - find any available seat

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a water drinking advisor using nested ifs.
#
# Ask the user for:
# - Their weight in kg
# - Whether they exercised today (yes/no)
# - Whether it's summer (yes/no)
#
# Logic (nested):
# If weight <= 0 → "Invalid weight"
# If weight valid:
#   Base water = weight * 0.033
#   If exercised:
#       If summer → add 1.0L (heat + exercise)
#       If not summer → add 0.75L (exercise only)
#   If not exercised:
#       If summer → add 0.5L (heat only)
#       If not summer → no addition (base only)
#
# Print the recommendation in liters (2 decimal places).
# Also classify: < 1.5L "low", 1.5-2.5L "normal", > 2.5L "high"
#
# Example interaction:
# Weight (kg): 70
# Exercised today? (yes/no): yes
# Is it summer? (yes/no): yes
# Recommended intake: 3.31 L
# Category: high

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a login system with role-based access using nested ifs.
#
# Define these users (as variables, not a real database):
# admin_user = "admin"
# admin_pass = "admin123"
# regular_user = "user"
# regular_pass = "user123"
# admin_active = True
# user_active = True
#
# Ask for username and password.
#
# Logic:
# If username matches admin:
#   If password correct:
#     If admin account active:
#       → Show admin dashboard
#     Else:
#       → "Admin account suspended"
#   Else:
#     → "Wrong password for admin"
# Elif username matches regular user:
#   If password correct:
#     If user account active:
#       → Show user dashboard
#     Else:
#       → "Account suspended"
#   Else:
#     → "Wrong password"
# Else:
#   → "Username not found"
#
# Admin dashboard shows: "ADMIN PANEL - Full access granted"
# User dashboard shows: "USER DASHBOARD - Limited access"
#
# Test with correct admin, wrong password, unknown user.

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this nested if code step by step.
# Before each print, write your prediction as a comment.
# Then run and verify.
#
# score = 72
# attendance = 65
# is_retake = False
#
# if score >= 50:
#     if attendance >= 75:
#         if score >= 90:
#             # prediction: ?
#             print("Merit scholarship!")
#         elif score >= 75:
#             # prediction: ?
#             print("Passed with distinction")
#         else:
#             # prediction: ?
#             print("Passed")
#     else:
#         if score >= 70:
#             # prediction: ?
#             print("Passed but attendance warning")
#         else:
#             # prediction: ?
#             print("Borderline - attendance too low")
# else:
#     if is_retake:
#         # prediction: ?
#         print("Failed - no more retakes")
#     else:
#         # prediction: ?
#         print("Failed - retake available")
#
# Answer as comments:
# Which if block does the output come from?
# What would change if attendance = 80?
# What would change if score = 45?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a blood pressure analyzer with nested ifs.
#
# Ask user for:
# - Systolic pressure (upper number, mmHg)
# - Diastolic pressure (lower number, mmHg)
# - Age of the patient
#
# Validation (outer checks):
# - Systolic must be 60-250, diastolic must be 40-150
# - If invalid → print specific error and stop
#
# Classification (nested inside valid check):
# Hypotension: systolic < 90 OR diastolic < 60
#   - If age > 65 → "Low BP - common in elderly, monitor closely"
#   - If age <= 65 → "Low BP - consult doctor"
# Normal: systolic < 120 AND diastolic < 80
#   - If age > 65 → "Normal BP - excellent for your age!"
#   - If age <= 65 → "Normal BP - keep it up!"
# Elevated: systolic 120-129 AND diastolic < 80
#   → "Elevated - lifestyle changes recommended"
#   - Nested: if age > 40 → add "Increased risk - monitor regularly"
# High Stage 1: systolic 130-139 OR diastolic 80-89
#   → "High BP Stage 1 - consult doctor"
# High Stage 2: systolic >= 140 OR diastolic >= 90
#   - If systolic >= 180 OR diastolic >= 120
#       → "CRISIS - seek emergency care immediately!"
#   - Otherwise
#       → "High BP Stage 2 - medical treatment needed"
#
# Print full report with values, category, and advice.

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a simplified enzyme kinetics analyzer.
#
# Ask user for:
# - Substrate concentration in mM (float)
# - Temperature in Celsius (float)
# - pH value (float)
#
# Validate all inputs first (outer check):
# - Concentration: must be >= 0
# - Temperature: must be 0-100°C
# - pH: must be 0-14
#
# If all valid, analyze conditions (nested):
#
# Temperature analysis:
# If temperature < 20:
#   If pH 6-8 → "Low activity - cold and suboptimal pH"
#   Else → "Very low activity - cold and wrong pH"
# If 20 <= temperature <= 42:
#   If pH 6.5-7.5:
#     If concentration >= 1.0 → "Optimal conditions - maximum activity"
#     Else → "Optimal pH and temp but substrate limited"
#   If pH 5-6.5 or 7.5-9:
#     → "Suboptimal pH - reduced activity"
#   Else:
#     → "Wrong pH - enzyme likely denatured"
# If temperature > 42:
#   If temperature > 60 → "Enzyme denatured - no activity"
#   Else → "High temperature - reduced activity"
#
# Print a lab report with all values and analysis.

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a flight booking eligibility checker.
#
# Ask user for:
# - Age
# - Is travelling alone? (yes/no)
# - Has valid passport? (yes/no)
# - Destination type: domestic / international
# - Has visa? (yes/no) - only ask if international
#
# Nested logic:
# If no passport → "Cannot travel - valid passport required"
# If has passport:
#   If domestic:
#     If age < 12:
#       If alone → "Cannot travel alone under 12 domestically"
#       If not alone → "Can travel domestically with guardian"
#     Elif age < 18:
#       If alone → "Can travel alone domestically (teen)"
#       If not alone → "Can travel domestically"
#     Else → "Full domestic travel privileges"
#   If international:
#     If no visa → "Visa required for international travel"
#     If has visa:
#       If age < 12:
#         If alone → "Cannot travel internationally alone under 12"
#         If not alone → "Can travel internationally with guardian"
#       Elif age < 18:
#         → "Can travel internationally with guardian consent"
#       Else → "Full international travel privileges"
#
# Print a boarding eligibility report.

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a DNA replication fidelity analyzer.
#
# A DNA sequence is being copied.
# The copy has some errors.
# Analyze the fidelity of the copy.
#
# Ask user for:
# - Original DNA sequence (string)
# - Copied DNA sequence (string)
#
# Validation (outer nested checks):
# - Both sequences must be non-empty
# - Both must contain only valid bases (A, T, C, G)
# - They must be the same length (can't compare different lengths)
#
# If all valid, analyze the copy (nested):
# Count mismatches (positions where bases differ):
# Use a loop: for i in range(len(original))
#             compare original[i] vs copy[i]
#
# Calculate error rate = mismatches / length * 100
#
# If 0 mismatches:
#   → "Perfect fidelity - no errors detected"
# If error_rate < 1%:
#   If mismatches == 1 → "Single point mutation detected"
#   Else → "Very high fidelity - minimal errors"
# If 1% <= error_rate < 5%:
#   → "Moderate error rate - possible mutagen exposure"
#   If any mismatch involves G→T or C→A → "Possible oxidative damage"
# If error_rate >= 5%:
#   If error_rate >= 20% → "Severe replication failure"
#   Else → "High error rate - significant DNA damage"
#
# Print a full replication report with:
# - Both sequences
# - Length
# - Mismatch positions and what changed (e.g. position 3: A→G)
# - Error rate
# - Assessment

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a comprehensive student scholarship eligibility system.
#
# Ask user for:
# - GPA (0.0 to 4.0)
# - Annual family income in PLN
# - Number of extracurricular activities (0 or more)
# - Is the student a first-generation college student? (yes/no)
# - Has the student received a scholarship before? (yes/no)
# - Student's field of study: STEM / Arts / Other
#
# Validate all inputs first.
#
# Eligibility logic (use nested ifs throughout):
#
# MERIT SCHOLARSHIP (GPA-based):
# If GPA >= 3.8:
#   If STEM field → 5000 PLN/month
#   If Arts field → 4000 PLN/month
#   If Other → 3500 PLN/month
# Elif GPA >= 3.5:
#   If received before → 2000 PLN (reduced renewal)
#   If not received before → 3000 PLN
# Elif GPA >= 3.0:
#   If extracurriculars >= 3 → 2000 PLN
#   Else → Not eligible for merit scholarship
# Else → Not eligible for merit scholarship
#
# NEED-BASED SCHOLARSHIP (income-based):
# If income < 20000:
#   If first-generation → 3000 PLN/month
#   Else → 2000 PLN/month
# Elif income < 40000:
#   If first-generation → 1500 PLN/month
#   Else → 1000 PLN/month
# Else → Not eligible for need-based
#
# TOTAL: merit + need (they can stack)
# If total > 7000 → cap at 7000 PLN/month
#
# Print a complete scholarship decision report with:
# - All input values
# - Merit scholarship: amount or "Not eligible"
# - Need-based scholarship: amount or "Not eligible"
# - Total award
# - Whether cap was applied
# - Personalized message based on field and GPA

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a hospital patient triage system using nested ifs.
# Triage determines how urgently a patient needs care.
#
# Ask for:
# - Heart rate (beats per minute)
# - Blood oxygen level SpO2 (%)
# - Temperature (°C)
# - Systolic blood pressure (mmHg)
# - Is patient conscious? (yes/no)
# - Is patient breathing? (yes/no)
# - Pain level (0-10)
#
# Triage levels (from most to least urgent):
# LEVEL 1 - IMMEDIATE (Red): Life threatening
# LEVEL 2 - URGENT (Orange): Serious but stable
# LEVEL 3 - LESS URGENT (Yellow): Needs attention
# LEVEL 4 - NON-URGENT (Green): Minor issues
#
# Logic (nested ifs, check most critical first):
#
# If NOT breathing → LEVEL 1 "Respiratory arrest - CPR needed"
# If NOT conscious:
#   If heart rate < 40 or > 180 → LEVEL 1 "Critical - cardiac emergency"
#   If SpO2 < 85 → LEVEL 1 "Critical hypoxia"
#   Else → LEVEL 2 "Unconscious but vitals stable"
# If conscious:
#   If SpO2 < 90:
#     If SpO2 < 85 → LEVEL 1 "Severe hypoxia"
#     Else → LEVEL 2 "Moderate hypoxia - oxygen needed"
#   Elif temperature > 41 or temperature < 35:
#     If temperature > 42 → LEVEL 1 "Hyperthermia emergency"
#     If temperature < 34 → LEVEL 1 "Hypothermia emergency"
#     Else → LEVEL 2 "Extreme temperature - monitor closely"
#   Elif systolic < 80 or systolic > 200:
#     → LEVEL 2 "Blood pressure crisis"
#   Elif heart_rate < 50 or heart_rate > 150:
#     If heart_rate > 180 → LEVEL 2 "Severe tachycardia"
#     Else → LEVEL 3 "Abnormal heart rate - monitoring needed"
#   Elif pain >= 8:
#     → LEVEL 3 "Severe pain management needed"
#   Elif pain >= 5:
#     → LEVEL 3 "Moderate pain - assessment needed"
#   Else:
#     → LEVEL 4 "Stable - routine assessment"
#
# Print a full triage report:
# - All vital signs with ✅/⚠/❌ status indicators
# - Triage level and color
# - Primary concern
# - Immediate action required
# - Estimated wait time based on level:
#   Level 1: Immediate (0 min)
#   Level 2: < 15 minutes
#   Level 3: < 60 minutes
#   Level 4: < 4 hours
# ============================================================