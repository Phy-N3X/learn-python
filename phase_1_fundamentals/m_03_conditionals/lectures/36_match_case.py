# ============================================================
# MODULE 03 | LECTURE 36 - match / case
# ============================================================
# What you will learn:
# - What match/case is and why it was introduced
# - Basic syntax and structure
# - Matching literal values
# - Matching multiple values in one case
# - The wildcard case (_)
# - Matching with conditions (guards)
# - Matching sequences and tuples
# - Matching with 'as' keyword
# - match/case vs if/elif/else - when to use which
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is match/case?
# ------------------------------------------------------------

# match/case was introduced in Python 3.10 (released 2021).
# It is Python's version of the "switch/case" statement
# found in many other languages (Java, C, JavaScript, etc.)
#
# ⚠ IMPORTANT: match/case requires Python 3.10 or newer!
# Check your version: python --version
# If you have 3.9 or older → use if/elif/else instead.
#
# Why was it introduced?
# Long chains of if/elif/else for checking one variable
# against many specific values are:
# - Repetitive (you write the variable name every time)
# - Harder to read than necessary
# - Slower (Python checks each elif condition)
#
# match/case solves this elegantly.
#
# Real life analogy:
# ┌─────────────────────────────────────────────────┐
# │ Look at the traffic light color:                │
# │   Red    → Stop                                 │
# │   Yellow → Slow down                            │
# │   Green  → Go                                   │
# │   Any other → Unknown signal                    │
# └─────────────────────────────────────────────────┘
#
# With if/elif:
# if color == "red":
#     stop()
# elif color == "yellow":
#     slow_down()
# elif color == "green":
#     go()
# else:
#     unknown()
#
# With match/case:
# match color:
#     case "red":
#         stop()
#     case "yellow":
#         slow_down()
#     case "green":
#         go()
#     case _:
#         unknown()
#
# Both do the same thing.
# match/case is cleaner when checking one value against many options.

# ------------------------------------------------------------
# PART 2: Basic syntax
# ------------------------------------------------------------

# Syntax:
#     match subject:
#         case pattern_1:
#             code to run if pattern_1 matches
#         case pattern_2:
#             code to run if pattern_2 matches
#         case _:
#             code to run if nothing matches (wildcard/default)
#
# Rules:
# 1. Start with 'match' followed by the value to examine
# 2. Each 'case' defines a pattern to match against
# 3. The body of each case must be indented (4 spaces)
# 4. Cases are checked TOP TO BOTTOM
# 5. ONLY the FIRST matching case runs (like elif)
# 6. 'case _:' is the wildcard - matches ANYTHING (like else)
# 7. If no case matches and no wildcard → nothing happens
# 8. No 'break' needed - Python exits after first match

# Simplest possible example:

day = "Monday"

match day:
    case "Monday":
        print("Start of the work week")
    case "Friday":
        print("Almost the weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend! 🎉")
    case _:
        print(f"Regular day: {day}")

# Output: Start of the work week

# Let's try with Saturday:

day = "Saturday"

match day:
    case "Monday":
        print("Start of the work week")
    case "Friday":
        print("Almost the weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend! 🎉")
    case _:
        print(f"Regular day: {day}")

# Output: It's the weekend! 🎉

# And with an unexpected value:

day = "Holiday"

match day:
    case "Monday":
        print("Start of the work week")
    case "Friday":
        print("Almost the weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend! 🎉")
    case _:
        print(f"Regular day: {day}")

# Output: Regular day: Holiday

# ------------------------------------------------------------
# PART 3: Matching literal values
# ------------------------------------------------------------

# match/case works with all basic types:
# strings, integers, floats, booleans, None

# Matching integers:

status_code = 404

match status_code:
    case 200:
        print("✅ 200 OK - Request successful")
    case 201:
        print("✅ 201 Created - Resource created")
    case 301:
        print("↪ 301 Moved Permanently")
    case 302:
        print("↪ 302 Found - Temporary redirect")
    case 400:
        print("❌ 400 Bad Request")
    case 401:
        print("❌ 401 Unauthorized - Login required")
    case 403:
        print("❌ 403 Forbidden - Access denied")
    case 404:
        print("❌ 404 Not Found - Page doesn't exist")
    case 500:
        print("🔥 500 Internal Server Error")
    case _:
        print(f"Unknown status code: {status_code}")

# Output: ❌ 404 Not Found - Page doesn't exist

# Matching floats:

ph = 7.0

match ph:
    case 7.0:
        print("Perfectly neutral (pure water)")
    case 0.0:
        print("Maximum acidity")
    case 14.0:
        print("Maximum alkalinity")
    case _:
        print(f"pH value: {ph}")

# Output: Perfectly neutral (pure water)

# Matching None:

result = None

match result:
    case None:
        print("No result available")
    case 0:
        print("Result is zero")
    case _:
        print(f"Result: {result}")

# Output: No result available

# Matching booleans:
# ⚠ Note: True == 1 and False == 0 in Python
# This can cause unexpected behavior with integers and booleans

value = True

match value:
    case True:
        print("Value is True")
    case False:
        print("Value is False")
    case _:
        print("Other value")

# Output: Value is True

# ------------------------------------------------------------
# PART 4: Matching multiple values in one case (OR patterns)
# ------------------------------------------------------------

# Use the pipe '|' operator to match multiple values
# in a single case block.
# This replaces long 'or' chains in if/elif.

# Example 1: Days of the week

day = "Wednesday"

match day:
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print(f"{day} is a weekday 💼")
    case "Saturday" | "Sunday":
        print(f"{day} is a weekend day 🎉")
    case _:
        print(f"'{day}' is not a valid day name")

# Output: Wednesday is a weekday 💼

# Example 2: Vowels and consonants

letter = input("Enter a letter: ").lower()

match letter:
    case "a" | "e" | "i" | "o" | "u":
        print(f"'{letter}' is a vowel")
    case "b" | "c" | "d" | "f" | "g" | "h" | "j" | "k" | "l" | "m" \
       | "n" | "p" | "q" | "r" | "s" | "t" | "v" | "w" | "x" | "y" | "z":
        print(f"'{letter}' is a consonant")
    case _:
        print(f"'{letter}' is not a letter")

# Example 3: Error categories

error_code = int(input("Enter error code: "))

match error_code:
    case 100 | 101 | 102:
        print("Informational response")
    case 200 | 201 | 202 | 204:
        print("Success response ✅")
    case 301 | 302 | 303 | 307 | 308:
        print("Redirection response ↪")
    case 400 | 401 | 403 | 404 | 405 | 422 | 429:
        print("Client error response ❌")
    case 500 | 502 | 503 | 504:
        print("Server error response 🔥")
    case _:
        print(f"Unknown or non-standard code: {error_code}")

# ------------------------------------------------------------
# PART 5: The wildcard case (_)
# ------------------------------------------------------------

# 'case _:' is the wildcard pattern.
# It matches ANYTHING and is used as the default/fallback.
# It must ALWAYS be the LAST case.
# It's optional - if omitted and nothing matches, nothing happens.

# Example WITH wildcard:

command = "fly"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
    case _:
        print(f"Unknown command: '{command}'")    # catches "fly"

# Output: Unknown command: 'fly'

# Example WITHOUT wildcard (nothing happens if no match):

command = "fly"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case "pause":
        print("Pausing...")
# No output - "fly" doesn't match anything, no wildcard

# The wildcard variable '_' is special:
# It's a throwaway variable name. Python convention says
# "I matched this but I don't care about its value".
# You CANNOT use '_' inside the case body to get the value.

# If you WANT to use the unmatched value, use a variable name:

command = "dance"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case unknown_command:            # captures the value!
        print(f"Unknown: '{unknown_command}'")

# Output: Unknown: 'dance'
# Here 'unknown_command' captures the value of command.
# This is different from '_' which discards it.

# ------------------------------------------------------------
# PART 6: Guards - adding conditions to cases
# ------------------------------------------------------------

# You can add an 'if' condition to any case.
# This is called a GUARD.
# The case only matches if BOTH the pattern AND the guard are True.
#
# Syntax:
#     case pattern if condition:
#         code

# Example 1: Categorizing numbers

number = int(input("Enter a number: "))

match number:
    case 0:
        print("Zero")
    case n if n > 0 and n % 2 == 0:
        print(f"{n} is positive and even")
    case n if n > 0:
        print(f"{n} is positive and odd")
    case n if n < 0 and n % 2 == 0:
        print(f"{n} is negative and even")
    case n if n < 0:
        print(f"{n} is negative and odd")

# Notice: 'n' in each case captures the value of 'number'
# Then the 'if' guard adds an additional condition.

# Example 2: Score with grade and bonus

score = 87
bonus_points = 5

match score:
    case s if s + bonus_points >= 90:
        print(f"Grade: A (with bonus: {s + bonus_points})")
    case s if s >= 80:
        print(f"Grade: B - Score: {s}")
    case s if s >= 70:
        print(f"Grade: C - Score: {s}")
    case s if s >= 60:
        print(f"Grade: D - Score: {s}")
    case _:
        print(f"Grade: F - Score: {score}")

# Output: Grade: A (with bonus: 92)

# Example 3: Temperature with range guards

temp = float(input("Enter temperature: "))

match temp:
    case t if t < -273.15:
        print("Impossible - below absolute zero!")
    case t if t < 0:
        print(f"{t}°C - Below freezing")
    case t if t < 20:
        print(f"{t}°C - Cold")
    case t if t < 30:
        print(f"{t}°C - Comfortable")
    case t if t < 40:
        print(f"{t}°C - Hot")
    case t:
        print(f"{t}°C - Dangerously hot")

# ------------------------------------------------------------
# PART 7: Matching sequences (tuples and lists)
# ------------------------------------------------------------

# match/case can match against the STRUCTURE of sequences.
# This is one of the most powerful features.
# You can match on length, specific values, or capture elements.

# Example 1: Matching tuples by content

point = (0, 0)

match point:
    case (0, 0):
        print("Origin point")
    case (x, 0):
        print(f"Point on X-axis at x={x}")
    case (0, y):
        print(f"Point on Y-axis at y={y}")
    case (x, y):
        print(f"Point at ({x}, {y})")

# Output: Origin point

point = (5, 0)
match point:
    case (0, 0):
        print("Origin point")
    case (x, 0):
        print(f"Point on X-axis at x={x}")    # matches! x captures 5
    case (0, y):
        print(f"Point on Y-axis at y={y}")
    case (x, y):
        print(f"Point at ({x}, {y})")

# Output: Point on X-axis at x=5

point = (3, 7)
match point:
    case (0, 0):
        print("Origin point")
    case (x, 0):
        print(f"Point on X-axis at x={x}")
    case (0, y):
        print(f"Point on Y-axis at y={y}")
    case (x, y):
        print(f"Point at ({x}, {y})")         # matches! captures both

# Output: Point at (3, 7)

# Example 2: Matching sequences by length

data = [1, 2, 3]

match data:
    case []:
        print("Empty list")
    case [x]:
        print(f"Single element: {x}")
    case [x, y]:
        print(f"Two elements: {x} and {y}")
    case [x, y, z]:
        print(f"Three elements: {x}, {y}, {z}")    # matches!
    case [first, *rest]:
        print(f"First: {first}, rest: {rest}")

# Output: Three elements: 1, 2, 3

data = [10, 20, 30, 40, 50]
match data:
    case []:
        print("Empty list")
    case [x]:
        print(f"Single element: {x}")
    case [x, y]:
        print(f"Two elements: {x} and {y}")
    case [x, y, z]:
        print(f"Three elements: {x}, {y}, {z}")
    case [first, *rest]:
        print(f"First: {first}, rest: {rest}")     # matches!

# Output: First: 10, rest: [20, 30, 40, 50]

# Example 3: Matching DNA codons as tuples

codon = ("A", "T", "G")

match codon:
    case ("A", "T", "G"):
        print("START codon - Methionine (Met)")
    case ("T", "A", "A") | ("T", "A", "G") | ("T", "G", "A"):
        print("STOP codon")
    case ("G", "C", base):
        print(f"Alanine (Ala) - GC{base}")
    case (b1, b2, b3):
        print(f"Codon: {b1}{b2}{b3}")

# Output: START codon - Methionine (Met)

# ------------------------------------------------------------
# PART 8: Matching with 'as' keyword
# ------------------------------------------------------------

# The 'as' keyword lets you capture the matched value
# while still matching a specific pattern.
# This is useful when you want to match AND use the value.

# Syntax:
#     case pattern as name:

# Example 1: Capture while matching

command = "quit"

match command:
    case "start" | "begin" as cmd:
        print(f"Starting system... (command was: '{cmd}')")
    case "stop" | "quit" | "exit" as cmd:
        print(f"Stopping system... (command was: '{cmd}')")    # matches!
    case cmd:
        print(f"Unknown command: '{cmd}'")

# Output: Stopping system... (command was: 'quit')

# Example 2: Capture tuple elements with 'as'

point = (3, 4)

match point:
    case (0, 0) as origin:
        print(f"At origin: {origin}")
    case (x, 0) as p:
        print(f"On X-axis: {p}")
    case (0, y) as p:
        print(f"On Y-axis: {p}")
    case (x, y) as p:
        distance = (x**2 + y**2) ** 0.5
        print(f"Point {p} is {distance:.2f} from origin")    # matches!

# Output: Point (3, 4) is 5.00 from origin

# ------------------------------------------------------------
# PART 9: match/case vs if/elif/else
# ------------------------------------------------------------

# Both accomplish similar goals.
# Knowing when to use each is important.

# USE match/case WHEN:
# ✅ Checking ONE value against MANY specific options
# ✅ You have many exact value comparisons (like a menu)
# ✅ You need to match sequence structures (tuples, lists)
# ✅ You want cleaner syntax for long if/elif chains
# ✅ You're on Python 3.10+

# USE if/elif/else WHEN:
# ✅ You need Python 3.9 or older compatibility
# ✅ Checking multiple DIFFERENT variables
# ✅ Complex boolean logic (and/or/not across different vars)
# ✅ Range checks (x > 10 and x < 50)
# ✅ The conditions don't fit a pattern-matching model

# Side by side comparison:

# if/elif version:
status = 404
if status == 200:
    print("OK")
elif status == 404:
    print("Not Found")
elif status == 500:
    print("Server Error")
else:
    print("Other")

# match/case version (cleaner for this use case):
match status:
    case 200:
        print("OK")
    case 404:
        print("Not Found")
    case 500:
        print("Server Error")
    case _:
        print("Other")

# Both work. match/case is more readable when:
# - The variable name appears many times in if/elif
# - There are many specific equality checks

# if/elif is better here (range checks on multiple variables):
temp = 25
humidity = 80

if temp > 30 and humidity > 70:
    print("Hot and humid")
elif temp > 30:
    print("Hot and dry")
elif temp < 10:
    print("Cold")
else:
    print("Comfortable")

# This is awkward to express with match/case.
# Guards would work but it would be less clear.

# ------------------------------------------------------------
# PART 10: Practical use case - command dispatcher
# ------------------------------------------------------------

# A very common use case: processing text commands.

print("Simple Python Calculator")
print("Commands: add, sub, mul, div, quit")

command = input("Enter command: ").lower().strip()
a = 0
b = 0

if command not in ["quit", "exit"]:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

match command:
    case "add" | "plus" | "+":
        result = a + b
        print(f"{a} + {b} = {result}")
    case "sub" | "subtract" | "minus" | "-":
        result = a - b
        print(f"{a} - {b} = {result}")
    case "mul" | "multiply" | "times" | "*":
        result = a * b
        print(f"{a} × {b} = {result}")
    case "div" | "divide" | "/":
        if b != 0:
            result = a / b
            print(f"{a} ÷ {b} = {result:.4f}")
        else:
            print("❌ Cannot divide by zero!")
    case "quit" | "exit" | "q":
        print("Goodbye! 👋")
    case _:
        print(f"Unknown command: '{command}'")
        print("Valid commands: add, sub, mul, div, quit")

# ------------------------------------------------------------
# PART 11: Practical use case - biological data processing
# ------------------------------------------------------------

# Example 1: Nucleotide base classifier

def analyze_base(base):
    base = base.upper()
    match base:
        case "A":
            print(f"Adenine - Purine base, pairs with T (DNA) or U (RNA)")
        case "T":
            print(f"Thymine - Pyrimidine base, pairs with A, DNA only")
        case "U":
            print(f"Uracil - Pyrimidine base, pairs with A, RNA only")
        case "C":
            print(f"Cytosine - Pyrimidine base, pairs with G")
        case "G":
            print(f"Guanine - Purine base, pairs with C")
        case _:
            print(f"'{base}' is not a standard nucleotide base")

analyze_base("A")    # Adenine - Purine base, pairs with T (DNA) or U (RNA)
analyze_base("g")    # Guanine - Purine base, pairs with C
analyze_base("X")    # 'X' is not a standard nucleotide base

# Example 2: Amino acid properties

amino_acid = input("Enter amino acid single-letter code: ").upper()

match amino_acid:
    case "G":
        print("Glycine - Smallest amino acid, very flexible")
        print("Properties: Nonpolar, aliphatic")
    case "A" | "V" | "L" | "I" | "P":
        print(f"{amino_acid}: Nonpolar, aliphatic amino acid")
        print("Found in hydrophobic protein cores")
    case "F" | "W" | "Y":
        print(f"{amino_acid}: Aromatic amino acid")
        print("Absorbs UV light at 280nm")
    case "S" | "T" | "C":
        print(f"{amino_acid}: Polar, uncharged amino acid")
    case "M":
        print("Methionine - Always the START amino acid")
        print("Corresponds to codon ATG")
    case "K" | "R" | "H":
        print(f"{amino_acid}: Positively charged at physiological pH")
    case "D" | "E":
        print(f"{amino_acid}: Negatively charged at physiological pH")
    case "N" | "Q":
        print(f"{amino_acid}: Polar amide side chain")
    case _:
        print(f"'{amino_acid}' is not a standard amino acid code")

# Example 3: Enzyme classification by EC number (first digit)

ec_class = int(input("Enter EC class number (1-7): "))

match ec_class:
    case 1:
        print("Class 1: Oxidoreductases")
        print("Catalyze oxidation-reduction reactions")
        print("Example: Alcohol dehydrogenase, Catalase")
    case 2:
        print("Class 2: Transferases")
        print("Transfer functional groups between molecules")
        print("Example: Kinases, Transaminases")
    case 3:
        print("Class 3: Hydrolases")
        print("Catalyze hydrolysis reactions")
        print("Example: Proteases, Lipases, Nucleases")
    case 4:
        print("Class 4: Lyases")
        print("Add or remove groups to form double bonds")
        print("Example: Decarboxylases, Dehydratases")
    case 5:
        print("Class 5: Isomerases")
        print("Catalyze isomerization reactions")
        print("Example: Racemases, Epimerases")
    case 6:
        print("Class 6: Ligases")
        print("Join two molecules using ATP")
        print("Example: DNA Ligase, Synthetases")
    case 7:
        print("Class 7: Translocases")
        print("Catalyze movement of ions/molecules across membranes")
        print("Example: Ion pumps, ATP synthase")
    case _:
        print(f"EC class {ec_class} does not exist. Valid range: 1-7")

# ------------------------------------------------------------
# PART 12: Practical use case - data type routing
# ------------------------------------------------------------

# match/case can check the TYPE of a value using type patterns.
# This is a powerful feature for handling mixed-type data.

# Syntax for type matching:
#     case int():     → matches if value is an integer
#     case str():     → matches if value is a string
#     case float():   → matches if value is a float
#     case list():    → matches if value is a list

def describe_value(value):
    match value:
        case None:
            print("Value is None - no data")
        case True | False:
            print(f"Boolean value: {value}")
        case int():
            print(f"Integer: {value}")
            print(f"  Even: {'yes' if value % 2 == 0 else 'no'}")
        case float():
            print(f"Float: {value:.4f}")
            print(f"  Rounded: {round(value)}")
        case str():
            print(f"String: '{value}'")
            print(f"  Length: {len(value)} characters")
            print(f"  Upper: '{value.upper()}'")
        case list():
            print(f"List with {len(value)} elements")
            print(f"  First: {value[0] if value else 'empty'}")
        case _:
            print(f"Unknown type: {type(value).__name__}")

describe_value(42)
describe_value(3.14)
describe_value("DNA")
describe_value(None)
describe_value([1, 2, 3])
describe_value(True)

# Output:
# Integer: 42
#   Even: yes
# Float: 3.1400
#   Rounded: 3
# String: 'DNA'
#   Length: 3
#   Upper: 'DNA'
# Value is None - no data
# List with 3 elements
#   First: 1
# Boolean value: True

# ------------------------------------------------------------
# PART 13: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Using match/case in Python < 3.10

# match command:      ← SyntaxError in Python 3.9 and earlier!
#     case "start":
#         print("ok")

# ✅ Fix: check version or use if/elif

# ❌ MISTAKE 2: Putting wildcard (_) before other cases

command = "start"

# Wrong - _ catches everything, cases below never reached:
# match command:
#     case _:
#         print("default")    ← catches "start" here!
#     case "start":
#         print("Starting")   ← never reached!

# ✅ Wildcard must ALWAYS be LAST:
match command:
    case "start":
        print("Starting")    # reached!
    case _:
        print("default")

# ❌ MISTAKE 3: Using == in case patterns

x = 10

# Wrong - SyntaxError or logic error:
# match x:
#     case x == 10:    ← SyntaxError! No comparison operators in patterns
#         print("ten")

# ✅ Just write the value directly:
match x:
    case 10:
        print("ten")
    case _:
        print("other")

# For ranges/comparisons, use guards:
match x:
    case n if n > 5:
        print("greater than 5")
    case _:
        print("5 or less")

# ❌ MISTAKE 4: Forgetting the colon after case

# match day:
#     case "Monday"       ← SyntaxError! Missing colon
#         print("Monday")

# ✅ Fix:
day = "Monday"
match day:
    case "Monday":          # colon required
        print("Monday")
    case _:
        print("other")

# ❌ MISTAKE 5: Forgetting the colon after match

# match day           ← SyntaxError! Missing colon
#     case "Monday":
#         print("Monday")

# ✅ Fix:
match day:              # colon required here too
    case "Monday":
        print("Monday")
    case _:
        print("other")

# ❌ MISTAKE 6: Trying to use OR with comma instead of pipe

day = "Saturday"

# Wrong:
# match day:
#     case "Saturday", "Sunday":    ← this matches a TUPLE, not OR!
#         print("Weekend")

# ✅ Fix: use | for OR patterns:
match day:
    case "Saturday" | "Sunday":    # pipe | for OR
        print("Weekend")
    case _:
        print("Weekday")

# ❌ MISTAKE 7: Using a variable name as a pattern (it captures, not compares!)

expected = "hello"
actual = "world"

# Wrong - 'expected' in case does NOT compare to the variable expected!
# It creates a new variable called 'expected' that captures the value!
match actual:
    case expected:              # ← captures 'actual' into 'expected'!
        print("Match!")         # this ALWAYS runs!
    case _:
        print("No match")

# ✅ Fix: use the value directly or use a guard:
match actual:
    case "hello":               # literal value
        print("Match!")
    case _:
        print("No match")       # this runs ✅

# Or use a guard:
target = "hello"
match actual:
    case val if val == target:
        print("Match!")
    case _:
        print("No match")       # this runs ✅

# ❌ MISTAKE 8: Empty case body (SyntaxError)

# match x:
#     case 1:         ← SyntaxError - empty case body!
#     case 2:
#         print("two")

# ✅ Fix: use 'pass' as placeholder:
match x:
    case 1:
        pass            # placeholder - does nothing
    case _:
        print("other")

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ match/case requires Python 3.10+
# ✅ Matches ONE value against MANY patterns
# ✅ Only the FIRST matching case runs
# ✅ case _: is the wildcard (default) - must be LAST
# ✅ Use | for OR patterns: case "a" | "b":
# ✅ Guards add conditions: case n if n > 0:
# ✅ Sequence matching: case (x, y): or case [a, b, c]:
# ✅ 'as' captures matched value: case "quit" as cmd:
# ✅ Variable in case CAPTURES value, doesn't compare!
# ✅ Use literal values in patterns, not variables
# ✅ match/case is best for equality checks against one value
# ✅ if/elif/else is better for range/multi-variable checks

# Quick reference:
# ┌──────────────────────────────────────────────────────────┐
# │ match value:                                             │
# │     case 1:              ← exact integer match          │
# │     case "hello":        ← exact string match           │
# │     case None:           ← None match                   │
# │     case 1 | 2 | 3:      ← OR pattern                   │
# │     case n if n > 0:     ← guard (variable + condition) │
# │     case (x, y):         ← tuple pattern                │
# │     case [a, b]:         ← list pattern                 │
# │     case [first, *rest]: ← list with capture            │
# │     case str():          ← type pattern                 │
# │     case val as name:    ← capture with alias           │
# │     case _:              ← wildcard (must be last)      │
# └──────────────────────────────────────────────────────────┘