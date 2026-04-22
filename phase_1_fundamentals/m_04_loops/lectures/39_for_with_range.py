# ============================================================
# MODULE 04 | LECTURE 39 - for with range()
# ============================================================
# What you will learn:
# - Combining for loops with range() - the classic pattern
# - Using the loop index in calculations
# - Iterating over sequences by index
# - Building patterns and tables
# - Index-based access vs direct iteration
# - Modifying sequences using index
# - Parallel iteration using index
# - Two-dimensional iteration with nested range()
# - Common real-world patterns
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: Why combine for with range()?
# ------------------------------------------------------------

# We already know two ways to loop:
#
# WAY 1: for item in sequence   → direct iteration
#         Gives you each ITEM directly.
#         Simple and clean when you just need values.
#
# WAY 2: for i in range(n)     → index-based iteration
#         Gives you NUMBERS (indices).
#         Use when you need the position, not just the value.
#
# Combining them: for i in range(len(sequence))
#         Gives you INDICES to access any sequence.
#
# When do you NEED the index?
# 1. You need to know WHERE in the sequence you are
# 2. You need to access the PREVIOUS or NEXT element
# 3. You need to modify the sequence based on position
# 4. You need to compare elements at specific positions
# 5. You want to repeat something exactly N times
# 6. The loop body depends on the iteration NUMBER
#
# Visual comparison:
#
# Direct iteration:          Index-based:
# for fruit in fruits:       for i in range(len(fruits)):
#     print(fruit)               print(fruits[i])
#
# Both print the same values.
# But only index-based knows WHERE each item is.

# ------------------------------------------------------------
# PART 2: Basic pattern - for i in range(n)
# ------------------------------------------------------------

# The most fundamental pattern: repeat exactly N times.
# 'i' is the loop counter (0, 1, 2, ..., n-1).

# Example 1: Repeat a message N times

n = 5
for i in range(n):
    print(f"Repetition {i + 1} of {n}")

# Output:
# Repetition 1 of 5
# Repetition 2 of 5
# Repetition 3 of 5
# Repetition 4 of 5
# Repetition 5 of 5

# Example 2: Use index in calculation

for i in range(1, 11):
    square = i ** 2
    cube = i ** 3
    print(f"{i:3d} │ {square:5d} │ {cube:7d}")

# Output:
#   1 │     1 │       1
#   2 │     4 │       8
#   3 │     9 │      27
# ...
#  10 │   100 │    1000

# Example 3: Print a numbered list

items = ["DNA extraction", "PCR amplification",
         "Gel electrophoresis", "Sequencing", "Analysis"]

print("Lab Protocol:")
for i in range(len(items)):
    print(f"  Step {i + 1}: {items[i]}")

# Output:
#   Step 1: DNA extraction
#   Step 2: PCR amplification
#   Step 3: Gel electrophoresis
#   Step 4: Sequencing
#   Step 5: Analysis

# Example 4: Access by index vs direct

dna = "ATCGATCG"

# Direct - gives characters:
for base in dna:
    print(base, end=" ")
print()    # A T C G A T C G

# Index-based - gives positions AND characters:
for i in range(len(dna)):
    print(f"{i}:{dna[i]}", end=" ")
print()    # 0:A 1:T 2:C 3:G 4:A 5:T 6:C 7:G

# ------------------------------------------------------------
# PART 3: Using the index in calculations
# ------------------------------------------------------------

# The index 'i' itself can drive mathematical patterns.

# Example 1: Powers of 2

print("Powers of 2:")
for i in range(11):
    print(f"2^{i:2d} = {2**i:6d}")

# Output:
# 2^ 0 =      1
# 2^ 1 =      2
# ...
# 2^10 =   1024

# Example 2: Fibonacci using index

n = 10
a, b = 0, 1
print(f"\nFirst {n} Fibonacci numbers:")
for i in range(n):
    print(f"F({i:2d}) = {a:6d}")
    a, b = b, a + b

# Example 3: Alternating signs

print("\nAlternating series:")
total = 0
for i in range(1, 11):
    sign = (-1) ** (i + 1)    # alternates +1, -1, +1, -1...
    term = sign * (1 / i)
    total += term
    print(f"Term {i:2d}: {'+' if sign > 0 else '-'}1/{i} → running sum = {total:.6f}")

# This approximates ln(2) ≈ 0.693147

# Example 4: Sine wave visualization

import math

print("\nSine wave:")
for i in range(37):
    angle = i * 10    # degrees: 0, 10, 20, ..., 360
    radians = math.radians(angle)
    value = math.sin(radians)
    bar_pos = int(value * 10) + 10    # shift to center
    bar = " " * bar_pos + "●"
    print(f"{angle:3d}°: {bar}")

# Example 5: Index controls padding/indentation

print("\nIndented items:")
topics = ["loops", "range", "for with range", "while", "break"]
for i in range(len(topics)):
    indent = "  " * i
    print(f"{indent}→ {topics[i]}")

# Output:
# → loops
#   → range
#     → for with range
#       → while
#         → break

# ------------------------------------------------------------
# PART 4: Accessing elements by index
# ------------------------------------------------------------

# When you need the VALUE at a position, use sequence[i].

# Example 1: Print with index

amino_acids = ["Ala", "Gly", "Val", "Leu", "Ile",
               "Pro", "Phe", "Trp", "Met", "Ser"]

print("Amino acid list:")
for i in range(len(amino_acids)):
    print(f"  [{i:2d}] {amino_acids[i]}")

# Example 2: Check adjacent elements

temperatures = [20.1, 22.3, 19.8, 25.6, 24.1, 28.9, 27.4]

print("\nTemperature changes:")
for i in range(1, len(temperatures)):
    change = temperatures[i] - temperatures[i - 1]
    direction = "↑" if change > 0 else "↓"
    print(f"Day {i} → Day {i+1}: {temperatures[i-1]:.1f} → "
          f"{temperatures[i]:.1f} ({direction} {abs(change):.1f}°C)")

# Output:
# Day 1 → Day 2: 20.1 → 22.3 (↑ 2.2°C)
# Day 2 → Day 3: 22.3 → 19.8 (↓ 2.5°C)
# ...

# Example 3: Find index of maximum

values = [3.2, 7.8, 2.1, 9.4, 5.6, 9.4, 1.3]
max_val = values[0]
max_idx = 0

for i in range(len(values)):
    if values[i] > max_val:
        max_val = values[i]
        max_idx = i

print(f"\nMaximum value: {max_val} at index {max_idx}")

# Example 4: Check if sorted

numbers = [1, 3, 5, 7, 9, 11]
is_sorted = True
broken_at = -1

for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        broken_at = i
        break

if is_sorted:
    print(f"\n{numbers} is sorted ✅")
else:
    print(f"\n{numbers} breaks sort order at index {broken_at}")

# Example 5: Look-ahead and look-behind simultaneously

dna = "ATGATCGCTTAAATG"
print("\nDi-nucleotide context:")
for i in range(1, len(dna) - 1):
    prev = dna[i - 1]
    curr = dna[i]
    nxt = dna[i + 1]
    print(f"Position {i:2d}: ...{prev}[{curr}]{nxt}...")

# ------------------------------------------------------------
# PART 5: Building sequences with range()
# ------------------------------------------------------------

# Using index to BUILD something - the accumulator pattern.

# Example 1: Build a list of squares

squares = []
for i in range(1, 11):
    squares.append(i ** 2)
print(f"Squares: {squares}")
# Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# Example 2: Build a string from parts

bases = "ATCG"
result = ""
for i in range(5):
    result += bases[i % len(bases)]    # cycle through bases
print(f"Repeated: {result}")    # ATCGA

# Example 3: Build a multiplication table as nested list

size = 5
table = []
for i in range(1, size + 1):
    row = []
    for j in range(1, size + 1):
        row.append(i * j)
    table.append(row)

print("\nMultiplication table:")
for row in table:
    for val in row:
        print(f"{val:4d}", end="")
    print()

# Output:
#    1   2   3   4   5
#    2   4   6   8  10
#    3   6   9  12  15
#    4   8  12  16  20
#    5  10  15  20  25

# Example 4: Build a sequence step by step

print("\nBuilding number pyramid:")
for i in range(1, 6):
    row = ""
    for j in range(1, i + 1):
        row += str(j)
    print(row)

# Output:
# 1
# 12
# 123
# 1234
# 12345

# Example 5: Sieve of Eratosthenes

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i in range(2, limit + 1) if is_prime[i]]

primes = sieve(50)
print(f"\nPrimes up to 50: {primes}")

# ------------------------------------------------------------
# PART 6: Parallel iteration with range()
# ------------------------------------------------------------

# When you need to iterate over TWO sequences simultaneously
# and need the same index for both.

# Example 1: Two lists at same index

names = ["Anna", "Bob", "Carol", "David", "Eve"]
scores = [92, 78, 88, 95, 71]

print("Results:")
for i in range(len(names)):
    grade = "A" if scores[i] >= 90 else "B" if scores[i] >= 80 else "C"
    print(f"  {names[i]:<8}: {scores[i]:3d} ({grade})")

# Output:
#   Anna    :  92 (A)
#   Bob     :  78 (C)
#   Carol   :  88 (B)
#   David   :  95 (A)
#   Eve     :  71 (C)

# Example 2: Three parallel sequences

reagents = ["Buffer A", "Enzyme B", "Substrate C"]
volumes_ml = [10.0, 2.5, 5.0]
concentrations = [1.0, 0.5, 2.0]

print("\nReaction Mix:")
total_volume = 0
for i in range(len(reagents)):
    amount = volumes_ml[i] * concentrations[i]
    total_volume += volumes_ml[i]
    print(f"  {reagents[i]:<12}: {volumes_ml[i]:5.1f} mL × "
          f"{concentrations[i]:.1f} M = {amount:.1f} mmol")
print(f"  {'Total volume':<12}: {total_volume:.1f} mL")

# Example 3: Sequence comparison

seq1 = "ATCGATCG"
seq2 = "ATCGTTCG"

print(f"\nSequence alignment:")
print(f"  Seq1: {seq1}")
print(f"  Seq2: {seq2}")
print(f"  Diff: ", end="")

mismatches = 0
for i in range(min(len(seq1), len(seq2))):
    if seq1[i] != seq2[i]:
        print("X", end="")
        mismatches += 1
    else:
        print("|", end="")

identity = (1 - mismatches / max(len(seq1), len(seq2))) * 100
print(f"\n  Identity: {identity:.1f}%  ({mismatches} mismatches)")

# Example 4: Weighted average

weights = [0.3, 0.2, 0.5]    # must sum to 1.0
scores = [88, 92, 79]
labels = ["Midterm", "Lab", "Final"]

weighted_sum = 0
print("\nWeighted grade calculation:")
for i in range(len(scores)):
    contribution = scores[i] * weights[i]
    weighted_sum += contribution
    print(f"  {labels[i]:<10}: {scores[i]} × {weights[i]:.1f} = {contribution:.1f}")
print(f"  {'Weighted avg':<10}: {weighted_sum:.1f}")

# ------------------------------------------------------------
# PART 7: Modifying a sequence using range()
# ------------------------------------------------------------

# Direct iteration doesn't let you modify the original list.
# Index-based iteration lets you change elements in place.

# Example 1: Double all values

numbers = [1, 2, 3, 4, 5]
print(f"Before: {numbers}")

for i in range(len(numbers)):
    numbers[i] *= 2

print(f"After:  {numbers}")    # [2, 4, 6, 8, 10]

# ❌ Direct iteration CAN'T modify the list:
numbers2 = [1, 2, 3, 4, 5]
for num in numbers2:
    num *= 2    # only changes local variable, NOT the list!
print(f"Unchanged: {numbers2}")    # [1, 2, 3, 4, 5]

# Example 2: Normalize values (scale to 0-1 range)

data = [15, 42, 8, 73, 31, 56]
min_val = data[0]
max_val = data[0]

for val in data:
    if val < min_val:
        min_val = val
    if val > max_val:
        max_val = val

print(f"\nOriginal data: {data}")
normalized = []
for i in range(len(data)):
    norm = (data[i] - min_val) / (max_val - min_val)
    normalized.append(round(norm, 3))
print(f"Normalized:    {normalized}")

# Example 3: Replace specific values

sequence = ["ATG", "GCT", "XXX", "TAC", "XXX", "TAA"]
print(f"\nBefore fix: {sequence}")

for i in range(len(sequence)):
    if sequence[i] == "XXX":
        sequence[i] = "NNN"    # replace unknown codons

print(f"After fix:  {sequence}")

# Example 4: Bubble sort using range()

def bubble_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

data = [64, 34, 25, 12, 22, 11, 90]
print(f"\nUnsorted: {data}")
sorted_data = bubble_sort(data.copy())
print(f"Sorted:   {sorted_data}")

# ------------------------------------------------------------
# PART 8: Two-dimensional patterns
# ------------------------------------------------------------

# Nested range() loops create 2D patterns.
# Outer loop = rows, inner loop = columns.

# Example 1: Grid coordinates

print("Grid coordinates (3×3):")
for row in range(3):
    for col in range(3):
        print(f"({row},{col})", end=" ")
    print()

# Output:
# (0,0) (0,1) (0,2)
# (1,0) (1,1) (1,2)
# (2,0) (2,1) (2,2)

# Example 2: Formatted multiplication table

print("\nMultiplication table (1-10):")
print("    ", end="")
for i in range(1, 11):
    print(f"{i:4d}", end="")
print()
print("    " + "----" * 10)

for i in range(1, 11):
    print(f"{i:3d}│", end="")
    for j in range(1, 11):
        print(f"{i*j:4d}", end="")
    print()

# Example 3: Identity matrix

size = 4
print(f"\nIdentity matrix ({size}×{size}):")
for i in range(size):
    for j in range(size):
        if i == j:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()

# Output:
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1

# Example 4: DNA matrix - pairwise identity

sequences = ["ATCGATCG", "ATCGTTCG", "AACGATCG", "ATCGATCC"]

print("\nPairwise identity matrix (%):")
print("       ", end="")
for i in range(len(sequences)):
    print(f"Seq{i+1:1d} ", end="")
print()

for i in range(len(sequences)):
    print(f"Seq{i+1}: ", end="")
    for j in range(len(sequences)):
        seq_a = sequences[i]
        seq_b = sequences[j]
        matches = 0
        for k in range(len(seq_a)):
            if seq_a[k] == seq_b[k]:
                matches += 1
        identity = matches / len(seq_a) * 100
        print(f"{identity:5.1f}", end="")
    print()

# Output:
#        Seq1  Seq2  Seq3  Seq4
# Seq1: 100.0  75.0  87.5  87.5
# Seq2:  75.0 100.0  62.5  62.5
# ...

# Example 5: Pascal's triangle

print("\nPascal's Triangle (6 rows):")
rows = 6
triangle = []
for i in range(rows):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.append(row)

for i in range(rows):
    spaces = " " * (rows - i - 1) * 2
    values = "   ".join(str(v) for v in triangle[i])
    print(spaces + values)

# Output:
#           1
#         1   1
#       1   2   1
#     1   3   3   1
#   1   4   6   4   1
# 1   5  10  10   5   1

# ------------------------------------------------------------
# PART 9: Common for+range() patterns
# ------------------------------------------------------------

# Pattern 1: Process every Nth element

sequence = "ATCGATCGATCGATCG"
n = 3    # every 3rd base

print(f"Every {n}rd base of '{sequence}':")
for i in range(0, len(sequence), n):
    print(f"  Position {i:2d}: {sequence[i]}")

# Pattern 2: Process in chunks

data = list(range(1, 21))    # 1 to 20
chunk_size = 4

print(f"\nData in chunks of {chunk_size}:")
for i in range(0, len(data), chunk_size):
    chunk = data[i:i + chunk_size]
    chunk_num = i // chunk_size + 1
    chunk_sum = sum(chunk)
    print(f"  Chunk {chunk_num}: {chunk} → sum = {chunk_sum}")

# Output:
#   Chunk 1: [1, 2, 3, 4] → sum = 10
#   Chunk 2: [5, 6, 7, 8] → sum = 26
#   Chunk 3: [9, 10, 11, 12] → sum = 42
#   Chunk 4: [13, 14, 15, 16] → sum = 58
#   Chunk 5: [17, 18, 19, 20] → sum = 74

# Pattern 3: Reverse using range

word = "bioinformatics"
reversed_word = ""
for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]
print(f"\n'{word}' reversed: '{reversed_word}'")

# Pattern 4: Sliding window

data = [1, 3, 5, 2, 8, 4, 7, 6]
window = 3

print(f"\nSliding window (size={window}) averages:")
for i in range(len(data) - window + 1):
    window_data = data[i:i + window]
    avg = sum(window_data) / window
    print(f"  Window {i+1}: {window_data} → avg = {avg:.2f}")

# Output:
#   Window 1: [1, 3, 5] → avg = 3.00
#   Window 2: [3, 5, 2] → avg = 3.33
#   Window 3: [5, 2, 8] → avg = 5.00
# ...

# Pattern 5: Running total with display

transactions = [100, -50, 200, -30, -80, 150, -20]
balance = 0

print("\nBank account transactions:")
print(f"{'Trans':>6} │ {'Amount':>8} │ {'Balance':>10}")
print("-" * 32)
for i in range(len(transactions)):
    balance += transactions[i]
    symbol = "+" if transactions[i] > 0 else ""
    print(f"{i+1:6d} │ {symbol}{transactions[i]:>7d} │ {balance:>10d}")

# ------------------------------------------------------------
# PART 10: for+range() in string processing
# ------------------------------------------------------------

# Using range() to process strings position by position.

# Example 1: Find all occurrences of a substring

text = "ATGATCATGATCGATG"
target = "ATG"
positions = []

for i in range(len(text) - len(target) + 1):
    if text[i:i + len(target)] == target:
        positions.append(i)

print(f"'{target}' found at positions: {positions}")
# 'ATG' found at positions: [0, 6, 13]

# Example 2: Count character frequency by position category

dna = "ATCGATCGATCG"
first_base_count = {"A": 0, "T": 0, "C": 0, "G": 0}

for i in range(0, len(dna), 3):    # every codon start (position 1)
    if dna[i] in first_base_count:
        first_base_count[dna[i]] += 1

print(f"\nFirst codon position base frequencies:")
for base, count in first_base_count.items():
    print(f"  {base}: {count}")

# Example 3: Palindrome check using range

def is_palindrome(s):
    s = s.lower()
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

words = ["racecar", "python", "madam", "level", "biology"]
for word in words:
    result = "✅ palindrome" if is_palindrome(word) else "❌ not palindrome"
    print(f"'{word}': {result}")

# Example 4: Caesar cipher with range

def caesar_encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted = chr((ord(char) - base + shift) % 26 + base)
            result += encrypted
        else:
            result += char
    return result

message = "Hello, World!"
shift = 13
encrypted = caesar_encrypt(message, shift)
decrypted = caesar_encrypt(encrypted, -shift)
print(f"\nOriginal:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")

# ------------------------------------------------------------
# PART 11: for+range() vs direct iteration - when to use which
# ------------------------------------------------------------

# DIRECT ITERATION (for item in sequence):
# ✅ You only need the VALUES, not positions
# ✅ Cleaner and more readable
# ✅ Works with any iterable (not just indexed sequences)
# ✅ Preferred in Python (more "Pythonic")

# INDEX-BASED (for i in range(len(sequence))):
# ✅ You need the INDEX (position number)
# ✅ You need to access ADJACENT elements (prev/next)
# ✅ You need to MODIFY the sequence in place
# ✅ You need to iterate MULTIPLE sequences in sync
# ✅ You need to start from a SPECIFIC position or skip positions

# Examples showing the difference:

scores = [88, 92, 78, 95, 84]

# Direct - clean when you just need values:
total = 0
for score in scores:
    total += score
print(f"\nDirect iteration - total: {total}")

# Index-based - needed when position matters:
print("Index-based - with rank:")
for i in range(len(scores)):
    print(f"  Rank {i+1}: {scores[i]}")

# Both are correct - choose based on what you need!

# The Pythonic preference:
# Python programmers prefer direct iteration when possible.
# Use enumerate() (Lecture 10) when you need BOTH index and value.
# Use range(len()) when you specifically need INDEX ARITHMETIC.

# ------------------------------------------------------------
# PART 12: Real-world use cases
# ------------------------------------------------------------

# Use case 1: GC content along a DNA sequence (sliding window)

dna = "ATGCGATACGCTTAAGGCCCCTAAATCGATCGATCG"
window_size = 6

print("GC content along sequence (window=6):")
print(f"Sequence: {dna}")
print("-" * 50)

for i in range(0, len(dna) - window_size + 1, 3):
    window = dna[i:i + window_size]
    gc = sum(1 for b in window if b in "GC")
    gc_pct = gc / window_size * 100
    bar = "█" * int(gc_pct / 10)
    print(f"Pos {i:2d}-{i+window_size-1:2d}: {window} │ "
          f"GC: {gc_pct:5.1f}% {bar}")

# Use case 2: Sequence alignment score

def alignment_score(seq1, seq2, match=2, mismatch=-1, gap=-2):
    score = 0
    length = min(len(seq1), len(seq2))
    alignment_str = ""

    for i in range(length):
        if seq1[i] == seq2[i]:
            score += match
            alignment_str += "|"
        elif seq1[i] == "-" or seq2[i] == "-":
            score += gap
            alignment_str += " "
        else:
            score += mismatch
            alignment_str += "."

    # gap penalty for length difference
    score += gap * abs(len(seq1) - len(seq2))

    return score, alignment_str

s1 = "ATCGATCG"
s2 = "ATCGTTCG"
score, alignment = alignment_score(s1, s2)

print(f"\nAlignment:")
print(f"  {s1}")
print(f"  {alignment}")
print(f"  {s2}")
print(f"  Score: {score}")

# Use case 3: Grade histogram

grades = [72, 85, 91, 68, 78, 95, 82, 65, 88, 74,
          93, 71, 87, 79, 96, 83, 69, 77, 90, 84]

buckets = {"A (90-100)": 0, "B (80-89)": 0,
           "C (70-79)": 0, "D (60-69)": 0, "F (<60)": 0}

for grade in grades:
    if grade >= 90:
        buckets["A (90-100)"] += 1
    elif grade >= 80:
        buckets["B (80-89)"] += 1
    elif grade >= 70:
        buckets["C (70-79)"] += 1
    elif grade >= 60:
        buckets["D (60-69)"] += 1
    else:
        buckets["F (<60)"] += 1

print("\nGrade Distribution:")
print("=" * 45)
for grade_range, count in buckets.items():
    bar = "█" * count
    print(f"{grade_range:15}: {bar:20} ({count:2d})")

# Use case 4: Matrix operations with range()

def matrix_multiply(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0] * cols_B for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = matrix_multiply(A, B)

print("\nMatrix multiplication:")
print(f"A = {A}")
print(f"B = {B}")
print("A × B =")
for row in C:
    print(f"  {row}")

# Output:
# A × B =
#   [19, 22]
#   [43, 50]

# Use case 5: Running statistics

data_stream = [23, 45, 12, 67, 34, 89, 56, 78, 90, 11]
running_sum = 0
running_max = data_stream[0]
running_min = data_stream[0]

print("\nRunning statistics:")
print(f"{'i':>3} │ {'val':>5} │ {'sum':>6} │ {'avg':>7} │ "
      f"{'min':>5} │ {'max':>5}")
print("-" * 45)

for i in range(len(data_stream)):
    val = data_stream[i]
    running_sum += val
    running_avg = running_sum / (i + 1)
    if val > running_max:
        running_max = val
    if val < running_min:
        running_min = val
    print(f"{i+1:3d} │ {val:5d} │ {running_sum:6d} │ "
          f"{running_avg:7.2f} │ {running_min:5d} │ {running_max:5d}")

# ------------------------------------------------------------
# PART 13: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Off-by-one with range(len())

items = ["a", "b", "c", "d", "e"]

# Wrong - goes one too far:
# for i in range(len(items) + 1):
#     print(items[i])    ← IndexError at i=5!

# ✅ Fix: range(len(items)) goes 0 to len-1
for i in range(len(items)):
    print(items[i], end=" ")
print()

# ❌ MISTAKE 2: Forgetting to handle adjacent elements at boundaries

numbers = [1, 2, 3, 4, 5]

# Wrong - crashes at last element:
# for i in range(len(numbers)):
#     print(numbers[i] + numbers[i+1])    ← IndexError at i=4!

# ✅ Fix: stop one before the end
for i in range(len(numbers) - 1):
    print(numbers[i] + numbers[i + 1], end=" ")
print()

# ❌ MISTAKE 3: Using index when direct iteration is cleaner

# Unnecessarily complex:
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(fruits[i])    # ← no index needed!

# ✅ Cleaner:
for fruit in fruits:
    print(fruit)

# ❌ MISTAKE 4: Wrong range for reverse

word = "Python"

# Wrong - range ends at -1 exclusive, so doesn't include 0:
# for i in range(len(word)-1, 0, -1):
#     print(word[i])    ← skips word[0] = 'P'!

# ✅ Fix: end at -1 to include index 0
for i in range(len(word) - 1, -1, -1):
    print(word[i], end="")
print()    # nohtyP

# ❌ MISTAKE 5: Forgetting range() produces integers

# range() gives integers, not floats:
for i in range(5):
    result = i / 4        # ✅ this is fine - int/int = float
    print(f"{i}/4 = {result:.2f}")

# But don't expect float step in range:
# for i in range(0.0, 1.0, 0.1):    ← TypeError!

# ✅ Use integer range and divide:
for i in range(0, 11):
    value = i / 10.0
    print(f"{value:.1f}", end=" ")
print()

# ❌ MISTAKE 6: Modifying list length while iterating by index

items = [1, 2, 3, 4, 5]
# Don't add/remove items while using range(len(items))!
# The range was computed at the START of the loop.

# ❌ MISTAKE 7: Using range(len()) on a string with slicing typo

text = "Hello"
# Wrong - range goes 0 to 4, but slicing [i:i+1] is still fine:
for i in range(len(text)):
    char = text[i:i+1]    # ✅ works, gets one char
    # char = text[i:i]    # ← gets empty string!
    print(char, end="")
print()

# ❌ MISTAKE 8: Nested range with wrong variable names

# Using same variable name in nested loops:
# for i in range(3):
#     for i in range(4):    ← outer 'i' is overwritten!
#         print(i)

# ✅ Use different names for nested loops:
for i in range(3):
    for j in range(4):    # ← different name
        print(f"({i},{j})", end=" ")
    print()

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ for i in range(n)        → repeat n times, i = 0..n-1
# ✅ for i in range(len(x))   → iterate over indices of x
# ✅ x[i]                     → access element at index i
# ✅ x[i-1], x[i+1]           → access neighbors
# ✅ for i in range(0,n,step) → every Nth position
# ✅ for i in range(n-1,-1,-1) → reverse order
# ✅ Nested range()            → 2D iteration (rows × cols)
# ✅ Use direct iteration when you only need values
# ✅ Use range(len()) when you need index arithmetic
# ✅ Don't add/remove items while iterating by index
# ✅ Off-by-one: range(len-1) for adjacent pair checks

# Quick reference:
# ┌──────────────────────────────────────────────────────────┐
# │ for i in range(n):          → 0, 1, ..., n-1            │
# │ for i in range(1, n+1):     → 1, 2, ..., n              │
# │ for i in range(len(lst)):   → all indices of lst         │
# │ for i in range(len(lst)-1): → all except last (pairs)   │
# │ for i in range(len-1,-1,-1):→ reverse indices           │
# │ for i in range(0,len,3):    → every 3rd index           │
# │                                                          │
# │ lst[i]            → access by index                     │
# │ lst[i-1], lst[i+1]→ neighbors                           │
# │ lst[i:i+n]        → chunk of n elements                 │
# │ lst[i] = value    → modify in place                     │
# └──────────────────────────────────────────────────────────┘