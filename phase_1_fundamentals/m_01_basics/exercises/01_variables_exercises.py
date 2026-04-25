# ============================================================
# MODULE 01 | EXERCISES 01 - Variables
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create three variables:
#   name    =  your name (string)
#   age     =  your age (integer)
#   height  =  your height in meters (float)
# Then print all three on separate lines.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("Exercise 1:")

name = "Mark"
age = 30
height = 1.81

print(name)
print(age)
print(height)



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create a variable called 'language' with value "Python"
# Print it, then change it to "Bioinformatics"
# Print it again.
# Expected output:
#   Python
#   Bioinformatics
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 2:")

language = "Python"
print(language)

language = "Bioinformatics"
print(language)



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Check and print the type of each variable below.
# Use type() function.
# Expected output: <class 'int'>, <class 'str'> etc.
#   x = 42
#   y = 3.14
#   z = "DNA"
#   q = True
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 3:")

x = 42
y = 3.14
z = "DNA"
q = True

print(type(x))
print(type(y))
print(type(z))
print(type(q))



# ------------------------------------------------------------
# EXERCISE 4 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Assign the value 100 to three variables at once:
# a, b and c
# Print all three.
# Expected output:
#   100
#   100
#   100
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 4:")

a = b = c = 100

print(a)
print(b)
print(c)



# ------------------------------------------------------------
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Use multiple assignment in one line to create:
#   city = "Gdansk"
#   country = "Poland"
#   continent = "Europe"
# Then print all three.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 5:")

city, country, continent = "Gdańsk", "Poland", "Europe"

print(city)
print(country)
print(continent)



# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
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
# CODE:
# ------------------------------------------------------------
print("\nExercise 6:")

first = 111
second = 999

print("Before: ", first, second)

first, second = second, first

print("After: ", first, second)



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
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
# CODE:
# ------------------------------------------------------------
print("\nExercise 7:")

result = None
print(result)
print(type(result))

result = 42
print(result)
print(type(result))



# ------------------------------------------------------------
# EXERCISE 8 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Below are badly named variables.
# Rewrite them using correct snake_case naming conventions.
# Just rename - keep the same values.

# UsersAge = 30
# FIRSTNAME = "Mark"
# last_Name = "Smith"
# emailADDRESS = "mark@email.com"
# is_logged_IN = True
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 8:")

users_age = 30
first_name = "Mark"
last_name = "Smith"
email_address = "mark@email.com"
is_logged_in = True



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Python is dynamically typed - a variable can change type.
# Create a variable x and assign these values one by one,
# printing the value and type after each assignment:
#   1. integer 10
#   2. float 3.14
#   3. string "hello"
#   4. boolean False
#   5. None
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 9:")

x = 10
print(type(x))

x = 3.14
print(type(x))

x = "hello"
print(type(x))

x = False
print(type(x))

x = None
print(type(x))



# ------------------------------------------------------------
# EXERCISE 10 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create variables for a student record:
#   student_name, student_age, student_gpa, is_active
# Assign any realistic values.
# Then reassign all of them in one line using multiple assignment.
# Print all values before and after.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 10:")

student_name = "Mark"
student_age = 30
student_gpa = 3.9
is_active = True

print("Before: ", student_name, student_age, student_gpa, is_active)

student_name, student_age, student_gpa, is_active = "John", 30, 4.5, False

print("After: ", student_name, student_age, student_gpa, is_active)



# ------------------------------------------------------------
# EXERCISE 11 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
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
# CODE:
# ------------------------------------------------------------
print("\nExercise 11:")

a = 5
b = 5
c = 500
d = 500

print(id(a))
print(id(b))
print(id(c))
print(id(d))

# a,b have same memory address, so do c,d



# ------------------------------------------------------------
# EXERCISE 12 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Predict the output before running the code.
# Write your prediction as a comment, then run and check.

#   x = 10
#   y = x
#   x = 20
# What is y here? Write prediction as comment: # y = ?
#   print(y)
#
#   a = [1, 2, 3]
#   b = a
#   a = [4, 5, 6]
# What is b here? Write prediction as comment: # b = ?
#   print(b)
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 12:")

x = 10
y = x
x = 20
# y has a value of 10
print(y)

a = [1, 2, 3]
b = a
a = [4, 5, 6]
# b has a value of [1, 2, 3]
print(b)



# ------------------------------------------------------------
# EXERCISE 13 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Without running the code first, find all the errors below.
# Write what each error is as a comment next to the line.
# Then fix all errors so the code runs correctly.

# 2fast = "too fast"
# my-var = 100
# class = "Biology"
# user name = "Anna"
# $price = 9.99
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
# 2fast = "too fast"    # Variable name cannot start with a number
# my-var = 100          # Variable name cannot have a hyphen
# class = "Biology"     # Variable name cannot be a keyword
# user name = "Anna"    # Variable name cannot have spaces
# $price = 9.99         # Variable name cannot have special symbols

too_fast = "too fast"
my_var = 100
subject = "Biology"
user_name = "Anna"
dollar_price = 9.99



# ------------------------------------------------------------
# EXERCISE 14 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
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
# CODE:
# ------------------------------------------------------------
print("\nExercise 14:")

profile_name = "Anna"
profile_age = 30
profile_gpa = 4.75
profile_height = 1.81
profile_is_student = True
profile_is_graduate = None

print("User profile:")
print("Age: ", profile_age)
print("Height: ", profile_height)
print("Gpa: ", profile_gpa)
print(profile_is_student)
print(profile_is_graduate)



# ------------------------------------------------------------
# EXERCISE 15 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Chain assignment puzzle.
# Trace through this code step by step.
# Before each print, write a comment with your prediction.
# Then run the code and verify.

#   a = 1
#   b = 2
#   c = 3
#
#   a, b, c = b, c, a
# Prediction: a=?, b=?, c=?
#   print(a, b, c)

#   a, b = a + b, a - b
# Prediction: a=?, b=?
#   print(a, b)
#
#   c = a
#   a = b
#   b = c
# Prediction: a=?, b=?
#   print(a, b)

# What is the final order of the original values 1, 2, 3?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 15:")

a = 1
b = 2
c = 3

a, b, c = b, c, a
# Prediction: a = 2, b = 3, c = 1
print(a, b, c)

a, b = a + b, a - b
# Prediction: a = 5, b = -1
print(a, b)

c = a
a = b
b = c
# Prediction: a = -1, b = 5
print(a, b)

# What is the final order of the original values 1, 2, 3?
# Prediction: a = -1, b = 5, c = 5
print(a, b, c)