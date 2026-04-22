# ============================================================
# MODULE 04 | LECTURE 44 - else in loops
# ============================================================
# What you will learn:
# - What the else clause in loops does
# - How else works with for loops
# - How else works with while loops
# - The critical rule: else runs ONLY if no break occurred
# - Why this feature exists and when it's useful
# - Common patterns: search, validation, prime checking
# - else in loops vs else in if statements (different!)
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is else in a loop?
# ------------------------------------------------------------

# You already know else in if statements:
# "if condition is True → do this, ELSE → do that"
#
# else in LOOPS is completely different.
# It does NOT mean "if the loop didn't run".
# It does NOT mean "if the condition was False".
#
# The rule is precise and unique:
# ┌─────────────────────────────────────────────────────────┐
# │ The else block runs when the loop COMPLETES NORMALLY    │
# │ (without being interrupted by break).                   │
# │                                                         │
# │ If break was hit → else is SKIPPED.                     │
# │ If loop finishes all iterations → else RUNS.            │
# └─────────────────────────────────────────────────────────┘
#
# Think of it as:
# "for each item... else if we didn't break"
# "while condition... else if condition became False naturally"
#
# Real life analogy:
# ┌─────────────────────────────────────────────────────────┐
# │ You search all drawers for your keys.                   │
# │                                                         │
# │ FOR each drawer:                                        │
# │     IF keys found → take them and STOP SEARCHING        │
# │ ELSE (searched everything without finding):             │
# │     "Keys not found anywhere - call locksmith"          │
# └─────────────────────────────────────────────────────────┘
#
# The else handles the "didn't find it" case elegantly.

# ------------------------------------------------------------
# PART 2: else with for loops - basic syntax
# ------------------------------------------------------------

# Syntax:
#     for variable in iterable:
#         body
#         if condition:
#             break
#     else:
#         runs only if loop completed without break

# Simplest example:

print("Example 1 - no break:")
for i in range(5):
    print(f"  i = {i}")
else:
    print("  else: loop completed normally (no break)")

# Output:
#   i = 0
#   i = 1
#   i = 2
#   i = 3
#   i = 4
#   else: loop completed normally (no break)

print("\nExample 2 - with break:")
for i in range(5):
    if i == 3:
        print(f"  Breaking at i = {i}")
        break
    print(f"  i = {i}")
else:
    print("  else: this will NOT print because break was used")

# Output:
#   i = 0
#   i = 1
#   i = 2
#   Breaking at i = 3
# (else block is skipped!)

print("\nExample 3 - empty sequence:")
for i in []:    # empty sequence
    print(f"  i = {i}")
else:
    print("  else: runs even for empty sequence!")

# Output:
#   else: runs even for empty sequence!
# Important: else runs even if the loop body never executed!

# Visual flow:
#
# for item in sequence:
#   ┌────────────────────────────────────┐
#   │  body                              │
#   │  if found: break ──────────────────┼──→ SKIP else
#   └────────────────────────────────────┘
#   ↑ repeat for each item
#   │
#   (all items processed, no break)
#   ↓
#   else block ──────────────────────────→ RUNS
#   ↓
#   continue after loop

# ------------------------------------------------------------
# PART 3: else with while loops
# ------------------------------------------------------------

# The same rule applies to while loops:
# else runs if the loop ended because the condition became False
# else is SKIPPED if break was used

# Syntax:
#     while condition:
#         body
#         if something:
#             break
#     else:
#         runs only if condition became False naturally (no break)

print("\nwhile else - no break:")
n = 0
while n < 5:
    print(f"  n = {n}")
    n += 1
else:
    print("  else: while condition became False (no break)")

# Output:
#   n = 0
#   n = 1
#   n = 2
#   n = 3
#   n = 4
#   else: while condition became False (no break)

print("\nwhile else - with break:")
n = 0
while n < 5:
    if n == 3:
        print(f"  Breaking at n = {n}")
        break
    print(f"  n = {n}")
    n += 1
else:
    print("  else: this will NOT print because break was used")

# Output:
#   n = 0
#   n = 1
#   n = 2
#   Breaking at n = 3
# (else block is skipped!)

print("\nwhile else - condition False from start:")
n = 10
while n < 5:    # False from the very beginning
    print(f"  n = {n}")
else:
    print("  else: runs even if while body never executed!")

# Output:
#   else: runs even if while body never executed!
# (just like for with empty sequence)

# ------------------------------------------------------------
# PART 4: The key use case - search patterns
# ------------------------------------------------------------

# The most COMMON and NATURAL use of loop else:
# Search for something, report "not found" if the search
# completes without finding it.
#
# WITHOUT else (the old way - using a flag variable):

numbers = [3, 7, 11, 14, 21, 33]
target = 14
found = False    # flag variable

for num in numbers:
    if num == target:
        found = True
        break

if found:
    print(f"\nFound {target}!")
else:
    print(f"\n{target} not found!")

# WITH else (the elegant Python way):

for num in numbers:
    if num == target:
        print(f"\nFound {target}!")
        break
else:
    print(f"\n{target} not found!")

# Both produce the same result, but the else version:
# - Eliminates the flag variable
# - Makes the intent clearer
# - Is more Pythonic

# More examples:

# Example 1: Search in a list

fruits = ["apple", "banana", "cherry", "date"]
search = "mango"

for fruit in fruits:
    if fruit == search:
        print(f"\n'{search}' found in fruits!")
        break
else:
    print(f"\n'{search}' not in our fruit list.")

# Output: 'mango' not in our fruit list.

# Example 2: Find first match with reporting

amino_acids = ["Ala", "Gly", "Met", "Phe", "Trp", "Lys"]
target_aa = "Met"

for i in range(len(amino_acids)):
    if amino_acids[i] == target_aa:
        print(f"\n'{target_aa}' found at position {i}")
        break
else:
    print(f"\n'{target_aa}' not found in sequence")

# Output: 'Met' found at position 2

# Example 3: Multiple search targets

dna = "ATCGATCGATCG"
targets = ["ATG", "TAA", "GGG"]

print("\nSearching for codons:")
for codon in targets:
    found_pos = -1
    for i in range(0, len(dna) - 2, 3):
        if dna[i:i+3] == codon:
            found_pos = i
            break
    else:
        print(f"  '{codon}': not found")
        continue    # continue to next codon
    print(f"  '{codon}': found at position {found_pos}")

# ------------------------------------------------------------
# PART 5: Prime number checker - classic example
# ------------------------------------------------------------

# The for/else combination is PERFECT for primality testing.
# This is the most cited example of loop else in Python.

def is_prime(n):
    """Check if n is prime using for/else."""
    if n < 2:
        return False
    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            return False    # not prime - divisor found
    else:
        return True         # no divisor found = prime!

# How it works:
# - Loop through all possible divisors (2 to √n)
# - If any divisor divides n evenly → not prime → return False
# - If loop completes without finding a divisor → prime → else runs

# Test it:
for n in range(2, 20):
    if is_prime(n):
        print(f"{n:3d} is prime ✅")
    else:
        print(f"{n:3d} is not prime")

# Alternative version showing the logic explicitly:

def is_prime_explicit(n):
    if n < 2:
        return False

    for divisor in range(2, int(n**0.5) + 1):
        if n % divisor == 0:
            print(f"    {n} is divisible by {divisor} - not prime")
            break
    else:
        print(f"    {n} has no divisors - it IS prime")
        return True

    return False

print("\nPrimality check with explanation:")
for n in [7, 9, 13, 15]:
    result = is_prime_explicit(n)

# ------------------------------------------------------------
# PART 6: Validation patterns with loop else
# ------------------------------------------------------------

# else is perfect for validation: check all items,
# report success if all pass, or failure on first failure.

# Example 1: Validate all items in a sequence

def validate_dna_sequence(sequence):
    """Check if sequence contains only valid DNA bases."""
    valid_bases = "ATCG"

    for i in range(len(sequence)):
        if sequence[i] not in valid_bases:
            print(f"  ❌ Invalid base '{sequence[i]}' at position {i}")
            break
    else:
        print(f"  ✅ Sequence is valid: {sequence}")
        return True

    return False

print("\nDNA Validation:")
test_sequences = ["ATCGATCG", "ATCXGATCG", "GCGCGCGC", "ATG1TCG"]
for seq in test_sequences:
    validate_dna_sequence(seq)

# Example 2: Check if all conditions are met

def check_experiment_ready(conditions):
    """Check if all experimental conditions are met."""
    print("\nChecking experimental conditions:")

    for condition, (value, min_val, max_val) in conditions.items():
        if not (min_val <= value <= max_val):
            print(f"  ❌ {condition}: {value} not in [{min_val}, {max_val}]")
            break
        print(f"  ✅ {condition}: {value} (OK)")
    else:
        print("  🎉 All conditions met - experiment can proceed!")
        return True

    print("  ⛔ Experiment cannot proceed!")
    return False

conditions = {
    "Temperature (°C)": (37.2, 36.5, 38.0),
    "pH": (7.1, 6.8, 7.4),
    "Humidity (%)": (45, 40, 60),
    "CO2 (%)": (5.2, 4.5, 6.0),
}

check_experiment_ready(conditions)

# Now with a failing condition:
bad_conditions = {
    "Temperature (°C)": (37.2, 36.5, 38.0),
    "pH": (9.5, 6.8, 7.4),    # pH too high!
    "Humidity (%)": (45, 40, 60),
}

check_experiment_ready(bad_conditions)

# Example 3: Password validation with else

def validate_password(password):
    """Validate password meets all requirements."""
    requirements = [
        (len(password) >= 8, "at least 8 characters"),
        (any(c.isupper() for c in password), "at least one uppercase"),
        (any(c.islower() for c in password), "at least one lowercase"),
        (any(c.isdigit() for c in password), "at least one digit"),
        (any(c in "!@#$%^&*()" for c in password), "at least one special char"),
        (" " not in password, "no spaces"),
    ]

    for check, description in requirements:
        if not check:
            print(f"  ❌ Failed: {description}")
            break
    else:
        print("  ✅ Password meets all requirements!")
        return True

    return False

print("\nPassword Validation:")
passwords = ["short", "LongButNoDigit!", "ValidPass123!", "has space 1A!"]
for pwd in passwords:
    print(f"\nChecking '{pwd}':")
    validate_password(pwd)

# ------------------------------------------------------------
# PART 7: else with while - practical patterns
# ------------------------------------------------------------

# Example 1: Binary search with else

def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            print(f"  Found {target} at index {mid}")
            break
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    else:
        print(f"  {target} not found in list")
        return -1

    return mid

print("\nBinary search:")
data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(f"List: {data}")
binary_search(data, 23)     # Found 23 at index 5
binary_search(data, 10)     # 10 not found in list

# Example 2: Retry with success/failure

import random
random.seed(42)

def attempt_connection(host, max_retries=5):
    attempt = 0
    while attempt < max_retries:
        attempt += 1
        # Simulate connection attempt (30% success rate)
        success = random.random() > 0.7
        print(f"  Attempt {attempt}/{max_retries}: "
              f"{'✅ Connected!' if success else '❌ Failed'}")
        if success:
            break
        # brief simulated delay
    else:
        print(f"  ⛔ Could not connect after {max_retries} attempts")
        return False

    print(f"  Connection established on attempt {attempt}")
    return True

print("\nConnection attempts:")
attempt_connection("lab-server-01")

# Example 3: User input with max attempts

def get_valid_input(prompt, valid_range, max_attempts=3):
    min_val, max_val = valid_range
    attempts = 0

    while attempts < max_attempts:
        attempts += 1
        try:
            value = float(input(f"{prompt} (attempt {attempts}/{max_attempts}): "))
            if min_val <= value <= max_val:
                break
            print(f"  Value must be between {min_val} and {max_val}")
        except ValueError:
            print("  Please enter a valid number")
    else:
        print(f"  Max attempts reached - using default value")
        return (min_val + max_val) / 2    # default = midpoint

    return value

# ph = get_valid_input("Enter pH", (0, 14))
# print(f"pH accepted: {ph}")

# ------------------------------------------------------------
# PART 8: else with break in nested loops
# ------------------------------------------------------------

# Remember: else belongs to the LOOP that DIRECTLY contains it.
# break in an inner loop doesn't affect else of the outer loop.

# Example 1: Searching in a 2D structure

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5

print("\n2D search with nested loops:")
found_row = -1
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            found_row = i
            break    # breaks inner loop
    if found_row != -1:
        break        # breaks outer loop
else:
    print(f"  {target} not found in matrix")

if found_row != -1:
    print(f"  Found {target} at ({found_row}, {j})")

# Note: the outer else only runs if the outer break never executed

# Example 2: Complex nested search with else on inner loop

sequences = ["ATCG", "GCTA", "TTATG", "CGCGCG"]
pattern = "ATG"

print("\nSearching for ATG in multiple sequences:")
for seq_idx in range(len(sequences)):
    seq = sequences[seq_idx]
    for i in range(len(seq) - len(pattern) + 1):
        if seq[i:i+len(pattern)] == pattern:
            print(f"  Seq {seq_idx+1} '{seq}': '{pattern}' found at pos {i}")
            break
    else:
        print(f"  Seq {seq_idx+1} '{seq}': '{pattern}' NOT found")

# Output:
#   Seq 1 'ATCG': 'ATG' NOT found
#   Seq 2 'GCTA': 'ATG' NOT found
#   Seq 3 'TTATG': 'ATG' found at pos 2
#   Seq 4 'CGCGCG': 'ATG' NOT found

# ------------------------------------------------------------
# PART 9: else vs flag variable - comparison
# ------------------------------------------------------------

# Two ways to solve the same problem.
# Both work. Understand both, prefer the Pythonic one.

items = [3, 7, 11, 14, 19, 22]
target = 14

print("\nApproach comparison for finding 14:")

# APPROACH 1: Flag variable (universal, works in all languages)
found = False
for item in items:
    if item == target:
        found = True
        break
if found:
    print(f"  Flag: Found {target}!")
else:
    print(f"  Flag: {target} not found")

# APPROACH 2: Loop else (Pythonic, Python-specific)
for item in items:
    if item == target:
        print(f"  Else:  Found {target}!")
        break
else:
    print(f"  Else:  {target} not found")

# APPROACH 3: Combining both (when you need the flag later too)
found = False
for item in items:
    if item == target:
        found = True
        break
else:
    found = False
# 'found' variable available for later use

print(f"  Both:  found = {found}")

# Which to use?
# - else: cleaner, more Pythonic, ideal for search patterns
# - flag: more explicit, universal (works in any language)
# - Use else when the search IS the whole purpose of the loop
# - Use flag when you need the found/not-found state elsewhere

# ------------------------------------------------------------
# PART 10: else in loops vs else in if - they're DIFFERENT!
# ------------------------------------------------------------

# This is a major source of confusion for beginners.
# The word "else" means different things in different contexts.

# ELSE IN IF - runs when the if condition is False:
x = 3
if x > 5:
    print("x is large")
else:
    print("x is not large")    # runs because x > 5 is False

# ELSE IN FOR - runs when the loop completes without break:
for i in [1, 2, 3]:
    pass    # no break here
else:
    print("for else: loop completed")    # runs (no break)

# ELSE IN WHILE - runs when condition becomes False naturally:
n = 3
while n > 0:
    n -= 1
else:
    print("while else: condition became False")    # runs (no break)

# The KEY difference:
# if/else: depends on a BOOLEAN CONDITION
# loop/else: depends on WHETHER break WAS USED

# Common confusion:
numbers = [1, 2, 3, 4, 5]

# WRONG interpretation: "else runs if the loop didn't execute"
for num in []:    # empty list - loop body never runs
    print(num)
else:
    print("This runs! Even though loop body never executed!")

# The else has NOTHING to do with whether the body ran.
# It ONLY cares about: did break happen? No? → run else.

# Summary table:
# ┌──────────────────┬────────────────────────────────────┐
# │ if x > 5: ...    │ else runs when x > 5 is FALSE      │
# │ else: ...        │                                    │
# ├──────────────────┼────────────────────────────────────┤
# │ for x in items:  │ else runs when NO break occurred   │
# │ else: ...        │ (regardless of loop body execution)│
# ├──────────────────┼────────────────────────────────────┤
# │ while cond:      │ else runs when cond becomes FALSE  │
# │ else: ...        │ naturally (not when break is used) │
# └──────────────────┴────────────────────────────────────┘

# ------------------------------------------------------------
# PART 11: continue does NOT affect else
# ------------------------------------------------------------

# Important: ONLY break affects the else clause.
# continue does NOT skip the else.
# The loop still "completes" from else's perspective.

print("\ncontinue does NOT skip else:")
for i in range(5):
    if i % 2 == 0:
        continue    # skip even numbers
    print(f"  Processing {i}")
else:
    print("  else: still runs! (continue doesn't affect else)")

# Output:
#   Processing 1
#   Processing 3
#   Processing 5 (wait - range goes 0-4, so 1,3)
#   else: still runs!

# Only break prevents else from running:
print("\nbreak DOES skip else:")
for i in range(5):
    if i == 3:
        break
    print(f"  Processing {i}")
else:
    print("  else: will NOT print (break was used)")

# Output:
#   Processing 0
#   Processing 1
#   Processing 2
# (else skipped!)

# ------------------------------------------------------------
# PART 12: Real-world use cases
# ------------------------------------------------------------

# Use case 1: Sequence feature finder

print("\n=== DNA Feature Finder ===")

def find_restriction_site(sequence, enzyme, cut_site):
    """Find if a restriction enzyme cut site exists in sequence."""
    seq_upper = sequence.upper()

    for i in range(len(seq_upper) - len(cut_site) + 1):
        if seq_upper[i:i+len(cut_site)] == cut_site:
            print(f"  {enzyme}: cut site '{cut_site}' found at position {i}")
            break
    else:
        print(f"  {enzyme}: cut site '{cut_site}' NOT found")
        return False

    return True

dna = "ATCGAATTCGATCGGGATCCATCG"
print(f"Sequence: {dna}")
print("Restriction enzyme analysis:")
find_restriction_site(dna, "EcoRI", "GAATTC")    # G|AATTC
find_restriction_site(dna, "BamHI", "GGATCC")    # G|GATCC
find_restriction_site(dna, "HindIII", "AAGCTT")  # A|AGCTT

# Use case 2: Authentication system

print("\n=== Authentication System ===")

user_database = {
    "admin": {"password": "admin123", "active": True, "role": "admin"},
    "anna": {"password": "anna456", "active": True, "role": "user"},
    "bob": {"password": "bob789", "active": False, "role": "user"},
}

def authenticate(username, password):
    checks = [
        (username in user_database, "Username not found"),
        (username in user_database and
         user_database[username]["password"] == password,
         "Wrong password"),
        (username in user_database and
         user_database[username]["active"],
         "Account is deactivated"),
    ]

    for check, error_msg in checks:
        if not check:
            print(f"  ❌ Auth failed: {error_msg}")
            break
    else:
        role = user_database[username]["role"]
        print(f"  ✅ Login successful! Role: {role}")
        return True

    return False

print("Authentication attempts:")
authenticate("anna", "anna456")     # success
authenticate("bob", "bob789")       # account deactivated
authenticate("anna", "wrongpass")   # wrong password
authenticate("charlie", "pass")     # user not found

# Use case 3: Data completeness checker

print("\n=== Data Completeness Checker ===")

required_fields = ["sample_id", "collection_date", "sample_type",
                   "concentration", "volume"]

samples = [
    {"sample_id": "S001", "collection_date": "2024-01-15",
     "sample_type": "blood", "concentration": 2.5, "volume": 5.0},
    {"sample_id": "S002", "collection_date": "2024-01-16",
     "sample_type": "urine", "concentration": None, "volume": 10.0},
    {"sample_id": "S003", "collection_date": "2024-01-17",
     "sample_type": "tissue", "concentration": 1.8},  # missing volume!
]

print("Checking sample completeness:")
complete_samples = []
incomplete_samples = []

for sample in samples:
    sample_id = sample.get("sample_id", "UNKNOWN")
    for field in required_fields:
        if field not in sample:
            print(f"  {sample_id}: ❌ Missing field: '{field}'")
            incomplete_samples.append(sample_id)
            break
        if sample[field] is None:
            print(f"  {sample_id}: ❌ Field '{field}' is None/empty")
            incomplete_samples.append(sample_id)
            break
    else:
        print(f"  {sample_id}: ✅ Complete")
        complete_samples.append(sample_id)

print(f"\nComplete: {complete_samples}")
print(f"Incomplete: {incomplete_samples}")

# Use case 4: Protocol validator

print("\n=== Protocol Validator ===")

def validate_pcr_protocol(protocol):
    """Validate a PCR protocol has all required steps in correct order."""
    required_steps = ["denaturation", "annealing", "extension"]
    protocol_lower = [step.lower() for step in protocol]

    print(f"Protocol: {protocol}")

    # Check for required steps
    for step in required_steps:
        for i in range(len(protocol_lower)):
            if step in protocol_lower[i]:
                print(f"  ✅ Found '{step}' at step {i+1}")
                break
        else:
            print(f"  ❌ Missing required step: '{step}'")
            break
    else:
        print("  ✅ Protocol is complete!")
        return True

    print("  ❌ Protocol validation FAILED")
    return False

protocols = [
    ["Initial Denaturation 95°C", "Denaturation 95°C",
     "Annealing 55°C", "Extension 72°C", "Final Extension 72°C"],
    ["Denaturation 95°C", "Extension 72°C"],  # missing annealing!
]

for proto in protocols:
    print()
    validate_pcr_protocol(proto)

# Use case 5: Convergence detector

print("\n=== Iterative Algorithm Convergence ===")

def find_fixed_point(f, x0, tolerance=1e-6, max_iter=100):
    """Find fixed point of function f (where f(x) = x)."""
    x = x0
    print(f"Starting at x = {x0}")

    for i in range(max_iter):
        x_new = f(x)
        error = abs(x_new - x)

        if error < tolerance:
            print(f"  Converged at iteration {i+1}: x = {x_new:.10f}")
            break

        x = x_new
    else:
        print(f"  ⚠ Did NOT converge after {max_iter} iterations")
        print(f"  Last value: {x_new:.10f}")
        return None

    return x_new

import math
# cos(x) = x has a fixed point near x = 0.739...
result = find_fixed_point(math.cos, 0.5)
if result:
    print(f"  Verification: cos({result:.6f}) = {math.cos(result):.6f}")

# ------------------------------------------------------------
# PART 13: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Thinking else means "loop didn't run"

# Wrong mental model:
for i in []:    # empty list - loop never runs
    pass
else:
    print("Else DOES run for empty loop!")  # this prints!

# Correct mental model: else runs when NO break occurred.

# ❌ MISTAKE 2: Thinking continue prevents else

for i in range(5):
    if i % 2 == 0:
        continue    # skip even numbers
    print(i, end=" ")
else:
    print("\nelse still runs!")  # this runs despite continues!

# ❌ MISTAKE 3: Using else when a flag is clearer

# Overly clever - hard to understand:
target = 7
for x in range(10):
    if x * x > target:
        print(f"First x where x² > {target}: {x}")
        break
else:
    print("No x found")    # When would this happen? Never for range(10)

# Cleaner with explicit logic:
result = next((x for x in range(10) if x * x > target), None)
if result is not None:
    print(f"First x where x² > {target}: {result}")

# ❌ MISTAKE 4: Forgetting break prevents else

numbers = [1, 3, 5, 7]
target = 5

for n in numbers:
    if n == target:
        break    # this PREVENTS else from running!
else:
    print("Not found")    # WON'T print if target is in list

# ✅ Correct usage:
for n in numbers:
    if n == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found")    # only runs if break didn't happen

# ❌ MISTAKE 5: Confusing loop else with if else

x = 5
# if else: based on condition being True/False:
if x > 3:
    print("big")
else:
    print("small")    # runs when x > 3 is False

# loop else: based on break usage:
for i in range(3):
    if i == 5:         # never true
        break
else:
    print("no break")  # runs because break never happened
    # NOT because "i never equaled 5"!

# ❌ MISTAKE 6: Return/raise in loop body - does it affect else?

def find_value(items, target):
    for item in items:
        if item == target:
            return item    # return exits function, not just loop
    else:
        return None    # runs if no return (no break equivalent occurred

# ⚠ Note: return in a loop is like break for else purposes
# Actually NO - return exits the FUNCTION entirely,
# bypassing the else block too!

# ❌ MISTAKE 7: Expecting else to catch exceptions

# Loop else does NOT catch exceptions.
# Use try/except for exception handling.

# ❌ MISTAKE 8: Nesting confusion

for i in range(3):
    for j in range(3):
        if j == 1:
            break    # inner break
    else:
        print(f"Inner else: i={i}")    # this DOES run!
        # Because inner break only affects inner loop/else
        # The inner loop breaks, but WHAT breaks it?
        # j==1 breaks it every time, so inner else NEVER runs!

# Wait - let me re-examine:
print("\nNested loop else demonstration:")
for i in range(3):
    print(f"Outer i={i}")
    for j in range(3):
        if j == 1:
            break    # always breaks inner loop
        print(f"  Inner j={j}")
    else:
        print(f"  Inner else (should NOT print because break always hits)")

# Output: inner else never runs because inner loop always breaks!

# Now without the inner break:
for i in range(3):
    print(f"Outer i={i}")
    for j in range(3):
        print(f"  Inner j={j}")
    else:
        print(f"  Inner else (DOES print - no inner break)")

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Loop else runs when loop completes WITHOUT break
# ✅ Loop else is SKIPPED when break is executed
# ✅ Loop else DOES run for empty sequences (no break possible)
# ✅ continue does NOT affect else (loop still "completes")
# ✅ Works with both for and while loops
# ✅ In nested loops: else belongs to its IMMEDIATE loop
# ✅ Loop else ≠ if else (completely different meaning!)
# ✅ Primary use case: search patterns (found/not found)
# ✅ Alternative to flag variables for search loops
# ✅ Classic example: primality testing

# Quick reference:
# ┌──────────────────────────────────────────────────────────┐
# │ for/while loop:                                          │
# │     body                                                 │
# │     if found: break   ─→ break hit → else SKIPPED       │
# │ else:                                                    │
# │     "not found" code  ─→ no break → else RUNS           │
# │                                                          │
# │ continue → does NOT prevent else                        │
# │ break    → DOES prevent else                            │
# │ empty sequence → else STILL RUNS                        │
# │                                                          │
# │ Typical use:                                             │
# │ for item in collection:                                  │
# │     if item == target:                                   │
# │         print("found!")                                  │
# │         break                                            │
# │ else:                                                    │
# │     print("not found")                                   │
# └──────────────────────────────────────────────────────────┘