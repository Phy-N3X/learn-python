# ============================================================
# MODULE 04 | LECTURE 46 - enumerate()
# ============================================================
# What you will learn:
# - What enumerate() is and why it exists
# - How to use enumerate() in a for loop
# - How to change the starting index
# - enumerate() with lists, strings, tuples
# - enumerate() with unpacking
# - Practical use cases
# - enumerate() vs range(len()) comparison
# - enumerate() with conditions
# - enumerate() with nested loops
# ============================================================


# ------------------------------------------------------------
# PART 1: The problem that enumerate() solves
# ------------------------------------------------------------

# Very often when looping over a list,
# you need BOTH the index AND the value.

# The OLD way - using range(len()):
fruits = ["apple", "banana", "cherry", "date"]

for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
# 3: date

# This works, but it is clunky.
# You have to manually get fruits[i] every time.
# Python has a much cleaner solution: enumerate()


# ------------------------------------------------------------
# PART 2: What is enumerate()?
# ------------------------------------------------------------

# enumerate() is a built-in Python function.
# It wraps an iterable and returns pairs of (index, value).

# Basic syntax:
# for index, value in enumerate(iterable):

fruits = ["apple", "banana", "cherry", "date"]

for index, value in enumerate(fruits):
    print(f"{index}: {value}")

# Output:
# 0: apple
# 1: banana
# 2: cherry
# 3: date

# Same result as range(len()) but much cleaner!

# What does enumerate() actually return?
fruits = ["apple", "banana", "cherry"]
result = enumerate(fruits)
print(result)           # <enumerate object at 0x...>
print(type(result))     # <class 'enumerate'>

# To see the content, convert to list:
print(list(enumerate(fruits)))
# [(0, 'apple'), (1, 'banana'), (2, 'cherry')]

# It returns a list of TUPLES: (index, value)
# Each tuple = one (index, value) pair


# ------------------------------------------------------------
# PART 3: Unpacking in enumerate()
# ------------------------------------------------------------

# When you write: for index, value in enumerate(...)
# Python automatically UNPACKS each tuple into two variables.

fruits = ["apple", "banana", "cherry"]

# This:
for index, value in enumerate(fruits):
    print(index, value)

# Is exactly the same as this:
for item in enumerate(fruits):
    index = item[0]
    value = item[1]
    print(index, value)

# You can name the variables anything:
for i, fruit in enumerate(fruits):
    print(f"Fruit #{i} is {fruit}")

# Output:
# Fruit #0 is apple
# Fruit #1 is banana
# Fruit #2 is cherry

# Common variable name conventions:
# for i, item in enumerate(...)       # generic
# for i, name in enumerate(names)     # specific to content
# for idx, val in enumerate(values)   # idx is short for index
# for num, word in enumerate(words)   # descriptive


# ------------------------------------------------------------
# PART 4: Changing the starting index
# ------------------------------------------------------------

# By default enumerate() starts counting from 0.
# You can change this with the 'start' parameter.

fruits = ["apple", "banana", "cherry"]

# Start from 1 (human-friendly numbering)
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}. {fruit}")

# Output:
# 1. apple
# 2. banana
# 3. cherry

# Start from any number:
for i, fruit in enumerate(fruits, start=10):
    print(f"{i}. {fruit}")

# Output:
# 10. apple
# 11. banana
# 12. cherry

# Start from a negative number:
for i, fruit in enumerate(fruits, start=-1):
    print(f"{i}. {fruit}")

# Output:
# -1. apple
#  0. banana
#  1. cherry

# Practical example - numbered list for a menu:
menu_items = ["Coffee", "Tea", "Juice", "Water"]

print("=== MENU ===")
for number, item in enumerate(menu_items, start=1):
    print(f"  {number}. {item}")
print("============")

# Output:
# === MENU ===
#   1. Coffee
#   2. Tea
#   3. Juice
#   4. Water
# ============


# ------------------------------------------------------------
# PART 5: enumerate() with different data types
# ------------------------------------------------------------

# enumerate() works with ANY iterable.

# With a STRING - iterates over characters:
word = "Python"

for i, char in enumerate(word):
    print(f"Position {i}: '{char}'")

# Output:
# Position 0: 'P'
# Position 1: 'y'
# Position 2: 't'
# Position 3: 'h'
# Position 4: 'o'
# Position 5: 'n'


# With a TUPLE:
coordinates = (10.5, 20.3, 30.1)

for i, coord in enumerate(coordinates):
    axis = ["x", "y", "z"][i]
    print(f"{axis}-axis: {coord}")

# Output:
# x-axis: 10.5
# y-axis: 20.3
# z-axis: 30.1


# With a STRING split into words:
sentence = "I love Python programming"
words = sentence.split()

for i, word in enumerate(words, start=1):
    print(f"Word {i}: {word}")

# Output:
# Word 1: I
# Word 2: love
# Word 3: Python
# Word 4: programming


# With a DICTIONARY (iterates over keys by default):
person = {"name": "Alice", "age": 25, "city": "Warsaw"}

for i, key in enumerate(person, start=1):
    print(f"{i}. {key} = {person[key]}")

# Output:
# 1. name = Alice
# 2. age = 25
# 3. city = Warsaw

# With dictionary .items():
for i, (key, value) in enumerate(person.items(), start=1):
    print(f"{i}. {key}: {value}")

# Output:
# 1. name: Alice
# 2. age: 25
# 3. city: Warsaw


# ------------------------------------------------------------
# PART 6: enumerate() vs range(len()) - full comparison
# ------------------------------------------------------------

# The same task done both ways - decide which is cleaner!

names = ["Alice", "Bob", "Charlie", "Diana"]

# WAY 1: range(len()) - OLD style
print("--- range(len()) ---")
for i in range(len(names)):
    print(f"{i + 1}. {names[i]}")

# WAY 2: enumerate() - PYTHONIC style
print("--- enumerate() ---")
for i, name in enumerate(names, start=1):
    print(f"{i}. {name}")

# Both produce:
# 1. Alice
# 2. Bob
# 3. Charlie
# 4. Diana

# enumerate() wins because:
# - No need to write len()
# - No need to write names[i]
# - More readable
# - Less chance of index errors
# - Considered "Pythonic" (the Python way)

# When to still use range(len()):
# - When you need to MODIFY the list by index
# - When you need to access MULTIPLE indexes at once

# Modifying list - range(len()) is appropriate here:
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2    # modifying the list

print(numbers)  # [2, 4, 6, 8, 10]

# You CAN also do this with enumerate:
numbers = [1, 2, 3, 4, 5]

for i, num in enumerate(numbers):
    numbers[i] = num * 2           # i for index, num for value

print(numbers)  # [2, 4, 6, 8, 10]


# ------------------------------------------------------------
# PART 7: Practical use cases
# ------------------------------------------------------------

# Use case 1: Finding the position of a specific item
fruits = ["apple", "banana", "cherry", "banana", "date"]

search = "banana"
positions = []

for i, fruit in enumerate(fruits):
    if fruit == search:
        positions.append(i)

print(f"'{search}' found at positions: {positions}")
# Output: 'banana' found at positions: [1, 3]


# Use case 2: Printing only EVEN-indexed items
items = ["a", "b", "c", "d", "e", "f"]

print("Even-indexed items:")
for i, item in enumerate(items):
    if i % 2 == 0:
        print(f"  [{i}] {item}")

# Output:
# Even-indexed items:
#   [0] a
#   [2] c
#   [4] e


# Use case 3: Finding the maximum value AND its position
scores = [85, 92, 78, 95, 88, 91]

max_score = scores[0]
max_index = 0

for i, score in enumerate(scores):
    if score > max_score:
        max_score = score
        max_index = i

print(f"Highest score: {max_score} at position {max_index}")
# Output: Highest score: 95 at position 3


# Use case 4: Creating a numbered report
students = [
    {"name": "Alice", "grade": 92},
    {"name": "Bob",   "grade": 85},
    {"name": "Carol", "grade": 78},
    {"name": "Dave",  "grade": 95}
]

print("=" * 35)
print("       STUDENT REPORT")
print("=" * 35)

for rank, student in enumerate(students, start=1):
    print(f"  {rank}. {student['name']:<10} Grade: {student['grade']}")

print("=" * 35)

# Output:
# ===================================
#        STUDENT REPORT
# ===================================
#   1. Alice      Grade: 92
#   2. Bob        Grade: 85
#   3. Carol      Grade: 78
#   4. Dave       Grade: 95
# ===================================


# Use case 5: Replacing specific elements by index
words = ["I", "love", "Java", "programming"]

for i, word in enumerate(words):
    if word == "Java":
        words[i] = "Python"         # replace at found index

print(words)
# Output: ['I', 'love', 'Python', 'programming']


# Use case 6: Alternating formatting (zebra striping)
items = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

for i, name in enumerate(items):
    if i % 2 == 0:
        print(f"  >>> {name}")      # even rows
    else:
        print(f"      {name}")      # odd rows

# Output:
#   >>> Alice
#       Bob
#   >>> Charlie
#       Diana
#   >>> Eve


# ------------------------------------------------------------
# PART 8: enumerate() with conditions and break
# ------------------------------------------------------------

# Finding FIRST occurrence and stopping:
values = [10, 25, 3, 47, 8, 52, 19]
threshold = 40

for i, value in enumerate(values):
    if value > threshold:
        print(f"First value above {threshold}: {value} at index {i}")
        break

# Output: First value above 40: 47 at index 3


# Skipping specific indexes with continue:
data = ["valid", "SKIP", "valid", "SKIP", "valid"]

for i, item in enumerate(data):
    if item == "SKIP":
        print(f"  Skipping index {i}")
        continue
    print(f"  Processing [{i}]: {item}")

# Output:
#   Processing [0]: valid
#   Skipping index 1
#   Processing [2]: valid
#   Skipping index 3
#   Processing [4]: valid


# ------------------------------------------------------------
# PART 9: enumerate() with nested loops
# ------------------------------------------------------------

# enumerate() in nested loops - tracking row and column:
matrix = [
    ["A", "B", "C"],
    ["D", "E", "F"],
    ["G", "H", "I"]
]

for row_idx, row in enumerate(matrix):
    for col_idx, value in enumerate(row):
        print(f"  [{row_idx}][{col_idx}] = {value}")

# Output:
#   [0][0] = A
#   [0][1] = B
#   [0][2] = C
#   [1][0] = D
#   [1][1] = E
#   [1][2] = F
#   [2][0] = G
#   [2][1] = H
#   [2][2] = I


# Printing a matrix with row numbers and column headers:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print column headers
print("     col0  col1  col2")

for row_idx, row in enumerate(matrix):
    print(f"row{row_idx}", end="  ")
    for col_idx, value in enumerate(row):
        print(f"{value:5}", end=" ")
    print()

# Output:
#      col0  col1  col2
# row0     1     2     3
# row1     4     5     6
# row2     7     8     9


# ------------------------------------------------------------
# PART 10: enumerate() - advanced tricks
# ------------------------------------------------------------

# Trick 1: Using _ when you only need the index
words = ["apple", "banana", "cherry"]

# If you only need the count (not the value):
for i, _ in enumerate(words, start=1):
    print(f"Item number: {i}")

# Output:
# Item number: 1
# Item number: 2
# Item number: 3


# Trick 2: Getting the last element's index
items = ["x", "y", "z"]
last_index = 0

for i, _ in enumerate(items):
    last_index = i

print(f"Last index: {last_index}")   # Last index: 2
# Better way: len(items) - 1, but good to know


# Trick 3: enumerate() with list comprehension
words = ["hello", "world", "python"]

# Create a list of "index: word" strings
indexed = [f"{i}: {word}" for i, word in enumerate(words)]
print(indexed)
# Output: ['0: hello', '1: world', '2: python']


# Trick 4: Converting enumerate to a dictionary
fruits = ["apple", "banana", "cherry"]

fruit_dict = {i: fruit for i, fruit in enumerate(fruits)}
print(fruit_dict)
# Output: {0: 'apple', 1: 'banana', 2: 'cherry'}

# Reversed - fruit as key, index as value:
fruit_index = {fruit: i for i, fruit in enumerate(fruits)}
print(fruit_index)
# Output: {'apple': 0, 'banana': 1, 'cherry': 2}


# Trick 5: Checking if item is first or last
items = ["first", "middle1", "middle2", "last"]
last_idx = len(items) - 1

for i, item in enumerate(items):
    if i == 0:
        label = "[FIRST]"
    elif i == last_idx:
        label = "[LAST]"
    else:
        label = "[MIDDLE]"
    print(f"  {label} {item}")

# Output:
#   [FIRST] first
#   [MIDDLE] middle1
#   [MIDDLE] middle2
#   [LAST] last


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# enumerate() wraps any iterable and adds an index counter
# Returns pairs of (index, value) as tuples
# Use: for i, value in enumerate(iterable)
# Default start = 0, change with: enumerate(iterable, start=1)
# Works with: lists, strings, tuples, dictionaries
# Cleaner and more Pythonic than range(len())
# Can be converted to list of tuples: list(enumerate(...))
# Can be used to build dictionaries with index as key
# break and continue work normally inside enumerate() loops
# Use _ when you need index but not the value: for i, _ in ...

# Quick reference:
# enumerate(items)           --> starts at 0
# enumerate(items, start=1)  --> starts at 1
# enumerate(items, start=10) --> starts at 10
# list(enumerate(items))     --> [(0,'a'), (1,'b'), ...]