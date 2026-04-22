# ============================================================
# MODULE 04 | LECTURE 42 - continue
# ============================================================
# What you will learn:
# - What continue does and how it differs from break
# - continue in for loops
# - continue in while loops
# - continue with nested loops
# - continue vs if/else - when to use which
# - Common patterns: filtering, skipping, validation
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is continue?
# ------------------------------------------------------------

# In the previous lecture we learned that break
# exits the loop COMPLETELY.
#
# continue is different:
# It skips the REST of the current iteration
# and jumps straight to the NEXT one.
# The loop itself continues - only this one step is skipped.
#
# Real life analogy:
# ┌─────────────────────────────────────────────────────┐
# │ You're checking lab samples one by one.             │
# │                                                     │
# │ With break:                                         │
# │ "This sample is contaminated - STOP everything!     │
# │  Don't check any more samples."                     │
# │                                                     │
# │ With continue:                                      │
# │ "This sample is contaminated - SKIP it.             │
# │  Move on to the next sample."                       │
# └─────────────────────────────────────────────────────┘
#
# break  → exits the loop entirely
# continue → skips to next iteration (loop continues)
#
# Visual comparison:
#
# WITHOUT continue:            WITH continue:
# for item in items:           for item in items:
#     step_1                       if skip_condition:
#     step_2                           continue   ─┐
#     step_3                       step_1          │
#                                  step_2          │
#                                  step_3      ◄───┘ skipped!

# ------------------------------------------------------------
# PART 2: Basic continue syntax
# ------------------------------------------------------------

# Syntax:
#     for item in sequence:
#         if skip_condition:
#             continue     ← skips rest of THIS iteration
#         rest_of_body     ← only runs if continue not hit

# Simplest example - skip even numbers:

print("Odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i, end=" ")
print()

# Output: 1 3 5 7 9

# What happens step by step:
# i=1: 1%2==0? No  → print 1
# i=2: 2%2==0? Yes → continue → jump to i=3
# i=3: 3%2==0? No  → print 3
# i=4: 4%2==0? Yes → continue → jump to i=5
# ... etc.

# Equivalent WITHOUT continue (using if/else):

print("Same result without continue:")
for i in range(1, 11):
    if i % 2 != 0:  # opposite condition
        print(i, end=" ")
print()

# Both produce the same output.
# continue is useful when the "skip" logic is complex
# or when you want to avoid deep nesting.

# Visual flow diagram:
#
# for item in sequence:
#   ┌─────────────────────────────┐
#   │  if skip_condition:         │
#   │      continue ──────────────┼──→ next iteration
#   │  rest of body               │    (back to top of loop)
#   └─────────────────────────────┘
#   ↑ repeats for each item

# ------------------------------------------------------------
# PART 3: continue in for loops
# ------------------------------------------------------------

# Example 1: Skip negative numbers

numbers = [3, -1, 7, -5, 2, -8, 9, 4]
positive_sum = 0

print("Processing (skipping negatives):")
for num in numbers:
    if num < 0:
        print(f"  Skipping {num}")
        continue  # skip negative numbers
    positive_sum += num
    print(f"  Adding {num}, running sum = {positive_sum}")

print(f"Sum of positives: {positive_sum}")

# Output:
#   Adding 3, running sum = 3
#   Skipping -1
#   Adding 7, running sum = 10
#   Skipping -5
#   Adding 2, running sum = 12
#   Skipping -8
#   Adding 9, running sum = 21
#   Adding 4, running sum = 25
# Sum of positives: 25

# Example 2: Skip invalid DNA bases

dna_with_errors = "ATCGXATCGNNATCG"
valid_bases = "ATCG"
clean_dna = ""
skipped = 0

for base in dna_with_errors:
    if base not in valid_bases:
        skipped += 1
        continue  # skip invalid bases
    clean_dna += base

print(f"\nOriginal: {dna_with_errors}")
print(f"Cleaned:  {clean_dna}")
print(f"Skipped:  {skipped} invalid base(s)")

# Example 3: Skip items that don't meet criteria

students = [
    ("Anna", 92),
    ("Bob", 58),  # below passing
    ("Carol", 85),
    ("David", 45),  # below passing
    ("Eve", 91),
    ("Frank", 67),
]

passing_grade = 60
print("\nPassing students (>=60):")
for name, score in students:
    if score < passing_grade:
        print(f"  ⬜ {name}: {score} (failed - skipped)")
        continue  # skip failing students
    grade = "A" if score >= 90 else "B" if score >= 80 else "C"
    print(f"  ✅ {name}: {score} → Grade {grade}")

# Example 4: Skip duplicates

sequence = "AATCGGATCGATCGGCTA"
seen = []
unique_codons = []

for i in range(0, len(sequence) - 2, 3):
    codon = sequence[i:i + 3]
    if codon in seen:
        continue  # skip if already seen
    seen.append(codon)
    unique_codons.append(codon)

print(f"\nUnique codons: {unique_codons}")

# Example 5: Skip comments in "data"

data_lines = [
    "# This is a comment",
    "23.5",
    "# Another comment",
    "18.2",
    "31.7",
    "# Measurement taken at noon",
    "27.3",
]

measurements = []
for line in data_lines:
    if line.startswith("#"):
        continue  # skip comment lines
    measurements.append(float(line))

print(f"\nMeasurements: {measurements}")
print(f"Average: {sum(measurements) / len(measurements):.2f}")

# ------------------------------------------------------------
# PART 4: continue in while loops
# ------------------------------------------------------------

# continue in while loops jumps back to the condition check.
# Make sure the loop variable is updated BEFORE continue
# if it's used in the condition - or you'll get an infinite loop!

# Example 1: Basic while + continue

print("Odd numbers via while loop:")
i = 0
while i < 10:
    i += 1  # ← increment BEFORE the continue check!
    if i % 2 == 0:
        continue  # skip even - jumps back to while condition
    print(i, end=" ")
print()

# Output: 1 3 5 7 9

# ⚠ DANGER: update loop variable BEFORE continue
# If you put i += 1 AFTER the continue check,
# and continue triggers → i never increments → infinite loop!

# ❌ WRONG - infinite loop risk:
# i = 0
# while i < 10:
#     if i % 2 == 0:
#         continue     # i never increments for even numbers!
#     print(i)
#     i += 1

# ✅ CORRECT - increment before continue check:
i = 0
while i < 10:
    i += 1  # update FIRST
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# Example 2: Process user input, skip empty

print("\nEnter words (empty line = stop, 'skip' = skip that entry):")
words = []
while True:
    word = input("Word: ").strip()
    if word == "":
        break  # empty = stop the whole loop
    if word.lower() == "skip":
        print("  (skipped)")
        continue  # 'skip' = continue to next iteration
    words.append(word)
    print(f"  Added: '{word}'")

print(f"Words collected: {words}")

# Example 3: Skip failed computations

print("\nSafe division:")
dividends = [10, 20, 0, 30, 0, 40]
divisor = 5

i = 0
while i < len(dividends):
    if dividends[i] == 0:
        print(f"  Skipping 0 at index {i}")
        i += 1
        continue  # skip zero values
    result = dividends[i] / divisor
    print(f"  {dividends[i]} / {divisor} = {result}")
    i += 1

# Example 4: while with continue and accumulator

print("\nSum of squares of odd numbers from 1 to 20:")
n = 0
total = 0

while n < 20:
    n += 1
    if n % 2 == 0:
        continue  # skip even numbers
    total += n * n

print(f"Total: {total}")  # 1+9+25+49+...+361 = 1000

# ------------------------------------------------------------
# PART 5: continue vs if/else - when to use which
# ------------------------------------------------------------

# Both can achieve the same result.
# The choice is about readability and style.

# SCENARIO: Process a list, skip invalid items

data = [10, -3, 25, 0, 8, -7, 42]

# APPROACH 1: Using continue (guard clause style)
# Good when: "get the bad cases out of the way first"

print("Approach 1 - continue:")
results = []
for val in data:
    if val <= 0:
        continue  # guard: skip invalid
    results.append(val * 2)
print(results)

# APPROACH 2: Using if/else
# Good when: "two clear paths, roughly equal importance"

print("Approach 2 - if/else:")
results = []
for val in data:
    if val > 0:
        results.append(val * 2)  # process valid
    # else: skip (do nothing)
print(results)

# APPROACH 3: Using if without else
# Also valid - cleanest when only one case matters

print("Approach 3 - simple if:")
results = []
for val in data:
    if val > 0:
        results.append(val * 2)
print(results)

# All three produce the same result!

# When continue SHINES (avoids deep nesting):

# ❌ Without continue - deeply nested:
for val in data:
    if val > 0:
        if val < 100:
            if val % 2 == 0:
                print(f"  Processing {val}")  # 3 levels deep!

# ✅ With continue - flat structure:
for val in data:
    if val <= 0:
        continue
    if val >= 100:
        continue
    if val % 2 != 0:
        continue
    print(f"  Processing {val}")  # 0 levels of nesting!

# The "early exit" pattern with continue is called
# a "guard clause" - check for bad cases first,
# handle the main logic at the base level.

# RULE OF THUMB:
# Use continue when it REDUCES nesting or makes code clearer.
# Use if/else when both branches have similar importance.
# Use simple if when you only need one branch.

# ------------------------------------------------------------
# PART 6: continue for data cleaning
# ------------------------------------------------------------

# A very common real-world use: cleaning messy data.
# Skip rows/values that don't meet quality criteria.

# Example 1: Clean a dataset

raw_data = [
    "23.5",
    "N/A",
    "18.2",
    "ERROR",
    "31.7",
    "",
    "27.3",
    "MISSING",
    "25.1",
]

print("Data cleaning:")
clean_data = []
skipped_count = 0

for entry in raw_data:
    # Skip empty entries
    if not entry.strip():
        print(f"  ⬜ Empty entry - skipped")
        skipped_count += 1
        continue

    # Skip non-numeric entries
    try:
        value = float(entry)
    except ValueError:
        print(f"  ⬜ '{entry}' - not a number, skipped")
        skipped_count += 1
        continue

    # Skip out-of-range values
    if not (0 <= value <= 100):
        print(f"  ⬜ {value} - out of range [0,100], skipped")
        skipped_count += 1
        continue

    # Valid entry - process it
    clean_data.append(value)
    print(f"  ✅ {value} - added")

print(f"\nClean data: {clean_data}")
print(f"Skipped: {skipped_count} entries")
print(f"Mean: {sum(clean_data) / len(clean_data):.2f}")

# Example 2: Filter amino acids by property

protein = "MKTAYIAKQRQISFVKSHFSRQLEERLGLIEV"
hydrophobic = "AVILMFWP"
charged = "KRHDEC"

print(f"\nAmino acid classification for: {protein}")
print(f"{'AA':>3} │ {'Type':>12}")
print("-" * 20)

for aa in protein:
    if aa in hydrophobic:
        aa_type = "Hydrophobic"
    elif aa in charged:
        aa_type = "Charged"
    else:
        continue  # skip neutral/polar for this analysis
    print(f"{aa:>3} │ {aa_type:>12}")

# Example 3: Clean and process log file

log_entries = [
    "2024-01-15 09:00 INFO Server started",
    "2024-01-15 09:01 DEBUG Memory: 45%",
    "2024-01-15 09:02 INFO User logged in",
    "2024-01-15 09:03 DEBUG CPU: 12%",
    "2024-01-15 09:04 ERROR Database timeout",
    "2024-01-15 09:05 DEBUG Memory: 47%",
    "2024-01-15 09:06 WARNING High CPU: 89%",
    "2024-01-15 09:07 ERROR Connection failed",
]

print("\nErrors and Warnings only:")
for entry in log_entries:
    parts = entry.split()
    if len(parts) < 3:
        continue  # malformed line - skip
    level = parts[2]
    if level in ("DEBUG", "INFO"):
        continue  # skip routine logs
    print(f"  ⚠ {entry}")

# ------------------------------------------------------------
# PART 7: continue in nested loops
# ------------------------------------------------------------

# continue only affects the INNERMOST loop it's in.
# Just like break, it cannot skip outer loop iterations.

# Example 1: continue in inner loop only

print("Skipping specific cells in grid:")
for row in range(4):
    for col in range(4):
        if (row + col) % 2 == 0:
            print(".", end=" ")
            continue  # skip printing value for "black" squares
        print(f"{row * 4 + col}", end=" ")
    print()

# Example 2: Process matrix, skip diagonal

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("\nMatrix without diagonal:")
off_diagonal_sum = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == j:
            print("_", end=" ")
            continue  # skip diagonal elements
        off_diagonal_sum += matrix[i][j]
        print(matrix[i][j], end=" ")
    print()
print(f"Sum of off-diagonal: {off_diagonal_sum}")

# Example 3: Multi-sequence filtering

sequences = [
    "ATCGATCG",
    "NNATCGAT",  # has N's (unknown bases)
    "ATCGTTCG",
    "XXXXXXXX",  # all invalid
    "GCGCGCGC",
]

print("\nFiltering valid sequences:")
valid_seqs = []
for seq_idx in range(len(sequences)):
    seq = sequences[seq_idx]
    has_invalid = False

    for base in seq:
        if base not in "ATCG":
            has_invalid = True
            break  # found invalid base - exit inner loop

    if has_invalid:
        print(f"  Seq {seq_idx + 1}: '{seq}' - contains invalid bases, skipped")
        continue  # continue to next sequence (outer loop)

    valid_seqs.append(seq)
    print(f"  Seq {seq_idx + 1}: '{seq}' - ✅ valid")

print(f"\nValid sequences: {valid_seqs}")

# ------------------------------------------------------------
# PART 8: continue for formatting output
# ------------------------------------------------------------

# continue is useful for skipping items that don't
# need to be printed or when you want to control output flow.

# Example 1: Print every Nth item with continue

print("Every 3rd amino acid:")
protein = "MKTAYIAKQRQISFVKSHFSRQ"
for i in range(len(protein)):
    if i % 3 != 0:
        continue  # skip non-3rd positions
    print(f"  Position {i:2d}: {protein[i]}")

# Example 2: Skip items already printed

print("\nUnique bases in order of first appearance:")
dna = "ATCGATGCGATCG"
printed = []
for base in dna:
    if base in printed:
        continue  # already shown this base
    printed.append(base)
    print(f"  First occurrence of '{base}'")

# Example 3: Structured report with continue

print("\nStudent Performance Report:")
print("=" * 50)
class_data = [
    ("Anna", [92, 88, 95, 91]),
    ("Bob", [45, 52, 48, 50]),
    ("Carol", [78, 82, 80, 85]),
    ("David", [30, 25, 40, 35]),
    ("Eve", [96, 94, 98, 95]),
]

passing_threshold = 60

for name, grades in class_data:
    avg = sum(grades) / len(grades)
    if avg < passing_threshold:
        print(f"  ❌ {name}: {avg:.1f} - FAILED (not in honor roll report)")
        continue  # skip further analysis for failing students
    # Only reaches here for passing students
    grade = "A" if avg >= 90 else "B" if avg >= 80 else "C"
    consistency = max(grades) - min(grades)
    status = "Consistent" if consistency <= 10 else "Variable"
    print(f"  ✅ {name}: {avg:.1f} → {grade} | {status} "
          f"(range: {min(grades)}-{max(grades)})")

# ------------------------------------------------------------
# PART 9: continue vs break - side by side
# ------------------------------------------------------------

# Clear comparison to cement the difference:

numbers = [1, 2, 3, -1, 4, 5, -2, 6]

print("Original:", numbers)

# BREAK: exits loop at first negative
print("\nWith BREAK (exits at first negative):")
result = []
for n in numbers:
    if n < 0:
        print(f"  Negative {n} found - STOPPING")
        break  # exit entire loop
    result.append(n)
print(f"  Result: {result}")

# CONTINUE: skips negatives, processes rest
print("\nWith CONTINUE (skips negatives, continues):")
result = []
for n in numbers:
    if n < 0:
        print(f"  Negative {n} found - SKIPPING")
        continue  # skip this one, keep going
    result.append(n)
print(f"  Result: {result}")

# NEITHER: processes everything including negatives
print("\nWith NEITHER (processes everything):")
result = []
for n in numbers:
    result.append(abs(n))  # convert to absolute value
print(f"  Result: {result}")

# Summary:
# break:    [1, 2, 3]         ← stops before -1
# continue: [1, 2, 3, 4, 5, 6]  ← skips -1 and -2
# neither:  [1, 2, 3, 1, 4, 5, 2, 6] ← abs of all

# Decision guide:
# ┌────────────────────────────────────────────────────────┐
# │ "Stop processing everything" → break                   │
# │ "Skip this one item, keep going" → continue            │
# │ "Process everything" → neither                         │
# └────────────────────────────────────────────────────────┘

# ------------------------------------------------------------
# PART 10: continue with complex conditions
# ------------------------------------------------------------

# The continue condition can be as complex as any if condition.

# Example 1: Multiple skip conditions

data = [
    ("Sample_01", 7.2, 23.5, True),  # (name, pH, temp, is_control)
    ("Sample_02", 3.1, 37.0, False),  # invalid pH
    ("Sample_03", 7.4, 95.0, False),  # invalid temp
    ("Sample_04", 6.8, 25.0, True),  # control - skip
    ("Sample_05", 7.1, 22.8, False),  # valid
    ("Sample_06", None, 24.0, False),  # missing pH
]

print("Processing experimental samples:")
valid_samples = []

for name, ph, temp, is_control in data:
    # Skip control samples
    if is_control:
        print(f"  ⬜ {name}: Control sample - skipped")
        continue

    # Skip missing data
    if ph is None or temp is None:
        print(f"  ⬜ {name}: Missing data - skipped")
        continue

    # Skip out-of-range pH
    if not (6.5 <= ph <= 8.0):
        print(f"  ⬜ {name}: pH {ph} out of range [6.5-8.0] - skipped")
        continue

    # Skip extreme temperatures
    if not (15.0 <= temp <= 40.0):
        print(f"  ⬜ {name}: Temp {temp}°C out of range [15-40] - skipped")
        continue

    # Valid sample - process it
    valid_samples.append((name, ph, temp))
    print(f"  ✅ {name}: pH={ph}, temp={temp}°C")

print(f"\nValid samples: {len(valid_samples)}/{len(data)}")

# Example 2: Continue with string conditions

text = """
This is a paragraph about Python programming.
# This line is a comment.
Python is great for bioinformatics.

Another line about data science.
# Skip this too.
Final line.
"""

print("\nProcessed text (skipping empty/comment lines):")
word_count = 0
for line in text.split("\n"):
    stripped = line.strip()
    if not stripped:
        continue  # skip empty lines
    if stripped.startswith("#"):
        continue  # skip comment lines
    words = len(stripped.split())
    word_count += words
    print(f"  [{words:2d} words] {stripped}")

print(f"Total words: {word_count}")

# ------------------------------------------------------------
# PART 11: continue in string processing
# ------------------------------------------------------------

# Example 1: Build a clean version of a string

raw_string = "H3ll0 W0rld! Th1s 1s Pyth0n."
letters_only = ""

for char in raw_string:
    if char.isdigit():
        continue  # skip digits
    letters_only += char

print(f"Original:     {raw_string}")
print(f"Digits removed: {letters_only}")

# Example 2: Extract only uppercase letters

mixed = "ATCGatcgATCGatcg"
uppercase_only = ""
for char in mixed:
    if not char.isupper():
        continue
    uppercase_only += char
print(f"\nUppercase only: {uppercase_only}")

# Example 3: Tokenize with skip conditions

dna_with_spaces = "ATG CGT TAC   GGG  TAA"
codons = []

for token in dna_with_spaces.split():
    if not token:
        continue  # skip empty tokens from multiple spaces
    if len(token) != 3:
        continue  # skip tokens that aren't codons
    if any(b not in "ATCG" for b in token):
        continue  # skip invalid codons
    codons.append(token)

print(f"\nExtracted codons: {codons}")

# Example 4: Word frequency - skip short words

text = "The quick brown fox jumps over the lazy dog"
word_freq = {}

for word in text.lower().split():
    if len(word) <= 2:
        continue  # skip words of 2 chars or less ("the", "a")
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print(f"\nWord frequency (words >2 chars):")
for word, count in word_freq.items():
    print(f"  '{word}': {count}")

# ------------------------------------------------------------
# PART 12: Real-world use cases
# ------------------------------------------------------------

# Use case 1: Scientific data pipeline

print("\n=== Scientific Data Pipeline ===")

experiment_data = [
    {"id": "EXP001", "temp": 37.0, "ph": 7.2, "conc": 1.5, "valid": True},
    {"id": "EXP002", "temp": 95.0, "ph": 7.1, "conc": 1.3, "valid": True},
    {"id": "EXP003", "temp": 37.5, "ph": 3.0, "conc": 1.8, "valid": True},
    {"id": "EXP004", "temp": 36.8, "ph": 7.0, "conc": -0.5, "valid": True},
    {"id": "EXP005", "temp": 37.2, "ph": 7.3, "conc": 2.1, "valid": False},
    {"id": "EXP006", "temp": 37.1, "ph": 7.1, "conc": 1.6, "valid": True},
]

processed = []
skip_log = []

for exp in experiment_data:
    exp_id = exp["id"]

    if not exp["valid"]:
        skip_log.append((exp_id, "marked invalid"))
        continue

    if not (35.0 <= exp["temp"] <= 42.0):
        skip_log.append((exp_id, f"temp {exp['temp']} out of range"))
        continue

    if not (6.5 <= exp["ph"] <= 8.5):
        skip_log.append((exp_id, f"pH {exp['ph']} out of range"))
        continue

    if exp["conc"] <= 0:
        skip_log.append((exp_id, f"concentration {exp['conc']} invalid"))
        continue

    # Valid experiment - calculate result
    activity = (exp["conc"] * 100) / (1 + abs(exp["ph"] - 7.0))
    processed.append({**exp, "activity": round(activity, 2)})

print(f"Processed: {len(processed)} experiments")
print(f"Skipped:   {len(skip_log)} experiments")

print("\nSkip reasons:")
for exp_id, reason in skip_log:
    print(f"  {exp_id}: {reason}")

print("\nResults:")
for exp in processed:
    print(f"  {exp['id']}: activity = {exp['activity']:.2f}")

# Use case 2: DNA sequence batch processor

print("\n=== DNA Sequence Batch Processor ===")

batch = [
    ("seq_01", "ATGCGATACGCTTAA"),
    ("seq_02", "GCGCGCGC"),  # no start codon
    ("seq_03", "ATG" + "X" * 9),  # contains X
    ("seq_04", "ATGAAATTTGGG"),  # no stop codon
    ("seq_05", "ATGCGATACGCTTAA"),  # duplicate of seq_01
    ("seq_06", "ATGGCCTAA"),
]

seen_sequences = []
results = []

for seq_id, sequence in batch:
    seq = sequence.upper()

    # Skip sequences with invalid characters
    if any(b not in "ATCG" for b in seq):
        print(f"  {seq_id}: ❌ Invalid characters - skipped")
        continue

    # Skip sequences without start codon
    if not seq.startswith("ATG"):
        print(f"  {seq_id}: ❌ No start codon - skipped")
        continue

    # Skip sequences without stop codon
    has_stop = False
    for i in range(0, len(seq) - 2, 3):
        if seq[i:i + 3] in ("TAA", "TAG", "TGA"):
            has_stop = True
            break
    if not has_stop:
        print(f"  {seq_id}: ❌ No stop codon - skipped")
        continue

    # Skip duplicate sequences
    if seq in seen_sequences:
        print(f"  {seq_id}: ❌ Duplicate sequence - skipped")
        continue

    # Valid sequence
    seen_sequences.append(seq)
    gc = sum(1 for b in seq if b in "GC") / len(seq) * 100
    results.append((seq_id, seq, gc))
    print(f"  {seq_id}: ✅ Valid | Length={len(seq)} | GC={gc:.1f}%")

print(f"\nValid sequences: {len(results)}/{len(batch)}")

# Use case 3: Real-time data stream simulator

print("\n=== Sensor Data Stream ===")
import random

random.seed(42)


# Simulate a stream of sensor readings
def generate_reading():
    return round(random.gauss(37.0, 2.5), 1)  # mean=37, std=2.5


readings_collected = []
total_generated = 0
target_count = 10

print(f"Collecting {target_count} valid readings...")
print(f"Valid range: 35.0°C - 39.0°C")
print()

while len(readings_collected) < target_count:
    reading = generate_reading()
    total_generated += 1

    if reading < 35.0 or reading > 39.0:
        print(f"  Reading {total_generated:3d}: {reading:5.1f}°C "
              f"- OUT OF RANGE, skipped")
        continue  # skip out-of-range readings

    readings_collected.append(reading)
    print(f"  Reading {total_generated:3d}: {reading:5.1f}°C "
          f"- ✅ collected ({len(readings_collected)}/{target_count})")

mean_temp = sum(readings_collected) / len(readings_collected)
print(f"\nCollection complete!")
print(f"Total generated: {total_generated}")
print(f"Valid collected: {len(readings_collected)}")
print(f"Rejection rate:  {(total_generated - target_count) / total_generated * 100:.1f}%")
print(f"Mean temperature: {mean_temp:.2f}°C")

# ------------------------------------------------------------
# PART 13: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Using break when continue is needed
# (stops everything instead of just skipping one item)

numbers = [3, -1, 5, -2, 8]

# Wrong - stops at first negative:
print("\nWrong (break stops at negative):")
for n in numbers:
    if n < 0:
        break  # stops everything!
    print(n, end=" ")
print()  # 3

# ✅ Correct - continue skips negative:
print("Correct (continue skips negative):")
for n in numbers:
    if n < 0:
        continue  # skips this one
    print(n, end=" ")
print()  # 3 5 8

# ❌ MISTAKE 2: Infinite loop - not updating loop variable before continue

# i = 0
# while i < 10:
#     if i % 2 == 0:
#         continue    # i never increments for even i!
#     print(i)
#     i += 1         # ← only reached for odd i

# ✅ Fix: update BEFORE the continue check
i = 0
while i < 10:
    i += 1  # ← update FIRST
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# ❌ MISTAKE 3: Thinking continue exits the loop

for i in range(5):
    if i == 3:
        continue  # doesn't exit! just skips to i=4
    print(i, end=" ")
print()
# Output: 0 1 2 4  ← 3 is skipped, 4 is still printed

# ❌ MISTAKE 4: continue outside a loop

# continue    ← SyntaxError! must be inside a loop

# ❌ MISTAKE 5: Unnecessary continue at end of loop body

for i in range(5):
    print(i)
    continue  # ← pointless! loop would continue anyway

# ✅ Fix: just remove it
for i in range(5):
    print(i)

# ❌ MISTAKE 6: Code after continue is unreachable

for i in range(5):
    if i < 3:
        continue
        print("Never prints!")  # unreachable!
    print(i)

# ✅ Fix: don't put code after continue
for i in range(5):
    if i < 3:
        continue
    print(i)  # only runs when i >= 3

# ❌ MISTAKE 7: continue only affects INNERMOST loop

for i in range(3):
    for j in range(3):
        if j == 1:
            continue  # skips j=1 in inner loop only
        print(f"({i},{j})", end=" ")
    print()

# Output:
# (0,0) (0,2)
# (1,0) (1,2)
# (2,0) (2,2)
# The outer loop is NOT affected by continue in the inner loop!

# ❌ MISTAKE 8: Using continue when a simple if is cleaner

# Overly complex with continue:
for i in range(10):
    if i % 2 == 0:
        continue
    print(i, end=" ")
print()

# Simpler without continue:
for i in range(1, 10, 2):  # just use the right range!
    print(i, end=" ")
print()

# Or with simple if:
for i in range(10):
    if i % 2 != 0:
        print(i, end=" ")
print()

# continue is best when skipping is the "exception"
# and processing is the "rule".

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ continue skips REST of current iteration, loop continues
# ✅ Works in both for and while loops
# ✅ Affects only the INNERMOST loop
# ✅ In while loops: update loop variable BEFORE continue
# ✅ continue ≠ break:
#    continue → skip this iteration, keep looping
#    break    → exit the entire loop
# ✅ Great for: filtering, data cleaning, guard clauses
# ✅ Reduces nesting when used as "guard clause"
# ✅ Code after continue in the loop body is unreachable
# ✅ Sometimes simple if is cleaner than continue

# Quick reference:
# ┌──────────────────────────────────────────────────────────┐
# │ for item in sequence:                                    │
# │     if skip_condition:                                   │
# │         continue   ──────────────────→ next iteration    │
# │     process_item   ← only runs if no continue           │
# │                                                          │
# │ while condition:                                         │
# │     counter += 1   ← update BEFORE continue!            │
# │     if skip_condition:                                   │
# │         continue   ──────────────────→ recheck condition │
# │     process        ← only runs if no continue           │
# │                                                          │
# │ continue vs break:                                       │
# │   continue → skip this one, keep going                  │
# │   break    → stop everything                            │
# │                                                          │
# │ Guard clause pattern:                                    │
# │   for x in data:                                        │
# │       if bad_condition_1: continue   ← check bad first  │
# │       if bad_condition_2: continue   ← then more checks │
# │       process(x)                    ← clean logic here  │
# └──────────────────────────────────────────────────────────┘