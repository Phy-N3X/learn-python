# ============================================================
# MODULE 04 | LECTURE 43 - pass
# ============================================================
# What you will learn:
# - What pass does (and doesn't do)
# - Why Python needs pass
# - pass in loops
# - pass in if/elif/else
# - pass in functions (preview)
# - pass in classes (preview)
# - pass vs continue vs break
# - Common use cases: placeholders, stubs, TODO markers
# - Real-world use cases
# - Common mistakes and edge cases
# ============================================================

# ------------------------------------------------------------
# PART 1: What is pass?
# ------------------------------------------------------------

# Python requires that every code block contains
# at least one statement.
# A block cannot be empty.
#
# But sometimes you WANT an empty block:
# - You're planning the structure but haven't written the code yet
# - A certain case should genuinely do nothing
# - You're writing a placeholder to be filled in later
# - You're creating a stub (skeleton) of a function or class
#
# pass is Python's "do nothing" statement.
# It is a valid statement that literally does nothing.
# It exists purely to satisfy Python's syntax requirement
# that blocks cannot be empty.
#
# Real life analogy:
# ┌─────────────────────────────────────────────────────┐
# │ Imagine a form with many fields.                    │
# │ You don't have data for some fields yet,            │
# │ so you write "N/A" or leave a blank line.           │
# │ The form is still valid - the field exists,         │
# │ it just has a placeholder value.                    │
# │                                                     │
# │ pass = "N/A" for code blocks                        │
# └─────────────────────────────────────────────────────┘
#
# pass:
# - Does absolutely nothing when executed
# - Produces no output
# - Changes no variables
# - Has no side effects
# - Simply allows Python to accept an otherwise empty block

# ------------------------------------------------------------
# PART 2: Why Python needs pass
# ------------------------------------------------------------

# Python uses INDENTATION to define blocks.
# Every block MUST have at least one statement.
# Without pass, empty blocks cause SyntaxError.

# ❌ SyntaxError - empty if block:
# x = 5
# if x > 0:
#          ← SyntaxError: expected an indented block

# ✅ Valid with pass:
x = 5
if x > 0:
    pass    # TODO: add logic here

# ❌ SyntaxError - empty for loop:
# for i in range(5):
#          ← SyntaxError: expected an indented block

# ✅ Valid with pass:
for i in range(5):
    pass    # loop does nothing (yet)

# ❌ SyntaxError - empty while:
# while True:
#          ← SyntaxError: expected an indented block

# ✅ Valid with pass:
# (Note: this would be an infinite loop that does nothing)
# while True:
#     pass

# ❌ SyntaxError - empty function:
# def my_function():
#          ← SyntaxError: expected an indented block

# ✅ Valid with pass:
def my_function():
    pass    # to be implemented later

# ❌ SyntaxError - empty class:
# class MyClass:
#          ← SyntaxError: expected an indented block

# ✅ Valid with pass:
class MyClass:
    pass    # to be implemented later

# ------------------------------------------------------------
# PART 3: pass in if/elif/else
# ------------------------------------------------------------

# Use pass when a particular condition should do nothing.

# Example 1: Handle only some cases

score = 75

if score >= 90:
    print("Excellent!")
elif score >= 70:
    print("Good job!")
elif score >= 60:
    pass    # deliberately do nothing for this range
else:
    print("Keep studying!")

# Example 2: Skip specific condition while developing

user_role = "viewer"

if user_role == "admin":
    print("Full access granted")
elif user_role == "editor":
    print("Edit access granted")
elif user_role == "viewer":
    pass    # TODO: implement viewer dashboard later
else:
    print("Unknown role")

# Example 3: Validate and do nothing if invalid

dna = "ATCGATCG"
valid_bases = "ATCG"

for base in dna:
    if base in valid_bases:
        pass    # valid base - no action needed here
    else:
        print(f"Invalid base: {base}")

# This is equivalent to:
for base in dna:
    if base not in valid_bases:
        print(f"Invalid base: {base}")
# (the second version is actually cleaner - pass not needed here)

# Example 4: Placeholder for future conditions

temperature = 25
humidity = 60

if temperature > 35 and humidity > 80:
    print("🔴 Dangerous heat index!")
elif temperature > 30 and humidity > 70:
    print("🟠 Very uncomfortable")
elif temperature > 25:
    pass    # TODO: add moderate heat warnings
else:
    print("🟢 Comfortable conditions")

# Example 5: Intentionally ignore specific errors
# (more common in try/except which we'll learn later)

data = ["42", "hello", "17", "world", "99"]
numbers = []

for item in data:
    try:
        num = int(item)
        numbers.append(num)
    except ValueError:
        pass    # silently skip non-numeric values

print(f"Numbers extracted: {numbers}")    # [42, 17, 99]

# ------------------------------------------------------------
# PART 4: pass in for loops
# ------------------------------------------------------------

# Using pass in loops - less common but valid.

# Example 1: Empty loop body (placeholder)

items = ["alpha", "beta", "gamma", "delta"]

# Loop structure defined, logic to be added later:
for item in items:
    pass    # TODO: process each item

# Example 2: Counting without processing

dna = "ATCGATCGATCG"
base_count = 0
for base in dna:
    base_count += 1
    pass    # no other processing needed - just counting

# (This is silly - len() would be better. Just illustrating pass.)

# Example 3: Structured loop with conditional pass

sequence = "ATCGATCGTT"
print("Scanning sequence:")
for i in range(len(sequence)):
    base = sequence[i]
    if base == "A":
        print(f"  Position {i}: Adenine (A)")
    elif base == "T":
        print(f"  Position {i}: Thymine (T)")
    elif base == "C":
        pass    # TODO: add Cytosine handling
    elif base == "G":
        pass    # TODO: add Guanine handling
    else:
        print(f"  Position {i}: Unknown base '{base}'")

# Example 4: Empty loop as intentional structure

# Sometimes used to "exhaust" an iterator:
# (consuming all items without doing anything with them)
# This is unusual but can be useful in specific contexts.

dummy_range = range(1000000)
for _ in dummy_range:
    pass    # consume the iterator (unusual use case)

# ------------------------------------------------------------
# PART 5: pass in while loops
# ------------------------------------------------------------

# Example 1: Structure placeholder

waiting = True
while waiting:
    pass    # TODO: implement waiting logic

# ⚠ The above is an INFINITE LOOP because 'waiting' never changes!
# Use carefully - usually pass in while is truly a placeholder.

# Example 2: Busy wait (spin loop) - professional use
# In real code, busy waiting burns CPU.
# Modern Python uses asyncio, threading, or time.sleep instead.
# But here's how it looks:

import time

# Simulated busy wait (only run for demonstration):
# start_time = time.time()
# while time.time() - start_time < 2:    # wait 2 seconds
#     pass    # do nothing, just wait

# Example 3: Conditional pass in while

count = 0
result = []

while count < 10:
    count += 1
    if count % 2 == 0:
        pass        # skip even numbers (do nothing)
    else:
        result.append(count)    # only odd numbers added

print(f"Odd numbers collected: {result}")
# [1, 3, 5, 7, 9]

# (continue would be more appropriate here, but pass works)

# ------------------------------------------------------------
# PART 6: pass as a stub in functions
# ------------------------------------------------------------

# One of the most COMMON real uses of pass:
# Writing function stubs when planning code structure.
# You define all functions first, implement them later.

# This is called "top-down development":
# 1. Design the overall structure
# 2. Write all function stubs with pass
# 3. Test that everything connects properly
# 4. Fill in the implementations one by one

def validate_dna(sequence):
    """Check if sequence contains only valid DNA bases."""
    pass    # TODO: implement validation

def calculate_gc_content(sequence):
    """Calculate GC content percentage."""
    pass    # TODO: implement GC calculation

def find_start_codons(sequence):
    """Find all ATG positions in sequence."""
    pass    # TODO: implement codon finder

def translate_sequence(sequence):
    """Translate DNA sequence to protein."""
    pass    # TODO: implement translation

def generate_report(sequence, analysis_results):
    """Generate analysis report."""
    pass    # TODO: implement reporting

# All functions exist and can be called - they just do nothing yet.
# You can write the main program flow first:

def analyze_dna(dna_sequence):
    """Main analysis pipeline."""
    # This structure works even before functions are implemented!
    is_valid = validate_dna(dna_sequence)
    gc = calculate_gc_content(dna_sequence)
    starts = find_start_codons(dna_sequence)
    protein = translate_sequence(dna_sequence)
    generate_report(dna_sequence, {"gc": gc, "starts": starts})

# Now implement them one by one:

def validate_dna(sequence):
    """Check if sequence contains only valid DNA bases."""
    if not sequence:
        return False
    for base in sequence:
        if base not in "ATCG":
            return False
    return True

def calculate_gc_content(sequence):
    """Calculate GC content percentage."""
    if not sequence:
        return 0.0
    gc = sum(1 for base in sequence if base in "GC")
    return gc / len(sequence) * 100

# Now these have real implementations!

# ------------------------------------------------------------
# PART 7: pass as a stub in classes (preview)
# ------------------------------------------------------------

# Classes (covered in a later module) use pass extensively
# for stub/placeholder development.

class DNASequence:
    """Represents a DNA sequence."""
    pass    # entire class is a stub

class ProteinAnalyzer:
    """Analyzes protein sequences."""

    def load_sequence(self, sequence):
        """Load a protein sequence."""
        pass    # TODO: implement

    def validate(self):
        """Validate the loaded sequence."""
        pass    # TODO: implement

    def calculate_properties(self):
        """Calculate physicochemical properties."""
        pass    # TODO: implement

    def generate_report(self):
        """Generate analysis report."""
        pass    # TODO: implement

# The class exists, can be instantiated, methods exist,
# nothing breaks - everything is just empty stubs.

analyzer = ProteinAnalyzer()
# analyzer.load_sequence("MKTAY")  # would work, returns None
# analyzer.validate()               # would work, returns None

# ------------------------------------------------------------
# PART 8: pass vs continue vs break - the critical comparison
# ------------------------------------------------------------

# These three look similar but do VERY different things.
# This is a common source of confusion for beginners.

# ┌──────────┬──────────────────────────────────────────────┐
# │ pass     │ Do nothing. Continue to next line in block.  │
# │ continue │ Skip rest of iteration. Go to NEXT iteration.│
# │ break    │ Exit the ENTIRE loop immediately.            │
# └──────────┴──────────────────────────────────────────────┘

numbers = [1, 2, 3, 4, 5]

# PASS - does nothing, loop proceeds normally:
print("With PASS:")
for n in numbers:
    if n == 3:
        pass        # does nothing - 3 still gets printed
    print(n, end=" ")
print()
# Output: 1 2 3 4 5  ← all numbers including 3

# CONTINUE - skips the rest of iteration:
print("With CONTINUE:")
for n in numbers:
    if n == 3:
        continue    # skip to next iteration - 3 not printed
    print(n, end=" ")
print()
# Output: 1 2 4 5  ← 3 is skipped

# BREAK - exits the loop:
print("With BREAK:")
for n in numbers:
    if n == 3:
        break       # exit the loop entirely
    print(n, end=" ")
print()
# Output: 1 2  ← stops before 3

# Detailed trace:
print("\nDetailed trace with n=3:")

print("PASS:")
for n in [1, 2, 3, 4, 5]:
    print(f"  Start of iteration: n={n}")
    if n == 3:
        print(f"  pass executed - nothing happens")
        pass
    print(f"  End of iteration: n={n} (still here!)")
print("  Loop finished normally")

print("\nCONTINUE:")
for n in [1, 2, 3, 4, 5]:
    print(f"  Start of iteration: n={n}")
    if n == 3:
        print(f"  continue - skipping rest of n=3 iteration")
        continue
    print(f"  End of iteration: n={n}")
print("  Loop finished normally")

print("\nBREAK:")
for n in [1, 2, 3, 4, 5]:
    print(f"  Start of iteration: n={n}")
    if n == 3:
        print(f"  break - exiting loop entirely!")
        break
    print(f"  End of iteration: n={n}")
print("  After loop (break jumped here)")

# Key insight:
# pass: "there's nothing to do in this branch, carry on"
# continue: "skip this iteration, go to the next one"
# break: "we're done with this loop entirely"

# ------------------------------------------------------------
# PART 9: pass for intentional no-ops
# ------------------------------------------------------------

# Sometimes you GENUINELY want a condition to do nothing.
# pass makes this explicit and intentional.

# Example 1: Event handler stub

def handle_event(event_type):
    if event_type == "click":
        print("Processing click...")
    elif event_type == "hover":
        pass    # hover events intentionally ignored
    elif event_type == "scroll":
        print("Processing scroll...")
    elif event_type == "keypress":
        pass    # keypress events intentionally ignored
    else:
        print(f"Unknown event: {event_type}")

# The pass makes it CLEAR that hover/keypress are
# intentionally not handled, not accidentally forgotten.

# Example 2: Exception handling (silent errors)

def safe_int(value):
    """Convert to int, return None on failure."""
    try:
        return int(value)
    except (ValueError, TypeError):
        pass    # intentionally do nothing - return None implicitly
    return None

print(safe_int("42"))        # 42
print(safe_int("hello"))     # None (ValueError caught, passed)
print(safe_int(None))        # None (TypeError caught, passed)

# Example 3: Base class method (overriding pattern)

class Animal:
    def speak(self):
        pass    # base class has no sound - subclasses override

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Fish(Animal):
    def speak(self):
        pass    # fish don't speak - intentional no-op!

dog = Dog()
cat = Cat()
fish = Fish()

dog.speak()     # Woof!
cat.speak()     # Meow!
fish.speak()    # (nothing - intentionally silent)

# ------------------------------------------------------------
# PART 10: Using pass with TODO comments
# ------------------------------------------------------------

# Best practice: always pair pass with a comment.
# pass alone doesn't explain WHY it's there.
# A TODO comment turns pass into self-documenting code.

# ❌ Bad - no explanation:
def process_data(data):
    pass

# ✅ Good - explains intent:
def process_data(data):
    pass    # TODO: implement data processing pipeline

# ✅ Even better - detailed TODO:
def process_data(data):
    # TODO: implement the following steps:
    # 1. Validate input data format
    # 2. Clean and normalize values
    # 3. Apply statistical transformations
    # 4. Return processed DataFrame
    pass

# Common TODO comment styles:
# pass    # TODO: implement
# pass    # FIXME: not working correctly
# pass    # HACK: temporary workaround
# pass    # NOTE: intentional no-op for base class
# pass    # PLACEHOLDER: will be replaced in production

# Example: Full stub with documentation

class BioinformaticsAnalyzer:
    """
    Main analyzer class for biological sequence data.
    TODO: Complete all method implementations.
    """

    def __init__(self):
        # TODO: initialize required attributes
        pass

    def load_fasta(self, filepath):
        """
        Load sequences from a FASTA file.
        TODO: Implement FASTA parser
        """
        pass

    def align_sequences(self, seq1, seq2):
        """
        Perform pairwise sequence alignment.
        TODO: Implement Smith-Waterman or Needleman-Wunsch
        """
        pass

    def predict_structure(self, sequence):
        """
        Predict secondary structure.
        TODO: Implement structure prediction algorithm
        """
        pass

    def export_results(self, output_path):
        """
        Export analysis results to file.
        TODO: Implement export in multiple formats (CSV, JSON, TSV)
        """
        pass

# ------------------------------------------------------------
# PART 11: pass in exception handling (try/except)
# ------------------------------------------------------------

# One of the most practical uses of pass:
# silently ignoring specific exceptions.
# We'll cover exceptions in detail in a later module.

# Example 1: Ignore specific errors

values = ["10", "abc", "25", None, "30", "xyz"]
total = 0

for val in values:
    try:
        num = int(val)
        total += num
    except (ValueError, TypeError):
        pass    # silently ignore non-convertible values

print(f"Sum of valid values: {total}")    # 65

# Example 2: Try multiple approaches

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        pass    # fall through to return default
    return 0    # default when division fails

print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # 0

# Example 3: File operations with pass

def read_file_safe(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        pass    # file doesn't exist - return None
    except PermissionError:
        pass    # no permission - return None
    return None

content = read_file_safe("nonexistent.txt")
if content is None:
    print("File could not be read")

# ------------------------------------------------------------
# PART 12: pass in type checking patterns
# ------------------------------------------------------------

# pass is useful when checking types and only certain
# types need processing.

mixed_data = [42, "hello", 3.14, True, [1, 2, 3],
              "world", 100, None, "Python", 2.71]

strings_found = []
integers_found = []

for item in mixed_data:
    if isinstance(item, bool):
        pass    # ignore booleans (bool is subclass of int in Python!)
    elif isinstance(item, int):
        integers_found.append(item)
    elif isinstance(item, str):
        strings_found.append(item)
    elif isinstance(item, float):
        pass    # intentionally ignoring floats
    else:
        pass    # ignore everything else

print(f"Integers: {integers_found}")    # [42, 100]
print(f"Strings: {strings_found}")      # ['hello', 'world', 'Python']

# Note: True is skipped because bool is a subclass of int,
# and we check for bool FIRST (before int) to exclude it.

# ------------------------------------------------------------
# PART 13: Common mistakes
# ------------------------------------------------------------

# ❌ MISTAKE 1: Confusing pass with continue

numbers = [1, 2, 3, 4, 5]

# Wrong: thinking pass skips to next iteration
print("WRONG - pass doesn't skip:")
for n in numbers:
    if n == 3:
        pass        # does NOT skip - 3 is still printed!
    print(n, end=" ")
print()
# Output: 1 2 3 4 5  ← 3 is still there!

# ✅ Use continue to actually skip:
print("CORRECT - continue skips:")
for n in numbers:
    if n == 3:
        continue    # actually skips 3
    print(n, end=" ")
print()
# Output: 1 2 4 5

# ❌ MISTAKE 2: Forgetting pass causes SyntaxError

# if condition:
#          ← SyntaxError! block is empty

# ✅ Always add pass or at least a comment (but comment alone isn't enough!)
# if condition:
#     # comment alone doesn't work either!  ← still SyntaxError!

# Only pass (or actual code) fills the block:
condition = True
if condition:
    pass    # ← this works

# ❌ MISTAKE 3: Using pass where none is needed

for i in range(5):
    print(i)
    pass        # ← pointless! loop continues anyway after print

# ✅ Just remove it:
for i in range(5):
    print(i)

# ❌ MISTAKE 4: Thinking pass returns something

def get_value():
    pass

result = get_value()
print(result)          # None - pass causes function to return None
print(type(result))    # <class 'NoneType'>

# pass doesn't return a value - but Python functions implicitly
# return None when no return statement is present.
# This is sometimes useful, sometimes a bug.

# ❌ MISTAKE 5: Using pass to "delete" an else branch

x = 5
# This still evaluates both branches:
if x > 0:
    print("positive")
else:
    pass    # ← this is fine and valid, but slightly wasteful

# ✅ Just remove the else entirely:
if x > 0:
    print("positive")
# (no else needed if you're doing nothing)

# ❌ MISTAKE 6: Leaving pass stubs in production code

# pass is for DEVELOPMENT, not production!
# Always replace pass stubs before shipping code.

def calculate_price(base_price, discount):
    pass    # ← this should NEVER be in production!

# ✅ Always implement before finalizing:
def calculate_price(base_price, discount):
    return base_price * (1 - discount)

# ❌ MISTAKE 7: Using pass to suppress all exceptions blindly

# ⚠ This is dangerous - hides all errors!
# try:
#     risky_operation()
# except Exception:
#     pass    # ← swallows ALL exceptions, even unexpected ones!

# ✅ Only suppress specific, expected exceptions:
try:
    int("hello")
except ValueError:
    pass    # only catches ValueError, lets others propagate

# ------------------------------------------------------------
# PART 14: Real-world use cases
# ------------------------------------------------------------

# Use case 1: Building a lab workflow skeleton

print("=== Lab Workflow System ===")

class LabWorkflow:
    """Automated laboratory workflow manager."""

    def initialize_instruments(self):
        # TODO: Connect to instruments via UART/USB
        # TODO: Run self-diagnostic checks
        # TODO: Load calibration data
        pass

    def load_samples(self, sample_list):
        # TODO: Validate sample IDs against LIMS
        # TODO: Check tube barcodes
        # TODO: Record sample positions
        pass

    def run_quality_control(self):
        # TODO: Prepare QC standards
        # TODO: Run QC samples first
        # TODO: Evaluate QC results before proceeding
        pass

    def perform_analysis(self, method):
        # TODO: Select correct analysis protocol
        # TODO: Process all samples
        # TODO: Handle instrument errors gracefully
        pass

    def export_results(self, format="csv"):
        # TODO: Collect results from all instruments
        # TODO: Apply unit conversions
        # TODO: Generate report in requested format
        pass

    def cleanup(self):
        # TODO: Wash needles and probes
        # TODO: Return samples to storage
        # TODO: Disconnect from instruments
        pass

# The workflow can be structured and connected now,
# even before any implementation exists:
workflow = LabWorkflow()
# workflow.initialize_instruments()
# workflow.load_samples(["S001", "S002", "S003"])
# workflow.run_quality_control()
# workflow.perform_analysis(method="HPLC")
# workflow.export_results(format="pdf")
# workflow.cleanup()

print("LabWorkflow class created successfully (stubs)")

# Use case 2: Configuration system with intentional no-ops

print("\n=== Configuration Handler ===")

def apply_config(config):
    """Apply configuration settings."""

    # Process logging settings
    log_level = config.get("log_level", "INFO")
    if log_level == "DEBUG":
        print("  Debug logging enabled")
    elif log_level == "INFO":
        print("  Info logging enabled")
    elif log_level == "WARNING":
        pass    # warning is default - no change needed
    elif log_level == "ERROR":
        print("  Error-only logging")
    elif log_level == "SILENT":
        pass    # no logging - intentional no-op

    # Process database settings
    db_type = config.get("db_type", "sqlite")
    if db_type == "sqlite":
        print("  Using SQLite (default)")
    elif db_type == "postgres":
        print("  Configuring PostgreSQL...")
    elif db_type == "mysql":
        print("  Configuring MySQL...")
    elif db_type == "mongodb":
        pass    # TODO: implement MongoDB support
    else:
        print(f"  Unknown database type: {db_type}")

configs_to_test = [
    {"log_level": "DEBUG", "db_type": "sqlite"},
    {"log_level": "WARNING", "db_type": "postgres"},
    {"log_level": "SILENT", "db_type": "mongodb"},
]

for cfg in configs_to_test:
    print(f"\nApplying config: {cfg}")
    apply_config(cfg)

# Use case 3: Protocol parser with selective processing

print("\n=== Lab Protocol Parser ===")

protocol_steps = [
    {"step": 1, "action": "centrifuge", "duration": 300, "rpm": 3000},
    {"step": 2, "action": "pipette", "volume": 50, "from": "sample", "to": "plate"},
    {"step": 3, "action": "incubate", "duration": 1800, "temp": 37},
    {"step": 4, "action": "wash", "cycles": 3},
    {"step": 5, "action": "read", "wavelength": 450},
    {"step": 6, "action": "comment", "text": "Check plate appearance"},
    {"step": 7, "action": "pause", "reason": "Manual inspection required"},
]

executable_steps = []
skipped_steps = []

for step in protocol_steps:
    action = step["action"]

    if action == "comment":
        pass        # comments are metadata only, not executable
    elif action == "pause":
        pass        # pauses handled separately by operator
    elif action in ("centrifuge", "pipette", "incubate", "wash", "read"):
        executable_steps.append(step)
        print(f"  Step {step['step']}: {action} - queued for execution")
    else:
        print(f"  Step {step['step']}: {action} - UNKNOWN ACTION")

print(f"\nExecutable steps: {len(executable_steps)}")
print(f"Skipped (comment/pause): "
      f"{len(protocol_steps) - len(executable_steps)}")

# Use case 4: Multi-format data reader

print("\n=== Multi-Format Data Reader ===")

def read_data(filename, file_format):
    """Read data from file in various formats."""

    data = None

    if file_format == "csv":
        # TODO: implement CSV reading with pandas or csv module
        print(f"  Reading CSV: {filename}")
        pass

    elif file_format == "json":
        # TODO: implement JSON reading with json module
        print(f"  Reading JSON: {filename}")
        pass

    elif file_format == "fasta":
        # TODO: implement FASTA parser
        print(f"  Reading FASTA: {filename}")
        pass

    elif file_format == "fastq":
        # TODO: implement FASTQ parser (FASTA + quality scores)
        print(f"  Reading FASTQ: {filename}")
        pass

    elif file_format == "vcf":
        # TODO: implement VCF (Variant Call Format) parser
        print(f"  Reading VCF: {filename}")
        pass

    elif file_format == "bed":
        # TODO: implement BED format parser
        print(f"  Reading BED: {filename}")
        pass

    else:
        print(f"  Unsupported format: {file_format}")
        return None

    return data    # None for now (stubs), real data when implemented

# Test the stub system:
test_files = [
    ("sequences.fasta", "fasta"),
    ("variants.vcf", "vcf"),
    ("expression.csv", "csv"),
    ("annotations.bed", "bed"),
    ("data.xyz", "xyz"),
]

for filename, fmt in test_files:
    result = read_data(filename, fmt)
    status = "returned data" if result is not None else "stub (returns None)"
    print(f"    → {status}")

# ------------------------------------------------------------
# SUMMARY
# ------------------------------------------------------------

# ✅ pass does NOTHING - it's a no-op statement
# ✅ Required when Python needs a block but you want it empty
# ✅ Used for: empty blocks, stubs, placeholders, intentional no-ops
# ✅ Always pair with a TODO comment explaining WHY
# ✅ pass ≠ continue ≠ break:
#    pass     → do nothing, continue normally
#    continue → skip to next loop iteration
#    break    → exit the loop entirely
# ✅ Common in: if/elif/else, loops, functions, classes, try/except
# ✅ Functions with only pass return None implicitly
# ✅ Remove all pass stubs before production deployment
# ✅ pass is a development tool, not a feature

# Quick reference:
# ┌──────────────────────────────────────────────────────────┐
# │ if condition:                                            │
# │     pass    ← empty block (does nothing)                │
# │                                                          │
# │ for i in range(10):                                      │
# │     pass    ← empty loop body                           │
# │                                                          │
# │ def function():                                          │
# │     pass    ← stub function (returns None)              │
# │                                                          │
# │ class MyClass:                                           │
# │     pass    ← stub class                                │
# │                                                          │
# │ pass vs continue vs break:                               │
# │   pass:     next line in current block (nothing skipped) │
# │   continue: next ITERATION (rest of current skipped)    │
# │   break:    exit ENTIRE loop                            │
# └──────────────────────────────────────────────────────────┘