# ============================================================
# MODULE 04 | LECTURE 45 - Nested Loops
# ============================================================
# What you will learn:
# - What a nested loop is
# - How to nest for loops
# - How to nest while loops
# - Mixing for and while loops
# - How indentation controls nesting levels
# - Practical patterns: grids, tables, matrices
# - How to control nested loops with break/continue
# - Performance awareness (time complexity basics)
# - Real-world use cases
# ============================================================


# ------------------------------------------------------------
# PART 1: What is a nested loop?
# ------------------------------------------------------------

# A nested loop is simply a loop inside another loop.
# When Python encounters a loop inside another loop,
# it runs the ENTIRE inner loop for EVERY iteration of the outer loop.

# Think of it like a clock:
# - The outer loop  = the hour hand   (moves slowly)
# - The inner loop  = the minute hand (completes full cycle each time)

for outer in range(3):
    for inner in range(3):
        print(f"outer={outer}, inner={inner}")

# Output:
# outer=0, inner=0
# outer=0, inner=1
# outer=0, inner=2
# outer=1, inner=0
# outer=1, inner=1
# outer=1, inner=2
# outer=2, inner=0
# outer=2, inner=1
# outer=2, inner=2

# Total iterations = outer_count x inner_count = 3 x 3 = 9

# Visual flow:
# outer=0 --> inner runs: 0, 1, 2
# outer=1 --> inner runs: 0, 1, 2
# outer=2 --> inner runs: 0, 1, 2


# ------------------------------------------------------------
# PART 2: Indentation - the key to nested loops
# ------------------------------------------------------------

# Python uses indentation to know what belongs to which loop.
# A single wrong indent changes everything.

# CORRECT - inner print is INSIDE both loops
for i in range(3):
    for j in range(3):
        print(i, j)       # 8 spaces - inside both loops

# WRONG INDENTATION EXAMPLE
for i in range(3):
    for j in range(3):
        pass
    print(i, j)           # 4 spaces - OUTSIDE inner loop
                          # this runs once per outer iteration only

# Three levels of indentation:
for i in range(2):            # level 1 - outer loop
    for j in range(2):        # level 2 - middle loop
        for k in range(2):    # level 3 - inner loop
            print(i, j, k)    # level 4 - inside all loops

# Output:
# 0 0 0
# 0 0 1
# 0 1 0
# 0 1 1
# 1 0 0
# 1 0 1
# 1 1 0
# 1 1 1
# Total: 2 x 2 x 2 = 8 iterations


# ------------------------------------------------------------
# PART 3: Nested for loops - practical patterns
# ------------------------------------------------------------

# Pattern 1: Multiplication table
print("Multiplication Table (1-5):")
print()

for i in range(1, 6):           # rows 1 to 5
    for j in range(1, 6):       # columns 1 to 5
        result = i * j
        print(f"{result:4}", end="")    # :4 = width of 4 chars
    print()                     # new line after each row

# Output:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25


# Pattern 2: Stars triangle (right-angled)
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *
# **
# ***
# ****
# *****

# How it works step by step:
# i=1 --> inner runs 1 time  --> *
# i=2 --> inner runs 2 times --> **
# i=3 --> inner runs 3 times --> ***
# i=4 --> inner runs 4 times --> ****
# i=5 --> inner runs 5 times --> *****


# Pattern 3: Stars triangle (inverted)
rows = 5

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

# Output:
# *****
# ****
# ***
# **
# *


# Pattern 4: Rectangle of characters
width = 8
height = 4
char = "#"

for row in range(height):
    for col in range(width):
        print(char, end="")
    print()

# Output:
# ########
# ########
# ########
# ########


# Pattern 5: Checkerboard
size = 6

for row in range(size):
    for col in range(size):
        if (row + col) % 2 == 0:
            print("■", end=" ")
        else:
            print("□", end=" ")
    print()

# Output:
# ■ □ ■ □ ■ □
# □ ■ □ ■ □ ■
# ■ □ ■ □ ■ □
# □ ■ □ ■ □ ■
# ■ □ ■ □ ■ □
# □ ■ □ ■ □ ■


# ------------------------------------------------------------
# PART 4: Nested loops with lists
# ------------------------------------------------------------

# Iterating over a list of lists (2D data)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# Output:
# 1 2 3
# 4 5 6
# 7 8 9


# Accessing with index:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"matrix[{i}][{j}] = {matrix[i][j]}")

# Output:
# matrix[0][0] = 1
# matrix[0][1] = 2
# matrix[0][2] = 3
# matrix[1][0] = 4
# matrix[1][1] = 5
# matrix[1][2] = 6
# matrix[2][0] = 7
# matrix[2][1] = 8
# matrix[2][2] = 9


# Finding an element in a 2D list:
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

target = 50
found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print(f"Found {target} at row {i}, column {j}")
            found = True

if not found:
    print(f"{target} not found in matrix")

# Output:
# Found 50 at row 1, column 1


# Summing all elements in a 2D list:
grades = [
    [85, 92, 78],
    [90, 88, 95],
    [70, 75, 80]
]

total = 0
count = 0

for student_grades in grades:
    for grade in student_grades:
        total += grade
        count += 1

average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average:.2f}")

# Output:
# Total: 753
# Count: 9
# Average: 83.67


# ------------------------------------------------------------
# PART 5: Nested while loops
# ------------------------------------------------------------

# You can also nest while loops inside each other.
i = 1

while i <= 3:
    j = 1
    while j <= 3:
        print(f"i={i}, j={j}")
        j += 1
    i += 1

# Output:
# i=1, j=1
# i=1, j=2
# i=1, j=3
# i=2, j=1
# i=2, j=2
# i=2, j=3
# i=3, j=1
# i=3, j=2
# i=3, j=3

# IMPORTANT: Each while loop needs its own counter.
# You MUST reset the inner counter INSIDE the outer loop!

# WRONG - inner loop only runs once total!
i = 1
j = 1       # j starts at 1 only once

while i <= 3:
    while j <= 3:       # after first outer iteration,
        print(i, j)     # j is already 4 - this never runs again!
        j += 1
    i += 1

# CORRECT - reset j inside outer loop
i = 1

while i <= 3:
    j = 1               # j resets for each outer iteration
    while j <= 3:
        print(i, j)
        j += 1
    i += 1


# Nested while with countdown pattern:
outer = 3

while outer > 0:
    inner = outer
    while inner > 0:
        print("*", end="")
        inner -= 1
    print(f"  <- outer={outer}")
    outer -= 1

# Output:
# ***  <- outer=3
# **   <- outer=2
# *    <- outer=1


# ------------------------------------------------------------
# PART 6: Mixing for and while loops
# ------------------------------------------------------------

# You can freely mix loop types.

# for outside, while inside:
words = ["hello", "world", "python"]

for word in words:
    i = 0
    while i < len(word):
        print(word[i], end="-")
        i += 1
    print()

# Output:
# h-e-l-l-o-
# w-o-r-l-d-
# p-y-t-h-o-n-


# while outside, for inside:
attempt = 1

while attempt <= 3:
    print(f"Attempt {attempt}:")
    for step in ["connect", "process", "save"]:
        print(f"  -> {step}")
    attempt += 1

# Output:
# Attempt 1:
#   -> connect
#   -> process
#   -> save
# Attempt 2:
#   -> connect
#   -> process
#   -> save
# Attempt 3:
#   -> connect
#   -> process
#   -> save


# ------------------------------------------------------------
# PART 7: break and continue in nested loops
# ------------------------------------------------------------

# CRITICAL RULE:
# break and continue only affect the INNERMOST loop they are in.

# break only exits the INNER loop:
for i in range(3):
    for j in range(5):
        if j == 2:
            break               # exits inner loop only!
        print(f"i={i}, j={j}")
    print(f"--- outer i={i} continues ---")

# Output:
# i=0, j=0
# i=0, j=1
# --- outer i=0 continues ---
# i=1, j=0
# i=1, j=1
# --- outer i=1 continues ---
# i=2, j=0
# i=2, j=1
# --- outer i=2 continues ---


# continue in nested loops:
for i in range(3):
    for j in range(4):
        if j == 2:
            continue            # skips j=2, continues inner loop
        print(f"i={i}, j={j}")

# Output:
# i=0, j=0
# i=0, j=1
# i=0, j=3
# i=1, j=0
# i=1, j=1
# i=1, j=3
# i=2, j=0
# i=2, j=1
# i=2, j=3


# Breaking out of ALL nested loops using a flag:
matrix = [
    [1,  2,  3,  4],
    [5,  6,  7,  8],
    [9,  10, 0,  12],   # 0 is here at [2][2]
    [13, 14, 15, 16]
]

target = 0
found = False

for i in range(len(matrix)):
    if found:
        break                       # breaks outer loop
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print(f"Found {target} at [{i}][{j}]")
            found = True
            break                   # breaks inner loop

# Output:
# Found 0 at [2][2]


# Alternative: using a function to break all loops cleanly:
def find_in_matrix(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return i, j         # exits the function entirely!
    return None, None

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row, col = find_in_matrix(matrix, 5)
if row is not None:
    print(f"Found at row={row}, col={col}")

# Output:
# Found at row=1, col=1


# ------------------------------------------------------------
# PART 8: Iterating over strings with nested loops
# ------------------------------------------------------------

# Strings are iterable, so you can nest loops over them too.
words = ["cat", "dog", "fish"]

for word in words:
    print(f"Word: {word}")
    for letter in word:
        print(f"  Letter: {letter}")

# Output:
# Word: cat
#   Letter: c
#   Letter: a
#   Letter: t
# Word: dog
#   Letter: d
#   Letter: o
#   Letter: g
# Word: fish
#   Letter: f
#   Letter: i
#   Letter: s
#   Letter: h


# Comparing all pairs of characters:
word = "abc"

for i in range(len(word)):
    for j in range(len(word)):
        if i != j:
            print(f"{word[i]} + {word[j]} = {word[i]}{word[j]}")

# Output:
# a + b = ab
# a + c = ac
# b + a = ba
# b + c = bc
# c + a = ca
# c + b = cb


# ------------------------------------------------------------
# PART 9: Common patterns and real-world applications
# ------------------------------------------------------------

# Pattern: All combinations (pairs)
colors = ["red", "green", "blue"]
sizes = ["S", "M", "L"]

print("All product variants:")
count = 0
for color in colors:
    for size in sizes:
        print(f"  {color} - {size}")
        count += 1

print(f"Total variants: {count}")

# Output:
# All product variants:
#   red - S
#   red - M
#   red - L
#   green - S
#   green - M
#   green - L
#   blue - S
#   blue - M
#   blue - L
# Total variants: 9


# Pattern: Unique pairs only (no repeats)
items = ["A", "B", "C", "D"]

print("Unique pairs:")
for i in range(len(items)):
    for j in range(i + 1, len(items)):      # j starts AFTER i
        print(f"  ({items[i]}, {items[j]})")

# Output:
# Unique pairs:
#   (A, B)
#   (A, C)
#   (A, D)
#   (B, C)
#   (B, D)
#   (C, D)


# Pattern: Processing student grades table
students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science", "English"]

grades = [
    [85, 92, 78],   # Alice's grades
    [90, 75, 88],   # Bob's grades
    [70, 85, 95]    # Charlie's grades
]

for i in range(len(students)):
    print(f"\n{students[i]}'s grades:")
    total = 0
    for j in range(len(subjects)):
        print(f"  {subjects[j]}: {grades[i][j]}")
        total += grades[i][j]
    average = total / len(subjects)
    print(f"  Average: {average:.1f}")

# Output:
# Alice's grades:
#   Math: 85
#   Science: 92
#   English: 78
#   Average: 85.0
#
# Bob's grades:
#   Math: 90
#   Science: 75
#   English: 88
#   Average: 84.3
#
# Charlie's grades:
#   Math: 70
#   Science: 85
#   English: 95
#   Average: 83.3


# ------------------------------------------------------------
# PART 10: Performance awareness
# ------------------------------------------------------------

# Every extra loop level MULTIPLIES your iterations.
n = 100

# 1 loop: 100 iterations
for i in range(n):
    pass

# 2 loops: 100 x 100 = 10,000 iterations
for i in range(n):
    for j in range(n):
        pass

# 3 loops: 100 x 100 x 100 = 1,000,000 iterations
for i in range(n):
    for j in range(n):
        for k in range(n):
            pass

# This is called time complexity:
# 1 loop  --> O(n)   --> linear
# 2 loops --> O(n2)  --> quadratic
# 3 loops --> O(n3)  --> cubic

# With n=1000:
# O(n)  =             1,000 operations  --> fast
# O(n2) =         1,000,000 operations  --> manageable
# O(n3) = 1,000,000,000,000 operations  --> very slow!

# Practical tip - always ask yourself:
# - Do I really need 3 nested loops?
# - Can I break early with break?
# - Can I use a flag to exit early?


# ------------------------------------------------------------
# PART 11: Centered pyramid and diamond patterns
# ------------------------------------------------------------

# Centered pyramid:
rows = 5

for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Output:
#     *
#    ***
#   *****
#  *******
# *********


# Diamond:
rows = 5

# Top half (including middle)
for i in range(1, rows + 1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Bottom half
for i in range(rows - 1, 0, -1):
    spaces = rows - i
    stars = 2 * i - 1
    print(" " * spaces + "*" * stars)

# Output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *


# ------------------------------------------------------------
# PART 12: Nested loops with dictionaries
# ------------------------------------------------------------

school = {
    "class_A": ["Alice", "Bob", "Charlie"],
    "class_B": ["Diana", "Eve"],
    "class_C": ["Frank", "Grace", "Hank", "Iris"]
}

for class_name, students in school.items():
    print(f"\n{class_name}:")
    for student in students:
        print(f"  - {student}")

# Output:
# class_A:
#   - Alice
#   - Bob
#   - Charlie
#
# class_B:
#   - Diana
#   - Eve
#
# class_C:
#   - Frank
#   - Grace
#   - Hank
#   - Iris


# Nested dictionary iteration:
inventory = {
    "fruits":     {"apple": 50, "banana": 30, "cherry": 100},
    "vegetables": {"carrot": 20, "broccoli": 15},
    "dairy":      {"milk": 10, "cheese": 25, "yogurt": 40}
}

total_items = 0

for category, products in inventory.items():
    print(f"\nCategory: {category}")
    category_total = 0
    for product, quantity in products.items():
        print(f"  {product}: {quantity} units")
        category_total += quantity
    print(f"  Subtotal: {category_total}")
    total_items += category_total

print(f"\nGrand total: {total_items} items")

# Output:
# Category: fruits
#   apple: 50 units
#   banana: 30 units
#   cherry: 100 units
#   Subtotal: 180
#
# Category: vegetables
#   carrot: 20 units
#   broccoli: 15 units
#   Subtotal: 35
#
# Category: dairy
#   milk: 10 units
#   cheese: 25 units
#   yogurt: 40 units
#   Subtotal: 75
#
# Grand total: 290 items


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# Nested loop = loop inside a loop
# Inner loop runs COMPLETELY for each outer iteration
# Total iterations = outer x inner (x inner2 if 3 levels)
# Indentation controls which loop a line belongs to
# break/continue only affect the INNERMOST loop
# Use a flag variable to break out of ALL nested loops
# For loops and while loops can be freely mixed
# Works with lists, strings, dictionaries
# 3+ levels of nesting can be very slow - use wisely
# Functions with return are the cleanest way to exit nested loops

# Common uses:
#   - 2D grids, matrices, tables
#   - All combinations of two sets
#   - Unique pairs without repetition
#   - Processing rows and columns of data
#   - Drawing patterns with characters
