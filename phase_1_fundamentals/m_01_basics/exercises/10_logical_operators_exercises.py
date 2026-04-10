# ============================================================
# MODULE 01 | EXERCISES 10 - Logical Operators
# ============================================================
# 15 exercises - logical operators only
# Allowed from previous lectures:
#   - variables, type()                 (lecture 01)
#   - numbers, math operators           (lecture 02)
#   - string methods, slicing           (lecture 03)
#   - bool, truthy/falsy                (lecture 04)
#   - print(), f-strings                (lecture 05)
#   - input() patterns                  (lecture 06)
#   - comments and docstrings           (lecture 07)
#   - math operators                    (lecture 08)
#   - comparison operators              (lecture 09)
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Truth table practice.
# For ALL four combinations of A and B (TT, TF, FT, FF):
# Print the result of: A and B, A or B, not A, not B
#
# Format output as a table:
#
# A      B      A and B  A or B  not A   not B
# ------ ------ -------- ------- ------- -------
# True   True   True     True    False   False
# True   False  False    True    False   True
# ...
#
# Use f-string alignment to make columns neat.
# Do NOT hardcode the results - use actual operators.



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Operator precedence - predict then verify.
# Write prediction as comment BEFORE running each line.
# If wrong, explain why with a comment.
#
# not True or False
# not (True or False)
# True or False and False
# (True or False) and False
# not True and not False
# not (True and not False)
# True and False or True and True
# not False and not False or False
# not (True or False) and True
# True or True and False or False



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Truthy and Falsy - predict bool() for each value.
# Write prediction as comment BEFORE running.
#
# Values to test:
# 0, 1, -1, 0.0, 0.1, -0.1
# "", " ", "0", "False"
# [], [0], [False], [[]]
# {}, {"a": 0}, {0}
# (), (0,), (False,)
# None, True, False
# float("inf"), float("nan")
#
# Print in format: "bool(value) = True/False"
# After all predictions, write a comment:
# "Falsy values I was surprised by: ..."



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Short-circuit evaluation - predict what gets printed.
# Consider WHICH functions get called, not just the result.
#
# def a():
#     print("A evaluated")
#     return True
#
# def b():
#     print("B evaluated")
#     return False
#
# def c():
#     print("C evaluated")
#     return True
#
# For each expression below, predict:
#   - Which functions are called (in order)
#   - The final result
# Write predictions as comments, then verify.
#
# Expression 1: a() and b()
# Expression 2: b() and a()
# Expression 3: a() or b()
# Expression 4: b() or a()
# Expression 5: b() and a() and c()
# Expression 6: a() or b() or c()
# Expression 7: b() or b() or c()
# Expression 8: a() and b() and c()
# Expression 9: not a() and b()
# Expression 10: not b() or c()



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# and/or return original values - predict exact output.
# These do NOT return True/False - they return original values!
# Write prediction as comment BEFORE running.
#
# 1 and 2
# 0 and 2
# "" and "hello"
# "hi" and "hello"
# 1 and 2 and 3
# 1 and 0 and 3
# 0 and "" and []
# 1 or 2
# 0 or 2
# "" or "hello"
# "hi" or "hello"
# 0 or "" or []
# 0 or "" or "found"
# None or 0 or "" or []
# None or 0 or "" or [] or "last"



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Default value pattern using or.
#
# For each scenario, use the "or default" pattern
# to get a display value. Then check if it's correct.
#
# Scenarios:
#   1. username = ""          default = "Anonymous"
#   2. username = "Anna"      default = "Anonymous"
#   3. city     = None        default = "Unknown city"
#      (Note: None or "x" works, but is it safe for all falsy?)
#   4. score    = 0           default = "No score"
#      (Is "or default" appropriate here? Write a comment!)
#   5. items    = []          default = ["placeholder"]
#   6. price    = 0.0         default = 9.99
#      (Same question as score - comment!)
#
# For cases where "or default" is WRONG,
# show the correct alternative using "if ... is None".



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Fix the WRONG logical expressions.
# Each line has a bug - find it, explain it, fix it.
#
# Given: x = 5, fruits = ["apple", "banana"]
#
# BUG 1: check if x is 3 or 5
# print(x == 3 or 5)
#
# BUG 2: check if x is NOT in range 1-10
# print(not x > 1 and x < 10)
#
# BUG 3: check if "mango" is not in fruits
# print(not "mango" in fruits)
#
# BUG 4: check if x is between 1 and 10 AND even
# print(1 < x < 10 and x % 2 == 0 or x == 4)
#
# BUG 5: default for potentially valid 0 value
# score = 0
# display = score or "No score yet"
# print(display)   ← should print 0, not "No score yet"
#
# For each bug:
# 1. Print the buggy result with label "WRONG:"
# 2. Explain the bug as a comment
# 3. Print the fixed result with label "FIXED:"



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# De Morgan's Laws verification.
#
# Part A: Verify both laws for ALL 4 combinations.
# Print a table showing original and De Morgan equivalent:
#
# A     B     not(A and B)  (not A) or (not B)  Equal?
# ----- ----- ------------- ------------------- ------
# True  True  False         False               True
# ...
#
# Part B: Apply De Morgan to simplify these expressions.
# For each, show original AND simplified, verify they match:
#
# Expression 1: not (x > 0 and x < 10)
# Expression 2: not (name == "" or name is None)
# Expression 3: not (score < 0 or score > 100)
# Expression 4: not (is_admin and is_logged_in)
#
# Use: x=5, name="Anna", score=85, is_admin=True, is_logged_in=False
#
# Part C: Write each simplified expression as a comment
# explaining in plain English what it means.



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# all() and any() patterns.
#
# Given:
# scores  = [85, 92, 60, 78, 95, 55, 88]
# names   = ["Alice", "Bob", "", "Diana", "Eve"]
# numbers = [2, 4, 6, 8, 10, 12]
# flags   = [True, True, False, True]
#
# Using all() and any() with generator expressions:
#
#   1. Are ALL scores above 50?
#   2. Are ALL scores above 70?
#   3. Is ANY score a perfect 100?
#   4. Is ANY score below 60?
#   5. Are ALL names non-empty?  (hint: all(name for name in names))
#   6. Is ANY name longer than 5 characters?
#   7. Are ALL numbers even?
#   8. Is ANY number greater than 10?
#   9. Are ALL flags True?
#   10. Is ANY flag False?
#
# Print each with a descriptive label.
# Then: rewrite question 1 and 4 WITHOUT all()/any()
# using a manual loop and verify results match.



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Safe operations using short-circuit evaluation.
#
# Write safe versions of these operations using short-circuit.
# Each must handle the edge case WITHOUT raising an error.
#
#   1. Safe first character:
#      text can be "" - return first char or "empty"
#      result = text and text[0] or "empty"
#      Test: text="" and text="Hello"
#
#   2. Safe division:
#      b can be 0 - return result or "undefined"
#      result = b != 0 and (a / b) or "undefined"
#      Test: a=10, b=0 and a=10, b=4
#      (Note: this has a bug if result is 0! Find it and fix it!)
#
#   3. Safe dictionary access:
#      data can be None - return value or "missing"
#      data = {"name": "Anna"}
#      result = data and data.get("name") or "missing"
#      result2 = data and data.get("age") or "missing"
#
#   4. Safe nested attribute:
#      user can be None, user["address"] can be None
#      user = {"name": "Anna", "address": None}
#      city = user and user.get("address") and user["address"].get("city") or "unknown"
#
# For each: show the safe expression and test edge cases.



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a complete access control system.
# Use ONLY logical operators (and, or, not).
#
# Given user data:
#   username     = "anna"
#   is_logged_in = True
#   is_admin     = False
#   is_premium   = True
#   age          = 17
#   account_days = 45
#
# Calculate True/False for each permission:
#
#   can_view_public    = any logged-in user OR guest
#   can_post           = logged in AND (premium OR admin)
#   can_delete_own     = logged in AND account older than 30 days
#   can_delete_any     = logged in AND admin
#   can_access_adult   = logged in AND age >= 18
#   can_access_beta    = logged in AND (admin OR (premium AND age >= 18))
#   is_restricted      = logged in AND NOT admin AND NOT premium
#   needs_verification = logged in AND age < 18 AND NOT admin
#
# Print a full permissions report:
#   ================================
#   ACCESS CONTROL REPORT: anna
#   ================================
#   View public:    ✓ / ✗
#   Post content:   ✓ / ✗
#   ...
#   ================================



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Logical operator chain analysis.
# For each expression, WITHOUT running it:
#   1. Trace through step by step
#   2. Identify which values get evaluated (short-circuit)
#   3. Predict the exact return value (not just True/False)
#   4. Write the type of the returned value
#
# Values: a=0, b="", c=[], d=1, e="hello", f=[1,2,3]
#
# Expression 1: a or b or c or d
# Expression 2: d and e and f
# Expression 3: a and e or d
# Expression 4: d or a and e
# Expression 5: not a and e or b
# Expression 6: a or b or c or a or b
# Expression 7: d and e or a and f
# Expression 8: (a or b) and (c or d)
# Expression 9: not (a or b or c)
# Expression 10: a or (b and e) or (c and f) or d
#
# After predictions, verify each one.
# Write a comment for any you got wrong explaining WHY.



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# DNA sequence validator - complete version.
# Use logical operators throughout.
# Write full docstrings for all functions.
#
# def is_valid_dna(sequence):
#   Valid if:
#     - not empty
#     - all uppercase
#     - only contains A, T, G, C
#     - length is multiple of 3 (complete codons)
#   Return True/False
#
# def has_start_codon(sequence):
#   Valid if sequence starts with "ATG"
#   Return True/False
#
# def has_stop_codon(sequence):
#   Valid if last 3 chars are TAA, TAG, or TGA
#   Return True/False
#
# def is_complete_gene(sequence):
#   Valid if: is_valid_dna AND has_start AND has_stop
#   Return True/False
#
# def analyze_sequence(sequence):
#   Print full analysis using all functions above
#
# Test sequences:
#   s1 = "ATGCGATTTAAAGCGATGTAA"   ← valid complete gene
#   s2 = "atgcgatttaaa"            ← lowercase invalid
#   s3 = "ATGCGATTTAAA"            ← no stop codon
#   s4 = "CGATTTAAAGCG"            ← no start codon
#   s5 = ""                        ← empty
#   s6 = "ATGCGXTTTAA"             ← invalid character



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Logical operators without if statements.
# Solve ALL parts using ONLY:
#   and, or, not, all(), any()
# NO if/elif/else allowed anywhere!
#
# Part A: Implement these as single expressions:
#
#   1. absolute_value(x)
#      Return x if x >= 0, else -x
#      Hint: (x >= 0 and x) or -x   ← but this has a bug for x=0!
#      Find the bug and fix it using is not None or another approach.
#
#   2. max_of_two(a, b)
#      Return the larger of a and b
#      Hint: (a >= b and a) or b
#
#   3. clamp(value, low, high)
#      Return value clamped between low and high
#      Hint: combine max_of_two and min_of_two
#
#   4. is_between(x, low, high)
#      Return True if low <= x <= high
#
#   5. first_truthy(*args)
#      Return first truthy value from args or None
#      Hint: use a loop and or logic
#
# Part B: Using all() and any() only:
#   6. all_positive(numbers)  → all values > 0
#   7. any_negative(numbers)  → any value < 0
#   8. none_zero(numbers)     → no value equals 0
#   9. all_unique(items)      → all items are different
#      Hint: len(items) == len(set(items))
#   10. has_duplicates(items) → any item appears more than once
#
# Test each function with at least 3 cases.



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Complete logical reasoning system.
#
# You are building a loan approval system.
# All decisions use ONLY logical operators.
# Write full docstrings for every function.
#
# Applicant data:
# applicants = [
#     {"name": "Alice",   "age": 30, "income": 60000,
#      "credit": 750, "employed": True,  "debt": 15000},
#     {"name": "Bob",     "age": 22, "income": 25000,
#      "credit": 580, "employed": True,  "debt": 5000},
#     {"name": "Charlie", "age": 45, "income": 120000,
#      "credit": 820, "employed": False, "debt": 200000},
#     {"name": "Diana",   "age": 17, "income": 5000,
#      "credit": 0,   "employed": False, "debt": 0},
#     {"name": "Edward",  "age": 35, "income": 80000,
#      "credit": 700, "employed": True,  "debt": 25000},
# ]
#
# Rules for loan approval:
#   age_ok      = age >= 18 AND age <= 75
#   income_ok   = income >= 30000
#   credit_ok   = credit >= 650
#   employed_ok = employed is True
#   debt_ok     = debt < (income * 0.4)   ← debt ratio < 40%
#   basic_ok    = age_ok AND income_ok AND employed_ok
#   credit_waiver = credit >= 800 AND income >= 100000
#   approved    = basic_ok AND (credit_ok OR credit_waiver) AND debt_ok
#
# For each applicant print:
#   ================================
#   Applicant: Alice
#   ================================
#   Age check:      ✓ (30)
#   Income check:   ✓ ($60,000)
#   Credit check:   ✓ (750)
#   Employment:     ✓
#   Debt ratio:     ✓ (25.0%)
#   Credit waiver:  ✗
#   --------------------------------
#   DECISION: APPROVED / REJECTED
#   ================================
#
# At the end print summary:
#   Approved: X/5 applicants

