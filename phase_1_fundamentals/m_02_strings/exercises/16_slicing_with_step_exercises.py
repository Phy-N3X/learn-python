# ============================================================
# MODULE 02 | EXERCISES 04 - Slicing with Step
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================


# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Given: word = "abcdefghij"
# Print the following slices and write a comment
# explaining what each one does:
#   word[::2]
#   word[::3]
#   word[1::2]
#   word[::1]



# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Reverse the following strings using [::-1].
# Print the original and reversed version for each.

word1 = "Python"
word2 = "Bioinformatics"
word3 = "12345"
word4 = "A"



# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output of each slice BEFORE running.
# Write your prediction as a comment, then verify.

text = "Hello World"
# Prediction: ?
print(text[::2])
# Prediction: ?
print(text[::3])
# Prediction: ?
print(text[1::2])
# Prediction: ?
print(text[::-1])
# Prediction: ?
print(text[::-2])



# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use step slicing to extract:
#   - every 2nd character starting from index 0
#   - every 2nd character starting from index 1
# from the string below.
# What do you notice about the two results?
# Write your observation as a comment.

word = "abcdefgh"



# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Check if the words below are palindromes
# using the [::-1] trick.
# For each word, print: "word : True/False"
# Expected output example:
#   racecar : True
#   python  : False

words = ["racecar", "python", "madam", "hello", "level", "world"]
# Hint: you will need to access each word separately for now
# (we haven't covered loops yet - do each one manually)



# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Given the encoded string below:
# The real message is hidden at every 2nd character (step=2)
# starting from index 0.
# Decode and print the message.
# Then explain in a comment how the encoding works.

encoded = "Phyetlhloon"



# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use step slicing to split the alphabet string
# into two interleaved halves.
# Print:
#   - all characters at even indexes (0, 2, 4...)
#   - all characters at odd indexes  (1, 3, 5...)
# Then combine them back using concatenation
# and verify it equals the original using ==

alphabet = "abcdefghijklmnop"



# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Trace through the code below manually.
# For each print statement, predict the output as a comment.
# Then run and verify.

word = "abcdefghij"
# Prediction: ?
print(word[8:2:-1])
# Prediction: ?
print(word[9:0:-2])
# Prediction: ?
print(word[7:1:-2])
# Prediction: ?
print(word[4::-1])
# Prediction: ?
print(word[-1:-6:-1])



# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Demonstrate the "wrong direction" concept.
# For the string "Python":
# Print the results of these slices and write a comment
# explaining WHY each gives an empty string (or doesn't):
#   word[4:1:1]
#   word[1:4:-1]
#   word[1:4:1]
#   word[4:1:-1]

word = "Python"



# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Given the DNA string below:
# Using step slicing:
#   - Extract every 3rd nucleotide starting from index 0
#   - Extract every 3rd nucleotide starting from index 1
#   - Extract every 3rd nucleotide starting from index 2
#   - Reverse the entire sequence
# Print each with a descriptive label.

dna = "ATGCCCGCATTAGTCGA"



# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a "mirror" string using slicing and concatenation.
# A mirror string looks like: "Python" → "PythonnohtyP"
# Do this for all three words below.
# Print each mirrored version.

word1 = "Python"
word2 = "Bio"
word3 = "DNA"



# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Find and fix ALL errors in the code below.
# Write what each error is as a comment next to it.
# Then fix all of them.

word = "Python"
print(word[::0])            # Error: ?
print(word[1:4:-1])         # Not an error, but explain the output
print(word[4:1:1])          # Not an error, but explain the output



# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# This exercise is about careful tracing.
# For the string "abcdefghij" (indexes 0-9):
#
# Without running, calculate the exact output of each slice.
# Show your working as a comment (list the indexes visited).
# Then verify by running.
#
# a) word[0:9:3]
# b) word[9:0:-3]
# c) word[::4]
# d) word[1::3]
# e) word[-1::-3]

word = "abcdefghij"



# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Decode the secret message using step slicing.
#
# The message below was encoded using this method:
#   1. The real message was written normally.
#   2. After each real character, 2 fake characters were inserted.
#   So the pattern is: real, fake, fake, real, fake, fake...
#   This means the real characters are at indexes: 0, 3, 6, 9...
#
# Part A: Decode the message using a single slice with step=3
# Part B: Re-encode the decoded message manually:
#         Add "xx" after each character of your decoded message
#         to reconstruct something similar to the original pattern.
#         (Hint: use indexing in a creative way - no loops yet,
#          so do it character by character with concatenation)
# Print both the decoded message and your re-encoded version.

encoded = "PxxYxxTxxHxxOxxNxx"



# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# This is the ultimate step slicing challenge.
#
# Part A:
# Given word = "abcdefghij"
# Using ONLY step slicing (no other string methods):
# Find TWO different slices that produce the same result "ace".
# Write both and verify with ==
#
# Part B:
# Given sentence = "I love Python programming"
# Using step slicing, extract every 3rd character from the end
# (i.e., step=-3 starting from the last character).
# Print the result and trace which characters were selected
# (write the indexes as a comment).
#
# Part C:
# Verify this claim using word = "Python":
#   word[::-1][::2]  gives the same result as  word[-1::-2]
# Print both, compare with ==, and write a comment explaining
# WHY they are (or aren't) the same - trace the indexes for both.
#
# Part D:
# Create a string of exactly 12 characters of your choice.
# Using step slicing, split it into 3 groups of 4 characters each
# WITHOUT using start/stop - use ONLY the step parameter
# and index arithmetic.
# Hint: this is tricky - think about what combination of
# start and step gives you characters at positions 0,3,6,9
# vs 1,4,7,10 vs 2,5,8,11