# ============================================================
# MODULE 02 | EXERCISES 16 - Slicing with Step
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given:

# word = "abcdefghij"

# Print slices and write a comment explaining what each one does:
#   word[::2]
#   word[::3]
#   word[1::2]
#   word[::1]
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("Exercise 1:")

word = "abcdefghij"

print(word[::2])      # acegi
print(word[::3])      # adgj
print(word[1::2])     # bdfhj
print(word[::1])      # abcdefghij



# ------------------------------------------------------------
# EXERCISE 2 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Reverse the following strings using [::-1].
# Print the original and reversed version for each.

# word1 = "Python"
# word2 = "Bioinformatics"
# word3 = "12345"
# word4 = "A"
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 2:")

word_1 = "Python"
word_2 = "Bioinformatics"
word_3 = "12345"
word_4 = "A"

reversed_1 = word_1[::-1]
reversed_2 = word_2[::-1]
reversed_3 = word_3[::-1]
reversed_4 = word_4[::-1]

print(f"Original: {word_1} | Reversed: {reversed_1}")
print(f"Original: {word_2} | Reversed: {reversed_2}")
print(f"Original: {word_3} | Reversed: {reversed_3}")
print(f"Original: {word_4} | Reversed: {reversed_4}")



# ------------------------------------------------------------
# EXERCISE 3 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Predict the output of each slice before running.
# Write your prediction as a comment, then verify.

# text = "Hello World"

# print(text[::2])    # Prediction: ?
# print(text[::3])    # Prediction: ?
# print(text[1::2])   # Prediction: ?
# print(text[::-1])   # Prediction: ?
# print(text[::-2])   # Prediction: ?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 3:")

text = "Hello World"

print(text[::2])    # Prediction: HloWrd
print(text[::3])    # Prediction: HlWl
print(text[1::2])   # Prediction: el ol
print(text[::-1])   # Prediction: dlroW olleH
print(text[::-2])   # Prediction: drW olH



# ------------------------------------------------------------
# EXERCISE 4 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given:

# word = "abcdefgh"

# Use step slicing to extract:
#   - every 2nd character starting from index 0
#   - every 2nd character starting from index 1

# Print results.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 4:")

word = "abcdefgh"

print(word[::2])
print(word[1::2])



# ------------------------------------------------------------
# EXERCISE 5 ✅ | EASY
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Check if the words below:

# words = ["racecar", "python", "madam", "hello", "level", "world"]

# are palindromes using the [::-1] trick. For each, print: "word : True/False"

# Expected output example:
#   racecar : True
#   python  : False
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 5:")

words = ["racecar", "python", "madam", "hello", "level", "world"]

word_1 = words[0][::-1]
word_2 = words[1][::-1]
word_3 = words[2][::-1]
word_4 = words[3][::-1]
word_5 = words[4][::-1]
word_6 = words[5][::-1]

print(f"Word '{word_1}' is a palindrome: {word_1 == words[0]}")
print(f"Word '{word_2}' is a palindrome: {word_2 == words[1]}")
print(f"Word '{word_3}' is a palindrome: {word_3 == words[2]}")
print(f"Word '{word_4}' is a palindrome: {word_4 == words[3]}")
print(f"Word '{word_5}' is a palindrome: {word_5 == words[4]}")
print(f"Word '{word_6}' is a palindrome: {word_6 == words[5]}")



# ------------------------------------------------------------
# EXERCISE 6 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given the encoded string:

# encoded = "Phyetlhloon"

# The real message is hidden at every 2nd character starting from 0.
# Decode and print the message.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 6:")

encoded = "Phyetlhloon"

decoded = encoded[::2]

print(decoded)



# ------------------------------------------------------------
# EXERCISE 7 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Use step slicing to split the alphabet string into two interleaved halves.

# alphabet = "abcdefghijklmnopqrstuvwxyz"

# Print:
#   - all characters at even indexes (0, 2, 4...)
#   - all characters at odd indexes  (1, 3, 5...)

# Then combine them back using concatenation
# and verify it equals the original using ==
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 7:")

alphabet = "abcdefghijklmnopqrstuvwxyz"

alphabet_even_version = alphabet[::2]
alphabet_odd_version = alphabet[1::2]

print(alphabet_even_version)
print(alphabet_odd_version)

full_alphabet = alphabet_even_version + alphabet_odd_version

print(full_alphabet)



# ------------------------------------------------------------
# EXERCISE 8 ✅ | EASY-MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Trace through the code below manually.
# For each print statement, predict the output as a comment.
# Then run and verify.

# word = "abcdefghij"

# print(word[8:2:-1])     # Prediction = ?
# print(word[9:0:-2])     # Prediction = ?
# print(word[7:1:-2])     # Prediction = ?
# print(word[4::-1])      # Prediction = ?
# print(word[-1:-6:-1])   # Prediction = ?
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 8:")

word = "abcdefghij"

print(word[8:2:-1])       # ihgfed
print(word[9:0:-2])       # jhfdb
print(word[7:1:-2])       # hfd
print(word[4::-1])        # edcba
print(word[-1:-6:-1])     # jihgf



# ------------------------------------------------------------
# EXERCISE 9 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Demonstrate the "wrong direction" concept. For the string:

# word = "Python"

# Print the results of these slices:
#   word[4:1:1]
#   word[1:4:-1]
#   word[1:4:1]
#   word[4:1:-1]
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 9:")

word = "Python"

print(word[4:1:1])       # ""
print(word[1:4:-1])      # ""
print(word[1:4:1])       # yth
print(word[4:1:-1])      # oht



# ------------------------------------------------------------
# EXERCISE 10 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Given the DNA string below:

# dna = "ATGCCCGCATTAGTCGA"

# Using step slicing:
#   - Extract every 3rd nucleotide starting from index 0
#   - Extract every 3rd nucleotide starting from index 1
#   - Extract every 3rd nucleotide starting from index 2
#   - Reverse the entire sequence

# Print each with a descriptive label.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 10:")

dna = "ATGCCCGCATTAGTCGA"

print(f"Starting index (3rd step): 0 -> {dna[::3]}")
print(f"Starting index (3rd step): 1 -> {dna[1::3]}")
print(f"Starting index (3rd step): 2 -> {dna[2::3]}")
print(f"Reversed: {dna[::-1]}")



# ------------------------------------------------------------
# EXERCISE 11 ✅ | MEDIUM
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Create a "mirror" string using slicing and concatenation.

# A mirror string looks like: "Python" → "PythonnohtyP"

# Do this for all three words:
#   word1 = "Python"
#   word2 = "Bio"
#   word3 = "DNA"

# Print each mirrored version.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 11:")

word_1 = "Python"
word_2 = "Bio"
word_3 = "DNA"

print(f"Original: {word_1} | with mirror: {word_1 + word_1[::-1]}")
print(f"Original: {word_2} | with mirror: {word_2 + word_2[::-1]}")
print(f"Original: {word_3} | with mirror: {word_3 + word_3[::-1]}")



# ------------------------------------------------------------
# EXERCISE 12 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Find and fix all errors in the code.

# word = "Python"

# print(word[::0])            # Prediction = ?
# print(word[1:4:-1])         # Prediction = ?
# print(word[4:1:1])          # Prediction = ?

# Write what each error is as a comment next to it.
# Then fix all of them.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 12:")

# word = "Python"

# print(word[::0])            # error: step cannot be 0
# print(word[1:4:-1])         # ""
# print(word[4:1:1])          # ""

word = "Python"

print(word[::1])
print(word[1:4:1])
print(word[4:1:-1])



# ------------------------------------------------------------
# EXERCISE 13 ✅ | MEDIUM-HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# For the string:

# word = "abcdefghij"

# Without running, calculate the exact output of each slice.
# Show your working as a comment (list the indexes visited).

# Then verify by running.
#   a) word[0:9:3]
#   b) word[9:0:-3]
#   c) word[::4]
#   d) word[1::3]
#   e) word[-1::-3]
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 12:")

word = "abcdefghij"

print(f"a) {word[0:9:3]}")      # adg
print(f"b) {word[9:0:-3]}")     # jgd
print(f"c) {word[::4]}")        # aei
print(f"d) {word[1::3]}")       # beh
print(f"e) {word[-1::-3]}")     # jgda



# ------------------------------------------------------------
# EXERCISE 14 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Decode the secret message using step slicing.

# encoded = "PxxYxxTxxHxxOxxNxx"

# Part A: Decode the message using a single slice

# Part B: Re-encode the decoded message manually:
#   Add "xx" after each character of your decoded message
#   to reconstruct something similar to the original pattern.

# Print both the decoded message and your re-encoded version.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 14:")

encoded = "PxxYxxTxxHxxOxxNxx"

print("Part A:")

decoded = encoded[::3]

print(decoded)

print("Part B:")

a = decoded[0]
b = decoded[1]
c = decoded[2]
d = decoded[3]
e = decoded[4]
f = decoded[5]

xx = "xx"
re_encoded = a + xx + b + xx + c + xx + d + xx + e + xx + f + xx

print(f"Original: {encoded}")
print(f"Decoded: {decoded}")
print(f"Re-encoded: {re_encoded}")



# ------------------------------------------------------------
# EXERCISE 15 ✅ | HARD
# ------------------------------------------------------------
# PROBLEM:
# ------------------------------------------------------------
# Part A:
#   Given: word = "abcdefghij"
#   Using only step slicing:
#   - find two different slices that produce the same result "ace".
#   - write both and verify with ==

# Part B:
#   Given: sentence = "I love Python programming"
#   Using step slicing, extract every 3rd character from the end
#   Print the result and trace which characters were selected

# Part C:
#   Verify this claim using word = "Python":
#     word[::-1][::2]  gives the same result as word[-1::-2]
#   Print both and compare with ==

# Part D:
#   Create a string of exactly 12 characters of your choice.
#   Using step slicing, split it into 3 groups of 4 characters.
# ------------------------------------------------------------
# CODE:
# ------------------------------------------------------------
print("\nExercise 15:")

print("Part A:")

word = "abcdefghij"

print(f"'ace' slicing: word[:5:2] -> {word[:5:2]}")
print(f"'ace' slicing: word[-10:-5:2] -> {word[-10:-5:2]}")

print("Part B:")

sentence = "I love Python programming"

print(sentence[-1::-3])     # gmrrnt  oI

print("Part C:")

word = "Python"

print(f"Does {word[::-1][::2]} == {word[-1::-2]}? : {word[-1::-2] == word[::-1][::2] }")

print("Part D:")

string = "zoologically"

print(string[::3])
print(string[1::3])
print(string[2::3])