# ============================================================
# MODULE 04 | LECTURE 38 - range()
# ============================================================
# What you will learn:
# - What range() is and why it exists
# - range() with one argument: range(stop)
# - range() with two arguments: range(start, stop)
# - range() with three arguments: range(start, stop, step)
# - Negative step - counting backwards
# - range() is NOT a list - it's a lazy sequence
# - Converting range to list
# - Common patterns with range()
# - Mathematical sequences using range()
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is range() and why do we need it?
# ------------------------------------------------------------

# In the previous lecture, we learned that for loops
# iterate over sequences like strings, lists, and tuples.
# But what if we want to repeat something a specific number
# of times, or generate a sequence of numbers?
#
# We COULD create a list manually:
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# But that's tedious for large ranges.
# What about [0, 1, 2, ..., 999999]? Not practical to type!
#
# range() solves this elegantly.
# It generates a sequence of integers on demand,
# without storing them all in memory at once.
#
# Real life analogy:
# ┌─────────────────────────────────────────────────────┐
# │ Without range:                                      │
# │ pages = [1, 2, 3, 4, 5, ..., 300]  ← type it all  │
# │                                                     │
# │ With range:                                         │
# │ pages = range(1, 301)  ← just describe the range   │
# └─────────────────────────────────────────────────────┘
#
# range() takes up to 3 arguments:
# range(stop)
# range(start, stop)
# range(start, stop, step)
#
# All arguments must be INTEGERS.
# The stop value is NEVER included (exclusive).

# ------------------------------------------------------------
# PART 2: range(stop) - one argument
# ------------------------------------------------------------

# The simplest form: range(stop)
# Generates numbers from 0 up to (but NOT including) stop
# Always starts at 0.

# Syntax:
#     range(stop)
#
# Generates: 0, 1, 2, ..., stop-1

# Let's see what's inside:
print(list(range(5)))     # [0, 1, 2, 3, 4]
print(list(range(10)))    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(1)))     # [0]
print(list(range(0)))     # []  ← empty! nothing before 0

# The stop value is NOT included:
# range(5) → 0, 1, 2, 3, 4  (NOT 5!)
# Think of it as: "give me 5 numbers starting from 0"

# Common use: repeat something N times
for i in range(5):
    print(f"Iteration: {i}")

# Output:
# Iteration: 0
# Iteration: 1
# Iteration: 2
# Iteration: 3
# Iteration: 4

# When you don't need the index value:
for _ in range(5):
    print("Hello!")

# Output:
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!

# Practical example: print a separator line
for _ in range(3):
    print("=" * 40)

# Output:
# ========================================
# ========================================
# ========================================

# Using the index value:
for i in range(8):
    print(f"Student {i + 1}: enrolled")    # i+1 to start from 1

# Output:
# Student 1: enrolled
# Student 2: enrolled
# ... (up to Student 8)

# ------------------------------------------------------------
# PART 3: range(start, stop) - two arguments
# ------------------------------------------------------------

# When you want to start from a number other than 0.
#
# Syntax:
#     range(start, stop)
#
# Generates: start, start+1, start+2, ..., stop-1
# start IS included, stop is NOT included

print(list(range(1, 6)))      # [1, 2, 3, 4, 5]
print(list(range(5, 10)))     # [5, 6, 7, 8, 9]
print(list(range(0, 5)))      # [0, 1, 2, 3, 4]  same as range(5)
print(list(range(10, 20)))    # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(list(range(1, 2)))      # [1]
print(list(range(5, 5)))      # []  ← empty! start == stop
print(list(range(5, 3)))      # []  ← empty! start > stop (need step=-1)

# Visual diagram:
#
# range(1, 6):
# ┌───┬───┬───┬───┬───┐
# │ 1 │ 2 │ 3 │ 4 │ 5 │   ← 6 not included!
# └───┴───┴───┴───┴───┘
#   ↑                 ↑
# start             stop-1

# Practical example: months of the year

for month in range(1, 13):
    print(f"Month {month:2d}")

# Output: Month 1, Month 2, ..., Month 12

# Page numbers in a book:
total_pages = 350
for page in range(1, total_pages + 1):
    pass    # process each page (simplified)
print(f"Processed {total_pages} pages")

# Countdown from 10 to 1 (NOT YET - need step for that):
# Instead: range with start and stop for positive sequences
for i in range(1, 11):
    print(f"{i:2d}: {'█' * i}")

# Output (visual bar chart):
#  1: █
#  2: ██
#  3: ███
# ...
# 10: ██████████

# Checking even numbers in range:
even_sum = 0
for n in range(2, 101):    # 2 to 100 inclusive
    if n % 2 == 0:
        even_sum += n
print(f"Sum of even numbers 2-100: {even_sum}")    # 2550

# ASCII characters:
print("Uppercase letters:")
for code in range(65, 91):    # ASCII 65=A, 90=Z
    print(chr(code), end=" ")
print()    # new line

# Output: A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

print("Lowercase letters:")
for code in range(97, 123):    # ASCII 97=a, 122=z
    print(chr(code), end=" ")
print()

# Output: a b c d e f g h i j k l m n o p q r s t u v w x y z

# ------------------------------------------------------------
# PART 4: range(start, stop, step) - three arguments
# ------------------------------------------------------------

# The most powerful form.
# Step controls how much to add each time.
#
# Syntax:
#     range(start, stop, step)
#
# Generates: start, start+step, start+2*step, ...
# Stops BEFORE reaching stop
# step can be positive or negative (not zero!)

# Positive step:

print(list(range(0, 10, 2)))      # [0, 2, 4, 6, 8]       ← evens
print(list(range(1, 10, 2)))      # [1, 3, 5, 7, 9]       ← odds
print(list(range(0, 30, 5)))      # [0, 5, 10, 15, 20, 25]
print(list(range(0, 100, 10)))    # [0, 10, 20, ..., 90]
print(list(range(1, 20, 3)))      # [1, 4, 7, 10, 13, 16, 19]

# How step works:
# range(0, 10, 2):
# Start: 0 → 0 is < 10 → include
# Next:  0 + 2 = 2 → 2 is < 10 → include
# Next:  2 + 2 = 4 → 4 is < 10 → include
# Next:  4 + 2 = 6 → 6 is < 10 → include
# Next:  6 + 2 = 8 → 8 is < 10 → include
# Next:  8 + 2 = 10 → 10 is NOT < 10 → STOP
# Result: [0, 2, 4, 6, 8]

# Examples with positive step:

# Print every other letter:
for i in range(0, len("ATCGATCG"), 2):
    print("ATCGATCG"[i], end="")
print()    # ACAC

# Multiples of 7:
print("Multiples of 7 up to 100:")
for n in range(7, 101, 7):
    print(n, end=" ")
print()

# Output: 7 14 21 28 35 42 49 56 63 70 77 84 91 98

# DNA codons from a sequence (groups of 3):
dna = "ATGCGATACGCTTAA"
print("\nCodons:")
for i in range(0, len(dna), 3):
    codon = dna[i:i+3]
    print(f"  Position {i:2d}: {codon}")

# Output:
#   Position  0: ATG
#   Position  3: CGA
#   Position  6: TAC
#   Position  9: GCT
#   Position 12: TAA

# Every 5th number from 0 to 50:
for n in range(0, 51, 5):
    print(f"{n:3d}", end=" ")
print()

# Output:   0   5  10  15  20  25  30  35  40  45  50

# ------------------------------------------------------------
# PART 5: Negative step - counting backwards
# ------------------------------------------------------------

# When step is negative, the range counts DOWN.
# start must be GREATER than stop for non-empty range.
#
# range(start, stop, -n):
# start must be > stop
# stops BEFORE reaching stop (stop is still exclusive!)

print(list(range(10, 0, -1)))     # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list(range(5, -1, -1)))     # [5, 4, 3, 2, 1, 0]
print(list(range(10, 0, -2)))     # [10, 8, 6, 4, 2]
print(list(range(100, 0, -10)))   # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]
print(list(range(0, 10, -1)))     # []  ← empty! start < stop with negative step

# Visual diagram for range(5, 0, -1):
#
# ┌───┬───┬───┬───┬───┐
# │ 5 │ 4 │ 3 │ 2 │ 1 │   ← 0 not included!
# └───┴───┴───┴───┴───┘
#   ↑                 ↑
# start             stop+1 (last included)

# Countdown:
print("Countdown:")
for i in range(10, 0, -1):
    print(f"{i}...", end=" ")
print("LAUNCH! 🚀")

# Output: 10... 9... 8... 7... 6... 5... 4... 3... 2... 1... LAUNCH! 🚀

# Reverse through a list:
amino_acids = ["Met", "Ala", "Gly", "Phe", "Lys"]
print("\nReversed sequence:")
for i in range(len(amino_acids) - 1, -1, -1):
    print(amino_acids[i], end=" ")
print()

# Output: Lys Phe Gly Ala Met

# Decreasing indentation:
for i in range(5, 0, -1):
    print(" " * (5 - i) + "★" * i)

# Output:
# ★★★★★
#  ★★★★
#   ★★★
#    ★★
#     ★

# Reverse a string using range:
word = "Python"
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print(f"'{word}' reversed: '{reversed_word}'")    # 'nohtyP'

# Countdown with condition:
print("\nOdd numbers from 19 to 1:")
for n in range(19, 0, -2):
    print(n, end=" ")
print()
# Output: 19 17 15 13 11 9 7 5 3 1

# ------------------------------------------------------------
# PART 6: range() is NOT a list - lazy evaluation
# ------------------------------------------------------------

# range() does NOT create all numbers in memory at once.
# It's a "lazy" object that generates numbers on demand.
# This makes it extremely memory-efficient.

# Compare:
# [0, 1, 2, ..., 999999] → stores 1 million integers in RAM
# range(1000000)          → stores only start, stop, step (3 numbers!)

import sys

list_size = sys.getsizeof(list(range(1000)))
range_size = sys.getsizeof(range(1000))

print(f"Size of list(range(1000)): {list_size} bytes")
print(f"Size of range(1000):       {range_size} bytes")

# Output (approximate):
# Size of list(range(1000)): 8056 bytes
# Size of range(1000):       48 bytes

# range is a completely different type:
r = range(5)
print(type(r))           # <class 'range'>
print(r)                 # range(0, 5)   ← NOT [0,1,2,3,4]!

# You can convert range to a list when needed:
print(list(r))           # [0, 1, 2, 3, 4]
print(tuple(r))          # (0, 1, 2, 3, 4)

# But for loops work directly on range - no conversion needed:
for i in range(5):       # ✅ efficient - no conversion
    print(i)

# range supports some list-like operations:
r = range(0, 20, 2)
print(len(r))            # 10
print(r[0])              # 0   ← indexing works!
print(r[4])              # 8
print(r[-1])             # 18  ← negative indexing works!
print(8 in r)            # True
print(7 in r)            # False

# range supports slicing:
print(list(r[2:5]))      # [4, 6, 8]

# ------------------------------------------------------------
# PART 7: Mathematical sequences with range()
# ------------------------------------------------------------

# range() makes mathematical sequences elegant.

# Example 1: Sum of first N natural numbers

n = 100
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of 1 to {n}: {total}")    # 5050
# Verify: n*(n+1)/2 = 100*101/2 = 5050 ✅

# Example 2: Factorial

n = 10
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")    # 10! = 3628800

# Example 3: Powers of 2

print("Powers of 2:")
for exp in range(0, 11):
    print(f"2^{exp:2d} = {2**exp:6d}")

# Output:
# 2^ 0 =      1
# 2^ 1 =      2
# 2^ 2 =      4
# ...
# 2^10 =   1024

# Example 4: Fibonacci sequence (first N numbers)

n = 10
a, b = 0, 1
print(f"First {n} Fibonacci numbers:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()
# Output: 0 1 1 2 3 5 8 13 21 34

# Example 5: Multiples and divisors

number = 36
print(f"\nDivisors of {number}:")
for i in range(1, number + 1):
    if number % i == 0:
        print(f"  {i} × {number // i} = {number}")

# Output:
#   1 × 36 = 36
#   2 × 18 = 36
#   3 × 12 = 36
#   4 × 9 = 36
#   6 × 6 = 36
#   9 × 4 = 36
#   12 × 3 = 36
#   18 × 2 = 36
#   36 × 1 = 36

# Example 6: Prime number check

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("\nPrime numbers up to 50:")
for n in range(2, 51):
    if is_prime(n):
        print(n, end=" ")
print()
# Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47

# Example 7: Sum of odd numbers

total_odd = 0
for n in range(1, 101, 2):    # step=2, all odd numbers
    total_odd += n
print(f"\nSum of odd numbers 1-99: {total_odd}")    # 2500

# Example 8: Triangle numbers

print("\nFirst 10 triangle numbers:")
for n in range(1, 11):
    triangle = n * (n + 1) // 2
    print(f"T({n}) = {triangle}")

# Output: T(1)=1, T(2)=3, T(3)=6, T(4)=10, ...

# ------------------------------------------------------------
# PART 8: Using range() with len()
# ------------------------------------------------------------

# A very common pattern: range(len(something))
# Gives you indices 0, 1, 2, ..., len-1
# Lets you access items by index

# This is useful when you need the index AND the value,
# or when you need to look at nearby elements.

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Print with index:
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
# 3: date
# 4: elderberry

# Modify based on index:
dna = "ATCGATCG"
for i in range(0, len(dna), 3):    # every 3rd position
    print(f"Codon at {i}: {dna[i:i+3]}")

# Look at two adjacent items at once:
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
print("\nAdjacent pairs:")
for i in range(len(numbers) - 1):    # stop one before the end
    print(f"  {numbers[i]}, {numbers[i+1]}")

# Output:
#   3, 1
#   1, 4
#   4, 1
# ...

# Check if a list is sorted:
is_sorted = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
print(f"\nList {numbers}")
print(f"Is sorted: {is_sorted}")    # False

# ------------------------------------------------------------
# PART 9: Nested range() patterns
# ------------------------------------------------------------

# range() works great in nested loops (which we'll cover in Lecture 09)
# Here's a preview of common patterns.

# Multiplication table:
print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i*j:3d}", end="")
    print()

# Output:
#   1  2  3
#   2  4  6
#   3  6  9

# Triangle pattern:
print("\nTriangle:")
for row in range(1, 6):
    for col in range(row):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
# ****
# *****

# Number pyramid:
print("\nPyramid:")
size = 5
for row in range(1, size + 1):
    spaces = " " * (size - row)
    stars = "* " * row
    print(spaces + stars)

# Output:
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

# ------------------------------------------------------------
# PART 10: range() with float steps (workaround)
# ------------------------------------------------------------

# ⚠ range() only works with INTEGERS.
# You CANNOT use float steps directly.

# ❌ This causes TypeError:
# for x in range(0, 1, 0.1):
#     print(x)
# TypeError: 'float' object cannot be interpreted as an integer

# ✅ Workaround 1: use integers and divide

print("pH values from 0 to 14 in steps of 0.5:")
for i in range(0, 29):    # 0 to 28 → divide by 2 → 0.0 to 14.0
    ph = i / 2
    print(f"{ph:.1f}", end=" ")
print()

# ✅ Workaround 2: multiply step and divide result

print("\nTemperatures 36.0 to 40.0 in steps of 0.1:")
for i in range(360, 401):    # 360 to 400 → divide by 10 → 36.0 to 40.0
    temp = i / 10
    print(f"{temp:.1f}°C", end=" ")
print()

# ✅ Workaround 3: calculate step count

start = 0.0
stop = 1.0
step = 0.25
steps = int((stop - start) / step) + 1
for i in range(steps):
    value = start + i * step
    print(f"{value:.2f}", end=" ")
print()
# Output: 0.00 0.25 0.50 0.75 1.00

# ✅ Workaround 4: use numpy (if available) - advanced
# import numpy as np
# for x in np.arange(0, 1, 0.1):
#     print(f"{x:.1f}", end=" ")

# ------------------------------------------------------------
# PART 11: Common range() patterns cheat sheet
# ------------------------------------------------------------

# ┌───────────────────────────────────────────────────────────┐
# │ range(n)          → 0, 1, 2, ..., n-1                    │
# │ range(1, n+1)     → 1, 2, 3, ..., n    (1-indexed)       │
# │ range(a, b)       → a, a+1, ..., b-1                     │
# │ range(a, b, 2)    → a, a+2, a+4, ...   (every other)     │
# │ range(n, 0, -1)   → n, n-1, ..., 1     (countdown)       │
# │ range(n-1, -1,-1) → n-1, n-2, ..., 0  (reverse index)   │
# │ range(0,n,2)      → 0, 2, 4, ..        (even indices)    │
# │ range(1,n,2)      → 1, 3, 5, ..        (odd indices)     │
# │ range(len(x))     → 0, 1, ..., len(x)-1 (all indices)   │
# └───────────────────────────────────────────────────────────┘

# Pattern: 1 to N inclusive
n = 10
for i in range(1, n + 1):
    print(i, end=" ")
print()    # 1 2 3 4 5 6 7 8 9 10

# Pattern: N to 1 countdown
for i in range(n, 0, -1):
    print(i, end=" ")
print()    # 10 9 8 7 6 5 4 3 2 1

# Pattern: even numbers up to N
for i in range(0, n + 1, 2):
    print(i, end=" ")
print()    # 0 2 4 6 8 10

# Pattern: odd numbers up to N
for i in range(1, n + 1, 2):
    print(i, end=" ")
print()    # 1 3 5 7 9

# Pattern: every 3rd index
my_list = list(range(20))
for i in range(0, len(my_list), 3):
    print(my_list[i], end=" ")
print()    # 0 3 6 9 12 15 18

# ------------------------------------------------------------
# PART 12: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Forgetting stop is exclusive

# Common error: range(1, 10) does NOT include 10!
print(list(range(1, 10)))    # [1, 2, 3, 4, 5, 6, 7, 8, 9]  ← no 10!

# ✅ Fix: use stop + 1 to include the last number
print(list(range(1, 11)))    # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ✅

# ❌ MISTAKE 2: Using float arguments

# range(0, 1.0)       ← TypeError! must be integer
# range(0, 10, 0.5)   ← TypeError! must be integer

# ✅ Fix: use only integers
print(list(range(0, 10, 2)))    # [0, 2, 4, 6, 8]

# ❌ MISTAKE 3: Step of zero

# range(0, 10, 0)    ← ValueError! step cannot be zero

# ✅ Fix: use non-zero step
print(list(range(0, 10, 1)))    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# ❌ MISTAKE 4: Wrong direction (empty range)

# Positive step but start > stop → empty:
print(list(range(10, 0, 1)))     # []  ← want countdown but step is +1

# ✅ Fix: use negative step for countdown:
print(list(range(10, 0, -1)))    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# ❌ MISTAKE 5: Printing range directly

r = range(5)
print(r)         # range(0, 5)  ← NOT [0, 1, 2, 3, 4]!

# ✅ Fix: convert to list if you want to see all values:
print(list(r))   # [0, 1, 2, 3, 4]

# ❌ MISTAKE 6: Thinking range starts at 1 by default

for i in range(5):
    print(i, end=" ")
print()    # 0 1 2 3 4  ← starts at 0!

# ✅ Fix: use range(1, 6) to start at 1:
for i in range(1, 6):
    print(i, end=" ")
print()    # 1 2 3 4 5

# ❌ MISTAKE 7: Using range with len() off-by-one

word = "Python"
# Wrong - goes one too far:
# for i in range(len(word) + 1):
#     print(word[i])    ← IndexError at i=6!

# ✅ Fix: range(len(word)) goes 0 to 5:
for i in range(len(word)):
    print(word[i], end="")
print()    # Python

# ❌ MISTAKE 8: Modifying range (it's immutable!)

r = range(5)
# r[0] = 10    ← TypeError! range doesn't support item assignment

# ✅ Convert to list first if modification needed:
lst = list(range(5))
lst[0] = 10
print(lst)    # [10, 1, 2, 3, 4]

# ❌ MISTAKE 9: Using range() with string arguments

# range("a", "z")    ← TypeError! strings not allowed

# ✅ For letter ranges, use ord() and chr():
for code in range(ord("a"), ord("z") + 1):
    print(chr(code), end=" ")
print()    # a b c d ... z

# ------------------------------------------------------------
# PART 13: Real-world use cases
# ------------------------------------------------------------

# Use case 1: Generate a series of student IDs

prefix = "STU"
start_id = 1001
count = 10

print("Generated Student IDs:")
for i in range(count):
    student_id = f"{prefix}{start_id + i:04d}"
    print(f"  {student_id}")

# Output:
# STU1001
# STU1002
# ...
# STU1010

# Use case 2: Create a temperature conversion table

print("\nCelsius to Fahrenheit Conversion Table")
print("=" * 35)
print(f"{'°C':>6} │ {'°F':>8} │ {'Description':}")
print("-" * 35)

for celsius in range(-20, 51, 5):
    fahrenheit = (celsius * 9 / 5) + 32
    if celsius < 0:
        desc = "Freezing ❄"
    elif celsius < 15:
        desc = "Cold 🧥"
    elif celsius < 25:
        desc = "Comfortable 😊"
    elif celsius < 35:
        desc = "Warm ☀"
    else:
        desc = "Hot 🌡"
    print(f"{celsius:6d} │ {fahrenheit:8.1f} │ {desc}")

# Use case 3: Codon position analysis

dna = "ATGCGATACGCTTAAGGCCCCTAA"
print(f"\nCodon Analysis of: {dna}")
print("=" * 40)

for i in range(0, len(dna) - 2, 3):
    codon = dna[i:i+3]
    pos = i + 1    # 1-indexed position

    match codon:
        case "ATG":
            annotation = "START / Met"
        case "TAA" | "TAG" | "TGA":
            annotation = "STOP"
        case _:
            annotation = "Coding"

    print(f"Position {pos:2d}-{pos+2:2d}: {codon} → {annotation}")

# Use case 4: Number pattern checker in range

print("\nNumber properties in range 1-30:")
print(f"{'N':>4} │ {'Even':>6} │ {'Odd':>5} │ {'3x':>5} │ {'5x':>5} │ {'Prime':>7}")
print("-" * 45)

for n in range(1, 31):
    is_even = "✅" if n % 2 == 0 else "  "
    is_odd = "✅" if n % 2 != 0 else "  "
    mult_3 = "✅" if n % 3 == 0 else "  "
    mult_5 = "✅" if n % 5 == 0 else "  "
    prime = "✅" if is_prime(n) else "  "
    print(f"{n:4d} │ {is_even:>6} │ {is_odd:>5} │ {mult_3:>5} │ {mult_5:>5} │ {prime:>7}")

# Use case 5: Simulated progress bar

import time    # for sleep (optional - comment out if not needed)

total_steps = 20
print("\nProcessing samples:")

for step in range(total_steps + 1):
    filled = int(step / total_steps * 30)
    empty = 30 - filled
    bar = "█" * filled + "░" * empty
    percent = step / total_steps * 100
    print(f"\r[{bar}] {percent:5.1f}% ({step}/{total_steps})", end="")
    # time.sleep(0.1)    # uncomment to see animation

print("\nDone! ✅")

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ range(stop)            → 0, 1, ..., stop-1
# ✅ range(start, stop)     → start, start+1, ..., stop-1
# ✅ range(start, stop, step) → start, start+step, ..., < stop
# ✅ stop is ALWAYS exclusive (never included)
# ✅ step can be positive or negative (never zero)
# ✅ Negative step → countdown (start must be > stop)
# ✅ range() is NOT a list → memory efficient (lazy)
# ✅ list(range(n)) → converts to list
# ✅ len(), indexing, slicing, 'in' work on range objects
# ✅ Only works with integers (not floats)
# ✅ Use range(len(x)) to get indices of a sequence

# Quick reference:
# ┌──────────────────────────────────────────────────────────┐
# │ range(5)          → [0, 1, 2, 3, 4]                     │
# │ range(1, 6)       → [1, 2, 3, 4, 5]                     │
# │ range(0, 10, 2)   → [0, 2, 4, 6, 8]                     │
# │ range(10, 0, -1)  → [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]    │
# │ range(5, -1, -1)  → [5, 4, 3, 2, 1, 0]                  │
# │ range(0, 10, 3)   → [0, 3, 6, 9]                        │
# │                                                          │
# │ for i in range(n):        → classic N-times loop        │
# │ for i in range(1, n+1):   → 1 to N inclusive            │
# │ for i in range(len(lst)): → index-based iteration       │
# │ for i in range(n, 0, -1): → countdown from N to 1      │
# └──────────────────────────────────────────────────────────┘