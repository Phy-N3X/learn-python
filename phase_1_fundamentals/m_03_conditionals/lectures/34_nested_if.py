# ============================================================
# MODULE 03 | LECTURE 34 - Nested if
# ============================================================
# What you will learn:
# - What nested if statements are
# - How and when to use them
# - How indentation works with multiple levels
# - Nested if vs elif - when to use which
# - How deep nesting can go (and when to stop)
# - Flattening nested ifs - cleaner alternatives
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is a nested if?
# ------------------------------------------------------------

# A nested if is simply an if statement INSIDE another if statement.
# "Nested" means one thing placed inside another.
#
# Think of it like a series of doors:
# To reach the inner room, you must first open the outer door.
# Only after passing through the first check
# do you encounter the second check.
#
# Real life analogy:
# ┌─────────────────────────────────────────────────┐
# │ IF you have a ticket:                           │
# │     IF your seat is in row A:                   │
# │         go to the front section                 │
# │     OTHERWISE:                                  │
# │         go to the back section                  │
# │ OTHERWISE:                                      │
# │     you cannot enter                            │
# └─────────────────────────────────────────────────┘
#
# The second IF only matters if the first IF is True.
# If you don't have a ticket, it doesn't matter which row you're in.
#
# This is the core idea of nested ifs:
# Inner conditions are only evaluated when outer conditions pass.

# Simplest possible example:

age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed - age and ID verified")
    else:
        print("Entry denied - no ID presented")
else:
    print("Entry denied - must be 18 or older")

# Output: Entry allowed - age and ID verified

# What happens step by step:
# 1. age >= 18? → 20 >= 18 → True → enter outer if block
# 2. has_id? → True → enter inner if block
# 3. Print "Entry allowed - age and ID verified"

# Now with age = 16:
age = 16
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed - age and ID verified")
    else:
        print("Entry denied - no ID presented")
else:
    print("Entry denied - must be 18 or older")

# Output: Entry denied - must be 18 or older
# The inner if is NEVER reached - outer condition failed.

# ------------------------------------------------------------
# PART 2: How indentation works with nested ifs
# ------------------------------------------------------------

# Each level of nesting adds 4 more spaces of indentation.
# This is how Python knows what belongs where.

# Level 0: main code (0 spaces)
# Level 1: inside first if (4 spaces)
# Level 2: inside nested if (8 spaces)
# Level 3: inside doubly nested if (12 spaces)

# Visual structure:

x = 15
y = 8
z = 3

if x > 10:                          # level 0 - main code
    print("x is large")             # level 1 - inside first if
    if y > 5:                       # level 1 - still inside first if
        print("y is also large")    # level 2 - inside nested if
        if z > 1:                   # level 2 - inside nested if
            print("z is positive")  # level 3 - inside doubly nested if
        else:
            print("z is small")     # level 3 - else of doubly nested
    else:
        print("y is small")         # level 2 - else of first nested if
else:
    print("x is small")             # level 1 - else of first if

print("Program continues")          # level 0 - back to main code

# Output:
# x is large
# y is also large
# z is positive
# Program continues

# Indentation map:
# ────────────────────────────────────────────────
# if x > 10:
#     ← 4 spaces
#     print("x is large")
#     if y > 5:
#         ← 8 spaces
#         print("y is also large")
#         if z > 1:
#             ← 12 spaces
#             print("z is positive")
# ────────────────────────────────────────────────

# ------------------------------------------------------------
# PART 3: Nested if / else combinations
# ------------------------------------------------------------

# You can mix if, elif, and else at each level of nesting.
# Each level is a completely independent decision tree.

# Example: Ticket pricing with multiple factors

age = 25
is_student = True
is_weekend = False

if age < 18:
    # Under 18 section
    if is_weekend:
        price = 15
        category = "Child Weekend"
    else:
        price = 10
        category = "Child Weekday"
else:
    # Adult section
    if is_student:
        if is_weekend:
            price = 25
            category = "Student Weekend"
        else:
            price = 20
            category = "Student Weekday"
    else:
        if is_weekend:
            price = 40
            category = "Adult Weekend"
        else:
            price = 30
            category = "Adult Weekday"

print(f"Category: {category}")
print(f"Ticket price: {price} PLN")
# Category: Student Weekday
# Ticket price: 20 PLN

# Another example: Login with role assignment

username = "admin"
password = "secret123"
is_active = True

correct_user = "admin"
correct_pass = "secret123"

if username == correct_user:
    if password == correct_pass:
        if is_active:
            print("✅ Login successful!")
            print("Role: Administrator")
            print("Access level: FULL")
        else:
            print("❌ Account is deactivated.")
            print("Contact support to reactivate.")
    else:
        print("❌ Wrong password.")
        print("Attempts remaining: 2")
else:
    print("❌ Username not found.")
    print("Please check your credentials.")

# Output:
# ✅ Login successful!
# Role: Administrator
# Access level: FULL

# ------------------------------------------------------------
# PART 4: Nested if with elif at inner levels
# ------------------------------------------------------------

# The inner levels can use elif too.
# This is a very common pattern.

# Example: BMI with age-specific advice

age = 35
bmi = 27.5

if age < 18:
    # Children/teens need different BMI interpretation
    if bmi < 18.5:
        print("Underweight for your age - consult pediatrician")
    elif bmi < 25:
        print("Healthy weight for your age")
    else:
        print("Above healthy range - consult pediatrician")
else:
    # Adults
    if bmi < 18.5:
        print("Underweight")
        if bmi < 16:
            print("⚠ Severely underweight - medical attention needed")
        elif bmi < 17:
            print("⚠ Moderately underweight")
        else:
            print("⚠ Mildly underweight")
    elif bmi < 25:
        print("Normal weight ✅")
        if age >= 65:
            print("Note: slightly higher BMI is acceptable for seniors")
    elif bmi < 30:
        print("Overweight")
        if age >= 65:
            print("Note: slightly higher BMI may be acceptable for seniors")
        else:
            print("Consider increasing physical activity")
    else:
        print("Obese - medical consultation recommended")

# Output:
# Overweight
# Consider increasing physical activity

# ------------------------------------------------------------
# PART 5: Nested if for validating multiple conditions
# ------------------------------------------------------------

# One of the most practical uses: validating input step by step.
# Each check only happens if the previous one passed.

# Example: Email validator

email = "user@example.com"

if len(email) > 0:
    if "@" in email:
        at_position = email.index("@")
        if at_position > 0:
            domain_part = email[at_position + 1:]
            if "." in domain_part:
                dot_position = domain_part.index(".")
                if dot_position > 0 and dot_position < len(domain_part) - 1:
                    print(f"✅ '{email}' appears to be a valid email")
                else:
                    print("❌ Invalid: dot is at wrong position in domain")
            else:
                print("❌ Invalid: domain has no dot")
        else:
            print("❌ Invalid: @ cannot be the first character")
    else:
        print("❌ Invalid: missing @ symbol")
else:
    print("❌ Invalid: email cannot be empty")

# Output: ✅ 'user@example.com' appears to be a valid email

# Example: Password strength validator

password = "MySecure123!"
has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        has_upper = True
    if char in "abcdefghijklmnopqrstuvwxyz":
        has_lower = True
    if char in "0123456789":
        has_digit = True
    if char in "!@#$%^&*()":
        has_special = True

if len(password) >= 8:
    if has_upper:
        if has_lower:
            if has_digit:
                if has_special:
                    print("💪 Strong password!")
                else:
                    print("🔶 Good password - add a special character")
            else:
                print("🔶 Add at least one digit")
        else:
            print("🔶 Add at least one lowercase letter")
    else:
        print("🔶 Add at least one uppercase letter")
else:
    print("❌ Password too short - minimum 8 characters")

# Output: 💪 Strong password!

# ------------------------------------------------------------
# PART 6: Nested if vs elif - choosing the right tool
# ------------------------------------------------------------

# This is crucial to understand.
# Nested if and elif solve DIFFERENT problems.
# Choosing the wrong one leads to bugs or unreadable code.

# NESTED IF: use when second condition DEPENDS ON first condition
# ELIF: use when conditions are ALTERNATIVES to each other

# Example A: Should be NESTED IF
# "If it's an animal, AND if that animal is a dog"
# Second condition only makes sense if first is true.

is_animal = True
species = "dog"

# Nested if - CORRECT here:
if is_animal:
    if species == "dog":
        print("It's a dog!")
    elif species == "cat":
        print("It's a cat!")
    else:
        print(f"It's a {species}")
else:
    print("Not an animal")

# Example B: Should be ELIF
# "If score is A, B, C, D, or F"
# These are alternatives - only one can be true.

score = 85

# elif - CORRECT here:
if score >= 90:
    print("A")
elif score >= 80:
    print("B")    # ✅ Only one grade is possible
elif score >= 70:
    print("C")
else:
    print("F")

# Would nested if work? Technically yes, but it's WRONG approach:
if score >= 90:
    print("A")
else:
    if score >= 80:
        print("B")    # Works but ugly - use elif instead!
    else:
        if score >= 70:
            print("C")
        else:
            print("F")

# Summary:
# ┌────────────────────────────────────────────────────────┐
# │ NESTED IF:                                             │
# │   if outer_condition:    ← must be True first          │
# │       if inner_condition:← then this is checked        │
# │                                                        │
# │ ELIF:                                                  │
# │   if condition_A:        ← alternatives               │
# │   elif condition_B:      ← only one runs              │
# │   elif condition_C:      ← mutually exclusive         │
# └────────────────────────────────────────────────────────┘

# ------------------------------------------------------------
# PART 7: How deep should you nest?
# ------------------------------------------------------------

# There is no technical limit to how deep you can nest.
# But readability suffers greatly beyond 2-3 levels.
#
# Rule of thumb:
# ✅ 1 level of nesting - perfectly fine
# ✅ 2 levels of nesting - usually fine
# ⚠  3 levels of nesting - consider restructuring
# ❌ 4+ levels of nesting - almost always a design problem
#
# When you see deeply nested code, ask yourself:
# "Can I restructure this with elif or guard clauses?"

# Example of TOO DEEP nesting (hard to read):

# if condition1:
#     if condition2:
#         if condition3:
#             if condition4:
#                 if condition5:
#                     print("finally!")    # 20 spaces deep!

# This is called "arrow code" because the indentation
# forms an arrow shape pointing right →
# It's a well-known code smell (sign of poor design).

# ------------------------------------------------------------
# PART 8: Flattening nested ifs - guard clauses
# ------------------------------------------------------------

# A "guard clause" is an early check that returns/exits
# if a condition fails, avoiding deep nesting.
# Instead of nesting everything inside ifs,
# you handle failure cases FIRST and return early.

# DEEPLY NESTED version (hard to read):

def process_user(username, password, is_active, has_permission):
    if username:
        if password:
            if is_active:
                if has_permission:
                    print("Processing user request...")
                    print("Request complete!")
                else:
                    print("No permission")
            else:
                print("Account inactive")
        else:
            print("No password")
    else:
        print("No username")

# FLATTENED version with guard clauses (much cleaner):

def process_user_clean(username, password, is_active, has_permission):
    if not username:
        print("No username")
        return                  # exit early - guard clause

    if not password:
        print("No password")
        return                  # exit early - guard clause

    if not is_active:
        print("Account inactive")
        return                  # exit early - guard clause

    if not has_permission:
        print("No permission")
        return                  # exit early - guard clause

    # Only reaches here if ALL checks passed!
    print("Processing user request...")
    print("Request complete!")

# Don't worry about 'def' and 'return' yet -
# we'll cover functions in a later module.
# The concept to understand: handle failures EARLY
# to avoid deep nesting.

# Same idea WITHOUT functions - just using variables:

username = "anna"
password = "pass123"
is_active = True
has_permission = True

# Guard clause style (without functions):
valid = True

if not username:
    print("No username")
    valid = False

if valid and not password:
    print("No password")
    valid = False

if valid and not is_active:
    print("Account inactive")
    valid = False

if valid and not has_permission:
    print("No permission")
    valid = False

if valid:
    print("✅ Processing user request...")

# Output: ✅ Processing user request...

# ------------------------------------------------------------
# PART 9: Combining nested if with and/or
# ------------------------------------------------------------

# Sometimes you can replace nested ifs with combined conditions.
# This reduces nesting level.

# VERSION A: nested if
age = 25
has_ticket = True
is_vip = False

if age >= 18:
    if has_ticket:
        if is_vip:
            print("VIP entrance")
        else:
            print("Standard entrance")
    else:
        print("No ticket")
else:
    print("Too young")

# VERSION B: combined with 'and' (flatter, but different logic flow)

if age >= 18 and has_ticket and is_vip:
    print("VIP entrance")
elif age >= 18 and has_ticket and not is_vip:
    print("Standard entrance")
elif age >= 18 and not has_ticket:
    print("No ticket")
else:
    print("Too young")

# Both produce the same output.
# Which is better depends on context.
# Nested if is clearer when conditions have a natural hierarchy.
# Combined conditions are clearer when conditions are parallel.

# Another example - when 'and' simplifies things:

# NESTED (unnecessary nesting):
x = 15
if x > 0:
    if x < 100:
        print("x is between 0 and 100")

# BETTER - use 'and' or chained comparison:
if x > 0 and x < 100:
    print("x is between 0 and 100")

# BEST - use chained comparison:
if 0 < x < 100:
    print("x is between 0 and 100")    # most Pythonic!

# ------------------------------------------------------------
# PART 10: Real-world use case - ATM machine logic
# ------------------------------------------------------------

# A realistic example with multiple levels of checks.

balance = 2500.00
pin_correct = True
card_active = True
daily_limit = 1000.00
withdrawn_today = 200.00

withdrawal = float(input("Enter withdrawal amount: "))

if card_active:
    if pin_correct:
        if withdrawal > 0:
            remaining_daily = daily_limit - withdrawn_today
            if withdrawal <= remaining_daily:
                if withdrawal <= balance:
                    balance -= withdrawal
                    print("=" * 35)
                    print("✅ TRANSACTION APPROVED")
                    print("=" * 35)
                    print(f"Dispensed:       {withdrawal:.2f} PLN")
                    print(f"Remaining limit: {remaining_daily - withdrawal:.2f} PLN")
                    print(f"Account balance: {balance:.2f} PLN")
                else:
                    print("❌ Insufficient funds")
                    print(f"Available: {balance:.2f} PLN")
                    print(f"Requested: {withdrawal:.2f} PLN")
            else:
                print("❌ Daily limit exceeded")
                print(f"Daily limit:      {daily_limit:.2f} PLN")
                print(f"Already withdrawn:{withdrawn_today:.2f} PLN")
                print(f"Remaining limit:  {remaining_daily:.2f} PLN")
        else:
            print("❌ Invalid amount - must be greater than 0")
    else:
        print("❌ Incorrect PIN")
        print("Card will be blocked after 3 failed attempts")
else:
    print("❌ Card is blocked or expired")
    print("Contact your bank for assistance")

# ------------------------------------------------------------
# PART 11: Real-world use case - biological classification
# ------------------------------------------------------------

# Simplified biological organism classification

organism_type = input("Is this a prokaryote or eukaryote? ").lower()
multicellular = input("Is it multicellular? (yes/no): ").lower() == "yes"
has_cell_wall = input("Does it have a cell wall? (yes/no): ").lower() == "yes"
can_photosynthesize = input("Can it photosynthesize? (yes/no): ").lower() == "yes"

if organism_type == "prokaryote":
    if has_cell_wall:
        if can_photosynthesize:
            print("Kingdom: Bacteria (Cyanobacteria)")
            print("Example: Anabaena, Nostoc")
        else:
            print("Kingdom: Bacteria")
            print("Example: E. coli, Bacillus")
    else:
        print("Kingdom: Bacteria (Mycoplasma-like)")
        print("Example: Mycoplasma pneumoniae")
elif organism_type == "eukaryote":
    if multicellular:
        if has_cell_wall:
            if can_photosynthesize:
                print("Kingdom: Plantae")
                print("Example: Oak tree, Rose, Fern")
            else:
                print("Kingdom: Fungi")
                print("Example: Mushroom, Mold, Yeast")
        else:
            print("Kingdom: Animalia")
            print("Example: Human, Dog, Eagle")
    else:
        if can_photosynthesize:
            print("Kingdom: Protista (algae-like)")
            print("Example: Euglena, Chlamydomonas")
        else:
            print("Kingdom: Protista (protozoa-like)")
            print("Example: Amoeba, Paramecium")
else:
    print("Unknown organism type")
    print("Please enter 'prokaryote' or 'eukaryote'")

# ------------------------------------------------------------
# PART 12: Real-world use case - grade and feedback system
# ------------------------------------------------------------

# A realistic school feedback system

score = float(input("Enter exam score (0-100): "))
attendance = float(input("Enter attendance % (0-100): "))
is_extra_credit = input("Did student complete extra credit? (yes/no): ").lower() == "yes"

if 0 <= score <= 100 and 0 <= attendance <= 100:
    # Apply extra credit bonus
    if is_extra_credit:
        score = min(100, score + 5)
        print(f"Extra credit applied! Adjusted score: {score}")

    # Determine grade
    if score >= 90:
        grade = "A"
        gpa_points = 4.0
        status = "Excellent"
    elif score >= 80:
        grade = "B"
        gpa_points = 3.0
        status = "Good"
    elif score >= 70:
        grade = "C"
        gpa_points = 2.0
        status = "Average"
    elif score >= 60:
        grade = "D"
        gpa_points = 1.0
        status = "Below average"
    else:
        grade = "F"
        gpa_points = 0.0
        status = "Failing"

    # Attendance impact
    if attendance >= 90:
        attendance_note = "Excellent attendance ✅"
        if grade == "F":
            print("Note: Despite good attendance, exam score is failing")
    elif attendance >= 75:
        attendance_note = "Good attendance"
    elif attendance >= 60:
        attendance_note = "⚠ Attendance below recommended level"
        if score >= 60 and score < 70:
            print("Warning: Low attendance may affect final grade")
    else:
        attendance_note = "❌ Poor attendance - academic probation risk"
        if score >= 60:
            gpa_points = max(0, gpa_points - 0.5)
            print("Attendance penalty applied to GPA points")

    # Print report
    print("\n" + "=" * 40)
    print("       ACADEMIC PERFORMANCE REPORT")
    print("=" * 40)
    print(f"Score:      {score:.1f}/100")
    print(f"Grade:      {grade}")
    print(f"Status:     {status}")
    print(f"GPA Points: {gpa_points:.1f}")
    print(f"Attendance: {attendance:.1f}%")
    print(f"Note:       {attendance_note}")
    print("=" * 40)
else:
    print("❌ Invalid input - score and attendance must be 0-100")

# ------------------------------------------------------------
# PART 13: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Wrong indentation level

x = 10
y = 5

# Wrong - inner if is at same level as outer if:
# if x > 0:
#     print("x positive")
# if y > 0:           ← this is a SEPARATE if, not nested!
#     print("y positive")

# To actually nest, y check must be INSIDE x block:
if x > 0:
    print("x positive")
    if y > 0:           # ← 8 spaces - properly nested
        print("y also positive")

# ❌ MISTAKE 2: Using nested if when elif is appropriate

score = 85

# Wrong - nested when alternatives needed:
if score >= 90:
    print("A")
else:
    if score >= 80:     # should be elif!
        print("B")
    else:
        if score >= 70: # should be elif!
            print("C")

# ✅ Correct - use elif for alternatives:
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")

# ❌ MISTAKE 3: Forgetting that inner else belongs to inner if

temperature = 25
humidity = 80

if temperature > 30:
    if humidity > 70:
        print("Hot and humid")
    else:
        print("Hot but dry")    # else belongs to: if humidity > 70
else:
    print("Not hot")            # else belongs to: if temperature > 30

# This is correct! But beginners often get confused
# about which else belongs to which if.
# The rule: else belongs to the NEAREST unmatched if above it
# at the SAME indentation level.

# ❌ MISTAKE 4: Checking impossible conditions in inner if

age = 25

if age >= 18:
    if age < 18:        # ← impossible! age can't be both >= 18 AND < 18
        print("impossible")
    else:
        print("adult")

# ✅ Fix: restructure logic
if age >= 18:
    print("adult")
else:
    print("minor")

# ❌ MISTAKE 5: Deeply nested code that could be flattened

# Overly nested:
name = "Anna"
age = 25
score = 85

if name:
    if age >= 18:
        if score >= 60:
            print(f"{name} passed the adult exam")

# ✅ Flattened with 'and':
if name and age >= 18 and score >= 60:
    print(f"{name} passed the adult exam")

# ❌ MISTAKE 6: Incorrect else alignment

# if x > 0:
#     if y > 0:
#         print("both positive")
# else:               ← which if does this belong to?
#     print("x not positive")

# Python aligns else with the if at the same indentation level.
# Make sure your else is at the right level!

# ✅ Clear version:
x = 5
y = 3
if x > 0:
    if y > 0:
        print("both positive")
    else:               # ← this belongs to: if y > 0
        print("x positive, y not")
else:                   # ← this belongs to: if x > 0
    print("x not positive")

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Nested if = if statement inside another if statement
# ✅ Inner condition is only checked when outer condition is True
# ✅ Each nesting level adds 4 spaces of indentation
# ✅ else belongs to the nearest if at the same indentation level
# ✅ You can mix if, elif, else at each nesting level
# ✅ Nested if ≠ elif - they solve different problems:
#     Nested if: second check DEPENDS ON first check
#     elif: conditions are ALTERNATIVES to each other
# ✅ Avoid nesting deeper than 2-3 levels
# ✅ Use guard clauses to flatten deep nesting
# ✅ Sometimes 'and' can replace nested ifs (when appropriate)

# Quick reference:
# ┌──────────────────────────────────────────────────────────┐
# │ if outer_condition:         ← checked first              │
# │     # outer True block                                   │
# │     if inner_condition:     ← checked only if outer True │
# │         # both True block                                │
# │     else:                   ← outer True, inner False    │
# │         # outer True, inner False block                  │
# │ else:                       ← outer False                │
# │     # outer False block                                  │
# │     # inner if NEVER reached here                        │
# │                                                          │
# │ ✅ Inner checks only run when outer check passes         │
# │ ✅ else aligns with its matching if                      │
# │ ✅ Max recommended depth: 2-3 levels                     │
# └──────────────────────────────────────────────────────────┘