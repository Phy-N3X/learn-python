# ============================================================
# MODULE 02 | EXERCISES 30 - in / not in
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Check if the following substrings exist in the text below.
# Print the result of each check (True or False).
#
# text = "Python is great for bioinformatics"
#
# Check for:
# 1. "Python"
# 2. "java"
# 3. "bio"
# 4. "great"
# 5. "!"
#
# Expected output:
# True
# False
# True
# True
# False

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Predict what each line will print BEFORE running the code.
# Write your prediction as a comment next to each line.
# Then run and check.
#
# text = "Hello, World!"
#
# print("World" in text)         # your prediction: ?
# print("world" in text)         # your prediction: ?
# print("!" in text)             # your prediction: ?
# print("Hello" not in text)     # your prediction: ?
# print("Python" not in text)    # your prediction: ?
# print("" in text)              # your prediction: ?

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Create a variable called 'sentence' with any value you like.
# Then create three variables that store the RESULT
# of an 'in' or 'not in' check (True or False).
#
# Requirements:
# - 'found' = result of checking if "Python" is in sentence
# - 'missing' = result of checking if "Java" is NOT in sentence
# - 'has_space' = result of checking if " " is in sentence
#
# Print all three variables and their types.
#
# Expected output format:
# found: True <class 'bool'>
# missing: True <class 'bool'>
# has_space: True <class 'bool'>

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL the errors in the code below.
# Write what each error is as a comment next to the line.
# Then fix all errors so the code runs correctly.
#
# text = "I love Python"
#
# print(Python in text)
# print("love" in Text)
# print("python" IN text)
# print(text in "love")
# print("I" not text)

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Ask the user to enter any word.
# Then check if the vowels a, e, i, o, u appear in their word.
# Print the result for each vowel separately.
#
# Example interaction (user enters "python"):
# Enter a word: python
# 'a' in 'python': False
# 'e' in 'python': False
# 'i' in 'python': False
# 'o' in 'python': True
# 'u' in 'python': False

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Write a program that checks if an email address
# entered by the user looks valid.
#
# Rules (basic check only):
# - Must contain "@"
# - Must contain "."
# - Must NOT contain spaces
#
# Print a specific message for each failed rule.
# If all rules pass, print "Email looks valid!"
#
# Example interaction 1:
# Enter email: user@gmail.com
# Email looks valid!
#
# Example interaction 2:
# Enter email: usergmail.com
# Error: missing @
#
# Example interaction 3:
# Enter email: user @gmail.com
# Error: contains spaces

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Below is a DNA sequence.
# Check if the following codons (3-letter sequences) appear in it.
# Print a clear message for each result.
#
# dna = "ATGCGATACGCTTAG"
#
# Check for: "ATG", "TAC", "GGG", "TAG", "CGA"
#
# Expected output:
# ATG found in sequence: True
# TAC found in sequence: True
# GGG found in sequence: False
# TAG found in sequence: True
# CGA found in sequence: True
#
# Then answer as a comment:
# Which of these codons is a START codon? (hint: ATG)
# Which is a STOP codon? (hint: TAG)

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a simple word censor program.
# The program checks if a message contains a forbidden word.
# If it does - print a warning.
# If it doesn't - print the message normally.
#
# Do it in a case-insensitive way (use .lower())
#
# Test your program with these messages:
# msg1 = "This is a perfectly fine message"
# msg2 = "This message contains SPAM content"
# msg3 = "Buy now! Great OFFER just for you! spam alert"
#
# forbidden = "spam"
#
# Expected output:
# ✓ This is a perfectly fine message
# ⚠ Warning: message contains forbidden word!
# ⚠ Warning: message contains forbidden word!

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this code step by step.
# Before each print, write your prediction as a comment.
# Then run the code and verify.
#
# text = "Data Science and Python"
# keyword = "python"
#
# result1 = keyword in text
# # Prediction: result1 = ?
# print(result1)
#
# result2 = keyword in text.lower()
# # Prediction: result2 = ?
# print(result2)
#
# result3 = keyword.upper() in text.upper()
# # Prediction: result3 = ?
# print(result3)
#
# result4 = "science" not in text
# # Prediction: result4 = ?
# print(result4)
#
# result5 = "science" not in text.lower()
# # Prediction: result5 = ?
# print(result5)
#
# Final question (answer as a comment):
# Why are result1 and result2 different?
# Why are result2 and result3 the same?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a password strength checker using only 'in' / 'not in'.
#
# Ask the user to enter a password.
# Check all of the following conditions and print the result
# of each check:
#
# 1. Contains at least one uppercase letter
#    (check if any char from "ABCDEFGHIJKLMNOPQRSTUVWXYZ" is in password)
# 2. Contains at least one digit
#    (check if any char from "0123456789" is in password)
# 3. Contains at least one special character
#    (check against "!@#$%^&*()")
# 4. Does NOT contain spaces
#
# Print a summary at the end: "Strong password" or "Weak password"
# (strong = all 4 conditions met)
#
# Example interaction:
# Enter password: MyPass123!
# Has uppercase: True
# Has digit: True
# Has special char: True
# No spaces: True
# Strong password ✅
#
# Tip: use a loop to check character by character,
# set a boolean flag to True if found.

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# You have a list of log messages from a server.
# Analyze them using 'in' / 'not in'.
#
# logs = [
#     "INFO: Server started successfully",
#     "INFO: User admin logged in",
#     "ERROR: Database connection failed",
#     "WARNING: High memory usage detected",
#     "ERROR: Timeout after 30 seconds",
#     "INFO: Backup completed",
#     "ERROR: Disk space critically low",
# ]
#
# Tasks:
# 1. Print all logs that contain "ERROR" with a ⚠ prefix
# 2. Print all logs that do NOT contain "ERROR" with a ✓ prefix
# 3. Count how many logs contain "ERROR"
# 4. Count how many logs contain "INFO"
# 5. Print whether any log contains "critical" (case-insensitive)
#
# Expected output format:
# ⚠ ERROR: Database connection failed
# ⚠ ERROR: Timeout after 30 seconds
# ⚠ ERROR: Disk space critically low
# ✓ INFO: Server started successfully
# ... etc.
# ERROR count: 3
# INFO count: 3
# Critical issue found: True

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a simple search engine for a small "database" of texts.
#
# articles = {
#     "article1": "Python is a popular programming language",
#     "article2": "DNA sequencing uses bioinformatics tools",
#     "article3": "Machine learning and Python go hand in hand",
#     "article4": "Proteins are made of amino acids",
#     "article5": "Python is used in data science and AI",
# }
#
# Ask the user to enter a search keyword.
# Search through all articles (case-insensitive).
# Print which articles contain the keyword.
# Print how many results were found.
#
# Example interaction 1:
# Enter search keyword: python
# Found in: article1
# Found in: article3
# Found in: article5
# Total results: 3
#
# Example interaction 2:
# Enter search keyword: biology
# No articles found for 'biology'
#
# Tip: use a loop to go through articles.items()
# (we'll cover dictionaries later - for now just use the structure given)

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a function called validate_dna() that checks
# if a given string is a valid DNA sequence.
#
# Rules for valid DNA:
# - Can only contain the characters A, T, C, G (uppercase)
# - Must NOT be empty
# - Must NOT contain spaces
# - Must NOT contain numbers
# - Must NOT contain lowercase letters
#
# The function should:
# - Print whether the sequence is valid or not
# - If invalid, print exactly WHY it's invalid (which rule failed)
#
# Test with:
# validate_dna("ATCGATCG")      → Valid DNA sequence ✅
# validate_dna("")              → Invalid: sequence is empty
# validate_dna("ATCG ATCG")    → Invalid: contains spaces
# validate_dna("ATCG1234")     → Invalid: contains numbers
# validate_dna("AtcGATCG")     → Invalid: contains lowercase letters
# validate_dna("ATCGXYZ")      → Invalid: contains unknown bases (X, Y, Z)
#
# Tip: for the last case, check each character using 'not in "ATCG"'

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a text analysis tool that analyzes a paragraph of text.
#
# Use this text:
# text = """
# Python is a high-level programming language known for its
# simplicity and readability. It is widely used in data science,
# machine learning, bioinformatics, and web development.
# Python was created by Guido van Rossum and first released in 1991.
# Today, Python is one of the most popular languages in the world.
# """
#
# Perform ALL of the following analyses using 'in' / 'not in':
#
# 1. Check if these topics are mentioned (case-insensitive):
#    ["data science", "machine learning", "bioinformatics",
#     "web development", "cybersecurity", "game development"]
#    Print: "✓ topic found" or "✗ topic not found"
#
# 2. Check if these people are mentioned:
#    ["Guido van Rossum", "Linus Torvalds", "Ada Lovelace"]
#    Print: "✓ person mentioned" or "✗ person not mentioned"
#
# 3. Count how many of the digits 0-9 appear in the text
#    Print each digit that IS found
#
# 4. Check if the text contains any of these punctuation marks:
#    ".", ",", "!", "?", ";"
#    Print each one that is found
#
# Print all results in a clean, readable format with headers.

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a simple chatbot that responds to user messages
# using 'in' / 'not in' to detect keywords.
#
# The chatbot should:
# - Run in a loop until the user types "quit" or "exit" or "bye"
# - Detect keywords in the user's message (case-insensitive)
# - Give different responses based on what keywords it finds
# - Handle unknown messages with a default response
#
# Keyword → Response mapping:
# "hello" or "hi"       → "Hello! How can I help you?"
# "python"              → "Python is a great language! I love it too."
# "dna" or "biology"    → "Bioinformatics is a fascinating field!"
# "help"                → "I can talk about Python, DNA, and biology."
# "name"                → "My name is PyBot. Nice to meet you!"
# "weather"             → "I'm a text bot, I don't know the weather!"
# none of the above     → "Interesting... tell me more!"
# "quit","exit","bye"   → "Goodbye! See you next time." (then stop)
#
# Example interaction:
# You: Hello there!
# PyBot: Hello! How can I help you?
#
# You: Tell me about Python
# PyBot: Python is a great language! I love it too.
#
# You: I study DNA sequences
# PyBot: Bioinformatics is a fascinating field!
#
# You: bye
# PyBot: Goodbye! See you next time.
#
# Tip: use a while loop with a flag variable (e.g. running = True)
# Use .lower() on user input before all checks.
# Check the exit keywords FIRST before other keywords.
# ============================================================