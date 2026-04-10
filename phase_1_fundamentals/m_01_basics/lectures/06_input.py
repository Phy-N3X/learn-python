# ============================================================
# MODULE 01 | LECTURE 06 - input()
# ============================================================
# What you will learn:
#   - What input() does
#   - How input() works
#   - input() always returns a string
#   - Converting input to other types
#   - Validating input
#   - Common patterns
#   - Common pitfalls
# ============================================================


# ------------------------------------------------------------
# PART 1: What is input()?
# ------------------------------------------------------------

# input() pauses the program and waits for the user to type
# When user presses ENTER - input() returns what was typed
# It ALWAYS returns a STRING - no matter what user types

# Basic usage - no prompt
# user_input = input()          # waits silently - bad practice

# With prompt - always provide a message!
# name = input("Enter your name: ")
# print("Hello,", name)

# For this lecture we will SIMULATE input() using variables
# so the code runs without waiting for you to type.
# In real programs replace the simulated value with input()

# SIMULATION pattern used throughout this lecture:
# Instead of:   name = input("Enter name: ")
# We write:     name = "Anna"   # simulated input
#               print("Enter name:", name)   # shows the prompt simulation

# This way you can run and study the code freely!


# ------------------------------------------------------------
# PART 2: input() Always Returns a String
# ------------------------------------------------------------

# This is the most important rule about input()!
# Even if user types a number - you get a STRING back

# Simulated inputs:
raw_age  = "25"          # what input() would return for "25"
raw_pi   = "3.14"        # what input() would return for "3.14"
raw_bool = "True"        # what input() would return for "True"

print(type(raw_age))     # <class 'str'>  ← NOT int!
print(type(raw_pi))      # <class 'str'>  ← NOT float!
print(type(raw_bool))    # <class 'str'>  ← NOT bool!

# This causes bugs if you forget!
a = "10"                 # simulated input
b = "20"                 # simulated input

print(a + b)             # "1020"  ← string concatenation, NOT addition!
print(int(a) + int(b))  # 30      ← correct: convert first!

# Always convert input to the type you need!


# ------------------------------------------------------------
# PART 3: Converting input() to Other Types
# ------------------------------------------------------------

# int() - convert to integer
raw = "42"                       # simulated input("Enter number: ")
number = int(raw)
print(number)                    # 42
print(type(number))              # <class 'int'>
print(number * 2)                # 84  ← now math works!

# float() - convert to float
raw = "3.14"                     # simulated input("Enter pi: ")
pi = float(raw)
print(pi)                        # 3.14
print(type(pi))                  # <class 'float'>
print(pi * 2)                    # 6.28

# bool() - tricky! bool("False") is True!
raw = "False"                    # simulated input
print(bool(raw))                 # True!  ← non-empty string = truthy
# We will handle proper bool input later

# Convert on the same line - common pattern
# age = int(input("Enter your age: "))
# Simulated:
age = int("25")
print(age)                       # 25
print(type(age))                 # <class 'int'>

# float on same line
# height = float(input("Enter height in meters: "))
# Simulated:
height = float("1.75")
print(height)                    # 1.75
print(type(height))              # <class 'float'>


# ------------------------------------------------------------
# PART 4: input() in Real Scenarios
# ------------------------------------------------------------

# Scenario 1: Simple greeting
# In real program:
# name = input("What is your name? ")
# Simulated:
name = "Anna"
print(f"Hello, {name}! Welcome to Python.")

# Scenario 2: Basic calculator
# In real program:
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# Simulated:
num1 = float("10.5")
num2 = float("4.5")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2:.2f}")

# Scenario 3: Age calculator
# In real program:
# birth_year = int(input("Enter your birth year: "))
# Simulated:
birth_year = int("2000")
current_year = 2025
age = current_year - birth_year
print(f"You are {age} years old.")

# Scenario 4: Temperature converter
# In real program:
# celsius = float(input("Enter temperature in Celsius: "))
# Simulated:
celsius = float("100")
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")

# Scenario 5: String manipulation from input
# In real program:
# sentence = input("Enter a sentence: ")
# Simulated:
sentence = "hello world python"
print(f"Original:   {sentence}")
print(f"Upper:      {sentence.upper()}")
print(f"Title:      {sentence.title()}")
print(f"Word count: {len(sentence.split())}")
print(f"Reversed:   {sentence[::-1]}")


# ------------------------------------------------------------
# PART 5: Stripping Input
# ------------------------------------------------------------

# Users often accidentally add spaces before/after their input
# Always strip() user input to be safe!

# Simulating input with accidental spaces:
raw_name = "  Anna  "         # user typed with spaces

# Without strip - spaces are included!
print(repr(raw_name))         # '  Anna  '
print(raw_name == "Anna")     # False!  ← bug!

# With strip - clean input
clean_name = raw_name.strip()
print(repr(clean_name))       # 'Anna'
print(clean_name == "Anna")   # True  ← correct!

# Best practice - always strip string input:
# name = input("Enter name: ").strip()
# Simulated:
name = "  Anna  ".strip()
print(name)                   # Anna

# Strip and convert in one line:
# age = int(input("Enter age: ").strip())
# Simulated:
age = int("  25  ".strip())
print(age)                    # 25
print(type(age))              # <class 'int'>


# ------------------------------------------------------------
# PART 6: Case-Insensitive Input
# ------------------------------------------------------------

# Users may type in different cases
# Always normalize case before comparing

# Simulated: user typed "YES" or "yes" or "Yes"
raw_answer = "YES"

# Without normalization - fragile:
print(raw_answer == "yes")      # False  ← bug if user types YES

# With normalization - robust:
answer = raw_answer.lower().strip()
print(answer == "yes")          # True   ← works for any case!

# Common patterns:
# answer = input("Continue? (yes/no): ").lower().strip()
# Simulated:
answer = "Yes".lower().strip()
print(answer)                   # yes

is_yes = answer == "yes"
print(is_yes)                   # True

# Multiple accepted values:
answer = "y"
is_confirmed = answer in ["yes", "y", "yeah", "yep", "sure"]
print(is_confirmed)             # True


# ------------------------------------------------------------
# PART 7: Handling Invalid Input with try/except
# ------------------------------------------------------------

# What happens when user types "abc" but you expect a number?
# int("abc") raises ValueError!

# Without error handling - program crashes:
# age = int(input("Enter age: "))  ← crashes if user types "abc"

# With try/except (we cover exceptions fully in Module 11):
def safe_int_input(prompt, simulated_value):
    """Safely convert input to int."""
    try:
        return int(simulated_value)
    except ValueError:
        print(f"Invalid input: '{simulated_value}' is not a number.")
        return None

# Valid input:
result = safe_int_input("Enter age: ", "25")
print(result)           # 25

# Invalid input:
result = safe_int_input("Enter age: ", "abc")
print(result)           # None  (after printing error message)

# Float version:
def safe_float_input(prompt, simulated_value):
    """Safely convert input to float."""
    try:
        return float(simulated_value)
    except ValueError:
        print(f"Invalid input: '{simulated_value}' is not a decimal number.")
        return None

result = safe_float_input("Enter price: ", "9.99")
print(result)           # 9.99

result = safe_float_input("Enter price: ", "nine")
print(result)           # None


# ------------------------------------------------------------
# PART 8: Input with Default Values
# ------------------------------------------------------------

# Sometimes you want a default if user presses ENTER without typing
# input() returns "" (empty string) when user just presses ENTER

# Simulated: user pressed ENTER (empty input)
raw = ""

# Using or for default value:
name = raw or "Anonymous"
print(name)             # Anonymous

# Simulated: user typed something
raw = "Anna"
name = raw or "Anonymous"
print(name)             # Anna

# With strip() to handle spaces:
# raw = input("Enter name (or press ENTER for Anonymous): ").strip()
# Simulated:
raw = "  ".strip()      # user typed only spaces
name = raw or "Anonymous"
print(name)             # Anonymous

# Default number:
raw = ""
try:
    age = int(raw) if raw else 18   # default age = 18
except ValueError:
    age = 18
print(age)              # 18


# ------------------------------------------------------------
# PART 9: Multiple Inputs on One Line
# ------------------------------------------------------------

# Sometimes you want user to enter multiple values at once
# Separated by spaces or commas

# Simulated: user types "10 20 30"
raw = "10 20 30"
numbers = raw.split()               # ["10", "20", "30"]
a, b, c = int(numbers[0]), int(numbers[1]), int(numbers[2])
print(a, b, c)                      # 10 20 30
print(a + b + c)                    # 60

# More elegant with map():
# map() applies a function to every element (preview of later topic)
raw = "10 20 30"
a, b, c = map(int, raw.split())
print(a, b, c)                      # 10 20 30

# Comma separated:
raw = "Anna,25,Warsaw"
name, age, city = raw.split(",")
name = name.strip()
age  = int(age.strip())
city = city.strip()
print(f"Name: {name}, Age: {age}, City: {city}")

# List of numbers from input:
raw = "1 2 3 4 5 6 7 8 9 10"
numbers = list(map(int, raw.split()))
print(numbers)                      # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(numbers))                 # 55
print(max(numbers))                 # 10


# ------------------------------------------------------------
# PART 10: input() Prompt Formatting
# ------------------------------------------------------------

# Good prompts make programs user-friendly
# Always make it clear what you expect

# Bad prompts:
# x = input("Input: ")        ← what should I type?
# n = input("Number? ")       ← what kind of number?

# Good prompts:
# name = input("Enter your full name: ")
# age  = input("Enter your age (18-99): ")
# temp = input("Enter temperature in Celsius (e.g. 36.6): ")
# ans  = input("Continue? (yes/no): ")

# Multi-line prompt for complex input:
prompt = (
    "\nPlease enter your details:"
    "\nFormat: FirstName LastName Age"
    "\nExample: Anna Kowalski 25"
    "\n> "
)
# raw = input(prompt)
# Simulated:
raw = "Anna Kowalski 25"
print(prompt + raw)     # shows what the interaction looks like

parts = raw.split()
first_name = parts[0]
last_name  = parts[1]
age        = int(parts[2])
print(f"Hello {first_name} {last_name}, you are {age} years old!")


# ------------------------------------------------------------
# PART 11: Common Pitfalls ⚠️
# ------------------------------------------------------------

# PITFALL 1: Forgetting to convert input
# raw = input("Enter number: ")   ← returns str!
# result = raw * 2                ← "1010" not 20!
raw = "10"
print(raw * 2)              # "1010"  ← string repetition!
print(int(raw) * 2)         # 20      ← correct!

# PITFALL 2: bool("False") is True!
raw = "False"
print(bool(raw))            # True!   ← non-empty string = truthy!
# Correct way to check boolean input:
is_active = raw.lower().strip() in ["true", "yes", "1", "y"]
print(is_active)            # False   ← correct!

# PITFALL 3: int() fails on float strings
raw = "3.14"
# print(int(raw))           # ValueError! "3.14" is not int format
print(float(raw))           # 3.14   ← use float() first
print(int(float(raw)))      # 3      ← then int() if needed

# PITFALL 4: Crashing on empty input
raw = ""
# print(int(raw))           # ValueError! can't convert empty string
age = int(raw) if raw.strip() else 0    # safe with default
print(age)                  # 0

# PITFALL 5: Not stripping whitespace
raw = "  25  "
# print(int(raw))           # ValueError on some systems!
print(int(raw.strip()))     # 25  ← always strip before converting

# PITFALL 6: Comparing string input with number
raw = "25"
# print(raw == 25)          # False! str != int
print(int(raw) == 25)       # True   ← convert first!


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ input()              - pauses program, waits for user
# ✅ input("prompt: ")    - always provide a clear prompt
# ✅ input() returns str  - ALWAYS, no matter what user types
# ✅ int(input())         - convert to int on same line
# ✅ float(input())       - convert to float on same line
# ✅ .strip()             - always strip user input
# ✅ .lower()             - normalize case for comparisons
# ✅ or "default"         - provide default for empty input
# ✅ try/except           - handle invalid input gracefully
# ✅ .split()             - multiple values from one input
# ✅ map(int, raw.split())- multiple numbers elegantly
# ⚠️  input() is ALWAYS str - convert before math/comparison
# ⚠️  bool("False") = True! - use .lower() in [...] instead
# ⚠️  int("3.14") fails    - use float() first, then int()
# ⚠️  int("") fails        - check for empty string first
# ⚠️  Always .strip()      - users add accidental spaces