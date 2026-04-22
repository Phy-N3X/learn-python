# ============================================================
# MODULE 04 | EXERCISES 44 - else in loops
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output of each code block BEFORE running.
# Write your prediction as a comment.
# Then run and verify.
#
# # Block A:
# for i in range(4):
#     print(i, end=" ")
# else:
#     print("ELSE_A")
# # prediction: ?
#
# # Block B:
# for i in range(4):
#     if i == 2:
#         break
#     print(i, end=" ")
# else:
#     print("ELSE_B")
# # prediction: ?
#
# # Block C:
# for i in range(4):
#     if i == 2:
#         continue
#     print(i, end=" ")
# else:
#     print("ELSE_C")
# # prediction: ?
#
# # Block D:
# for i in []:
#     print(i)
# else:
#     print("ELSE_D")
# # prediction: ?
#
# # Block E:
# n = 5
# while n > 0:
#     print(n, end=" ")
#     n -= 1
# else:
#     print("ELSE_E")
# # prediction: ?
#
# # Block F:
# n = 5
# while n > 0:
#     if n == 3:
#         break
#     print(n, end=" ")
#     n -= 1
# else:
#     print("ELSE_F")
# # prediction: ?
#
# Final questions (answer as comments):
# Why does Block C print "ELSE_C" even though continue was used?
# Why does Block D print "ELSE_D" even though the loop never ran?
# What's the ONE thing that prevents else from running?

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Rewrite these flag-variable search patterns
# using for/else instead. Keep the same behavior.
#
# # Pattern 1 - rewrite with for/else:
# target = "banana"
# fruits = ["apple", "cherry", "date", "elderberry"]
# found = False
# for fruit in fruits:
#     if fruit == target:
#         found = True
#         break
# if found:
#     print(f"Found: {target}")
# else:
#     print(f"Not found: {target}")
#
# # Pattern 2 - rewrite with while/else:
# numbers = [3, 7, 15, 22, 31]
# target = 15
# i = 0
# found = False
# while i < len(numbers):
#     if numbers[i] == target:
#         found = True
#         break
#     i += 1
# if not found:
#     print(f"{target} not in list")
# else:
#     print(f"Found {target} at index {i}")
#
# # Pattern 3 - rewrite with for/else:
# dna = "ATCGATCG"
# has_start = False
# for i in range(0, len(dna)-2, 3):
#     if dna[i:i+3] == "ATG":
#         has_start = True
#         break
# if has_start:
#     print("Start codon found!")
# else:
#     print("No start codon")

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL errors in the code below.
# Write what each error is as a comment.
# Then fix all errors.
#
# # Error set 1:
# for i in range(5):
#     if i == 3:
#         break
# else:
#     print("loop ended")
# else:
#     print("duplicate else!")
#
# # Error set 2:
# items = [1, 2, 3]
# for item in items:
#     pass
#     else:            # indented under pass - wrong!
#         print("done")
#
# # Error set 3 - logical error:
# # This should print "not found" if target not in list
# # But it has a bug - what is it?
# target = 5
# numbers = [1, 2, 3, 4, 6, 7]
# for n in numbers:
#     if n == target:
#         print(f"Found {target}!")
# else:
#     print(f"{target} not found")    # this always prints!

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use for/else to implement a DNA codon searcher.
# Search for specific codons in a DNA sequence.
#
# dna = "ATCGATGCGATACGCTTAAGGCCCCTAA"
#
# For each codon in this list, search in the DNA sequence
# (reading in frame, every 3 bases from position 0):
# codons_to_find = ["ATG", "TAA", "GGG", "CGA", "TTT"]
#
# For each codon:
# - Search through the sequence in codons (step 3)
# - Use for/else: if found → print position, if not → print "not found"
#
# Expected output format:
# Searching for 'ATG': found at position 6 (codon #3)
# Searching for 'TAA': found at position 24 (codon #9)
# Searching for 'GGG': not found in reading frame
# Searching for 'CGA': found at position 3 (codon #2)
# Searching for 'TTT': not found in reading frame

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Use for/else to check if a number is prime.
# Ask the user for a number.
# Use the classic for/else primality test.
#
# For primality check: test divisors from 2 to √n
# If any divisor found → not prime (break)
# else → it is prime
#
# After checking primality:
# - If prime: print "X is prime! ✅"
# - If not prime: print "X is not prime. Smallest factor: Y"
#   (where Y is the smallest divisor found)
#
# Also: print all prime numbers from 2 to N
# using the same for/else technique.
#
# Example interaction:
# Enter a number: 17
# 17 is prime! ✅
# Primes up to 17: 2 3 5 7 11 13 17

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build an experiment validator using for/else.
# Check if experimental conditions are all within range.
#
# Create a list of (parameter_name, value, min_allowed, max_allowed) tuples:
# conditions = [
#     ("Temperature", 37.2, 36.0, 38.5),
#     ("pH", 7.1, 6.8, 7.6),
#     ("Incubation_time_min", 45, 30, 60),
#     ("Volume_ul", 150, 100, 200),
#     ("Concentration_mM", 0.5, 0.1, 1.0),
# ]
#
# Use for/else to validate ALL conditions at once:
# - Loop through conditions
# - If any fails → print specific error and break
# - else (all pass) → print "All conditions validated - proceed!"
#
# Test 1: All conditions valid (as given above)
# Test 2: Change pH to 9.0 (invalid) - should fail at pH check
# Test 3: Change Temperature to 35.0 AND Concentration to 2.0
#         (both invalid - should fail at FIRST failure)
#
# For each test, print which condition failed and why.

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Use while/else to implement a retry mechanism.
# Simulate network requests that sometimes fail.
#
# import random
# random.seed(42)
#
# def make_request(url):
#     """Simulates a network request. Returns True ~40% of the time."""
#     return random.random() < 0.4
#
# Use while/else to retry up to MAX_RETRIES times:
# - If request succeeds → print success + which attempt, break
# - If max retries exceeded → while condition becomes False → else runs
# - else block: print "All retries exhausted"
#
# Test with these URLs and max_retries values:
# ("https://api.lab.com/samples", 3)
# ("https://db.research.org/data", 5)
# ("https://fastserver.com/api", 10)
#
# For each URL, also print:
# - Total attempts made
# - Whether it succeeded or failed
# - Success rate (based on random seed, track actual)

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a password strength checker using for/else.
# Check multiple password requirements.
#
# Requirements to check (in order):
# 1. Length >= 12 characters
# 2. Contains at least one uppercase letter (A-Z)
# 3. Contains at least one lowercase letter (a-z)
# 4. Contains at least one digit (0-9)
# 5. Contains at least one special character (!@#$%^&*())
# 6. Does NOT contain spaces
# 7. Does NOT contain the word "password" (case insensitive)
# 8. Does NOT have 3 or more consecutive identical characters
#
# Use for/else over a list of (check_name, check_function) pairs:
# - If any check fails → print failure reason, break
# - else → "Strong password! All requirements met."
#
# Test these passwords:
# "Short1!"
# "LongButNoSpecialChar123"
# "ValidStr0ng!Pass#word"
# "ValidStr0ng!Pass#"
# "NoConsecutive123!@#"
# "aaa_bad_triple_123!"
#
# For each, print the first failed requirement (or "strong").

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this for/else code and predict ALL outputs.
# Write predictions as comments before each section.
# Then run and verify.
#
# # Section A:
# data = [4, 8, 15, 16, 23, 42]
# for val in data:
#     if val > 20:
#         print(f"First value > 20: {val}")
#         break
# else:
#     print("No value > 20 found")
# # prediction: ?
#
# # Section B:
# primes_found = 0
# for n in range(10, 20):
#     for d in range(2, n):
#         if n % d == 0:
#             break
#     else:
#         primes_found += 1
#         print(f"Prime: {n}")
# print(f"Total primes: {primes_found}")
# # prediction: which primes? total count?
#
# # Section C:
# sequences = ["ATCG", "NNATG", "GCGC"]
# for seq in sequences:
#     for base in seq:
#         if base not in "ATCG":
#             print(f"Invalid: '{seq}'")
#             break
#     else:
#         print(f"Valid: '{seq}'")
# # prediction: ?
#
# # Section D:
# n = 10
# while n > 0:
#     n -= 3
#     if n < 0:
#         break
# else:
#     print("while else ran")
# print(f"Final n: {n}")
# # prediction: does else run? what is n?
#
# Answer as comments:
# In Section B, why does the INNER else add to primes_found?
# In Section D, does the while condition or the break stop the loop?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a multi-criteria data validator using for/else.
#
# You have a dataset of protein measurements:
# proteins = [
#     {"id": "P001", "sequence": "MKTAYIAK", "mw": 850.5,
#      "pi": 7.2, "stability": "stable"},
#     {"id": "P002", "sequence": "MKT", "mw": 350.1,
#      "pi": 5.5, "stability": "unstable"},
#     {"id": "P003", "sequence": "MKTAYIAKQRQISFVK", "mw": 1850.2,
#      "pi": 8.9, "stability": "stable"},
#     {"id": "P004", "sequence": "BKTAYIAK", "mw": 900.0,
#      "pi": 7.1, "stability": "stable"},
#     {"id": "P005", "sequence": "MKTAYIAKQRQISFVKSHFS", "mw": 2250.8,
#      "pi": 6.8, "stability": "stable"},
# ]
#
# Validation criteria (check in this order, stop at first failure):
# 1. Sequence length >= 8 amino acids
# 2. Sequence starts with 'M' (Methionine - start)
# 3. Sequence contains only valid amino acid codes (ACDEFGHIKLMNPQRSTVWY)
# 4. Molecular weight matches length estimate (length * 110 ± 15%)
# 5. pI must be between 4.0 and 12.0
# 6. Stability must be "stable" or "unstable" or "partially stable"
#
# For each protein:
# - Use for/else over the criteria list
# - If any fails → record failure with reason
# - else → add to valid_proteins list
#
# After processing:
# - Print table of valid proteins with all properties
# - Print list of failed proteins with their failure reasons
# - Print summary statistics

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a sequence alignment verifier using for/else.
# Verify that a proposed pairwise alignment is valid.
#
# An alignment consists of two strings of equal length
# where gaps are represented by '-'.
#
# Alignment validity rules:
# 1. Both strings must be the same length
# 2. Neither string can start or end with a gap
# 3. No column can have gaps in BOTH sequences simultaneously
# 4. Maximum gap length in any single run is 5
# 5. Alignment identity must be > 30% (non-gap matches / alignment length)
# 6. Aligned characters (no gaps) must be valid nucleotides or amino acids
#
# Test these alignments:
# alignment_1 = ("ATCG--ATCG", "ATCGATCG--")    # ends with gap
# alignment_2 = ("ATCG--ATCG", "ATCG-AATCG")    # different lengths
# alignment_3 = ("ATCG--ATCG", "ATCG--ATCG")    # both gapped in same column
# alignment_4 = ("ATCGATCGATCG", "ATCGATCGATCG") # perfect alignment
# alignment_5 = ("ATCG------ATCG", "ATCGATCGATCG--") # gap too long
#
# For each alignment, use for/else to check each rule in order.
# If a rule fails → explain which rule and why → break
# else → print "Valid alignment! Identity: X%"
# Also show the alignment visually with | for matches, X for mismatches.

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a prime factorization tool using while/else.
#
# For a number N, find its complete prime factorization.
# Use nested while loops with else clauses.
#
# Algorithm:
# - Start with divisor = 2
# - While divisor² <= N:
#     - While N is divisible by divisor:
#         - Record divisor as factor
#         - Divide N by divisor
#     - Increment divisor
# - If N > 1: N itself is a prime factor
#
# Use while/else to:
# - Detect when N is prime (the outer while else runs and N > 1)
# - Detect when all factors are found
# - Find the largest prime factor
#
# For each number, print:
# - The factorization: N = p1^e1 × p2^e2 × ...
# - Whether N is prime (special case)
# - Number of distinct prime factors
# - Sum of prime factors (with repetition)
# - Product verification: multiply all factors back
#
# Test with: 1, 2, 12, 36, 100, 360, 1000, 9973 (prime), 999983 (prime)

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Create a comprehensive DNA ORF validator using for/else.
#
# An ORF (Open Reading Frame) must satisfy these criteria:
# 1. Must start with ATG
# 2. Must end with a stop codon (TAA, TAG, or TGA)
# 3. Length must be divisible by 3
# 4. Length must be at least 18 bp (6 codons minimum)
# 5. Must not contain internal stop codons (except the final one)
# 6. GC content must be between 30% and 75%
# 7. No single nucleotide run longer than 6 bases (e.g., AAAAAAA is invalid)
# 8. First codon after ATG must not be a stop codon (protein must be > 1 aa)
#
# Test these candidate ORFs:
# candidates = [
#     "ATGAAATTTGGGCCCTAA",                   # valid
#     "GCTATGAAATTTGGGCCCTAA",                # doesn't start with ATG
#     "ATGAAATTTGGGCCC",                      # no stop codon
#     "ATGTAA",                               # too short (6 bp)
#     "ATGAAATAATTTGGGCCCTAA",               # internal stop codon
#     "ATGAAATTTGGGCCCTAAAAAAAAAATAA",       # long poly-A run
#     "ATGAAATTTGGGCCCGGGAAATTTGGGCCCTAA",  # check GC content
#     "ATGCGCGCGCGCGCGCGCGCGCGCGCGCGCTAA", # high GC
# ]
#
# For each candidate, use for/else over the criteria list:
# - If any criterion fails → print which criterion and why, break
# - else → print "Valid ORF! [statistics]"
#
# Statistics for valid ORFs:
# - Length in bp and codons
# - GC content
# - Predicted protein length (codons - 1, excluding stop)
# - Estimated molecular weight (protein length × 110 Da)

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a complete sequence database search system
# using for/else at multiple levels.
#
# Database of protein sequences:
# protein_db = {
#     "UniProt:P00533": {"name": "EGFR", "organism": "Homo sapiens",
#                         "sequence": "MRPSGTAGAALLALLAALCPASRALEEKKVC",
#                         "function": "receptor tyrosine kinase",
#                         "length": 1210},
#     "UniProt:P01308": {"name": "INS", "organism": "Homo sapiens",
#                         "sequence": "MALWMRLLPLLALLALWGPDPAAAFVNQHLC",
#                         "function": "glucose metabolism",
#                         "length": 110},
#     "UniProt:P68871": {"name": "HBB", "organism": "Homo sapiens",
#                         "sequence": "MVHLTPEEKSAVTALWGKVNVDEVGGEALG",
#                         "function": "oxygen transport",
#                         "length": 147},
#     "UniProt:P00533_M": {"name": "EGFR_MOUSE", "organism": "Mus musculus",
#                           "sequence": "MRPSGTAGAALLALLAALCPASRALEEKKVC",
#                           "function": "receptor tyrosine kinase",
#                           "length": 1211},
# }
#
# Implement these search functions, each using for/else:
#
# 1. search_by_name(query):
#    Find all proteins where query appears in name (case insensitive)
#    Use for/else: else prints "No proteins found with name: query"
#
# 2. search_by_function(keyword):
#    Find proteins whose function description contains keyword
#    Use for/else: else prints "No proteins with function: keyword"
#
# 3. search_by_sequence_motif(motif):
#    Find proteins containing exact motif in their sequence
#    Use nested for/else:
#    - outer: over all proteins
#    - inner: over sequence positions to find motif
#    - inner else: this protein doesn't have the motif
#
# 4. search_by_criteria(organism=None, min_length=0, max_length=99999,
#                        function_keyword=None):
#    Find proteins matching ALL given criteria
#    Use for/else over criteria list:
#    - If protein fails any criterion → continue to next protein
#    - else (all criteria passed) → add to results
#
# 5. find_similar_sequences(query_id, min_identity=0.7):
#    Compare query sequence to all others
#    Use for/else: else prints "No similar sequences found"
#    Identity = matching characters / shorter sequence length
#
# For each search function:
# - Print results in a formatted table
# - Show total hits found
# - Show search time (iteration count, not real time)

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a complete constraint satisfaction solver
# using nested for/else loops.
#
# Problem: Schedule laboratory experiments.
# You have:
# - 4 time slots: ["9:00", "11:00", "14:00", "16:00"]
# - 4 instruments: ["PCR", "Centrifuge", "Spectro", "HPLC"]
# - 4 researchers: ["Anna", "Bob", "Carol", "David"]
# - 4 experiments: ["EXP001", "EXP002", "EXP003", "EXP004"]
#
# Constraints to satisfy (check with for/else):
# 1. Each time slot has exactly one experiment
# 2. Each instrument is used at most once
# 3. Each researcher works at most once
# 4. Specific requirements (hard constraints):
#    - EXP001 requires PCR machine
#    - EXP002 requires HPLC
#    - Anna cannot work in the 9:00 slot (personal constraint)
#    - Bob and Carol cannot work in adjacent time slots
#    - EXP003 and EXP004 cannot use the same instrument type
#      (both need the spectrophotometer - create conflict intentionally)
#    - David must work before Carol in the schedule
#
# Algorithm (backtracking with for/else):
# - Try to assign one experiment per time slot
# - For each slot, try all possible (experiment, instrument, researcher) combos
# - Use for/else: if no valid assignment found → else prints "backtrack"
#   and return False (need to try different assignment for previous slot)
# - If all slots assigned → print schedule
#
# Implementation:
# - Use recursive approach with for/else at each level
# - Track all attempted assignments (for debugging)
# - Print the search process (which assignments were tried)
# - Print the final valid schedule (if found)
# - If no schedule possible → explain which constraint makes it impossible
#
# After finding (or failing to find) a schedule:
# - Print total assignments attempted
# - Print total backtracks needed
# - Verify the solution against all constraints
# - Suggest which constraint to relax if no solution found
# ============================================================