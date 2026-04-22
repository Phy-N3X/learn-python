# ============================================================
# MODULE 04 | LECTURE 40 - while loop
# ============================================================
# What you will learn:
# - What the while loop is and how it differs from for
# - Basic while loop syntax
# - How the condition is evaluated
# - Infinite loops and how to avoid them
# - while vs for - when to use which
# - while with a counter variable
# - while with user input
# - while with sentinel values
# - do-while pattern in Python
# - while with complex conditions
# - Common patterns: countdown, search, validation
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is a while loop?
# ------------------------------------------------------------

# The FOR loop is perfect when you know IN ADVANCE
# how many times to loop (or what to loop over).
#
# But sometimes you DON'T know how many iterations you need.
# You just want to keep looping UNTIL something happens.
#
# Examples where you don't know the count in advance:
# - Keep asking for input until user enters valid data
# - Keep reading data until end of file
# - Keep running until user types "quit"
# - Keep trying until a connection succeeds
# - Keep searching until the target is found
#
# The WHILE loop solves this:
# "Keep doing something AS LONG AS a condition is True"
#
# Real life analogy:
# ┌─────────────────────────────────────────────────────┐
# │ WHILE you are hungry:                               │
# │     eat one more bite                               │
# │                                                     │
# │ WHILE the patient's fever is above 38°C:            │
# │     administer medication every 6 hours             │
# │                                                     │
# │ WHILE the experiment is running:                    │
# │     record measurements every minute               │
# └─────────────────────────────────────────────────────┘
#
# The loop continues as long as the condition stays True.
# When the condition becomes False → loop ends.

# ------------------------------------------------------------
# PART 2: Basic while loop syntax
# ------------------------------------------------------------

# Syntax:
#     while condition:
#         code to repeat
#
# Rules:
# 1. Start with keyword 'while'
# 2. Write a condition (same as in if statements)
# 3. End the line with colon ':'
# 4. Indent the body (4 spaces)
# 5. The condition is checked BEFORE each iteration
# 6. If condition is False from the start → body never runs
# 7. The body must eventually make the condition False!
#    (otherwise: infinite loop)

# Simplest example:

count = 0
while count < 5:
    print(f"count = {count}")
    count += 1    # ← CRITICAL: update the condition variable!

print("Loop finished!")

# Output:
# count = 0
# count = 1
# count = 2
# count = 3
# count = 4
# Loop finished!

# What happens step by step:
# Check: count < 5? → 0 < 5 → True  → run body, count = 1
# Check: count < 5? → 1 < 5 → True  → run body, count = 2
# Check: count < 5? → 2 < 5 → True  → run body, count = 3
# Check: count < 5? → 3 < 5 → True  → run body, count = 4
# Check: count < 5? → 4 < 5 → True  → run body, count = 5
# Check: count < 5? → 5 < 5 → False → EXIT loop
# Continue with code after loop.

# Visual flow diagram:
#
#  ┌─────────────────┐
#  │  check condition │◄──────────┐
#  └────────┬────────┘           │
#           │                    │
#        True/False              │
#           │                    │
#    True ──►  run body ─────────┘
#           │
#    False ─► exit loop
#           │
#           ▼
#    code after loop

# ------------------------------------------------------------
# PART 3: The condition is checked BEFORE the body
# ------------------------------------------------------------

# If the condition is False from the very start,
# the body NEVER executes - not even once.

x = 10
while x < 5:
    print("This will never print!")
    x += 1

print(f"x is still {x}")    # x is still 10

# The loop body was skipped completely.
# Python checked: 10 < 5 → False → jump over entire loop.

# Another example:

items = []    # empty list (falsy)
while items:
    print("Processing item...")
    items.pop()

print("Nothing to process - list was already empty")

# ------------------------------------------------------------
# PART 4: The update step - critical!
# ------------------------------------------------------------

# EVERY while loop must have a way to eventually
# make the condition False.
# Without this → INFINITE LOOP (program never stops)
#
# Three common ways to control the loop:
# 1. Increment/decrement a counter
# 2. Update a variable used in the condition
# 3. Use break to exit (covered in next lecture)

# METHOD 1: Counter

count = 1
while count <= 10:
    print(count, end=" ")
    count += 1    # without this → infinite loop!
print()
# Output: 1 2 3 4 5 6 7 8 9 10

# METHOD 2: Update condition variable directly

number = 256
while number > 1:
    print(number, end=" ")
    number = number // 2    # keep halving
print()
# Output: 256 128 64 32 16 8 4 2

# METHOD 3: Approach a target value

value = 1.0
target = 1000.0
steps = 0
while value < target:
    value *= 2
    steps += 1
print(f"Reached {value} in {steps} steps")
# Reached 1024.0 in 10 steps

# ❌ INFINITE LOOP EXAMPLE (DO NOT RUN):
# count = 0
# while count < 5:
#     print(count)
#     # MISSING: count += 1
#     # count never changes → condition always True → loops forever!

# How to stop an infinite loop if you accidentally run one:
# Press Ctrl+C in the terminal to interrupt.

# ------------------------------------------------------------
# PART 5: while vs for - when to use which
# ------------------------------------------------------------

# Use FOR when:
# ✅ You know the number of iterations in advance
# ✅ You're iterating over a sequence (string, list, range)
# ✅ The iteration has a clear start and end

# Use WHILE when:
# ✅ You don't know how many iterations you'll need
# ✅ You loop until a condition changes
# ✅ You're waiting for user input
# ✅ You're searching for something (stop when found)
# ✅ The loop could run 0 times

# Side by side comparison:

# Same result - two different tools:

# FOR (good when count is known):
print("FOR version:")
for i in range(5):
    print(i, end=" ")
print()

# WHILE (good when condition drives the loop):
print("WHILE version:")
i = 0
while i < 5:
    print(i, end=" ")
    i += 1
print()

# Output is identical: 0 1 2 3 4

# But WHILE is better here (you don't know how many steps):
import math
n = 2
print(f"\nPowers of 2 less than 1000:")
while n < 1000:
    print(n, end=" ")
    n *= 2
print()
# You don't know in advance that there are 9 values!

# FOR is better here (clear sequence):
print("\nMonths 1-12:")
for month in range(1, 13):
    print(month, end=" ")
print()

# ------------------------------------------------------------
# PART 6: while with a counter variable
# ------------------------------------------------------------

# The classic "while as a for loop" pattern.
# Useful when you need more control over the counter.

# Basic counter:
n = 1
while n <= 10:
    print(f"{n:2d} × {n:2d} = {n*n:4d}")
    n += 1

# Counting DOWN:
print("\nCountdown:")
n = 10
while n >= 1:
    print(f"{n}...", end=" ")
    n -= 1
print("LAUNCH! 🚀")

# Counting with different steps:
print("\nEven numbers:")
n = 0
while n <= 20:
    print(n, end=" ")
    n += 2
print()

# Non-uniform steps:
print("\nDoubling:")
n = 1
while n <= 1000:
    print(n, end=" ")
    n *= 2
print()
# Output: 1 2 4 8 16 32 64 128 256 512

# Counter tracking iterations:
attempts = 0
max_attempts = 5
value = 100

print("\nHalving until below 10:")
while value >= 10:
    value = value // 2
    attempts += 1
    print(f"  Attempt {attempts}: value = {value}")

print(f"Finished in {attempts} attempts. Final value: {value}")

# ------------------------------------------------------------
# PART 7: while with user input
# ------------------------------------------------------------

# One of the most important real-world uses.
# Keep asking until valid input is given.

# Example 1: Basic input loop

while True:    # deliberate infinite loop - exits via break
    user_input = input("Enter a positive number: ")
    if user_input.isdigit() and int(user_input) > 0:
        number = int(user_input)
        print(f"You entered: {number}")
        break    # exit the loop
    else:
        print("Invalid! Please enter a positive integer.")

# Example 2: Menu loop

print("\n--- Simple Calculator ---")
running = True
while running:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Quit")
    choice = input("Choose: ")

    if choice == "1":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(f"Result: {a + b}")
    elif choice == "2":
        a = float(input("First number: "))
        b = float(input("Second number: "))
        print(f"Result: {a - b}")
    elif choice == "3":
        print("Goodbye!")
        running = False
    else:
        print("Invalid choice. Try again.")

# Example 3: Input validation with specific rules

while True:
    password = input("Set password (min 8 chars, must contain digit): ")
    has_digit = any(char.isdigit() for char in password)
    if len(password) >= 8 and has_digit:
        print("✅ Password accepted!")
        break
    else:
        if len(password) < 8:
            print("❌ Too short! Minimum 8 characters.")
        if not has_digit:
            print("❌ Must contain at least one digit.")

# Example 4: Guess the number game

import random
secret = random.randint(1, 100)
attempts = 0
max_attempts = 7

print("\n=== Guess the Number (1-100) ===")
while attempts < max_attempts:
    attempts += 1
    remaining = max_attempts - attempts
    guess = int(input(f"Attempt {attempts}/{max_attempts}: "))

    if guess == secret:
        print(f"🎉 Correct! You found it in {attempts} attempts!")
        break
    elif guess < secret:
        print(f"📈 Too low! {remaining} attempts left.")
    else:
        print(f"📉 Too high! {remaining} attempts left.")
else:
    print(f"❌ Out of attempts! The number was {secret}.")

# ------------------------------------------------------------
# PART 8: Sentinel values
# ------------------------------------------------------------

# A sentinel value is a special value that signals "stop".
# It's not real data - it's a signal to end the loop.
# Common sentinels: -1, 0, "", "quit", "done", None

# Example 1: Sum numbers until user enters -1

print("\nEnter numbers to sum. Enter -1 to stop.")
total = 0
count = 0

while True:
    value = int(input("Number (-1 to stop): "))
    if value == -1:    # sentinel value
        break
    total += value
    count += 1

if count > 0:
    print(f"Sum: {total}")
    print(f"Count: {count}")
    print(f"Average: {total/count:.2f}")
else:
    print("No numbers entered.")

# Example 2: Process strings until empty input

print("\nEnter DNA bases one at a time.")
print("Press Enter with no input to stop.")
sequence = ""

while True:
    base = input("Enter base (A/T/C/G or Enter to stop): ").upper()
    if base == "":    # empty string = sentinel
        break
    if base in "ATCG":
        sequence += base
        print(f"  Current sequence: {sequence}")
    else:
        print(f"  Invalid base: '{base}' - skipped")

print(f"\nFinal sequence: {sequence}")
print(f"Length: {len(sequence)}")

# Example 3: Process until "quit"

print("\nCommand interpreter (type 'quit' to exit):")
history = []

while True:
    command = input(">>> ").strip().lower()
    if command in ("quit", "exit", "q"):
        print("Goodbye!")
        break
    elif command == "history":
        for i, cmd in enumerate(history):
            print(f"  {i+1}: {cmd}")
    elif command == "help":
        print("Commands: history, help, quit")
    elif command == "":
        continue    # skip empty input, ask again
    else:
        history.append(command)
        print(f"Executed: {command}")

# ------------------------------------------------------------
# PART 9: do-while pattern in Python
# ------------------------------------------------------------

# Many languages (C, Java, JavaScript) have a do-while loop:
# do {
#     body
# } while (condition);
#
# This ALWAYS runs the body AT LEAST ONCE,
# then checks the condition.
#
# Python doesn't have do-while, but you can simulate it:

# Pattern 1: while True with break at end (most common)

while True:
    # body always runs at least once
    user_input = input("Enter your name: ")
    if user_input.strip():    # valid name
        break
    print("Name cannot be empty!")

print(f"Welcome, {user_input}!")

# Pattern 2: Execute once, then check

attempts = 0
while True:
    attempts += 1
    result = attempts * 7
    print(f"Attempt {attempts}: result = {result}")
    if result >= 50:    # condition checked AFTER body runs
        break

print(f"Stopped after {attempts} iterations")

# Pattern 3: Using a flag variable

is_first = True
number = 0
while is_first or number != 42:
    is_first = False
    number = int(input("Guess (42 to win): "))
    if number != 42:
        print("Not 42! Try again.")

print("You found it!")

# ------------------------------------------------------------
# PART 10: while with complex conditions
# ------------------------------------------------------------

# The condition can be as complex as any if condition.
# Use and, or, not, comparisons, function calls, etc.

# Example 1: Multiple conditions with AND

temperature = 37.5
time_elapsed = 0
max_time = 24

print("Monitoring patient temperature:")
while temperature > 37.2 and time_elapsed < max_time:
    print(f"  Hour {time_elapsed:2d}: {temperature:.1f}°C - "
          f"{'⚠ Fever' if temperature >= 38.0 else 'Elevated'}")
    temperature -= 0.3
    time_elapsed += 1

if temperature <= 37.2:
    print(f"✅ Temperature normalized after {time_elapsed} hours")
else:
    print(f"❌ Temperature still elevated after {max_time} hours!")

# Example 2: OR condition

connection_ok = False
data_ok = False
retry = 0

while not connection_ok or not data_ok:
    retry += 1
    print(f"Attempt {retry}...")
    if retry >= 2:
        connection_ok = True
    if retry >= 3:
        data_ok = True
    if retry > 10:
        print("Too many retries - giving up")
        break

if connection_ok and data_ok:
    print("✅ System ready!")

# Example 3: Condition uses function result

def check_convergence(values, tolerance=0.001):
    if len(values) < 2:
        return False
    return abs(values[-1] - values[-2]) < tolerance

# Iterative averaging (finds square root approximately)
values = [2.0]    # starting estimate for sqrt(2)
target = 2        # we want sqrt(2)

while not check_convergence(values):
    x = values[-1]
    next_x = (x + target / x) / 2
    values.append(next_x)

print(f"\nNewton's method for √{target}:")
for i, v in enumerate(values):
    print(f"  Step {i}: {v:.10f}")
print(f"  math.sqrt({target}) = {math.sqrt(target):.10f}")

# Example 4: String-based condition

sequence = ""
valid_bases = "ATCG"

while not sequence.endswith("TAA") and len(sequence) < 30:
    base = valid_bases[len(sequence) % 4]
    sequence += base

print(f"\nGenerated sequence: {sequence}")
print(f"Ended with stop codon: {sequence.endswith('TAA')}")

# ------------------------------------------------------------
# PART 11: while for searching and scanning
# ------------------------------------------------------------

# while loops are excellent for searching algorithms.

# Example 1: Linear search

def find_element(data, target):
    i = 0
    while i < len(data) and data[i] != target:
        i += 1
    if i < len(data):
        return i    # found at index i
    return -1       # not found

numbers = [15, 42, 8, 73, 31, 56, 19, 84]
idx = find_element(numbers, 56)
print(f"\nSearching for 56 in {numbers}")
print(f"Found at index: {idx}")    # 5

# Example 2: Binary search

def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    iterations = 0

    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        print(f"  Iteration {iterations}: checking index {mid} = {sorted_list[mid]}")

        if sorted_list[mid] == target:
            return mid, iterations
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, iterations

sorted_nums = [2, 7, 13, 18, 25, 36, 42, 58, 74, 91]
print(f"\nBinary search for 42 in {sorted_nums}:")
idx, iters = binary_search(sorted_nums, 42)
print(f"Found at index {idx} in {iters} iterations")

# Example 3: Find first matching element

amino_acids = ["Ala", "Gly", "Met", "Phe", "Met", "Lys"]
target_aa = "Met"
i = 0

while i < len(amino_acids) and amino_acids[i] != target_aa:
    i += 1

if i < len(amino_acids):
    print(f"\nFirst '{target_aa}' found at position {i}")
else:
    print(f"\n'{target_aa}' not found")

# Example 4: Collatz sequence

print("\nCollatz sequence starting at 27:")
n = 27
steps = 0
max_val = n

while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    steps += 1
    if n > max_val:
        max_val = n
    print(f"  Step {steps:3d}: {n:6d}")

print(f"Reached 1 in {steps} steps. Peak value: {max_val}")

# ------------------------------------------------------------
# PART 12: while loop with accumulator
# ------------------------------------------------------------

# Same accumulator pattern as with for loops.
# Useful when the number of iterations is unknown.

# Example 1: Sum until threshold

print("\nSum numbers until total exceeds 100:")
total = 0
n = 1
numbers_used = []

while total <= 100:
    total += n
    numbers_used.append(n)
    n += 1

print(f"Numbers: {numbers_used}")
print(f"Total: {total}")
print(f"Count: {len(numbers_used)}")

# Example 2: Build string until condition

print("\nBuilding sequence until GC content > 60%:")
dna = ""
bases = "ATCG"
i = 0

while True:
    dna += bases[i % 4]
    gc = (dna.count("G") + dna.count("C")) / len(dna)
    i += 1
    if gc > 0.6 or len(dna) >= 20:
        break

print(f"Sequence: {dna}")
print(f"GC content: {gc:.1%}")
print(f"Length: {len(dna)}")

# Example 3: Compound interest until goal

principal = 1000.0
rate = 0.08     # 8% annual interest
goal = 2000.0
year = 0

print("\nCompound interest growth:")
print(f"{'Year':>6} │ {'Balance':>12}")
print("-" * 22)

while principal < goal:
    year += 1
    principal *= (1 + rate)
    print(f"{year:6d} │ {principal:12.2f} PLN")

print(f"\nGoal of {goal:.2f} PLN reached in {year} years!")

# ------------------------------------------------------------
# PART 13: Nested while loops
# ------------------------------------------------------------

# while loops can be nested, just like for loops.

# Example 1: Simple nested while

i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"({i},{j})", end=" ")
        j += 1
    print()
    i += 1

# Output:
# (1,1) (1,2) (1,3)
# (2,1) (2,2) (2,3)
# (3,1) (3,2) (3,3)

# Example 2: Mixed - while outer, for inner

print("\nTest matrix:")
row = 1
while row <= 4:
    for col in range(1, 5):
        print(f"{row * col:4d}", end="")
    print()
    row += 1

# Example 3: Two-level validation

print("\nTwo-level input:")
outer_done = False
while not outer_done:
    name = input("Enter your name (min 3 chars): ").strip()
    if len(name) < 3:
        print("Name too short!")
        continue

    age_valid = False
    while not age_valid:
        age_str = input(f"Enter {name}'s age: ")
        if age_str.isdigit() and 0 < int(age_str) < 150:
            age = int(age_str)
            age_valid = True
        else:
            print("Invalid age! Enter a number between 1 and 149.")

    print(f"✅ Registered: {name}, age {age}")
    outer_done = True

# ------------------------------------------------------------
# PART 14: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Forgetting to update the condition variable
# (leads to infinite loop)

# count = 0
# while count < 5:
#     print(count)
#     # MISSING: count += 1   ← infinite loop!

# ✅ Fix: always update the variable that controls the condition
count = 0
while count < 5:
    print(count, end=" ")
    count += 1    # ← must be here!
print()

# ❌ MISTAKE 2: Condition never becomes False

# x = 5
# while x > 0:
#     x += 1     ← x grows! condition never False → infinite!

# ✅ Fix: make sure updates move toward False condition
x = 5
while x > 0:
    x -= 1     # ← decreasing toward 0
print(f"x = {x}")    # 0

# ❌ MISTAKE 3: Wrong condition direction

# countdown = 0
# while countdown > 10:    ← 0 > 10 is False from start!
#     print(countdown)
#     countdown += 1

# ✅ Fix: check logic - should it be < or >?
countdown = 0
while countdown < 10:
    print(countdown, end=" ")
    countdown += 1
print()

# ❌ MISTAKE 4: Update is inside an if block (sometimes missed)

n = 0
while n < 5:
    if n % 2 == 0:
        print(f"{n} is even")
    n += 1    # ← must be at while level, NOT inside if!
    # If n+=1 were inside 'if', odd values would loop forever!

# ❌ MISTAKE 5: Off-by-one in condition

# Want to print 1 to 10:
n = 1
while n < 10:    # ← wrong! stops at 9
    print(n, end=" ")
    n += 1
print()    # 1 2 3 4 5 6 7 8 9  ← missing 10!

# ✅ Fix:
n = 1
while n <= 10:   # ← correct: includes 10
    print(n, end=" ")
    n += 1
print()    # 1 2 3 4 5 6 7 8 9 10

# ❌ MISTAKE 6: Infinite loop with float comparison

# Due to floating point precision, this might loop forever:
# x = 0.0
# while x != 1.0:    ← might never be exactly 1.0!
#     x += 0.1

# ✅ Fix: use >= or round comparison
x = 0.0
while x < 1.0 - 0.0001:    # tolerance approach
    x += 0.1
print(f"\nx ≈ {x:.1f}")    # 1.0

# ❌ MISTAKE 7: Forgetting colon

# while count < 5      ← SyntaxError! Missing colon
#     print(count)
#     count += 1

# ✅ Fix:
count = 0
while count < 5:    # colon required
    count += 1

# ❌ MISTAKE 8: Using while when for is clearly better

# Unnecessarily complex while loop:
i = 0
my_list = [10, 20, 30, 40, 50]
while i < len(my_list):
    print(my_list[i])
    i += 1

# ✅ Cleaner with for:
for item in my_list:
    print(item)

# ------------------------------------------------------------
# PART 15: Real-world use cases
# ------------------------------------------------------------

# Use case 1: ATM simulation

print("\n=== ATM MACHINE ===")
balance = 1500.00
pin = "1234"
max_attempts = 3
attempt = 0
authenticated = False

while attempt < max_attempts and not authenticated:
    attempt += 1
    entered_pin = input(f"Enter PIN (attempt {attempt}/{max_attempts}): ")
    if entered_pin == pin:
        authenticated = True
    else:
        remaining = max_attempts - attempt
        if remaining > 0:
            print(f"❌ Wrong PIN. {remaining} attempt(s) remaining.")
        else:
            print("❌ Card blocked! Too many wrong attempts.")

if authenticated:
    print(f"✅ Welcome! Balance: {balance:.2f} PLN")
    while True:
        print("\n1. Withdraw  2. Deposit  3. Balance  4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            amount = float(input("Amount: "))
            if amount <= balance:
                balance -= amount
                print(f"✅ Dispensed {amount:.2f} PLN. Balance: {balance:.2f} PLN")
            else:
                print("❌ Insufficient funds!")
        elif choice == "2":
            amount = float(input("Amount: "))
            balance += amount
            print(f"✅ Deposited {amount:.2f} PLN. Balance: {balance:.2f} PLN")
        elif choice == "3":
            print(f"Current balance: {balance:.2f} PLN")
        elif choice == "4":
            print("Thank you. Goodbye!")
            break
        else:
            print("Invalid choice.")

# Use case 2: PCR cycle simulator

print("\n=== PCR Cycle Simulator ===")
initial_copies = 1
target_copies = 1000000
cycle = 0

copies = initial_copies
print(f"Initial DNA copies: {copies}")

while copies < target_copies:
    cycle += 1
    copies *= 2    # each cycle doubles the DNA
    efficiency = min(100, cycle * 10)
    print(f"Cycle {cycle:2d}: {copies:>10,} copies "
          f"({'✅' if copies >= target_copies else '⏳'})")

print(f"\n🎯 Target of {target_copies:,} copies reached in {cycle} cycles!")
print(f"   Theoretical: {initial_copies} × 2^{cycle} = {copies:,}")

# Use case 3: Iterative numerical method (Newton's method for sqrt)

def find_sqrt(n, tolerance=1e-10):
    if n < 0:
        return None
    if n == 0:
        return 0.0

    x = n / 2.0    # initial guess
    iterations = 0

    while True:
        iterations += 1
        x_new = (x + n / x) / 2.0
        if abs(x_new - x) < tolerance:
            break
        x = x_new

    return x_new, iterations

print("\n=== Square Root Finder ===")
for num in [2, 9, 144, 2.5, 0.01]:
    result, iters = find_sqrt(num)
    print(f"√{num:6.2f} = {result:.10f} (found in {iters} iterations)")

# use case 4: Data validation pipeline

print("\n=== Student Data Entry ===")
students = []
max_students = 3

while len(students) < max_students:
    print(f"\nEntering student {len(students)+1}/{max_students}:")

    while True:
        name = input("  Name: ").strip()
        if len(name) >= 2:
            break
        print("  ❌ Name must be at least 2 characters")

    while True:
        age_str = input("  Age: ")
        if age_str.isdigit() and 16 <= int(age_str) <= 100:
            age = int(age_str)
            break
        print("  ❌ Age must be between 16 and 100")

    while True:
        gpa_str = input("  GPA (0.0-4.0): ")
        try:
            gpa = float(gpa_str)
            if 0.0 <= gpa <= 4.0:
                break
            print("  ❌ GPA must be between 0.0 and 4.0")
        except ValueError:
            print("  ❌ Invalid number format")

    students.append({"name": name, "age": age, "gpa": gpa})
    print(f"  ✅ Student {name} added!")

print("\n=== Registered Students ===")
for i, student in enumerate(students):
    status = "Honor Roll" if student["gpa"] >= 3.5 else "Regular"
    print(f"{i+1}. {student['name']:20} | "
          f"Age: {student['age']:3d} | "
          f"GPA: {student['gpa']:.2f} | "
          f"{status}")

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ while condition:      → runs as long as condition is True
# ✅ Check BEFORE body    → may run 0 times if False from start
# ✅ MUST update condition → or risk infinite loop
# ✅ Use for known count  → for loop is cleaner
# ✅ Use while for unknown count → until something happens
# ✅ Sentinel values      → special value to signal "stop"
# ✅ do-while pattern     → while True: ... if done: break
# ✅ Complex conditions   → and, or, not all work
# ✅ Ctrl+C to stop       → emergency exit from infinite loop
# ✅ while True + break   → when exit condition is inside body

# Quick reference:
# ┌──────────────────────────────────────────────────────────┐
# │ while condition:        → basic syntax                   │
# │     body                                                 │
# │     update!             ← must change condition          │
# │                                                          │
# │ while True:             → infinite loop (use with break) │
# │     body                                                 │
# │     if exit_condition:                                   │
# │         break                                            │
# │                                                          │
# │ Common patterns:                                         │
# │   Counter:  n = 0; while n < limit: n += 1              │
# │   Input:    while True: x = input(); if valid: break     │
# │   Search:   while i < n and not found: i += 1           │
# │   Sentinel: while value != -1: value = int(input())      │
# └──────────────────────────────────────────────────────────┘