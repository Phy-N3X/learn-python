# ============================================================
# MODULE 04 | LECTURE 47 - zip()
# ============================================================
# What you will learn:
# - What zip() is and why it exists
# - How zip() works with two lists
# - How zip() works with three or more lists
# - What happens when lists have different lengths
# - zip() with enumerate()
# - zip() with unpacking
# - unzipping with zip(*)
# - zip() with strings, tuples, dictionaries
# - Practical use cases
# - zip_longest() from itertools
# ============================================================


# ------------------------------------------------------------
# PART 1: The problem that zip() solves
# ------------------------------------------------------------

# Imagine you have two related lists:
names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# You want to print them together:
# Alice scored 85
# Bob scored 92
# Charlie scored 78

# The OLD way - using range(len()):
for i in range(len(names)):
    print(f"{names[i]} scored {scores[i]}")

# This works, but it is clunky.
# You have to manually index BOTH lists.
# Python has a much cleaner solution: zip()


# ------------------------------------------------------------
# PART 2: What is zip()?
# ------------------------------------------------------------

# zip() is a built-in Python function.
# It takes two or more iterables and "zips" them together
# into pairs (or triples, etc.) like a zipper on a jacket.

# Visual concept:
# names  = ["Alice",  "Bob",  "Charlie"]
#              |         |        |
# scores = [  85,       92,      78   ]
#              |         |        |
# result = [("Alice",85),("Bob",92),("Charlie",78)]

# Basic syntax:
# for a, b in zip(list1, list2):

names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for name, score in zip(names, scores):
    print(f"{name} scored {score}")

# Output:
# Alice scored 85
# Bob scored 92
# Charlie scored 78

# Clean, readable, Pythonic!


# What does zip() actually return?
names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

result = zip(names, scores)
print(result)           # <zip object at 0x...>
print(type(result))     # <class 'zip'>

# To see the content, convert to list:
print(list(zip(names, scores)))
# [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# It returns a list of TUPLES.
# Each tuple = one group of matching elements.


# ------------------------------------------------------------
# PART 3: zip() with two lists - unpacking
# ------------------------------------------------------------

# When you write: for name, score in zip(names, scores)
# Python automatically UNPACKS each tuple.

names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# This:
for name, score in zip(names, scores):
    print(name, score)

# Is exactly the same as this:
for pair in zip(names, scores):
    name  = pair[0]
    score = pair[1]
    print(name, score)

# You can name the variables anything meaningful:
first_names = ["Alice", "Bob", "Charlie"]
last_names  = ["Smith", "Jones", "Brown"]

for first, last in zip(first_names, last_names):
    print(f"Full name: {first} {last}")

# Output:
# Full name: Alice Smith
# Full name: Bob Jones
# Full name: Charlie Brown


# ------------------------------------------------------------
# PART 4: zip() with THREE or more lists
# ------------------------------------------------------------

# zip() can handle any number of iterables at once.

names   = ["Alice", "Bob", "Charlie"]
scores  = [85, 92, 78]
grades  = ["B", "A", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score} points -> Grade {grade}")

# Output:
# Alice: 85 points -> Grade B
# Bob: 92 points -> Grade A
# Charlie: 78 points -> Grade C


# Four lists at once:
products   = ["Apple",  "Banana", "Cherry"]
prices     = [1.20,     0.50,     3.00]
quantities = [100,      250,      50]
in_stock   = [True,     True,     False]

print(f"{'Product':<10} {'Price':>6} {'Qty':>5} {'In Stock':>10}")
print("-" * 35)

for product, price, qty, stock in zip(products, prices, quantities, in_stock):
    stock_label = "Yes" if stock else "No"
    print(f"{product:<10} {price:>6.2f} {qty:>5} {stock_label:>10}")

# Output:
# Product     Price   Qty   In Stock
# -----------------------------------
# Apple        1.20   100        Yes
# Banana       0.50   250        Yes
# Cherry       3.00    50         No


# ------------------------------------------------------------
# PART 5: What happens with DIFFERENT length lists?
# ------------------------------------------------------------

# zip() STOPS at the SHORTEST list!
# Extra elements from longer lists are IGNORED.

short = [1, 2, 3]
long  = [10, 20, 30, 40, 50]

for a, b in zip(short, long):
    print(a, b)

# Output:
# 1 10
# 2 20
# 3 30
# 40 and 50 are IGNORED because short list ran out!

# Visual:
# short = [1,    2,    3   ]
# long  = [10,   20,   30,   40,   50]
#          |     |     |     X     X   <- stops here
# pairs = [(1,10),(2,20),(3,30)]


# This can be dangerous if you expect all elements to match:
names  = ["Alice", "Bob", "Charlie", "Diana"]  # 4 items
scores = [85, 92, 78]                           # 3 items - Diana missing!

for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Output:
# Alice: 85
# Bob: 92
# Charlie: 78
# Diana is silently skipped! No error, no warning!

# Always make sure your lists have the same length
# OR use zip_longest() if you want to keep all elements.


# ------------------------------------------------------------
# PART 6: zip_longest() - keeping all elements
# ------------------------------------------------------------

# If you need ALL elements even when lists differ in length,
# use zip_longest() from the itertools module.

from itertools import zip_longest

names  = ["Alice", "Bob", "Charlie", "Diana"]
scores = [85, 92, 78]

# Default fill value is None:
for name, score in zip_longest(names, scores):
    print(f"{name}: {score}")

# Output:
# Alice: 85
# Bob: 92
# Charlie: 78
# Diana: None       <- filled with None

# Custom fill value:
for name, score in zip_longest(names, scores, fillvalue="N/A"):
    print(f"{name}: {score}")

# Output:
# Alice: 85
# Bob: 92
# Charlie: 78
# Diana: N/A        <- filled with "N/A"


# zip_longest() with multiple lists of different lengths:
a = [1, 2, 3]
b = [10, 20]
c = [100, 200, 300, 400]

for x, y, z in zip_longest(a, b, c, fillvalue=0):
    print(x, y, z)

# Output:
# 1 10 100
# 2 20 200
# 3 0 300
# 0 0 400


# ------------------------------------------------------------
# PART 7: Unzipping with zip(*)
# ------------------------------------------------------------

# zip(*) is the REVERSE of zip().
# It "unzips" a list of tuples back into separate lists.

# zip() joins lists together:
names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
zipped = list(zip(names, scores))
print(zipped)
# [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# zip(*) separates them back:
unzipped = list(zip(*zipped))
print(unzipped)
# [('Alice', 'Bob', 'Charlie'), (85, 92, 78)]

# Assign to separate variables:
names_back, scores_back = zip(*zipped)
print(names_back)   # ('Alice', 'Bob', 'Charlie')
print(scores_back)  # (85, 92, 78)

# Note: zip(*) returns TUPLES, not lists.
# Convert to list if needed:
names_back = list(names_back)
print(names_back)   # ['Alice', 'Bob', 'Charlie']


# Practical unzip example - transposing a matrix:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
for row in matrix:
    print(" ", row)

transposed = list(zip(*matrix))

print("Transposed matrix:")
for row in transposed:
    print(" ", row)

# Output:
# Original matrix:
#   [1, 2, 3]
#   [4, 5, 6]
#   [7, 8, 9]
# Transposed matrix:
#   (1, 4, 7)
#   (2, 5, 8)
#   (3, 6, 9)

# Rows became columns, columns became rows!


# ------------------------------------------------------------
# PART 8: zip() with different data types
# ------------------------------------------------------------

# zip() works with ANY iterable.

# With STRINGS - iterates character by character:
word1 = "ABC"
word2 = "xyz"

for char1, char2 in zip(word1, word2):
    print(f"{char1} pairs with {char2}")

# Output:
# A pairs with x
# B pairs with y
# C pairs with z


# Comparing two strings character by character:
s1 = "Python"
s2 = "Pythop"

differences = 0
for i, (c1, c2) in enumerate(zip(s1, s2)):
    if c1 != c2:
        print(f"Difference at position {i}: '{c1}' vs '{c2}'")
        differences += 1

if differences == 0:
    print("Strings are identical!")
else:
    print(f"Total differences: {differences}")

# Output:
# Difference at position 5: 'n' vs 'p'
# Total differences: 1


# With TUPLES:
coords_2d = ((0, 0), (1, 2), (3, 4))
labels     = ("origin", "point A", "point B")

for label, (x, y) in zip(labels, coords_2d):
    print(f"{label}: x={x}, y={y}")

# Output:
# origin: x=0, y=0
# point A: x=1, y=2
# point B: x=3, y=4


# With RANGE:
letters = ["a", "b", "c", "d", "e"]

for number, letter in zip(range(1, 6), letters):
    print(f"{number} -> {letter}")

# Output:
# 1 -> a
# 2 -> b
# 3 -> c
# 4 -> d
# 5 -> e


# ------------------------------------------------------------
# PART 9: zip() with enumerate()
# ------------------------------------------------------------

# You can combine zip() AND enumerate() together.
# enumerate() adds an index, zip() pairs the lists.

names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name}: {score}")

# Output:
# 1. Alice: 85
# 2. Bob: 92
# 3. Charlie: 78

# Note the double unpacking: (name, score)
# enumerate gives: (index, (name, score))
# we unpack both at once


# Ranked leaderboard with enumerate + zip:
players = ["Alice", "Bob", "Charlie", "Diana"]
points  = [1200, 980, 1450, 1100]
levels  = [15, 12, 18, 14]

print("=" * 40)
print(f"{'RANK':<6} {'PLAYER':<12} {'POINTS':>7} {'LEVEL':>6}")
print("=" * 40)

for rank, (player, pts, lvl) in enumerate(zip(players, points, levels), start=1):
    print(f"{rank:<6} {player:<12} {pts:>7} {lvl:>6}")

print("=" * 40)

# Output:
# ========================================
# RANK   PLAYER       POINTS  LEVEL
# ========================================
# 1      Alice          1200     15
# 2      Bob             980     12
# 3      Charlie        1450     18
# 4      Diana          1100     14
# ========================================


# ------------------------------------------------------------
# PART 10: Practical use cases
# ------------------------------------------------------------

# Use case 1: Creating a dictionary from two lists
keys   = ["name", "age", "city"]
values = ["Alice", 25, "Warsaw"]

person = dict(zip(keys, values))
print(person)
# Output: {'name': 'Alice', 'age': 25, 'city': 'Warsaw'}

# This is very common and very Pythonic!


# Use case 2: Calculating totals from two lists
prices    = [10.99, 5.49, 3.99, 8.75]
quantities = [2, 5, 3, 1]

total = 0
print("Order summary:")
for price, qty in zip(prices, quantities):
    subtotal = price * qty
    print(f"  {qty} x ${price:.2f} = ${subtotal:.2f}")
    total += subtotal

print(f"Total: ${total:.2f}")

# Output:
# Order summary:
#   2 x $10.99 = $21.98
#   5 x $5.49 = $27.45
#   3 x $3.99 = $11.97
#   1 x $8.75 = $8.75
# Total: $70.15


# Use case 3: Comparing two lists element by element
expected = [10, 20, 30, 40, 50]
actual   = [10, 25, 30, 45, 50]

print("Test results:")
all_pass = True

for i, (exp, act) in enumerate(zip(expected, actual)):
    if exp == act:
        print(f"  Test {i+1}: PASS ({act})")
    else:
        print(f"  Test {i+1}: FAIL (expected {exp}, got {act})")
        all_pass = False

print(f"\nAll tests passed: {all_pass}")

# Output:
# Test results:
#   Test 1: PASS (10)
#   Test 2: FAIL (expected 20, got 25)
#   Test 3: PASS (30)
#   Test 4: FAIL (expected 40, got 45)
#   Test 5: PASS (50)
#
# All tests passed: False


# Use case 4: Merging two lists into a list of tuples
x_coords = [0, 1, 2, 3, 4]
y_coords = [0, 1, 4, 9, 16]

points = list(zip(x_coords, y_coords))
print(points)
# Output: [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

for x, y in points:
    print(f"Point ({x}, {y})")

# Output:
# Point (0, 0)
# Point (1, 1)
# Point (2, 4)
# Point (3, 9)
# Point (4, 16)


# Use case 5: Parallel sorting
names  = ["Charlie", "Alice", "Diana", "Bob"]
scores = [78, 85, 92, 91]

# Zip, sort by score, then unzip
paired = list(zip(scores, names))   # score first for sorting!
paired.sort(reverse=True)           # sort by first element (score)

print("Sorted by score (highest first):")
for rank, (score, name) in enumerate(paired, start=1):
    print(f"  {rank}. {name}: {score}")

# Output:
# Sorted by score (highest first):
#   1. Diana: 92
#   2. Bob: 91
#   3. Alice: 85
#   4. Charlie: 78


# Use case 6: Building a formatted table from multiple lists
headers    = ["Name", "Department", "Salary"]
names      = ["Alice", "Bob", "Charlie"]
departments = ["IT", "HR", "Finance"]
salaries   = [75000, 58000, 82000]

# Print header
print(f"{'Name':<12} {'Department':<12} {'Salary':>10}")
print("-" * 36)

# Print rows
for name, dept, sal in zip(names, departments, salaries):
    print(f"{name:<12} {dept:<12} {sal:>10,.0f}")

# Output:
# Name         Department       Salary
# ------------------------------------
# Alice        IT               75,000
# Bob          HR               58,000
# Charlie      Finance          82,000


# ------------------------------------------------------------
# PART 11: zip() vs range(len()) - full comparison
# ------------------------------------------------------------

names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

# WAY 1: range(len()) - OLD style
print("--- range(len()) ---")
for i in range(len(names)):
    print(f"{names[i]}: {scores[i]}")

# WAY 2: zip() - PYTHONIC style
print("--- zip() ---")
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# WAY 3: zip() + enumerate() - when you also need index
print("--- zip() + enumerate() ---")
for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(f"{i}. {name}: {score}")

# zip() wins because:
# - No need to write len()
# - No manual indexing with [i]
# - Much more readable
# - Works with any iterable, not just lists
# - Considered "Pythonic"

# When to still use range(len()):
# - When you need to modify items in BOTH lists by index
# - When you need to access non-matching indexes


# ------------------------------------------------------------
# PART 12: zip() - advanced tricks
# ------------------------------------------------------------

# Trick 1: zip() in list comprehension
names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]

combined = [f"{name}: {score}" for name, score in zip(names, scores)]
print(combined)
# Output: ['Alice: 85', 'Bob: 92', 'Charlie: 78']


# Trick 2: Creating a dictionary with dict(zip())
keys   = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]

my_dict = dict(zip(keys, values))
print(my_dict)
# Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}


# Trick 3: zip() to check if two lists are equal element by element
list1 = [1, 2, 3, 4]
list2 = [1, 2, 3, 4]

all_equal = all(a == b for a, b in zip(list1, list2))
print(f"Lists are equal: {all_equal}")
# Output: Lists are equal: True


# Trick 4: Consecutive pairs from ONE list using zip
numbers = [1, 2, 3, 4, 5]

# Pair each element with the NEXT one:
for current, next_val in zip(numbers, numbers[1:]):
    print(f"{current} -> {next_val}")

# Output:
# 1 -> 2
# 2 -> 3
# 3 -> 4
# 4 -> 5

# Very useful for detecting changes between consecutive values!


# Trick 5: Three consecutive elements (sliding window)
data = [10, 20, 15, 30, 25, 40]

for a, b, c in zip(data, data[1:], data[2:]):
    print(f"Window: {a}, {b}, {c}  ->  avg: {(a+b+c)/3:.1f}")

# Output:
# Window: 10, 20, 15  ->  avg: 15.0
# Window: 20, 15, 30  ->  avg: 21.7
# Window: 15, 30, 25  ->  avg: 23.3
# Window: 30, 25, 40  ->  avg: 31.7


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# zip() pairs elements from two or more iterables together
# Returns zip object - convert with list() to see contents
# Each element of zip result is a TUPLE
# Use: for a, b in zip(list1, list2)
# Use: for a, b, c in zip(list1, list2, list3)
# Stops at the SHORTEST iterable - longer ones get truncated!
# Use zip_longest() from itertools to keep ALL elements
# zip(*zipped) REVERSES zip - splits pairs back into lists
# Works with: lists, strings, tuples, ranges, dictionaries
# Combine with enumerate() when you also need an index
# dict(zip(keys, values)) creates a dictionary from two lists
# zip(list, list[1:]) creates consecutive pairs from one list

# Quick reference:
# zip(a, b)                    --> pairs two iterables
# zip(a, b, c)                 --> groups three iterables
# list(zip(a, b))              --> [(a0,b0), (a1,b1), ...]
# dict(zip(keys, values))      --> {key0: val0, key1: val1}
# zip(*paired)                 --> unzips back to originals
# zip_longest(a, b, fillvalue) --> keeps all, fills gaps
# zip(lst, lst[1:])            --> consecutive pairs