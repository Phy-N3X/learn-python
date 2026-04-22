# ============================================================
# MODULE 04 | EXERCISES 46 - enumerate()
# ============================================================
# 15 exercises from easiest to hardest
# Topic: enumerate() only
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 | EASY
# ------------------------------------------------------------
# Use enumerate() to print each fruit with its index.
#
# Expected output:
# 0: apple
# 1: banana
# 2: cherry
# 3: date

fruits = ["apple", "banana", "cherry", "date"]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 2 | EASY
# ------------------------------------------------------------
# Use enumerate() with start=1 to print a numbered list.
#
# Expected output:
# 1. Math
# 2. Science
# 3. English
# 4. History

subjects = ["Math", "Science", "English", "History"]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 3 | EASY
# ------------------------------------------------------------
# Use enumerate() to iterate over a string
# and print each character with its position.
#
# Expected output:
# Position 0: P
# Position 1: y
# Position 2: t
# Position 3: h
# Position 4: o
# Position 5: n

word = "Python"

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 4 | EASY
# ------------------------------------------------------------
# Convert the enumerate object to a list and print it.
# Then print how many pairs it contains.
#
# Expected output:
# [(0, 'red'), (1, 'green'), (2, 'blue')]
# Number of pairs: 3

colors = ["red", "green", "blue"]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 5 | EASY
# ------------------------------------------------------------
# Use enumerate() to print only the items
# at EVEN indexes (0, 2, 4...).
#
# Expected output:
# [0] cat
# [2] dog
# [4] fish

animals = ["cat", "bird", "dog", "snake", "fish"]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 6 | EASY-MEDIUM
# ------------------------------------------------------------
# Use enumerate() to print a menu.
# Numbers should start from 1.
# Mark the LAST item with " <-- LAST ITEM"
#
# Expected output:
# === TODAY'S MENU ===
# 1. Pizza
# 2. Pasta
# 3. Salad
# 4. Soup <-- LAST ITEM

menu = ["Pizza", "Pasta", "Salad", "Soup"]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 7 | EASY-MEDIUM
# ------------------------------------------------------------
# Use enumerate() to find ALL positions of a target value.
# Store positions in a list, then print them.
#
# Expected output:
# 'python' found at positions: [1, 4, 6]

words = ["java", "python", "c++", "ruby", "python", "go", "python"]
target = "python"

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 8 | EASY-MEDIUM
# ------------------------------------------------------------
# Use enumerate() to number the words in a sentence.
# Split the sentence first, then enumerate the words.
#
# Expected output:
# Word 1: Learning
# Word 2: Python
# Word 3: is
# Word 4: really
# Word 5: fun

sentence = "Learning Python is really fun"

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 9 | MEDIUM
# ------------------------------------------------------------
# Use enumerate() to find the index of the MAXIMUM value
# in the list. Do NOT use the index() method.
# Use only enumerate() and a loop.
#
# Expected output:
# Max value: 97
# Found at index: 4

scores = [85, 92, 78, 88, 97, 73, 91]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 10 | MEDIUM
# ------------------------------------------------------------
# Use enumerate() to replace every item at an ODD index
# with the string "REPLACED".
# Print the list before and after.
#
# Expected output:
# Before: ['a', 'b', 'c', 'd', 'e', 'f']
# After:  ['a', 'REPLACED', 'c', 'REPLACED', 'e', 'REPLACED']

items = ["a", "b", "c", "d", "e", "f"]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 11 | MEDIUM
# ------------------------------------------------------------
# Use enumerate() to print a matrix with row numbers.
# Each row should show: "Row X: [values]"
# Then print which row has the highest SUM.
#
# Expected output:
# Row 1: [3, 7, 2]  sum=12
# Row 2: [8, 1, 5]  sum=14
# Row 3: [4, 9, 6]  sum=19
# Highest sum: Row 3 with sum=19

matrix = [
    [3, 7, 2],
    [8, 1, 5],
    [4, 9, 6]
]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 12 | MEDIUM-HARD
# ------------------------------------------------------------
# Use enumerate() to create TWO dictionaries from one list:
# 1. index_to_word:  {0: 'apple', 1: 'banana', ...}
# 2. word_to_index:  {'apple': 0, 'banana': 1, ...}
# Print both dictionaries.
# Then use word_to_index to find the index of "cherry".
#
# Expected output:
# index_to_word: {0: 'apple', 1: 'banana', 2: 'cherry', 3: 'date'}
# word_to_index: {'apple': 0, 'banana': 1, 'cherry': 2, 'date': 3}
# Index of 'cherry': 2

fruits = ["apple", "banana", "cherry", "date"]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 13 | MEDIUM-HARD
# ------------------------------------------------------------
# You have a list of temperatures.
# Use enumerate() to:
# 1. Print each day and temperature
# 2. Mark days where temp > 30 as "HOT"
# 3. Mark days where temp < 10 as "COLD"
# 4. Otherwise mark as "NORMAL"
# 5. After the loop, print how many days were HOT, COLD, NORMAL
#
# Expected output:
# Day 1:  12°C - NORMAL
# Day 2:  35°C - HOT
# Day 3:   8°C - COLD
# Day 4:  22°C - NORMAL
# Day 5:  31°C - HOT
# Day 6:   5°C - COLD
# Day 7:  28°C - NORMAL
# ---
# HOT days:    2
# COLD days:   2
# NORMAL days: 3

temperatures = [12, 35, 8, 22, 31, 5, 28]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 14 | HARD
# ------------------------------------------------------------
# Use enumerate() with a nested loop to print a matrix.
# Add row numbers (starting from 1) and column headers.
# Also find and print the position of the minimum value.
#
# Expected output:
#        C1    C2    C3    C4
# R1:     5    12     3    18
# R2:    19     7    22     4
# R3:     8    15     1    11
#
# Minimum value: 1 at Row 3, Column 3

matrix = [
    [5,  12,  3, 18],
    [19,  7, 22,  4],
    [8,  15,  1, 11]
]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 15 | HARD
# ------------------------------------------------------------
# You have a list of student results.
# Use enumerate() to:
# 1. Print a full ranked report (rank starts at 1)
# 2. Find who improved compared to the PREVIOUS student
#    (score higher than the one before them)
# 3. Mark improved students with "(+)" next to their name
# 4. After the report, print the name of the student
#    with the BEST score and their rank
#
# Expected output:
# ==============================
#  RANK  NAME         SCORE
# ==============================
#    1.  Alice          85
#    2.  Bob            91  (+)
#    3.  Charlie        78
#    4.  Diana          95  (+)
#    5.  Eve            88
#    6.  Frank          99  (+)
# ==============================
# Best student: Frank (rank 6) with score 99
#
# Note: rank 1 (first student) cannot be marked with (+)
# because there is no previous student to compare to.

results = [
    {"name": "Alice",   "score": 85},
    {"name": "Bob",     "score": 91},
    {"name": "Charlie", "score": 78},
    {"name": "Diana",   "score": 95},
    {"name": "Eve",     "score": 88},
    {"name": "Frank",   "score": 99}
]

# YOUR CODE HERE: