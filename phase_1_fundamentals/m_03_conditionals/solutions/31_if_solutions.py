# ============================================================
# MODULE 03 | EXERCISES 31 - if
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
print("Exercise 1:")

temperature = 35

if temperature > 30:
    print("It's hot outside!")



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
print("\nExercise 2:")

x = 10

if x > 5:
    print("A")        # prediction: A

if x == 10:
    print("B")        # prediction: B

if x != 10:
    print("C")        # prediction: NOTHING

if x >= 10:
    print("D")        # prediction: D

if x <= 9:
    print("E")        # prediction: NOTHING

if x:
    print("F")        # prediction: F



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
print("\nExercise 3:")


age = 18

if age == 18:              # "=" instead of "=="
    print("Adult")

if age >= 18:              # lack of ":" symbol
    print("Can vote")

if age > 17:
    print("Not a minor")   # lack of indentation

if age < 100:              # "If" instead of "if"
    print("Not a centenarian")



# ------------------------------------------------------------
# EXERCISE 4 ✅ | EASY
# ------------------------------------------------------------
print("\nExercise 4:")

age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote!")



# ------------------------------------------------------------
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
is_raining = True
has_umbrella = False
temperature = 5

print("\nExercise 5:")

if is_raining:
    print("Take an umbrella")

if has_umbrella:
    print("You don't have umbrella")

if temperature < 10:
    print("Wear a jacket!")



# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
print("\nExercise 6:")

user_number = int(input("Enter a number: "))

if user_number > 0:
    print(f"{user_number} is positive")

if user_number < 0:
    print(f"{user_number} is negative")

if user_number == 0:
    print(f"{user_number} is zero")

if user_number  % 2 == 0:
    print(f"{user_number} is even")



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
score = 85
ph = 7.4
age = 25
temperature = 22

print("\nExercise 7:")

if 80 <= score <= 89:
    print("Grade: B")

if 7.35 <= ph <= 7.45:
    print("Normal blood pH")

if 18 <= age <= 65:
    print("Working age")

if 18 <= temperature <= 26:
    print("Comfortable temperature")



# ------------------------------------------------------------
# EXERCISE 8 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
correct_username = "admin"
correct_password = "python123"

print("\nExercise 8:")

user_login = input("Enter your login: ")
user_password = input("Enter your password: ")

if user_login == correct_username and user_password == correct_password:
    print("Login successful. Welcome, administrator!")



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
a = 15
b = 3
name = "Python"
items = ""

print("\nExercise 9:")

if a > b and a > 10:
    # prediction: prints "A is large and greater than b"
    print("A is large and greater than b")

if a % b == 0:
    # prediction: prints "a is divisible by b"
    print("a is divisible by b")

if name.startswith("Py") and len(name) > 4:
    # prediction: prints "Name starts with Py and is long enough"
    print("Name starts with Py and is long enough")

if not items:
    # prediction: prints "Items list is empty"
    print("Items list is empty")

if a > 10 or b > 10:
    # prediction: prints "At least one is greater than 10"
    print("At least one is greater than 10")



# ------------------------------------------------------------
# EXERCISE 10 ✅ | MEDIUM
# ------------------------------------------------------------
user_weight = float(input("Enter your weight [kg]: "))
user_height = float(input("Enter your height [m]: "))

bmi = user_weight / (user_height ** 2)

print("\nExercise 10:")

print(f"Your BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Underweight")

if 18.5 <= bmi < 25:
    print("Normal")

if 25 <= bmi < 30:
    print("Overweight")

if bmi >= 30:
    print("Obese")



# ------------------------------------------------------------
# EXERCISE 11 ✅ | MEDIUM
# ------------------------------------------------------------
print("\nExercise 11:")

user_dna_base = input("Enter DNA base (A | T | C | G): ")
dna_base = user_dna_base.upper()

print("Base: ", dna_base)

if dna_base not in "ATCG":
    print("Invalid base entered.\nValid bases: A, T, C, G only.")

if dna_base == "A":
    print("Complementary base: T")
if dna_base == "T":
    print("Complementary base: A")
if dna_base == "G":
    print("Complementary base: C")
if dna_base == "C":
    print("Complementary base: G")



# ------------------------------------------------------------
# EXERCISE 12 ✅ | MEDIUM
# ------------------------------------------------------------
print("\nExercise 12:")

user_number = int(input("Enter a number: "))

print("===== NUMBER PROPERTIES ANALYZER =====")

if user_number < 0:
    print(f"→ {user_number} is negative number")
if user_number == 0:
    print(f"→ {user_number} is equal zero")
if user_number > 0:
    print(f"→ {user_number} is positive number")

if user_number % 2 == 0:
    print(f"→ {user_number} is even number")
if user_number % 2 != 0:
    print(f"→ {user_number} is odd number")

if user_number % 3 == 0:
    print(f"→ {user_number} is divisible by 3")
if user_number % 3 != 0:
    print(f"→ {user_number} is not divisible by 3")

if user_number % 5 == 0:
    print(f"→ {user_number} is divisible by 5")
if user_number % 5 != 0:
    print(f"→ {user_number} is not divisible by 5")

if (user_number % 3 == 0) and (user_number % 5 ==0):
    print(f"→ {user_number} is divisible by both 3 and 5 (therefore divisible by 15 too)")
if not (user_number % 3 == 0) and not (user_number % 5 == 0):
    print(f"→ {user_number} is not divisible by both 3 and 5 (therefore is not divisible by 15)")

if ((user_number ** 0.5) ** 2) == user_number:
    print(f"→ {user_number} is a perfect square")
if ((user_number ** 0.5) ** 2) != user_number:
    print(f"→ {user_number} is not a perfect square")

if 1 <= user_number <= 100:
    print(f"→ {user_number} is between 1 and 100")

print("=" * 38)



# ------------------------------------------------------------
# EXERCISE 13 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
print("\nExercise 13:")

protein_alphabet = "ACDEFGHIKLMNPQRSTVWY"
user_protein_sequence = input("Enter protein sequence: ")

print("===== PROTEIN SEQUENCE ANALYSER =====")
print("Sequence length: ", len(user_protein_sequence))
if len(user_protein_sequence) < 10:
    print("Length category: short")

if 10 <= len(user_protein_sequence) <= 100:
    print("Length category: medium")

if len(user_protein_sequence) > 100:
    print("Length category: long")

if user_protein_sequence.isupper() :
    print("All characters valid")

if  user_protein_sequence.startswith("M"):
    print("Protein starts with methionine (M)")

if not user_protein_sequence.startswith("M"):
    print("Protein does not starts with methionine (M)")

if "C" in user_protein_sequence:
    print("Protein contains cysteine (C)")

if "C" not in user_protein_sequence:
    print("Protein does not contain cysteine (C)")

print("=" * 37)



# ------------------------------------------------------------
# EXERCISE 14 ✅ | HARD
# ------------------------------------------------------------
print("\nExercise 14:")

user_temperature = float(input("Enter temperature: "))
user_unit = input("Enter unit (C/F/K): ")

celsius_to_fahrenheit = (user_temperature * 9/5) + 32
celsius_to_kelvin = user_temperature + 273.15
fahrenheit_to_celsius = (celsius_to_fahrenheit - 32) * 5/9
fahrenheit_to_kelvin = (celsius_to_fahrenheit + 459.67) * 5/9
kelvin_to_celsius = celsius_to_kelvin - 273.15
kelvin_to_fahrenheit = celsius_to_kelvin * 9/5 - 459.67

print("==== CONVERSION ====")

if user_unit.upper() not in "CFK":
    print("Invalid unit!\nUnit must be C, F or K")

if user_unit.upper() == "C":
    print(f"Celsius:\t{user_temperature:.2f} °C")
    print(f"Fahrenheit:\t{celsius_to_fahrenheit:.2f} °F")
    print(f"Kelvin:\t{celsius_to_kelvin:.2f} K")

if user_unit.upper() == "F":
    print(f"Celsius:\t{fahrenheit_to_celsius:.2f} °C")
    print(f"Fahrenheit:\t{user_temperature:.2f} °F")
    print(f"Kelvin:\t{fahrenheit_to_kelvin:.2f} K")

if user_unit.upper() == "K":
    print(f"Celsius:\t{kelvin_to_celsius:.2f} °C")
    print(f"Fahrenheit:\t{kelvin_to_fahrenheit:.2f} °F")
    print(f"Kelvin:\t{user_temperature:.2f} K")

print("== CLASSIFICATION ==")

if user_temperature < -273.15:
    print("Impossible (below absolute zero)!")
if -273.15 <= user_temperature <= -89:
    print("Extremely cold (record: -89°C Antarctica)")
if -89 <= user_temperature <= 0:
    print("Freezing")
if 0 <= user_temperature <= 20:
    print("Cold")
if 20 <= user_temperature <= 30:
    print("Comfortable")
if 30 <= user_temperature <= 40:
    print("Hot")
if user_temperature > 40:
    print("Dangerously hot")

print("=" * 20)



# ------------------------------------------------------------
# EXERCISE 15 ✅ | HARD
# ------------------------------------------------------------
print("\nExercise 15:")

user_weight = float(input("Enter your weight [kg]: "))

base_intake = user_weight * 0.033
intake_sum = base_intake

user_activity = int(input("Enter your activity (1/2/3): "))

if user_activity == 2:
    intake_sum += 0.5
    print("You're active - great! Stay hydrated during exercise.")

if user_activity == 3:
    intake_sum += 1.0
    print("You're active - great! Stay hydrated during exercise.")

is_summer = input("Is it summer? (yes/no): ")
summer_bonus = 0.0

if is_summer.lower() in ["yes", "y", "yeah", "of course", "yea", "duh"]:
    summer_bonus = 0.5
    intake_sum += summer_bonus
    print("Hot weather increases water loss through sweat.")

is_drinking_coffee = input("Do you drink coffee? (yes/no): ")
user_cups = 0

if is_drinking_coffee.lower() in ["yes", "y", "yeah", "of course", "yea", "duh"]:
    print("Coffee is a mild diuretic - extra water helps!")
    user_cups = int(input("How many cups of coffee do you drink: "))
    intake_sum += user_cups * 0.3

is_sick = input("Are you sick or have fever? (yes/no): ")

if is_sick.lower() in ["yes", "y", "yeah", "of course", "yea", "duh"]:
    intake_sum += 1.0

print("\n===== WATER INTAKE REPORT =====")
print(f"Base intake: \t\t{base_intake:.2f} L ({user_weight:.0f} kg * 0.033)")

if user_activity == 2:
    print(f"Activity bonus: \t+0.50 L")

if user_activity == 3:
    print(f"Activity bonus: \t+1.00 L")

if summer_bonus:
    print(f"Summer bonus: \t\t+{summer_bonus:.2f} L")

if user_cups > 0:
    print(f"Coffee bonus: \t\t+{user_cups * 0.3:.2f} L ({user_cups} cups)")

print(f"Total recommended: \t{intake_sum:.2f} L")
print()

if intake_sum <= 2.0:
    print("Water intake too low (avg: 2.0L)")
else:
    print("Above average daily intake (avg: 2.0L)")

print("=" * 31)