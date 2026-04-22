# ============================================================
# MODULE 04 | EXERCISES 47 - zip()
# ============================================================
# 15 exercises from easiest to hardest
# Topic: zip() only
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 | EASY
# ------------------------------------------------------------
# Use zip() to print each name with its corresponding score.
#
# Expected output:
# Alice scored 85
# Bob scored 92
# Charlie scored 78
# Diana scored 88

names  = ["Alice", "Bob", "Charlie", "Diana"]
scores = [85, 92, 78, 88]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 2 | EASY
# ------------------------------------------------------------
# Convert the two lists into a list of tuples using zip().
# Print the result.
# Then print how many pairs were created.
#
# Expected output:
# [('Math', 90), ('Science', 85), ('English', 92), ('History', 78)]
# Number of pairs: 4

subjects = ["Math", "Science", "English", "History"]
grades   = [90, 85, 92, 78]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 3 | EASY
# ------------------------------------------------------------
# Use zip() with THREE lists to print a product summary.
#
# Expected output:
# Apple    costs $1.20 and we have 100 in stock
# Banana   costs $0.50 and we have 250 in stock
# Cherry   costs $3.00 and we have 50 in stock

products   = ["Apple", "Banana", "Cherry"]
prices     = [1.20, 0.50, 3.00]
quantities = [100, 250, 50]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 4 | EASY
# ------------------------------------------------------------
# Use dict(zip()) to create a dictionary from two lists.
# Print the resulting dictionary.
# Then print the value for the key "age".
#
# Expected output:
# {'name': 'Alice', 'age': 25, 'city': 'Warsaw', 'job': 'developer'}
# Age: 25

keys   = ["name", "age", "city", "job"]
values = ["Alice", 25, "Warsaw", "developer"]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 5 | EASY
# ------------------------------------------------------------
# You have two lists of different lengths.
# First predict what will happen when you zip() them.
# Write your prediction as a comment.
# Then run and verify.
# Finally print a warning if lengths differ.
#
# Expected output:
# (a, 1)
# (b, 2)
# (c, 3)
# Warning: lists have different lengths! (5 vs 3)

letters = ["a", "b", "c", "d", "e"]
numbers = [1, 2, 3]

# Prediction: how many pairs will be printed? # YOUR ANSWER HERE

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 6 | EASY-MEDIUM
# ------------------------------------------------------------
# Use zip_longest() from itertools to pair these lists.
# Fill missing values with "N/A".
# Print each pair.
#
# Expected output:
# Alice - 85
# Bob - 92
# Charlie - N/A
# Diana - N/A

from itertools import zip_longest

names  = ["Alice", "Bob", "Charlie", "Diana"]
scores = [85, 92]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 7 | EASY-MEDIUM
# ------------------------------------------------------------
# Use zip() to compare two strings character by character.
# Print each position and whether the characters match.
# At the end print the total number of differences.
#
# Expected output:
# Position 0: 'P' vs 'P' --> MATCH
# Position 1: 'y' vs 'y' --> MATCH
# Position 2: 't' vs 't' --> MATCH
# Position 3: 'h' vs 'X' --> DIFFERENT
# Position 4: 'o' vs 'o' --> MATCH
# Position 5: 'n' vs 'n' --> MATCH
# Total differences: 1

s1 = "Python"
s2 = "PyXhon"

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 8 | EASY-MEDIUM
# ------------------------------------------------------------
# Use zip() to calculate the total cost of an order.
# Print each item's subtotal and the grand total.
#
# Expected output:
# 2 x Coffee    @ $3.50 = $7.00
# 1 x Sandwich  @ $6.99 = $6.99
# 3 x Cookie    @ $1.25 = $3.75
# 4 x Juice     @ $2.50 = $10.00
# ----------------------------
# Grand total: $27.74

items      = ["Coffee", "Sandwich", "Cookie", "Juice"]
prices     = [3.50, 6.99, 1.25, 2.50]
quantities = [2, 1, 3, 4]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 9 | MEDIUM
# ------------------------------------------------------------
# Use zip(*) to UNZIP the list of tuples back into
# two separate lists. Print both.
# Then verify by zipping them back together.
#
# Expected output:
# Names:  ['Alice', 'Bob', 'Charlie', 'Diana']
# Scores: [85, 92, 78, 88]
# Verified: [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('Diana', 88)]

paired = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("Diana", 88)]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 10 | MEDIUM
# ------------------------------------------------------------
# Use zip() with enumerate() to print a ranked leaderboard.
# Number starts from 1.
#
# Expected output:
# ==============================
# RANK  PLAYER       SCORE
# ==============================
#    1  Alice         1450
#    2  Diana         1200
#    3  Frank         1100
#    4  Bob            980
# ==============================
# Winner: Alice with 1450 points!

players = ["Alice", "Diana", "Frank", "Bob"]
scores  = [1450, 1200, 1100, 980]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 11 | MEDIUM
# ------------------------------------------------------------
# Use zip() to transpose a matrix (swap rows and columns).
# Print the original and the transposed version.
#
# Expected output:
# Original:
#   [1, 2, 3]
#   [4, 5, 6]
#   [7, 8, 9]
# Transposed:
#   (1, 4, 7)
#   (2, 5, 8)
#   (3, 6, 9)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 12 | MEDIUM-HARD
# ------------------------------------------------------------
# Use zip() to create consecutive pairs from ONE list.
# Then calculate the DIFFERENCE between each consecutive pair.
# Mark pairs where value went UP with (+) and DOWN with (-).
#
# Expected output:
# 10 -> 15: +5  (UP)
# 15 -> 8:  -7  (DOWN)
# 8  -> 20: +12 (UP)
# 20 -> 20: 0   (SAME)
# 20 -> 13: -7  (DOWN)

values = [10, 15, 8, 20, 20, 13]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 13 | MEDIUM-HARD
# ------------------------------------------------------------
# Use zip() to run a "parallel test" on two lists.
# Compare expected vs actual values.
# Print PASS or FAIL for each test.
# At the end print a summary.
#
# Expected output:
# Test 1: PASS  (expected=10,  got=10)
# Test 2: FAIL  (expected=20,  got=25)
# Test 3: PASS  (expected=30,  got=30)
# Test 4: FAIL  (expected=40,  got=38)
# Test 5: PASS  (expected=50,  got=50)
# ----------------------------
# Results: 3 passed, 2 failed

expected = [10, 20, 30, 40, 50]
actual   = [10, 25, 30, 38, 50]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 14 | HARD
# ------------------------------------------------------------
# Use zip() and zip_longest() to merge THREE student lists.
# Some students are missing from some lists (use "N/A").
# Print a full table and calculate each student's average
# (ignore "N/A" values when calculating average).
#
# Expected output:
# Name         Math    Science  English   Average
# ------------------------------------------------
# Alice          85         92       78     85.00
# Bob            90        N/A       88     89.00
# Charlie       N/A         75       95     85.00
# Diana          88         80      N/A     84.00

from itertools import zip_longest

names        = ["Alice", "Bob",  "Charlie", "Diana"]
math_scores  = [85,      90,     None,      88]
sci_scores   = [92,      None,   75,        80]
eng_scores   = [78,      88,     95,        None]

# YOUR CODE HERE:


# ------------------------------------------------------------
# EXERCISE 15 | HARD
# ------------------------------------------------------------
# Use zip() to implement a SLIDING WINDOW of size 3
# over a list of daily temperatures.
# For each window:
# - Print the three values
# - Print the average
# - Mark if the trend is RISING, FALLING, or MIXED
#   (RISING = each value higher than previous,
#    FALLING = each value lower than previous,
#    MIXED = neither)
# At the end print the window with the highest average.
#
# Expected output:
# Window 1: [12, 18, 15]  avg=15.0  MIXED
# Window 2: [18, 15, 22]  avg=18.3  MIXED
# Window 3: [15, 22, 25]  avg=20.7  RISING
# Window 4: [22, 25, 19]  avg=22.0  MIXED
# Window 5: [25, 19, 13]  avg=19.0  FALLING
# Window 6: [19, 13, 20]  avg=17.3  MIXED
# ----------------------------
# Hottest window: Window 4 with avg=22.0

temperatures = [12, 18, 15, 22, 25, 19, 13, 20]

# YOUR CODE HERE: