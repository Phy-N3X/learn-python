# ============================================================
# MODULE 03 | EXERCISES 32 - if / else
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
#print("Exercise 1:")
#
#temperature = 20
#
#if temperature > 30:
#    print("It's hot! Stay hydrated.")
#else:
#    print("The temperature is comfortable.")



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
#print("\nExercise 2:")
#
#a = 10
#b = 20
#
#if a > b:
#    print("A")          # prediction: False
#else:
#    print("B")          # prediction: prints "B"
#
#if a != b:
#    print("C")          # prediction: prints "C"
#else:
#    print("D")          # prediction: False
#
#if a == 10 and b == 10:
#    print("E")          # prediction: False
#else:
#    print("F")          # prediction: prints "F"
#
#if not a:
#    print("G")          # prediction: False
#else:
#    print("H")          # prediction: prints "H"
#
#x = ""
#if x:
#    print("I")          # prediction: False
#else:
#    print("J")          # prediction: prints "J"



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
#print("\nExercise 3:")
#
#score = 75
#
#if score >= 50:           # lack of ":" symbol
#    print("Passed")
#else:                     # "Else" instead of "else"
#    print("Failed")
#
#if score > 100:
#    print("Perfect")
#else:                     # else cannot have condition
#    print("Invalid")
#
#if score == 75:
#    print("Exactly 75")
#else:
#    print("Not 75")       # lack of indentation



# ------------------------------------------------------------
# EXERCISE 4 ✅ | EASY
# ------------------------------------------------------------
#print("\nExercise 4:")
#
#user_number = int(input("Enter a number: "))
#
#if user_number > 0:
#    print(f"{user_number} is positive number.")
#else:
#    print(f"{user_number} is negative number.")
#
#print(f"Number entered: {user_number}")



# ------------------------------------------------------------
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
#print("\nExercise 5:")
#
#user_number = int(input("Enter a number: "))
#
#if user_number % 2 == 0:
#    print(f"{user_number} is EVEN (remainder: {user_number % 2})")
#else:
#    print(f"{user_number} is ODD (remainder: {user_number % 2})")



# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
#print("\nExercise 6:")
#
#correct_login = "admin"
#correct_password = "python123"
#
#user_login = input("Enter a login: ")
#user_password = input("Enter a password: ")
#
#if user_login == correct_login and user_password == correct_password:
#    print("Login successful! Welcome, administrator!")
#    print("Access level: ADMINISTRATOR")
#else:
#    print("Login failed. Invalid credentials.")
#    print("Please try again.")



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
#print("\nExercise 7:")
#
#balance = 1000.00
#
#print("=== ATM ===")
#print(f"Your balance: {balance:.2f} PLN")
#
#user_withdrawal = float(input("Enter withdrawal amount: "))
#
#if user_withdrawal <= balance:
#    print("Withdrawal successful!")
#    print(f"Dispensed: {user_withdrawal:.2f} PLN")
#    print(f"Remaining balance: {balance - user_withdrawal:.2f} PLN")
#else:
#    print("Insufficient funds!")
#    print(f"Requested: {user_withdrawal:.2f} PLN")
#    print(f"Available: {balance:.2f} PLN")
#    print(f"Shortfall: {user_withdrawal - balance:.2f} PLN")



# ------------------------------------------------------------
# EXERCISE 8 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
#print("\nExercise 8:")
#
#user_sequence = input("Enter a nucleotide sequence: ").upper()
#
#if user_sequence:
#    if "U" in user_sequence:
#        print("Type: RNA")
#        print("Contains uracil (U): Yes")
#    else:
#        print("Type: DNA")
#        print("Contains uracil (U): No")
#else:
#    print("No sequence entered!")
#
#print("Sequence length: ", len(user_sequence))



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
#print("\nExercise 9:")
#
#x = 0
#y = 10
#name = "Python"
#
#if x:
#    # prediction: False
#    print("x is truthy")
#else:
#    # prediction: prints "x is falsy"
#    print("x is falsy")
#
#if y > 5 and name == "Python":
#    # prediction: prints "Both conditions met"
#    print("Both conditions met")
#else:
#    # prediction: False
#    print("At least one condition failed")
#
#if not name:
#    # prediction: False
#    print("Name is empty")
#else:
#    # prediction: prints "Name is: {name}"
#    print(f"Name is: {name}")
#
#result = y > x
#if result:
#    # prediction: prints "y is greater than x"
#    print("y is greater than x")
#else:
#    # prediction: False
#    print("y is not greater than x")



# ------------------------------------------------------------
# EXERCISE 10 ✅ | MEDIUM
# ------------------------------------------------------------
#print("\nExercise 10:")
#
#ticket_price = 0
#
#user_age = int(input("Enter your age: "))
#
#if user_age >= 18:
#    if 18 <= user_age <= 64:
#        ticket_price = 35
#        print("Category: Adult")
#    else:
#        ticket_price = 18
#        print("Category: Senior")
#else:
#    print("Category: Reduced")
#
#    if user_age < 5:
#        ticket_price = 0
#    else:
#        if 5 <= user_age <= 12:
#            ticket_price = 15
#        else:
#            if 13 <= user_age <= 17:
#                ticket_price = 20
#
#print(f"Price {ticket_price} PLN")



# ------------------------------------------------------------
# EXERCISE 11 ✅ | MEDIUM
# ------------------------------------------------------------
#print("\nExercise 11:")
#
#user_temperature = float(input("Enter body temperature (°C): "))
#
#print("Normal body temperature: 36.1 - 37.2")
#print(f"Temperature: {user_temperature:.1f}°C")
#
#if 36.1 <= user_temperature <= 37.2:
#    print("Status: Normal temperature")
#else:
#    if user_temperature < 36.1:
#        print("Status: Hypothermia risk - seek medical advice!")
#        print(f"Below normal by: {(user_temperature - 36.1):.1f}°C")
#    else:
#        if user_temperature > 37.2:
#            print("Status: Fever detected - seek medical advice!")
#            print(f"Above normal by: {(user_temperature - 37.2):.1f}°C")



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
#print("\nExercise 12:")
#
#first_number = int(input("Enter first number: "))
#second_number = int(input("Enter second number: "))
#
#print()
#
#if first_number == second_number:
#    print("They're equal!")
#else:
#    if first_number > second_number:
#        print(f"{first_number} is greater than {second_number}")
#    else:
#        print(f"{first_number} is less than {second_number}")
#
#print(f"Sum: {first_number + second_number}")
#print(f"Division: {first_number} / {second_number} = {(first_number / second_number):.2f}")


# Print ALL of the following using if/else statements:
# 1. Which is larger (or if they're equal)
# 2. Their sum and which range it falls in:
#    sum < 0 → "Negative sum"
#    sum == 0 → "Zero sum"
#    sum > 0 → "Positive sum"
# 3. The larger number divided by the smaller
#    (only if smaller != 0, otherwise print "Cannot divide by zero")
# 4. Whether both numbers have the same sign
#    (both positive, both negative, or mixed)


# Example interaction:
# Enter first number: 8
# Enter second number: -3
#   Comparison: 8 is greater than -3
#   Sum: 5 → Positive sum
#   Division: 8 / -3 = -2.67
#   Signs: Mixed (one positive, one negative)



# ------------------------------------------------------------
# EXERCISE 13 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
#print("\nExercise 13:")
#
#user_sequence = input("Enter protein sequence: ")
#user_da_or_kda = input("Display in Da or kDa: ").lower()
#
#weight_Da = len(user_sequence) * 110
#weight_kDa = weight_Da / 1000
#
#if not user_sequence:
#    print("Invalid: empty sequence")
#else:
#    if not user_sequence.isalpha():
#        print("Invalid: sequence contains numbers")
#    else:
#        if user_da_or_kda == "da":
#            print(f"Estimated weight: {weight_Da} Da")
#        else:
#            if user_da_or_kda == "kda":
#                print(f"Estimated weight: {weight_kDa} kDa")
#            else:
#                print(f"Command unknown: {user_da_or_kda}")
#
#print()
#print(f"Sequence: {user_sequence}")
#print(f"Length: {len(user_sequence)} amino acids")
#
#if weight_kDa < 10:
#    print("Classification: Small peptide")
#else:
#    if 10 <= weight_kDa <= 100:
#        print("Classification: Average protein")
#    else:
#        print("Classification: Large protein")



# ------------------------------------------------------------
# EXERCISE 14 ✅ | HARD
# ------------------------------------------------------------
#print("\nExercise 14:")
#
#user_monthly_income = float(input("Monthly income: "))
#user_monthly_expenses = float(input("Monthly expenses: "))
#user_requested_loan_amount = float(input("Loan amount: "))
#user_employment_status = input("Employment status (employed / self-employed / unemployed): ")
#
#disposable_income = user_monthly_income - user_monthly_expenses
#maximum_eligible_loan = disposable_income * 36
#
#print()
#print("===== LOAN DECISION REPORT =====")
#
#print(f"Disposable income: {disposable_income} PLN/month")
#print(f"Maximum eligible loan: {maximum_eligible_loan} PLN")
#print(f"Requested loan: {user_requested_loan_amount} PLN")
#
#if disposable_income > 0 and user_requested_loan_amount < maximum_eligible_loan and user_employment_status in ["employed", "self-employed"]:
#    print("Status: ACCEPTED")
#else:
#    print("Status: DENIED")
#
#if user_employment_status == "self-employed":
#    print("Interest rate: 6.325%")
#    print(f"Estimated monthly repayment: {user_requested_loan_amount * (0.06325 / 12) / (1 - (1 + 0.06325 / 12) ** -36):.2f} PLN")
#
#if user_employment_status == "employed":
#    print("Interest rate: 5.50%")
#    print(f"Estimated monthly repayment: {user_requested_loan_amount * (0.055 / 12) / (1 - (1 + (0.055 / 12)) ** -36):.2f} PLN")
#
#print("=" * 32)



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a scientific unit converter with validation.
#
# Ask the user:
# 1. What they want to convert:
#    "temp" → temperature
#    "mass" → mass
#    "dist" → distance
#    anything else → "Unknown conversion type"
#
# 2. Based on their choice, ask for value and direction.
#
# Temperature conversions:
# C→F: (C * 9/5) + 32
# F→C: (F - 32) * 5/9
# C→K: C + 273.15
# K→C: K - 273.15
# Validate: Kelvin cannot be below 0, Celsius cannot be below -273.15
#
# Mass conversions:
# kg→g:  * 1000
# g→kg:  / 1000
# kg→lb: * 2.20462
# lb→kg: / 2.20462
# Validate: mass cannot be negative
#
# Distance conversions:
# m→km:  / 1000
# km→m:  * 1000
# m→mi:  * 0.000621371
# mi→m:  / 0.000621371
# Validate: distance cannot be negative
#
# For each conversion:
# - Validate the input value FIRST using if/else
# - If invalid → print specific error and stop
# - If valid → convert and print result with 4 decimal places
# - Also print if result is above/below a meaningful threshold:
#   temp: above/below human body temperature (37°C equivalent)
#   mass: above/below 1kg equivalent
#   dist: above/below 1km equivalent
#
# Example interaction:
# What to convert? (temp/mass/dist): temp
# Enter value: -300
# Enter unit (C/F/K): C
# ❌ Invalid: -300°C is below absolute zero (-273.15°C)
#
# What to convert? (temp/mass/dist): mass
# Enter value: 2500
# Enter unit (kg/g/lb): g
# Convert to (kg/lb): kg
# 2500.0000 g = 2.5000 kg
# Above 1kg threshold
# ============================================================