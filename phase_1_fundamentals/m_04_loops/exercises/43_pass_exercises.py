# ============================================================
# MODULE 04 | EXERCISES 43 - pass
# ============================================================
# 15 exercises from easiest to hardest
# ============================================================

# ------------------------------------------------------------
# EXERCISE 1 ⬜ | EASY
# ------------------------------------------------------------
# Predict the output BEFORE running each code block.
# Write your prediction as a comment.
# Then run and verify.
#
# # Block A:
# for i in range(5):
#     if i == 2:
#         pass
#     print(i, end=" ")
# print()
# # prediction: ?
#
# # Block B:
# for i in range(5):
#     if i == 2:
#         continue
#     print(i, end=" ")
# print()
# # prediction: ?
#
# # Block C:
# for i in range(5):
#     if i == 2:
#         break
#     print(i, end=" ")
# print()
# # prediction: ?
#
# # Block D:
# x = 10
# if x > 5:
#     pass
# print("After if:", x)
# # prediction: ?
#
# # Block E:
# def mystery():
#     pass
# result = mystery()
# print(result)
# print(type(result))
# # prediction: ?
#
# Final question (answer as comment):
# Why are Block A and Block B different even though
# both have 'if i == 2'?
# What does pass return when used in a function?

# ------------------------------------------------------------
# EXERCISE 2 ⬜ | EASY
# ------------------------------------------------------------
# Fill in the blanks: replace each ??? with either
# pass, continue, or break - whichever makes the output correct.
# Explain your choice as a comment.
#
# # Blank 1: Output should be: 0 1 2 3 4 (all numbers)
# for i in range(5):
#     if i == 3:
#         ???   # choice: ? because ?
#     print(i, end=" ")
# print()
#
# # Blank 2: Output should be: 0 1 2 4 (skip 3)
# for i in range(5):
#     if i == 3:
#         ???   # choice: ? because ?
#     print(i, end=" ")
# print()
#
# # Blank 3: Output should be: 0 1 2 (stop at 3)
# for i in range(5):
#     if i == 3:
#         ???   # choice: ? because ?
#     print(i, end=" ")
# print()
#
# # Blank 4: Function exists but does nothing
# def placeholder():
#     ???
#
# # Blank 5: Loop body is empty for now
# items = ["a", "b", "c"]
# for item in items:
#     ???

# ------------------------------------------------------------
# EXERCISE 3 ⬜ | EASY
# ------------------------------------------------------------
# Find ALL errors in the code below.
# Write what each error is as a comment.
# Then fix all errors so the code runs correctly.
#
# # Error 1:
# if True:
#
# # Error 2:
# for i in range(5):
#     # TODO: add logic later
#
# # Error 3:
# def my_function():
#
# # Error 4:
# for i in range(5):
#     if i == 3:
#         pass
#         print(f"This should print when i=3: {i}")
#
# # Error 5 - logical error, not syntax:
# numbers = [1, 2, 3, 4, 5]
# for n in numbers:
#     if n % 2 == 0:
#         pass    # intended to skip even numbers
#     print(n)   # but this still prints everything!

# ------------------------------------------------------------
# EXERCISE 4 ⬜ | EASY
# ------------------------------------------------------------
# Use pass to write a complete "skeleton" program
# for a student grade management system.
# Don't implement any logic yet - only write the structure.
#
# Create these functions with pass and a descriptive comment:
# 1. add_student(name, student_id) - adds a new student
# 2. remove_student(student_id) - removes a student
# 3. add_grade(student_id, subject, grade) - records a grade
# 4. get_average(student_id) - calculates student average
# 5. get_class_average() - calculates class average
# 6. get_top_student() - finds student with highest average
# 7. get_failing_students(threshold) - finds students below threshold
# 8. generate_report(output_format) - generates a report
# 9. export_data(filename) - saves data to file
# 10. import_data(filename) - loads data from file
#
# Then write a main program that calls all functions
# (they'll return None since they're stubs - that's fine).
# Verify that the program runs without errors.

# ------------------------------------------------------------
# EXERCISE 5 ⬜ | EASY
# ------------------------------------------------------------
# Create a lab instrument control system skeleton using pass.
# The system controls different types of lab instruments.
#
# Write stub functions for each instrument type:
#
# Centrifuge:
# - set_speed(rpm)
# - set_duration(seconds)
# - set_temperature(celsius)
# - start()
# - stop()
# - get_status()
#
# PCR Machine:
# - load_program(program_name)
# - set_cycles(count)
# - start_run()
# - pause_run()
# - get_progress()
# - export_results()
#
# Spectrophotometer:
# - set_wavelength(nm)
# - blank_calibration()
# - measure_sample(sample_id)
# - scan_spectrum(start_nm, end_nm, step_nm)
# - export_spectrum()
#
# All functions should use pass with a meaningful TODO comment.
# After defining all stubs, call each function once to verify
# no errors occur (even though they return None).

# ------------------------------------------------------------
# EXERCISE 6 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Write a number classifier using if/elif/else with pass.
# Some categories should use pass (intentionally do nothing).
#
# For each number from 1 to 20:
# - If divisible by both 3 and 5: print "FizzBuzz"
# - If divisible by 3 only: print "Fizz"
# - If divisible by 5 only: print "Buzz"
# - If the number is 13: pass (skip 13 - it's unlucky!)
# - If prime and not covered above: print "Prime: N"
# - Otherwise: pass (don't print regular composite numbers)
#
# Use pass in the appropriate places.
# The key: some numbers should produce no output at all.
#
# After the loop, print a count of:
# - How many numbers were "FizzBuzz"
# - How many were "Fizz"
# - How many were "Buzz"
# - How many were primes
# - How many were silently skipped (pass was the outcome)

# ------------------------------------------------------------
# EXERCISE 7 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Create a DNA sequence event handler using pass.
# Process each base in a sequence and respond to "events".
#
# dna = "ATGCGATACGCTTAAGGCCCCTAAATCG"
#
# Event types and responses:
# - Base 'A': count it (just increment counter, no print)
# - Base 'T': pass (thymine events are ignored in this system)
# - Base 'C': count it
# - Base 'G': print "G-event at position X" AND count it
# - Every 3rd position (codon boundary): print codon formed
# - Any other character: print warning
#
# After processing:
# - Print A count, C count, G count
# - Print "T events ignored: X" (where X is count of T's)
# - Print all codon boundaries found
# - Print total positions processed
#
# Use pass where specified (for T events).
# Notice how pass makes it clear T is deliberately skipped.

# ------------------------------------------------------------
# EXERCISE 8 ⬜ | EASY-MEDIUM
# ------------------------------------------------------------
# Build a configuration parser using pass for
# unsupported settings.
#
# config_lines = [
#     "debug = true",
#     "log_level = INFO",
#     "database = mysql",
#     "cache = redis",        # not yet supported
#     "queue = rabbitmq",     # not yet supported
#     "port = 8080",
#     "host = localhost",
#     "theme = dark",         # not yet supported
#     "language = en",
#     "timezone = UTC",
# ]
#
# Supported settings: debug, log_level, port, host, language, timezone
# Unsupported (use pass): cache, queue, theme, database
# Unknown settings: print warning
#
# For each config line:
# 1. Parse key and value (split by '=')
# 2. If unsupported → pass (skip silently with counter tracking)
# 3. If supported → print "Applied: key = value"
# 4. If unknown → print warning
#
# After processing:
# - Print all applied settings
# - Print count of unsupported (silently skipped)
# - Print count of unknown settings
#
# Use pass for unsupported settings to make it CLEAR
# they are intentionally not processed.

# ------------------------------------------------------------
# EXERCISE 9 ⬜ | MEDIUM
# ------------------------------------------------------------
# Trace through this code involving pass and predict outputs.
# Write predictions as comments before each print.
# Then run and verify.
#
# # Block A:
# def process(value):
#     if value > 0:
#         return value * 2
#     elif value == 0:
#         pass
#     else:
#         return -value
#
# # predictions:
# print(process(5))    # ?
# print(process(0))    # ?
# print(process(-3))   # ?
#
# # Block B:
# results = []
# for i in range(10):
#     if i % 3 == 0:
#         pass
#     elif i % 2 == 0:
#         results.append(i)
#     else:
#         pass
# # prediction: results = ?
# print(results)
#
# # Block C:
# class Counter:
#     def __init__(self):
#         self.count = 0
#
#     def increment(self):
#         self.count += 1
#
#     def decrement(self):
#         pass    # TODO: implement
#
#     def reset(self):
#         pass    # TODO: implement
#
# c = Counter()
# c.increment()
# c.increment()
# c.increment()
# c.decrement()    # does nothing
# c.reset()        # does nothing
# # prediction: c.count = ?
# print(c.count)
#
# Answer as comments:
# Why does process(0) return None?
# In Block B, why aren't multiples of 3 in results?
# What happens to c.count after decrement() which has pass?

# ------------------------------------------------------------
# EXERCISE 10 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a protocol execution engine with intentional
# no-ops using pass.
#
# In laboratory automation, some protocol steps are
# "documentation only" and don't require machine action.
#
# protocol = [
#     ("action",  "centrifuge", {"speed": 3000, "time": 300}),
#     ("note",    "Check pellet visibility", {}),
#     ("action",  "aspirate", {"volume": 200, "source": "tube1"}),
#     ("warning", "Samples are light-sensitive from here", {}),
#     ("action",  "dispense", {"volume": 200, "dest": "plate"}),
#     ("note",    "Allow 5 min equilibration", {}),
#     ("action",  "incubate", {"temp": 37, "time": 600}),
#     ("warning", "Do not open incubator during run", {}),
#     ("action",  "read_absorbance", {"wavelength": 450}),
#     ("note",    "Protocol complete", {}),
# ]
#
# Processing rules:
# - "action" steps: print "EXECUTING: step_name with params"
#   and add to execution_log
# - "note" steps: pass (notes are human-readable only,
#   not executed by the machine) BUT count them
# - "warning" steps: print "⚠ WARNING: message" BUT
#   don't add to execution_log
#
# After processing all steps:
# - Print execution log (only action steps)
# - Print count of notes (that used pass)
# - Print count of warnings
# - Print total steps processed
# - Calculate "automation coverage" = actions / total steps × 100%

# ------------------------------------------------------------
# EXERCISE 11 ⬜ | MEDIUM
# ------------------------------------------------------------
# Build a bioinformatics pipeline skeleton using pass.
# This represents a real RNA-seq analysis pipeline.
#
# Create stub functions for a complete RNA-seq workflow:
#
# Phase 1 - Quality Control:
# def check_read_quality(fastq_file): pass
# def trim_adapters(fastq_file, adapter_seq): pass
# def filter_low_quality(fastq_file, min_quality): pass
#
# Phase 2 - Alignment:
# def build_reference_index(genome_file): pass
# def align_reads(reads_file, index_path): pass
# def sort_bam(bam_file): pass
# def index_bam(bam_file): pass
#
# Phase 3 - Quantification:
# def count_features(bam_file, annotation_file): pass
# def normalize_counts(count_matrix): pass
# def calculate_tpm(count_matrix, gene_lengths): pass
#
# Phase 4 - Differential Expression:
# def fit_model(count_matrix, conditions): pass
# def calculate_pvalues(model): pass
# def apply_multiple_testing_correction(pvalues): pass
# def identify_de_genes(results, threshold): pass
#
# Phase 5 - Visualization and Reporting:
# def plot_pca(count_matrix): pass
# def plot_heatmap(de_genes): pass
# def plot_volcano(results): pass
# def generate_html_report(all_results): pass
#
# After writing all stubs:
# 1. Write a main() function that calls all stubs in order
# 2. Print which phase each function belongs to
# 3. Count total functions per phase
# 4. Verify everything runs without errors
# 5. Then implement ONE function fully (your choice)
#    and verify it works alongside the stubs

# ------------------------------------------------------------
# EXERCISE 12 ⬜ | MEDIUM
# ------------------------------------------------------------
# Create a data type router using pass for unsupported types.
#
# Write a function process_value(value) that handles
# different data types differently.
#
# Handling rules:
# - int: if positive → double it; if negative → absolute value; if 0 → pass
# - float: round to 2 decimal places
# - str: if longer than 10 chars → truncate with "..."; else → uppercase
# - list: if empty → pass; else → sort and return
# - tuple: convert to list, sort, convert back to tuple
# - bool: pass (intentionally not processed)
# - None: pass (intentionally not processed)
# - dict: if has "value" key → process that key's value recursively
# - set: convert to sorted list
# - any other type: pass (return None)
#
# Test with these values:
# test_values = [
#     42, -7, 0, 3.14159, "Hello World",
#     "Hi", [3, 1, 4, 1, 5], [], (5, 3, 1, 4),
#     True, None, {"value": 99}, {"name": "test"},
#     {3, 1, 4, 1, 5}, 2+3j  # complex number
# ]
#
# For each value, print:
# Original: [value] ([type]) → Result: [result]
# Mark values where pass was used: "→ [SKIPPED - intentional no-op]"
#
# Count and print at the end:
# - How many values were processed
# - How many were intentionally skipped (pass)
# - What types were skipped

# ------------------------------------------------------------
# EXERCISE 13 ⬜ | MEDIUM-HARD
# ------------------------------------------------------------
# Design and implement a game engine skeleton using pass.
# The game: Simple text-based "Lab Escape" puzzle game.
#
# Using pass for ALL unimplemented parts, create:
#
# Game State Management:
# class GameState:
#     def __init__(self): ...
#     def save(self, filename): pass
#     def load(self, filename): pass
#     def reset(self): pass
#
# Room System:
# class Room:
#     def __init__(self, name, description): ...
#     def add_item(self, item): pass
#     def remove_item(self, item): pass
#     def add_exit(self, direction, room): pass
#     def describe(self): pass
#
# Player System:
# class Player:
#     def __init__(self, name): ...
#     def move(self, direction): pass
#     def pick_up(self, item): pass
#     def use_item(self, item, target): pass
#     def check_inventory(self): pass
#
# Puzzle System:
# class Puzzle:
#     def __init__(self, description, solution): ...
#     def attempt(self, answer): pass
#     def give_hint(self): pass
#     def is_solved(self): pass
#
# Game Engine:
# class GameEngine:
#     def __init__(self): ...
#     def setup_world(self): pass
#     def process_command(self, command): pass
#     def check_win_condition(self): pass
#     def run(self): pass
#
# Requirements:
# 1. All classes and methods created with pass stubs
# 2. Write a setup_world() IMPLEMENTATION that creates
#    at least 3 rooms, 2 puzzles, and 3 items
# 3. Implement process_command() to handle: go, take, use,
#    look, inventory, solve, hint, quit
# 4. Implement check_win_condition() - player must have
#    collected "key_card" and solved all puzzles
# 5. Implement run() as the main game loop
# 6. All other methods can remain as pass stubs
#
# Demonstrate that the game can start, the player can
# move between rooms, and the win condition can be checked.

# ------------------------------------------------------------
# EXERCISE 14 ⬜ | HARD
# ------------------------------------------------------------
# Build a comprehensive bioinformatics class hierarchy
# using pass for the skeleton and implementing key methods.
#
# Create this inheritance hierarchy:
#
# BiologicalSequence (base class)
# ├── NucleotideSequence
# │   ├── DNASequence
# │   └── RNASequence
# └── ProteinSequence
#
# BiologicalSequence methods (implement these):
# - __init__(self, sequence, name="unnamed")
# - __len__(self): return sequence length
# - __str__(self): return formatted string
# - validate(self): pass (to be overridden)
# - get_composition(self): pass (to be overridden)
# - calculate_molecular_weight(self): pass
# - to_fasta(self): return FASTA format string
#
# NucleotideSequence methods:
# - validate(self): check only valid nucleotides
# - get_composition(self): count each nucleotide
# - reverse_complement(self): pass (to be overridden)
# - find_motif(self, motif): find all positions of motif
# - gc_content(self): calculate GC%
#
# DNASequence methods:
# - validate(self): only ATCG allowed
# - reverse_complement(self): implement A↔T, C↔G + reverse
# - transcribe(self): convert to RNA (T→U)
# - translate(self): pass (complex - stub only)
# - find_orfs(self): pass (complex - stub only)
#
# RNASequence methods:
# - validate(self): only AUCG allowed
# - reverse_complement(self): implement A↔U, C↔G + reverse
# - back_transcribe(self): convert to DNA (U→T)
# - translate(self): pass (complex - stub only)
#
# ProteinSequence methods:
# - validate(self): only standard 20 amino acid codes
# - get_composition(self): count each amino acid
# - calculate_molecular_weight(self): implement (each aa ~110Da)
# - predict_charge(self, pH): pass (complex - stub only)
# - find_domains(self): pass (complex - stub only)
#
# After creating the hierarchy:
# 1. Create instances of each concrete class
# 2. Call all implemented methods and show output
# 3. Verify pass stubs return None without errors
# 4. Show polymorphism: loop through a list of mixed
#    sequence types, call validate() on each

# ------------------------------------------------------------
# EXERCISE 15 ⬜ | HARD
# ------------------------------------------------------------
# Create a complete laboratory information management system
# (LIMS) skeleton with strategic use of pass.
#
# The system manages samples, experiments, results, and reports.
# Use pass for ALL complex implementations,
# but implement the core data management layer.
#
# Core data structures (implement fully):
# - Sample registry (dictionary: id → sample data)
# - Experiment log (list of experiment records)
# - Results database (nested dict: experiment → results)
# - User registry (dictionary: username → permissions)
#
# Implement these functions FULLY (no pass):
# def register_sample(sample_id, sample_type, source, date):
#     # Add to registry, validate inputs, return success/failure
#
# def log_experiment(exp_id, sample_ids, protocol, operator):
#     # Validate all samples exist, log experiment
#
# def store_result(exp_id, measurement_type, value, unit):
#     # Validate experiment exists, store result
#
# def get_sample_history(sample_id):
#     # Return all experiments for this sample
#
# Implement as STUBS with pass (complex analysis):
# def calculate_statistics(exp_id): pass
# def generate_qc_report(exp_id): pass
# def compare_experiments(exp_id_1, exp_id_2): pass
# def export_to_excel(exp_ids, filename): pass
# def backup_database(filepath): pass
# def restore_database(filepath): pass
# def audit_trail(start_date, end_date): pass
# def alert_on_anomaly(threshold): pass
#
# Implement the main interactive loop:
# - Menu-driven interface
# - Register at least 5 samples
# - Log at least 3 experiments
# - Store results for each experiment
# - Query sample history
# - Show which functions are implemented vs stubs
# - Print system statistics
#
# Use pass strategically where noted,
# and make it clear in comments WHY each pass is there.
# ============================================================