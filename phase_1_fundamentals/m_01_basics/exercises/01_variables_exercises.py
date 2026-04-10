# ============================================================
# MODULE 01 | EXERCISES 01 - Variables
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Create three variables:
#   name     = your name (string)
#   age      = your age (integer)
#   height   = your height in meters (float)
# Then print all three on separate lines.



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Create a variable called 'language' with value "Python"
# Print it, then change it to "Bioinformatics"
# Print it again.
# Expected output:
#   Python
#   Bioinformatics



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Check and print the TYPE of each variable below.
# Use type() function.
# Expected: <class 'int'>, <class 'str'> etc.

x = 42
y = 3.14
z = "DNA"
q = True



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Assign the value 100 to three variables at once:
# a, b and c
# Print all three.
# Expected output:
#   100
#   100
#   100



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Use multiple assignment in ONE line to create:
#   city = "Gdansk"
#   country = "Poland"
#   continent = "Europe"
# Then print all three.



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create two variables:
#   first = 111
#   second = 999
# Swap their values WITHOUT using a third variable.
# Print both before and after the swap.
# Expected output:
#   Before: 111 999
#   After: 999 111



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a variable 'result' and assign None to it.
# Print it and its type.
# Then assign the value 42 to it.
# Print it and its type again.
# Expected output:
#   None
#   <class 'NoneType'>
#   42
#   <class 'int'>



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | MEDIUM
# ------------------------------------------------------------
# Below are BADLY named variables.
# Rewrite them using correct snake_case naming conventions.
# Just rename - keep the same values.

UsersAge = 30
FIRSTNAME = "Mark"
last_Name = "Smith"
emailADDRESS = "mark@email.com"
is_logged_IN = True



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Python is dynamically typed - a variable can change type.
# Create a variable x and assign these values one by one,
# printing the value AND type after each assignment:
#   1. integer 10
#   2. float 3.14
#   3. string "hello"
#   4. boolean False
#   5. None



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create variables for a student record:
#   student_name, student_age, student_gpa, is_active
# Assign any realistic values.
# Then reassign ALL of them in ONE line using multiple assignment.
# Print all values before and after.



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Investigate memory with id()
# Create:
#   a = 5
#   b = 5
#   c = 500
#   d = 500
# Print id() for all four variables.
# Are a and b pointing to the same object?
# Are c and d pointing to the same object?
# Write your observation as a comment.



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Predict the output BEFORE running the code.
# Write your prediction as a comment, then run and check.

x = 10
y = x
x = 20
# What is y here? Write prediction as comment: # y = ?
print(y)

a = [1, 2, 3]
b = a
a = [4, 5, 6]
# What is b here? Write prediction as comment: # b = ?
print(b)



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Without running the code first, find ALL the errors below.
# Write what each error is as a comment next to the line.
# Then fix ALL errors so the code runs correctly.

2fast = "too fast"
my-var = 100
class = "Biology"
user name = "Anna"
$price = 9.99



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Create a simple "profile" using only variables.
# Requirements:
#   - At least 6 variables describing a person
#   - Use correct types (str, int, float, bool)
#   - All names must follow snake_case
#   - One variable must be None (data not available yet)
#   - Print all variables with a descriptive label
# Example output format:
#   Name: Anna
#   Age: 25
#   GPA: 4.75
#   ...



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Chain assignment puzzle.
# Trace through this code step by step.
# Before each print, write a comment with your prediction.
# Then run the code and verify.

a = 1
b = 2
c = 3

a, b, c = b, c, a
# Prediction: a=?, b=?, c=?
print(a, b, c)

a, b = a + b, a - b
# Prediction: a=?, b=?
print(a, b)

c = a
a = b
b = c
# Prediction: a=?, b=?
print(a, b)

# Final question (write as comment):
# What is the final order of the original values 1, 2, 3?