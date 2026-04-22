# ============================================================
# MODULE 02 | EXERCISES 29 - String Multiplication
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================
#
# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Print the character "=" exactly 40 times in one line.
# Use string multiplication - do NOT type 40 equal signs manually.
#
# Expected output:
# ========================================
# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Create a variable called 'separator' that contains
# 30 dashes using string multiplication.
# Then print it.
#
# Expected output:
# ------------------------------
# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Print the word "echo " (with a space) exactly 5 times
# using string multiplication.
#
# Expected output:
# echo echo echo echo echo
# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Predict what each line will print BEFORE running the code.
# Write your prediction as a comment next to each line.
# Then run and check.
#
# print("ha" * 4)          # your prediction: ?
# print("*" * 0)           # your prediction: ?
# print(3 * "Python ")     # your prediction: ?
# print("ab" * -2)         # your prediction: ?
# print("=-" * 5)          # your prediction: ?
# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Ask the user to enter a character (single letter or symbol)
# and then print it 10 times in a row using multiplication.
#
# Example interaction:
# Enter a character: #
# ##########
# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Find ALL the errors in the code below.
# Write what each error is as a comment next to the line.
# Then fix all errors so the code runs correctly.
#
# print("hello" * 3.0)
# print("hi" * "5")
# print("bye" * -1)
# print(result * 2)
# print("ab" * "cd")
# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a simple title banner using string multiplication
# and string concatenation (+).
#
# Requirements:
# - Line 1: 40 "=" characters
# - Line 2: ">>>> " + your name + " <<<<"
# - Line 3: 40 "=" characters
#
# Example output (for name "Anna"):
# ========================================
# >>>> Anna <<<<
# ========================================
# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Ask the user how many stars they want.
# Convert the input to an integer.
# Print a row of that many "★" characters.
#
# Then print a warning if they enter 0 or a negative number.
#
# Example interaction 1:
# How many stars do you want? 7
# ★★★★★★★
#
# Example interaction 2:
# How many stars do you want? -3
# (empty line - no stars printed)
# Tip: negative and zero give empty string automatically!
# Just print the result and add one line explaining what happened.
# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a simple staircase pattern using a loop
# and string multiplication.
#
# The staircase should have 6 steps.
# Each step adds one "#" compared to the previous.
#
# Expected output:
# #
# ##
# ###
# ####
# #####
# ######
#
# Then build the same staircase going DOWN (from 6 to 1).
#
# Expected output:
# ######
# #####
# ####
# ###
# ##
# #
# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a progress bar function called show_progress().
# It takes one argument: percent (a number from 0 to 100).
#
# Rules:
# - The bar is always 10 characters wide (inside the brackets)
# - Every 10% = one filled block "█"
# - Remaining space = "░"
# - Format: [██████░░░░] 60%
#
# Call your function with these values:
# 0, 20, 50, 75, 100
#
# Expected output:
# [░░░░░░░░░░] 0%
# [██░░░░░░░░] 20%
# [█████░░░░░] 50%
# [███████░░░] 75%
# [██████████] 100%
# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Without running the code first, trace through each step.
# Write your prediction as a comment before each print.
# Then run and verify.
#
# n = 3
# symbol = "-*-"
#
# line1 = symbol * n
# # Prediction: line1 = ?
# print(line1)
#
# line2 = symbol * (n + 2)
# # Prediction: line2 = ?
# print(line2)
#
# line3 = (">" * n) + " TEXT " + ("<" * n)
# # Prediction: line3 = ?
# print(line3)
#
# line4 = (symbol + " ") * n
# # Prediction: line4 = ?
# print(line4)
#
# n = 0
# line5 = "hello" * n + "world"
# # Prediction: line5 = ?
# print(line5)
# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a simple menu display using string multiplication.
#
# Requirements:
# - Print a top border of 40 "*" characters
# - Print the title "MAIN MENU" centered using spaces
#   (calculate how many spaces to add: (40 - len("MAIN MENU")) // 2)
# - Print a divider of 40 "-" characters
# - Print 3 menu options with "→ " prefix
# - Print a bottom border of 40 "*" characters
#
# Expected output:
# ****************************************
#                 MAIN MENU
# ----------------------------------------
# → 1. Start Game
# → 2. Load Game
# → 3. Quit
# ****************************************
# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Build a multiplication table display for string repetition.
#
# Ask the user for a word and print a table
# showing that word multiplied from 1 to 5.
#
# Each row should be numbered and show the result.
#
# Example interaction (user enters "py"):
# Enter a word: py
#
# 1x │ py
# 2x │ pypy
# 3x │ pypypy
# 4x │ pypypypy
# 5x │ pypypypypy
#
# Tip: use a loop and f-string for formatting.
# The "│" character is a Unicode pipe - copy it from here.
# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Create a reusable function called print_box()
# that draws a text box around any message.
#
# Requirements:
# - The box adjusts its width to the length of the text
# - Add 2 spaces of padding on each side of the text
# - Use "+" for corners, "-" for top/bottom, "|" for sides
# - The function should work for ANY length of text
#
# Call it with at least 3 different strings of different lengths.
#
# Expected output for print_box("Hi"):
# +------+
# |  Hi  |
# +------+
#
# Expected output for print_box("Python is great!"):
# +--------------------+
# |  Python is great!  |
# +--------------------+
#
# Expected output for print_box("DNA"):
# +-------+
# |  DNA  |
# +-------+
# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a diamond pattern using string multiplication,
# spaces, and a loop.
#
# The function diamond(size) should draw a diamond
# where 'size' controls how wide the middle row is.
# Size must be an odd number.
#
# Rules:
# - Top half: starts with 1 star, grows by 2 each row
# - Middle: the widest row (size stars)
# - Bottom half: mirror of top half
# - Stars are centered using spaces
#
# Call diamond(7) and diamond(5).
#
# Expected output for diamond(7):
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# Expected output for diamond(5):
#   *
#  ***
# *****
#  ***
#   *
#
# Tip: think about how many spaces go before each row.
# For size=7, the widest row needs 0 spaces.
# The row above needs 1 space. The row above that needs 2, etc.
# Use string multiplication for both spaces and stars.
# ============================================================