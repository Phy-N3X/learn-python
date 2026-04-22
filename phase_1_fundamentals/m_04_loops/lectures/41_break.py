# ============================================================
# MODULE 04 | LECTURE 41 - break
# ============================================================
# What you will learn:
# - What break does and why we need it
# - break in while loops
# - break in for loops
# - break with nested loops
# - break vs modifying the condition
# - Common patterns: search, validation, menu
# - break with else clause (preview of Lecture 08)
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is break?
# ------------------------------------------------------------

# Sometimes you're looping through something and you find
# what you were looking for - so you want to STOP immediately.
# Or a certain condition occurs that means "we're done here".
#
# Without break, you'd have to loop through EVERYTHING
# even after finding what you need - wasted time and effort.
#
# break is a statement that IMMEDIATELY exits the loop.
# No more iterations. No condition check.
# Python jumps to the first line AFTER the loop.
#
# Real life analogy:
# ┌─────────────────────────────────────────────────────┐
# │ You're searching through a stack of papers           │
# │ for a specific document.                             │
# │                                                      │
# │ Without break:                                       │
# │ "I found it at paper 3, but I'll still check         │
# │  papers 4, 5, 6... all the way to the bottom."      │
# │                                                      │
# │ With break:                                          │
# │ "Found it at paper 3! Stop searching. Done."         │
# └─────────────────────────────────────────────────────┘
#
# break only exits the INNERMOST loop it's in.
# If nested, the outer loop continues.

# ------------------------------------------------------------
# PART 2: break in a while loop
# ------------------------------------------------------------

# The most common use: exiting a while True loop
# when a specific condition is met inside the body.

# Simplest example:

i = 0
while True:          # would loop forever without break
    print(f"i = {i}")
    i += 1
    if i >= 5:
        break        # exits the while loop immediately

print("After the loop")

# Output:
# i = 0
# i = 1
# i = 2
# i = 3
# i = 4
# After the loop

# Visual flow:
#
# while True:
#   ┌─────────────────────────┐
#   │  body runs              │
#   │  if condition:          │
#   │      break ─────────────┼──→ exits here
#   │  continues if no break  │
#   └─────────────────────────┘
#   ↑ loops back if no break  │
#                             ↓
#                    first line after loop

# Example 2: Finding first even number

numbers = [3, 7, 11, 4, 8, 2, 9]
found = None

i = 0
while i < len(numbers):
    if numbers[i] % 2 == 0:
        found = numbers[i]
        break          # stop as soon as we find it
    i += 1

if found is not None:
    print(f"First even number: {found}")    # 4
else:
    print("No even numbers found")

# Example 3: Keep asking until valid input

while True:
    user_input = input("Enter a positive integer: ").strip()
    if user_input.isdigit() and int(user_input) > 0:
        number = int(user_input)
        break                # valid input → exit loop
    print("Invalid! Please enter a positive integer.")

print(f"You entered: {number}")

# Example 4: Countdown with early exit

count = 10
while count >= 0:
    if count == 5:
        print("Halfway there! Stopping early.")
        break
    print(f"{count}...", end=" ")
    count -= 1

print(f"\nStopped at count = {count}")

# Output:
# 10... 9... 8... 7... 6...
# Halfway there! Stopping early.
# Stopped at count = 5

# ------------------------------------------------------------
# PART 3: break in a for loop
# ------------------------------------------------------------

# break works in for loops too.
# It exits the for loop early, before all items are processed.

# Example 1: Search for an item

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

target = "cherry"
found_at = -1

for i in range(len(fruits)):
    if fruits[i] == target:
        found_at = i
        break    # no need to check the rest!

if found_at != -1:
    print(f"'{target}' found at index {found_at}")
else:
    print(f"'{target}' not found")

# Without break, we'd check "date" and "elderberry" too - pointless!

# Example 2: Find first invalid base in DNA

dna = "ATCGXATCG"
valid_bases = "ATCG"
first_invalid = None
invalid_pos = -1

for i in range(len(dna)):
    if dna[i] not in valid_bases:
        first_invalid = dna[i]
        invalid_pos = i
        break    # found the first invalid - stop

if first_invalid:
    print(f"First invalid base: '{first_invalid}' at position {invalid_pos}")
else:
    print("All bases are valid")

# Output: First invalid base: 'X' at position 4

# Example 3: Process until stop codon

codons = ["ATG", "GCT", "TAC", "GAA", "TAA", "GGG", "CCC"]
protein = []

for codon in codons:
    if codon in ("TAA", "TAG", "TGA"):
        print(f"Stop codon found: {codon} - translation terminated")
        break    # stop translating
    protein.append(codon)

print(f"Protein codons: {protein}")

# Output:
# Stop codon found: TAA - translation terminated
# Protein codons: ['ATG', 'GCT', 'TAC', 'GAA']
# (GGG and CCC are never processed!)

# Example 4: Find first prime number in list

numbers = [8, 15, 22, 13, 6, 31, 7]

for num in numbers:
    # check if num is prime
    is_prime = num > 1
    divisor = 2
    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break    # inner break - exits the while
        divisor += 1

    if is_prime:
        print(f"First prime found: {num}")
        break        # outer break - exits the for

# Output: First prime found: 13

# ------------------------------------------------------------
# PART 4: break vs modifying the condition
# ------------------------------------------------------------

# You can often achieve the same result two ways:
# 1. Using break
# 2. Using a flag variable and modifying the condition
#
# Both work. break is usually cleaner and more direct.

# PROBLEM: Find index of first negative number in list

numbers = [5, 12, 8, -3, 7, -1, 9]

# METHOD 1: Using break (cleaner)

result_idx = -1
for i in range(len(numbers)):
    if numbers[i] < 0:
        result_idx = i
        break

print(f"Method 1 - First negative at index: {result_idx}")    # 3

# METHOD 2: Using a flag variable (more verbose)

result_idx = -1
found = False
i = 0
while i < len(numbers) and not found:
    if numbers[i] < 0:
        result_idx = i
        found = True
    i += 1

print(f"Method 2 - First negative at index: {result_idx}")    # 3

# Both give the same result.
# Method 1 (break) is shorter and more readable.
# Method 2 (flag) is sometimes preferred when you need
# the flag variable later in the code.

# WHEN BREAK IS CLEARLY BETTER:
# - Exiting from inside a complex nested structure
# - When the exit condition is only known mid-iteration
# - When you need to exit immediately (not at end of iteration)

# WHEN FLAG VARIABLE MIGHT BE BETTER:
# - When you need to know IF something was found
#   (though you can check the variable after break too)
# - When the "found" state matters for later logic

# Common pattern combining both:

items = ["cat", "dog", "elephant", "fish"]
search = "elephant"
found_item = None

for item in items:
    if item == search:
        found_item = item
        break

# Check result after loop:
if found_item:
    print(f"Found: {found_item}")
else:
    print("Not found")

# ------------------------------------------------------------
# PART 5: break with nested loops
# ------------------------------------------------------------

# CRITICAL RULE: break only exits the INNERMOST loop.
# The outer loop continues normally!

# Example 1: break exits only inner loop

print("Break in inner loop only:")
for i in range(3):
    print(f"Outer loop: i = {i}")
    for j in range(5):
        if j == 2:
            break        # exits inner for loop only
        print(f"  Inner loop: j = {j}")
    print(f"  Inner loop finished (outer continues)")

# Output:
# Outer loop: i = 0
#   Inner loop: j = 0
#   Inner loop: j = 1
#   Inner loop finished (outer continues)
# Outer loop: i = 1
#   Inner loop: j = 0
#   Inner loop: j = 1
#   Inner loop finished (outer continues)
# Outer loop: i = 2
#   Inner loop: j = 0
#   Inner loop: j = 1
#   Inner loop finished (outer continues)

# Example 2: Searching in a 2D grid

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
target = 5
found_row = -1
found_col = -1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            found_row = i
            found_col = j
            break       # exits inner loop
    if found_row != -1:
        break           # exits outer loop too!

print(f"\nFound {target} at row {found_row}, col {found_col}")
# Found 5 at row 1, col 1

# Example 3: The "found flag" pattern for nested loops
# (classic approach to break out of multiple levels)

grid = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]
target = "F"
found = False

for row_idx in range(len(grid)):
    for col_idx in range(len(grid[row_idx])):
        if grid[row_idx][col_idx] == target:
            found = True
            break              # exits inner loop
    if found:
        break                  # exits outer loop

if found:
    print(f"'{target}' found at ({row_idx}, {col_idx})")
else:
    print(f"'{target}' not found")

# Output: 'F' found at (1, 2)

# Example 4: Processing DNA sequences - stop at first stop codon

sequences = [
    "ATGGCTGAA",
    "ATGTAAATG",     # has STOP in middle
    "GCTATCGGG",
]

print("\nProcessing sequences:")
for seq_idx in range(len(sequences)):
    seq = sequences[seq_idx]
    print(f"\nSequence {seq_idx + 1}: {seq}")
    stopped_early = False

    for i in range(0, len(seq) - 2, 3):
        codon = seq[i:i+3]
        if codon in ("TAA", "TAG", "TGA"):
            print(f"  STOP codon {codon} at position {i}")
            stopped_early = True
            break
        else:
            print(f"  Codon: {codon}")

    if stopped_early:
        print(f"  Translation stopped early")

# ------------------------------------------------------------
# PART 6: while True with break - the do-while pattern
# ------------------------------------------------------------

# "while True" with break is Python's way of doing do-while.
# The body ALWAYS runs at least once.
# break decides when to exit.

# Pattern 1: Validate input - run once, repeat if invalid

while True:
    age_str = input("Enter your age: ")
    if age_str.isdigit():
        age = int(age_str)
        if 0 <= age <= 150:
            break    # valid → exit
    print("Please enter a valid age (0-150)")

print(f"Age accepted: {age}")

# Pattern 2: Menu that runs until quit

options = {"a": "Add", "b": "Browse", "c": "Clear", "q": "Quit"}

while True:
    print("\nMenu:", " | ".join(f"{k}={v}" for k, v in options.items()))
    choice = input("Choose: ").lower().strip()

    if choice not in options:
        print(f"Invalid choice. Options: {', '.join(options.keys())}")
        continue    # we'll learn continue in next lecture

    if choice == "q":
        print("Quitting...")
        break

    print(f"You selected: {options[choice]}")

# Pattern 3: Retry until success

import random

max_retries = 5
retry = 0

while True:
    retry += 1
    success = random.random() > 0.7    # 30% chance of success

    print(f"Attempt {retry}: {'✅ Success!' if success else '❌ Failed'}")

    if success:
        break
    if retry >= max_retries:
        print("Max retries reached - giving up")
        break

# ------------------------------------------------------------
# PART 7: break in search algorithms
# ------------------------------------------------------------

# break is the natural tool for search algorithms.
# Stop when you find what you're looking for.

# Example 1: Linear search with break

def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i    # found - return immediately (like break)
    return -1           # not found

# Example 2: Binary search with break

def binary_search(sorted_data, target):
    left = 0
    right = len(sorted_data) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_data[mid] == target:
            return mid           # found!
        elif sorted_data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1    # not found

data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print(f"\nBinary search for 23: index {binary_search(data, 23)}")    # 5
print(f"Binary search for 10: index {binary_search(data, 10)}")      # -1

# Example 3: Finding first occurrence of pattern in DNA

def find_pattern(sequence, pattern):
    seq_len = len(sequence)
    pat_len = len(pattern)

    for i in range(seq_len - pat_len + 1):
        match = True
        for j in range(pat_len):
            if sequence[i + j] != pattern[j]:
                match = False
                break    # inner break - this position doesn't match
        if match:
            return i     # outer exit - pattern found at i
    return -1

seq = "ATCGATCGATGATCGATCG"
pat = "ATG"
pos = find_pattern(seq, pat)
print(f"\nPattern '{pat}' first found at position: {pos}")    # 8

# Example 4: Finding all occurrences (no early exit)

def find_all_patterns(sequence, pattern):
    positions = []
    pat_len = len(pattern)

    for i in range(len(sequence) - pat_len + 1):
        match = True
        for j in range(pat_len):
            if sequence[i + j] != pattern[j]:
                match = False
                break    # break inner loop only
        if match:
            positions.append(i)
            # NO outer break - we want ALL occurrences

    return positions

positions = find_all_patterns(seq, pat)
print(f"All '{pat}' positions: {positions}")

# ------------------------------------------------------------
# PART 8: break for error handling and validation
# ------------------------------------------------------------

# break is excellent for stopping when an error is detected.

# Example 1: Validate DNA sequence

def validate_dna(sequence):
    valid_bases = "ATCG"
    errors = []

    for i in range(len(sequence)):
        if sequence[i] not in valid_bases:
            errors.append((i, sequence[i]))
            # don't break - we want to find ALL errors

    return errors

sequences = ["ATCGATCG", "ATCXGAT", "AABBCC", "TTTTTTTT"]

print("\nDNA Validation:")
for seq in sequences:
    errors = validate_dna(seq)
    if errors:
        error_details = ", ".join(f"pos {p}: '{c}'" for p, c in errors)
        print(f"  ❌ {seq}: errors at {error_details}")
    else:
        print(f"  ✅ {seq}: valid")

# Example 2: Break on first critical error

def process_data(values):
    results = []
    for i in range(len(values)):
        val = values[i]

        if val is None:
            print(f"  ❌ Critical: None value at index {i} - stopping")
            break          # critical error → stop immediately
        elif val < 0:
            print(f"  ⚠ Warning: negative value {val} at index {i} - skipping")
            continue       # non-critical → skip this one
        else:
            results.append(val * 2)
            print(f"  ✅ Processed index {i}: {val} → {val*2}")

    return results

print("\nData processing:")
test_data = [5, 8, -2, 3, None, 7, 4]
result = process_data(test_data)
print(f"Results: {result}")

# Example 3: Password checker - break on success

print("\nPassword entry system:")
stored_hash = hash("secret123")    # simplified - don't do this in real code
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    password = input(f"Password (attempt {attempt}/{max_attempts}): ")
    if hash(password) == stored_hash:
        print("✅ Access granted!")
        break
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"❌ Wrong password. {remaining} attempt(s) left.")
        else:
            print("❌ Account locked!")

# ------------------------------------------------------------
# PART 9: break with else (preview of Lecture 08)
# ------------------------------------------------------------

# Python has a unique feature: for/while loops can have an else clause.
# The else block runs ONLY if the loop completed WITHOUT break.
# If break was used → else is SKIPPED.
#
# This is very useful for "search and report" patterns.

# Example 1: Search with for/else

targets = [1, 3, 5, 7, 9]
search = 5

for num in targets:
    if num == search:
        print(f"Found {search}!")
        break
else:
    print(f"{search} not found in list")    # only runs if no break

# Output: Found 5!

targets = [1, 3, 5, 7, 9]
search = 4

for num in targets:
    if num == search:
        print(f"Found {search}!")
        break
else:
    print(f"{search} not found in list")    # break didn't happen → else runs

# Output: 4 not found in list

# Example 2: Primality test with else

n = 17
for divisor in range(2, int(n**0.5) + 1):
    if n % divisor == 0:
        print(f"{n} is NOT prime (divisible by {divisor})")
        break
else:
    print(f"{n} IS prime")    # only if no break (no divisor found)

# Output: 17 IS prime

# We'll cover this in detail in Lecture 08.

# ------------------------------------------------------------
# PART 10: Common patterns with break
# ------------------------------------------------------------

# Pattern 1: First match search

def find_first(sequence, predicate):
    """Find first element satisfying predicate."""
    for item in sequence:
        if predicate(item):
            return item    # implicit break via return
    return None

numbers = [4, 8, 15, 16, 23, 42]
first_large = find_first(numbers, lambda x: x > 20)
print(f"\nFirst number > 20: {first_large}")    # 23

# Pattern 2: Scan until condition

def scan_until(sequence, stop_condition):
    """Collect items until stop condition is met."""
    collected = []
    for item in sequence:
        if stop_condition(item):
            break
        collected.append(item)
    return collected

dna_codons = ["ATG", "GCT", "TAC", "TAA", "GGG"]
before_stop = scan_until(dna_codons, lambda c: c in ("TAA", "TAG", "TGA"))
print(f"Codons before stop: {before_stop}")    # ['ATG', 'GCT', 'TAC']

# Pattern 3: Retry with max attempts

def try_operation(max_retries=3):
    for attempt in range(1, max_retries + 1):
        print(f"  Attempt {attempt}...")
        success = random.random() > 0.6    # 40% success rate
        if success:
            print(f"  ✅ Succeeded on attempt {attempt}")
            break
    else:
        print(f"  ❌ Failed after {max_retries} attempts")

print("\nRetry pattern:")
try_operation()

# Pattern 4: Break out of infinite input loop

def get_valid_float(prompt, min_val, max_val):
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            print(f"  Must be between {min_val} and {max_val}")
        except ValueError:
            print("  Invalid number format")

# ph = get_valid_float("Enter pH (0-14): ", 0, 14)
# print(f"pH entered: {ph}")

# Pattern 5: Delimiter-based parsing

text = "name=Anna;age=25;city=Warsaw;END;extra=data"
data = {}

for part in text.split(";"):
    if part == "END":
        break                    # stop at END marker
    if "=" in part:
        key, value = part.split("=", 1)
        data[key] = value

print(f"\nParsed data: {data}")
# {'name': 'Anna', 'age': '25', 'city': 'Warsaw'}

# ------------------------------------------------------------
# PART 11: Real-world use cases
# ------------------------------------------------------------

# Use case 1: Real-time monitoring with threshold

print("\n=== Temperature Monitor ===")
readings = [36.8, 37.1, 37.5, 38.2, 38.9, 39.4, 37.8]
critical_threshold = 39.0
alert_issued = False

print(f"{'Reading':>8} │ {'Temp':>6} │ Status")
print("-" * 35)

for i in range(len(readings)):
    temp = readings[i]

    if temp >= critical_threshold:
        status = "🔴 CRITICAL - ALERT!"
        print(f"{i+1:8d} │ {temp:6.1f} │ {status}")
        alert_issued = True
        break    # stop monitoring, alert raised
    elif temp >= 38.0:
        status = "🟡 Fever"
    elif temp >= 37.5:
        status = "🟠 Elevated"
    else:
        status = "🟢 Normal"

    print(f"{i+1:8d} │ {temp:6.1f} │ {status}")

if alert_issued:
    print(f"\n⚠ CRITICAL ALERT: Temperature {temp}°C exceeds {critical_threshold}°C!")
    print(f"  Monitoring stopped. Take immediate action!")
else:
    print("\n✅ All readings within acceptable range.")

# Use case 2: Sequence assembly - find longest overlap

def find_overlap(seq1, seq2, min_overlap=4):
    """Find length of longest overlap of end of seq1 with start of seq2."""
    max_overlap = min(len(seq1), len(seq2))
    for overlap in range(max_overlap, min_overlap - 1, -1):
        if seq1[-overlap:] == seq2[:overlap]:
            return overlap    # found it - stop
    return 0

reads = ["ATCGATCGTA", "CGATCGTACG", "TCGTACGCTA"]
print("\n=== Sequence Overlap Analysis ===")
for i in range(len(reads)):
    for j in range(len(reads)):
        if i != j:
            overlap = find_overlap(reads[i], reads[j])
            if overlap >= 4:
                print(f"Read {i+1} → Read {j+1}: overlap = {overlap} bp")
                print(f"  {reads[i]}")
                print(f"  {'':>{len(reads[i])-overlap}}{reads[j][:overlap]} ← overlap")

# Use case 3: Menu-driven lab tool

print("\n=== Lab Data Analyzer ===")
data_sets = {
    "absorbance": [0.12, 0.45, 0.78, 0.23, 0.56],
    "concentration": [0.5, 1.5, 2.5, 0.8, 1.8],
    "temperature": [25.0, 37.0, 42.0, 55.0, 70.0],
}

while True:
    print("\nAvailable datasets:", ", ".join(data_sets.keys()))
    print("Commands: analyze <name> | list | quit")
    command = input(">>> ").strip().lower()

    if command == "quit":
        print("Exiting lab tool. Goodbye!")
        break

    elif command == "list":
        for name, values in data_sets.items():
            print(f"  {name}: {len(values)} values")

    elif command.startswith("analyze "):
        dataset_name = command[8:]
        if dataset_name in data_sets:
            values = data_sets[dataset_name]
            total = sum(values)
            mean = total / len(values)
            min_v = values[0]
            max_v = values[0]
            for v in values:
                if v < min_v:
                    min_v = v
                if v > max_v:
                    max_v = v
            print(f"\nAnalysis of '{dataset_name}':")
            print(f"  Count: {len(values)}")
            print(f"  Mean:  {mean:.4f}")
            print(f"  Min:   {min_v:.4f}")
            print(f"  Max:   {max_v:.4f}")
            print(f"  Range: {max_v - min_v:.4f}")
        else:
            print(f"Dataset '{dataset_name}' not found")

    else:
        print(f"Unknown command: '{command}'")

# Use case 4: Iterative algorithm with convergence check

print("\n=== Newton's Method (sqrt calculator) ===")
target = float(input("Find square root of: "))

if target < 0:
    print("Cannot find square root of negative number!")
else:
    x = target / 2.0    # initial guess
    tolerance = 1e-10
    max_iter = 100
    iteration = 0

    print(f"\n{'Iter':>5} │ {'Estimate':>20} │ {'Error':>15}")
    print("-" * 50)

    while iteration < max_iter:
        iteration += 1
        x_new = (x + target / x) / 2.0
        error = abs(x_new - x)

        print(f"{iteration:5d} │ {x_new:20.15f} │ {error:15.2e}")

        if error < tolerance:
            print(f"\n✅ Converged in {iteration} iterations!")
            break
        x = x_new
    else:
        print(f"\n⚠ Did not converge in {max_iter} iterations")

    print(f"Result:    {x_new:.15f}")
    print(f"math.sqrt: {math.sqrt(target):.15f}")

# ------------------------------------------------------------
# PART 12: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: break outside a loop (SyntaxError)

# break    ← SyntaxError! break must be inside a loop

# ✅ break must always be inside a for or while loop

# ❌ MISTAKE 2: Thinking break exits ALL loops (it doesn't!)

found = False
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break    # only exits inner for loop!
    # outer loop continues!
    print(f"Outer loop i={i} continues after inner break")

# Output:
# Outer loop i=0 continues after inner break
# Outer loop i=1 continues after inner break  ← outer DID continue!
# Outer loop i=2 continues after inner break

# ✅ Fix: use a flag variable or restructure
found = False
for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            found = True
            break
    if found:
        break    # now exits outer loop too

# ❌ MISTAKE 3: Unnecessary break (code after break is unreachable)

for i in range(5):
    print(i)
    break        # breaks after first iteration every time!
    print("This never runs")    # unreachable!

# ✅ Fix: only use break inside a condition
for i in range(5):
    if i == 3:
        break
    print(i)

# ❌ MISTAKE 4: Using break when continue is needed

# Want to skip negatives, not stop at first negative:
numbers = [3, -1, 5, -2, 8]

# Wrong: stops at first negative
print("\nWrong (uses break):")
for n in numbers:
    if n < 0:
        break      # stops entirely!
    print(n)

# ✅ Correct: use continue to skip
print("Correct (uses continue):")
for n in numbers:
    if n < 0:
        continue   # skip this one, keep going
    print(n)

# ❌ MISTAKE 5: Relying on loop variable after break
# (the variable keeps its last value - this is actually fine,
#  but beginners sometimes think it resets)

items = ["a", "b", "c", "d"]
for item in items:
    if item == "c":
        break

print(f"\nAfter break, item = '{item}'")    # 'c' - the value when break occurred
# This is correct behavior, not a mistake - just be aware of it!

# ❌ MISTAKE 6: break in an if statement, not the loop
# (break is valid inside if, AS LONG AS the if is inside a loop)

for i in range(5):
    if i == 3:
        break         # ✅ valid - if is inside the loop
    print(i)

# ❌ Confusion: people sometimes think break is inside the if
# Actually, break belongs to the LOOP, not the if.
# The if just controls whether break is reached.

# ❌ MISTAKE 7: Expecting break to skip to next iteration

numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n == 3:
        break         # exits loop entirely, not just skipping 3!
    print(n)

# Output: 1 2  (3, 4, 5 are all skipped, not just 3)
# Use continue (next lecture) to skip just one iteration

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ break exits the INNERMOST loop immediately
# ✅ Works in both for and while loops
# ✅ Execution continues at first line AFTER the loop
# ✅ Only exits ONE level of nesting (innermost)
# ✅ For nested loops: use flag variable to break multiple levels
# ✅ while True + break = do-while pattern
# ✅ for/while + else: else only runs if no break occurred
# ✅ Use break for: search, validation, menus, error detection
# ✅ Don't confuse break (exit loop) with continue (skip iteration)
# ✅ Code after break inside loop body is unreachable

# Quick reference:
# ┌──────────────────────────────────────────────────────────┐
# │ for item in sequence:     while condition:               │
# │     if something:             if something:              │
# │         break    ──────────────────► exits loop          │
# │     more_code    ← skipped after break                  │
# │                                                          │
# │ code_after_loop  ← resumes here                         │
# │                                                          │
# │ Nested: break only exits INNERMOST loop                 │
# │ To exit outer: use flag variable                        │
# │                                                          │
# │ while True:      → runs until break                     │
# │     if done: break                                       │
# │                                                          │
# │ for x in items:  → else only if NO break occurred       │
# │     if found: break                                      │
# │ else: print("not found")                                 │
# └──────────────────────────────────────────────────────────┘