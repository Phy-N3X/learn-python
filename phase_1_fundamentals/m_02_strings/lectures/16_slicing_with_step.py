# ============================================================
# MODULE 02 | LECTURE 04 - Slicing with Step
# ============================================================
# What you will learn:
#   - What the step parameter is
#   - Full slicing syntax: string[start:stop:step]
#   - How step works with positive values
#   - How step works with negative values (reversing!)
#   - Useful step shortcuts
#   - Combining start, stop and step
#   - Real world use cases
#   - Common mistakes and how to avoid them
# ============================================================


# ------------------------------------------------------------
# PART 1: Recap and the missing piece
# ------------------------------------------------------------

# So far we know: string[start:stop]
# This gives us characters from start up to (not including) stop.
# But there is a THIRD parameter we haven't used yet: STEP.

# Full syntax:
#   string[start:stop:step]
#
# step = how many positions to jump between each character
#
# Default step is 1 → take every character, one by one.
# That's why string[0:6] and string[0:6:1] are identical!

word = "Python"
print(word[0:6])        # Python  ← step defaults to 1
print(word[0:6:1])      # Python  ← explicitly step=1, same result


# ------------------------------------------------------------
# PART 2: Step = 2 (every other character)
# ------------------------------------------------------------

# With step=2, Python jumps 2 positions each time.
# It takes a character, skips one, takes one, skips one...

word = "Python"
#  P  y  t  h  o  n
#  0  1  2  3  4  5

print(word[0:6:2])  # Pto
# Explanation:
#   index 0 → P  (take)
#   index 1 → y  (skip - jumped by 2)
#   index 2 → t  (take)
#   index 3 → h  (skip - jumped by 2)
#   index 4 → o  (take)
#   index 5 → n  (skip - jumped by 2)
#   index 6 → stop (end of slice)
# Result: P, t, o → "Pto"

print(word[1:6:2])  # yhn
# Explanation:
#   index 1 → y  (take)
#   index 3 → h  (take, jumped by 2)
#   index 5 → n  (take, jumped by 2)
# Result: y, h, n → "yhn"


# ------------------------------------------------------------
# PART 3: Step = 3 (every third character)
# ------------------------------------------------------------

word = "abcdefghij"
#  a  b  c  d  e  f  g  h  i  j
#  0  1  2  3  4  5  6  7  8  9

print(word[0:10:3])     # adgj
# index 0 → a  (take)
# index 3 → d  (take, jumped by 3)
# index 6 → g  (take, jumped by 3)
# index 9 → j  (take, jumped by 3)
# index 12 → stop (beyond string)

print(word[0:10:4])     # aei
# index 0 → a  (take)
# index 4 → e  (take, jumped by 4)
# index 8 → i  (take, jumped by 4)
# index 12 → stop (beyond string)

print(word[0:10:5])     # af
# index 0 → a  (take)
# index 5 → f  (take, jumped by 5)
# index 10 → stop (beyond string)


# ------------------------------------------------------------
# PART 4: Omitting start and stop with step
# ------------------------------------------------------------

# Just like before, you can omit start and/or stop.
# When combined with step, this is very powerful.

word = "abcdefghij"

# Every other character from the beginning:
print(word[::2])        # acegi   ← start=0, stop=end, step=2

# Every third character from the beginning:
print(word[::3])        # adgj    ← start=0, stop=end, step=3

# Every other character starting from index 1:
print(word[1::2])       # bdfhj   ← start=1, stop=end, step=2

# Every other character up to index 7:
print(word[:7:2])       # aceg    ← start=0, stop=7, step=2

# The full string (step=1 is default):
print(word[::1])        # abcdefghij

# Most common shortcut you will see in real code:
sentence = "Hello World"
print(sentence[::2])    # HloWrd
print(sentence[::3])    # HoWl


# ------------------------------------------------------------
# PART 5: Negative step - going BACKWARDS
# ------------------------------------------------------------

# This is where slicing becomes really powerful.
# A NEGATIVE step makes Python go from RIGHT to LEFT.
# Instead of moving forward, it moves backward.

word = "Python"

# Step = -1 → go backwards one character at a time:
print(word[::-1])       # nohtyP  ← the string REVERSED!

# This is one of the most famous Python tricks.
# word[::-1] reverses any string in one line!

# Let's trace it step by step:
# word = "Python"
# start = end of string (default for negative step)
# stop  = beginning of string (default for negative step)
# step  = -1 (go backwards)
#
# index 5 → n  (take)
# index 4 → o  (take, jumped by -1)
# index 3 → h  (take, jumped by -1)
# index 2 → t  (take, jumped by -1)
# index 1 → y  (take, jumped by -1)
# index 0 → P  (take, jumped by -1)
# Result: "nohtyP"

# Step = -2 → go backwards, every other character:
print(word[::-2])       # nhy
# index 5 → n  (take)
# index 3 → h  (take, jumped by -2)
# index 1 → y  (take, jumped by -2)
# index -1 → stop (beyond beginning)


# ------------------------------------------------------------
# PART 6: Default values change with negative step!
# ------------------------------------------------------------

# This is the trickiest part of step slicing.
# When step is POSITIVE:
#   default start = 0        (beginning)
#   default stop  = length   (end)
#   direction: left → right
#
# When step is NEGATIVE:
#   default start = length-1 (end of string)
#   default stop  = before index 0 (before beginning)
#   direction: right → left

word = "Python"

# Positive step - left to right:
print(word[::1])        # Python  (start=0, stop=6, step=1)

# Negative step - right to left:
print(word[::-1])       # nohtyP  (start=5, stop=before 0, step=-1)

# This means:
# word[5::-1]  is the same as  word[::-1]  when going backwards
# Let's verify:
print(word[5::-1])      # nohtyP  ← same!
print(word[5:0:-1])     # nohty   ← stops BEFORE index 0, so no 'P'!
print(word[5:1:-1])     # noht    ← stops BEFORE index 1, so no 'y'!

# The "stop is excluded" rule still applies when going backwards!
# word[5:0:-1] means: start at 5, go backwards, stop BEFORE index 0
# So index 0 (P) is NOT included.


# ------------------------------------------------------------
# PART 7: Reversing strings - the most famous use of step=-1
# ------------------------------------------------------------

# word[::-1] is THE standard Python way to reverse a string.
# Every Python programmer knows this trick.

# Reverse any string:
print("Hello"[::-1])        # olleH
print("Python"[::-1])       # nohtyP
print("racecar"[::-1])      # racecar  ← same! it's a palindrome!
print("12345"[::-1])        # 54321
print("A"[::-1])            # A        ← single char, same

# Palindrome check using reversal:
word = "racecar"
is_palindrome = word == word[::-1]
print(is_palindrome)        # True  ← elegant one-liner!

word = "python"
is_palindrome = word == word[::-1]
print(is_palindrome)        # False

# This is FAR cleaner than comparing character by character!


# ------------------------------------------------------------
# PART 8: Combining start, stop and negative step
# ------------------------------------------------------------

# You can fully control where to start, where to stop,
# and how to step - even when going backwards.

word = "abcdefghij"
#  a  b  c  d  e  f  g  h  i  j
#  0  1  2  3  4  5  6  7  8  9

# From index 8 down to index 2 (not including 2), step -1:
print(word[8:2:-1])     # ihgfed
# 8→i, 7→h, 6→g, 5→f, 4→e, 3→d, stop before 2

# From index 9 down to index 0 (not including 0), step -2:
print(word[9:0:-2])     # jhfdb
# 9→j, 7→h, 5→f, 3→d, 1→b, stop before 0

# From index 8 down to the beginning, step -3:
print(word[8::-3])      # ifc
# wait - let's trace: 8→i, 5→f, 2→c, then -1 which is before stop=0? no...
# 8→i, 5→f, 2→c, next would be -1 which is before start of string → stop
# Result: ifc

# From index 7 backwards, every 2:
print(word[7:1:-2])     # hfd
# 7→h, 5→f, 3→d, stop before 1

# Tip: when mixing negative step with explicit start/stop,
# trace it carefully step by step.
# Remember: stop is ALWAYS excluded, regardless of direction.


# ------------------------------------------------------------
# PART 9: What happens with step = 0?
# ------------------------------------------------------------

# Step cannot be 0. It would mean "don't move" → infinite loop.
# Python raises a ValueError if you try step=0.

word = "Python"
# print(word[::0])
# ❌ ValueError: slice step cannot be zero

# Always make sure your step is non-zero!
# Positive step → left to right
# Negative step → right to left


# ------------------------------------------------------------
# PART 10: Useful step patterns - a reference guide
# ------------------------------------------------------------

text = "abcdefghij"
#       0123456789

# ── Every character (normal) ──
print(text[::1])        # abcdefghij

# ── Every 2nd character ──
print(text[::2])        # acegi

# ── Every 2nd character, starting at 1 ──
print(text[1::2])       # bdfhj

# ── Every 3rd character ──
print(text[::3])        # adgj

# ── Reversed ──
print(text[::-1])       # jihgfedcba

# ── Reversed, every 2nd ──
print(text[::-2])       # jhfdb

# ── First half only ──
print(text[:5])         # abcde   (no step needed)

# ── Second half only ──
print(text[5:])         # fghij   (no step needed)

# ── First half, every 2nd ──
print(text[:5:2])       # ace

# ── Last 4, reversed ──
print(text[-1:-5:-1])   # jihg


# ------------------------------------------------------------
# PART 11: Step with negative indexes
# ------------------------------------------------------------

# You can mix negative indexes and negative step freely.

word = "Python"
#  P  y  t  h  o  n
# -6 -5 -4 -3 -2 -1

# From -1 (last) to -6 (first), not including -6:
print(word[-1:-6:-1])   # nohty   ← reversed, but without P!
# -1→n, -2→o, -3→h, -4→t, -5→y, stop before -6 (which is P)

# From -1 to beginning (including P):
print(word[::-1])       # nohtyP  ← full reversal

# Every 2nd character from the end:
print(word[-1::-2])     # nht
# -1→n, -3→h, -5→t  → "nht"

# Combining positive start and negative step:
print(word[4::-1])      # ohtyP
# 4→o, 3→h, 2→t, 1→y, 0→P, stop


# ------------------------------------------------------------
# PART 12: Real world applications
# ------------------------------------------------------------

# ── Application 1: Check if a number is a palindrome ──
number_str = "12321"
is_palindrome = number_str == number_str[::-1]
print(is_palindrome)    # True

# ── Application 2: Extract every nth character from DNA ──
dna = "AATGCCGTATCG"
# Every 3rd character (first nucleotide of each codon):
first_bases = dna[::3]
print(first_bases)      # ACT  ← hmm wait let's trace
# 0→A, 3→G, 6→G, 9→C → "AGGC" actually! Let's verify:
print(dna[::3])         # AGGC  ← yes

# ── Application 3: Decode a simple cipher ──
# Every other character starting from 0 is the real message:
encoded = "Phyetlhloon"
decoded = encoded[::2]
print(decoded)          # Python  ← !

# ── Application 4: Reverse words display ──
name = "Anna"
reversed_name = name[::-1]
print(reversed_name)    # annA

# ── Application 5: Sample data at regular intervals ──
# Imagine measurements taken every second:
measurements = "0123456789"  # simplified as string
# Take every 3rd measurement:
sampled = measurements[::3]
print(sampled)          # 0369

# ── Application 6: Mirror a string ──
half = "Python"
mirrored = half + half[::-1]
print(mirrored)         # PythonnohtyP

# ── Application 7: Extract odd-position characters ──
text = "abcdefgh"
odd_positions  = text[1::2]   # indexes 1, 3, 5, 7
even_positions = text[0::2]   # indexes 0, 2, 4, 6
print(odd_positions)    # bdfh
print(even_positions)   # aceg


# ------------------------------------------------------------
# PART 13: Common mistakes with step slicing
# ------------------------------------------------------------

word = "Python"

# ── Mistake 1: Forgetting stop is excluded ──
# "I want from index 4 down to index 0 including index 0"
print(word[4:0:-1])     # ohty   ← P is NOT included!
print(word[4::-1])      # ohtyP  ← correct! omit stop to include index 0

# ── Mistake 2: Wrong direction ──
# Positive step but start > stop → empty string!
print(word[4:1:1])      # ""  ← can't go right when start is already right of stop
print(word[1:4:1])      # yth ← correct order for positive step

# Negative step but start < stop → empty string!
print(word[1:4:-1])     # ""  ← can't go left when start is already left of stop
print(word[4:1:-1])     # oht ← correct order for negative step

# ── Mistake 3: Confusing step=2 with skip=2 ──
# step=2 means "jump 2 positions" → you get every 2nd character
# It does NOT mean "skip 2 characters"
word = "abcdef"
print(word[::2])        # ace  ← every 2nd: a(skip b)c(skip d)e(skip f)
# step=2 → you take index 0, then jump +2 to index 2, then jump +2 to index 4

# ── Mistake 4: step=0 ──
# print(word[::0])      # ❌ ValueError: slice step cannot be zero


# ------------------------------------------------------------
# PART 14: Step slicing on other sequences (preview)
# ------------------------------------------------------------

# Everything you learned about step slicing on strings
# works IDENTICALLY on lists and tuples (Module 05).
# The syntax is exactly the same!

# String:
word = "Python"
print(word[::2])        # Pto

# List (preview - covered in Module 05):
# numbers = [0, 1, 2, 3, 4, 5]
# print(numbers[::2])   # [0, 2, 4]  ← same logic!

# So mastering string slicing now means you already
# understand list slicing when you get there!


# ------------------------------------------------------------
# PART 15: The complete slicing syntax summary
# ------------------------------------------------------------

# string[start:stop:step]
#
# start: where to begin (default: 0 for positive step, -1 for negative)
# stop:  where to end - EXCLUDED (default: end for positive, before start for negative)
# step:  jump size and direction (default: 1, cannot be 0)
#
# Quick reference:
# ┌─────────────────┬──────────────────────────────────┐
# │ Slice           │ Meaning                          │
# ├─────────────────┼──────────────────────────────────┤
# │ s[:]            │ full copy                        │
# │ s[::1]          │ full copy (explicit step=1)      │
# │ s[::-1]         │ reversed                         │
# │ s[::2]          │ every 2nd character              │
# │ s[1::2]         │ every 2nd, starting at index 1   │
# │ s[::-2]         │ every 2nd, reversed              │
# │ s[a:b]          │ from a to b (b excluded)         │
# │ s[a:b:n]        │ from a to b, every nth           │
# │ s[a:b:-1]       │ from a to b backwards (b excl.)  │
# └─────────────────┴──────────────────────────────────┘


# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ Full syntax: string[start:stop:step]
# ✅ step = how many positions to jump each time
# ✅ Default step = 1 (forward, one by one)
# ✅ Positive step → left to right
# ✅ Negative step → right to left
# ✅ step = 0 → ValueError (forbidden!)
# ✅ word[::-1]  → reverses the string (most famous trick!)
# ✅ word[::2]   → every other character
# ✅ word[::n]   → every nth character
# ✅ Stop is ALWAYS excluded, even with negative step
# ✅ With negative step: default start = last char, default stop = before first
# ✅ Wrong direction (positive step, start > stop) → empty string ""
# ✅ Works identically on lists and tuples (Module 05)