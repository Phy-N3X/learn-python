# ============================================================
# MODULE 01 | EXERCISES 01 - Variables
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
name = "Mark"
age = 30
height = 1.81

print(name)
print(age)
print(height)



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
language = "Python"
print(language)

language = "Bioinformatics"
print(language)



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
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
a = b = c = 100

print(a)
print(b)
print(c)



# ------------------------------------------------------------
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
city, country, continent = "Gdańsk", "Poland", "Europe"

print(city)
print(country)
print(continent)



# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
first = 111
second = 999

print("Before: ", first, second)

first, second = second, first

print("After: ", first, second)



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
result = None
print(result)
print(type(result))

result = 42
print(result)
print(type(result))



# ------------------------------------------------------------
# EXERCISE 8 ✅ | MEDIUM
# ------------------------------------------------------------
users_age = 30
first_name = "Mark"
last_name = "Smith"
email_address = "mark@email.com"
is_logged_in = True



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
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
#2fast = "too fast"    # Variable name cannot start with a number
#my-var = 100          # Variable name cannot have a hyphen
#class = "Biology"     # Variable name cannot be a keyword
#user name = "Anna"    # Variable name cannot have spaces
#$price = 9.99         # Variable name cannot have special symbols

too_fast = "too fast"
my_var = 100
subject = "Biology"
user_name = "Anna"
dollar_price = 9.99



# ------------------------------------------------------------
# EXERCISE 14 ✅ | HARD
# ------------------------------------------------------------
profile_name = "Anna"
profile_age = 25
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