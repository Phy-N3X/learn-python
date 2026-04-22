# ============================================================
# MODULE 02 | EXERCISES 20 - .replace()
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Use .replace() to make these simple substitutions.
# Print the original and the result for each.

sentence1 = "I love cats"
# Replace "cats" with "dogs"

sentence2 = "Hello World"
# Replace "World" with "Python"

sentence3 = "The sky is blue"
# Replace "blue" with "grey"



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate that .replace() replaces ALL occurrences.
# For each string, predict the output BEFORE running.
# Write your prediction as a comment, then verify.

text1 = "banana"
# Prediction: ?
print(text1.replace("a", "o"))

text2 = "the cat sat on the mat"
# Prediction: ?
print(text2.replace("at", "og"))

text3 = "aabbaa"
# Prediction: ?
print(text3.replace("a", "x"))



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Demonstrate that .replace() does NOT modify the original.
# Show the mistake first (calling without storing result),
# then show the correct approach.
# Write comments explaining what happens in each case.

text = "Hello World"
# Step 1: Call .replace() without storing - show it does nothing
# Step 2: Store in new variable - show it works
# Step 3: Reassign same variable - show it works



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use the count parameter to limit replacements.
# For the string below, print the result of:
#   a) replacing all "the" occurrences (no count)
#   b) replacing only the first "the"
#   c) replacing only the first 2 "the"
# Label each output.

text = "the cat sat on the mat near the fence by the tree"



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Use .replace() with "" to DELETE substrings.
# For each case, remove the specified part and print the result.

text1 = "Hello, World!"
# Remove all commas

text2 = "P-y-t-h-o-n"
# Remove all hyphens

text3 = "   Hello   World   "
# Remove all spaces (not strip - remove ALL spaces including middle!)

text4 = "ATG-CCC-GCA-TTA"
# Remove all dashes from this DNA sequence



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Case sensitivity exercise.
# Given: text = "Cat cat CAT"
# Try replacing "cat" (lowercase) only.
# Predict the output before running.
# Then replace each variant separately and print results.
# Finally, use .lower() + .replace() to replace ALL variants.

text = "Cat cat CAT"
# Prediction for text.replace("cat", "dog"): ?
print(text.replace("cat", "dog"))
print(text.replace("Cat", "dog"))
print(text.replace("CAT", "dog"))
# Now replace all variants using .lower():



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Fill in a template using .replace().
# The template below uses placeholders in CAPS.
# Replace each placeholder with a real value.
# Use chained .replace() calls in ONE expression.

template = "Dear FIRSTNAME LASTNAME, your order ORDER_ID will arrive on DATE."
first_name = "Anna"
last_name = "Kowalska"
order_id = "ORD-2024-789"
date = "March 15, 2024"

# Replace all placeholders and print the result.



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Normalize these messy strings using .replace().
# For each, apply the replacements described and print the result.

# a) Replace all tabs with 4 spaces:
tabbed = "Name\tAge\tCity\tCountry"

# b) Replace Windows newlines (\r\n) with Unix newlines (\n):
windows = "Line1\r\nLine2\r\nLine3"
print(repr(windows.replace("\r\n", "\n")))

# c) Replace multiple spaces with a single space:
# Hint: you can't do this perfectly with one .replace(),
# but try: replace "  " (2 spaces) with " " (1 space) - chain a few times
messy = "Hello    World     Python"

# d) Convert snake_case to readable text with title case:
snake = "first_name_last_name_age"



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a simple username sanitizer.
# Given a "display name", convert it to a valid username:
#   1. Replace spaces with underscores
#   2. Replace hyphens with underscores
#   3. Replace dots with underscores
#   4. Convert to lowercase
# Do all replacements in ONE chained expression.
# Print the original and the sanitized username.

name1 = "Anna Kowalska"
name2 = "Jan-Piotr Nowak"
name3 = "Maria.Wiśniewska"
name4 = "Piotr Jan Kowalczyk-Nowak"



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Number format converter.
# European format uses: period for thousands, comma for decimal
# US format uses:       comma for thousands, period for decimal
#
# Convert these European numbers to US format.
# Be careful: you need to use a temporary placeholder
# to avoid replacing the wrong characters!
# Hint:
#   Step 1: replace "." with a placeholder (e.g., "TEMP")
#   Step 2: replace "," with "."
#   Step 3: replace "TEMP" with ","

eu_num1 = "1.234,56"       # should become "1,234.56"
eu_num2 = "1.000.000,00"   # should become "1,000,000.00"
eu_num3 = "42,99"          # should become "42.99"



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Investigate the edge case: replacing empty string "".
#
# Part A:
# Run this and explain the output as a detailed comment:
text = "abc"
print(text.replace("", "-"))
# What does this output? Why?
# How many "-" characters appear? Where exactly?
#
# Part B:
# Verify your explanation by checking the length:
print(len(text))
print(len(text.replace("", "-")))
# What is the relationship between the lengths?
# Write the formula as a comment.
#
# Part C:
# Can you think of a use case where this behavior is useful?
# Write your idea as a comment.



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Investigate what happens when replacement chains interact.
# Predict the output of EACH step before running.
# Show your working for each prediction.

text = "aabbcc"

# Prediction: ?
print(text.replace("a", "b").replace("b", "c"))

# Prediction: ?
print(text.replace("b", "c").replace("a", "b"))

# Why are these different? Write a step-by-step explanation.

# Now predict this one:
text2 = "abcabc"
# Prediction: ?
print(text2.replace("abc", "xyz").replace("x", "A"))

# And this one - careful!
text3 = "hello"
# Prediction: ?
print(text3.replace("l", "ll").replace("ll", "L"))



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find ALL errors and unexpected behaviors below.
# For each line write a comment:
#   a) Is it a Python error? If so, what kind?
#   b) If not an error, is the output what you'd expect?
#      Explain any surprising behavior.

text = "Hello World"
text.replace("World", "Python")     # Issue: ?
print(text)                         # What prints here?

print("Hello".replace())            # Error: ?
print("Hello".replace("l"))         # Error: ?

result = "Hello".replace("hello", "Hi")
print(result)                       # Surprising? Explain.

result2 = "Hello".replace("Hello", "Hello")
print(result2)                      # What prints? Meaningful?



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a simple "find and replace" text processor.
#
# You are given a text and a list of (old, new) pairs.
# Apply ALL replacements to the text.
# Since we haven't covered loops, do it manually.
#
# text = "The quick brown fox jumps over the lazy dog"
#
# Replacements to apply (in this order):
#   ("The", "A")
#   ("quick", "slow")
#   ("brown", "white")
#   ("fox", "turtle")
#   ("jumps", "crawls")
#   ("over", "under")
#   ("lazy", "energetic")
#   ("dog", "cat")
#
# Part A: Apply all replacements using a SINGLE chain of .replace() calls.
# Part B: Apply the SAME replacements but in REVERSE order.
#         Does the result differ? Explain why or why not.
# Part C: What would happen if "The" → "A" was applied LAST?
#         Would it affect anything? Test it.

text = "The quick brown fox jumps over the lazy dog"



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Multi-part challenge: text cleaning and transformation pipeline.
#
# Part A:
# Given the messy text below, clean it using ONLY .replace():
#   1. Replace all double spaces with single spaces
#      (apply multiple times if needed)
#   2. Replace " ," with ","    (space before comma)
#   3. Replace " ." with "."    (space before period)
#   4. Replace "\n" with " "    (newlines to spaces)
#   5. Replace "\t" with " "    (tabs to spaces)
# Print the cleaned version.

messy_text = "Hello ,  World .\nThis   is\ta   test  text  with  many   issues ."

# Part B:
# Given a DNA sequence with various formatting issues:
#   1. Remove all spaces
#   2. Remove all dashes
#   3. Remove all newlines
#   4. Convert to uppercase
# Print the clean sequence and its length.

raw_dna = "ATG - CCC\nGCA - TTA\nGTC - GA"

# Part C:
# Given a simple CSV line with inconsistent spacing around commas:
# "  Anna  ,  25  ,  Warsaw  ,  Poland  "
# Using .replace() and .strip():
#   1. Replace " , " with "," (space-comma-space → just comma)
#   2. Replace " ," with ","
#   3. Replace ", " with ","
#   4. Strip the whole result
# Print the cleaned CSV line.
# Then verify: does it equal "Anna,25,Warsaw,Poland"?

raw_csv = "  Anna  ,  25  ,  Warsaw  ,  Poland  "