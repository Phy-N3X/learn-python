# ============================================================
# MODULE 04 | EXERCISES 45 - Nested Loops
# ============================================================
# 15 exercises from easiest to hardest
# Topic: Nested Loops only
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 | EASY
# ------------------------------------------------------------
# Write a nested for loop that prints all combinations
# of two ranges: outer from 1 to 3, inner from 1 to 3.
#
# Expected output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3
# 3 1
# 3 2
# 3 3

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 2 | EASY
# ------------------------------------------------------------
# Print the following rectangle of stars using nested loops.
# Use variables for width and height.
#
# width = 6, height = 4
#
# Expected output:
# ******
# ******
# ******
# ******

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 3 | EASY
# ------------------------------------------------------------
# You have this list of lists.
# Use nested loops to print every element on a separate line.
#
# Expected output:
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 4 | EASY
# ------------------------------------------------------------
# Use nested loops to print a right-angled triangle of stars.
# 5 rows.
#
# Expected output:
# *
# **
# ***
# ****
# *****

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 5 | EASY
# ------------------------------------------------------------
# You have two lists below.
# Print all possible full name combinations.
#
# Expected output:
# Anna Smith
# Anna Jones
# Ben Smith
# Ben Jones
# Cara Smith
# Cara Jones

first_names = ["Anna", "Ben", "Cara"]
last_names = ["Smith", "Jones"]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 6 | EASY-MEDIUM
# ------------------------------------------------------------
# Print a 5x5 multiplication table using nested loops.
# Format each number with a width of 4 characters.
#
# Expected output:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 7 | EASY-MEDIUM
# ------------------------------------------------------------
# You have a list of words below.
# Use nested loops to print each word,
# and below it - each letter on a separate indented line.
#
# Expected output:
# hi
#   h
#   i
# cat
#   c
#   a
#   t
# sun
#   s
#   u
#   n

words = ["hi", "cat", "sun"]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 8 | EASY-MEDIUM
# ------------------------------------------------------------
# Use nested WHILE loops (not for!) to print this pattern.
# Remember to reset the inner counter correctly!
#
# Expected output:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 9 | MEDIUM
# ------------------------------------------------------------
# Use nested loops to find the sum of all elements
# in this 2D list. Also count how many elements there are.
#
# Expected output:
# Sum: 45
# Count: 9
# Average: 5.0

numbers = [
    [3, 7, 2],
    [8, 1, 5],
    [4, 9, 6]
]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 10 | MEDIUM
# ------------------------------------------------------------
# Print all UNIQUE pairs from this list.
# No pair repeated, no pair with itself.
# (1,2) and (2,1) count as the SAME - print only once.
#
# Expected output:
# (1, 2)
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)
# (3, 4)

items = [1, 2, 3, 4]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 11 | MEDIUM
# ------------------------------------------------------------
# Use nested loops to print a checkerboard pattern.
# Size: 6x6. Use "■" and "□" characters (or X and O).
#
# Expected output:
# ■ □ ■ □ ■ □
# □ ■ □ ■ □ ■
# ■ □ ■ □ ■ □
# □ ■ □ ■ □ ■
# ■ □ ■ □ ■ □
# □ ■ □ ■ □ ■

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 12 | MEDIUM-HARD
# ------------------------------------------------------------
# You have a list of students and their grades below.
# For each student:
# - Print their name
# - Print each grade
# - Print their average (2 decimal places)
# - Print whether they PASSED (average >= 75) or FAILED
#
# Expected output format:
# Alice: grades=[85, 90, 78, 92], avg=86.25, PASSED
# Bob:   grades=[70, 88, 95, 60], avg=78.25, PASSED
# Charlie: grades=[99, 75, 82, 88], avg=86.00, PASSED

students = ["Alice", "Bob", "Charlie"]
grades = [
    [85, 90, 78, 92],
    [70, 88, 95, 60],
    [99, 75, 82, 88]
]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 13 | MEDIUM-HARD
# ------------------------------------------------------------
# Use nested loops to search for a target value in a 2D list.
# Stop searching as soon as you find it (use break + flag).
# Print every cell you check before finding it.
#
# Expected output:
# Searching...
# Checked [0][0] = 5
# Checked [0][1] = 12
# Checked [0][2] = 3
# Checked [1][0] = 19
# Found 7 at row=1, col=1
# Search stopped.

matrix = [
    [5,  12,  3],
    [19,  7, 22],
    [8,  15,  1]
]
target = 7

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 14 | HARD
# ------------------------------------------------------------
# Print a centered diamond pattern using nested loops.
# The size (half-height) should be stored in a variable.
#
# size = 5
#
# Expected output:
#     *
#    ***
#   *****
#  *******
# *********
#  *******
#   *****
#    ***
#     *
#
# Requirements:
# - Use a variable size = 5
# - Use nested loops (outer for rows, inner for spaces and stars)
# - No string multiplication tricks - print char by char

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 15 | HARD
# ------------------------------------------------------------
# You have a school dictionary below.
# Use nested loops to:
# 1. Print each subject
# 2. Under each subject, print each student
# 3. Print their individual grades
# 4. Print their average for that subject
# 5. After ALL subjects, print each student's OVERALL average
#    across all subjects combined
#
# Expected output format:
# Subject: Mathematics
#   Alice: [88, 92, 79] -> avg: 86.33
#   Bob:   [70, 65, 80] -> avg: 71.67
#
# Subject: Science
#   Alice: [95, 90, 85] -> avg: 90.00
#   Bob:   [88, 72, 91] -> avg: 83.67
#
# Subject: English
#   Alice: [78, 82, 88] -> avg: 82.67
#   Bob:   [90, 85, 92] -> avg: 89.00
#
# Overall averages:
#   Alice: 86.33
#   Bob:   81.44

school = {
    "Mathematics": {
        "Alice": [88, 92, 79],
        "Bob":   [70, 65, 80]
    },
    "Science": {
        "Alice": [95, 90, 85],
        "Bob":   [88, 72, 91]
    },
    "English": {
        "Alice": [78, 82, 88],
        "Bob":   [90, 85, 92]
    }
}

# YOUR CODE HERE: